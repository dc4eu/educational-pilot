# The European Higher Education Microcredential (EUHEMC) JSON Schema

The European Higher Education Microcredential (EUHEMC) JSON Schema defines the structure and constraints for issuing verifiable microcredentials based on the European Learning Model (ELM) 3.2 and EBSI Verifiable Credentials. Below is the schema, annotated with comments to highlight mandatory ELM elements and EUHEMC-specific requirements.


## Key Notes

The schema enforces mandatory ELM elements (e.g., PersonType, LearningAchievementType, LearningAssessmentType) and EUHEMC-specific requirements (e.g., 1–15 ECTS, at least one competence).
Comments (//) clarify which fields are mandatory and why, aiding developers in implementation and validation.
The schema is designed for use with EBSI’s JSON-LD Verifiable Credentials, ensuring interoperability and security.

## Schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "European Higher Education Microcredential (EUHEMC)",
  "type": "object",
  "allOf": [
    { "$ref": "#/$defs/EuropeanDigitalCredentialType" },
    {
      "type": "object",
      "properties": {
        "issuerCountry": {
          "$ref": "#/$defs/ConceptType",
          "//": "Mandatory (Annex I): Country/region of the issuer, e.g., Spain."
        },
        "qualityAssurance": {
          "$ref": "#/$defs/ConceptType",
          "//": "Mandatory (Annex I): Type of quality assurance, e.g., ESG-compliant."
        },
        "credentialSubject": {
          "type": "object",
          "allOf": [
            { "$ref": "#/$defs/PersonType" },
            {
              "properties": {
                "hasClaim": {
                  "type": "array",
                  "items": { "$ref": "#/$defs/ClaimNodeType" },
                  "minItems": 2,
                  "contains": [
                    { "$ref": "#/$defs/LearningAchievementType" },
                    { "$ref": "#/$defs/LearningAssessmentType" }
                  ]
                }
              }
            }
          ]
        }
      },
      "required": ["issuerCountry", "qualityAssurance", "credentialSubject"]
    }
  ],
  "$defs": {
    "LearningAchievementType": {
      "type": "object",
      "properties": {
        "id": { "$ref": "#/$defs/GenericIdType" },
        "type": { "const": "LearningAchievement" },
        "title": { "$ref": "#/$defs/Many!LangStringType" },
        "creditReceived": {
          "type": "array",
          "items": { "$ref": "#/$defs/CreditPointType" },
          "minItems": 1,
          "maxItems": 1
        },
        "level": {
          "$ref": "#/$defs/ConceptType",
          "//": "Mandatory (Annex I): EQF/QF-EHEA level, e.g., EQF Level 6."
        },
        "participationForm": {
          "$ref": "#/$defs/ConceptType",
          "//": "Mandatory (Annex I): Form of participation, e.g., Online, In-person."
        },
        "stackability": {
          "$ref": "#/$defs/ConceptType",
          "//": "Optional (Annex I): Indicates stackability, e.g., Stackable towards degree."
        },
        "learningOutcome": {
          "type": "array",
          "items": { "$ref": "#/$defs/LearningOutcomeType" },
          "minItems": 1
        },
        "awardedBy": { "$ref": "#/$defs/AwardingProcessType" }
      },
      "required": ["id", "type", "title", "creditReceived", "level", "participationForm", "learningOutcome", "awardedBy"]
    },
    "LearningAssessmentType": {
      "type": "object",
      "properties": {
        "id": { "$ref": "#/$defs/GenericIdType" },
        "type": { "const": "LearningAssessment" },
        "title": { "$ref": "#/$defs/Many!LangStringType" },
        "assessmentType": {
          "$ref": "#/$defs/ConceptType",
          "//": "Mandatory (Annex I): Type of assessment, e.g., Written Exam."
        },
        "grade": { "$ref": "#/$defs/NoteType" },
        "awardedBy": { "$ref": "#/$defs/AwardingProcessType" }
      },
      "required": ["id", "type", "title", "assessmentType", "grade", "awardedBy"]
    },
    "PersonType": {
      "type": "object",
      "properties": {
        "id": { "$ref": "#/$defs/GenericIdType" },
        "type": { "const": "Person" },
        "fullName": { "$ref": "#/$defs/Many!LangStringType" },
        "givenName": { "$ref": "#/$defs/Many!LangStringType" },
        "familyName": { "$ref": "#/$defs/Many!LangStringType" },
        "nationalID": {
          "type": "object",
          "properties": {
            "id": { "$ref": "#/$defs/GenericIdType" },
            "type": { "const": "LegalIdentifier" },
            "notation": { "type": "string" },
            "spatial": { "$ref": "#/$defs/ConceptType" }
          },
          "required": ["id", "type", "notation", "spatial"]
        }
      },
      "required": ["id", "type", "fullName", "givenName", "familyName"]
    },
    "ConceptType": {
      "type": "object",
      "properties": {
        "id": { "$ref": "#/$defs/GenericIdType" },
        "type": { "const": "Concept" },
        "prefLabel": { "$ref": "#/$defs/Many!LangStringType" }
      },
      "required": ["id", "type", "prefLabel"]
    },
    "EuropeanDigitalCredentialType": {
      "type": "object",
      "properties": {
        "@context": {
          "type": "array",
          "items": { "type": "string" },
          "minItems": 2,
          "contains": [
            { "const": "https://www.w3.org/2018/credentials/v1" },
            { "const": "https://w3id.org/edc/v1" }
          ]
        },
        "id": { "$ref": "#/$defs/GenericIdType" },
        "type": {
          "type": "array",
          "items": { "type": "string" },
          "minItems": 3,
          "contains": [
            { "const": "VerifiableCredential" },
            { "const": "EuropeanDigitalCredential" },
            { "const": "EuropeanHigherEducationMicroCredentials" }
          ]
        },
        "issuer": {
          "type": "object",
          "properties": {
            "id": { "$ref": "#/$defs/GenericIdType" }
          },
          "required": ["id"]
        },
        "issuanceDate": { "type": "string", "format": "date-time" },
        "issued": { "type": "string", "format": "date-time" },
        "validFrom": { "type": "string", "format": "date-time" },
        "credentialSchema": {
          "type": "object",
          "properties": {
            "id": { "type": "string", "format": "uri" },
            "type": { "const": "JsonSchema" }
          },
          "required": ["id", "type"]
        },
        "displayParameter": {
          "type": "object",
          "properties": {
            "id": { "$ref": "#/$defs/GenericIdType" },
            "type": { "const": "DisplayParameter" },
            "title": { "$ref": "#/$defs/Many!LangStringType" },
            "language": {
              "type": "array",
              "items": { "$ref": "#/$defs/ConceptType" },
              "minItems": 1
            },
            "primaryLanguage": { "$ref": "#/$defs/ConceptType" },
            "individualDisplay": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "id": { "$ref": "#/$defs/GenericIdType" },
                  "type": { "const": "IndividualDisplay" },
                  "fieldPath": { "type": "string" },
                  "label": { "$ref": "#/$defs/Many!LangStringType" },
                  "order": { "type": "integer", "minimum": 1 }
                },
                "required": ["id", "type", "fieldPath", "label", "order"]
              }
            }
          },
          "required": ["id", "type", "title", "language", "primaryLanguage", "individualDisplay"]
        }
      },
      "required": ["@context", "id", "type", "issuer", "issuanceDate", "issued", "validFrom", "credentialSchema", "displayParameter"]
    },
    "GenericIdType": {
      "type": "string",
      "pattern": "^(urn:uuid:[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}|did:ebsi:[a-zA-Z0-9]+|urn:[a-z]+:[a-z]+:.+)$"
    },
    "Many!LangStringType": {
      "type": "object",
      "patternProperties": {
        "^[a-z]{2}$": { "type": "string" }
      },
      "additionalProperties": false,
      "minProperties": 1
    },
    "CreditPointType": {
      "type": "object",
      "properties": {
        "id": { "$ref": "#/$defs/GenericIdType" },
        "type": { "const": "CreditPoint" },
        "framework": { "$ref": "#/$defs/ConceptType" },
        "point": { "type": "string", "pattern": "^[1-9][0-9]*$" }
      },
      "required": ["id", "type", "framework", "point"]
    },
    "LearningOutcomeType": {
      "type": "object",
      "properties": {
        "id": { "$ref": "#/$defs/GenericIdType" },
        "type": { "const": "LearningOutcome" },
        "title": { "$ref": "#/$defs/Many!LangStringType" },
        "relatedCompetence": {
          "type": "array",
          "items": { "$ref": "#/$defs/ConceptType" },
          "minItems": 1
        },
        "relatedESCOSkill": {
          "type": "array",
          "items": { "$ref": "#/$defs/ConceptType" }
        }
      },
      "required": ["id", "type", "title", "relatedCompetence"]
    },
    "AwardingProcessType": {
      "type": "object",
      "properties": {
        "id": { "$ref": "#/$defs/GenericIdType" },
        "type": { "const": "AwardingProcess" },
        "awardingBody": {
          "type": "object",
          "properties": {
            "id": { "$ref": "#/$defs/GenericIdType" },
            "type": { "const": "Organisation" },
            "legalName": { "$ref": "#/$defs/Many!LangStringType" }
          },
          "required": ["id", "type", "legalName"]
        }
      },
      "required": ["id", "type", "awardingBody"]
    },
    "ClaimNodeType": {
      "type": "object",
      "oneOf": [
        { "$ref": "#/$defs/LearningAchievementType" },
        { "$ref": "#/$defs/LearningAssessmentType" }
      ]
    },
    "NoteType": {
      "type": "object",
      "properties": {
        "id": { "$ref": "#/$defs/GenericIdType" },
        "type": { "const": "Note" },
        "noteLiteral": { "$ref": "#/$defs/Many!LangStringType" }
      },
      "required": ["id", "type", "noteLiteral"]
    }
  }
}
```