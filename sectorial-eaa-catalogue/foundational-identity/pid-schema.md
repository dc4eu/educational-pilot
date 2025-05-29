# Foundational Identity Schema

## Overview

This document describes the Person Identification Data (PID) model for Natural Persons, which forms the foundation for identity verification across the European education and professional qualifications framework. The model is implemented using the W3C Verifiable Credentials Data Model (VCDM) and conforms to the requirements specified in the European regulation referenced at https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202402977.

## Person Identification Data Structure

The PID credential for natural persons contains a set of standardized attributes that provide reliable identification of individuals:

```json
{
  "credentialSubject": {
      // PID attributes
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

## Full Schema Serialization

Below is the full JSON schema for the Person Identification Data:

```json
{
  "$schema" : "https://json-schema.org/draft/2020-12/schema",
  "title" : "Person Identification Data for the Natural Person",
  "description" : "Reference: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202402977",
  "type" : "object",
  "allOf" : [
    {
      "$ref" : "https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/0xbe77a21356835dc09d3d8149ea832ae0a4bae0ae9c869d18219ef8f4a74b4644"
    },
    {
      "type" : "object",
      "properties" : {
        "credentialSubject" : {
          "type" : "object",
          "properties" : {
            "family_name" : {
              "type" : "string",
              "description" : "Current last name(s) or surname(s) of the user to whom the person identification data relates.",
              "minLength" : 1
            },
            "given_name" : {
              "type" : "string",
              "description" : "Current first name(s), including middle name(s) where applicable, of the user to whom the person identification data relates.",
              "minLength" : 1
            },
            "birth_date" : {
              "type" : "string",
              "format" : "date",
              "description" : "Day, month, and year on which the user to whom the person identification data relates was born."
            },
            "birth_place" : {
              "type" : "string",
              "description" : "The country as an alpha-2 country code as specified in ISO 3166-1, or the state, province, district, or local area or the municipality, city, town, or village where the user to whom the person identification data relates was born."
            },
            "nationality" : {
              "type" : "array",
              "items" : {
                "type" : "string",
                "enum" : [
                  "AF",
                  "AX",
                  "AL",
                  "DZ",
                  "AS",
                  "AD",
                  "AO",
                  "AI",
                  "AQ",
                  "AG",
                  "AR",
                  "AM",
                  "AW",
                  "AU",
                  "AT",
                  "AZ",
                  "BS",
                  "BH",
                  "BD",
                  "BB",
                  "BY",
                  "BE",
                  "BZ",
                  "BJ",
                  "BM",
                  "BT",
                  "BO",
                  "BQ",
                  "BA",
                  "BW",
                  "BV",
                  "BR",
                  "IO",
                  "BN",
                  "BG",
                  "BF",
                  "BI",
                  "CV",
                  "KH",
                  "CM",
                  "CA",
                  "KY",
                  "CF",
                  "TD",
                  "CL",
                  "CN",
                  "CX",
                  "CC",
                  "CO",
                  "KM",
                  "CD",
                  "CG",
                  "CK",
                  "CR",
                  "CI",
                  "HR",
                  "CU",
                  "CW",
                  "CY",
                  "CZ",
                  "DK",
                  "DJ",
                  "DM",
                  "DO",
                  "EC",
                  "EG",
                  "SV",
                  "GQ",
                  "ER",
                  "EE",
                  "SZ",
                  "ET",
                  "FK",
                  "FO",
                  "FJ",
                  "FI",
                  "FR",
                  "GF",
                  "PF",
                  "TF",
                  "GA",
                  "GM",
                  "GE",
                  "DE",
                  "GH",
                  "GI",
                  "GR",
                  "GL",
                  "GD",
                  "GP",
                  "GU",
                  "GT",
                  "GG",
                  "GN",
                  "GW",
                  "GY",
                  "HT",
                  "HM",
                  "VA",
                  "HN",
                  "HK",
                  "HU",
                  "IS",
                  "IN",
                  "ID",
                  "IR",
                  "IQ",
                  "IE",
                  "IM",
                  "IL",
                  "IT",
                  "JM",
                  "JP",
                  "JE",
                  "JO",
                  "KZ",
                  "KE",
                  "KI",
                  "KP",
                  "KR",
                  "KW",
                  "KG",
                  "LA",
                  "LV",
                  "LB",
                  "LS",
                  "LR",
                  "LY",
                  "LI",
                  "LT",
                  "LU",
                  "MO",
                  "MG",
                  "MW",
                  "MY",
                  "MV",
                  "ML",
                  "MT",
                  "MH",
                  "MQ",
                  "MR",
                  "MU",
                  "YT",
                  "MX",
                  "FM",
                  "MD",
                  "MC",
                  "MN",
                  "ME",
                  "MS",
                  "MA",
                  "MZ",
                  "MM",
                  "NA",
                  "NR",
                  "NP",
                  "NL",
                  "NC",
                  "NZ",
                  "NI",
                  "NE",
                  "NG",
                  "NU",
                  "NF",
                  "MK",
                  "MP",
                  "NO",
                  "OM",
                  "PK",
                  "PW",
                  "PS",
                  "PA",
                  "PG",
                  "PY",
                  "PE",
                  "PH",
                  "PN",
                  "PL",
                  "PT",
                  "PR",
                  "QA",
                  "RE",
                  "RO",
                  "RU",
                  "RW",
                  "BL",
                  "SH",
                  "KN",
                  "LC",
                  "MF",
                  "PM",
                  "VC",
                  "WS",
                  "SM",
                  "ST",
                  "SA",
                  "SN",
                  "RS",
                  "SC",
                  "SL",
                  "SG",
                  "SX",
                  "SK",
                  "SI",
                  "SB",
                  "SO",
                  "ZA",
                  "GS",
                  "SS",
                  "ES",
                  "LK",
                  "SD",
                  "SR",
                  "SJ",
                  "SE",
                  "CH",
                  "SY",
                  "TW",
                  "TJ",
                  "TZ",
                  "TH",
                  "TL",
                  "TG",
                  "TK",
                  "TO",
                  "TT",
                  "TN",
                  "TR",
                  "TM",
                  "TC",
                  "TV",
                  "UG",
                  "UA",
                  "AE",
                  "GB",
                  "US",
                  "UM",
                  "UY",
                  "UZ",
                  "VU",
                  "VE",
                  "VN",
                  "VG",
                  "VI",
                  "WF",
                  "EH",
                  "YE",
                  "ZM",
                  "ZW"
                ]
              },
              "description" : "One or more alpha-2 country codes as specified in ISO 3166-1, representing the nationality of the user to whom the person identification data relates."
            },
            "resident_address" : {
              "type" : "string",
              "description" : "The full address of the place where the user to whom the person identification data relates currently resides or can be contacted (street name, house number, city etc.)."
            },
            "resident_country" : {
              "type" : "string",
              "enum" : [
                "AF",
                "AX",
                "AL",
                "DZ",
                "AS",
                "AD",
                "AO",
                "AI",
                "AQ",
                "AG",
                "AR",
                "AM",
                "AW",
                "AU",
                "AT",
                "AZ",
                "BS",
                "BH",
                "BD",
                "BB",
                "BY",
                "BE",
                "BZ",
                "BJ",
                "BM",
                "BT",
                "BO",
                "BQ",
                "BA",
                "BW",
                "BV",
                "BR",
                "IO",
                "BN",
                "BG",
                "BF",
                "BI",
                "CV",
                "KH",
                "CM",
                "CA",
                "KY",
                "CF",
                "TD",
                "CL",
                "CN",
                "CX",
                "CC",
                "CO",
                "KM",
                "CD",
                "CG",
                "CK",
                "CR",
                "CI",
                "HR",
                "CU",
                "CW",
                "CY",
                "CZ",
                "DK",
                "DJ",
                "DM",
                "DO",
                "EC",
                "EG",
                "SV",
                "GQ",
                "ER",
                "EE",
                "SZ",
                "ET",
                "FK",
                "FO",
                "FJ",
                "FI",
                "FR",
                "GF",
                "PF",
                "TF",
                "GA",
                "GM",
                "GE",
                "DE",
                "GH",
                "GI",
                "GR",
                "GL",
                "GD",
                "GP",
                "GU",
                "GT",
                "GG",
                "GN",
                "GW",
                "GY",
                "HT",
                "HM",
                "VA",
                "HN",
                "HK",
                "HU",
                "IS",
                "IN",
                "ID",
                "IR",
                "IQ",
                "IE",
                "IM",
                "IL",
                "IT",
                "JM",
                "JP",
                "JE",
                "JO",
                "KZ",
                "KE",
                "KI",
                "KP",
                "KR",
                "KW",
                "KG",
                "LA",
                "LV",
                "LB",
                "LS",
                "LR",
                "LY",
                "LI",
                "LT",
                "LU",
                "MO",
                "MG",
                "MW",
                "MY",
                "MV",
                "ML",
                "MT",
                "MH",
                "MQ",
                "MR",
                "MU",
                "YT",
                "MX",
                "FM",
                "MD",
                "MC",
                "MN",
                "ME",
                "MS",
                "MA",
                "MZ",
                "MM",
                "NA",
                "NR",
                "NP",
                "NL",
                "NC",
                "NZ",
                "NI",
                "NE",
                "NG",
                "NU",
                "NF",
                "MK",
                "MP",
                "NO",
                "OM",
                "PK",
                "PW",
                "PS",
                "PA",
                "PG",
                "PY",
                "PE",
                "PH",
                "PN",
                "PL",
                "PT",
                "PR",
                "QA",
                "RE",
                "RO",
                "RU",
                "RW",
                "BL",
                "SH",
                "KN",
                "LC",
                "MF",
                "PM",
                "VC",
                "WS",
                "SM",
                "ST",
                "SA",
                "SN",
                "RS",
                "SC",
                "SL",
                "SG",
                "SX",
                "SK",
                "SI",
                "SB",
                "SO",
                "ZA",
                "GS",
                "SS",
                "ES",
                "LK",
                "SD",
                "SR",
                "SJ",
                "SE",
                "CH",
                "SY",
                "TW",
                "TJ",
                "TZ",
                "TH",
                "TL",
                "TG",
                "TK",
                "TO",
                "TT",
                "TN",
                "TR",
                "TM",
                "TC",
                "TV",
                "UG",
                "UA",
                "AE",
                "GB",
                "US",
                "UM",
                "UY",
                "UZ",
                "VU",
                "VE",
                "VN",
                "VG",
                "VI",
                "WF",
                "EH",
                "YE",
                "ZM",
                "ZW"
              ],
              "description" : "The country where the user to whom the person identification data relates currently resides, as an alpha-2 country code as specified in ISO 3166-1."
            },
            "resident_state" : {
              "type" : "string",
              "description" : "The state, province, district, or local area where the user to whom the person identification data relates currently resides."
            },
            "resident_city" : {
              "type" : "string",
              "description" : "The municipality, city, town, or village where the user to whom the person identification data relates currently resides."
            },
            "resident_postal_code" : {
              "type" : "string",
              "description" : "The postal code of the place where the user to whom the person identification data relates currently resides."
            },
            "resident_street" : {
              "type" : "string",
              "description" : "The name of the street where the user to whom the person identification data relates currently resides."
            },
            "resident_house_number" : {
              "type" : "string",
              "description" : "The house number where the user to whom the person identification data relates currently resides, including any affix or suffix."
            },
            "personal_administrative_number" : {
              "type" : "string",
              "description" : "A value assigned to the natural person that is unique among all personal administrative numbers issued by the provider of person identification data. Where Member States opt to include this attribute, they shall describe in their electronic identification schemes under which the person identification data is issued, the policy that they apply to the values of this attribute, including, where applicable, specific conditions for the processing of this value."
            },
            "portrait" : {
              "type" : "string",
              "description" : "Facial image of the wallet user compliant with ISO 19794-5 or ISO 39794 specifications."
            },
            "family_name_birth" : {
              "type" : "string",
              "description" : "Last name(s) or surname(s) of the person identification data user at the time of birth."
            },
            "given_name_birth" : {
              "type" : "string",
              "description" : "First name(s), including middle name(s), of the person identification data user at the time of birth."
            },
            "sex" : {
              "type" : "integer",
              "enum" : [
                0,
                1,
                2,
                3,
                4,
                5,
                6,
                9
              ],
              "description" : "Sex of the user. Values: 0 = not known, 1 = male, 2 = female, 3 = other, 4 = inter, 5 = diverse, 6 = open, 9 = not applicable. For values 0, 1, 2 and 9, ISO/IEC 5218 applies."
            },
            "email_address" : {
              "type" : "string",
              "format" : "email",
              "description" : "Electronic mail address of the user to whom the person identification data relates [in conformance with RFC 5322]."
            },
            "mobile_phone_number" : {
              "type" : "string",
              "pattern" : "^\\+\\d+$",
              "description" : "Mobile telephone number of the user to whom the person identification data relates, starting with the ‘+’ symbol as the international code prefix and the country code, followed by numbers only."
            },
            "expiry_date" : {
              "type" : "string",
              "format" : "date-time",
              "description" : "Date (and if possible time) when the person identification data will expire."
            },
            "document_number" : {
              "type" : "string",
              "description" : "A number for the person identification data, assigned by the provider of person identification data.",
              "nullable" : true
            },
            "issuing_authority" : {
              "type" : "string",
              "description" : "Name of the administrative authority that issued the person identification data, or the ISO 3166 alpha-2 country code of the respective Member State if there is no separate authority entitled to issue person identification data."
            },
            "issuing_country" : {
              "type" : "string",
              "pattern" : "^[A-Z]{2}$",
              "description" : "Alpha-2 country code, as specified in ISO 3166-1, of the country or territory of the provider of the person identification data."
            },
            "issuing_jurisdiction" : {
              "type" : "string",
              "pattern" : "^[A-Z]{2}(-[A-Za-z0-9]{1,3})?$",
              "description" : "Country subdivision code of the jurisdiction that issued the person identification data, as specified in ISO 3166-2:2020, Clause 8. The first part of the code shall be the same as the value for the issuing country.",
              "nullable" : true
            },
            "location_status" : {
              "type" : "string",
              "description" : "The location of validity status information on the person identification data where the providers of person identification data revoke person identification data.",
              "nullable" : true
            }
          },
          "required" : [
            "family_name",
            "given_name",
            "birth_date",
            "birth_place",
            "nationality",
            "expiry_date",
            "issuing_authority",
            "issuing_country"
          ]
        }
      }
    }
  ]
}
```

## Example Credential

Here's an example of a PID credential:

```json
{
  "@context": [
    "https://www.w3.org/2018/credentials/v1",
    "https://europa.eu/2024/credentials/pid/v1"
  ],
  "id": "urn:uuid:3add94f4-28ec-42a1-8704-bb5c99c6bf2f",
  "type": ["VerifiableCredential", "PersonIdentificationData"],
  "issuer": "did:ebsi:zgh4Xd45QP6qTSw9ixth9a",
  "issuanceDate": "2024-01-15T12:30:45Z",
  "validFrom": "2024-01-15T12:30:45Z",
  "expirationDate": "2029-01-14T23:59:59Z",
  "credentialSubject": {
    "id": "did:ebsi:zb9Jhi4RMW1JUP3JFJPmk5",
    "personIdentificationData": {
      "family_name": "García",
      "given_name": "María Elena",
      "birth_date": "1990-05-12",
      "birth_place": "ES",
      "nationality": ["ES"],
      "resident_address": "Calle Mayor 123, 28001 Madrid",
      "resident_country": "ES",
      "resident_city": "Madrid",
      "resident_postal_code": "28001",
      "resident_street": "Calle Mayor",
      "resident_house_number": "123",
      "email_address": "maria.garcia@example.com",
      "mobile_phone_number": "+34612345678",
      "sex": 2,
      "expiry_date": "2029-01-14T23:59:59Z",
      "issuing_authority": "Ministry of Interior",
      "issuing_country": "ES"
    }
  },
  "proof": {
    "type": "EcdsaSecp256k1Signature2019",
    "created": "2024-01-15T12:30:45Z",
    "proofPurpose": "assertionMethod",
    "verificationMethod": "did:ebsi:zgh4Xd45QP6qTSw9ixth9a#keys-1",
    "jws": "eyJhbGciOiJFUzI1NksiLCJiNjQiOmZhbHNlLCJjcml0IjpbImI2NCJdfQ..kUGw-vrfwAdcVLrRhOzLWi-QgDTrVJHCEkK3PUbCQ4qR69KCxtprKmSyV1HzVGOJ2-_YgGK77JJi5vMGQP3IHw"
  }
}
```

## Schema Versioning

The PID schema follows the European regulatory requirements and may be updated as these requirements evolve. Implementations should:

- Check for schema updates regularly
- Maintain backward compatibility
- Support validation against the specified schema version
- Handle attributes that may be added in future versions

Current version: 1.0.0 (based on EU regulation referenced in the schema)
