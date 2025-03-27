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
      "description": "Date when the doctor ID was issued"
    },
    "expirationDate": {
      "type": "string",
      "format": "date",
      "description": "Date when the doctor ID expires"
    },
    "credentialSubject": {
      "type": "object",
      "description": "Information about the doctor and their status",
      "properties": {
        "id": {
          "type": "string",
          "format": "uri"
        },
        "given_name": {
          "description": "Current first name(s), including middle name(s) where applicable, of the user to whom the person identification data relates.",  
          "type": "string"
        },
        "family_name": {
          "description": "Current last name(s) or surname(s) of the user to whom the person identification data relates.",
          "type": "string"
        },
        "personal_administrative_number": {
          "description": "Nationally registered physician number. eIDAS: a value assigned to the natural person that is unique among all personal administrative numbers issued by the provider of person identification data.",
          "type": "string",
          "pattern": "([A-Z]{4}[0-9]{5})"
        },
        "legally_entitled": {
          "description": "Attribute identifying whether a professional is legally entitled to practice or not. For doctors identifies whether or not a medical practitioner is legally qualified to practice as a doctor.",
          "type": "boolean"
        },
        "professional_body": {
          "description": "National or Regional professional body to which the physician has been registered.",
          "type": "object",
          "properties": {
            "id": {
              "type": "string",
              "format": "uri",
              "description": "identifier for the National or Regional Professional Body to which the physician is or has been registered."
            },
            "name": {
              "type": "string",
              "description":"Official legal name of the National or Regional Professional Body."
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
      },
      "required": [
        "id",
        "given_name",
        "family_name",
        "personal_administrative_number",
        "legally_entitled"
      ]
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
    "https://eaa-rulebook.europa.eu/2023/credentials/cps/v1"
  ],
  "id": "https://university-example.eu/credentials/cps/5678",
  "type": ["VerifiableCredential", "ProfessionalSuitabilityCredential"],
  "issuer": {
    "id": "did:ebsi:ZCM0ZTWWGLzPBfCB1g1RJuqmLFp4Sv1oWkUVO6mLydQ",
    "name": {
      "en": "National Professional Body of Physicians",
      "es": "Consejo General de Médicos"
    }
  },
  "issuanceDate": "2024-09-01",
  "expirationDate": "2027-08-31",
  "credentialSubject": {
    "id": "did:ebsi:BB9p3QkKmR0Yrxkv3IGBzdPhl_BzxHhAOYo_jV9eTHw",
    "given_name": "Name",
    "family_name": "Surname/s",
    "dateOfBirth": "1992-03-25",
    "personal_administrative_number": "ABCD12345",
    "legally_entitled": "true",
    "professional_body": {
        "name": "Regional Professinal Body of Physicians of Madrid",
        "membership_start_date": "2023-05-03"
     },
  "proof": {
    "type": "EcdsaSecp256k1Signature2019",
    "created": "2024-09-01T08:15:27Z",
    "proofPurpose": "assertionMethod",
    "verificationMethod": "did:ebsi:ZCM0ZTWWGLzPBfCB1g1RJuqmLFp4Sv1oWkUVO6mLydQ#keys-1",
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
