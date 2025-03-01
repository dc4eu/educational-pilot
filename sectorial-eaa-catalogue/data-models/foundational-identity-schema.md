# Foundational Identity Schema

## Overview

This document describes the Person Identification Data (PID) model for Natural Persons, which forms the foundation for identity verification across the European education and professional qualifications framework. The model is implemented using the W3C Verifiable Credentials Data Model (VCDM) and conforms to the requirements specified in the European regulation referenced at https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202402977.

## Person Identification Data Structure

The PID credential for natural persons contains a set of standardized attributes that provide reliable identification of individuals. These attributes are contained within a `personIdentificationData` object in the credential subject:

```json
{
  "credentialSubject": {
    "personIdentificationData": {
      // PID attributes
    }
  }
}
```

## Core Required Attributes

The following attributes are mandatory for all PID credentials:

| Attribute | Description | Format |
|-----------|-------------|--------|
| `family_name` | Current last name(s) or surname(s) of the user | String (non-empty) |
| `given_name` | Current first name(s), including middle name(s) where applicable | String (non-empty) |
| `birth_date` | Day, month, and year on which the user was born | Date (ISO 8601) |
| `birth_place` | Country, state, province, district, local area, municipality, city, town, or village where the user was born | String (ISO 3166-1 alpha-2 for countries) |
| `nationality` | One or more nationalities of the user | Array of ISO 3166-1 alpha-2 country codes |
| `expiry_date` | Date (and if possible time) when the identification data will expire | Date-time (ISO 8601) |
| `issuing_authority` | Authority that issued the identification data | String |
| `issuing_country` | Country or territory of the provider of the identification data | ISO 3166-1 alpha-2 country code |

## Optional Attributes

The following attributes can be included to provide additional identification information:

### Address Information

| Attribute | Description | Format |
|-----------|-------------|--------|
| `resident_address` | Full address of the place where the user currently resides | String |
| `resident_country` | Country where the user currently resides | ISO 3166-1 alpha-2 country code |
| `resident_state` | State, province, district, or local area where the user currently resides | String |
| `resident_city` | Municipality, city, town, or village where the user currently resides | String |
| `resident_postal_code` | Postal code of the place where the user currently resides | String |
| `resident_street` | Name of the street where the user currently resides | String |
| `resident_house_number` | House number where the user currently resides, including any affix or suffix | String |

### Additional Identification

| Attribute | Description | Format |
|-----------|-------------|--------|
| `personal_administrative_number` | Unique identifier assigned to the natural person by the provider | String |
| `portrait` | Facial image of the user | String (ISO 19794-5 or ISO 39794 compliant) |
| `family_name_birth` | Last name(s) or surname(s) at birth | String |
| `given_name_birth` | First name(s), including middle name(s), at birth | String |
| `sex` | Sex of the user | Integer (ISO/IEC 5218 values) |
| `document_number` | Number for the identification data, assigned by the provider | String |

### Contact Information

| Attribute | Description | Format |
|-----------|-------------|--------|
| `email_address` | Electronic mail address of the user | String (RFC 5322 compliant) |
| `mobile_phone_number` | Mobile telephone number of the user | String (starting with '+' followed by country code and numbers) |

### Issuing Information

| Attribute | Description | Format |
|-----------|-------------|--------|
| `issuing_jurisdiction` | Country subdivision code of the issuing jurisdiction | ISO 3166-2:2020 code |
| `location_status` | Location of validity status information | String |

## Sex Attribute Enumeration

The `sex` attribute uses the following enumeration values:

| Value | Description | Standard |
|-------|-------------|----------|
| 0 | Not known | ISO/IEC 5218 |
| 1 | Male | ISO/IEC 5218 |
| 2 | Female | ISO/IEC 5218 |
| 3 | Other | Extended |
| 4 | Inter | Extended |
| 5 | Diverse | Extended |
| 6 | Open | Extended |
| 9 | Not applicable | ISO/IEC 5218 |

## Implementation in Verifiable Credentials

The PID schema extends the base W3C Verifiable Credentials Data Model. A complete PID credential would include:

1. Standard VC properties (`id`, `type`, `issuer`, etc.)
2. The credentialSubject containing the personIdentificationData object
3. Cryptographic proofs for verification

## Usage in Educational Contexts

In educational and professional qualification contexts, the PID serves as:

1. **The foundation for identity verification** during credential issuance and verification
2. **A source of verified personal data** that can be referenced by other credentials
3. **A basis for identity matching** across different educational systems and borders
4. **A trusted identity anchor** for the European Digital Identity framework

## Privacy Considerations

When implementing the PID schema:

- Apply data minimization principles by only requesting necessary attributes
- Implement selective disclosure to share only required identity information
- Ensure appropriate data protection measures are in place
- Respect user consent for data sharing
- Comply with relevant data protection regulations, including GDPR

## Schema Versioning

The PID schema follows the European regulatory requirements and may be updated as these requirements evolve. Implementations should:

- Check for schema updates regularly
- Maintain backward compatibility
- Support validation against the specified schema version
- Handle attributes that may be added in future versions

Current version: 1.0.0 (based on EU regulation referenced in the schema)
