# Microcredentials Schema

## Overview

This document describes the data model and schema for University Microcredentials, which provide certified, verifiable digital credentials attesting to the achievement of specific learning outcomes following a short learning experience. The model is implemented using the European Learning Model (ELM) v3.2 and the W3C Verifiable Credentials Data Model (VCDM), aligning with the European Digital Credentials for Learning (EDC) framework and the Council of the EU Recommendation (2022).

## Definition

A University Microcredential is a certified, verifiable digital credential that attests to the achievement of specific learning outcomes following a short learning experience. These credentials are issued in a secure digital format and are recognised across the European Higher Education Area (EHEA).

## Data Model Structure

The Microcredential model extends the European Learning Model (ELM) v3.2, using its structure for representing achievements, activities, assessments, and entitlements. The credential is serialized as a Verifiable Credential with the following high-level structure:

```json
{
  "@context": [
    "https://www.w3.org/2018/credentials/v1",
    "https://europa.eu/2022/credentials/microcredential/v1"
  ],
  "id": "urn:uuid:...",
  "type": ["VerifiableCredential", "EuropeanDigitalCredential", "UniversityMicrocredential"],
  "issuer": {
    // Organisation details
  },
  "issuanceDate": "2023-07-15T10:00:00Z",
  "credentialSubject": {
    "id": "did:example:123",
    "achievement": {
      // Achievement details
    },
    "activities": [
      // Learning activities
    ],
    "assessments": [
      // Assessment details
    ],
    "entitlements": [
      // Optional entitlements
    ]
  }
}
```

## Core Components and Mandatory Elements

### 1. Organisation (Issuer)

The issuing organisation must include:

| Element | Description | ELM Mapping |
|---------|-------------|-------------|
| Legal Name | Full legal name of the issuing university | `issuer.legalName` |
| Accreditation | Accreditation details of the institution | `issuer.accreditation` with `title`, `accreditingAgent`, and `dcType` |
| Location | Country of the registered office (minimum) | `issuer.location.address.countryCode` |

### 2. Credential Information

Basic information about the credential:

| Element | Description | ELM Mapping |
|---------|-------------|-------------|
| Title | Must include "University microcredential in [name]" | `displayParameter.title` |
| Type | "Generic" or "Accredited" | `credentialProfiles` |
| Valid From | Date of credential issuance | `validFrom` |
| Accreditation | Internal quality assurance details | Referenced in credential metadata |

### 3. Achievement

The main achievement represented by the microcredential:

| Element | Description | ELM Mapping |
|---------|-------------|-------------|
| Title | Name reflecting the objective of the learning experience | `credentialSubject.achievement.title` |
| Awarded By | Same as the issuing organisation | `credentialSubject.achievement.awardedBy.awardingBody` |
| Credit System | Must specify ECTS | `credentialSubject.achievement.creditPoint.framework` |
| ECTS Credits | Total credits awarded | `credentialSubject.achievement.creditPoint.point` |
| Thematic Area | ISCED-F classification | `credentialSubject.achievement.thematicArea` |
| Learning Mode | Face-to-face, online, or hybrid | `credentialSubject.achievement.mode` |
| Language | Primary language of instruction | `credentialSubject.achievement.language` |
| Target Group | Predefined categories | `credentialSubject.achievement.targetGroup` |
| Learning Environment | Typically "formal" | `credentialSubject.achievement.learningSetting` |
| EQF Level | European Qualifications Framework level (5-8) | `credentialSubject.achievement.eqfLevel` |

### 4. Learning Outcomes

Each microcredential must specify learning outcomes:

| Element | Description | ELM Mapping |
|---------|-------------|-------------|
| Title | Clear, measurable statement | `credentialSubject.achievement.learningOutcome[].title` |
| Type | "Skill" or "Knowledge" | `credentialSubject.achievement.learningOutcome[].dcType` |
| Related Skills | At least one ESCO competency | `credentialSubject.achievement.learningOutcome[].relatedESCOSkill` |

