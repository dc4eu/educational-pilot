# Wallet Relying Party PKI Guidelines

**Author**: Nacho Alamillo, Logalty  
**Date**: 17th July 2025  
**Version**: 2.0  
**Scope**: PKI orientations for WP5 piloting in DC4EU project

## Overview

This document provides comprehensive guidelines for implementing Public Key Infrastructure (PKI) for **Wallet Relying Parties (WRPs)** within the **DC4EU (Digital Credentials for Europe)** framework. It specifies the technical requirements for organisations that intend to rely upon wallet units for the provision of public or private services through digital interaction.

## Regulatory Foundation

### Primary Reference
**Commission Implementing Regulation (EU) 2025/848** of 6 May 2025 laying down rules for the application of Regulation (EU) No 910/2014 as regards the registration of wallet-relying parties (CIR on WRP).

### Key Definitions

| Term | Definition |
|------|------------|
| **Wallet-relying party** | A relying party that intends to rely upon wallet units for the provision of public or private services by means of digital interaction |
| **Registrar of wallet-relying parties** | The body responsible for establishing and maintaining the list of registered wallet-relying parties in their territory |
| **Wallet-relying party access certificate (WRPAC)** | A **certificate for electronic seals or signatures** authenticating and validating the wallet-relying party |
| **Wallet-relying party registration certificate (WRPRC)** | A **data object** that describes the **intended use** of the relying party and **indicates the attributes** the relying party has registered to request from users |
| **Provider of WRPAC** | Natural or legal person mandated by a Member State to issue wallet-relying party access certificates |
| **Provider of WRPRC** | Natural or legal person mandated by a Member State to issue wallet-relying party registration certificates |

## Certificate Architecture

### Wallet-Relying Party Access Certificates (WRPAC)

**Legal Framework**: Article 7 of CIR on WRP

#### Requirements
- **Authority Designation**: Member States shall authorise at least one certificate authority to issue WRPACs
- **Exclusive Issuance**: Only registered wallet-relying parties may receive WRPACs
- **Harmonised Implementation**: Certificate policies and practice statements must be syntactically and semantically harmonised across the Union
- **Technical Standard**: Compliance with Annex IV requirements

#### Certificate Structure (X.509v3 Format)

| **Certificate Attribute** | **Legal Person Encoding** | **Natural Person Encoding** |
|---------------------------|----------------------------|------------------------------|
| **Subject** | `organizationName` as per ETSI EN 319 412-3 clause 4.2.1 | Choice of (`givenName` and/or `surname`) as per ETSI EN 319 412-2 clause 4.2.4 |
| **User-friendly name** | `commonName` as per ETSI EN 319 412-3 clause 4.2.1 | `commonName` as per ETSI EN 319 412-2 clause 4.2.4 |
| **Identifier** | `organizationIdentifier` as per ETSI EN 319 412-1 clause 5.1.4 | `serialNumber` as per ETSI EN 319 412-1 clause 5.1.3 |
| **URL** | Subject Alternative Name URI as per RFC 5280 clause 4.2.1.6 | Subject Alternative Name URI as per RFC 5280 clause 4.2.1.6 |
| **Country code** | `countryName` as per ETSI EN 319 412-3 clause 4.2.1 | `countryName` as per ETSI EN 319 412-2 clause 4.2.4 |

### Wallet-Relying Party Registration Certificates (WRPRC)

**Legal Framework**: Article 8 of CIR on WRP

#### Requirements
- **Optional Implementation**: Member States may authorise certificate authorities for WRPRC issuance
- **Exclusive Issuance**: Only registered wallet-relying parties eligible
- **Intended Use Expression**: Each intended use must be clearly expressed
- **General Access Policy**: Harmonised policy informing users of data request limitations
- **Privacy Policy URL**: Mandatory inclusion of privacy policy reference

#### Token Structure (JWT/CWT Format)

##### Header Components
- **`typ`**: Token type (`rc-wrp+jwt` for JWT, `rc-wrp+cwt` for CWT)
- **`alg`**: Signature algorithm
- **`x5c`**: Complete certificate chain for verification
- **`b64`**: Value `true` (compact serialisation)
- **`crt`**: List with value `"b64"`

