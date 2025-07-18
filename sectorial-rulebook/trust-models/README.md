# DC4EU Digital Trust Framework - Overview

## Introduction

The **Digital Credentials for Europe (DC4EU)** project establishes a comprehensive digital trust framework that enables secure issuance, presentation, and verification of Electronic Attestations of Attributes (EAAs) within the European Digital Identity Wallet (EUDIW) ecosystem.

## Trust Models Foundation

### **Regulatory and Trust Framework Context**
[**Trust Models for Education and Professional Qualifications**](./trust-models-education.md)  
**Essential background**: Understanding classical PKI limitations and the complementary dPKI model under eIDAS2

> **Recommended Reading Order**: Start with Trust Models foundation to understand the regulatory context and why both classical PKI and dPKI are needed, then proceed to implementation guidance below.

This framework comprises two complementary Public Key Infrastructure (PKI) models that work together to create an end-to-end trust architecture, addressing both **identity verification** (classical PKI) and **authorisation validation** (dPKI) as outlined in the Trust Models foundation document:

1. **Wallet Relying Party PKI** - Authenticates entities that consume digital credentials
2. **Issuer Trust Model** - Enables entities to issue trusted digital credentials using hybrid X.509/DID technology

## Architecture Overview

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────────┐
│   CREDENTIAL    │    │                  │    │    CREDENTIAL       │
│    ISSUERS      │    │      EUDIW       │    │    CONSUMERS        │
│                 │    │   (EU Digital    │    │  (Relying Parties)  │
│ • Universities  │───▶│   ID Wallet)     │───▶│ • Employers         │
│ • Gov. Bodies   │    │                  │    │ • Service Providers │
│ • TSPs          │    │                  │    │ • Verification Svcs │
└─────────────────┘    └──────────────────┘    └─────────────────────┘
         │                       │                         │
         ▼                       ▼                         ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────────┐
