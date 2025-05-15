# Continuous Professional Development Schema

## Overview

The Continuous Professional Development Schema defines the data structure to represent periodic verification and levels in which the professional can be positioned on the basis of his or her professional training and experience, which could include evaluation, recognition and certification of the knowledge acquired throughout the professional's life.

## Schema Structure

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://eaa-rulebook.europa.eu/schemas/cpd/0.0.1",
  "title": "Doctor ID",
  "description": "Schema for Continuous Professional Development credentials",
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
        "https://eaa-rulebook.europa.eu/2023/credentials/cpd/v01"
      ]
    },
    "id": {
      "type": "string",
      "format": "uri",
      "description": "Unique identifier for the CPD credential"
    },
    "type": {
      "type": "array",
      "description": "Credential type definitions",
      "items": {
        "type": "string"
      },
      "default": ["VerifiableCredential", "ContinuousProfessionalDevelopmentCredential"]
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
        }
      },
      "required": ["id", "name"]
    },
    "issuanceDate": {
      "type": "string",
      "format": "date",
      "description": "Date when the CPD certificate was issued"
    },
    "expirationDate": {
      "type": "string",
      "format": "date",
      "description": "Date when the CPD certificate expires"
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
        "professional_level": {
          "description": "Expertise level of a professional. To be defined according the type of profession.",
          "type": "string"
        }
      },
      "required": ["id", "given_name", "family_name"]
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
    "https://eaa-rulebook.europa.eu/2023/credentials/cpd/v01"
  ],
  "id": "https://university-example.eu/credentials/cpd/2468",
  "type": ["VerifiableCredential", "ContinuousProfessionalDevelopmentCredential"],
  "issuer": {
    "id": "did:ebsi:PBfCB1g1RJuydQqmLFp4Sv1oWkUVO6mLZCM0ZTWWGLzPBfCB1g1RJuydQ",
    "name": {
      "en": "National Professional Body of Technical Engineers of Spain",
      "es": "Consejo General de la Ingeniería Técnica Industrial de España"
    }
  },
  "issuanceDate": "2024-09-01",
  "expirationDate": "2027-08-31",
  "credentialSubject": {
    "id": "did:ebsi:GBzdPhl1BzBB9p3QkKmR0Yrxkv3IxHhAOYo1jV9eTHw",
    "givenName": "Name",
    "familyName": "Surname/s",
    "personal_administrative_number": "FGHIJ1234",
    "legally_entitled": "true",
    "professional_speciality": "mechanical"
  },
  "proof": {
    "type": "EcdsaSecp256k1Signature2019",
    "created": "2024-09-01T08:15:27Z",
    "proofPurpose": "assertionMethod",
    "verificationMethod": "did:ebsi:PBfCB1g1RJuydQqmLFp4Sv1oWkUVO6mLZCM0ZTWWGLzPBfCB1g1RJuydQ#keys-1",
    "proofValue": "prrofValueHash"
  }
}
```

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
