# DSTRL Pilot3 - Combined Implementation (Pilot1 + Pilot2)

**DDeployment and Testing Scenarios Results Library - Dual Trust Model Implementation**

Welcome to Pilot3 of the DC4EU  Deployment and Testing Scenarios Results Library (DSTRL) project. This pilot demonstrates the simultaneous implementation of both Classical PKI (Pilot1) and Hybrid Trust (Pilot2) approaches, providing educational institutions with comprehensive dual trust model capabilities and maximum flexibility for credential issuance and verification.

## Overview

Pilot3 represents the most comprehensive approach within the DC4EU piloting framework, enabling institutions to operate both classical PKI-based and decentralised PKI-based credential systems simultaneously. This approach provides maximum flexibility for institutional stakeholders whilst ensuring compatibility with diverse verification requirements and regulatory frameworks across different contexts and jurisdictions.

## Current Implementation Status

For comprehensive tracking of Pilot3 dual implementation progress, including both Classical PKI and Decentralised PKI component status, please refer to the [**DC4EU Piloting Status Tracker**](../procedures/piloting/piloting-status-tracker.md).

**Quick Status Overview:**
- **Participating Countries**: Netherlands, Portugal
- **Total Institutions**: 3 organisations (6 implementations - 3 PKI + 3 dPKI)
- **Classical PKI Component**: SaaS instances by SUNET/SURF
- **Decentralised PKI Component**: 100% DNS availability and DID deployment
- **Dual Trust Model Status**: Complete dual implementation across all participants

## Fundamental Architecture

### Combined Trust Model Definition

```
Pilot3 = Pilot1 + Pilot2
```

**Dual Infrastructure Requirement**
- **Classical PKI Component**: Traditional certificate-based trust chains (Pilot1)
- **Decentralised PKI Component**: DID-based blockchain-anchored trust (Pilot2)
- **Dual Endpoint Architecture**: Separate public endpoints for each trust model
- **Unified User Experience**: Seamless integration across both systems

### Trust Model Flexibility
**User Choice and Adaptability**
- **Context-Appropriate Selection**: Users choose optimal trust model per interaction
- **Verifier Compatibility**: Support for diverse verification system requirements
- **Regulatory Compliance**: Alignment with varying national and international requirements
- **Future-Proof Strategy**: Smooth transition pathway between trust models

## Technical Architecture

### Dual Infrastructure Components

#### Classical PKI Infrastructure (Pilot1 Component)
- **Trust Model**: Classical PKI with hierarchical certificate authorities
- **Credential Format**: SD-JWT (Selective Disclosure JSON Web Token)
- **Platform**: SUNET/SURF SaaS environment
- **Wallet Technology**: wwWallet for credential storage and management
- **Endpoint**: PKI-based public endpoint for classical verification

#### Decentralised PKI Infrastructure (Pilot2 Component)
- **Trust Model**: Hybrid Classical PKI + Decentralised PKI
- **Credential Format**: W3C Verifiable Credentials
- **Platform**: ATOS/IZERTIS Dockerised solution
- **Wallet Technology**: EUDI Wallet (EUDIW by IZERTIS)
- **Endpoint**: dPKI-based public endpoint for decentralised verification

### Implementation Requirements

#### Complete Dual Implementation
**Infrastructure Obligations**
- **Parallel Deployment**: Both Pilot1 and Pilot2 infrastructure fully operational
- **Dual Evidence Provision**: All onboarding requirements for both pilot types
- **Cross-System Compatibility**: Unified user management across both trust models
- **Operational Coordination**: Simultaneous maintenance and support for both systems

## Current Pilot3 Participating Institutions

### Netherlands Implementation

#### University of Twente (UTWENTE)
- **Classical PKI Endpoint**: SUNET/SURF SaaS instance
- **Decentralised PKI Endpoint**: `lsput.utwente.nl`
- **DID Implementation**: `did:ebsi:zT8nF3mYx2tKp7qZ4Rh5GsV`
- **Dual Trust Status**: Complete implementation

#### Saxion University of Applied Sciences (SAXION)
- **Classical PKI Endpoint**: SUNET/SURF SaaS instance
- **Decentralised PKI Endpoint**: `lspsaxion.saxion.nl`
- **DID Implementation**: `did:ebsi:zZ97WmbVmSr6UpU5jb5X8HK`
- **Dual Trust Status**: Full operational deployment

### Portugal Implementation

#### COFAC - Lusófona University (ULUSOFONA)
- **Classical PKI Endpoint**: SUNET/SURF SaaS instance
- **Decentralised PKI Endpoint**: `lspulusofona.ulusofona.pt`
- **DID Implementation**: `did:ebsi:zrmS9sGhR5J6vHu2gzMkN8t`
- **Dual Trust Status**: Complete dual infrastructure

## Implementation Benefits and Capabilities

### Maximum Flexibility
**Multi-Modal Credential Support**
- **SD-JWT Credentials**: Classical PKI-based selective disclosure tokens
- **W3C Verifiable Credentials**: Standards-compliant verifiable credentials
- **Dual Wallet Support**: Both wwWallet and EUDI Wallet compatibility
- **Cross-Format Verification**: Support for diverse verifier requirements

### Comprehensive Trust Coverage
**Universal Verification Compatibility**
- **Traditional Systems**: Legacy PKI-based verification support
- **Modern Systems**: Decentralised identity verification capabilities
- **Hybrid Environments**: Mixed trust model support
- **Future Systems**: Preparation for emerging standards and technologies

