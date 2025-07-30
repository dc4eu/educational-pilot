# DSTRL Pilot3 - Combined Implementation (Pilot1 + Pilot2)

**Deployment and Testing Scenarios Results Library - Dual Implementation Approach**

Welcome to Pilot3 of the DC4EU Deployment and Testing Scenarios Results Library (DSTRL) project. This pilot demonstrates the simultaneous implementation of both Classical PKI (Pilot1) and Decentralised PKI (Pilot2) approaches as separate, parallel systems, providing educational institutions with comprehensive dual deployment capabilities and maximum flexibility for credential issuance and verification across different trust frameworks.

## Overview

Pilot3 represents the most comprehensive approach within the DC4EU piloting framework, enabling institutions to operate both classical PKI-based and decentralised PKI-based credential systems as independent, parallel implementations. This approach provides maximum flexibility for institutional stakeholders whilst ensuring compatibility with diverse verification requirements and regulatory frameworks across different contexts and jurisdictions.

**Important clarification**: Pilot3 does not implement a single hybrid system combining classical and decentralised PKI. Instead, it requires institutions to deploy both Pilot1 and Pilot2 solutions as separate, independent systems operating in parallel.

## Current Implementation Status

For comprehensive tracking of Pilot3 dual implementation progress, including both Classical PKI and Decentralised PKI component status, please refer to the [**DC4EU Piloting Status Tracker**](../procedures/piloting/piloting-status-tracker.md).

**Quick Status Overview:**
- **Participating Countries**: Netherlands, Portugal
- **Total Institutions**: 3 organisations (6 implementations - 3 Pilot1 + 3 Pilot2)
- **Classical PKI Component**: SaaS instances by SUNET/SURF
- **Decentralised PKI Component**: 100% DNS availability and DID deployment
- **Dual Implementation Status**: Complete parallel deployment across all participants

## Fundamental Architecture

### Combined Implementation Definition

```
Pilot3 = Pilot1 + Pilot2 (as separate parallel systems)
```

**Dual Infrastructure Requirement**
- **Classical PKI Component**: Complete Pilot1 implementation with traditional certificate-based trust chains
- **Decentralised PKI Component**: Complete Pilot2 implementation with DID-based blockchain-anchored trust
- **Separate System Architecture**: Independent endpoints and infrastructure for each pilot
- **Parallel User Experience**: Users can access both systems independently

### Implementation Flexibility
**Separate System Operation**
- **Independent Trust Models**: Each pilot operates with its own trust framework
- **Separate Verification Pathways**: Distinct verification systems for each approach
- **Technology Choice**: Users and verifiers choose the most appropriate system per use case
- **Regulatory Compliance**: Alignment with varying national and international requirements through multiple options

## Technical Architecture

### Dual Infrastructure Components

#### Classical PKI Infrastructure (Complete Pilot1 Implementation)
- **Trust Model**: Classical PKI with hierarchical certificate authorities
- **Credential Format**: SD-JWT (Selective Disclosure JSON Web Token)
- **Platform**: SUNET/SURF SaaS environment
- **Wallet Technology**: wwWallet for credential storage and management
- **Endpoint**: Separate PKI-based public endpoint for classical verification
- **Implementation**: Full Pilot1 specifications and requirements

#### Decentralised PKI Infrastructure (Complete Pilot2 Implementation)
- **Trust Model**: Decentralised PKI with EBSI integration
- **Credential Format**: W3C Verifiable Credentials
- **Platform**: ATOS/IZERTIS Dockerised solution
- **Wallet Technology**: EUDI Wallet (EUDIW by IZERTIS)
- **Endpoint**: Separate dPKI-based public endpoint for decentralised verification
- **Implementation**: Full Pilot2 specifications and requirements

### Implementation Requirements

#### Complete Parallel Implementation
**Infrastructure Obligations**
- **Separate Deployment**: Both Pilot1 and Pilot2 infrastructure fully operational as independent systems
- **Dual Evidence Provision**: All onboarding requirements for both pilots completed separately
- **Independent System Management**: Separate operational procedures for each trust model
- **Parallel Maintenance**: Simultaneous but independent support for both systems

## Current Pilot3 Participating Institutions

### Netherlands Implementation

#### University of Twente (UTWENTE)
- **Classical PKI System**: SUNET/SURF SaaS instance (Pilot1)
- **Decentralised PKI System**: `lsput.utwente.nl` (Pilot2)
- **DID Implementation**: `did:ebsi:zkZ45tZchyqA5NwQ5s9jPLN`
- **SPOC**: Helenn Vanderzaag
- **Implementation Status**: Complete parallel deployment

