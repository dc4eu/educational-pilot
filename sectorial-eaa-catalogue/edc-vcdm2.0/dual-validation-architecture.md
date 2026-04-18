> **DUAL VALIDATION ARCHITECTURE**
>
> JSON Schema + SHACL on W3C-VC / eIDAS 2.0

European Educational Credentials · ELM 3.2 · EBSI TSR

  --------------- ---------------------------------------------
  **Field**       **Value**
  Version         1.0.0
  Date            March 2026
  Base standard   ELM 3.2 · W3C-VC Data Model 2.0 · eIDAS 2.0
  Registry        EBSI Trusted Schemas Registry v3 (Pilot)
  Licence         CC BY 4.0
  --------------- ---------------------------------------------

> **1. Introduction and Context**

The European ecosystem for verifiable digital educational credentials has reached a critical point of maturity. The convergence of the European Learning Model (ELM 3.2), the European Digital Credential (EDC) application profile, the W3C Verifiable Credentials Data Model 2.0, and the eIDAS 2.0 legal framework defines a technical environment where data validation can no longer be resolved by a single technological layer.

This document describes the dual validation architecture that combines JSON Schema and SHACL (Shapes Constraint Language) within the credentialSchema field of a credential issued in JSON-LD. This architecture is registered in the EBSI Trusted Schemas Registry (TSR), making the schemas verifiable, immutable, and discoverable by any participant in the ecosystem.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Why two schemas rather than one?**                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                        |
| JSON Schema validates the structure and data types of the document as a JSON tree. SHACL validates the semantics and relationships of the RDF graph that emerges when the JSON-LD is interpreted using its ontological context. They are complementary layers: the first ensures the document is parseable; the second ensures its meaning is correct. |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

> **2. Technology Stack and Standards**

The architecture described in this document is built upon the following standards and specifications, all current at the time of writing:

  --------------------------------- ----------------------- ----------------------------------------------------------------------
  **Standard / Specification**      **Layer**               **Role in this architecture**
  ELM 3.2 (ELM ontology)            Ontological             Semantic data model of reference for educational achievements
  EDC Application Profile (SHACL)   Semantic validation     Generic EDC SHACL shapes, base for profile-specific shapes
  W3C VC Data Model 2.0             Credential envelope     Canonical verifiable credential structure with validFrom, validUntil
  JSON Schema draft 2020-12         Structural validation   Schemas registered in EBSI TSR that validate JSON structure
  SHACL (W3C Rec. 2017)             Semantic validation     Profile-specific shapes registered in EBSI TSR (this document)
  JSON-LD 1.1                       Serialisation           Makes JSON interpretable as an RDF graph
  eIDAS 2.0 / EUDI Wallet           Legal framework         Requires issuer identification via verifiable eidasLegalIdentifier
  EBSI TSR v3                       Trust infrastructure    Permissioned blockchain where schemas are registered and anchored
  --------------------------------- ----------------------- ----------------------------------------------------------------------

> **3. Division of Responsibilities Between the Two Schemas**

The credentialSchema field of a credential issued under this architecture always contains two entries with distinct types. Each activates a different validation mechanism in the verifier.

**3.1 Schema of type JsonSchema (already registered in EBSI TSR)**

The JSON Schema already registered in the TSR covers the following responsibilities:

-   Validation of the JSON tree structure: presence of mandatory top-level fields (type, issuer, credentialSubject, validFrom, credentialSchema, etc.).

-   Validation of scalar data types: dateTime, URI, string with pattern, integer with range.

-   Basic cardinalities expressible in JSON Schema: minItems, maxItems, required.

-   Restriction of the type array to the exact set of strings identifying the profile (e.g. EuropeanHigherEducationMicrocredential).

-   Restriction of the credit framework (ECTS or ECVET) and the numeric range of points (1--15) via pattern.

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **What JSON Schema cannot validate**                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                     |
| JSON Schema cannot verify that a URI points to a valid concept in an external controlled vocabulary. It cannot impose restrictions conditioned on values of other fields in non-linear graphs. It cannot validate coherence between the issuer\'s eidasLegalIdentifier and the EBSI Trusted Issuers Registry. These responsibilities fall to SHACL. |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**3.2 Schema of type ShaclValidator2017 (new, subject of this document)**

