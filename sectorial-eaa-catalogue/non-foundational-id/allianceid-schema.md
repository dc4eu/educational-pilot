# Verifiable AllianceID Schema

## Overview

This document describes the Verifiable AllianceID model, which provides a standardized format for representing identity credentials for natural persons participating in European University Alliances. The model is implemented using the W3C Verifiable Credentials Data Model (VCDM) and serves as a component of the non-foundational identity framework for European educational and professional qualifications.

## Verifiable AllianceID Structure

The Verifiable AllianceID credential contains a set of standardized attributes that identify a person within the context of European University Alliances. These attributes are contained within the `credentialSubject` object of a verifiable credential:

```json
{
  "credentialSubject": {
    "id": "did:example:123456789abcdefghi",
    "identifier": {
      "schemeID": "urn:schac:europeanUniversityAllianceCode",
      "value": "int:euai:alliance.eu:EUNETWORK",
      "id": "urn:schac:europeanUniversityAllianceCode:int:euai:alliance.eu:EUNETWORK"
    }
  }
}
```

## Core Required Attributes

The following attributes are mandatory for all Verifiable AllianceID credentials:

| Attribute | Description | Format |
|-----------|-------------|--------|
| `id` | Unique identifier of the credential subject (typically a DID) | String |
| `identifier` | Object containing identification information for the University Alliance | Object |

### Identifier Object Structure

The `identifier` object has the following structure:

| Attribute | Description | Format | Required |
|-----------|-------------|--------|----------|
| `schemeID` | Schema used to define alternative identification | String | Yes |
| `value` | Alternative identification value | String | Yes |
| `id` | URI of the identifier | URI format string | No |

## Identifier Format

The Verifiable AllianceID follows a specific format for the identifier:

```
urn:schac:europeanUniversityAllianceCode:int:euai:<sHO>:<code>
```

Where:
- `<sHO>` is the schacHomeOrganization of the Alliance that issued the credential
- `<code>` is the university alliance code

This format ensures consistency across different European University Alliances while providing clear identification of the specific alliance.

## Implementation in Verifiable Credentials

The Verifiable AllianceID schema extends the base W3C Verifiable Credentials Data Model. A complete Verifiable AllianceID credential would include:

1. Standard VC properties (`id`, `type`, `issuer`, etc.)
2. The credentialSubject containing the AllianceID attributes
3. Cryptographic proofs for verification

## Usage in Educational Contexts

In educational and professional qualification contexts, the Verifiable AllianceID serves as:

1. **A common identifier** for participants across European University Alliances
2. **A standardized format** for exchanging information within alliance networks
3. **A means of verification** for alliance membership and participation
4. **A building block** for credentials related to alliance activities and achievements
5. **A non-foundational identity** that complements other educational credentials

## Privacy Considerations

When implementing the Verifiable AllianceID schema:

- Apply data minimization principles by only requesting necessary attributes
- Implement selective disclosure to share only required identity information
- Ensure appropriate data protection measures are in place
- Respect user consent for data sharing
- Comply with relevant data protection regulations, including GDPR

## Full Schema Serialization

