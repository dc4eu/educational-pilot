# Chapter 1: foundational identity data models

## Introduction

Foundational identity data models form the bedrock of trust within the DC4EU sectoral EAA catalogue. These models operate under the **eID legal regime** established by eIDAS2 and provide the essential identity verification mechanisms that enable all subsequent digital credential interactions within the European digital identity wallet (EUDIW) ecosystem.

Unlike electronic attestations of attributes (EAAs) that operate under the trust services legal regime, foundational identity credentials establish the legal identity of natural persons and legal entities, serving as the authoritative source of identity information that underpins the entire digital credentials framework.

## Legal framework and regulatory compliance

### eIDAS2 and the eID legal regime

Foundational identity credentials are governed by the eID legal regime under the revised eIDAS regulation (eIDAS2), which establishes stringent requirements for:

- **Legal recognition**: foundational identity credentials must be legally recognised across all EU member states
- **High level of assurance**: these credentials require the highest levels of identity verification and security
- **Interoperability**: technical standards ensure seamless cross-border recognition and verification
- **Privacy protection**: advanced privacy-preserving mechanisms protect sensitive identity information

### European architecture and reference framework (ARF)

The foundational identity models conform to the European architecture and reference framework, ensuring:

- **Standardised data structures**: common schemas across member states facilitate interoperability
- **Trust framework alignment**: integration with European trust infrastructures and registries
- **Security requirements**: implementation of robust cryptographic protections and secure lifecycle management
- **User control**: emphasis on user sovereignty and consent-based information sharing

## 1.1 Person identifier (PID) specification

### Overview and purpose

The person identification data (PID) represents the cornerstone of foundational identity within the DC4EU ecosystem. As a qualified electronic attestation of attributes (QEAA), the PID provides unique, legally recognised identification for natural persons across all European member states.

### Legal and regulatory foundation

The PID specification is based on European regulation [OJ:L_202402977](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202402977), ensuring compliance with the first batch of eIDAS implementing acts and full integration with the EUDIW framework.

### Core data structure

