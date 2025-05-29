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
  "$id": "https://tsr.ebsi.europa.eu/schemas/euvet-microcredential.schema.json",
  "title": "European Vocational Education and Training Microcredential",
  "description": "Profile schema extending the base EDC-W3C-VC to define microcredentials issued by vocational education and training institutions in Europe.",
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
            "const": "EuropeanVocationalEducationTrainingMicrocredential"
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
                                "ECVET"
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
  ]
}
```