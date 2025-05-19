# EUVETMC Unsigned Credential Example

- Includes all mandatory EUVETMC elements: learner identification, 5-ECVET learning achievement, assessment with grade, learning outcome with competence, and optional ESCO skill.
- Issued by a VET provider (e.g., Croatian VET Agency, `did:ebsi:vetCroatia123`).
- Quality Assurance: Aligned with EQAVET standards, ensuring trust.
- Stackability: Supports stacking toward VET qualifications, per receiving institutions.
- No proof field, as unsigned.

```json
{
  "@context": [
    "https://www.w3.org/2018/credentials/v1",
    "https://w3id.org/edc/v1"
  ],
  "id": "urn:uuid:9e7c4f8d-1b9a-4e1b-8f2a-7b9c0d5e6d3a",
  "type": [
    "VerifiableCredential",
    "EuropeanDigitalCredential",
    "EuropeanVETMicroCredentials"
  ],
  "issuer": {
    "id": "did:ebsi:vetCroatia123"
  },
  "issuerCountry": {
    "id": "urn:concept:hr",
    "type": "Concept",
    "prefLabel": { "en": "Croatia" }
  },
  "issuanceDate": "2025-05-04T10:00:00Z",
  "issued": "2025-05-04T10:00:00Z",
  "validFrom": "2025-05-04T10:00:00Z",
  "qualityAssurance": {
    "id": "urn:concept:eqavet",
    "type": "Concept",
    "prefLabel": { "en": "EQAVET-compliant" }
  },
  "credentialSubject": {
    "id": "did:ebsi:example:vetstudent456",
    "type": "Person",
    "fullName": { "en": "Ana Kovačić" },
    "givenName": { "en": "Ana" },
    "familyName": { "en": "Kovačić" },
    "nationalID": {
      "id": "urn:legal:hr:OIB:9876543210",
      "type": "LegalIdentifier",
      "notation": "9876543210",
      "spatial": {
        "id": "urn:concept:hr",
        "type": "Concept",
        "prefLabel": { "en": "Croatia" }
      }
    },
    "hasClaim": [
      {
        "id": "urn:uuid:2b3c4d5e-6f7g-8h9i-0j1k-2l3m4n5o6p7q",
        "type": "LearningAchievement",
        "title": { "en": "Renewable Energy Installation" },
        "creditReceived": [
          {
            "id": "urn:uuid:3c4d5e6f-7g8h-9i0j-1k2l-3m4n5o6p7q8r",
            "type": "CreditPoint",
            "framework": {
              "id": "urn:concept:ECVET",
              "type": "Concept",
              "prefLabel": { "en": "ECVET" }
            },
            "point": "5"
          }
        ],
        "level": {
          "id": "urn:concept:eqf4",
          "type": "Concept",
          "prefLabel": { "en": "EQF Level 4" }
        },
        "learningSetting": {
          "id": "urn:concept:work-based",
          "type": "Concept",
          "prefLabel": { "en": "Work-based" }
        },
        "stackability": {
          "id": "urn:concept:stackable",
          "type": "Concept",
          "prefLabel": { "en": "Stackable toward VET qualification" }
        },
        "learningOutcome": [
          {
            "id": "urn:uuid:4d5e6f7g-8h9i-0j1k-2l3m-4n5o6p7q8r9s",
            "type": "LearningOutcome",
            "title": { "en": "Ability to install solar panels" },
            "relatedCompetence": [
              {
                "id": "urn:concept:solar-installation",
                "type": "Concept",
                "prefLabel": { "en": "Solar Panel Installation" }
              }
            ],
            "relatedESCOSkill": [
              {
                "id": "http://data.europa.eu/esco/skill/67890",
                "type": "Concept",
                "prefLabel": { "en": "Renewable Energy Systems" }
              }
            ]
          }
        ],
        "awardedBy": {
          "id": "urn:uuid:award-1",
          "type": "AwardingProcess",
          "awardingBody": {
            "id": "did:ebsi:vetCroatia123",
            "type": "Organisation",
            "legalName": { "en": "Agency for VET and Adult Education" }
          }
        }
      },
      {
        "id": "urn:uuid:5e6f7g8h-9i0j-1k2l-3m4n-5o6p7q8r9s0t",
        "type": "LearningAssessment",
        "title": { "en": "Solar Installation Practical Test" },
        "assessmentType": {
          "id": "urn:concept:practical",
          "type": "Concept",
          "prefLabel": { "en": "Practical Test" }
        },
        "grade": {
          "id": "urn:uuid:6f7g8h9i-0j1k-2l3m-4n5o-6p7q8r9s0t1u",
          "type": "Note",
          "noteLiteral": { "en": "90/100" }
        },
        "awardedBy": {
          "id": "urn:uuid:award-2",
          "type": "AwardingProcess",
          "awardingBody": {
            "id": "did:ebsi:vetCroatia123",
            "type": "Organisation",
            "legalName": { "en": "Agency for VET and Adult Education" }
          }
        }
      }
    ]
  },
  "credentialSchema": {
    "id": "https://trusted-registries.ebsi.eu/schemas/euvetmc/1.0",
    "type": "JsonSchema"
  },
  "displayParameter": {
    "id": "urn:uuid:7g8h9i0j-1k2l-3m4n-5o6p-7q8r9s0t1u2v",
    "type": "DisplayParameter",
    "title": { "en": "EUVETMC Display" },
    "language": [
      {
        "id": "urn:concept:en",
        "type": "Concept",
        "prefLabel": { "en": "English" }
      }
    ],
    "primaryLanguage": {
      "id": "urn:concept:en",
      "type": "Concept",
      "prefLabel": { "en": "English" }
    },
    "individualDisplay": [
      {
        "id": "urn:uuid:8h9i0j1k-2l3m-4n5o-6p7q-8r9s0t1u2v3w",
        "type": "IndividualDisplay",
        "fieldPath": "credentialSubject.fullName",
        "label": { "en": "Full Name" },
        "order": 1
      },
      {
        "id": "urn:uuid:9i0j1k2l-3m4n-5o6p-7q8r-9s0t1u2v3w4x",
        "type": "IndividualDisplay",
        "fieldPath": "credentialSubject.hasClaim[0].title",
        "label": { "en": "Achievement Title" },
        "order": 2
      }
    ]
  }
}
```