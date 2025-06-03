# Accreditation Medical Training Schema

## Overview

JSON Schema.... (TBC)

## Schema Structure

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://eaa-rulebook.europa.eu/schemas/seaformec/0.0.1",
  "title": "EBSI Medical Verifiable Accreditation training",
  "description": "EBSI Medical Verifiable Accreditation training schema for accrediting continuous medical education programmes",
  "type": "object",
  "properties" : {
    "@context": {
      "type": "array",
      "description": "JSON-LD context",
      "items": {
        "type": "string"
      },
      "default": [
        "https://www.w3.org/2018/credentials/v1",
        "https://eaa-rulebook.europa.eu/2023/credentials/seaformec/v01"
      ]
    },
    "id": {
      "type": "string",
      "format": "uri",
      "description": "Unique identifier for the doctor ID credential"
    },
    "type": {
      "type": "array",
      "description": "Credential type definitions",
      "items": {
        "type": "string"
      },
      "default": ["VerifiableCredential", "ContinuousMedicalTrainingAccreditation"]
    },
    "issuer": {
      "type": "object",
      "description": "Information about the issuing institution",
      "properties": {
        "id": {
          "type": "string",
          "format": "uri",
          "description": "Unique identifier of the issuing institution"
        },
        "legalName": {
          "type": "object",
          "description": "Multilingual name of the issuing institution",
          "additionalProperties": {
            "type": "string"
          }
        },
        "issuing_country": {
          "type": "string",
          "description": "Country of the issuing institution"
        }
      },
      "required": ["id", "legalName", "issuing_country"]
    },
    "issuanceDate": {
      "type": "string",
      "format": "date",
      "description": "Date when the doctor ID was issued"
    },
    "expirationDate": {
      "type": "string",
      "format": "date",
      "description": "Date when the eCIP expires"
    },
    "credentialSubject": {
      "type": "object",
      "properties": {
        "id": {
          "description": "Defines a unique identifier of the Verifiable attestation",
          "type": "string"
        },
        "authorizationClaims": {
          "description": "Defines a list of claims that define/determine the authorization of an Issuer to issue certain types of VCs. Mandatory",
          "type": "object",
          "properties": {
            "accreditationType": {
              "description": "Defines the type of accreditation. Mandatory*",
              "type": "string",
              "format": "uri"
            },
            "report": {
              "description": "Includes an accessible report of the quality assurance decision",
              "type": "array",
              "items": {
                "type": "string",
                "format": "uri"
              }
            },
            "accreditingAgent": {
              "type": "object",
              "description": "Information about the accrediting institution",
              "properties": {
                "id": {
                  "type": "string",
                  "format": "uri",
                  "description": "Unique identifier of the accrediting institution"
                },
                "name": {
                  "type": "object",
                  "description": "Multilingual name of the accrediting institution",
                  "additionalProperties": {
                    "type": "string"
                  }
                }
              },
              "required": ["id", "name"]
            },
            "limitQualification": {
              "description": " Defines The qualification that was accredited ",
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "id": {
                    "description": "Defines a portable and unique identifier of the qualification",
                    "type": "string",
                    "format": "uri"
                  },
                  "title": {
                    "description": "Defines the title of the qualification",
                    "type": "string"
                  },
                  "alternativeLabel": {
                    "description": "Defines an alternative name of the qualification",
                    "type": "array",
                    "items": {
                      "type": "string"
                    }
                  },
                  "EQFLevel": {
                    "description": "Defines the qualification level as specified by the European Qualification Framework.",
                    "type": "string",
                    "format": "uri"
                  },
                  "NQFLevel": {
                    "description": "Defines the qualification level as specified by a National Qualification Framework.",
                    "type": "string",
                    "format": "uri"
                  },
                  "trainingDuration": {
                    "type": "object",
                    "description": "Duration of the study programme",
                    "properties": {
                      "startDate": {
                        "type": "string",
                        "format": "date",
                        "description": "Start date of training activity"
                      },
                      "endDate": {
                        "type": "string",
                        "format": "date",
                        "description": "End date of training activity"
                      }
                    }
                  },
                  "volumeOfLearning": {
                    "type": "string",
                    "format": "duration",
                    "description": "The estimated number of hours the learner is expected to spend engaged in learning to earn the award."
                  },
                  "mode": {
                    "type": "array",
                    "description": "The mode of learning and or assessment",
                    "items": {
                      "type": "object",
                      "properties": {
                        "id": {
                            "type": "string",
                            "format" : "uri"
                        },
                        "type": {
                          "const": "Concept"
                        },
                        "inScheme": {
                          "type": "object",
                          "properties": {
                            "id": {
                              "type": "string",
                              "format": "uri"
                            },
                            "type": {
                              "const": "ConceptScheme"
                            }
                          }
                        },
                        "prefLabel": {
                          "type": "object",
                          "properties": {
                            "category": {
                              "type": "string",
                              "enum": ["Presential", "Online", "Hybrid"]
                            }
                          }
                        }
                      },
                      "required": ["id", "type", "inScheme", "prefLabel"]
                    }
                  },
                  "creditPoint": {
                    "type": "array",
                    "description": "The credit points assigned to the learning specification.",
                    "items": {
                      "type": "object",
                      "properties": {
                        "id": {
                          "type": "string",
                          "format": "uri"
                        },
                        "type": {
                          "const": "CreditPoint"
                        },
                        "framework": {
                          "type": "object",
                          "properties": {
                            "id": {
                              "type": "string",
                              "format": "uri"
                            },
                            "type": {
                              "const": "Concept"
                            },
                            "prefLabel": {
                              "type": "object",
                              "additionalProperties": {
                                "type": "string"
                              }
                            },
                            "inScheme": {
                              "properties": {
                                "id": {
                                  "type": "string",
                                  "format": "uri"
                                },
                                "type": {
                                  "const": "ConceptScheme"
                                }
                              }
                            }
                          }
                        },
                        "point": {
                          "type": "string"
                        }
                      },
                      "required": ["id", "type", "framework", "point"]
                    }      
                  },
                  "limitQFLevel": {
                    "description": "Defines the european qualification level for which the accreditation is valid",
                    "type": "array",
                    "items": {
                      "type": "string",
                      "format": "uri"
                    }
                  },
                  "limitJurisdiction": {
                    "description": "Defines the jurisdiction for which the accreditation is valid",
                    "type": "array",
                    "items": {
                      "type": "string",
                      "format": "uri"
                    }
                  },
                  "reviewDate": {
                    "description": "Defines the The date when the accreditation has to be re-viewed",
                    "type": "string",
                    "format": "date-time"
                  }
                },
                "required": ["accreditationType", "limitJurisdiction"]
              }
            },
            "required": ["id", "authorizationClaims"]
          }
        }
      }
    }
  }
}
```

## Example credential

[Accreditation Medical Training - SEAFORMEC/UEMS example](./examples/AccreditationMedicalTraining_SEAFORMEC.json)

## Schema Versioning

- **Version**: 0.0.1
- **Last Updated**: 2025-05-02
- **Status**: Draft

## Implementation Considerations

When implementing this schema:

- Ensure all required fields are provided
- Support multilingual representation of key information
- Implement appropriate privacy protections for personal information
- Include only necessary personal data
- Use standardised classification systems for medical specialities
- Consider selective disclosure requirements for sensitive attributes

## Extensions

The schema can be extended to support:

- Additional institution-specific requirements
