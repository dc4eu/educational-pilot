# MyAcademicID Schema

## Overview

This document describes the MyAcademicID model, which provides a standardized format for representing academic identity credentials within the European Education Area. The model is implemented using the W3C Verifiable Credentials Data Model (VCDM) and serves as a key component of the non-foundational identity framework for European educational and professional qualifications.

## MyAcademicID Structure

The MyAcademicID credential contains a set of standardized attributes that identify and characterize a student or academic within the European academic ecosystem. These attributes are contained within the `credentialSubject` object of a verifiable credential:

```json
{
  "credentialSubject": {
    "id": "did:example:123456789abcdefghi",
    "communityUserIdentifier": "a1b2c3d4e5f6@erasmus.eduteams.org",
    // Other MyAcademicID attributes
  }
}
```

## Core Required Attributes

The following attributes are mandatory for all MyAcademicID credentials:

| Attribute | Description | Format | OID Reference |
|-----------|-------------|--------|--------------|
| `id` | Unique identifier of the credential subject (typically a DID) | String | N/A |
| `communityUserIdentifier` | Opaque and non-revocable identifier following eduPersonUniqueId syntax | String | 1.3.6.1.4.1.5923.1.1.1.13 |
| `displayName` | User's full name (firstname lastname) | String | 2.16.840.1.113730.3.1.241 |
| `givenName` | Part of person's name that is not their surname | String | 2.5.4 |
| `familyName` | Person's surname | String | 2.5.4.4 |
| `emailAddress` | Email address of the user | String (email format) | 0.9.2342.19200300.100.1.3 |
| `assurance` | Identity assurance level following REFEDS Assurance Framework | Array of URI strings | 1.3.6.1.4.1.5923.1.1.1.11 |

## Optional Attributes

The following attributes can be included to provide additional academic context:

### Academic Identification

| Attribute | Description | Format | OID Reference |
|-----------|-------------|--------|--------------|
| `europeanStudentIdentifier` | European Student Identifier (ESI) ensuring mobility | Array of strings | 1.3.6.1.4.1.25178.1.2.14 |
| `organization` | Organization description of the user | String | 1.3.6.1.4.1.25178.1.2.9 |

### Affiliations and Entitlements

| Attribute | Description | Format | OID Reference |
|-----------|-------------|--------|--------------|
| `externalAffiliation` | Affiliation within Home Organization (follows eduPersonScopedAffiliation syntax) | Array of strings | 1.3.6.1.4.1.25178.4.1.11 |
| `entitlements` | Entitlements of the user | Array of strings | 1.3.6.1.4.1.5923.1.1.1.7 |

## Key Identifiers

### Community User Identifier

The `communityUserIdentifier` follows the syntax of eduPersonUniqueId attribute of eduPerson:
- Consists of a "uniqueID" part and fixed scope "erasmus.eduteams.org", separated by @ sign
- The uniqueID part contains up to 64 hexadecimal digits (a-f, 0-9)
- Unique and persistent within the MyAcademicId namespace
- Used for identity matching and similar purposes

### European Student Identifier (ESI)

The `europeanStudentIdentifier` attribute:
- Ensures mobility across European institutions
- Has a lifetime limited to the period of student's mobility
- Structure is defined in referenced documentation
- Should not be parsed to extract information about the originating organization

## Assurance Levels

The `assurance` attribute contains one or more URIs that represent the level of identity assurance following the REFEDS Assurance Framework (RAF). This indicates the trustworthiness of the identity verification process that was used to issue the credential.

## Implementation in Verifiable Credentials

The MyAcademicID schema extends the base W3C Verifiable Credentials Data Model. A complete MyAcademicID credential would include:

1. Standard VC properties (`id`, `type`, `issuer`, etc.)
2. The credentialSubject containing the MyAcademicID attributes
3. Cryptographic proofs for verification

## Usage in Educational Contexts

In educational and professional qualification contexts, the MyAcademicID serves as:

1. **A common identifier** for student mobility across European institutions
2. **A standardized format** for exchanging student information
3. **A basis for academic identity matching** across different educational systems
4. **A building block** for educational credential ecosystems
5. **A non-foundational identity** that complements the PID (Person Identification Data)

