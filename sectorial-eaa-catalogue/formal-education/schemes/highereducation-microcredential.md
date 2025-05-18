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
    }
    // Other definitions (PersonType, ConceptType, etc.) remain unchanged
  }
}
```