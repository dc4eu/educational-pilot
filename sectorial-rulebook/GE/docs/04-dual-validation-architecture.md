# 04 — Dual validation architecture: JSON Schema + SHACL

## 4.1 Motivation

A learning credential that crosses a border, a sector or a generation must survive two independent questions:

1. Is it **syntactically well-formed**? Does it have all mandatory fields, the correct types, the expected formats?
2. Is it **semantically coherent**? Do the declared values belong to authoritative vocabularies? Do the relationships between fields satisfy business rules of the educational domain (for example, ECTS coherent with EQF, national framework coherent with the issuing Member State)?

Both questions are necessary. A JSON can be syntactically valid and semantically incoherent (for example, declaring 360 ECTS for an EQF level 4). And a semantically rich model can be ambiguous in its serialisation structure if not syntactically delimited.

The **dual validation architecture** resolves this duality by running the two validations in parallel over the same credential, employing for each the most appropriate technology: **JSON Schema** for the syntactic layer and **SHACL** for the semantic layer over the RDF graph.

W3C-VCDM, by being defined over **JSON-LD 1.1**, natively exposes an RDF graph that is processable by SHACL without the need for an intermediate transformation. This property is what turns dual validation into an operational practice, not a theoretical promise.

## 4.2 Two validations for two questions

### 4.2.1 JSON Schema (syntactic layer)

**Responsibilities**:

- Presence of mandatory fields (`@context`, `type`, `issuer`, `credentialSubject`, `credentialStatus`, etc.).
- Primitive types (string, integer, ISO 8601 date-time, boolean).
- Formats (IRI, UUID, `xsd:dateTime`).
- Minimum and maximum cardinalities on structural fields.
- Enumerated values for technical identifiers (for example, `type` with `"VerifiableCredential"`).

**Reference technology**: JSON Schema Draft 2020-12.

**Output**: binary structural conformity (valid / invalid) with error messages locatable by JSON Pointer.

### 4.2.2 SHACL (semantic layer)

**Responsibilities**:

- Validation of the RDF graph resulting from expanding the JSON-LD.
- Constraints on the content of authoritative vocabularies: EQF 1–8, ISCED-F levels, ESCO codes, national frameworks registered in ELI.
- Cross-field relationships: for example, if `creditPoints.framework = "http://data.europa.eu/snb/credit/25831c2"` (ECTS), then the EQF level must be coherent with the admissible range and `creditPoints.point` must respect a multiple of 0.5 within an admissible threshold.
- Conformity of the issuing entity with the accreditation profile: for example, an issuer of higher-education microcredentials must be registered as accredited by an EQAR member agency or recognised by the competent national authority.
- Simultaneous and coherent presence of the two `credentialSchema` entries (see §4.3).

**Reference technology**: SHACL 1.0 (W3C Recommendation, 20 July 2017) with a minimal RDFS reasoner.

**Output**: structured SHACL report (`sh:ValidationReport`) listing each non-conformity with its `sh:focusNode`, `sh:resultPath`, `sh:value`, `sh:resultSeverity` and `sh:resultMessage`.

## 4.3 The dual `credentialSchema` entry as an architectural pattern

The `credentialSchema` field of W3C-VCDM admits **a single value or a list**. When a list is provided, the consumer must run all declared validations. The dual architecture takes advantage of this property to declare both schemas within the same credential, without the need for additional registers or out-of-band metainformation.

```json
"credentialSchema": [
  {
    "id": "https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/0x05332a9dc53a4a26a15711262904f2a1dd081cf3da735350f42dac20426530a4",
    "type": "FullJsonSchemaValidator2021"
  },
  {
    "id": "https://registry.example.eu/shapes/eudiw-he-micro-shape.ttl",
    "type": "ShaclValidator2017"
  }
]
```

**Key editorial principle**: the JSON Schema with identifier `0x05332a9dc53a4a26a15711262904f2a1dd081cf3da735350f42dac20426530a4` is already operationally registered in the **EBSI Trusted Schemas Registry v3** for the higher-education microcredential. The dual architecture **does not modify it**; it adds alongside it a reference to the complementary SHACL shape. Backward compatibility with existing implementations is guaranteed.

## 4.4 Regulatory formalisation: requirements `EAA-7.2.1.3-W3C-01..04`

The proposed W3C-VC profile for the EUDIW raises the dual architecture from a recommended pattern to a **normative requirement** within the technical profile. The four requirements are symmetrical to those already applicable to mdoc (based on CDDL) and to SD-JWT VC (JSON Schema plus typed vocabulary).

