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
  "title": "Verifiable AllianceID",
  "description": "Schema of an EBSI Verifiable University Alliance ID for a natural person participating in the Alliance",
  "type": "object",
  "allOf": [
    {
      "$ref": "https://www.w3.org/2018/credentials/v1"
    },
    {
      "properties": {
        "credentialSubject": {
          "description": "Defines additional properties on credentialSubject to describe IDs that do not have a substantial level of assurance.",
          "type": "object",
          "properties": {
            "id": {
              "description": "Defines a unique identifier of the credential subject",
              "type": "string"
            },
            "identifier": {
              "type": "object",
              "description": "Defines the identifier for the University Alliance. Format: urn:schac:europeanUniversityAllianceCode:int:euai:<sHO>:<code>. sHO: the schacHomeOrganization of the Alliance that issued the credential, <code> the university alliance code",
              "$ref": "#/$defs/identifier"
            }
          },
          "required": ["id", "identifier"]
        }
      }
    }
  ],
  "$defs": {
    "identifier": {
      "description": "Defines an alternative Identifier object",
      "type": "object",
      "properties": {
        "schemeID": {
          "description": "Defines the schema used to define alternative identification",
          "type": "string"
        },
        "value": {
          "description": "Define the alternative identification value",
          "type": "string"
        },
        "id": {
          "description": "The URI of the identifier",
          "type": "string",
          "format": "uri"
        }
      },
      "required": ["schemeID", "value"]
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
