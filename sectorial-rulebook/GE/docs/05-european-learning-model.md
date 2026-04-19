# 05 — The European Learning Model v3.2 as semantic underpinning

## 5.1 What the European Learning Model is

The **European Learning Model (ELM)** is the reference ontology published by the European Commission (DG EMPL, Europass Team) to represent any learning experience and any educational or professional credential issued in Europe. Its purpose is twofold:

1. Provide a **common vocabulary** that allows issuers from any sector (higher education, vocational training, employers, public authorities, continuing-training providers) to describe with the same semantics what a person has learned, proved or achieved.
2. Act as a **mapping layer** to the European controlled vocabularies (EQF, ESCO, ISCED-F, NACE, national frameworks registered in ELI) and to the educational quality frameworks (ENQA/EQAR, ECVET and ECTS standards).

The version in force at the time of writing this document is **ELM v3.2**, published together with the **Europass European Digital Credentials for Learning (EDC) v1.9** and registered in the **EBSI Trusted Schemas Registry v3** as an operational profile.

## 5.2 Alignment with W3C-VCDM

ELM has been redesigned, since its version 3, to be **JSON-LD native**. Each ELM class is an OWL class with a resolvable IRI and canonical JSON-LD serialisation. This means that an ELM credential is simultaneously:

- A JSON object consumable by traditional tools.
- An RDF graph consumable by SHACL, SPARQL and OWL reasoners.
- A W3C Verifiable Credential conformant with VCDM (1.1 or 2.0) when wrapped with the appropriate `@context` and `type`.

Equivalence is established via the ELM `@context`, which aligns ELM classes with the standard VCDM properties (`credentialSubject`, `issuer`, `validFrom`, `validUntil`, `credentialStatus`, `credentialSchema`) and with the European controlled vocabularies.

## 5.3 Principal classes of ELM v3.2

The ELM v3.2 hierarchy is organised around seven class families:

| Family | Representative classes | Purpose |
|---|---|---|
| Agents | `Person`, `Organisation`, `Agent` | Represent persons, institutions and systems as subjects, issuers or evaluators. |
| Achievements | `LearningAchievement`, `LearningActivity`, `LearningAssessment` | Describe what has been learned, in which activity and how it has been assessed. |
| Qualifications | `Qualification`, `LearningOpportunity` | Represent the degree, the microcredential, the professional qualification, the training opportunity. |
| Accreditation | `Accreditation` | Declare accreditations of the issuer, programme or evaluator. |
| Outcomes | `LearningOutcome`, `Skill`, `Knowledge`, `Competence` | Express learning outcomes in terms of knowledge, skills and competences. |
| Credits | `AwardingProcess`, `CreditPoint` | Articulate the awarding of the achievement, the associated credits and the assessment process. |
| Claims | `Claim` | Declare verifiable claims about the person (achievements, qualifications, experiences). |

Each ELM class aligns with its equivalent in VCDM: `credentialSubject` is an ELM `Person`, `issuer` is an ELM `Organisation`, and the `hasClaim` structure organises achievements as `Claim`s that link to `LearningAchievement`, `Qualification` or `LearningActivity`.

## 5.4 Integrated controlled vocabularies

ELM does not invent new vocabularies; it references the authoritative European ones through stable IRIs published by the EU:

- **EQF — European Qualifications Framework**: levels 1 to 8 as `eqf:Concept` at `http://data.europa.eu/snb/eqf/`.
- **ISCED-F — International Standard Classification of Education, Fields**: field-of-study codes as `isced-f:Concept` at `http://data.europa.eu/snb/isced-f/`.
- **ESCO — European Skills, Competences, Qualifications and Occupations**: occupations and skills at `http://data.europa.eu/esco/`.
- **NACE — statistical classification of economic activities**: sectoral code associated with the qualification where applicable.
- **ELI — European Legislation Identifier**: referencing legal acts underpinning an accreditation or a qualification.
- **National qualifications frameworks**: aligned with EQF through the official correspondence published by each Member State.

This native integration realises **Requirement R1** (semantic expressiveness) and **Requirement R6** (integration with quality frameworks) of chapter 02.

## 5.5 Example: higher-education microcredential in ELM + VCDM

An EUHEMC (European Higher Education Microcredential) credential over W3C-VCDM 2.0 referencing ELM v3.2:

```json
{
  "@context": [
    "https://www.w3.org/ns/credentials/v2",
    "http://data.europa.eu/snb/model/context/edc-ap.jsonld"
  ],
  "id": "urn:uuid:3c39ff5d-58d7-4f9a-a3e4-5f1f6e0e7d2b",
  "type": ["VerifiableCredential", "EuropeanHigherEducationMicrocredential"],
  "issuer": {
    "id": "did:web:urv.cat",
    "type": "Organisation",
    "legalName": "Universitat Rovira i Virgili",
    "eidasLegalIdentifier": "urn:eidas:legalPersonIdentifier:ES:Q9350003A",
    "registeredIn": {
      "id": "http://data.europa.eu/eli/jurisdiction/ESP",
      "type": "Jurisdiction"
    },
    "accreditation": [
      {
        "id": "https://accreditations.example.eu/aneca/urv-2024",
        "type": "Accreditation",
        "decisionDate": "2024-06-15",
        "accreditingAgent": "urn:agent:EQAR:ANECA"
      }
    ]
  },
  "validFrom": "2026-01-15T00:00:00Z",
  "credentialSubject": {
    "id": "did:key:z6MkhaXgBZDvotDkL5257faiztiGiC2QtKLGpbnnEGta2doK",
    "type": "Person",
    "hasClaim": [
      {
        "id": "urn:uuid:a4e1-...-claim-01",
        "type": "LearningAchievementClaim",
        "awardingBody": "did:web:urv.cat",
        "awardedBy": {
          "id": "urn:uuid:proc-01",
          "type": "AwardingProcess",
          "issuedOn": "2026-01-15"
        },
        "specifiedBy": {
          "id": "urn:uuid:micro-data-analytics-001",
          "type": "Qualification",
          "title": { "@value": "Microcredential in Data Analytics for Humanities", "@language": "en" },
          "hasEQFLevel": "http://data.europa.eu/snb/eqf/7",
          "hasISCEDFCode": "http://data.europa.eu/snb/isced-f/0619",
          "creditPoints": {
            "framework": "http://data.europa.eu/snb/credit/25831c2",
            "point": 6.0
          },
          "learningOutcome": [
            {
              "title": "Apply statistical techniques to textual corpora",
              "relatedSkill": "http://data.europa.eu/esco/skill/..."
            }
          ]
        }
      }
    ]
  },
  "credentialStatus": {
    "id": "https://status.example.eu/pilot/bsl-urv-2026#12345",
    "type": "BitstringStatusListEntry",
    "statusPurpose": "revocation",
    "statusListIndex": "12345",
    "statusListCredential": "https://status.example.eu/pilot/bsl-urv-2026"
  },
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
}
```

All semantic values are **resolvable IRIs** pointing to European authoritative vocabularies. The verifier may dereference them to validate that they belong to the scheme (EQF, ESCO, ISCED-F) and to obtain multilingual labels in any official EU language.

## 5.6 Coverage of learning modalities

ELM v3.2 natively covers all modalities enumerated by the 2022 Council Recommendation on microcredentials and by the **European Approach to Micro-credentials** (European qualification system):

- **Formal education**: higher education (`EuropeanHigherEducationMicrocredential`, `EuropeanHigherEducationDiploma`), secondary education.
- **Vocational education and training**: `EuropeanVETMicrocredential`, VET qualifications, certificates from accredited centres.
- **Professional qualifications**: professional certifications, both regulated (`Regulated Profession` in the sense of Directive 2005/36/EC) and non-regulated.
- **Continuing professional development (CPD)**: learning throughout professional life, on-the-job learning, periodic recertification.
- **Informal and non-formal learning**: participation certificates, credentials issued by employers, learning by experience (APEL).
- **Quality assurance**: `Accreditation` as an independent credential for issuers, programmes and evaluators.

**Requirement R9** of chapter 02 is satisfied directly by the ELM taxonomy.

## 5.7 Sectoral extensibility

ELM admits sectoral extensions without any redesign of the core ontology. Three extension mechanisms coexist:

1. **Subclasses**: a sector can define a specific subclass of `LearningAchievement`, `Qualification` or `Accreditation` and publish the IRI in its own namespace.
2. **Additional properties**: through extension of the `@context` with properties that do not conflict with the core ELM vocabulary.
3. **Application profiles**: subsets of ELM with additional SHACL constraints, published as authoritative shapes in recognised registers.

This mechanism is what underpins the **Sectoral EAA Catalogue** published by DC4EU (see [07 — Sectoral EAA catalogue](./07-sectoral-eaa-catalogue.md)), with 18 educational and professional credential types defined as ELM profiles.

## 5.8 Multilingual traceability

All labels and descriptions of ELM classes and properties are published in the 24 official EU languages. The values of the controlled vocabularies (EQF, ESCO, ISCED-F) are also multilingual. An ELM credential issued in Spanish may be rendered in German, French, Polish or Swedish without reissuance: the recipient obtains localised labels from the canonical IRI of the concept.

This property is critical for cross-border mobility: a person with a microcredential issued by an Italian university may present it to a Polish employer, which will interpret it automatically in its own language without human intervention.

## 5.9 Open Badges 3.0 and international equivalence

The international educational-credentials community works on a convergent set of specifications that share VCDM as their core:

- **Open Badges 3.0** (1EdTech Consortium): international specification of educational credentials built on VCDM. It admits the same issuance, storage and verification infrastructure as an EUDIW EAA.
- **CTDL — Credential Transparency Description Language** (Credential Engine): US vocabulary alignable with ELM via bilateral mapping.
- **LER — Learning and Employment Records**: emerging labour-market standards, with convergence towards VCDM.

ELM and Open Badges 3.0 are **semantically compatible** at the common core: both describe achievements, issuers, subjects and assessments over VCDM. A credential issued in Europe under ELM may be interpreted by a North American employer or an Asian LER system without reissuance, provided that the consumer has the appropriate `@context`.

**Requirement R9** (full coverage of modalities) and **Requirement R7** (portability) are satisfied with empirical support in global deployments.

## 5.10 Outcome

ELM v3.2 contributes to the EUDIW profile for W3C-VC:

1. A common and extensible vocabulary for all learning modalities.
2. Native integration with European controlled vocabularies and educational quality frameworks.
3. Semantic compatibility with the global credentialing ecosystems (Open Badges, CTDL, LER).
4. Multilingual traceability for the 24 official languages.
5. Sectoral extensibility without modification of the core.
6. Operational availability in the Europass Dataspace and in the EBSI Trusted Schemas Registry v3.

Together with the [dual validation architecture](./04-dual-validation-architecture.md) and the [lifecycle and trust framework](./06-lifecycle-and-trust.md), ELM completes the semantic layer of the proposed profile.

---

**Next**: [06 — Lifecycle and trust framework](./06-lifecycle-and-trust.md)