| Id | Requirement |
|---|---|
| `EAA-7.2.1.3-W3C-01` | Every EAA in W3C-VC format SHALL include in `credentialSchema` two entries: `FullJsonSchemaValidator2021` and `ShaclValidator2017`. |
| `EAA-7.2.1.3-W3C-02` | The referenced JSON Schema SHALL cover the complete syntactic layer: presence, types, formats and cardinalities. |
| `EAA-7.2.1.3-W3C-03` | The referenced SHACL shape SHALL cover the semantic layer: controlled vocabularies, cross-field relationships and conformity with the applicable educational quality framework. |
| `EAA-7.2.1.3-W3C-04` | Both schemas SHALL be available in authoritative registers with integrity-proof mechanisms (`digestMultibase` or equivalent) and stable resolvable URIs. |

## 4.5 Concrete example: higher-education microcredential

The two documents that define dual validation for a European higher-education microcredential (EUHEMC) are shown below.

### 4.5.1 JSON Schema — relevant fragment

The operational JSON Schema is the one registered in EBSI with identifier `0x05332a9dc53a4a26a15711262904f2a1dd081cf3da735350f42dac20426530a4`. An illustrative fragment:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/0x05332a9dc53a4a26a15711262904f2a1dd081cf3da735350f42dac20426530a4",
  "title": "EUHEMC — European Higher Education Microcredential",
  "type": "object",
  "required": ["@context", "id", "type", "issuer", "validFrom", "credentialSubject", "credentialStatus", "credentialSchema"],
  "properties": {
    "@context": {
      "type": "array",
      "contains": { "const": "https://www.w3.org/ns/credentials/v2" }
    },
    "type": {
      "type": "array",
      "contains": { "const": "EuropeanHigherEducationMicrocredential" }
    },
    "credentialSubject": {
      "type": "object",
      "required": ["id", "hasClaim"],
      "properties": {
        "hasClaim": {
          "type": "array",
          "minItems": 1,
          "items": { "$ref": "#/$defs/LearningAchievement" }
        }
      }
    }
  }
}
```

### 4.5.2 SHACL — complete shape in Turtle

The complementary SHACL shape operates over the expanded RDF graph of the same credential:

```turtle
@prefix sh:       <http://www.w3.org/ns/shacl#> .
@prefix xsd:      <http://www.w3.org/2001/XMLSchema#> .
@prefix cred:     <https://www.w3.org/2018/credentials#> .
@prefix elm:      <http://data.europa.eu/snb/model/> .
@prefix eqf:      <http://data.europa.eu/snb/eqf/> .
@prefix isced-f:  <http://data.europa.eu/snb/isced-f/> .
@prefix credit:   <http://data.europa.eu/snb/credit/> .
@prefix eli:      <http://data.europa.eu/eli/ontology#> .
@prefix he-micro: <https://registry.example.eu/shapes/he-micro#> .

he-micro:CredentialShape
    a sh:NodeShape ;
    sh:targetClass elm:LearningAchievementCredential ;
    sh:property [
        sh:path cred:issuer ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
        sh:node he-micro:IssuerShape ;
        sh:message "The issuer shall comply with the accreditation profile." ;
    ] ;
    sh:property [
        sh:path cred:credentialSubject ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
        sh:property [
            sh:path elm:hasClaim ;
            sh:minCount 1 ;
            sh:node he-micro:LearningAchievementShape ;
        ] ;
    ] .

he-micro:IssuerShape
    a sh:NodeShape ;
    sh:property [
        sh:path elm:accreditation ;
        sh:minCount 1 ;
        sh:message "The issuer shall declare at least one valid accreditation." ;
    ] ;
    sh:property [
        sh:path elm:registeredIn ;
        sh:minCount 1 ;
        sh:class eli:Jurisdiction ;
        sh:message "The issuer shall declare the jurisdiction in which it is registered." ;
    ] .

he-micro:LearningAchievementShape
    a sh:NodeShape ;
    sh:property [
        sh:path elm:hasEQFLevel ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
        sh:node he-micro:EQFConceptShape ;
    ] ;
    sh:property [
        sh:path elm:creditPoints ;
        sh:minCount 1 ;
        sh:node he-micro:ECTSCreditShape ;
    ] ;
    sh:property [
        sh:path elm:hasISCEDFCode ;
        sh:minCount 1 ;
        sh:nodeKind sh:IRI ;
        sh:pattern "^http://data.europa.eu/snb/isced-f/" ;
    ] .

he-micro:EQFConceptShape
    a sh:NodeShape ;
    sh:property [
        sh:path ( [ sh:inversePath rdf:type ] ) ;
        sh:hasValue eqf:Concept ;
    ] ;
    sh:property [
        sh:path skos:inScheme ;
        sh:hasValue eqf:EQFScheme ;
        sh:message "The EQF level shall refer to the authoritative scheme published by the EU." ;
    ] .

