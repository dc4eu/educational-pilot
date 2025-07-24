# DSTRL Pilot2 - Hybrid Trust with W3C Verifiable Credentials

**Digital Student Records and Transcript Ledger - Decentralised PKI Implementation**

Welcome to Pilot2 of the DC4EU Digital Student Records and Transcript Ledger (DSTRL) project. This pilot demonstrates the implementation of digital educational credentials using a hybrid trust model that combines Classical PKI with Decentralised PKI, utilising W3C Verifiable Credentials and European Blockchain Services Infrastructure (EBSI) integration.

## Overview

Pilot2 represents the next generation of digital credential infrastructure, designed to align with eIDAS 2.0 regulation and the European Union Digital Identity (EUDI) Wallet ecosystem. This pilot provides educational institutions with a forward-looking approach that combines the reliability of traditional PKI with the flexibility and interoperability of decentralised identity technologies.

## Current Implementation Status

For comprehensive implementation progress tracking across all participating institutions, including DNS endpoint deployment, DID implementation status, and cross-border verification capabilities, please refer to the [**DC4EU Piloting Status Tracker**](../procedures/piloting/piloting-status-tracker.md).

**Quick Status Overview:**
- **Participating Countries**: Belgium, Germany, Hungary, Italy, Lithuania, Poland, Portugal, Romania, Spain, Sweden
- **Total Institutions**: 28 organisations
- **DNS Endpoint Status**: 100% availability for cross-border verification
- **DID Implementation Status**: Fully deployed across all participants
- **Scenarios Template Compliance**: Universal provision

## Technical Architecture

### Trust Model
**Hybrid Trust: Classical PKI + Decentralised PKI**
- **Classical PKI Component**: Traditional certificate authorities and trust chains
- **Decentralised PKI Component**: Distributed Identifiers (DIDs) and blockchain anchoring
- **EBSI Integration**: European Blockchain Services Infrastructure trust registries
- **Dynamic Trust Discovery**: Real-time trust validation across multiple trust anchors

### Credential Format
**W3C Verifiable Credentials (VC)**
- **W3C-VCDM 1.1 & 2.0**: Standards-compliant credential structure
- **JSON-LD Format**: Semantic interoperability and linked data principles
- **Digital Signatures**: Multiple signature mechanisms (JWS, jAdES)
- **Selective Disclosure**: Privacy-preserving information sharing capabilities

### Core Infrastructure Components
- **DID Management**: Decentralised identifier creation and resolution
- **EBSI Trust Registries**: European blockchain-based trust infrastructure
- **EUDI Wallet**: European digital wallet for credential storage
- **uSelf Platform**: ATOS/IZERTIS implementation for credential operations

## Implementation Approach

### EBSI-Anchored Trust Framework
Pilot2 leverages the European Blockchain Services Infrastructure for trust establishment:

**Trust Registry Integration**
- **Issuer Registration**: DID-based issuer identity anchoring
- **Schema Registration**: Credential type and structure validation
- **Revocation Registry**: Real-time credential status monitoring
- **Cross-Border Recognition**: Automatic trust establishment across member states

**Decentralised Governance**
- **Distributed Trust**: No single point of failure or control
- **Consensus Mechanisms**: Blockchain-based agreement protocols
- **Transparency**: Public verification of trust relationships
- **Interoperability**: Standards-based cross-system compatibility

### Flexible Deployment Options
Pilot2 supports multiple deployment approaches to accommodate diverse institutional requirements:

**ATOS/IZERTIS Dockerised Solution**
- Self-hosted institutional deployment
- Full control over infrastructure and data
- Customisable integration with existing systems
- Institutional sovereignty over credential issuance

**Govpart SaaS Instance**
- Managed service deployment option
- Reduced technical overhead for institutions
- Standardised implementation with customisation options
- Professional support and maintenance services

**National SaaS Implementations**
- Country-specific managed services (e.g., OPI/NASK in Poland)
- National regulatory compliance and coordination
- Shared infrastructure among national institutions
- Coordinated cross-border verification capabilities

## Implementation Variations by Region

### Dockerised Deployment Countries
**Belgium, Hungary, Italy, Lithuania, Portugal, Romania, Spain**
- **Technical Approach**: ATOS/IZERTIS Dockerised solution
- **Institutional Control**: High autonomy over infrastructure
- **Customisation Level**: Extensive institutional customisation capabilities
- **Maintenance Model**: Institutional or contracted technical support

### SaaS Deployment Countries
**Germany**
- **Technical Approach**: Govpart SaaS instance
- **Institutional Control**: Managed service with institutional configuration
- **Customisation Level**: Service-level customisation options
- **Maintenance Model**: Professional managed service support

### National SaaS Implementation
**Poland**
- **Technical Approach**: OPI/NASK national SaaS instance
- **Institutional Control**: National coordination with institutional participation
- **Customisation Level**: National standards with institutional variation
- **Maintenance Model**: National infrastructure management

### Unique Implementation Approaches
**Spain - Medical Professional Integration**
- **CGCOM**: Medical professional credential integration
- **UNED**: Distance education specialisation
- **Multiple Universities**: Coordinated regional implementation

## User Journey Categories

### Core Educational Credential Journeys
1. **Personal Identity Document (PID) Integration**
2. **Educational ID Issuance and Management**
3. **Academic Achievement Credential Issuance**
4. **Professional Qualification Attestation**
5. **Quality Assurance Agency Verification**
6. **Cross-Border Credential Recognition**
7. **Employer and Third-Party Verification**

### Advanced Credential Lifecycle Management
- **Credential Revocation and Suspension**
- **Credential Updates and Amendments**
- **Batch Credential Operations**
- **Audit Trail and Compliance Reporting**