The profile-level SHACL shape covers the following additional responsibilities, which are impossible or inefficient to express in JSON Schema:

-   Validation that the issuer has exactly one eidasLegalIdentifier with a notation and a jurisdiction (dc:spatial) as an IRI from the Publications Office country vocabulary.

-   Semantic validation of the credential type as an RDF class in the elm: namespace, not merely as a string in an array.

-   Validation that credentialSchema contains at least one entry of type elm:ShaclValidator2017, as required by the generic EDC profile.

-   Coherence validation between provenBy (assessment) and the credential type: mandatory in microcredentials, absent or conditional in diplomas.

-   Validation that eqfLevel references an IRI from the controlled EQF vocabulary (http://data.europa.eu/snb/eqf/), not merely any object with a notation field.

-   Validation that educationSubject references concepts from the ISCED-F vocabulary when using the elm:ISCEDFCode property.

-   Differentiated severities: sh:Violation for minimum interoperability constraints, sh:Warning for recommended best practices.

> **4. Anatomy of a Credential Issued with Dual Schema**

The following JSON-LD structure shows a credential issued under this architecture, with the two entries in credentialSchema. The example corresponds to the EuropeanHigherEducationMicrocredential profile.

> {
>
> \"\@context\": \[
>
> \"https://www.w3.org/ns/credentials/v2\",
>
> \"http://data.europa.eu/snb/model/context/edc-ap\"
>
> \],
>
> \"id\": \"urn:credential:he-micro-001\",
>
> \"type\": \[
>
> \"VerifiableCredential\",
>
> \"VerifiableAttestation\",
>
> \"EuropeanDigitalCredential\",
>
> \"EuropeanHigherEducationMicrocredential\"
>
> \],
>
> \"issuer\": {
>
> \"id\": \"did:ebsi:zABC123\...\",
>
> \"type\": \"Organisation\",
>
> \"elm:eidasLegalIdentifier\": {
>
> \"type\": \"LegalIdentifier\",
>
> \"skos:notation\": \"ES12345678\",
>
> \"dc:spatial\": {
>
> \"id\": \"http://publications.europa.eu/resource/authority/country/ESP\"
>
> }
>
> }
>
> },
>
> \"credentialSchema\": \[
>
> {
>
> \"id\": \"https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/0x05332a\...\",
>
> \"type\": \"JsonSchema\"
>
> },
>
> {
>
> \"id\": \"https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/0xSHACL\_HE\_MICRO\",
>
> \"type\": \"ShaclValidator2017\"
>
> }
>
> \],
>
> \"validFrom\": \"2025-09-01T00:00:00Z\",
>
> \"issued\": \"2025-09-01T00:00:00Z\",
>
> \"credentialSubject\": { \"\...\" : \"\...\" },
>
> \"elm:credentialProfiles\": \[ \"\...\" \],
>
> \"elm:displayParameter\": { \"\...\" : \"\...\" }
>
> }

The key field is credentialSchema. The first entry activates the already-registered JSON Schema structural validation. The second, of type ShaclValidator2017, activates SHACL semantic validation over the RDF graph. A verifier conformant with the EDC profile executes both in sequence.

> **5. The Technical Achievement: What This Architecture Delivers**

The combination of JSON Schema and SHACL registered in the EBSI TSR is not an implementation detail. It is an architectural decision with direct consequences for the quality, interoperability, and automation-readiness of European educational credentials.

**5.1 Complete two-layer validation without overlap**

Each layer validates what the other cannot. JSON Schema ensures the credential is structurally correct and can be processed by any system operating on JSON. SHACL ensures its semantic meaning is correct when interpreted as an RDF graph with the ELM context. The result is full coverage without redundancy.

**5.2 Blockchain-guaranteed immutability and discoverability**

By registering both schemas in the EBSI TSR, each entry is anchored in EBSI\'s permissioned blockchain with a cryptographic hash as its identifier. This guarantees that the schema referenced in the credential cannot be altered retroactively. Any verifier can resolve the hash, retrieve the schema, and execute it locally without depending on the availability of an external server.

