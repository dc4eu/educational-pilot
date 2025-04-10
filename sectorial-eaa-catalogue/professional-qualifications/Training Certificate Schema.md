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

```json
{
  "@context": [
    "https://www.w3.org/2018/credentials/v1",
    "https://eaa-rulebook.europa.eu/2023/credentials/trainingCert/v01"
  ],
  "id": "https://professional-example.eu/credentials/trainingCert/1234",
  "type": ["VerifiableCredential", "ProfessionalTrainingCredential"],
  "issuer": {
    "id": "did:ebsi:rpCTNQkBNHPhNHSqJhGXUhL3xWtL5Fst3EVb2A9PZGnuqJBWN",
    "name": {
      "en": "Foundation for Research, Teaching, Training, and Professional Competence of Registered Physicians in Spain",
      "es": "Fundación para la Formación de la Organización Médica Colegial de España"
    },
    "accreditation": [
      {
        "accreditationBody": "UEMS-EACCME",
        "accreditationDate": "2024-12-01"
      },
      {
        "accreditationBody": "FFOMC",
        "accreditationDate": "2024-12-01"
      }
    ]
  },
  "issuanceDate": "2024-12-01",
  "credentialSubject": {
    "id": "did:ebsi:W3D7hkBbJJwJkUcKfCpMfMRRuzhSvxcMPwYMrMdj25X5QzYr",
    "givenName": "Nombre",
    "familyName": "Apellido/s",
    "qualification": {
      "title": "Buen Quehacer del Médico (BQM)",
      "level": {
        "eqfLevel": 8
      },
      "fieldOfStudy": {
        "name": {
          "es": "...",
          "en": "..."
        }
      },
      "trainingAwarded": "BQM - Relación médico-paciente",
      "trainingDuration": {
        "startDate": "2024-11-24",
        "endDate": "2024-11-27"
      },
      "volumeOfLearning": "PT10H",
      "mode": [ 
        {
          "id": "http://data.europa.eu/snb/learning-assessment/9191af2ed9",
          "type": "Concept",
          "inScheme": {
            "id": "http://data.europa.eu/snb/learning-assessment/25831c2",
            "type": "ConceptScheme"
          },
          "prefLabel": {
            "en": [ "Presential" ]
          }
        }
      ],
      "creditPoint": [ 
        {
          "id": "urn:epass:creditPoint:1",
          "type": "CreditPoint",
          "framework": {
            "id": "http://data.europa.eu/snb/education-credit/60b314e826",
            "type": "Concept",
            "inScheme": {
              "id": "http://data.europa.eu/snb/education-credit/25831c2",
              "type": "ConceptScheme"
            },
            "prefLabel": {
              "en": "Spanish National Health System Continuing Education Credits",
              "es": "Crédicos Españoles de Formación Continuada del Sistema Nacional de Salud"
            }
          },
          "point" : "1,5"
        },
        {
          "id": "urn:epass:creditPoint:2",
          "type": "CreditPoint",
          "framework": {
            "id": "http://data.europa.eu/snb/education-credit/e82660b314",
            "type": "Concept",
            "inScheme": {
              "id": "http://data.europa.eu/snb/education-credit/31c2258",
              "type": "ConceptScheme"
            },
            "prefLabel": {
              "en": "Spanish Medical Professional Body of Accreditation for CPD/FMC. / European Accreditation Council for Continuing Medical Education de la Union Européenne de Médecins Spécialistes (UEMS).",
              "es": "Consejo Profesional Médico Español de Acreditación para el DPC/FMC. / Consejo Europeo de Acreditación de la Formación Médica Continuada de la Unión Europea de Médicos Especialistas (UEMS)."
            }
          },
          "point": "10"
        }
      ],
      "sponsor": "Sponsor of training activity, if any",
      "partner": "partner of training activity, if any",
      "entryRequirement": {
            "id": "urn:prof:note:1",
            "type": "Note",
            "noteLiteral" : {
              "en": "Registered doctors",
              "es": "Médicos colegiados"
            }
      },
      "learningOutcomes": [
        {
          "category": "knowledge",
            "description": {
              "en": "...",
              "es": "Aprender a liderar situaciones en las que un médico debe proporcionar asistencia sanitaria en el Sistema Nacional de Salud a personas de otros países."
            }
          },
        {
          "category": "skills",
          "description": {
            "en": "...",
            "es": "..."
          }
        }
      ]
    }
  },
  "proof": {
    "type": "EcdsaSecp256k1Signature2019",
    "created": "2024-12-01T10:25:43Z",
    "proofPurpose": "assertionMethod",
    "verificationMethod": "did:ebsi:JhGXUhL3xWtL5Fst3EVb2A9PZGnuqJBWNrpCTNQkBNHPhNHSq#keys-1",
    "proofValue": "ZaGPRyMuPW2X5yCWuLiQTjB3RPJWAyxgQLbDpzeXPuVfJfHAiz58DAdFfa9SkqZMVPxAQpic7ndSayn6RrxWE2mSmFU"
  }
}
```

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