#### Saxion University of Applied Sciences (SAXION)
- **Classical PKI System**: SUNET/SURF SaaS instance (Pilot1)
- **Decentralised PKI System**: `lspsaxion.saxion.nl` (Pilot2)
- **DID Implementation**: `did:ebsi:zZ97WmbVmSr6UpU5jb5X8HK`
- **SPOC**: Helenn Vanderzaag
- **Implementation Status**: Full operational deployment

### Portugal Implementation

#### COFAC - Lusófona University (ULUSOFONA)
- **Classical PKI System**: SUNET/SURF SaaS instance (Pilot1)
- **Decentralised PKI System**: `lspulusofona.ulusofona.pt` (Pilot2)
- **DID Implementation**: `did:ebsi:zrmS9sGhR5J6vHu2gzMkN8t`
- **SPOC**: Rui Ribeiro
- **Implementation Status**: Complete dual infrastructure

## Implementation Experience and Lessons Learned

### Piloting Agent Feedback Summary

Based on comprehensive surveys conducted with participating institutions:

**Implementation Assessment**
- **Average Recommendation Score**: 6.3/10 (across 6 piloting agent responses)
- **Problem Rate**: 67% (4 of 6 responses encountered technical issues)
- **Success Stories**: COFAC achieved highest satisfaction (9/10), Saxion showed strong performance (7-8/10 range)

**Common Implementation Challenges**
- Credential retrieval issues in wallet applications
- Integration complexity with existing institutional systems
- User interface and experience refinements needed
- Technical coordination between parallel systems

### End-User Experience Data

Comprehensive end-user surveys collected 146 responses across all 3 institutions:

**Participation Metrics**
- **University of Twente**: 84 responses (highest participation)
- **Saxion University**: 52 responses (strong participation)
- **COFAC - Lusófona**: 10 responses (good participation)

**Key Findings**
- Users experienced both Classical PKI and Decentralised PKI approaches
- Mixed pilot type reporting reflects the dual nature of Pilot3 testing
- Users appreciated having multiple verification pathways available

## Implementation Benefits and Capabilities

### Maximum System Flexibility
**Multi-Modal Credential Support**
- **Independent SD-JWT System**: Complete classical PKI-based selective disclosure tokens
- **Independent W3C VC System**: Full standards-compliant verifiable credentials
- **Dual Wallet Support**: Separate wwWallet and EUDI Wallet implementations
- **Diverse Verifier Support**: Compatibility with both traditional and modern verification systems

### Comprehensive Trust Coverage
**Universal Verification Compatibility**
- **Legacy System Support**: Full traditional PKI-based verification capabilities
- **Modern System Support**: Complete decentralised identity verification capabilities
- **Choice-Based Verification**: Users select optimal system per interaction
- **Future-Proof Strategy**: Parallel preparation for emerging standards and technologies

### Risk Mitigation Through Redundancy
**Operational Resilience**
- **System Redundancy**: Alternative trust pathways if one system experiences issues
- **Technology Diversification**: Multiple verification mechanisms available independently
- **Standards Evolution**: Smooth transition capability as standards develop
- **Regulatory Flexibility**: Compliance with diverse regulatory requirements through choice

## Institutional Implementation Strategies

### For Educational Institutions

#### Dual Assessment and Planning
1. **Parallel Infrastructure Assessment**: Evaluate capacity for managing both trust models independently
2. **Use Case Analysis**: Determine optimal trust model selection for different institutional scenarios
3. **Resource Allocation**: Plan technical and human resources for dual independent implementation
4. **Phased Deployment**: Develop timeline for sequential or parallel system deployment

#### Implementation Pathway
**Phase 1: Infrastructure Preparation**
- Establish both Classical PKI and dPKI infrastructure capabilities as separate systems
- Configure independent endpoints and management interfaces
- Integrate with institutional identity and academic record systems for both pilots

**Phase 2: Pilot Testing**
- Deploy limited-scope testing with select user groups on both systems
- Validate both trust model implementations independently
- Test user journey flows across both systems separately

**Phase 3: Production Deployment**
- Scale to full institutional implementation of both systems
- Provide comprehensive user training for both independent systems
- Establish operational procedures for parallel system management

### For Technology Partners

#### Technical Integration Requirements
**Classical PKI Component (Complete Pilot1)**
- X.509v3 PKI certificate management
- SD-JWT credential processing capabilities
- wwWallet integration and support
- Traditional PKI infrastructure maintenance

**Decentralised PKI Component (Complete Pilot2)**
- DID registration and management capabilities
- W3C VC standards implementation
- EBSI blockchain integration
- EUDI wallet compatibility and support