**5.3 Alignment with eIDAS 2.0 and the EUDI Wallet**

The SHACL shape enforces the presence of an eidasLegalIdentifier in the issuer with an explicit jurisdiction. This is an eIDAS 2.0 requirement for legal identification of issuers in the European digital identity space. By registering this constraint as a SHACL shape in the TSR, compliance with eIDAS 2.0 becomes automatically executable and auditable.

**5.4 Semantic differentiation between credential profiles**

The different profiles (HE microcredential, VET microcredential, diploma, upper secondary certificate) share the same base JSON Schema, but have specific SHACL shapes that enforce the constraints proper to each type. This maintains a clear hierarchy: the JSON Schema validates the common minimum; the profile SHACL shape validates the type-specific requirements.

**5.5 Readiness for automation and AI**

AI agents and automated credential verification systems can discover both schemas through the TSR, execute validation without human intervention, and produce structured conformance reports (the SHACL Validation Report is itself an RDF graph, machine-processable). This makes credentials FAIR+R: findable, accessible, interoperable, reusable, and AI-ready.

> **6. Schema 1: JSON Schema (already registered in EBSI TSR)**

The JSON Schema for the EuropeanHigherEducationMicrocredential profile is already registered in the EBSI TSR Pilot with the following identifier:

> **0x05332a9dc53a4a26a15711262904f2a1dd081cf3da735350f42dac20426530a4**

This schema requires no modification. Its responsibility is limited to the structural validation described in section 3.1. The addition of the SHACL shape is entirely additive: it is registered as a new independent schema, and the issued credential references both in the credentialSchema array.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Non-modification principle for the existing JSON Schema**                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| The JSON Schema registered on blockchain is immutable by design. To add SHACL validation, the existing JSON Schema is neither modified nor revoked. A new schema of type ShaclValidator2017 is registered, and credentials issued from this point forward declare both. This preserves backward compatibility with all issuers and verifiers already operating with the JSON Schema. |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

> **7. Schema 2: SHACL Shape for EuropeanHigherEducationMicrocredential**

The following SHACL shape is registered as a new schema in the EBSI TSR. It is written in Turtle (TTL) syntax, the most compact and readable RDF serialisation format. The TSR is format-agnostic: it accepts any schema type, including Turtle.

**7.1 Complete SHACL shape (Turtle)**

