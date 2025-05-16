```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://schema.europa.eu/credentials/v1/esc-credential-schema.json",
  "title": "European Student Card Credential",
  "description": "Schema for a European Student Card as a Verifiable Credential",
  "type": "object",
  "required": ["@context", "type", "issuer", "issuanceDate", "credentialSubject", "proof"],
  "properties": {
    "@context": {
      "type": "array",
      "items": {
        "type": "string",
        "format": "uri"
      },
      "description": "Context URIs defining the vocabulary used in the VC"
    },
    "id": {
      "type": "string",
      "format": "uri",
      "description": "Unique identifier for the credential (e.g., UUID URI)"
    },
    "type": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "List of credential types"
    },
    "issuer": {
      "type": "string",
      "format": "uri",
      "description": "DID or URI identifying the issuer (e.g., HEI)"
    },
    "issuanceDate": {
      "type": "string",
      "format": "date-time",
      "description": "Date the credential was issued"
    },
    "expirationDate": {
      "type": "string",
      "format": "date-time",
      "description": "Date the credential expires (optional)"
    },
    "credentialSubject": {
      "type": "object",
      "description": "Claims about the student",
      "required": ["id", "givenName", "familyName", "email", "esi", "escn", "institutionPIC", "academicLevel"],
      "properties": {
        "id": {
          "type": "string",
          "format": "uri",
          "description": "DID of the student holder"
        },
        "givenName": {
          "type": "string",
          "description": "Student's given name"
        },
        "familyName": {
          "type": "string",
          "description": "Student's family name"
        },
        "email": {
          "type": "string",
          "format": "email",
          "description": "Student email address"
        },
        "esi": {
          "type": "string",
          "description": "European Student Identifier"
        },
        "escn": {
          "type": "string",
          "description": "European Student Card Number (UUID format)"
        },
        "institutionPIC": {
          "type": "string",
          "description": "Participant Identification Code of the issuing institution"
        },
        "academicLevel": {
          "type": "string",
          "enum": ["Bachelor", "Master", "PhD", "Other"],
          "description": "Academic level of the student"
        },
        "cardType": {
          "type": "string",
          "enum": ["Physical", "Digital"],
          "description": "Format of the ESC"
        },
        "status": {
          "type": "string",
          "enum": ["active", "revoked", "suspended"],
          "description": "Status of the ESC"
        }
      }
    },
    "credentialStatus": {
      "type": "object",
      "description": "Status list configuration for revocation/suspension",
      "required": ["id", "type", "statusPurpose", "statusListIndex", "statusListCredential"],
      "properties": {
        "id": {
          "type": "string",
          "format": "uri",
          "description": "URI to this credential’s status entry"
        },
        "type": {
          "type": "string",
          "enum": ["StatusList2021Entry"],
          "description": "Status type"
        },
        "statusPurpose": {
          "type": "string",
          "enum": ["revocation", "suspension"],
          "description": "Purpose of status tracking"
        },
        "statusListIndex": {
          "type": "string",
          "description": "Index in the status list"
        },
        "statusListCredential": {
          "type": "string",
          "format": "uri",
          "description": "URI of the status list credential document"
        }
      }
    },
    "proof": {
      "type": "object",
      "description": "Cryptographic proof",
      "required": ["type", "created", "proofPurpose", "verificationMethod", "jws"],
      "properties": {
        "type": {
          "type": "string",
          "description": "Signature type (e.g., Ed25519Signature2020)"
        },
        "created": {
          "type": "string",
          "format": "date-time",
          "description": "When the proof was created"
        },
        "proofPurpose": {
          "type": "string",
          "enum": ["assertionMethod"],
          "description": "Purpose of the proof"
        },
        "verificationMethod": {
          "type": "string",
          "description": "URI to the verification method (e.g., public key)"
        },
        "jws": {
          "type": "string",
          "description": "JWS signature value"
        }
      }
    }
  }
}

```