# DSTRL Pilot3 - Combined Implementation (Pilot1 + Pilot2)

**Digital Student Records and Transcript Ledger - Dual Trust Model Implementation**

Welcome to Pilot3 of the DC4EU Digital Student Records and Transcript Ledger (DSTRL) project. This pilot demonstrates the simultaneous implementation of both Classical PKI (Pilot1) and Hybrid Trust (Pilot2) approaches, providing educational institutions with comprehensive dual trust model capabilities and maximum flexibility for credential issuance and verification.

## Overview

Pilot3 represents the most comprehensive approach within the DC4EU piloting framework, enabling institutions to operate both classical PKI-based and decentralised PKI-based credential systems simultaneously. This approach provides maximum flexibility for institutional stakeholders whilst ensuring compatibility with diverse verification requirements and regulatory frameworks across different contexts and jurisdictions.

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
- **Dual Evidence Provision**: All onboarding requirements for both trust models
- **Separate Public Endpoints**: Distinct access points for each trust model
- **Unified Management**: Coordinated administration across both systems

**Technical Specifications**
- **Classical PKI**: X.509v3 certificates, CRL coordination, traditional PKI management
- **Decentralised PKI**: DID registration, EBSI integration, W3C VC support
- **Cross-System Compatibility**: Unified user accounts and credential mapping

## Pilot3 Participating Institutions

### Current Implementation Scope
Three European institutions have successfully implemented Pilot3:

#### Netherlands (2 institutions)
**University of Twente (UTWENTE)**
- **Focus**: Technical and engineering education programmes
- **Classical PKI**: 60 users, 172 credentials (SD-JWT format)
- **dPKI**: 60 users, 180 credentials (W3C VC format)
- **SPOC**: Marten van Sinderen
- **dPKI DID**: `did:ebsi:zS6r8mbU5UjXh7rHK9W6vJ2`

**Saxion University of Applied Sciences (SAXION)**
- **Focus**: Applied sciences and professional education
- **Classical PKI**: 30 users, 120 credentials (SD-JWT format)
- **dPKI**: 30 users, 90 credentials (W3C VC format)
- **SPOC**: Franco de Vitta
- **dPKI DID**: `did:ebsi:zZ97WmbVmSr6UpU5jb5X8HK`

#### Portugal (1 institution)
**COFAC - Lusófona University (ULUSOFONA)**
- **Focus**: Private international education
- **Implementation Status**: Full infrastructure deployment (both trust models)
- **SPOC**: Paulo Ferreira
- **dPKI DID**: `did:ebsi:zrmS9sGhR5J6vHu2gzMkN8t`

### Aggregate Implementation Impact
- **Total Users**: 90 across both trust models
- **Total Credentials**: 562 credentials across dual frameworks
- **Classical PKI Credentials**: 292 (SD-JWT format)
- **dPKI Credentials**: 270 (W3C VC format)

## User Experience Architecture

### Multi-Path User Journeys
Pilot3 users have multiple interaction pathways available:

#### Option 1: Classical PKI Path (Pilot1 Component)
**Traditional Certificate-Based Experience**
- **Authentication**: PKI certificate-based identity verification
- **Credential Format**: SD-JWT with selective disclosure capabilities
- **Verification**: Hierarchical trust chain validation
- **User Interface**: wwWallet application for credential management

#### Option 2: Decentralised PKI Path (Pilot2 Component)
**Next-Generation Digital Identity Experience**
- **Authentication**: DID-based decentralised identity management
- **Credential Format**: W3C Verifiable Credentials
- **Verification**: Hybrid PKI + EBSI blockchain validation
- **User Interface**: EUDI Wallet for credential storage and presentation

#### Option 3: Hybrid Usage Pattern
**Flexible Context-Appropriate Selection**
- **Use Case Optimisation**: Select optimal trust model per interaction
- **Verifier Compatibility**: Adapt to recipient system capabilities
- **Personal Preference**: User choice based on comfort and familiarity
- **Technical Constraints**: Fallback options for system limitations

### Complete User Journey Coverage

#### Universal Journey Support
**From Pilot1 (Classical PKI)**
- PKI-based user onboarding and authentication workflows
- SD-JWT credential request and issuance procedures
- Certificate-based credential verification processes
- Cross-border PKI credential recognition mechanisms

**From Pilot2 (Decentralised PKI)**
- DID-based user onboarding and identity management
- W3C VC credential request and issuance workflows
- Decentralised credential verification procedures
- EBSI-based cross-border credential recognition

#### Integrated User Experience
- **Unified Account Management**: Consistent user profiles across both systems
- **Credential Portfolio**: Combined view of all credentials regardless of format
- **Presentation Choice**: User selects appropriate credential format per context
- **Seamless Transition**: Ability to move between trust models without friction

## Comparative Technical Analysis

### Infrastructure Implementation Comparison

| Component | Classical PKI (Pilot1) | dPKI (Pilot2) |
|-----------|------------------------|---------------|
| **Platform Provider** | SUNET/SURF | ATOS/IZERTIS |
| **Deployment Model** | SaaS | Dockerised |
| **Wallet Technology** | wwWallet | EUDI Wallet |
| **Credential Format** | SD-JWT | W3C VC |
| **Trust Mechanism** | X.509 PKI only | Hybrid PKI + DID |
| **Cross-Border Verification** | Limited | Full capability |
| **Governance Layer** | Static | Dynamic |

### User Journey Performance Analysis