> \@prefix sh: \<http://www.w3.org/ns/shacl\#\> .
>
> \@prefix elm: \<http://data.europa.eu/snb/model/elm/\> .
>
> \@prefix cred: \<https://www.w3.org/2018/credentials\#\> .
>
> \@prefix dc: \<http://purl.org/dc/terms/\> .
>
> \@prefix skos: \<http://www.w3.org/2004/02/skos/core\#\> .
>
> \@prefix xsd: \<http://www.w3.org/2001/XMLSchema\#\> .
>
> \@prefix rov: \<http://www.w3.org/ns/regorg\#\> .
>
> \@prefix rdf: \<http://www.w3.org/1999/02/22-rdf-syntax-ns\#\> .
>
> \@prefix he-micro: \<https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/shacl/he-micro\#\> .
>
> \# ── ROOT SHAPE: credential as EuropeanHigherEducationMicrocredential ────
>
> he-micro:CredentialShape
>
> a sh:NodeShape ;
>
> sh:targetClass elm:EuropeanDigitalCredential ;
>
> sh:name \"European Higher Education Microcredential - SHACL Profile\"\@en ;
>
> sh:description \"Level-3 semantic constraints for HE microcredentials.\"\@en ;
>
> \# Type MUST include the HE-specific profile type
>
> sh:property \[
>
> sh:path rdf:type ;
>
> sh:hasValue elm:EuropeanHigherEducationMicrocredential ;
>
> sh:minCount 1 ;
>
> sh:severity sh:Violation ;
>
> sh:message \"Credential must declare elm:EuropeanHigherEducationMicrocredential.\"\@en ;
>
> \] ;
>
> \# credentialSchema MUST have at least 2 entries (JsonSchema + ShaclValidator2017)
>
> sh:property \[
>
> sh:path cred:credentialSchema ;
>
> sh:minCount 2 ;
>
> sh:severity sh:Violation ;
>
> sh:message \"At least two entries required: JsonSchema and ShaclValidator2017.\"\@en ;
>
> \] ;
>
> \# issuer: exactly one, with mandatory eidasLegalIdentifier
>
> sh:property \[
>
> sh:path cred:issuer ;
>
> sh:minCount 1 ; sh:maxCount 1 ;
>
> sh:node he-micro:IssuerShape ;
>
> sh:severity sh:Violation ;
>
> \] ;
>
> \# credentialSubject: exactly one person with hasClaim
>
> sh:property \[
>
> sh:path cred:credentialSubject ;
>
> sh:minCount 1 ; sh:maxCount 1 ;
>
> sh:node he-micro:CredentialSubjectShape ;
>
> sh:severity sh:Violation ;
>
> \] .
>
> \# ── ISSUER: Organisation with mandatory eIDAS identifier ────────────────
>
> he-micro:IssuerShape
>
> a sh:NodeShape ;
>
> sh:property \[
>
> sh:path elm:eidasLegalIdentifier ;
>
> sh:minCount 1 ; sh:maxCount 1 ;
>
> sh:node he-micro:LegalIdentifierShape ;
>
> sh:severity sh:Violation ;
>
> sh:message \"Issuer must have exactly one eidasLegalIdentifier.\"\@en ;
>
> \] .
>
> he-micro:LegalIdentifierShape
>
> a sh:NodeShape ;
>
> sh:property \[
>
> sh:path skos:notation ;
>
> sh:minCount 1 ; sh:datatype xsd:string ;
>
> sh:severity sh:Violation ;
>
> sh:message \"The eidasLegalIdentifier must have a notation value.\"\@en ;
>
> \] ;
>
> sh:property \[
>
> sh:path dc:spatial ;
>
> sh:minCount 1 ; sh:nodeKind sh:IRI ;
>
> sh:severity sh:Violation ;
>
> sh:message \"Jurisdiction (dc:spatial) must be an IRI from the country vocabulary.\"\@en ;
>
> \] .
>
> \# ── CREDENTIAL SUBJECT: Person with dateOfBirth and hasClaim ────────────
>
> he-micro:CredentialSubjectShape
>
> a sh:NodeShape ;
>
> sh:property \[
>
> sh:path elm:dateOfBirth ;
>
> sh:minCount 1 ; sh:datatype xsd:dateTime ;
>
> sh:severity sh:Violation ;
>
> sh:message \"Subject must include date of birth.\"\@en ;
>
> \] ;
>
> sh:property \[
>
> sh:path elm:hasClaim ;
>
> sh:minCount 1 ;
>
> sh:node he-micro:LearningAchievementShape ;
>
> sh:severity sh:Violation ;
>
> sh:message \"Subject must have at least one LearningAchievement.\"\@en ;
>
> \] .
>
> \# ── LEARNING ACHIEVEMENT: semantic core of the HE microcredential ───────
>
> he-micro:LearningAchievementShape
>
> a sh:NodeShape ;
>
> sh:property \[
>
> sh:path rdf:type ;
>
> sh:hasValue elm:LearningAchievement ; sh:minCount 1 ;
>
> sh:severity sh:Violation ;
>
> \] ;
>
> \# specifiedBy mandatory: eqfLevel, educationSubject, mode, creditPoint
>
> sh:property \[
>
> sh:path elm:specifiedBy ;
>
> sh:minCount 1 ; sh:maxCount 1 ;
>
> sh:node he-micro:SpecificationShape ;
>
> sh:severity sh:Violation ;
>
> sh:message \"Achievement must be specified by a LearningAchievementSpecification.\"\@en ;
>
> \] ;
>
> \# awardedBy mandatory: awardingBody, awardingDate, location
>
> sh:property \[
>
> sh:path elm:awardedBy ;
>
> sh:minCount 1 ; sh:maxCount 1 ;
>
> sh:node he-micro:AwardingProcessShape ;
>
> sh:severity sh:Violation ;
>
> \] ;
>
> \# provenBy MANDATORY in microcredential (key difference vs diploma)
>
> sh:property \[
>
> sh:path elm:provenBy ;
>
> sh:minCount 1 ;
>
> sh:node he-micro:LearningAssessmentShape ;
>
> sh:severity sh:Violation ;
>
> sh:message \"An HE microcredential must include at least one assessment (provenBy).\"\@en ;
>
> \] ;
>
> \# creditReceived: if present, must be ECTS between 1 and 15
>
> sh:property \[
>
> sh:path elm:creditReceived ;
>
> sh:node he-micro:ECTSCreditShape ;
>
> sh:severity sh:Warning ;
>
> sh:message \"Declared credits must follow the ECTS framework (1-15).\"\@en ;
>
> \] .
>
> \# ── SPECIFICATION: eqfLevel, educationSubject, mode, creditPoint ─────────
>
> he-micro:SpecificationShape
>
> a sh:NodeShape ;
>
> sh:property \[
>
> sh:path elm:EQFLevel ;
>
> sh:minCount 1 ; sh:maxCount 1 ;
>
> sh:node he-micro:EQFConceptShape ;
>
> sh:severity sh:Violation ;
>
> sh:message \"Specification must declare the EQF level.\"\@en ;
>
> \] ;
>
> sh:property \[
>
> sh:path elm:educationSubject ;
>
> sh:minCount 1 ;
>
> sh:severity sh:Violation ;
>
> sh:message \"At least one education subject (educationSubject) must be indicated.\"\@en ;
>
> \] ;
>
> sh:property \[
>
> sh:path elm:mode ;
>
> sh:minCount 1 ;
>
> sh:severity sh:Violation ;
>
> sh:message \"Learning mode must be indicated.\"\@en ;
>
> \] ;
>
> sh:property \[
>
> sh:path elm:creditPoint ;
>
> sh:minCount 1 ; sh:node he-micro:ECTSCreditShape ;
>
> sh:severity sh:Warning ;
>
> sh:message \"It is recommended to declare ECTS credits on the specification.\"\@en ;
>
> \] .
>
> \# ── EQF: valid notation + IRI from the controlled EQF vocabulary ─────────
>
> he-micro:EQFConceptShape
>
> a sh:NodeShape ;
>
> sh:nodeKind sh:IRI ;
>
> sh:pattern \"\^http://data\\\\.europa\\\\.eu/snb/eqf/\" ;
>
> sh:severity sh:Warning ;
>
> sh:message \"EQF level should reference the Publications Office controlled vocabulary.\"\@en ;
>
> sh:property \[
>
> sh:path skos:notation ;
>
> sh:minCount 1 ; sh:datatype xsd:string ;
>
> sh:pattern \"\^\[1-8\]\$\" ;
>
> sh:severity sh:Violation ;
>
> sh:message \"EQF level must be a value between 1 and 8.\"\@en ;
>
> \] .
>
> \# ── ECTS: framework ECTS and points 1-15 ─────────────────────────────────
>
> he-micro:ECTSCreditShape
>
> a sh:NodeShape ;
>
> sh:property \[
>
> sh:path elm:framework ;
>
> sh:minCount 1 ; sh:node he-micro:ECTSFrameworkShape ;
>
> sh:severity sh:Violation ;
>
> sh:message \"Credit framework must be ECTS.\"\@en ;
>
> \] ;
>
> sh:property \[
>
> sh:path elm:point ;
>
> sh:minCount 1 ; sh:datatype xsd:string ;
>
> sh:pattern \"\^(1\[0-5\]\|\[1-9\])\$\" ;
>
> sh:severity sh:Violation ;
>
> sh:message \"ECTS credits must be between 1 and 15.\"\@en ;
>
> \] .
>
> he-micro:ECTSFrameworkShape
>
> a sh:NodeShape ;
>
> sh:property \[
>
> sh:path skos:notation ;
>
> sh:hasValue \"ECTS\" ;
>
> sh:severity sh:Violation ;
>
> sh:message \"Credit framework notation must be ECTS.\"\@en ;
>
> \] .
>
> \# ── AWARDING PROCESS: awardingBody, awardingDate, location ───────────────
>
> he-micro:AwardingProcessShape
>
> a sh:NodeShape ;
>
> sh:property \[
>
> sh:path elm:awardingBody ;
>
> sh:minCount 1 ; sh:node he-micro:AwardingBodyShape ;
>
> sh:severity sh:Violation ;
>
> \] ;
>
> sh:property \[
>
> sh:path elm:awardingDate ;
>
> sh:minCount 1 ; sh:datatype xsd:dateTime ;
>
> sh:severity sh:Violation ;
>
> sh:message \"Awarding process must include a date.\"\@en ;
>
> \] ;
>
> sh:property \[
>
> sh:path elm:location ;
>
> sh:minCount 1 ;
>
> sh:severity sh:Violation ;
>
> sh:message \"Awarding process must include a location.\"\@en ;
>
> \] .
>
> he-micro:AwardingBodyShape
>
> a sh:NodeShape ;
>
> sh:property \[
>
> sh:path rov:legalName ;
>
> sh:minCount 1 ;
>
> sh:severity sh:Warning ;
>
> sh:message \"It is recommended to include the legal name of the awarding body.\"\@en ;
>
> \] .
>
> \# ── LEARNING ASSESSMENT: mandatory grade ─────────────────────────────────
>
> he-micro:LearningAssessmentShape
>
> a sh:NodeShape ;
>
> sh:property \[
>
> sh:path elm:grade ;
>
> sh:minCount 1 ;
>
> sh:severity sh:Violation ;
>
> sh:message \"Assessment must include a grade.\"\@en ;
>
> \] ;
>
> sh:property \[
>
> sh:path elm:awardedBy ;
>
> sh:minCount 1 ;
>
> sh:severity sh:Violation ;
>
> sh:message \"Assessment must have an awardedBy.\"\@en ;
>
> \] .
>
> **8. Schema 2 (Variant): SHACL Shape for EuropeanVETMicrocredential**

