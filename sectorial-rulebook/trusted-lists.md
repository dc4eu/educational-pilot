# Trusted Lists

## Overview

The system maintains several critical lists to support trust in educational credentials across three distinct implementation approaches. Within the trust framework, these lists support European education policy through interconnected registries that establish trust across the educational ecosystem, whilst accommodating different verification methodologies deployed in the DC4EU pilots.

## Key Components

### Trusted Issuers
- Authorised organisations that can issue credentials
- Ensures only legitimate institutions can grant qualifications
- Maintains academic integrity by authorising legitimate institutions
- Links to national and European educational registries
- **Implementation varies by pilot approach** (detailed in verification sections below)

### Relying Parties
- Organisations authorised to verify and accept credentials
- Creates clear paths for credential recognition
- Supports trustworthy verification processes
- Enables appropriate usage of educational credentials
- **Verification mechanisms differ across Classical PKI, dPKI, and Hybrid modes**

### Trusted Accreditation Organisations
- Bodies that validate educational institutions
- Maintains quality standards
- Links to European quality frameworks such as EQAR
- Provides a foundation for institutional trust

### Data Models Catalogue
- Standardised formats for representing educational credentials
- Enables consistent credential representation across all implementation approaches
- Supports cross-border interpretation of qualifications
- Facilitates automated processing of educational information

### Trusted Schemes
- Templates ensuring consistent credential structure
- Supports automated processing across systems
- Defines standard formats for different credential types
- Enables semantic interoperability

## Verification Approaches by Pilot Implementation

### Classical PKI Pilot (Pilot 1) Verification

In Classical PKI implementations, verification follows traditional certificate-based trust models:

**Verification Process:**
- Relying party services verify the issuer's certificate against the Trusted Lists using **Certificate Revocation Lists (CRLs) and Online Certificate Status Protocol (OCSP)**
- The relying party may query the Authentic Source Data Store (for PID) or Database with Educational Records (for credentials) to confirm authenticity
- **X.509 certificate chain validation** ensures the issuer's certificate is not revoked
- Trust is established through traditional Public Key Infrastructure hierarchies

**Key Characteristics:**
- Relies on established PKI trust chains
- Uses X.509 certificates for issuer authentication
- Employs CRLs/OCSP for revocation checking
- Integrates with existing university PKI infrastructure

### Decentralised PKI (dPKI) Pilot (Pilot 2) Verification with Enhanced Privacy

In dPKI implementations, verification leverages decentralised trust mechanisms with enhanced privacy features:

**Verification Process:**
- **DID (Decentralised Identifier) resolution** to obtain cryptographic keys and service endpoints
- **EBSI Trusted Issuer Registry** validation to verify institutional authorisation
- **EBSI Schema Registry** checking for credential format compliance
- **Decentralised proxy StatusLists** for revocation checking to avoid "phone home" scenarios

**Enhanced Privacy Features:**
- **EBSI Proxy** serves as a decentralised proxy gateway
- **Decentralised StatusLists** enable privacy-preserving status checking for both revocation and suspension
- **No direct communication** between verifier and issuer during verification
- **Proxy-based status verification** prevents tracking of verification activities

**Key Characteristics:**
- Uses W3C Verifiable Credentials with DID-based trust
- Employs blockchain-anchored trust registries (EBSI)
- Implements privacy-preserving verification mechanisms
- **Supports both revocation and suspension status checking** through decentralised proxy StatusLists
- Addresses Member State requirements for granular credential status management

### Hybrid Mode (Pilot 3) Verification

Hybrid implementations combine both Classical PKI and dPKI approaches for maximum interoperability:

**Dual-Path Verification Process:**
- **Certificate-DID binding validation** ensures consistency between PKI and dPKI components
- **Path 1: Traditional PKI verification** including certificate chain validation and revocation checking
- **Path 2: dPKI verification** through DID resolution and EBSI registry validation
- **Binding verification** confirms the X.509 certificate is properly bound to the DID

**Performance Considerations:**
- Verification time approximately 161% longer than pure dPKI due to dual validation paths
- Requires additional network requests for both PKI and dPKI validation
- Enhanced security through dual trust anchors

**Key Characteristics:**
- Supports legacy PKI systems whilst enabling modern dPKI features
- Provides fallback capability if one verification path fails
- Ensures maximum trust through dual validation
- Maintains interoperability with existing institutional infrastructure

## Implementation Considerations

When implementing trusted lists across different verification approaches:

### Governance Processes
- **Classical PKI**: Traditional certificate authority governance structures
- **dPKI**: Decentralised governance through EBSI registries and community consensus
- **Hybrid**: Coordinated governance across both traditional and decentralised systems

### Update Mechanisms
- **Classical PKI**: Certificate lifecycle management and CRL/OCSP updates
- **dPKI**: Blockchain-based registry updates and decentralised status management
- **Hybrid**: Synchronised updates across both PKI and dPKI components

### List Verification Efficiency
- **Classical PKI**: Optimised for traditional certificate validation workflows
- **dPKI**: Enhanced privacy through proxy-based verification without direct issuer contact
- **Hybrid**: Balanced approach with intelligent fallback mechanisms

### Privacy Considerations
- **Classical PKI**: Standard PKI privacy limitations with potential "phone home" scenarios
- **dPKI**: **Enhanced privacy through decentralised proxy StatusLists** preventing tracking
- **Hybrid**: Privacy benefits of dPKI whilst maintaining PKI compatibility

## Cross-Border Scenarios

For cross-border educational mobility, trusted lists provide recognition mechanisms that vary by implementation:

### Classical PKI Cross-Border Recognition
- Traditional certificate trust chains across Member States
- Mutual recognition of certification authorities
- Standard PKI-based qualification verification

### dPKI Cross-Border Recognition
- **EBSI-based European trust infrastructure** enables seamless cross-border verification
- **Decentralised registries** eliminate need for bilateral trust agreements
- **Privacy-preserving verification** maintains confidentiality across borders

### Hybrid Cross-Border Recognition
- **Maximum interoperability** across different national implementations
- **Fallback mechanisms** ensure verification even if one system is unavailable
- **Gradual migration path** for institutions transitioning between approaches

## Integration with European Frameworks

Trusted lists integrate with European frameworks differently across implementations:

### European Quality Assurance Register (EQAR)
- **Classical PKI**: Traditional API-based integration
- **dPKI**: Blockchain-anchored quality assurance records
- **Hybrid**: Dual integration supporting both approaches

### National Qualification Frameworks
- **Classical PKI**: Standard PKI-based qualification mapping
- **dPKI**: Verifiable credential-based framework integration
- **Hybrid**: Comprehensive mapping across both systems

### European Qualification Framework (EQF)
- **Classical PKI**: Traditional qualification level verification
- **dPKI**: Decentralised qualification framework integration through EBSI
- **Hybrid**: Enhanced qualification verification through multiple trust paths

## Business Requirements for Credential Status Management

### Revocation vs Suspension - A Critical Distinction

From a business perspective, educational credentials may require different status management approaches across Member States:

**Revocation (Permanent Invalidation):**
- Credential is permanently invalid and cannot be restored
- Typically used for cases of fraud, misrepresentation, or fundamental errors
- Requires complete removal from trusted status

**Suspension (Temporary Invalidation):**
- Credential is temporarily invalid but may be restored
- Used for administrative holds, pending investigations, or temporary restrictions
- Allows for reinstatement once conditions are resolved

**Member State Variations:**
- Some Member States require **both revocation and suspension** capabilities
- Business processes may mandate different handling for temporary vs permanent invalidation
- Legal frameworks may distinguish between suspended and revoked credentials

### Implementation Across Verification Approaches

**Classical PKI Limitations:**
- Traditional CRL/OCSP primarily designed for revocation scenarios
- **Limited granular support** for suspension vs revocation distinction
- May require custom extensions or additional infrastructure

**dPKI Advantages:**
- **Native support for both revocation and suspension** through StatusList2021
- **Granular status management** with multiple status purposes
- **Privacy-preserving status checking** for both revocation and suspension
- **Flexible business rule implementation** to meet diverse Member State requirements

**Hybrid Approach:**
- Combines PKI revocation checking with dPKI suspension capabilities
- Provides **comprehensive status management** across both systems
- Ensures compliance with varying Member State business requirements

The dPKI implementation provides significant privacy improvements over traditional approaches:

### Decentralised Proxy StatusLists
- **Prevents "phone home" scenarios** where verification activities are tracked
- **Proxy-based revocation checking** maintains privacy whilst ensuring security
- **Decentralised status management** eliminates single points of privacy failure

### Enhanced Verification Privacy
- **No direct issuer contact** during verification process
- **EBSI proxy services** shield verification activities from monitoring
- **Distributed verification** prevents centralised tracking of credential usage

This privacy-preserving approach represents a significant advancement over traditional PKI verification methods, whilst maintaining the security and trust requirements of the European educational ecosystem.