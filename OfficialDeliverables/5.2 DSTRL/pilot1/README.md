# DSTRL Pilot1 - Classical PKI with SD-JWT

**Deployment and Testing Scenarios Results Library - Classical PKI Implementation**

Welcome to Pilot1 of the DC4EU Deployment and Testing Scenarios Results Library  (DSTRL) project. This pilot demonstrates the implementation of digital educational credentials using traditional Public Key Infrastructure (PKI) with Selective Disclosure JSON Web Tokens (SD-JWT) for credential format.

## Overview

Pilot1 represents a pragmatic approach to digital credential implementation that leverages existing PKI infrastructure whilst introducing modern selective disclosure capabilities. This pilot provides educational institutions with a pathway to digital credentials that builds upon familiar certificate-based trust models whilst ensuring compliance with European digital identity standards.

## Current Implementation Status

For the latest implementation progress across all participating institutions, including DNS endpoint availability, certificate deployment status, and cross-border verification capabilities, please refer to the [**DC4EU Piloting Status Tracker**](../procedures/piloting/piloting-status-tracker.md).

**Quick Status Overview:**
- **Participating Countries**: Denmark, Finland, Netherlands, Norway, Sweden
- **Total Institutions**: 5 organisations
- **DNS Endpoint Status**: Limited (SaaS managed instances)
- **X.509v3 Certificate Status**: Mixed implementation progress
- **Scenarios Template Compliance**: 100% across all participants

## Technical Architecture

### Trust Model
**Classical PKI (Public Key Infrastructure)**
- Hierarchical trust chains using established Certificate Authorities
- X.509v3 PKI certificates for issuer authentication
- X.509v3 PMI certificates for relying party verification
- Traditional certificate validation and revocation mechanisms

### Credential Format
**SD-JWT (Selective Disclosure JSON Web Token)**
- JSON Web Token structure with selective disclosure capabilities
- Privacy-preserving credential presentation
- Compatibility with existing JWT infrastructure
- Support for credential minimisation and data protection

### Core Components
- **Issuer Infrastructure**: PKI-based credential issuance systems
- **Wallet Technology**: wwWallet for credential storage and management
- **Verification Services**: Certificate-based trust chain validation
- **SaaS Platform**: SUNET/SURF test environment for streamlined deployment

## Implementation Approach

### SaaS-First Strategy
Pilot1 prioritises accessible implementation through Software-as-a-Service delivery:

**SUNET/SURF SaaS Environment**
- Pre-configured PKI infrastructure
- Standardised issuer public keys for cross-institutional compatibility
- Managed certificate authorities and trust chain validation
- Simplified deployment for educational institutions

**Institutional Benefits**
- Reduced technical overhead for participating institutions
- Standardised implementation approach across Nordic region
- Collaborative infrastructure sharing among NRENs
- Focused institutional effort on user experience and integration

### Trust Chain Management
**Certificate Hierarchy**
1. **Root Certificate Authority**: SUNET/SURF managed CA
2. **Intermediate CAs**: Regional or national certificate authorities
3. **Entity Certificates**: Institutional issuer and relying party certificates
4. **End-User Authentication**: Traditional PKI credential validation

## User Journey Documentation

### Credential Issuance Journey
1. **User Authentication**: PKI certificate-based institutional login
2. **Credential Request**: Student or staff initiates credential request
3. **Identity Verification**: Institution validates user identity and entitlements
4. **Credential Generation**: SD-JWT format credential creation
5. **Wallet Delivery**: Secure transfer to wwWallet application
6. **Storage Confirmation**: Verification of successful credential storage

### Credential Verification Journey
1. **Presentation Request**: Verifier initiates credential request
2. **Selective Disclosure**: User selects information to share
3. **Credential Presentation**: SD-JWT credential transmitted
4. **Signature Verification**: PKI-based authenticity validation
5. **Trust Chain Validation**: Certificate authority verification
6. **Decision Response**: Accept/reject determination

## Strengths and Capabilities

### Established Infrastructure Leverage
- **Familiar Technology**: Builds on well-understood PKI principles
- **Existing Investments**: Utilises current certificate infrastructure
- **Proven Security**: Time-tested cryptographic mechanisms
- **Regulatory Compliance**: Alignment with eIDAS 1.0 frameworks