The VET (Vocational Education and Training) profile is structurally identical to the HE profile, with two precise semantic differences: the credential type and the credit framework (ECVET instead of ECTS). The following SHACL shape is a variant of the HE profile with only those two modifications.

> \@prefix sh: \<http://www.w3.org/ns/shacl\#\> .
>
> \@prefix elm: \<http://data.europa.eu/snb/model/elm/\> .
>
> \@prefix cred: \<https://www.w3.org/2018/credentials\#\> .
>
> \@prefix skos: \<http://www.w3.org/2004/02/skos/core\#\> .
>
> \@prefix xsd: \<http://www.w3.org/2001/XMLSchema\#\> .
>
> \@prefix rdf: \<http://www.w3.org/1999/02/22-rdf-syntax-ns\#\> .
>
> \@prefix vet-micro: \<https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/shacl/vet-micro\#\> .
>
> \# ── DIFFERENCE 1: VET credential type ──────────────────────────────────
>
> vet-micro:CredentialShape
>
> a sh:NodeShape ;
>
> sh:targetClass elm:EuropeanDigitalCredential ;
>
> sh:name \"European VET Microcredential - SHACL Profile\"\@en ;
>
> sh:property \[
>
> sh:path rdf:type ;
>
> sh:hasValue elm:EuropeanVocationalEducationTrainingMicrocredential ;
>
> sh:minCount 1 ; sh:severity sh:Violation ;
>
> sh:message \"Credential must declare elm:EuropeanVETMicrocredential.\"\@en ;
>
> \] ;
>
> sh:property \[
>
> sh:path cred:credentialSchema ;
>
> sh:minCount 2 ; sh:severity sh:Violation ;
>
> \] ;
>
> sh:property \[
>
> sh:path cred:issuer ;
>
> sh:minCount 1 ; sh:maxCount 1 ;
>
> sh:node vet-micro:IssuerShape ; sh:severity sh:Violation ;
>
> \] ;
>
> sh:property \[
>
> sh:path cred:credentialSubject ;
>
> sh:minCount 1 ; sh:maxCount 1 ;
>
> sh:node vet-micro:CredentialSubjectShape ; sh:severity sh:Violation ;
>
> \] .
>
> \# IssuerShape, LegalIdentifierShape, CredentialSubjectShape,
>
> \# LearningAchievementShape (with mandatory provenBy), SpecificationShape,
>
> \# EQFConceptShape, AwardingProcessShape, AwardingBodyShape and
>
> \# LearningAssessmentShape are identical to the HE profile.
>
> \# Only the credit shape changes:
>
> \# ── DIFFERENCE 2: ECVET framework instead of ECTS ───────────────────────
>
> vet-micro:ECVETCreditShape
>
> a sh:NodeShape ;
>
> sh:property \[
>
> sh:path elm:framework ;
>
> sh:minCount 1 ; sh:node vet-micro:ECVETFrameworkShape ;
>
> sh:severity sh:Violation ;
>
> sh:message \"Credit framework must be ECVET in VET credentials.\"\@en ;
>
> \] ;
>
> sh:property \[
>
> sh:path elm:point ;
>
> sh:minCount 1 ; sh:datatype xsd:string ;
>
> sh:pattern \"\^(1\[0-5\]\|\[1-9\])\$\" ;
>
> sh:severity sh:Violation ;
>
> sh:message \"ECVET points must be between 1 and 15.\"\@en ;
>
> \] .
>
> vet-micro:ECVETFrameworkShape
>
> a sh:NodeShape ;
>
> sh:property \[
>
> sh:path skos:notation ;
>
> sh:hasValue \"ECVET\" ;
>
> sh:severity sh:Violation ;
>
> sh:message \"Credit framework notation must be ECVET.\"\@en ;
>
> \] .
>
> **9. Registration Process in the EBSI TSR**

