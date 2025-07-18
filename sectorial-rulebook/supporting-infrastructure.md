# Supporting Infrastructure

## Overview

This infrastructure supports the entire credential ecosystem whilst maintaining security, privacy, and usability across European educational systems. The underlying system creates a foundation that enables all other components to function effectively through a hybrid trust model that combines traditional PKI with decentralised PKI (dPKI) and verifiable data registers.

## Key Requirements

### Multi-domain and Sector Support
- Works across educational domains
- Supports varied credential types
- Accommodates different institutional needs
- Enables cross-sector recognition

### Distributed Architecture
- Avoids centralised points of failure
- Distributes trust and responsibility
- Supports system resilience
- Maintains institutional autonomy

### Pan-European Coverage
- Functions across all member states
- Supports cross-border operations
- Enables European-wide recognition
- Maintains consistency across regions

### Privacy-enhanced Verification
- Protects user privacy during verification
- Prevents unnecessary tracking
- Implements data minimisation
- Supports selective disclosure

### Data Protection Compliance
- Aligns with GDPR requirements
- Implements privacy by design
- Supports data subject rights
- Enables appropriate governance

### Security Audit Mechanisms
- Provides transparency on system operation
- Enables security verification
- Supports compliance checking
- Maintains system integrity

### Verification Record Keeping
- Maintains appropriate audit trails
- Supports future verification needs
- Enables dispute resolution
- Provides operational evidence

### Service Discovery Tools
- Helps locate verification services
- Supports issuer discovery
- Enables wallet-service connections
- Facilitates ecosystem navigation

### Cross-country Legal Entity Recognition
- Supports recognition of institutions across borders
- Enables trust in foreign entities
- Maintains consistent verification
- Supports institutional mobility

## Trust Infrastructure Models

### Classical PKI Infrastructure

The classical PKI provides the foundational trust anchor for the educational ecosystem:

**Trust Hierarchy**:
- National Certificate Authorities (CAs)
- Educational PKI hierarchies
- Institutional certificate chains
- Cross-border trust lists

**Key Components**:
- Certificate Authority (CA) trust stores
- Certificate Revocation Lists (CRLs)
- Online Certificate Status Protocol (OCSP) services
- Certificate validation services
- Cross-certification mechanisms

**Characteristics**:
- Established regulatory compliance
- Mature tooling and infrastructure
- Predictable verification times (~200ms)
- Well-understood security models

### Decentralised PKI with Verifiable Data Registers

The dPKI infrastructure leverages EBSI and verifiable data registers to enable granular governance:

**Trust Components**:
- EBSI Trust Registry
- Trusted Issuer Registry
- Trusted Schema Registry
- Accreditation Registry
- Revocation Registry

**Key Features**:
- Decentralised identifier (DID) resolution
- Verifiable credential schemas
- Distributed trust anchors
- Granular authorisation verification
- Self-sovereign identity support

**Characteristics**:
- Enhanced privacy through selective disclosure
- Granular governance capabilities
- Reduced verification times (~150ms)
- Regulatory alignment with eIDAS 2.0

### Hybrid Trust Model

The hybrid approach combines both classical PKI and dPKI to provide enhanced trust assurance:

**Architecture**:
- Dual trust path validation
- X.509-DID binding mechanisms
- Fallback capabilities
- Cross-validation protocols

**Trust Enhancement**:
- Both PKI and dPKI paths must validate successfully
- Certificate-DID binding verification
- Enhanced interoperability with legacy systems
- Resilient operation during infrastructure unavailability

**Performance Considerations**:
- Increased verification time (~407ms total)
- Additional network requests required
- Enhanced trust assurance through dual validation
- Improved system resilience

## Implementation Considerations

### Trust Model Selection

**Pure dPKI - Recommended When**:
- Digital-native organisation with no legacy PKI infrastructure
- Performance is critical (≈150ms verification time)
- Simplified maintenance is preferred
- EBSI infrastructure is highly reliable in deployment context

**Hybrid Model - Recommended When**:
- Legacy PKI integration is required
- Maximum interoperability with existing systems is needed
- Enhanced trust assurance through dual validation is valued
- Regulatory compliance requires traditional PKI elements
- Fallback capability during EBSI unavailability is important

**Classical PKI - Recommended When**:
- Existing PKI infrastructure is mature and well-established
- Regulatory requirements mandate traditional PKI approaches
- Decentralised infrastructure is not yet available
- Conservative trust model is preferred

### Technical Implementation

**Infrastructure Requirements**:
- Scalability to accommodate growing ecosystem needs
- Security maintained through regular updates
- Performance optimised for efficient operations
- Interoperability enabling system connections
- Governance frameworks clearly defined

**Hybrid Model Dependencies**:
```
Classical PKI Components:
- Certificate Authority trust stores
- OCSP responder services
- CRL distribution points
- Certificate validation libraries

dPKI Components:
- EBSI registry access
- DID resolution services
- Verifiable credential validators
- Trust registry interfaces

Hybrid-Specific Components:
- X.509-DID binding validators
- Dual-path verification engines
- Fallback orchestration services
- Cross-validation protocols
```

### Security Considerations

**Enhanced Security Benefits**:
- Dual trust anchors requiring compromise of both PKI and dPKI
- Binding integrity preventing certificate/DID substitution attacks
- Comprehensive audit trails across both trust models
- Resilient operation during partial infrastructure failures

**Risk Management**:
- Binding verification failures invalidate entire credential
- Coordination required between PKI and dPKI lifecycle management
- Increased complexity in error handling and monitoring
- Performance impact requiring careful system design

## Cross-Border Scenarios

For cross-border educational mobility, supporting infrastructure provides:

**Trust Interoperability**:
- Consistent operation across member states
- Recognition of diverse national PKI infrastructures
- EBSI-mediated trust for dPKI credentials
- Hybrid validation supporting both trust models

**Service Integration**:
- Technical support for credential recognition
- Reliable verification services across borders
- Integration with diverse educational systems
- Harmonised privacy and disclosure policies

## Technical Components

The supporting infrastructure includes:

**Trust Infrastructure**:
- Trust registries (EBSI and national)
- Verification services (PKI and dPKI)
- Certificate authorities and trust anchors
- Binding validation services

**Service Discovery**:
- Service directories
- Issuer discovery mechanisms
- Wallet-service connection protocols
- Cross-border service location

**Governance Framework**:
- Authorisation verification systems
- Compliance monitoring tools
- Audit trail mechanisms
- Dispute resolution processes

**Integration Interfaces**:
- Legacy system bridges
- API gateways
- Protocol translation services
- Progressive enhancement capabilities

**Supporting Documentation**:
- Technical specifications
- Integration guides
- Compliance frameworks
- Operational procedures

## Conclusion

The supporting infrastructure provides a robust foundation for European educational credential systems through flexible trust models that can accommodate diverse institutional needs, regulatory requirements, and technical capabilities. The hybrid approach offers enhanced resilience and interoperability whilst maintaining the security and privacy standards required for educational credential management across Europe.