##### Payload Components
- **`sub`**: Subject of the WRPRC
- **`service`**: Service description with multi-language support
  - `lang`: BCP47 language tag (RFC5646)
  - `value`: Service description
- **`entitlements`**: List of assigned entitlements (see Entitlements section)
- **`privacy_policy`**: URL to privacy policy
- **`certificate_policy`**: URL to certificate policy and practice statement
- **`iat`**: Unix timestamp of issuance
- **`status`**: URI to status list for validity information

## WRP Entitlements Framework

### Entitlement Categories
As defined in Annex I.12 of the regulation:

| **Entitlement ID** | **Description** | **OID** | **URI** |
|-------------------|-----------------|---------|---------|
| `Service_Provider` | General service provider | `id-etsi-wrpa-entitlement 1` | `https://uri.etsi.org/19475/Entitlement/Service_Provider` |
| `QEAA_Provider` | Qualified trust service provider issuing qualified electronic attestations of attributes | `id-etsi-wrpa-entitlement 2` | `https://uri.etsi.org/19475/Entitlement/QEAA_Provider` |
| `Non_Q_EAA_Provider` | Trust service provider issuing non-qualified electronic attestations of attributes | `id-etsi-wrpa-entitlement 3` | `https://uri.etsi.org/19475/Entitlement/Non_Q_EAA_Provider` |
| `PUB_EAA_Provider` | Public sector body issuing electronic attestations from authentic sources | `id-etsi-wrpa-entitlement 4` | `https://uri.etsi.org/19475/Entitlement/PUB_EAA_Provider` |
| `PID_Provider` | Provider of person identification data | `id-etsi-wrpa-entitlement 5` | `https://uri.etsi.org/19475/Entitlement/PID_Provider` |
| `QCert_for_ESeal_Provider` | Qualified trust service provider issuing qualified certificates for electronic seals | `id-etsi-wrpa-entitlement 6` | `https://uri.etsi.org/19475/Entitlement/QCert_for_ESeal_Provider` |
| `QCert_for_ESig_Provider` | Qualified trust service provider issuing qualified certificates for electronic signatures | `id-etsi-wrpa-entitlement 7` | `https://uri.etsi.org/19475/Entitlement/QCert_for_ESig_Provider` |
| `rQSigCDs_Provider` | Qualified trust service provider managing remote qualified electronic signature creation devices | `id-etsi-wrpa-entitlement 9` | `https://uri.etsi.org/19475/Entitlement/rQSigCDs_Provider` |
| `rQSealCDs_Provider` | Qualified trust service provider managing remote qualified electronic seal creation devices | `id-etsi-wrpa-entitlement 8` | `https://uri.etsi.org/19475/Entitlement/rQSealCDs_Provider` |
| `ESig_ESeal_Creation_Provider` | Non-qualified provider for remote signature/seal creation | `id-etsi-wrpa-entitlement 10` | `https://uri.etsi.org/19475/Entitlement/ESig_ESeal_Creation_Provider` |

### OID Arc Structure
```
id-etsi-wrpa-entitlement OBJECT IDENTIFIER ::=
{ itu-t(0) identified-organization(4) etsi(0) eudiwrpa(19475) entitlement(1)}
```

## Implementation Guidelines for DC4EU Pilot

### WRPAC Naming Scheme

| **Component** | **Field** | **Description** |
|---------------|-----------|-----------------|
| **SubjectName** |  |  |
|  | `countryName (C)` | Country where the WRP is registered |
|  | `organizationName (O)` | Legal name of the WRP |
|  | `organisationIdentifier (OI)` | Identifier of the WRP (e.g., TIN, LEI, EUDI) |
|  | `commonName (CN)` | Friendly name of the WRP |
| **SubjectAlternativeName** |  |  |
|  | `dnsName` | URL (IA5String format) |
|  | `registeredID (1..n)` | `0.4.0.19495.1.x` where x represents the entitlement |
|  | `distinguishedName` |  |
|  | `organisationalUnitName (OU)` | Service description |