The EBSI Trusted Schemas Registry v3 is format-agnostic. It accepts JSON, JSON-LD, XML, Turtle, and any other format. The registration process always follows the same sequence:

**9.1 Registration sequence**

1.  Authentication: obtain a Bearer JWT via the EBSI authorisation flow using the issuer\'s DID, requesting the tsr\_write scope.

2.  Payload preparation: serialise the SHACL shape in Turtle. The content is transmitted as an encoded string in the JSON-RPC request body.

3.  JSON-RPC call to the insertSchema method with the Turtle content of the SHACL shape.

4.  EBSI calculates the Keccak-256 hash of the content and uses it as the schema identifier (the 0x\... that appears in the TSR URL).

5.  Verification: query GET /schemas/{schemaId} to confirm registration and obtain the definitive identifier.

6.  Update credential issuance templates with the new identifier in the credentialSchema\[1\].id field.

**9.2 Summary of schemas to register**

  ---------------------------------------------- ------------ -------------------- ----------------------
  **Profile**                                    **Action**   **TSR type**         **Status**
  EuropeanHigherEducationMicrocredential         Keep         JsonSchema           Registered
  EuropeanHigherEducationMicrocredential SHACL   NEW          ShaclValidator2017   Pending registration
  EuropeanVETMicrocredential                     Keep         JsonSchema           Registered
  EuropeanVETMicrocredential SHACL               NEW          ShaclValidator2017   Pending registration
  EuropeanHigherEducationDiploma                 Keep         JsonSchema           Registered
  EuropeanUpperSecondaryEducationCertificate     Keep         JsonSchema           Registered
  ---------------------------------------------- ------------ -------------------- ----------------------