### Risk Mitigation
**Operational Resilience**
- **Trust Model Redundancy**: Alternative trust pathways if one system fails
- **Verification Fallback**: Multiple verification mechanisms available
- **Technology Evolution**: Smooth transition as standards evolve
- **Regulatory Flexibility**: Compliance with diverse regulatory requirements

## Institutional Implementation Strategies

### For Educational Institutions

#### Dual Assessment and Planning
1. **Dual Infrastructure Assessment**: Evaluate capacity for managing both trust models
2. **Use Case Analysis**: Determine optimal trust model for different institutional scenarios
3. **Resource Allocation**: Plan technical and human resources for dual implementation
4. **Phased Deployment**: Develop timeline for sequential or parallel implementation

#### Implementation Pathway
**Phase 1: Infrastructure Preparation**
- Establish both Classical PKI and dPKI infrastructure capabilities
- Configure dual endpoints and management interfaces
- Integrate with institutional identity and academic record systems

**Phase 2: Pilot Testing**
- Deploy limited-scope testing with select user groups
- Validate both trust model implementations
- Test user journey flows across both systems

**Phase 3: Production Deployment**
- Scale to full institutional implementation
- Provide comprehensive user training for both systems
- Establish operational procedures for dual trust model management

### For Technology Partners

#### Technical Integration Requirements
**Classical PKI Component (Pilot1)**
- X.509v3 PKI certificate management
- SD-JWT credential processing capabilities
- wwWallet integration and support
- Traditional PKI infrastructure maintenance

**Decentralised PKI Component (Pilot2)**
- DID registration and management capabilities
- W3C VC standards implementation
- EBSI blockchain integration
- EUDI wallet compatibility and support

#### Unified System Management
- **Cross-System User Management**: Unified identity across both trust models
- **Credential Mapping**: Correlation between SD-JWT and W3C VC formats
- **Operational Monitoring**: Comprehensive oversight of dual infrastructure
- **Support Coordination**: Integrated technical support across both platforms

## Directory Structure

### Infrastructure Documentation (`/infrastructure`)
- **Dual Trust Model Architecture**: Combined implementation specifications
- **Classical PKI Setup**: Traditional certificate-based infrastructure requirements
- **Decentralised PKI Setup**: DID and blockchain integration procedures
- **Cross-System Integration**: Unified management and operational procedures

### Piloting Agent Scenarios (`/PAs`)
- **Netherlands Implementation Reports**: UTWENTE and SAXION deployment documentation
- **Portugal Implementation Reports**: ULUSOFONA comprehensive implementation analysis
- **Dual Trust Model Analysis**: Comparative assessment of both trust approaches
- **Lessons Learned Documentation**: Best practices and implementation insights

### User Journey Documentation (`/userjourneys`)
- **Dual System User Flows**: Combined classical and decentralised user journeys
- **Trust Model Selection Guidance**: User decision-making support
- **Cross-System Credential Management**: Unified credential lifecycle procedures
- **Verification Workflow Options**: Multiple verification pathway documentation

## Related Documentation

### Cross-Reference Links
- [**Piloting Status Tracker**](../procedures/piloting/piloting-status-tracker.md) - Comprehensive dual implementation status monitoring
- [**Deployment Methodology**](../procedures/Deployment_methodology.md) - Combined implementation framework
- [**Compliance Tracking**](../procedures/entities/compliance.md) - Dual compliance monitoring
- [**Pilot1 Classical PKI**](../pilot1/README.md) - Classical PKI component specifications
- [**Pilot2 Decentralised PKI**](../pilot2/README.md) - Decentralised PKI component specifications

### Technical Implementation Guides
- [Infrastructure Architecture Overview](./infrastructure/README.md)
- [Dual Trust Model Implementation](./infrastructure/dual-trust-implementation.md)
- [Cross-System Integration Procedures](./infrastructure/cross-system-integration.md)
- [Unified User Journey Templates](./userjourneys/README.md)

## Operational Considerations

### Resource Requirements
**Enhanced Technical Capability**
- **Dual Infrastructure Maintenance**: Both PKI and dPKI system management
- **Cross-System Expertise**: Technical knowledge of both trust models
- **Operational Complexity**: Increased monitoring and support requirements
- **Training Investment**: Comprehensive staff education across both systems

### Strategic Benefits
**Future-Proof Implementation**
- **Technology Evolution Preparedness**: Ready for standards development
- **Regulatory Flexibility**: Compliance with diverse requirements
- **Stakeholder Accommodation**: Support for varied verification preferences
- **Innovation Leadership**: Advanced implementation showcasing best practices

## Support and Resources

### Technical Support Network
- **SUNET/SURF Classical PKI Support**: Traditional PKI infrastructure assistance
- **ATOS/IZERTIS Decentralised PKI Support**: Modern dPKI implementation guidance
- **DC4EU Project Office**: Overall coordination and strategic guidance
- **Peer Institution Network**: Knowledge sharing among Pilot3 implementers

### Best Practices and Knowledge Sharing
- **Dual Implementation Documentation**: Comprehensive technical guides
- **Cross-System Integration Examples**: Practical implementation patterns
- **Operational Procedures**: Day-to-day management and maintenance guidance
- **User Experience Optimisation**: Combined system usability enhancement

### Innovation and Development
- **Standards Evolution Participation**: Active contribution to emerging standards
- **Trust Model Research**: Advanced research into hybrid trust architectures
- **Interoperability Enhancement**: Continuous improvement of cross-system compatibility
- **European Digital Identity Leadership**: Contributing to EUDI ecosystem development

---

*For detailed implementation progress tracking and current status of both Classical PKI and Decentralised PKI components, please refer to the [Piloting Status Tracker](../procedures/piloting/piloting-status-tracker.md).*