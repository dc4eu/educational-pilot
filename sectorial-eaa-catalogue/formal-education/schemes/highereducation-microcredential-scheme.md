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
  "title": "European Higher Education Microcredential",
  "description": "Subschema for Verifiable Credentials representing microcredentials issued in Higher Education, based on EDC-W3C-VC and ELM 3.2",
  "type": "object",
  "allOf": [
    {
      "$ref": "https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/0x411a2c5880fe8bd97229546044f55b65846d272594511815cd5b89f000dc3da7"
    },
    {
      "type": "object",
      "properties": {
        "type": {
          "type": "array",
          "contains": {
            "const": "EuropeanHigherEducationMicrocredential"
          }
        },
        "credentialSubject": {
          "type": "object",
          "required": [
            "id",
            "type",
            "dateOfBirth",
            "familyName",
            "givenName",
            "hasClaim"
          ],
          "properties": {
            "hasClaim": {
              "type": "array",
              "minItems": 1,
              "items": {
                "type": "object",
                "required": [
                  "type",
                  "title",
                  "awardedBy",
                  "specifiedBy",
                  "provenBy"
                ],
                "properties": {
                  "type": {
                    "type": "array",
                    "contains": {
                      "const": "LearningAchievement"
                    }
                  },
                  "creditReceived": {
                    "type": "array",
                    "minItems": 1,
                    "maxItems": 3,
                    "items": {
                      "type": "object",
                      "required": [
                        "framework",
                        "point"
                      ],
                      "properties": {
                        "framework": {
                          "type": "object",
                          "properties": {
                            "notation": {
                              "enum": [
                                "ECTS"
                              ]
                            }
                          },
                          "required": [
                            "notation"
                          ]
                        },
                        "point": {
                          "type": "string",
                          "pattern": "^(1[0-5]|[1-9])$"
                        }
                      }
                    }
                  },
                  "provenBy": {
                    "type": "array",
                    "minItems": 1,
                    "items": {
                      "type": "object",
                      "required": [
                        "grade",
                        "specifiedBy",
                        "awardedBy"
                      ]
                    }
                  },
                  "specifiedBy": {
                    "type": "object",
                    "required": [
                      "creditPoint",
                      "educationSubject",
                      "mode",
                      "eqfLevel"
                    ],
                    "properties": {
                      "creditPoint": {
                        "type": "array",
                        "minItems": 1
                      },
                      "eqfLevel": {
                        "type": "object",
                        "required": [
                          "notation"
                        ],
                        "properties": {
                          "notation": {
                            "type": "string"
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  ],
  "$id": "https://tsr.ebsi.europa.eu/schemas/euhe-microcredential.schema.json"
}
```