#### Parallel System Management
- **Independent System Administration**: Separate management interfaces for each trust model
- **Credential Format Specialisation**: Distinct processing for SD-JWT and W3C VC formats
- **Operational Monitoring**: Independent oversight of both infrastructure components
- **Support Coordination**: Separate but coordinated technical support for both platforms

## Directory Structure

### Infrastructure Documentation (`/infrastructure`)
- **Parallel Implementation Architecture**: Independent system specifications
- **Classical PKI Setup**: Complete Pilot1 infrastructure requirements
- **Decentralised PKI Setup**: Complete Pilot2 DID and blockchain integration procedures
- **Dual System Management**: Parallel operational procedures

### Piloting Agent Scenarios (`/PAs`)
- **Netherlands Implementation Reports**: UTWENTE and SAXION dual deployment documentation
- **Portugal Implementation Reports**: ULUSOFONA comprehensive parallel implementation analysis
- **Comparative Analysis**: Assessment of both trust approaches operating independently
- **Lessons Learned Documentation**: Best practices and implementation insights from dual deployment

### User Journey Documentation (`/userjourneys`)
- **Independent System User Flows**: Separate classical and decentralised user journeys
- **System Selection Guidance**: User decision-making support for choosing appropriate system
- **Parallel Credential Management**: Independent credential lifecycle procedures
- **Multiple Verification Options**: Documentation for diverse verification pathway selection

## Related Documentation

### Cross-Reference Links
- [**Piloting Status Tracker**](../procedures/piloting/piloting-status-tracker.md) - Comprehensive dual implementation status monitoring
- [**Deployment Methodology**](../procedures/Deployment_methodology.md) - Parallel implementation framework
- [**Compliance Tracking**](../procedures/entities/compliance.md) - Dual system compliance monitoring
- [**Pilot1 Classical PKI**](../pilot1/README.md) - Complete classical PKI component specifications
- [**Pilot2 Decentralised PKI**](../pilot2/README.md) - Complete decentralised PKI component specifications

### Technical Implementation Guides
- [Infrastructure Architecture Overview](./infrastructure/README.md)
- [Parallel Implementation Guide](./infrastructure/parallel-implementation.md)
- [Independent System Integration Procedures](./infrastructure/independent-system-integration.md)
- [Dual User Journey Templates](./userjourneys/README.md)

## Operational Considerations

### Resource Requirements
**Enhanced Technical Capability**
- **Parallel Infrastructure Maintenance**: Independent PKI and dPKI system management
- **Dual System Expertise**: Technical knowledge of both trust models operating separately
- **Increased Operational Complexity**: Monitoring and support requirements for two independent systems
- **Comprehensive Training Investment**: Staff education across both systems and their independent operation

### Strategic Benefits
**Future-Proof Implementation**
- **Technology Evolution Preparedness**: Ready for standards development with multiple pathways
- **Regulatory Flexibility**: Compliance with diverse requirements through system choice
- **Stakeholder Accommodation**: Support for varied verification preferences through independent options
- **Innovation Leadership**: Advanced implementation showcasing comprehensive best practices

## Support and Resources

### Technical Support Network
- **SUNET/SURF Classical PKI Support**: Traditional PKI infrastructure assistance
- **ATOS/IZERTIS Decentralised PKI Support**: Modern dPKI implementation guidance
- **DC4EU Project Office**: Overall coordination and strategic guidance
- **Peer Institution Network**: Knowledge sharing among Pilot3 implementers

### Best Practices and Knowledge Sharing
- **Parallel Implementation Documentation**: Comprehensive technical guides for dual deployment
- **Independent System Integration Examples**: Practical implementation patterns for separate systems
- **Operational Procedures**: Day-to-day management and maintenance guidance for both systems
- **User Experience Optimisation**: Independent system usability enhancement

### Innovation and Development
- **Standards Evolution Participation**: Active contribution to emerging standards through multiple pathways
- **Comparative Trust Model Research**: Advanced research into parallel trust architectures
- **System Interoperability Enhancement**: Continuous improvement of independent system compatibility
- **European Digital Identity Leadership**: Contributing to EUDI ecosystem development through comprehensive deployment

---

*For detailed implementation progress tracking and current status of both Classical PKI and Decentralised PKI components operating as independent parallel systems, please refer to the [Piloting Status Tracker](../procedures/piloting/piloting-status-tracker.md).*

**Note**: This Pilot3 implementation approach provides institutions with the maximum flexibility by deploying both Pilot1 and Pilot2 solutions as separate, independent systems rather than attempting to create a single hybrid solution. This parallel approach ensures full compliance with both trust models whilst providing users and verifiers with clear choices between different verification pathways.