### 5. Activities

Learning activities associated with the microcredential:

| Element | Description | ELM Mapping |
|---------|-------------|-------------|
| Title | Title of the activity | `credentialSubject.activities[].title` |
| Granted By | Issuing university | `credentialSubject.activities[].directedBy` |
| Workload | Hours (25 hours = 1 ECTS) | `credentialSubject.activities[].workload` |

### 6. Assessment

Assessment methods used to evaluate achievement:

| Element | Description | ELM Mapping |
|---------|-------------|-------------|
| Name | Name of the assessment | `credentialSubject.assessments[].title` |
| Awarded By | Issuing institution | `credentialSubject.assessments[].assessedBy` |
| Identity Verification | Required for virtual/remote assessments | `credentialSubject.assessments[].idVerification` |
| Type | Practical or final assessment | `credentialSubject.assessments[].dcType` |
| Mode | On-site, hybrid, or online | `credentialSubject.assessments[].mode` |
| Grading System | Standardised options | `credentialSubject.assessments[].grade` |

### 7. Entitlement (if applicable)

Rights granted by the microcredential:

| Element | Description | ELM Mapping |
|---------|-------------|-------------|
| Title | Name of the entitlement | `credentialSubject.entitlements[].title` |
| Awarded By | Certifying institution | `credentialSubject.entitlements[].awardedBy` |
| State | "Active" or "Prospective" | `credentialSubject.entitlements[].entitlementStatus` |

## Optional Elements

The schema supports additional optional elements for all components:

### Credential Optional Elements

| Element | Description | ELM Mapping |
|---------|-------------|-------------|
| Organisers | Collaborating entities | Additional `issuer` information |
| Expiry Date | Date when credential expires | `expirationDate` |
| Description | Summary of learning objectives | `displayParameter.description` |
| Course Edition | Label for specific offering | Custom attribute |
| ECTS Label | Credit details as metadata | Included in credential metadata |

### Achievement Optional Elements

| Element | Description | ELM Mapping |
|---------|-------------|-------------|
| Description | Text describing what was achieved | `credentialSubject.achievement.description` |
| Award Date | When achievement was awarded | `credentialSubject.achievement.awardedBy.awardingDate` |
| Learning Volume | Workload in hours | `credentialSubject.achievement.volumeOfLearning` |
| Maximum Duration | Course duration in months | `credentialSubject.achievement.maximumDuration` |
| Learning Opportunity Type | Type classification | `credentialSubject.achievement.dcType` |

### Learning Outcomes Optional Elements

| Element | Description | ELM Mapping |
|---------|-------------|-------------|
| Level of Reuse | Categorization of transferability | `credentialSubject.achievement.learningOutcome[].reusabilityLevel` |
| Related Capabilities | Non-ESCO frameworks | `credentialSubject.achievement.learningOutcome[].relatedSkill` |
| Short Label | Identifier for searchability | `credentialSubject.achievement.learningOutcome[].alternativeLabel` |

### Activities Optional Elements

| Element | Description | ELM Mapping |
|---------|-------------|-------------|
| Directed By | University department or external entity | `credentialSubject.activities[].directedBy` (detailed) |
| Description | Descriptive text | `credentialSubject.activities[].description` |
| Start/End Date | Temporal period | `credentialSubject.activities[].temporal` |
| Completion Percentage | Degree completed | `credentialSubject.activities[].levelOfCompletion` |
| Activity Type | Categorization | `credentialSubject.activities[].dcType` |
| Location | Where activity took place | `credentialSubject.activities[].location` |
| Sub-activities | Component activities | `credentialSubject.activities[].hasPart` |

### Assessment Optional Elements

| Element | Description | ELM Mapping |
|---------|-------------|-------------|
| Description | Explanation of assessment method | `credentialSubject.assessments[].description` |

### Entitlement Optional Elements