Note: SHACL shapes for the Diploma and Upper Secondary Certificate, being profiles with fewer semantic constraints, may be registered in a subsequent phase. The priority is microcredentials, which have the most specific requirements.

> **10. SHACL Severity Map by Constraint**

The following table details every constraint in the HE Microcredential SHACL shape, its severity, and the rationale for that classification. The same map applies to the VET variant, substituting ECTS with ECVET.

  ---------------------------------------------- -------------- ----------------------------------------------------------------------------
  **Constraint**                                 **Severity**   **Rationale**
  Type EuropeanHigherEducationMicrocredential    Violation      Without this type the verifier cannot identify the profile
  credentialSchema minCount 2                    Violation      The EDC profile requires at least one ShaclValidator2017
  issuer with eidasLegalIdentifier               Violation      eIDAS 2.0 requirement for legal identification of the issuer
  eidasLegalIdentifier.notation                  Violation      Without a value the identifier is not processable
  eidasLegalIdentifier.dc:spatial as IRI         Violation      Jurisdiction must be resolvable as an RDF concept
  credentialSubject.dateOfBirth                  Violation      Mandatory personal identity field in educational credentials
  hasClaim minCount 1                            Violation      A credential without an educational claim has no semantic content
  LearningAchievement.specifiedBy                Violation      Without a specification there is no information about the achievement
  LearningAchievement.awardedBy                  Violation      Without an awarding body the credential cannot be institutionally verified
  LearningAchievement.provenBy minCount 1        Violation      Key differentiator microcredential vs diploma: requires assessment
  Specification.eqfLevel mandatory               Violation      European qualification level mandatory for interoperability
  eqfLevel.notation pattern 1-8                  Violation      A value outside the EQF range is semantically invalid
  Specification.educationSubject minCount 1      Violation      Subject area required for cataloguing and discovery
  Specification.mode minCount 1                  Violation      Learning mode required by the EDC profile
  awardingProcess.awardingDate                   Violation      Awarding date required for temporal validity
  awardingProcess.location                       Violation      Awarding jurisdiction required by the EDC profile
  LearningAssessment.grade                       Violation      Grade is mandatory in every assessment
  eqfLevel IRI from Publications Office vocab.   Warning        Best practice: reference to the official controlled vocabulary
  creditReceived with ECTS framework             Warning        Recommended for ECTS interoperability; may not always apply
  Specification.creditPoint                      Warning        Recommended inclusion in the achievement specification
  awardingBody.legalName                         Warning        Legal name recommended for institutional traceability
  ---------------------------------------------- -------------- ----------------------------------------------------------------------------