Below is the full JSON schema for the Verifiable AllianceID:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "EBSI Verifiable Attestation",
  "description": "The schema defines a generic structure for any EBSI-related Verifiable Credentials according to the VCDM v1.1",
  "type": "object",
  "properties": {
    "@context": {
      "description": "Semantic context for the issued credential. First element MUST be https://www.w3.org/2018/credentials/v1",
      "type": "array",
      "items": {
        "type": "string",
        "format": "uri"
      },
      "contains": {
        "const": "https://www.w3.org/2018/credentials/v1"
      },
      "minItems": 1,
      "uniqueItems": true
    },
    "id": {
      "description": "Globally unique identifier for the issued credential",
      "type": "string",
      "format": "uri"
    },
    "type": {
      "description": "Full type chain, used to identify the credential base types",
      "type": "array",
      "items": {
        "type": "string"
      },
      "contains": {
        "type": "string",
        "const": "VerifiableAttestation"
      },
      "uniqueItems": true
    },
    "issuer": {
      "description": "Defines a property for expressing the issuer of a Verifiable Credential",
      "oneOf": [
        {
          "description": "DID of the credential issuer",
          "type": "string",
          "format": "uri"
        },
        {
          "type": "object",
          "required": [
            "id"
          ],
          "properties": {
            "id": {
              "description": "DID of the credential issuer",
              "type": "string",
              "format": "uri"
            }
          }
        }
      ]
    },
    "issuanceDate": {
      "description": "Defines the date and time, when the issued credential becomes valid",
      "type": "string",
      "format": "date-time"
    },
    "issued": {
      "description": "Defines when the issued credential was issued",
      "type": "string",
      "format": "date-time"
    },
    "validFrom": {
      "description": "Defines the date and time, when the issued credential becomes valid",
      "type": "string",
      "format": "date-time"
    },
    "validUntil": {
      "description": "Defines the date and time, when the issued credential expires",
      "type": "string",
      "format": "date-time"
    },
    "expirationDate": {
      "description": "Defines the date and time, when the issued credential expires",
      "type": "string",
      "format": "date-time"
    },
    "credentialSubject": {
      "description": "Defines information about the subject that is defined by the type chain",
      "anyOf": [
        {
          "$ref": "#/$defs/credentialSubject"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/$defs/credentialSubject"
          }
        }
      ]
    },
    "credentialStatus": {
      "description": "Defines suspension and/or revocation details for the issued credential. Further redefined by the type extension",
      "anyOf": [
        {
          "$ref": "#/$defs/credentialStatus"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/$defs/credentialStatus"
          }
        }
      ]
    },
    "credentialSchema": {
      "description": "One or more schemas that validate the Verifiable Credential.",
      "anyOf": [
        {
          "$ref": "#/$defs/credentialSchema"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/$defs/credentialSchema"
          }
        }
      ]
    },
    "termsOfUse": {
      "description": "Contains the terms under which the issued credential was issued",
      "anyOf": [
        {
          "$ref": "#/$defs/termsOfUse"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/$defs/termsOfUse"
          }
        }
      ]
    },
    "evidence": {
      "description": "Contains the optional evidence used to issue this credential",
      "anyOf": [
        {
          "$ref": "#/$defs/evidence"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/$defs/evidence"
          }
        }
      ]
    }
  },
  "required": [
    "@context",
    "id",
    "type",
    "issuer",
    "issuanceDate",
    "issued",
    "validFrom",
    "credentialSubject",
    "credentialSchema"
  ],
  "$defs": {
    "credentialSubject": {
      "description": "Defines information about the subject that is defined by the type chain",
      "type": "object",
      "properties": {
        "id": {
          "description": "Defines the DID of the subject that is described by the issued credential",
          "type": "string",
          "format": "uri"
        }
      }
    },
    "credentialStatus": {
      "description": "Defines suspension and/or revocation details for the issued credential. Further redefined by the type extension",
      "type": "object",
      "properties": {
        "id": {
          "description": "Exact identity for the credential status",
          "type": "string",
          "format": "uri"
        },
        "type": {
          "description": "Defines the revocation type extension",
          "type": "string"
        }
      },
      "required": [
        "id",
        "type"
      ]
    },
    "credentialSchema": {
      "description": "Contains information about the credential schema on which the issued credential is based",
      "type": "object",
      "properties": {
        "id": {
          "description": "References the credential schema stored on the Trusted Schemas Registry (TSR) on which the Verifiable Authorisation is based on",
          "type": "string",
          "format": "uri"
        },
        "type": {
          "description": "Defines credential schema type",
          "type": "string"
        }
      },
      "required": [
        "id",
        "type"
      ]
    },
    "termsOfUse": {
      "description": "Contains the terms under which the issued credential was issued",
      "type": "object",
      "properties": {
        "id": {
          "description": "Contains a URL that points to where more information about this instance of terms of use can be found.",
          "type": "string"
        },
        "type": {
          "description": "Defines the type extension",
          "type": "string"
        }
      },
      "required": [
        "type"
      ]
    },
    "evidence": {
      "type": "object",
      "properties": {
        "id": {
          "description": "If present, it SHOULD contain a URL that points to where more information about this instance of evidence can be found.",
          "type": "string"
        },
        "type": {
          "anyOf": [
            {
              "description": "Defines the evidence type extension",
              "type": "string"
            },
            {
              "description": "Defines the evidence type extension",
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          ]
        }
      },
      "required": [
        "type"
      ]
    }
  }
}
```

## Example Credential

Here's an example of a Verifiable AllianceID credential:

```json
{
  "@context": [
    "https://www.w3.org/2018/credentials/v1",
    "https://europa.eu/2023/credentials/allianceid/v1"
  ],
  "id": "urn:uuid:7c8aed6e-57b4-45cf-b0f9-1d7bc2d8c84a",
  "type": ["VerifiableCredential", "VerifiableAllianceID"],
  "issuer": "did:ebsi:za57y29fhM3Nj8jKPkALW5",
  "issuanceDate": "2023-10-15T14:35:42Z",
  "validFrom": "2023-10-15T14:35:42Z",
  "expirationDate": "2025-10-14T23:59:59Z",
  "credentialSubject": {
    "id": "did:ebsi:zmqJZHv7TF8TRfpk2j4xPy",
    "identifier": {
      "schemeID": "urn:schac:europeanUniversityAllianceCode",
      "value": "int:euai:una-europa.eu:UNAEUROPA",
      "id": "urn:schac:europeanUniversityAllianceCode:int:euai:una-europa.eu:UNAEUROPA"
    }
  },
  "proof": {
    "type": "EcdsaSecp256k1Signature2019",
    "created": "2023-10-15T14:35:42Z",
    "proofPurpose": "assertionMethod",
    "verificationMethod": "did:ebsi:za57y29fhM3Nj8jKPkALW5#keys-1",
    "jws": "eyJhbGciOiJFUzI1NksiLCJiNjQiOmZhbHNlLCJjcml0IjpbImI2NCJdfQ..0xEdBniX3qYP_uJfpn1L7tJFLciDJYWUNIYvO7TkdFh5S5GHT92KT5YHaVPC6rM3QiAWzOEzQH2M-flXSFhQXA"
  }
}
```

## European University Alliances Context

The Verifiable AllianceID is specifically designed for the European University Alliances initiative, which:

- Creates transnational alliances of higher education institutions across the EU
- Develops long-term structural and strategic partnerships
- Promotes European values and identity
- Enhances the quality and competitiveness of European higher education

Examples of European University Alliances include:
- UNA Europa
- YUFE (Young Universities for the Future of Europe)
- EUTOPIA (European University Alliance)
- 4EU+ Alliance
- CIVIS (A European Civic University)

## Relationship to Other Educational Identifiers

The Verifiable AllianceID complements other educational identifiers:

- **More specific** than general educational identifiers like MyAcademicID
- **More focused** on alliance-specific activities and recognition
- **Less formal** than foundational identities like PID
- **Cross-institutional** by design to support alliance mobility

## Schema Versioning

The Verifiable AllianceID schema may be updated as European University Alliances evolve. Implementations should:

- Check for schema updates regularly
- Maintain backward compatibility
- Support validation against the specified schema version
- Handle attributes that may be added in future versions

Current version: 1.0.0