## Privacy Considerations

When implementing the MyAcademicID schema:

- Apply data minimization principles by only requesting necessary attributes
- Implement selective disclosure to share only required identity information
- Ensure appropriate data protection measures are in place
- Respect user consent for data sharing
- Comply with relevant data protection regulations, including GDPR

## Full Schema Serialization

Below is the full JSON schema for the MyAcademicID:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "MyAcademicId",
  "description": "Schema of an MyAcademicId Verifiable Credential",
  "type": "object",
  "allOf": [
    {
      "$ref": "https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/0xbe77a21356835dc09d3d8149ea832ae0a4bae0ae9c869d18219ef8f4a74b4644"
    },
    {
      "properties": {
        "credentialSubject": {
          "description": "Defines additional properties on credentialSubject to describe IDs that do not have a substantial level of assurance.",
          "type": "object",
          "properties": {
            "id": {
              "description": "Defines a unique identifier of the credential subject. DID of the user",
              "type": "string"
            },
            "communityUserIdentifier": {
              "description": "User’s Community Identifier is an opaque and non-revocable identifier (i.e. it cannot change over time) that follows the syntax of eduPersonUniqueId  attribute of eduPerson. It consists of “uniqueID” part and fixed scope “erasmus.eduteams.org”, separated by at sign. The uniqueID part contains up to 64 hexadecimal digits (a-f, 0-9). The identifier is unique and persistent within the MyAcademicId namespace. The identifier can be used for identity matching, etc. OID: 1.3.6.1.4.1.5923.1.1.1.13 Definition: https: //wiki.refeds.org/display/STAN/eduPerson+2021-11#eduPerson202111-eduPersonUniqueId",
              "type": "string"
            },
            "europeanStudentIdentifier": {
              "description": "The European Student Identifier (ESI) of the user. ESI ensures mobility. Lifetime is limited to the period of student's mobility. ESI structure is defined in the document referenced below. ESI SHOULD NOT be parsed to extract information about the originating organisation of the student since the identifier structure is subject to a change. OID: 1.3.6.1.4.1.25178.1.2.14 Definition: https: //wiki.geant.org/display/SM/European+Student+Identifier",
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "externalAffiliation": {
              "description": "Affiliation within Home Organization.  One or more home organisations (such as, universities, research institutions or private companies) this user is affiliated with. The syntax and semantics follows eduPersonScopedAffiliation attribute. Affiliation is external to the MyAcademicId. OID: 1.3.6.1.4.1.25178.4.1.11 Definition: https: //wiki.refeds.org/display/STAN/eduPerson+2021-11#eduPerson202111-eduPersonScopedAffiliation",
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "organization": {
              "description": "This attribute describes the organization of this user. OID: 1.3.6.1.4.1.25178.1.2.9",
              "type": "string"
            },
            "displayName": {
              "description": "User’s name (firstname lastname). For more complex names. OID: 2.16.840.1.113730.3.1.241 Definition: https: //wiki.refeds.org/display/STAN/eduPerson+2021-11#eduPerson202111-displayName",
              "type": "string"
            },
            "givenName": {
              "description": "strings that are the part of a person's name that is not their surname (see RFC4519). OID: 2.5.4.Definition: https: //wiki.refeds.org/display/STAN/eduPerson+2021-11#eduPerson202111-givenName",
              "type": "string"
            },
            "familyName": {
              "description": "strings that are a person's surname (see RFC4519). OID: 2.5.4.4 Definition: https: //wiki.refeds.org/display/STAN/eduPerson+2021-11#eduPerson202111-sn",
              "type": "string"
            },
            "emailAddress": {
              "description": "address of the user. OID: 0.9.2342.19200300.100.1.3 Definition: https: //wiki.refeds.org/display/STAN/eduPerson+2021-11#eduPerson202111-homePostalAddress",
              "type": "string",
              "format": "email"
            },
            "entitlements": {
              "description": "This attribute describes the entitlements of this user. OID: 1.3.6.1.4.1.5923.1.1.1.7 Definition: https: //wiki.refeds.org/display/STAN/eduPerson+2021-11#eduPerson202111-eduPersonEntitlement",
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "assurance": {
              "description": "Assurance of the identity of the user, following REFEDS Assurance Framework (RAF). OID: 1.3.6.1.4.1.5923.1.1.1.11 Definition: https: //wiki.refeds.org/display/STAN/eduPerson+2021-11#eduPerson202111-eduPersonAssurance",
              "type": "array",
              "items": {
                "type": "string",
                "format": "uri"
              }
            }
          },
          "required": [
            "id",
            "communityUserIdentifier",
            "displayName",
            "givenName",
            "familyName",
            "emailAddress",
            "assurance"
          ]
        }
      }
    }
  ]
}
```

## Example Credential

Here's an example of a MyAcademicID credential:

```json
{
  "@context": [
    "https://www.w3.org/2018/credentials/v1",
    "https://europa.eu/2023/credentials/myacademicid/v1"
  ],
  "id": "urn:uuid:5e9b4e8a-1dae-4797-86a6-f24392436c7f",
  "type": ["VerifiableCredential", "MyAcademicID"],
  "issuer": "did:ebsi:zbU6M5T5DxcgJiCUT78Fbk",
  "issuanceDate": "2023-09-01T10:15:38Z",
  "validFrom": "2023-09-01T10:15:38Z",
  "expirationDate": "2024-08-31T23:59:59Z",
  "credentialSubject": {
    "id": "did:ebsi:zd6NuZy9JfQV4SeYd3P3L7",
    "communityUserIdentifier": "a2b1c5d8e3f7@erasmus.eduteams.org",
    "europeanStudentIdentifier": [
      "esi:eac-rew:fr:78e7t6y5432@univ-paris1.fr"
    ],
    "externalAffiliation": [
      "student@univ-paris1.fr",
      "member@univ-paris1.fr"
    ],
    "organization": "Université Paris 1 Panthéon-Sorbonne",
    "displayName": "Sophie Martin",
    "givenName": "Sophie",
    "familyName": "Martin",
    "emailAddress": "sophie.martin@student.univ-paris1.fr",
    "entitlements": [
      "urn:mace:egi.eu:group:vo.geant.org:role=member",
      "urn:geant:eduteams.org:service:eduteams-app:group:vo.geant.org#member"
    ],
    "assurance": [
      "https://refeds.org/assurance/IAP/low",
      "https://refeds.org/assurance/ATP/ePA-1m"
    ]
  },
  "proof": {
    "type": "EcdsaSecp256k1Signature2019",
    "created": "2023-09-01T10:15:38Z",
    "proofPurpose": "assertionMethod",
    "verificationMethod": "did:ebsi:zbU6M5T5DxcgJiCUT78Fbk#keys-1",
    "jws": "eyJhbGciOiJFUzI1NksiLCJiNjQiOmZhbHNlLCJjcml0IjpbImI2NCJdfQ..nKvn2UpIDMYDH5EefQcW4BuhJJLWFckDJRxVhevyoR9ExzSNS_9yQq_LJFN2-q_kTGKRDxgfJN-LPQNcEG3peg"
  }
}
```

## Relationship to eduPerson and REFEDS

The MyAcademicID schema leverages several attributes from the eduPerson schema and the REFEDS (Research and Education FEDerations) standards:

- The `communityUserIdentifier` is based on eduPersonUniqueId
- The `externalAffiliation` follows the eduPersonScopedAffiliation attribute syntax
- The `assurance` attribute aligns with the REFEDS Assurance Framework (RAF)
- Other attributes like `displayName`, `givenName`, and `familyName` follow standard eduPerson definitions

This alignment with established standards ensures interoperability with existing academic identity systems across Europe.

## Differences from Foundational Identity

Unlike the Person Identification Data (PID), which is a foundational identity with high assurance levels, the MyAcademicID is a:

- Non-foundational identity focused specifically on academic contexts
- Credential that does not require the same level of identity verification as PID
- Complementary identity that can be linked to a PID when necessary
- More flexible identity suitable for academic mobility and cross-border scenarios

## Schema Versioning

The MyAcademicID schema follows established academic identity standards and may be updated as these standards evolve. Implementations should:

- Check for schema updates regularly
- Maintain backward compatibility
- Support validation against the specified schema version
- Handle attributes that may be added in future versions

Current version: 1.0.0
