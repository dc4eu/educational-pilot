# DSTRL Pilots Overview

**Deployment and Testing Scenarios Results Library - Pilot Implementations Content Summary**

This document provides a comprehensive overview of the contents within the three pilot implementation directories of the DSTRL (Deployment and Testing Scenarios Results Library). Each pilot represents a distinct technical approach to implementing digital educational credentials, with documented deployment results, testing scenarios, and institutional implementation experiences.

## Pilots Architecture Summary

The DC4EU project implements three distinct pilot configurations, each representing different trust models and technical approaches:

- **Pilot 1**: Classical PKI with SD-JWT credentials
- **Pilot 2**: Hybrid Trust (Classical PKI + Decentralised PKI) with W3C Verifiable Credentials in alignment to 1st batch of the implementing acts
- **Pilot 3**: Combined implementation (Pilot 1 + Pilot 2) with dual trust models

For real-time implementation status across all pilots, see: [**Piloting Status Tracker**](./procedures/piloting/piloting-status-tracker.md)

---

## Pilot 1: Classical PKI Implementation

### Directory: `/pilot1/`

**Implementation Approach**: Traditional Public Key Infrastructure with Selective Disclosure JSON Web Tokens  
**Trust Model**: Hierarchical certificate authorities and X.509v3 certificates  
**Platform**: SUNET/SURF SaaS environment  
**Wallet Technology**: wwWallet  

### Content Overview

#### Main Documentation [`/pilot1/README.md`]
**Purpose**: Comprehensive overview of Classical PKI implementation approach  
**Key Content**:
- Technical architecture with traditional PKI trust chains
- SD-JWT credential format implementation details
- SaaS-first deployment strategy through SUNET/SURF infrastructure
- Current implementation status and known limitations
- Cross-references to deployment methodology and status tracker

**Participating Regions**: Denmark, Finland, Netherlands, Norway, Sweden  
**Total Institutions**: 5 organisations  

#### Directory Structure Content

##### **Infrastructure Documentation** [`/pilot1/infrastructure/`]
**Purpose**: Technical implementation guidance and requirements  
**Content Areas**:
- PKI implementation guidelines and certificate management procedures
- X.509v3 certificate provisioning and trust chain establishment
- Integration specifications for institutional identity management systems
- Security configuration standards and operational guidance
- SD-JWT processing capabilities and selective disclosure implementation

**Key Technical Requirements**:
- X.509v3 PKI certificates as issuer credentials
- X.509v3 PMI certificates as relying party verification
- Certificate Revocation Lists (CRL) coordination for trust verification
- Classical PKI infrastructure maintenance and monitoring

##### **Piloting Agent Scenarios** [`/pilot1/PAs/`]
**Purpose**: Real-world implementation results from participating institutions  
**Content Areas**:
- Detailed implementation reports from Nordic educational institutions
- User journey documentation and testing outcomes
- Technical configuration examples and deployment templates
- Lessons learned from SaaS deployment approach
- Cross-border verification testing results and limitations

**Implementation Evidence**:
- Institution-specific deployment configurations
- User onboarding and training experiences
- Technical challenges and resolution approaches
- Performance metrics and user satisfaction results

##### **User Journey Documentation** [`/pilot1/userjourneys/`]
**Purpose**: Step-by-step credential lifecycle processes  
**Content Areas**:
- Credential issuance workflows with PKI authentication
- SD-JWT credential presentation and selective disclosure procedures
- Certificate-based verification processes and trust validation
- Cross-border recognition scenarios and testing results
- Error handling procedures and troubleshooting guidance

**Core User Journey Flows**:
1. PKI-based user authentication and wallet setup
2. Educational credential request and institutional validation  
3. SD-JWT credential generation and wallet delivery
4. Selective disclosure presentation to verifying parties
5. Certificate chain validation and verification decisions

### Implementation Results Summary

**Current Status**:
- **X.509v3 Certificate Implementation**: Mixed progress across participating institutions
- **DNS Endpoint Availability**: Limited due to SaaS managed infrastructure  
- **Cross-Border Verification**: Restricted to integrity checks in current deployment
- **User Experience**: Positive feedback on familiar PKI-based workflows

**Key Achievements**:
- Successful leverage of existing NREN PKI infrastructure
- Standardised implementation through collaborative SaaS approach
- Demonstrated selective disclosure privacy protection capabilities
- Validated traditional certificate-based trust model effectiveness

**Outstanding Challenges**:
- Limited relying party certificate provisioning in pilot environment
- Cross-border verification constraints due to infrastructure limitations
- Need for enhanced CRL/OCSP infrastructure for real-time status checking