### Technical Specifications

#### Cryptographic Requirements
- **Key Types**: EC (P-256, P-384, P-521) or RSA (minimum 2048-bit)
- **Signature Algorithms**: ES256, ES384, ES512, RS256, RS384, RS512
- **Hash Functions**: SHA-256 or stronger
- **Certificate Validity**: As determined by issuing CA policy

#### Compliance Standards
- **ETSI EN 319 412** series for certificate profiles
- **RFC 5280** for X.509 certificate and CRL profiles
- **RFC 7519** for JSON Web Token (JWT)
- **RFC 8392** for CBOR Web Token (CWT)
- **RFC 5646** for language tags

## Registration Process

### Step 1: WRP Registration
1. **Legal Entity Verification**: Establish legal status and jurisdiction
2. **Service Definition**: Clearly define intended digital services
3. **Entitlement Selection**: Choose appropriate entitlements from the framework
4. **Technical Capability Assessment**: Demonstrate ability to handle digital credentials

### Step 2: Certificate Issuance
1. **Certificate Authority Selection**: Choose an authorised WRPAC provider
2. **Certificate Signing Request (CSR)**: Generate CSR with appropriate subject information
3. **Identity Verification**: Complete identity verification process
4. **Certificate Delivery**: Receive WRPAC and any associated WRPRC

### Step 3: Integration
1. **Technical Integration**: Implement certificate in wallet relying systems
2. **Protocol Compliance**: Ensure compliance with EUDIW protocols
3. **Testing**: Conduct interoperability testing with pilot partners
4. **Operational Deployment**: Begin production use

## Security Considerations

### Certificate Management
- **Secure Storage**: Store private keys in Hardware Security Modules (HSMs)
- **Access Control**: Implement robust access controls for certificate operations
- **Backup and Recovery**: Establish certificate backup and recovery procedures
- **Lifecycle Management**: Plan for certificate renewal and revocation

### Operational Security
- **Monitoring**: Implement certificate status monitoring
- **Incident Response**: Establish procedures for security incidents
- **Audit Logging**: Maintain comprehensive audit logs
- **Compliance Monitoring**: Regular compliance assessments

## Privacy Considerations

### Data Minimisation
- **Purpose Limitation**: Only request necessary attributes
- **Consent Management**: Implement clear consent mechanisms
- **Data Retention**: Define appropriate data retention policies
- **User Rights**: Support user rights under GDPR

### Transparency
- **Privacy Policies**: Maintain clear, accessible privacy policies
- **Data Processing Information**: Provide transparent information about data processing
- **User Control**: Enable user control over data sharing

## Integration with EBSI

### Trust Verification
- **DID Resolution**: Verify issuer identities through EBSI DID Registry
- **Accreditation Validation**: Check issuer accreditations via Trusted Issuers Registry
- **Schema Compliance**: Validate credential schemas against Trusted Schema Registry

### Interoperability
- **Cross-border Recognition**: Ensure certificates work across EU member states
- **Standard Compliance**: Adhere to EBSI technical specifications
- **Protocol Support**: Implement required EBSI protocols

## Conclusion

This PKI framework for Wallet Relying Parties provides the foundation for trusted digital credential verification within the DC4EU ecosystem. By following these guidelines, organisations can:

- **Establish Trust**: Build reliable relationships with digital wallet users
- **Ensure Compliance**: Meet regulatory requirements across the European Union
- **Enable Interoperability**: Participate in the broader European digital identity ecosystem
- **Protect Users**: Implement privacy-preserving credential verification

For detailed implementation of the issuer side of this ecosystem, please refer to the [X.509-DID Binding Guide for Credential Issuers](./x509-did-binding-guide.md).

## References

- Commission Implementing Regulation (EU) 2025/848
- ETSI EN 319 412 series
- RFC 5280 - Internet X.509 Public Key Infrastructure
- RFC 7519 - JSON Web Token (JWT)
- RFC 8392 - CBOR Web Token (CWT)
- eIDAS Regulation (EU) No 910/2014

---

*This document is part of the DC4EU project deliverables for Work Package 5 (WP5) piloting activities.*