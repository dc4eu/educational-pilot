# Educational ID Schema

## Overview

The Educational ID Schema defines the data structure for representing educational identity credentials that confirm a student's affiliation with an educational institution. This schema supports verification of student status, programme enrolment, and access rights.

## Schema Structure

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://eaa-rulebook.europa.eu/schemas/educational-id/1.0.0",
  "title": "Educational ID",
  "description": "Schema for educational identity credentials",
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
        "https://eaa-rulebook.europa.eu/2023/credentials/educational-id/v1"
      ]
    },
    "id": {
      "type": "string",
      "format": "uri",
      "description": "Unique identifier for the educational ID credential"
    },
    "type": {
      "type": "array",
      "description": "Credential type definitions",
      "items": {
        "type": "string"
      },
      "default": ["VerifiableCredential", "EducationalIdCredential"]
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
        "type": {
          "type": "string",
          "description": "Type of educational institution",
          "enum": [
            "University",
            "College",
            "VocationalSchool",
            "SecondarySchool",
            "PrimarySchool",
            "ResearchInstitute",
            "Other"
          ]
        }
      },
      "required": ["id", "name"]
    },
    "issuanceDate": {
      "type": "string",
      "format": "date",
      "description": "Date when the educational ID was issued"
    },
    "expirationDate": {
      "type": "string",
      "format": "date",
      "description": "Date when the educational ID expires"
    },
    "credentialSubject": {
      "type": "object",
      "description": "Information about the student and their status",
      "properties": {
        "id": {
          "type": "string",
          "format": "uri",
          "description": "Identifier of the credential subject"
        },
        "fullName": {
          "type": "string",
          "description": "Full name of the student"
        },
        "dateOfBirth": {
          "type": "string",
          "format": "date",
          "description": "Date of birth of the student"
        },
        "studentId": {
          "type": "string",
          "description": "Institutional student identifier"
        },
        "academicStatus": {
          "type": "string",
          "description": "Academic status of the student",
          "enum": [
            "EnrolledFull",
            "EnrolledPart",
            "Exchange",
            "OnLeave",
            "Graduated",
            "Withdrawn",
            "Suspended"
          ]
        },
        "programme": {
          "type": "object",
          "description": "Information about the enrolled programme",
          "properties": {
            "name": {
              "type": "object",
              "description": "Multilingual name of the programme",
              "additionalProperties": {
                "type": "string"
              }
            },
            "level": {
              "type": "object",
              "description": "Level of the programme",
              "properties": {
                "eqfLevel": {
                  "type": "integer",
                  "minimum": 1,
                  "maximum": 8,
                  "description": "European Qualifications Framework level"
                },
                "isced": {
                  "type": "string",
                  "description": "ISCED classification code"
                }
              }
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
              }
            },
            "startDate": {
              "type": "string",
              "format": "date",
              "description": "Start date of the programme enrollment"
            },
            "expectedEndDate": {
              "type": "string",
              "format": "date",
              "description": "Expected completion date of the programme"
            },
            "currentYear": {
              "type": "integer",
              "description": "Current year of study in the programme"
            },
            "academicUnit": {
              "type": "object",
              "description": "Academic unit (faculty, department, etc.) information",
              "properties": {
                "name": {
                  "type": "object",
                  "description": "Multilingual name of the academic unit",
                  "additionalProperties": {
                    "type": "string"
                  }
                },
                "type": {
                  "type": "string",
                  "description": "Type of academic unit",
                  "enum": ["Faculty", "School", "Department", "Institute", "Centre", "Other"]
                }
              }
            }
          },
          "required": ["name"]
        },
        "accessRights": {
          "type": "array",
          "description": "Access rights granted to the student",
          "items": {
            "type": "object",
            "properties": {
              "type": {
                "type": "string",
                "description": "Type of access right",
                "enum": [
                  "Library",
                  "SportsFacilities",
                  "DigitalResources",
                  "Laboratories",
                  "StudentUnion",
                  "CampusBuildings",
                  "Other"
                ]
              },
              "description": {
                "type": "object",
                "description": "Multilingual description of the access right",
                "additionalProperties": {
                  "type": "string"
                }
              },
              "validUntil": {
                "type": "string",
                "format": "date",
                "description": "Validity end date for the specific access right"
              }
            },
            "required": ["type"]
          }
        },
        "photo": {
          "type": "string",
          "description": "Base64 encoded photo of the student",
          "contentEncoding": "base64"
        },
        "internationalStudent": {
          "type": "boolean",
          "description": "Indicates if the student is an international student"
        },
        "exchangeProgramme": {
          "type": "object",
          "description": "Information about exchange programme, if applicable",
          "properties": {
            "name": {
              "type": "string",
              "description": "Name of the exchange programme (e.g., Erasmus+)"
            },
            "homeInstitution": {
              "type": "object",
              "description": "Information about the home institution",
              "properties": {
                "name": {
                  "type": "object",
                  "description": "Multilingual name of the home institution",
                  "additionalProperties": {
                    "type": "string"
                  }
                },
                "country": {
                  "type": "string",
                  "description": "Country of the home institution"
                }
              }
            },
            "startDate": {
              "type": "string",
              "format": "date",
              "description": "Start date of the exchange period"
            },
            "endDate": {
              "type": "string",
              "format": "date",
              "description": "End date of the exchange period"
            }
          }
        }
      },
      "required": ["fullName", "studentId", "academicStatus"]
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
  "required": ["@context", "id", "type", "issuer", "issuanceDate", "expirationDate", "credentialSubject", "proof"]
}
```

## Example Credential

```json
{
  "@context": [
    "https://www.w3.org/2018/credentials/v1",
    "https://eaa-rulebook.europa.eu/2023/credentials/educational-id/v1"
  ],
  "id": "https://university-example.eu/credentials/educational-id/9876",
  "type": ["VerifiableCredential", "EducationalIdCredential"],
  "issuer": {
    "id": "did:ebsi:2A9PZGnuqJBWNrpCTNQkBNHPhNHSqJhGXUhL3xWtL5Fst3EVb",
    "name": {
      "en": "University of Example",
      "fr": "Université d'Exemple",
      "de": "Universität Beispiel"
    },
    "type": "University"
  },
  "issuanceDate": "2023-09-01",
  "expirationDate": "2024-08-31",
  "credentialSubject": {
    "id": "did:ebsi:zhSvxcMPwYMrMdj25X5QzYrW3D7hkBbJJwJkUcKfCpMfMRRu",
    "fullName": "Carlos Rodriguez",
    "dateOfBirth": "2000-03-25",
    "studentId": "S21345678",
    "academicStatus": "EnrolledFull",
    "programme": {
      "name": {
        "en": "Bachelor of Science in Computer Engineering",
        "fr": "Licence en Ingénierie Informatique",
        "de": "Bachelor of Science in Computeringenieurwesen"
      },
      "level": {
        "eqfLevel": 6,
        "isced": "0714"
      },
      "fieldOfStudy": {
        "code": "0714",
        "name": {
          "en": "Electronics and Automation",
          "fr": "Électronique et automatisation",
          "de": "Elektronik und Automatisierung"
        }
      },
      "startDate": "2022-09-01",
      "expectedEndDate": "2026-06-30",
      "currentYear": 2,
      "academicUnit": {
        "name": {
          "en": "Faculty of Engineering",
          "fr": "Faculté d'Ingénierie",
          "de": "Fakultät für Ingenieurwissenschaften"
        },
        "type": "Faculty"
      }
    },
    "accessRights": [
      {
        "type": "Library",
        "description": {
          "en": "Access to all university libraries and digital resources",
          "fr": "Accès à toutes les bibliothèques universitaires et aux ressources numériques",
          "de": "Zugang zu allen Universitätsbibliotheken und digitalen Ressourcen"
        },
        "validUntil": "2024-08-31"
      },
      {
        "type": "SportsFacilities",
        "description": {
          "en": "Access to university sports facilities",
          "fr": "Accès aux installations sportives universitaires",
          "de": "Zugang zu den Sporteinrichtungen der Universität"
        },
        "validUntil": "2024-08-31"
      }
    ],
    "photo": "iVBORw0KGgoAAAANSUhEUgAAABAA...",
    "internationalStudent": false
  },
  "proof": {
    "type": "EcdsaSecp256k1Signature2019",
    "created": "2023-09-01T08:15:27Z",
    "proofPurpose": "assertionMethod",
    "verificationMethod": "did:ebsi:2A9PZGnuqJBWNrpCTNQkBNHPhNHSqJhGXUhL3xWtL5Fst3EVb#keys-1",
    "proofValue": "z4a2FvTshj6vM4YByKKiiaA5xru6kNJKR76TQXcm2xrr47rH1gobQeFCYGzUBchvLNfMayd5qFyNtSw6tPCxBh7KT"
  }
}
```

## Schema Versioning

- **Version**: 1.0.0
- **Last Updated**: 2023-09-01
- **Status**: Draft

## Implementation Considerations

When implementing this schema:

- Ensure all required fields are provided
- Educational ID credentials should always have an expiration date
- Support multilingual representation of key information
- Implement appropriate privacy protections for personal information
- Include only necessary personal data
- Use standardised classification systems for academic programmes
- Consider selective disclosure requirements for sensitive attributes
- Include photo only when necessary for identification purposes

## Extensions

The schema can be extended to support:

- Additional institution-specific access rights
- Integration with campus management systems
- Digital service authorisations
- Accessibility accommodations information
- Extended international mobility data
- Dual degree programme information
- Special academic status designations
