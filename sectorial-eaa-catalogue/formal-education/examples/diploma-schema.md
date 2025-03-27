# Diploma Schema

## Overview

The Diploma Schema defines the data structure for representing formal diplomas, degrees, and qualification certificates issued by recognised educational institutions. This schema supports comprehensive documentation of academic achievements at various levels of education.

## Schema Structure

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://eaa-rulebook.europa.eu/schemas/diploma/1.0.0",
  "title": "Diploma",
  "description": "Schema for educational diplomas and degree certificates",
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
        "https://eaa-rulebook.europa.eu/2023/credentials/diploma/v1"
      ]
    },
    "id": {
      "type": "string",
      "format": "uri",
      "description": "Unique identifier for the diploma credential"
    },
    "type": {
      "type": "array",
      "description": "Credential type definitions",
      "items": {
        "type": "string"
      },
      "default": ["VerifiableCredential", "DiplomaCredential"]
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
        "name": {
          "type": "object",
          "description": "Multilingual name of the issuing institution",
          "additionalProperties": {
            "type": "string"
          }
        },
        "accreditation": {
          "type": "array",
          "description": "Accreditation information for the issuing institution",
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
      "description": "Date when the diploma was issued"
    },
    "expirationDate": {
      "type": "string",
      "format": "date",
      "description": "Date when the diploma expires, if applicable"
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
        "fullName": {
          "type": "string",
          "description": "Full name of the graduate"
        },
        "dateOfBirth": {
          "type": "string",
          "format": "date",
          "description": "Date of birth of the graduate"
        },
        "placeOfBirth": {
          "type": "string",
          "description": "Place of birth of the graduate"
        },
        "qualification": {
          "type": "object",
          "description": "Details about the qualification achieved",
          "properties": {
            "name": {
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
                },
                "isced": {
                  "type": "string",
                  "description": "ISCED classification code"
                }
              },
              "required": ["eqfLevel"]
            },
            "fieldOfStudy": {
              "type": "object",
              "description": "Field of study information",
              "properties": {
                "code": {
                  "type": "string",
                  "description": "Classification code for the field of study"
                },
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
            "degreeAwarded": {
              "type": "object",
              "description": "Multilingual name of the degree awarded",
              "additionalProperties": {
                "type": "string"
              }
            },
            "studyDuration": {
              "type": "object",
              "description": "Duration of the study programme",
              "properties": {
                "years": {
                  "type": "number",
                  "description": "Duration in years"
                },
                "ects": {
                  "type": "number",
                  "description": "Total ECTS credits"
                },
                "startDate": {
                  "type": "string",
                  "format": "date",
                  "description": "Start date of studies"
                },
                "endDate": {
                  "type": "string",
                  "format": "date",
                  "description": "End date of studies"
                }
              }
            },
            "graduationDate": {
              "type": "string",
              "format": "date",
              "description": "Date of graduation"
            },
            "finalResult": {
              "type": "object",
              "description": "Final result information",
              "properties": {
                "grade": {
                  "type": "string",
                  "description": "Final grade achieved"
                },
                "description": {
                  "type": "object",
                  "description": "Multilingual description of the grading system",
                  "additionalProperties": {
                    "type": "string"
                  }
                }
              }
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
            },
            "supplementaryDocument": {
              "type": "object",
              "description": "Reference to a diploma supplement or other supplementary document",
              "properties": {
                "id": {
                  "type": "string",
                  "format": "uri",
                  "description": "Identifier for the supplementary document"
                },
                "type": {
                  "type": "string",
                  "description": "Type of supplementary document"
                },
                "name": {
                  "type": "object",
                  "description": "Multilingual name of the supplementary document",
                  "additionalProperties": {
                    "type": "string"
                  }
                }
              }
            }
          },
          "required": ["name", "level", "degreeAwarded"]
        }
      },
      "required": ["fullName", "qualification"]
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
    }
  },
  "required": ["@context", "id", "type", "issuer", "issuanceDate", "credentialSubject", "proof"]
}
```

## Example Credential

```json
{
  "@context": [
    "https://www.w3.org/2018/credentials/v1",
    "https://eaa-rulebook.europa.eu/2023/credentials/diploma/v1"
  ],
  "id": "https://university-example.eu/credentials/diploma/1234",
  "type": ["VerifiableCredential", "DiplomaCredential"],
  "issuer": {
    "id": "did:ebsi:2A9PZGnuqJBWNrpCTNQkBNHPhNHSqJhGXUhL3xWtL5Fst3EVb",
    "name": {
      "en": "University of Example",
      "fr": "Université d'Exemple",
      "de": "Universität Beispiel"
    },
    "accreditation": [
      {
        "accreditationBody": "National Higher Education Authority",
        "accreditationId": "NHE-2023-789",
        "accreditationDate": "2023-01-15",
        "validUntil": "2028-01-14"
      }
    ]
  },
  "issuanceDate": "2024-02-15",
  "credentialSubject": {
    "id": "did:ebsi:zhSvxcMPwYMrMdj25X5QzYrW3D7hkBbJJwJkUcKfCpMfMRRu",
    "fullName": "Maria Garcia",
    "dateOfBirth": "1998-05-12",
    "placeOfBirth": "Madrid",
    "qualification": {
      "name": {
        "en": "Master of Science in Computer Science",
        "fr": "Master en Sciences Informatiques",
        "de": "Master of Science in Informatik"
      },
      "level": {
        "eqfLevel": 7,
        "nqfLevel": "Level 7",
        "isced": "0613"
      },
      "fieldOfStudy": {
        "code": "0613",
        "name": {
          "en": "Software and Applications Development and Analysis",
          "fr": "Développement et analyse de logiciels et d'applications",
          "de": "Software- und Anwendungsentwicklung und -analyse"
        }
      },
      "degreeAwarded": {
        "en": "Master of Science",
        "fr": "Master en Sciences",
        "de": "Master of Science"
      },
      "studyDuration": {
        "years": 2,
        "ects": 120,
        "startDate": "2022-09-15",
        "endDate": "2024-06-30"
      },
      "graduationDate": "2024-06-30",
      "finalResult": {
        "grade": "A",
        "description": {
          "en": "Excellent - outstanding performance with only minor errors",
          "fr": "Excellent - résultat remarquable avec seulement des erreurs mineures",
          "de": "Ausgezeichnet - hervorragende Leistung mit nur geringfügigen Fehlern"
        }
      },
      "learningOutcomes": [
        {
          "category": "knowledge",
          "description": {
            "en": "Advanced knowledge of computer science principles and practices",
            "fr": "Connaissance avancée des principes et pratiques de l'informatique",
            "de": "Fortgeschrittene Kenntnisse der Informatikprinzipien und -praktiken"
          }
        },
        {
          "category": "skills",
          "description": {
            "en": "Design and implement complex software systems",
            "fr": "Concevoir et mettre en œuvre des systèmes logiciels complexes",
            "de": "Entwerfen und Implementieren komplexer Softwaresysteme"
          }
        }
      ],
      "supplementaryDocument": {
        "id": "https://university-example.eu/credentials/diploma/1234/supplement",
        "type": "DiplomaSupplementCredential",
        "name": {
          "en": "Diploma Supplement",
          "fr": "Supplément au diplôme",
          "de": "Diplomzusatz"
        }
      }
    }
  },
  "proof": {
    "type": "EcdsaSecp256k1Signature2019",
    "created": "2024-02-15T10:25:43Z",
    "proofPurpose": "assertionMethod",
    "verificationMethod": "did:ebsi:2A9PZGnuqJBWNrpCTNQkBNHPhNHSqJhGXUhL3xWtL5Fst3EVb#keys-1",
    "proofValue": "z58DAdFfa9SkqZMVPxAQpic7ndSayn6RrxWE2mSmFUZaGPRyMuPW2X5yCWuLiQTjB3RPJWAyxgQLbDpzeXPuVfJfHAi"
  }
}
```

## Schema Versioning

- **Version**: 1.0.0
- **Last Updated**: 2024-02-15
- **Status**: Draft

## Implementation Considerations

When implementing this schema:

- Ensure all required fields are provided
- Support multilingual representation of key information
- Include appropriate accreditation information
- Link to supplementary documents when available
- Provide comprehensive learning outcome information
- Use standard classification systems for fields of study and qualification levels

## Extensions

The schema can be extended to support:

- Additional jurisdiction-specific qualification information
- Integration with professional certification systems
- More detailed learning outcome taxonomies
- Advanced cryptographic proof formats
- Additional metadata for credential aggregation