## Strengths and Capabilities

### Future-Ready Architecture
- **eIDAS 2.0 Alignment**: Preparation for upcoming European regulation
- **EUDI Wallet Compatibility**: Integration with European digital identity ecosystem
- **Blockchain Integration**: Leveraging EBSI for trust establishment
- **Standards Compliance**: W3C and European standards adherence

### Enhanced Security and Privacy
- **Decentralised Trust**: Reduced single points of failure
- **Selective Disclosure**: Fine-grained privacy control
- **Cryptographic Integrity**: Advanced digital signature mechanisms
- **Blockchain Anchoring**: Immutable trust establishment

### Cross-Border Interoperability
- **Automatic Trust Discovery**: Dynamic trust relationship establishment
- **Standards-Based Verification**: W3C VC universal compatibility
- **EBSI Trust Registry**: European-wide trust infrastructure
- **Multi-Language Support**: International credential presentation

## Current Implementation Achievements

### Technical Infrastructure Success
- **100% DNS Endpoint Availability**: Complete cross-border verification infrastructure
- **Universal DID Deployment**: All institutions operating with decentralised identifiers
- **EBSI Integration**: Successful blockchain trust registry integration
- **W3C VC Compliance**: Standards-compliant credential issuance

### Operational Capabilities
- **Cross-Border Verification**: Active verification between multiple countries
- **Multiple Deployment Models**: Successful variety of institutional approaches
- **Professional Integration**: Medical and educational professional qualification support
- **Scalable Architecture**: Support for large-scale institutional deployment

## Directory Structure

### Infrastructure Documentation (`/infrastructure`)
- Hybrid trust model implementation specifications
- DID management and EBSI integration procedures
- W3C Verifiable Credentials processing guidelines
- Cross-border verification configuration

### Piloting Agent Scenarios (`/PAs`)
- Detailed institutional implementation reports by country
- Deployment model comparisons and analysis
- Lessons learned and best practices documentation
- Technical configuration examples and templates

### User Journey Documentation (`/userjourneys`)
- W3C VC credential issuance workflows
- Decentralised verification processes
- EUDI Wallet integration procedures
- Cross-border recognition scenarios

## Getting Started with Pilot2

### For Educational Institutions

#### Implementation Planning
1. **Infrastructure Assessment**: Evaluate capacity for hybrid trust model implementation
2. **Deployment Model Selection**: Choose between Dockerised, SaaS, or National approaches
3. **Integration Architecture**: Design connection with existing institutional systems
4. **Stakeholder Engagement**: Coordinate with technical, legal, and academic stakeholders

#### Technical Implementation
1. **DID Infrastructure Setup**: Establish decentralised identifier management
2. **EBSI Integration**: Configure European blockchain trust registry connections
3. **W3C VC Processing**: Implement verifiable credentials issuance and verification
4. **Cross-Border Testing**: Validate verification capabilities with international partners

#### Operational Deployment
1. **User Onboarding**: Deploy EUDI wallet setup and user registration
2. **Credential Workflows**: Implement institutional credential issuance processes
3. **Verification Services**: Enable third-party verification capabilities
4. **Monitoring and Analytics**: Establish operational oversight and performance tracking

### For Technology Partners

#### Technical Integration Requirements
- **DID Infrastructure**: Decentralised identifier creation and management systems
- **EBSI Connectivity**: European blockchain integration capabilities
- **W3C VC Processing**: Verifiable credentials standards implementation
- **EUDI Wallet Support**: European digital identity wallet compatibility

## Related Documentation

### Cross-Reference Links
- [**Piloting Status Tracker**](../procedures/piloting/piloting-status-tracker.md) - Real-time implementation status across all pilots
- [**Deployment Methodology**](../procedures/Deployment_methodology.md) - Standardised implementation framework
- [**Compliance Tracking**](../procedures/entities/compliance.md) - Regulatory compliance monitoring
- [**Pilot1 Classical PKI**](../pilot1/README.md) - Traditional PKI approach comparison
- [**Pilot3 Combined Implementation**](../pilot3/README.md) - Dual trust model deployment

### Technical Documentation
- [Infrastructure Architecture Guide](./infrastructure/README.md)
- [DID Implementation Specifications](./infrastructure/did-implementation.md)
- [EBSI Integration Procedures](./infrastructure/ebsi-integration.md)
- [W3C VC Processing Guidelines](./infrastructure/w3c-vc-processing.md)
- [User Journey Implementation Templates](./userjourneys/README.md)

## Support and Resources

### Technical Support Network
- **ATOS/IZERTIS Technical Team**: Dockerised solution support and development
- **Govpart Support Services**: SaaS instance management and customisation
- **National Support Teams**: Country-specific technical assistance (e.g., OPI/NASK)
- **DC4EU Project Office**: Overall project coordination and guidance

### Community and Knowledge Sharing
- **Implementation Community**: Active peer support network across 28 institutions
- **Best Practices Repository**: Shared knowledge base and documentation
- **Regular Coordination Meetings**: Ongoing collaboration and problem-solving sessions
- **Training and Capacity Building**: Continuous education and skill development programmes

### Innovation and Development
- **Standards Development Participation**: Active contribution to W3C and European standards
- **EBSI Integration Enhancement**: Ongoing blockchain infrastructure optimisation
- **EUDI Wallet Evolution**: Participation in European digital identity wallet development
- **Cross-Border Verification Advancement**: Continuous improvement of international recognition capabilities

---

*For detailed implementation progress and current status across all participating institutions, please refer to the [Piloting Status Tracker](../procedures/piloting/piloting-status-tracker.md).*