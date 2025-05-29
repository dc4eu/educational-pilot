```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://eaa-rulebook.europa.eu/schemas/engineer-id/0.0.1",
  "title": "Engineer ID",
  "description": "Schema for engineers identity credentials",
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
        "https://eaa-rulebook.europa.eu/2023/credentials/engineer-id/v01"
      ]
    },
    "id": {
      "type": "string",
      "format": "uri",
      "description": "Unique identifier for the engineer ID credential"
    },
    "type": {
      "type": "array",
      "description": "Credential type definitions",
      "items": {
        "type": "string"
      },
      "default": ["VerifiableCredential", "EngineerIdCredential"]
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
      "description": "Date when the ID was issued"
    },
    "credentialSubject": {
      "type": "object",
      "description": "Information about the engineer and their status",
      "properties": {
        "id": {
          "type": "string"
        },
        "givenName": {
          "description": "Current first name(s), including middle name(s) where applicable.",  
          "type": "string"
        },
        "familyName": {
          "description": "Current last name(s) or surname(s).",
          "type": "string"
        },
        "professionalBody": {
          "description": "Corresponds to the national or regional professional body of engineers where the professional is registered.",
          "type": "string"
        },
        "personal_administrative_number": {
          "description": "Identification number of the registered engineer.",
          "type": "string"
        },
        "legally_entitled": {
          "description": "Defines whether the engineer is considered to be qualified to practise.",
          "type": "boolean"
        },
        "engineering_speciality": {
          "description": "List representing the engineering specialty of the professional.",
          "type": "array",
          "items": {
              "type": "string",
              "enum": [
                  "Aeronautical engineer",
                  "Agricultural engineer",
                  "Building engineer",
                  "Chemical engineer",
                  "Civil and environmental engineer",
                  "Civil engineer",
                  "Computer science engineer",
                  "Construction/Civil engineer: building of roads, bridges, railways",
                  "Electrical and computer engineer",
                  "Electrical engineer",
                  "Electromechanical engineer",
                  "Electronic engineer",
                  "Energy engineer",
                  "Engineer",
                  "Engineer fishing fleet",
                  "Environmental engineer",
                  "Forest engineer",
                  "Gas engineer",
                  "Geographical engineer",
                  "Geotechnical engineer",
                  "Industrial engineer",
                  "Information systems engineer",
                  "Marine engineer",
                  "Mechanical engineer",
                  "Mining engineer",
                  "Telecommunications engineer"
              ]
          }
        }
      },
      "required": [ "id", "givenName", "familyName", "personal_administrative_number", "engineering_speciality"]
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