he-micro:ECTSCreditShape
    a sh:NodeShape ;
    sh:property [
        sh:path elm:framework ;
        sh:hasValue credit:25831c2 ;
        sh:message "The declared credit framework shall be ECTS for higher education." ;
    ] ;
    sh:property [
        sh:path elm:point ;
        sh:datatype xsd:decimal ;
        sh:minInclusive 0.5 ;
        sh:maxInclusive 360.0 ;
    ] .
```

The shape captures the key semantic rules of the domain: the issuer shall be accredited and registered in a jurisdiction; the achievement shall declare EQF level, ECTS credits and ISCED-F; the values shall belong to the European authoritative vocabularies; the credits shall respect the admissible range for a higher-education microcredential.

## 4.6 Verification pipeline

A receiving verifier runs four steps over the received credential:

1. **Cryptographic verification**: validation of the Data Integrity proof (`ecdsa-rdfc-2019`, `bbs-2023`) or JOSE/COSE where applicable. Status check in `BitstringStatusList`.
2. **Syntactic validation**: execution of the declared JSON Schema. Structural report obtained.
3. **Expansion to RDF**: processing of the JSON-LD according to `@context` until the canonical graph is obtained.
4. **Semantic validation**: execution of the SHACL shape over the graph. `sh:ValidationReport` obtained.

The four steps are executed with **standard and open tools**, without proprietary APIs. Any implementer may replicate the pipeline with:

- **JSON-LD**: `jsonld` (Digital Bazaar), `pyld`, `titanium-json-ld`.
- **JSON Schema**: `ajv`, `jsonschema` (Python), `NJsonSchema`.
- **SHACL**: TopBraid SHACL, `pyshacl`, Apache Jena SHACL, `shacl-js`.

The combination of these open components is what enables **digital sovereignty by design** (see [01 — Context and foundations](./01-context-and-foundations.md), §1.7).

## 4.7 Authoritative registers

The two schemas reside in trusted registers with stable resolvable URIs:

- **EBSI Trusted Schemas Registry v3** (https://api-pilot.ebsi.eu/trusted-schemas-registry/v3) for the JSON Schema. Schemas are immutable by construction (the identifier is a content hash) and versionable through new registrations.
- **Authoritative SHACL registers**: for ELM v3.2, the register operated by the Europass Team of DG EMPL; for sectoral profiles, registers hosted by recognised consortia (Sectoral EAA Catalogue operated by DC4EU and successors).

Resolvable identifiers ensure that the verifier always retrieves the version referenced by the credential, regardless of the place of issuance and the passage of time.

## 4.8 Non-modification principle

The regulatory proposal adopts the principle of **non-modification** of existing operational artefacts. Specifically:

- The JSON Schema registered in EBSI is not modified. The regulatory proposal **adds** the reference to the SHACL shape; it does not **change** the JSON Schema.
- The ELM v3.2 profiles already published in the Europass Dataspace are not redesigned. The SHACL shape operates over the ELM graph without altering the ontology.
- Credentials already issued under the current JSON Schema remain valid. The SHACL shape applies to credentials issued from the moment the dual profile enters into force.

This principle preserves the **investments already made** by the ecosystem (DC4EU, EBSI-VECTOR, ISBE, TRACE4EU) and reduces the cost of adopting the EUDIW profile to practically zero for current implementers.

## 4.9 Operational coverage in EBSI

The **EBSI Trusted Schemas Registry v3** operates the dual architecture in production. Registered schemas are accompanied by SHACL shapes maintained by thematic consortia (education: DC4EU and successors; mobility: TRACE4EU; social: Safe Island) with traceability over the trust identifiers.

The EBSI Ledger additionally provides the decentralised trust mechanism for issuers and for status lists (`BitstringStatusList`), closing the validation perimeter on a European infrastructure operated by the Commission.

## 4.10 Outcome

The dual architecture combines three properties:

1. **Completeness**: both layers, syntactic and semantic, are verified against the same credential.
2. **Openness**: all technologies are W3C Recommendations or open standards.
3. **Operational immediacy**: the two registers (JSON Schema in EBSI TSR v3; SHACL shape in authoritative registers) are in production.

It is on this architecture that the subsequent chapters rest: the [European Learning Model v3.2](./05-european-learning-model.md) defines the semantic vocabulary verified by the shapes; the [lifecycle and trust framework](./06-lifecycle-and-trust.md) articulates the fourth step (status and revocation) of the pipeline; the [sectoral EAA catalogue](./07-sectoral-eaa-catalogue.md) lists the 18 SHACL shapes + JSON Schemas already published.

---

**Next**: [05 — European Learning Model](./05-european-learning-model.md)
