# The European VET Microcredential (EUVETMC) JSON Schema

The EUVETMC JSON Schema defines the structure and constraints for issuing verifiable microcredentials in VET, based on ELM 3.2 and EBSI Verifiable Credentials. It aligns with EUHEMC but adapts to VET contexts (e.g., ECVET, EQAVET).

## Key Notes
- Enforces mandatory ELM elements and EUVETMC requirements (e.g., 1–15 ECVET, EQAVET quality assurance).
- Designed for EBSI’s JSON-LD Verifiable Credentials, ensuring interoperability.
- Comments clarify mandatory fields per Council Recommendation (Annex I).

## Schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "European VET Microcredential (EUVETMC)",
  "type": "object",
  "allOf": [
    { "$ref": "#/$defs/EuropeanDigitalCredentialType" },
    {
      "type": "object",
      "properties": {
        "issuerCountry": {
          "$ref": "#/$defs/ConceptType",
          "//": "Mandatory (Annex I): Country of issuer, e.g., Croatia."
        },
        "qualityAssurance": {
          "$ref": "#/$defs/ConceptType",
          "//": "Mandatory (Annex I): EQAVET-compliant quality assurance."
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
          "minItems": 1
        },
        "level": {
          "$ref": "#/$defs/ConceptType",
          "//": "Mandatory (Annex I): EQF level, e.g., EQF Level 4."
        },
        "learningSetting": {
          "$ref": "#/$defs/ConceptType",
          "//": "Mandatory (Annex I): Setting, e.g., Work-based."
        },
        "stackability": {
          "$ref": "#/$defs/ConceptType",
          "//": "Optional (Annex I): Stackable toward qualification."
        },
        "learningOutcome": {
          "type": "array",
          "items": { "$ref": "#/$defs/LearningOutcomeType" },
          "minItems": 1
        },
        "awardedBy": { "$ref": "#/$defs/AwardingProcessType" }
      },
      "required": ["id", "type", "title", "creditReceived", "level", "learningSetting", "learningOutcome", "awardedBy"]
    },
    "LearningAssessmentType": {
      "type": "object",
      "properties": {
        "id": { "$ref": "#/$defs/GenericIdType" },
        "type": { "const": "LearningAssessment" },
        "title": { "$ref": "#/$defs/Many!LangStringType" },
        "assessmentType": {
          "$ref": "#/$defs/ConceptType",
          "//": "Mandatory (Annex I): Type, e.g., Practical Test."
        },
        "grade": { "$ref": "#/$defs/NoteType" },
        "awardedBy": { "$ref": "#/$defs/AwardingProcessType" }
      },
      "required": ["id", "type", "title", "assessmentType", "grade", "awardedBy"]
    }
  }
}
```