| Element | Description | ELM Mapping |
|---------|-------------|-------------|
| Description | Descriptive text | `credentialSubject.entitlements[].description` |
| Type of Duties | Categorization | `credentialSubject.entitlements[].dcType` |
| Valid Jurisdictions | Where entitlement applies | `credentialSubject.entitlements[].limitJurisdiction` |

## Implementation Using ELM v3.2

The Microcredential schema leverages the ELM v3.2 data model by:

1. Using the `EuropeanDigitalCredential` type with additional `UniversityMicrocredential` type
2. Structuring learning outcomes according to the ELM's LearningOutcome component
3. Implementing the credential-achievement-activity-assessment pattern from ELM
4. Leveraging ELM's support for multi-language content
5. Using standard identifiers from European frameworks (ISCED-F, EQF, ESCO)

## Example (Partial)

```json
{
  "@context": [
    "https://www.w3.org/2018/credentials/v1",
    "https://europa.eu/2022/credentials/microcredential/v1"
  ],
  "id": "urn:uuid:3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "type": ["VerifiableCredential", "EuropeanDigitalCredential", "UniversityMicrocredential"],
  "issuer": {
    "id": "did:ebsi:zqpV2ER2HpKT1SraiKrfgd",
    "type": "Organisation",
    "legalName": {
      "en": "University of Madrid"
    },
    "location": {
      "address": {
        "countryCode": {
          "type": "Concept",
          "notation": "ES"
        }
      }
    },
    "accreditation": [{
      "title": {
        "en": "Official University Recognition"
      },
      "accreditingAgent": {
        "id": "https://eqar.eu/institutions/12345",
        "type": "Organisation",
        "legalName": {
          "en": "Ministry of Universities"
        }
      },
      "dcType": {
        "id": "http://data.europa.eu/snb/accreditation/institutional"
      }
    }]
  },
  "credentialSubject": {
    "id": "did:ebsi:zfk5F9MbPyJxp9pFLdDjKL",
    "achievement": {
      "type": "LearningAchievement",
      "title": {
        "en": "University microcredential in Data Science Fundamentals"
      },
      "creditPoint": {
        "framework": {
          "type": "Concept",
          "id": "http://data.europa.eu/snb/credit/ects"
        },
        "point": "5"
      },
      "eqfLevel": {
        "type": "Concept",
        "id": "http://data.europa.eu/snb/eqf/6"
      },
      "thematicArea": {
        "type": "Concept",
        "id": "http://data.europa.eu/snb/isced-f/0613"
      },
      "mode": {
        "type": "Concept",
        "id": "http://data.europa.eu/snb/learning-mode/online"
      },
      "language": {
        "type": "Concept",
        "notation": "en"
      },
      "learningSetting": {
        "type": "Concept",
        "id": "http://data.europa.eu/snb/learning-setting/formal"
      },
      "learningOutcome": [
        {
          "type": "LearningOutcome",
          "title": {
            "en": "Apply basic statistical methods to analyze datasets"
          },
          "dcType": {
            "type": "Concept",
            "id": "http://data.europa.eu/snb/learning-outcome/skill"
          },
          "relatedESCOSkill": {
            "type": "Concept",
            "id": "http://data.europa.eu/esco/skill/21523"
          }
        }
      ]
    }
  }
}
```

## Versioning and Compatibility

The Microcredential schema follows the versioning pattern of ELM v3.2:
- Major versions for breaking changes
- Minor versions for feature additions
- Patch versions for corrections

Current version: 1.0.0 (aligned with ELM v3.2)

## References

- European Learning Model (ELM) v3.2
- Council of the EU Recommendation on Microcredentials (2022)
- European Digital Credentials for Learning (EDC) framework
- W3C Verifiable Credentials Data Model
- ESCO (European Skills, Competences, Qualifications and Occupations) framework
- European Qualifications Framework (EQF)
- International Standard Classification of Education (ISCED-F)