#### Successful Implementation Outcomes
**Universal Completion Across Trust Models**
- ✅ **Wallet Installation**: 100% success rate for both wallet types
- ✅ **PID Retrieval**: Complete implementation across both trust approaches
- ✅ **Educational ID Issuance**: Successful operation in both Classical PKI and dPKI
- ✅ **Diploma Issuance**: Full implementation across both trust frameworks
- ⚠️ **Verification Capabilities**: Classical PKI limited to integrity checks, dPKI offers full verification

#### Performance and Limitation Analysis
**Classical PKI Component Constraints**
- **Verification Limitations**: No RP certificates available, preventing full cross-border verification
- **Lifecycle Management**: Limited revocation and suspension capabilities
- **Static Governance**: PKI certificates provide identity confirmation but not dynamic authorisation

**dPKI Component Advantages**
- **Complete Verification**: Full trust chain validation and cross-border recognition
- **Dynamic Governance**: Real-time policy updates and trust management
- **Future Compatibility**: Alignment with eIDAS 2.0 and EUDI wallet ecosystem

## Implementation Guidance

### For Educational Institutions

#### Strategic Planning and Assessment
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
- **Classical PKI Setup**: Traditional certificate-based infrastructure
- **dPKI Implementation**: Decentralised PKI deployment procedures
- **Integration Guidelines**: Unified system management best practices

### Pilot Agent Documentation (`/PAs`)
- **University of Twente Implementation**: Technical education dual trust model
- **Saxion Applied Sciences Case**: Professional education implementation
- **Lusófona International Education**: Private sector dual implementation
- **Comparative Analysis**: Cross-institutional implementation insights

### User Journey Documentation (`/userjourneys`)
- **Combined User Journey Flows**: Integrated experience across both trust models
- **Trust Model Selection Guidelines**: User guidance for optimal system choice
- **Credential Format Guidance**: Understanding SD-JWT vs W3C VC applications
- **Troubleshooting and Support**: Comprehensive user assistance procedures

## Benefits and Value Proposition

### Maximum Flexibility and Compatibility
- **Universal Verifier Support**: Compatibility with any verification system preference
- **Regulatory Compliance**: Alignment with current and future regulatory requirements
- **Technology Evolution**: Smooth transition pathway as standards evolve
- **Risk Mitigation**: Reduced dependency on single trust model or technology

### Comprehensive User Choice
- **Context-Appropriate Selection**: Optimal trust model for each use case
- **User Preference**: Individual choice based on comfort and requirements
- **Verifier Accommodation**: Ability to meet diverse verification system needs
- **Future-Proof Experience**: Compatibility with evolving digital credential ecosystem

### Institutional Strategic Advantages
- **Complete Preparedness**: Readiness for any future regulatory or technological changes
- **Market Leadership**: Demonstration of comprehensive digital credential capabilities
- **Stakeholder Confidence**: Assurance of continued service regardless of technology evolution
- **Innovation Platform**: Foundation for advanced credential system development

## Success Metrics and Evaluation

### Technical Performance Assessment
- **Dual System Uptime**: >99% availability across both trust models
- **Cross-System Integration**: Seamless user experience between trust models
- **Credential Interoperability**: Successful mapping between SD-JWT and W3C VC formats
- **Performance Optimisation**: Comparable response times across both systems

### User Experience Evaluation
- **Trust Model Selection**: User preference patterns and decision factors
- **System Satisfaction**: Comparative user experience across both trust models
- **Learning Curve**: User adaptation time for dual system capabilities
- **Support Requirements**: Technical assistance needs for complex implementation

### Institutional Impact Analysis
- **Implementation Complexity**: Resource requirements for dual trust model deployment
- **Operational Efficiency**: Comparative administrative burden assessment
- **Strategic Positioning**: Institutional readiness for future regulatory changes
- **Innovation Enablement**: Advanced capability development opportunities

## Future Development and Evolution

### Short-term Enhancements
- **Performance Optimisation**: Improved efficiency across both trust models
- **User Interface Integration**: Enhanced unified experience across systems
- **Credential Migration**: Tools for moving credentials between trust models
- **Advanced Analytics**: Comprehensive usage and performance monitoring

### Long-term Strategic Alignment
- **Regulatory Evolution**: Adaptation to eIDAS 2.0 and future requirements
- **Technology Convergence**: Integration of classical and decentralised approaches
- **Global Interoperability**: Extension to international credential recognition
- **Next-Generation Standards**: Preparation for emerging credential technologies

## Support and Resources

### Comprehensive Technical Support
- **SUNET/SURF Platform**: Classical PKI SaaS infrastructure support
- **ATOS/IZERTIS Platform**: Decentralised PKI Dockerised solution support
- **DC4EU Consortium**: Multi-partner technical collaboration and guidance
- **Community Resources**: Peer support and knowledge sharing forums

### Specialised Training and Capacity Building
- **Dual Trust Model Workshops**: Comprehensive implementation training
- **User Experience Training**: End-user guidance for both systems
- **Technical Integration Support**: Developer and administrator training
- **Strategic Planning Assistance**: Institutional transformation guidance

---

**Contact Information:**
- **Project Website**: https://www.dc4eu.eu
- **Technical Documentation**: Comprehensive dual implementation guides
- **Implementation Support**: Contact DC4EU consortium for specialised assistance
- **Community Forums**: Access peer support and knowledge sharing

*Pilot3 provides educational institutions with the most comprehensive and future-proof approach to digital credential implementation, ensuring compatibility with all current and anticipated future requirements whilst maximising user choice and institutional flexibility.*