# Professional ID Schema

## Overview

The Professional ID Schema defines the data structure for representing identity credentials of any professional.

## Schema Structure

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://eaa-rulebook.europa.eu/schemas/professional-id/0.0.1",
  "title": "Professional ID",
  "description": "Schema for professional identity credentials",
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
        "https://eaa-rulebook.europa.eu/2023/credentials/professional-id/v01"
      ]
    },
    "id": {
      "type": "string",
      "format": "uri",
      "description": "Unique identifier for the professional ID credential"
    },
    "type": {
      "type": "array",
      "description": "Credential type definitions",
      "items": {
        "type": "string"
      },
      "default": ["VerifiableCredential", "ProfessionalIdCredential"]
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
        "issuing_country": {
          "type": "string",
          "description": "Country of the issuing institution"
      },
      "required": ["id", "name"]
    },
    "issuanceDate": {
      "type": "string",
      "format": "date",
      "description": "Date when the professional ID was issued"
    },
    "credentialSubject": {
      "type": "object",
      "description": "Information about the registered professional",
      "properties": {
        "id": {
          "type": "string"
        },
        "givenName": {
          "description": "Current first name(s), including middle name(s) where applicable, of the professional.",  
          "type": "string"
        },
        "familyName": {
          "description": "Current last name(s) or surname(s) of the professional.",
          "type": "string"
        },
         "document_number": {
          "description": "A number for the person identification data, assigned by the provider of person identification data.",
          "type": "string"
        },
        "personal_administrative_number": {
          "description": "Identification number of the registered professional.",
          "type": "string"
        },
        "legally_entitled": {
          "description": "Attribute identifying whether a professional is legally entitled to practice or not.",
          "type": "boolean"
        },
        "professional_speciality": {
          "description": "Specific area of knowledge within a profession that allows the professional to carry out specific tasks in accordance with that speciality.",
          "type": "array",
          "items": {
                    "type": "string"
                }
        }
      },
      "required": ["id", "givenName", "familyName", "personal_administrative_number"]
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
  "required": ["@context", "id", "type", "issuer", "issuanceDate", "expirationDate", "credentialSubject"]
}
```

## Example Credential

[Professional ID example](./examples/ProfesionalID.json)

## Schema Versioning

- **Version**: 0.0.1
- **Last Updated**: 2025-03-27
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
