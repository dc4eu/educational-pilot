# Professional and sectorial training certificate Schema

## Overview

The training certificate schema defines the data structure for representing training activities carreid out by any professional.

## Schema Structure

```json
{
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://eaa-rulebook.europa.eu/schemas/trainingCert/0.0.1",
    "title": "Professional Training Certificate",
    "description": "Schema for professional and sectorial training certificates",
    "type": "object",
    "properties": {
      "@context": {
        "type": "array",
        "description": "JSON-LD context",
        "items": {
          "type": "string"
        },
        "default": [
          "https://www.w3.org/2018/credentials/v1",
          "https://eaa-rulebook.europa.eu/2023/credentials/professionalTrainingCert/v01"
        ]
      },
      "id": {
        "type": "string",
        "format": "uri",
        "description": "Unique identifier for the training credential"
      },
      "type": {
        "type": "array",
        "description": "Credential type definitions",
        "items": {
          "type": "string"
        },
        "default": ["VerifiableCredential", "ProfessionalTrainingCredential"]
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
          "vatIdentifier": {
            "type": "object",
            "description": "VAT number of the issuing institution",
            "properties":{
              "type": {
                "const": "LegalIdentifier"
              },
              "notation": {
                "type": "string",
                "description": "VAT Number"
              }
            }
          },
          "legalName": {
            "type": "object",
            "description": "Multilingual name of the issuing institution",
            "additionalProperties": {
              "type": "string"
            }
          },
          "accreditation": {
            "type": "array",
            "description": "Accreditation information",
            "items": {
              "type": "object",
              "properties": {
                "accreditationBody": {
                  "type": "string",
                  "description": "Name of the accreditation body"
                },
                "accreditationId": {
                  "type": "string",
                  "description": "Identifier of the accreditation"
                },
                "accreditationDate": {
                  "type": "string",
                  "format": "date",
                  "description": "Date of accreditation"
                },
                "validUntil": {
                  "type": "string",
                  "format": "date",
                  "description": "Accreditation validity end date"
                }
              },
              "required": ["accreditationBody", "accreditationId"]
            }
          }
        },
        "required": ["id", "name"]
      },
      "issuanceDate": {
        "type": "string",
        "format": "date",
        "description": "Date when the credential was issued"
      },
      "credentialSubject": {
        "type": "object",
        "description": "Information about the graduate and qualification",
        "properties": {
          "id": {
            "type": "string",
            "format": "uri",
            "description": "Identifier of the credential subject"
          },
          "givenName": {
            "type": "string",
            "description": "Current first name(s), including middle name(s) where applicable, of the user to whom the person identification data relates."
          },
          "familyName": {
            "type": "string",
            "description": "Current last name(s) or surname(s) of the user to whom the person identification data relates."
          },
          "qualification": {
            "type": "object",
            "description": "Details about the qualification achieved",
            "properties": {
              "title": {
                "type": "object",
                "description": "Multilingual name of the qualification",
                "additionalProperties": {
                  "type": "string"
                }
              },
              "level": {
                "type": "object",
                "description": "Qualification level information",
                "properties": {
                  "eqfLevel": {
                    "type": "integer",
                    "minimum": 1,
                    "maximum": 8,
                    "description": "European Qualifications Framework level"
                  },
                  "nqfLevel": {
                    "type": "string",
                    "description": "National Qualifications Framework level"
                  }
                },
                "required": ["eqfLevel"]
              },
              "fieldOfStudy": {
                "type": "object",
                "description": "Field of study information",
                "properties": {
                  "name": {
                    "type": "object",
                    "description": "Multilingual name of the field of study",
                    "additionalProperties": {
                      "type": "string"
                    }
                  }
                },
                "required": ["name"]
              },
              "trainingAwarded": {
                "type": "object",
                "description": "Multilingual name of the training awarded",
                "additionalProperties": {
                  "type": "string"
                }
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
              "sponsor": {
                  "type": "string",
                  "description": "An entity, other than the training provider, that collaborates in the development of the activity, either by providing funding, resources, promotion or public endorsement. They are not involved in the training provision or in the writing of the material."
              },
              "partner": {
                "type": "string",
                "description": "Entity involved in the provision of the training or in the drafting of the material."
              },
              "entryRequirement": {
                "type": "object",
                "description": "Specific entry requirements or prerequisites of individuals for which this specification is designed to start this learning opportunity",
                "properties": {
                  "id": {
                    "type": "string",
                    "format": "uri"
                  },
                  "type":{
                    "const": "Note"
                  },
                  "noteLiteral": {
                    "type": "object",
                    "additionalProperties": {
                      "type": "string"
                    }
                  }
                },
                "required": ["noteLiteral"]
              },
              "learningOutcomes": { 
                "type": "array",
                "description": "Learning outcomes achieved",
                "items": {
                  "type": "object",
                  "properties": {
                    "category": {
                      "type": "string",
                      "enum": ["knowledge", "skills", "competence"],
                      "description": "Category of learning outcome"
                    },
                    "description": {
                      "type": "object",
                      "description": "Multilingual description of the learning outcome",
                      "additionalProperties": {
                        "type": "string"
                      }
                    }
                  },
                  "required": ["category", "description"]
                }
              }
            }
          },
          "required": ["title", "trainingAwarded"]
        },
        "required": ["givenName", "qualification"]
      },
      "proof": {
        "type": "object",
        "description": "Cryptographic proof of the credential",
        "properties": {
          "type": {
            "type": "string",
            "description": "Type of proof"
          },
          "created": {
            "type": "string",
            "format": "date-time",
            "description": "Date and time when the proof was created"
          },
          "proofPurpose": {
            "type": "string",
            "description": "Purpose of the proof"
          },
          "verificationMethod": {
            "type": "string",
            "format": "uri",
            "description": "Method used to verify the proof"
          },
          "proofValue": {
            "type": "string",
            "description": "Value of the proof"
          }
        },
        "required": ["type", "created", "proofPurpose", "verificationMethod", "proofValue"]
      },
    "required": ["@context", "id", "type", "issuer", "issuanceDate", "credentialSubject", "proof"]
  }
}
```

## Example Credential

[Professional Training Certificate example](./examples/ProfessionalTrainingCertificate.json)

## Schema Versioning

- **Version**: 0.0.1
- **Last Updated**: 2025-04-04
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
