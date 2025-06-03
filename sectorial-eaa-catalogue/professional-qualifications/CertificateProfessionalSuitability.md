# Certificate of Professional Suitability Schema

## Overview

JSON Schema for a Certificate of Professional Suitability that validates whether a registered physician has an up to date certificate of professional competence and is able to practice as a doctor.

## Schema Structure

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://eaa-rulebook.europa.eu/schemas/cps/0.0.1",
  "title": "Doctor ID",
  "description": "Schema for professional suitabilty credentials for physicians",
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
        "https://eaa-rulebook.europa.eu/2023/credentials/cps/v01"
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
      "default": ["VerifiableCredential", "ProfessionalSuitabilityCredential"]
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
      "description": "Information about the doctor and their status",
      "properties": {
        "id": {
          "type": "string",
          "format": "uri"
        },
        "givenName": {
          "description": "Current first name(s), including middle name(s) where applicable, of the user to whom the person identification data relates.",  
          "type": "string"
        },
        "familyName": {
          "description": "Current last name(s) or surname(s) of the user to whom the person identification data relates.",
          "type": "string"
        },
        "legally_entitled": {
          "description": "Defines whether the professional is considered to be qualified to practise medicine, and there is no record of the professional having been sanctioned or disqualified from practising as a doctor.",
          "type": "boolean"
        },
        "medical_registration": {
          "description": "National or Regional professional body to which the physician has been registered.",
          "type": "array",
          "items": {
            "properties": {
              "medical_board": {
                "description": "Corresponds to the regional professional body of physicians where the professional is registered.",
                "type": "array",
                "items": {
                  "type": "string"
                }
              },
              "personal_administrative_number": {
                "description": "Identification number of the registered physician.",
                "type": "string",
                "pattern": "([0-9]{9})"
              },
              "membership_start_date": {
                "description": "Date from which a professional has been registered to the National or Regional Physicians Body.",
                "type": "string",
                "format": "date"
              },
              "membership_end_date": {
                "description": "Date from which a professional has been deregistered to the National or Regional Physicians Body",
                "type": "string",
                "format": "date"
              }
            }
          }
        }
      },
      "required": ["id", "givenName", "familyName", "medical_registration", "legally_entitled"]
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

[Certificate of Professional Suitability example](./examples/CertificateOfProfessionalSuitability.json)

## Schema Versioning

- **Version**: 0.0.2
- **Last Updated**: 2025-04-02
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