│ Pure dPKI or    │    │      EBSI        │    │   WRP PKI Model     │
│ Hybrid Models   │    │  (Trust Anchor)  │    │                     │
│                 │    │                  │    │ • WRPAC Certificates│
│ • Pure dPKI     │    │ • DID Registry   │    │ • WRPRC Tokens      │
│ • X.509+DID     │    │ • Accreditations │    │ • Entitlements      │
│ • JAdES D-Zero  │    │ • Trust Lists    │    │                     │
└─────────────────┘    └──────────────────┘    └─────────────────────┘
```

## Trust Flow Process

### 1. **Issuer Registration and Setup**
- Legal entities register with EBSI and also obtain X.509v3 certificates
- Bind X.509v3 certificates to Decentralised Identifiers (DIDs) for enhanced trust
- Register as authorised credential issuers in EBSI registries

### 2. **Relying Party Registration**
- Service providers register as Wallet Relying Parties (WRPs)
- Obtain Wallet Relying Party Access Certificates (WRPAC)
- Receive appropriate entitlements for their service category

### 3. **Credential Lifecycle**
- **Issuance**: Authorised issuers create EAAs signed with X.509/DID-bound keys
- **Storage**: Credentials stored securely in EUDIW
- **Presentation**: Users present credentials to verified relying parties
- **Verification**: Relying parties validate credentials using EBSI trust infrastructure

## Key Components

### EBSI (European Blockchain Services Infrastructure)
- **Central trust anchor** for the European digital identity ecosystem
- **DID Registry**: Manages decentralised identifiers for all participants
- **Trusted Issuers Registry**: Maintains accreditations and authorisations
- **Trusted Schema Registry**: Ensures credential format compliance

### Hybrid PKI Architecture
- **Traditional X.509 PKI**: Provides established certificate-based trust
- **Decentralised PKI (dPKI)**: Offers blockchain-anchored identity verification
- **Combined Model**: Leverages strengths of both approaches for maximum interoperability

## Regulatory Compliance

Both PKI models ensure full compliance with:
- **eIDAS Regulation** (EU) No 910/2014 and amendments
- **Commission Implementing Regulation** (EU) 2025/848
- **ETSI standards** for digital certificates and trust services
- **W3C Verifiable Credentials** specification

## Implementation Scenarios

### Scenario 2 Focus
This framework specifically addresses **DC4EU Scenario 2**:
- Non-qualified Trust Service Providers (TSPs)
- Public sector bodies as authentic data sources
- Enhanced trust through EBSI verification
- Example: Universitat Rovira i Virgili issuing academic credentials

## Benefits

### For Issuers
- **Enhanced Trust**: EBSI accreditation increases credential reliability
- **Interoperability**: Standards-based approach ensures cross-border acceptance
- **Flexibility**: Hybrid model accommodates various organisational PKI setups

### For Relying Parties
- **Verified Identity**: WRPAC ensures authentic service provider identity
- **Clear Entitlements**: Transparent permissions for data access
- **Automated Verification**: Streamlined credential validation processes

### For Users
- **Control**: Manage credential sharing through EUDIW
- **Privacy**: Minimal data disclosure principles
- **Portability**: Credentials work across European Union member states

## Technical Standards

- **Certificate Format**: X.509v3 for traditional PKI components
- **Token Format**: JWT/CWT for modern registration certificates
- **Signature Algorithms**: ES256/ES256K for cryptographic operations
- **Key Management**: Hardware Security Module (HSM) recommendations
- **Binding Method**: SHA-256 certificate thumbprints (x5t#S256)

## Implementation Approaches

The DC4EU framework supports multiple implementation approaches for credential issuance and verification:

### **Pure dPKI Implementation**
For organisations implementing purely decentralised PKI without traditional certificate integration:

### **Hybrid X.509-DID Implementation** 
For organisations requiring integration between traditional PKI infrastructure and decentralised identity systems:

## Implementation Guidance

### **For All Relying Parties**
[**Wallet Relying Party PKI Guidelines**](./wallet-relying-party-pki.md)  
Comprehensive guide for credential verification, WRPAC/WRPRC implementation, and entitlements framework

---

### **For Credential Issuers - Choose Your Approach**

#### Pure dPKI Implementation
[**EUHEMC JAdES D-Zero Signature Guide**](./issaunce_detailed.md)  
Complete signing process using pure dPKI with EBSI, JAdES D-Zero profile implementation

[**EUHEMC JAdES D-Zero Verification Guide**](./verification-details.md)  
Step-by-step verification with practical code examples, tools, and troubleshooting

#### Hybrid X.509-DID Implementation
[**X.509-DID Binding Guide for Credential Issuers**](./x509-did-binding-guide.md)  
Advanced hybrid approach combining traditional PKI with DID binding, EBSI integration workflows

---

### **Architecture Decision Support**

[**Hybrid PKI Impact Analysis: X.509-DID vs Pure dPKI**](./hybrid-pki-impact-analysis.md)  
**Essential reading before implementation**: Comprehensive comparison, performance impact analysis, migration strategies, and technical trade-offs

[**Hybrid vs Pure dPKI: Key Differences and Impact**](./hybrid-vs-pure-dpki-differences.md)  
**Focused technical comparison**: Direct side-by-side analysis of implementation differences, code examples, and performance implications

> **Implementation Recommendation**: Start with the Impact Analysis document to understand the technical and business implications of each approach, then review the Key Differences guide for specific implementation details, and finally follow the specific implementation guide for your chosen model.

## Support and Resources

- **DC4EU Project**: [Official Website]
- **EBSI Documentation**: [Technical Specifications]
- **eIDAS Regulation**: [Legal Framework]
- **Implementation Support**: [Contact Information]

---

*This overview provides a high-level understanding of the DC4EU trust framework. For technical implementation details, security considerations, and step-by-step procedures, please consult the detailed guides linked above.*