---

## Pilot 2: Decentralised PKI Implementation

### Directory: `/pilot2/`

**Implementation Approach**: Hybrid trust combining Classical PKI with Decentralised PKI  
**Trust Model**: W3C Verifiable Credentials with DID-based trust and EBSI integration  
**Platform**: Multiple options (ATOS/IZERTIS Dockerised, Govpart SaaS, National implementations)  
**Wallet Technology**: EUDI Wallet (EUDIW by IZERTIS)  

### Content Overview

#### Main Documentation [`/pilot2/README.md`]
**Purpose**: Comprehensive overview of decentralised PKI implementation approach  
**Key Content**:
- Hybrid trust model architecture combining traditional and decentralised approaches
- W3C Verifiable Credentials implementation with JSON-LD format
- EBSI integration for European blockchain-based trust establishment
- Multiple deployment model options and regional implementation strategies
- Current implementation achievements and cross-border verification success

**Participating Regions**: Belgium, Germany, Hungary, Italy, Lithuania, Poland, Portugal, Romania, Spain, Sweden  
**Total Institutions**: 28 organisations  

#### Directory Structure Content

##### **Infrastructure Documentation** [`/pilot2/infrastructure/`]
**Purpose**: Decentralised identity infrastructure implementation guidance  
**Content Areas**:
- DID (Decentralised Identifier) implementation and management procedures
- EBSI (European Blockchain Services Infrastructure) integration specifications
- W3C Verifiable Credentials processing guidelines and standards compliance
- Trust registry configuration and schema registration processes
- Security architecture for cryptographic operations and key management

**Key Technical Requirements**:
- DID implementation enabling trust discovery for issuers and relying parties
- Complete education/professional qualifications governance documentation
- EBSI blockchain integration for decentralised trust establishment
- W3C VC standards compliance with JSON-LD format support

##### **Piloting Agent Scenarios** [`/pilot2/PAs/`]
**Purpose**: Diverse implementation results across multiple deployment models  
**Content Areas**:
- Multi-national case studies across 28 participating institutions
- Comparative analysis of Dockerised vs. SaaS vs. National implementations
- Spanish university implementations with comprehensive deployment reports
- Technical integration examples and real-world configuration templates
- Cross-border verification success stories and international collaboration evidence

**Implementation Evidence by Deployment Model**:
- **Dockerised Solutions**: Institutional autonomy and customisation capabilities
- **SaaS Implementations**: Managed service benefits and standardised deployment  
- **National Coordination**: Poland's OPI/NASK national infrastructure approach
- **Professional Integration**: Medical professional credentials (CGCOM Spain)

##### **User Journey Documentation** [`/pilot2/userjourneys/`]
**Purpose**: Decentralised identity user experience flows  
**Content Areas**:
- PID (Personal Identification) retrieval process with eIDAS 2.0 integration
- Educational ID issuance with DID-anchored academic identity
- Academic achievement verification and learning outcome credential validation
- EAA (European Attestation of Attributes) verification processes
- Cross-border recognition and international verification procedures

**Advanced User Journey Categories**:
- **Authentic Source Integration**: National ID systems and educational registries
- **Cross-Border Recognition Framework**: Automatic trust discovery via EBSI
- **Enhanced Lifecycle Management**: Granular status management and temporal validity
- **Professional Qualification Integration**: Recognition authority connections

### Implementation Results Summary

**Current Status**:
- **DID Implementation**: 100% successful deployment across all participating institutions
- **DNS Endpoint Availability**: Complete availability enabling full cross-border verification
- **EBSI Integration**: Universal blockchain trust registry integration achieved
- **W3C VC Standards**: Complete compliance with verifiable credentials specifications

**Key Achievements**:
- Demonstrated superior cross-border verification capabilities  
- Successful implementation of diverse deployment models accommodating institutional preferences
- Evidence of effective decentralised identity technology adoption
- Validated hybrid trust model combining traditional and innovative approaches

**Innovation Highlights**:
- First large-scale implementation of EBSI for educational credentials
- Successful integration with European Digital Identity Wallet ecosystem
- Demonstrated automatic trust discovery mechanisms across member states
- Validated real-world application of W3C Verifiable Credentials standards

---

## Pilot 3: Combined Implementation

### Directory: `/pilot3/`

**Implementation Approach**: Dual trust model supporting both Classical and Decentralised PKI  
**Architecture Definition**: `Pilot3 = Pilot1 + Pilot2`  
**Platform**: Parallel implementation of both SUNET/SURF SaaS and ATOS/IZERTIS Dockerised solutions  
**Wallet Technology**: Both wwWallet and EUDI Wallet support  