The PID credential is structured using the W3C verifiable credentials data model (VCDM) v1.1, providing international interoperability whilst maintaining European legal requirements:

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
      // PID attributes as defined below
    }
  }
}
```

### Mandatory attributes

All PID credentials must include the following core identification attributes:

| Attribute | Description | Format | Example |
|-----------|-------------|--------|---------|
| `family_name` | Current last name(s) or surname(s) | String (non-empty) | "García" |
| `given_name` | Current first name(s), including middle names | String (non-empty) | "María Elena" |
| `birth_date` | Day, month, and year of birth | Date (ISO 8601) | "1990-05-12" |
| `birth_place` | Country where person was born | String (ISO 3166-1 alpha-2) | "ES" |
| `nationality` | One or more nationalities | Array of ISO 3166-1 alpha-2 | ["ES"] |
| `expiry_date` | When identification data expires | Date-time (ISO 8601) | "2029-01-14T23:59:59Z" |
| `issuing_authority` | Authority that issued the data | String | "Ministry of Interior" |
| `issuing_country` | Country of issuing authority | ISO 3166-1 alpha-2 | "ES" |

### Optional attributes

The PID schema supports additional attributes to provide comprehensive identification:

#### Address information
- `resident_address`: complete current address
- `resident_country`: country of residence (ISO 3166-1 alpha-2)
- `resident_state`: state, province, or region
- `resident_city`: municipality or city
- `resident_postal_code`: postal code
- `resident_street`: street name
- `resident_house_number`: house number with any affixes

#### Personal identification
- `personal_administrative_number`: unique identifier from issuing authority
- `portrait`: facial image (ISO 19794-5 or ISO 39794 compliant)
- `family_name_birth`: birth surname if different from current
- `given_name_birth`: birth given names if different from current
- `sex`: gender indicator using ISO/IEC 5218 values (0-9)
- `document_number`: specific document identifier

#### Contact information
- `email_address`: electronic mail address (RFC 5322 compliant)
- `mobile_phone_number`: mobile number with country code

### Sex attribute enumeration

The optional `sex` attribute uses standardised enumeration values:

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

### EAA characterisation

The PID is characterised within the DC4EU framework as follows:

```json
{
  "eaa_id": "PID",
  "title": "Person Identifier (PID)",
  "description": "Foundational identity credential representing a unique, legal, and verifiable identifier for natural persons across Member States, aligned with eIDAS 2.0 and ARF.",
  "credential_type": "QEAA",
  "sectoral_scope": "CrossSectoral",
  "issuable_by": {
    "authorised_roles": ["PIDAccreditedAuthority"],
    "taor_required": true
  },
  "requires_pid": false,
  "disclosure_policy": {
    "restricted_access": true,
    "verifier_role_check": true,
    "confidentiality_level": "confidential"
  },
  "revocation_support": {
    "method": "StatusList2021",
    "supports_suspension": true
  }
}
```

### Privacy and selective disclosure

The PID implementation emphasises privacy protection through:

- **Selective disclosure**: users can share only necessary attributes for specific verification purposes
- **Zero-knowledge proofs**: advanced cryptographic mechanisms enable verification without revealing sensitive data
- **Purpose limitation**: verifiers can only access information relevant to their declared purposes
- **Consent management**: users maintain granular control over information sharing decisions

### Cross-border recognition

The PID's design ensures seamless cross-border functionality:

- **Mutual recognition**: eIDAS2 mandates acceptance across all EU member states
- **Standardised verification**: common technical protocols enable automated recognition
- **Legal equivalence**: PID credentials carry legal weight equivalent to physical identity documents
- **Quality assurance**: trust registries ensure credential authenticity and issuer authorisation

## 1.2 Legal entity identification models

### Overview and institutional context

Legal entity identification models provide standardised digital identification for educational institutions, professional organisations, and other entities within the DC4EU ecosystem. These models ensure that credential-issuing organisations can be reliably identified, verified, and trusted across European borders.

### Key components

#### Organisational identifiers
- **Legal entity identifiers (LEI)**: globally unique identification codes
- **National registration numbers**: country-specific business registration identifiers
- **Educational institution codes**: sector-specific institutional identifiers
- **SCHAC home organisation**: standardised academic community identifiers

#### Digital identity infrastructure
- **Decentralised identifiers (DIDs)**: blockchain-based institutional identifiers registered in EBSI
- **Qualified electronic seals**: cryptographic credentials for institutional authentication
- **X.509v3 certificates**: PKI-based institutional certificates for secure communications
- **Certificate-DID binding**: cryptographic linkage between traditional PKI and decentralised identity

#### Institutional metadata
- **Accreditation information**: official recognition and authorisation status
- **Operational scope**: types of credentials the institution is authorised to issue
- **Quality assurance**: alignment with European and national quality frameworks
- **Contact and location data**: official institutional contact information and addresses

### Trust service provider registration

Under eIDAS2, educational institutions must register as trust service providers (TSPs), requiring:

- **Legal identity verification**: comprehensive validation of institutional legal status
- **Authorisation documentation**: proof of educational accreditation and scope of authority
- **Technical compliance**: implementation of required security and operational standards
- **Ongoing monitoring**: continuous compliance verification and audit requirements

### Integration with trust registries

Legal entities must register in multiple interconnected trust registries:

#### Trusted issuer registry (TIR)
- Maps institutional DIDs to authorised credential types
- Provides verifiable authorisation information
- Enables automated issuer verification
- Supports dynamic scope management

#### Trusted accreditation organisation registry (TAOR)
- Lists entities authorised to accredit educational institutions
- Enables verification of accreditation chains
- Supports cross-border recognition of quality assurance
- Maintains accreditation status information

#### Trusted schema registry (TSR)
- Associates credential schemas with authorised issuers
- Defines disclosure policies and verification requirements
- Provides machine-readable policy information
- Enables automated compliance checking

## 1.3 Cross-border identity verification

### European interoperability framework

Cross-border identity verification within the DC4EU ecosystem operates through a comprehensive framework that ensures seamless recognition and verification of foundational identity credentials across all European member states.

### eIDAS node integration

The system integrates with eIDAS nodes to provide:

- **Cross-border authentication**: automated verification of foreign identity credentials
- **Level of assurance mapping**: standardised confidence levels across different national systems
- **Attribute translation**: semantic mapping between different national identity schemas
- **Trust chain validation**: verification of credential authenticity across jurisdictional boundaries

### Mutual recognition mechanisms

#### Technical interoperability
- **Standardised schemas**: common data models ensure technical compatibility
- **Unified verification protocols**: shared verification procedures across member states
- **Cryptographic compatibility**: aligned cryptographic standards and algorithms
- **Status checking**: real-time verification of credential validity and revocation status

#### Legal recognition framework
- **Legal equivalence**: foundational identity credentials carry equal legal weight across the EU
- **Regulatory alignment**: harmonised implementation of eIDAS2 requirements
- **Dispute resolution**: established procedures for cross-border verification disputes
- **Liability frameworks**: clear responsibility allocation for cross-border verification failures

### Privacy-preserving protocols

Cross-border verification implements advanced privacy protection:

#### Minimal disclosure principles
- **Purpose limitation**: verification requests must specify legitimate purposes
- **Data minimisation**: only necessary attributes are shared across borders
- **Consent requirements**: user consent for cross-border information sharing
- **Retention limitations**: strict controls on retention of shared identity information

#### Advanced cryptographic protection
- **Zero-knowledge proofs**: verification without revealing sensitive identity details
- **Attribute-based credentials**: sharing of specific attributes rather than complete identity profiles
- **Unlinkability**: prevention of cross-border identity correlation without user consent
- **Forward privacy**: protection against future correlation of historical verification activities

## Implementation considerations

### Technical requirements

Implementing foundational identity data models requires:

- **EUDIW integration**: compatibility with European digital identity wallet protocols
- **EBSI connectivity**: connection to European blockchain services infrastructure
- **PKI infrastructure**: robust public key infrastructure for classical cryptographic operations
- **HSM deployment**: hardware security modules for cryptographic key protection

### Governance and compliance

Successful implementation demands:

- **Regulatory compliance**: adherence to eIDAS2 and national implementation requirements
- **Quality assurance**: alignment with European and national quality frameworks
- **Audit capabilities**: comprehensive logging and monitoring for compliance verification
- **Cross-border coordination**: alignment with other member states' implementation approaches

### User experience design

Foundational identity systems must provide:

- **Intuitive interfaces**: user-friendly access to identity management capabilities
- **Transparent control**: clear information about identity data usage and sharing
- **Seamless integration**: smooth interaction with educational and professional services
- **Accessibility compliance**: support for users with diverse needs and capabilities

## Future evolution and standards alignment

### Emerging technologies

The foundational identity framework is designed to accommodate:

- **Quantum-resistant cryptography**: preparation for post-quantum cryptographic migration
- **Enhanced biometric integration**: support for advanced biometric verification methods
- **AI-assisted verification**: intelligent automation of identity verification processes
- **Blockchain innovations**: leverage of emerging blockchain and distributed ledger technologies

### International alignment

Future development will consider:

- **Global standards compatibility**: alignment with international identity standards
- **Third country recognition**: potential extension of recognition beyond the EU
- **Commercial ecosystem integration**: connection with global digital identity ecosystems
- **Technology neutrality**: support for diverse technological approaches and implementations

This foundational identity framework establishes the essential trust infrastructure that enables all other digital credentials within the DC4EU ecosystem, providing the security, interoperability, and legal recognition necessary for Europe's digital education and professional qualifications transformation.