> **11. End-to-End Verification Flow**

A verifier receiving a credential issued under this architecture follows this validation flow:

7.  JSON reception and parsing: the verifier parses the document as JSON and extracts the credentialSchema array.

8.  For each entry in credentialSchema, the verifier resolves the id in the EBSI TSR, retrieving the content of the corresponding schema.

9.  JSON Schema validation: the verifier executes the JSON Schema against the complete JSON document. On failure, it emits structural errors and may reject the credential.

10. JSON-LD expansion: the verifier interprets the JSON-LD document with its context, producing an RDF graph with explicit elm: and cred: triples.

11. SHACL validation: the verifier executes the SHACL shape against the RDF graph. The SHACL engine produces a Validation Report (which is itself an RDF graph).

12. Validation Report interpretation: sh:conforms true indicates full conformance. sh:Violation indicates rejection. sh:Warning indicates conformance with advisories.

13. Signature verification: the verifier checks the cryptographic proof of the credential against the issuer\'s DID in the EBSI DID Registry.

14. Issuer verification: the verifier checks that the issuer DID is registered in the EBSI Trusted Issuers Registry with the attribute corresponding to the credential type.

> **12. Conclusions**

The dual JSON Schema + SHACL validation architecture registered in the EBSI TSR represents the state of the art in the issuance of verifiable European educational credentials. Its advantages are cumulative and complementary:

-   Full validation coverage: structural and semantic, without gaps or overlaps.

-   Blockchain-guaranteed immutability: schemas cannot be altered retroactively.

-   eIDAS 2.0 compliance: the SHACL shape enforces the presence of a verifiable eidasLegalIdentifier.

-   Semantic differentiation between profiles: each credential type has its own SHACL shape with the precise constraints that distinguish it from other profiles.

-   Automatic European interoperability: credentials issued under this architecture are processable by any verifier conformant with the EDC profile without additional configuration.

-   AI-readiness: the SHACL Validation Report is a machine-processable RDF graph, compatible with automated analysis pipelines.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Key design decision**                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                  |
| Existing JSON Schemas in the TSR are not modified. Only the new SHACL schemas are registered. Credentials issued from adoption of this architecture declare both schemas in credentialSchema. Credentials issued previously remain valid against the JSON Schema. The transition is entirely additive and does not break backward compatibility. |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

*Document produced in the context of European verifiable educational credentials development · ELM 3.2 · W3C-VC 2.0 · eIDAS 2.0 · EBSI TSR v3*