### Content Overview

#### Main Documentation [`/pilot3/README.md`]
**Purpose**: Comprehensive overview of combined dual trust model implementation  
**Key Content**:
- Dual infrastructure architecture supporting both classical and decentralised approaches
- Strategic institutional positioning for maximum verification compatibility
- Implementation requirements combining both pilot approaches
- Resource allocation and operational complexity management
- Future-proof strategy for evolving digital identity standards

**Participating Regions**: Netherlands, Portugal  
**Total Institutions**: 3 organisations (6 implementations: 3 PKI + 3 dPKI)  

#### Directory Structure Content

##### **Infrastructure Documentation** [`/pilot3/infrastructure/`]
**Purpose**: Dual trust model technical implementation specifications  
**Content Areas**:
- Combined infrastructure deployment requirements from both pilot approaches
- Dual endpoint architecture with separate PKI and dPKI verification capabilities
- Cross-system integration procedures and unified management approaches
- Classical PKI certificate management alongside DID implementation
- Operational coordination for parallel trust model maintenance

**Technical Implementation Requirements**:
- **From Pilot1**: X.509v3 certificates, CRL coordinates, classical PKI infrastructure
- **From Pilot2**: DID implementation, EBSI integration, W3C VC processing capabilities
- **Additional**: Unified user experience design and cross-system operational procedures

##### **Piloting Agent Scenarios** [`/pilot3/PAs/`]
**Purpose**: Advanced institutional implementation results demonstrating dual capabilities  
**Content Areas**:
- Netherlands implementation reports from University of Twente and Saxion University
- Portugal implementation analysis from COFAC Lusófona University
- Dual trust model comparative assessment and operational effectiveness analysis
- Resource requirement documentation and cost-benefit analysis
- Lessons learned from comprehensive dual infrastructure deployment

**Institutional Implementation Evidence**:
- **University of Twente**: Complete dual implementation with both PKI and dPKI endpoints
- **Saxion University**: Applied sciences institutional dual trust model deployment
- **COFAC Lusófona University**: International private education dual approach validation

##### **User Journey Documentation** [`/pilot3/userjourneys/`]
**Purpose**: Flexible user experience across both trust models  
**Content Areas**:
- Dual system user flows combining classical PKI and decentralised PKI options
- Trust model selection guidance for context-appropriate credential presentation
- Cross-system credential management and lifecycle procedures
- User choice and flexibility documentation for diverse verification scenarios
- Unified user experience design across both wwWallet and EUDI Wallet platforms

**User Experience Options**:
- **Option 1**: Classical PKI path for traditional certificate-based interactions
- **Option 2**: Decentralised PKI path for self-sovereign identity principles
- **Option 3**: Hybrid usage allowing dynamic selection based on requirements

### Implementation Results Summary

**Current Status**:
- **Dual Infrastructure**: Successfully demonstrated parallel operation of both trust models
- **Classical PKI Component**: SaaS implementation with SUNET/SURF managed infrastructure
- **Decentralised PKI Component**: 100% DNS availability and complete DID deployment
- **Cross-System Integration**: Validated unified user experience across both approaches

**Key Achievements**:
- Proved feasibility of comprehensive dual trust model operations
- Demonstrated maximum flexibility for diverse verification requirements
- Validated strategic institutional positioning for technology evolution
- Evidence of successful resource allocation for complex dual infrastructure

**Strategic Value**:
- **Future-Proof Strategy**: Preparation for evolving digital identity standards and regulations
- **Stakeholder Accommodation**: Support for diverse verification preferences and requirements
- **Risk Mitigation**: Alternative trust pathways providing operational resilience
- **Innovation Leadership**: Advanced implementation showcasing best practices for dual trust models

---

## Cross-Pilot Comparative Analysis

### Technical Approach Comparison

| Aspect | Pilot 1 (Classical PKI) | Pilot 2 (Decentralised PKI) | Pilot 3 (Combined) |
|--------|-------------------------|------------------------------|---------------------|
| **Trust Model** | Hierarchical PKI | Hybrid PKI + Decentralised | Dual (Both Models) |
| **Credential Format** | SD-JWT | W3C Verifiable Credentials | Both SD-JWT & W3C VC |
| **Infrastructure** | SaaS (SUNET/SURF) | Flexible deployment options | Parallel infrastructure |
| **Cross-Border Capability** | Limited (integrity checks) | Complete verification | Maximum compatibility |
| **Implementation Complexity** | Low to Medium | Medium | High |
| **Resource Requirements** | Standard | Variable by deployment | Comprehensive |