### Selective Disclosure Benefits
- **Privacy Protection**: Minimal data sharing capabilities
- **GDPR Compliance**: Data minimisation and consent mechanisms
- **Flexible Presentation**: Context-appropriate information sharing
- **User Control**: Individual control over personal data disclosure

## Current Limitations and Considerations

### Verification Constraints
Current implementation faces specific technical limitations:

**Relying Party Certificate Availability**
- Limited RP certificate provisioning in pilot environment
- Prevents full cross-border verification testing
- Restricts demonstration of complete trust chain validation

**Cross-Border Interoperability**
- Verification limited to integrity checks in current deployment
- Full trust chain validation requires additional infrastructure
- International recognition depends on bilateral trust agreements

### Lifecycle Management
**Limited Credential Lifecycle Features**
- Revocation mechanisms not fully implemented in pilot
- Suspension capabilities require additional PKI infrastructure
- Real-time status checking depends on CRL/OCSP availability

## Directory Structure

### Infrastructure Documentation (`/infrastructure`)
- PKI implementation guidelines and requirements
- Certificate management procedures and best practices
- Integration specifications for institutional systems
- Security configuration and operational guidance

### Piloting Agent Scenarios (`/PAs`)
- Detailed implementation reports from participating institutions
- User journey documentation and testing results
- Lessons learned and implementation insights
- Technical configuration examples and templates

### User Journey Documentation (`/userjourneys`)
- Step-by-step credential issuance processes
- Verification workflow specifications
- User experience guidance and recommendations
- Error handling and troubleshooting procedures

## Getting Started with Pilot1

### For Educational Institutions

#### Assessment and Planning
1. **Infrastructure Assessment**: Review existing PKI infrastructure and integration capabilities
2. **Stakeholder Engagement**: Identify key participants and user groups
3. **Use Case Definition**: Define specific credential types and verification scenarios
4. **Resource Planning**: Allocate technical and administrative resources

#### Technical Implementation
1. **SaaS Onboarding**: Register with SUNET/SURF test environment
2. **Integration Development**: Implement institutional system integration
3. **Certificate Configuration**: Configure PKI certificates and trust relationships
4. **Testing and Validation**: Conduct comprehensive functionality testing

#### Operational Deployment
1. **User Onboarding**: Deploy user registration and wallet setup processes
2. **Credential Issuance**: Begin controlled credential issuance to pilot users
3. **Verification Testing**: Test verification workflows with partner institutions
4. **Monitoring and Support**: Implement operational monitoring and user support

### For Technology Partners

#### Integration Requirements
- SD-JWT processing capabilities
- PKI certificate management systems
- wwWallet compatibility and support
- Classical PKI infrastructure maintenance

## Related Documentation

### Cross-Reference Links
- [**Piloting Status Tracker**](../procedures/piloting/piloting-status-tracker.md) - Current implementation status across all pilots
- [**Deployment Methodology**](../procedures/Deployment_methodology.md) - Standardised implementation approach
- [**Compliance Tracking**](../procedures/entities/compliance.md) - Regulatory compliance monitoring
- [**Pilot2 Implementation**](../pilot2/README.md) - Decentralised PKI approach
- [**Pilot3 Combined Approach**](../pilot3/README.md) - Dual trust model implementation

### Technical Documentation
- [Infrastructure Setup Guide](./infrastructure/README.md)
- [PKI Certificate Management](./infrastructure/certificate-management.md)
- [SD-JWT Implementation Specifications](./infrastructure/sd-jwt-processing.md)
- [User Journey Templates](./userjourneys/README.md)

## Support and Resources

### Technical Support
- **SUNET/SURF Technical Team**: SaaS environment support and maintenance
- **DC4EU Project Office**: Project coordination and guidance
- **Community Forums**: Peer support and knowledge sharing
- **Documentation Portal**: Comprehensive technical documentation

### Training and Capacity Building
- **Implementation Workshops**: Regular training sessions for technical teams
- **Best Practices Sharing**: Community-driven knowledge exchange
- **User Experience Guidelines**: Support for institutional deployment teams
- **Troubleshooting Resources**: Common issues and resolution procedures

---

*For current implementation status and progress tracking across all DC4EU pilots, please refer to the [Piloting Status Tracker](../procedures/piloting/piloting-status-tracker.md).*