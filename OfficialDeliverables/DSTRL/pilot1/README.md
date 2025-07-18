# DSTRL Pilot1 - Classical PKI with SD-JWT

**Digital Student Records and Transcript Ledger - Classical PKI Implementation**

Welcome to Pilot1 of the DC4EU Digital Student Records and Transcript Ledger (DSTRL) project. This pilot demonstrates the implementation of digital educational credentials using traditional Public Key Infrastructure (PKI) with Selective Disclosure JSON Web Tokens (SD-JWT) for credential format.

## Overview

Pilot1 represents a pragmatic approach to digital credential implementation that leverages existing PKI infrastructure whilst introducing modern selective disclosure capabilities. This pilot provides educational institutions with a pathway to digital credentials that builds upon familiar certificate-based trust models whilst ensuring compliance with European digital identity standards.

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
- Standardised issuer public keys for interoperability
- Centralised trust management and coordination
- Reduced technical barriers for institutional adoption

**Alternative National Solutions**
- Support for national PKI implementations (e.g., Finnish DVV)
- Integration with existing national digital identity systems
- Flexibility for country-specific regulatory requirements

### User Experience Design
**wwWallet Integration**
- Familiar interface leveraging existing PKI user experience
- Seamless credential storage and presentation
- Cross-platform compatibility and accessibility
- Support for multiple credential types and formats

## Pilot Participants and Implementation

### Nordic and Dutch Focus
Pilot1 has been implemented across educational institutions in Northern Europe:

**Participating Countries and Institutions:**
- **Finland**: Finnish National Agency for Education (OPH)
- **Netherlands**: Amsterdam University of Applied Sciences (AUAS)
- **Denmark**: Danmarks Tekniske Universitet (DTU)
- **Sweden**: Ladok Consortium
- **Norway**: Sikt - Norwegian Agency for Shared Services in Education and Research

### Implementation Scale
- **Total Users Onboarded**: 125 across all institutions
- **Credentials Issued**: 371 educational credentials
- **Verification Scope**: Integrity checks and partial trust chain validation

## Technical Specifications

### Infrastructure Requirements

#### For Issuing Institutions
- **X.509v3 PKI Certificate**: Institutional issuer certificate
- **Public Key Infrastructure**: Standard PKI management capabilities
- **Integration APIs**: Connection to Student Information Systems
- **SaaS Access**: SUNET/SURF environment or equivalent national solution

#### For Verifying Institutions
- **X.509v3 PMI Certificate**: Relying party certificate for verification
- **Certificate Validation**: CRL and OCSP checking capabilities
- **Verification Infrastructure**: PKI-based trust chain validation
- **API Integration**: Connection to verification services

### Supported Credential Types
- **Educational ID**: Institutional identity credentials for students and staff
- **Academic Diplomas**: Formal qualification certificates
- **Transcripts of Records**: Academic achievement documentation
- **Professional Qualifications**: Vocational and professional certifications

## User Journey Flows

### Credential Issuance Journey
1. **User Onboarding**: PKI-based authentication and identity verification
2. **Credential Request**: Initiation through institutional systems
3. **Identity Verification**: PKI certificate-based authentication
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
1. **Infrastructure Review**: Evaluate existing PKI capabilities
2. **Integration Planning**: Assess Student Information System compatibility
3. **Regulatory Alignment**: Ensure compliance with national requirements
4. **User Community Preparation**: Plan staff and student onboarding

#### Implementation Steps
1. **Environment Setup**: Configure SUNET/SURF SaaS access or national equivalent
2. **Certificate Provisioning**: Obtain necessary PKI certificates
3. **System Integration**: Connect institutional systems to credential platform
4. **Testing and Validation**: Conduct pilot testing with limited user groups
5. **Production Deployment**: Scale to full institutional implementation

### For Technology Partners

#### Technical Integration
- **API Documentation**: RESTful services for credential operations
- **SDK Availability**: Development libraries and integration tools
- **Testing Frameworks**: Validation and compliance testing tools
- **Support Resources**: Technical documentation and community forums

## Success Metrics and Evaluation

### Technical Performance Indicators
- **Credential Issuance Success Rate**: Target >95% successful issuance
- **Verification Response Time**: <5 seconds for trust chain validation
- **System Availability**: >99% uptime for critical services
- **Error Rate**: <1% for credential operations

### User Experience Metrics
- **User Adoption Rate**: Percentage of eligible users onboarded
- **User Satisfaction**: Feedback scores and usability assessments
- **Support Request Volume**: Technical assistance requirements
- **Training Effectiveness**: User competency development

### Institutional Impact Assessment
- **Administrative Efficiency**: Reduction in manual credential processing
- **Cost Effectiveness**: Operational cost comparison with traditional methods
- **Security Improvement**: Incident reduction and fraud prevention
- **Compliance Achievement**: Regulatory requirement fulfilment

## Future Development and Evolution

### Short-term Enhancements
- **Complete RP Certificate Infrastructure**: Enable full cross-border verification
- **Enhanced Lifecycle Management**: Implement comprehensive revocation systems
- **Extended Credential Types**: Support additional educational credential formats
- **Performance Optimisation**: Improve response times and scalability

### Long-term Strategic Alignment
- **eIDAS 2.0 Preparation**: Evolution towards new regulatory requirements
- **Hybrid Trust Models**: Integration pathways with decentralised approaches
- **EUDI Wallet Compatibility**: Alignment with European digital wallet initiatives
- **Cross-Pilot Interoperability**: Integration with Pilot2 capabilities

## Support and Resources

### Technical Support
- **SUNET/SURF Technical Team**: SaaS platform support and maintenance
- **DC4EU Project Team**: Implementation guidance and best practices
- **Community Forums**: Peer support and knowledge sharing
- **Documentation Portal**: Comprehensive technical and operational guides

### Training and Capacity Building
- **Technical Training**: PKI and SD-JWT implementation workshops
- **Operational Training**: Credential management and verification procedures
- **User Training**: End-user guidance for students and staff
- **Leadership Briefings**: Strategic overview for institutional decision-makers

## Compliance and Security

### Regulatory Alignment
- **eIDAS Compliance**: Current and future regulatory requirement satisfaction
- **GDPR Implementation**: Data protection and privacy safeguards
- **National Regulations**: Country-specific compliance requirements
- **Educational Standards**: Alignment with academic quality frameworks

### Security Framework
- **PKI Security**: Certificate-based authentication and encryption
- **Audit Trail**: Comprehensive logging and monitoring capabilities
- **Incident Response**: Security event detection and response procedures
- **Regular Assessment**: Ongoing security evaluation and improvement

---

**Contact Information:**
- **Project Website**: https://www.dc4eu.eu
- **Technical Documentation**: Available through DC4EU project resources
- **Implementation Support**: Contact your national education research network
- **Community Support**: Access through DC4EU community channels

*Pilot1 provides a proven pathway for educational institutions to begin their digital credential journey whilst leveraging existing PKI investments and expertise. The classical approach ensures compatibility with current systems whilst introducing modern selective disclosure capabilities essential for privacy-preserving credential management.*