### Implementation Success Factors

#### **Pilot 1 Success Patterns**
- Effective leverage of existing PKI infrastructure and NREN partnerships
- Standardised SaaS approach reducing institutional technical burden
- Familiar technology base supporting user adoption
- Collaborative Nordic implementation model

#### **Pilot 2 Success Patterns**
- Flexible deployment options accommodating diverse institutional requirements
- Superior cross-border verification capabilities through EBSI integration
- Forward-looking technical architecture aligning with eIDAS 2.0
- Multi-national collaboration demonstrating European interoperability

#### **Pilot 3 Success Patterns**
- Strategic institutional positioning for maximum adaptability
- Comprehensive dual capability providing future-proof implementation
- Advanced technical coordination demonstrating feasibility of complex systems
- Innovation leadership in dual trust model operations

### Regional Implementation Insights

#### **Nordic Region (Pilot 1 Focus)**
- **Collaborative Approach**: Shared SaaS infrastructure through NREN partnerships
- **Infrastructure Leverage**: Building on established PKI foundations
- **Standardisation Benefits**: Coordinated implementation reducing complexity
- **Regional Coordination**: Effective cross-national collaboration model

#### **Central and Southern Europe (Pilot 2 Dominance)**
- **Innovation Adoption**: Forward-looking decentralised identity technology implementation
- **Deployment Flexibility**: Multiple approaches accommodating diverse institutional contexts
- **Technical Leadership**: Leading European blockchain and verifiable credentials adoption
- **Cross-Border Excellence**: Demonstrated international verification capabilities

#### **Strategic Pioneers (Pilot 3 Implementation)**
- **Maximum Capability**: Comprehensive dual trust model implementation
- **Resource Investment**: Significant commitment to advanced technical capabilities
- **Future Preparedness**: Strategic positioning for evolving standards and requirements
- **Innovation Demonstration**: Proof of concept for complex multi-trust-model operations

## Documentation Integration and Cross-References

### Key Integration Points

All pilot directories integrate with the broader DSTRL framework through:

- **[Piloting Status Tracker](./procedures/piloting/piloting-status-tracker.md)**: Real-time implementation monitoring across all pilots
- **[Deployment Methodology](./procedures/Deployment_methodology.md)**: Standardised implementation framework application
- **[Compliance Framework](./procedures/entities/compliance.md)**: Regulatory adherence monitoring and validation
- **[Legal Entity Framework](./procedures/entities-main-framework.md)**: Organisational role definition and compliance requirements

### Documentation Quality and Standards

Each pilot directory maintains:
- **Comprehensive README files**: Strategic overview and navigation guidance
- **Technical Documentation**: Infrastructure implementation specifications
- **Implementation Evidence**: Real-world deployment results and lessons learned
- **User Experience Documentation**: Complete user journey flows and procedures
- **Cross-Reference Integration**: Systematic linking to broader DSTRL framework

## Strategic Recommendations

### For Future Implementations

#### **Pilot Selection Guidance**
- **Choose Pilot 1**: Institutions with established PKI infrastructure seeking familiar implementation approach
- **Choose Pilot 2**: Forward-looking institutions ready for decentralised identity and eIDAS 2.0 preparation
- **Choose Pilot 3**: Strategic institutions seeking maximum flexibility and comprehensive verification compatibility

#### **Implementation Success Factors**
- **Technical Preparation**: Adequate infrastructure assessment and resource allocation
- **Staff Training**: Comprehensive education programmes for operational teams
- **Cross-Border Planning**: Early engagement with international verification partnerships
- **User Experience Focus**: Systematic user onboarding and support development

### For Policy and Standards Development

#### **Evidence-Based Recommendations**
- **Standards Adoption**: Strong evidence supporting W3C Verifiable Credentials and EBSI integration
- **Cross-Border Frameworks**: Validated mechanisms for international credential recognition
- **Regulatory Preparation**: Demonstrated pathways for eIDAS 2.0 compliance and implementation
- **Technology Evolution**: Evidence supporting decentralised identity adoption in European context

---

**Document Purpose**: Comprehensive overview of DSTRL pilot implementation directories and content  
**Target Audience**: Project stakeholders, implementation teams, policy makers, and research communities  
**Maintenance**: Updated with ongoing piloting results and lessons learned  
**Version**: 2.0 (Comprehensive Implementation Results Integration)  
**Last Updated**: July 2025