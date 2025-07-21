# DC4EU Piloting Agents Progress Tracker - PKI Status Overview

**Document Version**: Latest Status Update  
**Source**: DC4EU Tracker PKI Corrected  
**Last Updated**: July 2025  

## Executive Summary

This document provides a comprehensive overview of the current piloting status across all DC4EU implementations, tracking the progress of educational institutions participating in the Digital Credentials for Europe (DC4EU) project. The tracker monitors three distinct pilot implementations and their associated technical requirements, infrastructure deployment, and compliance status.

## Pilot Implementation Overview

### Pilot Architecture Summary

The DC4EU project implements three distinct pilot configurations:

- **Pilot 1**: Classical PKI with SD-JWT credentials
- **Pilot 2**: Hybrid Trust (Classical PKI + Decentralised PKI) with W3C Verifiable Credentials  
- **Pilot 3**: Combined implementation (Pilot 1 + Pilot 2) with dual trust models

## Current Piloting Status by Categories

### Pilot 1 - Classical PKI Implementation

**Participating Countries**: Denmark, Finland, Netherlands, Norway, Sweden  
**Total Institutions**: 5 organisations  
**Trust Model**: Classical PKI with hierarchical certificate authorities  
**Credential Format**: SD-JWT (Selective Disclosure JSON Web Token)  

#### Key Technical Requirements Status:
- **X.509v3 Issuer Certificates**: Mixed implementation status (partial completion)
- **X.509v3 RP Certificates**: Limited provision in current pilot environment  
- **CRL Implementation**: Partial deployment across participating institutions
- **Scenarios Templates**: Fully provided across all participants
- **DNS Availability**: Limited (SaaS instances managed by SUNET/SURF)

### Pilot 2 - Decentralised PKI Implementation

**Participating Countries**: Belgium, Germany, Hungary, Italy, Lithuania, Poland, Portugal, Romania, Spain, Sweden  
**Total Institutions**: 28 organisations  
**Trust Model**: Hybrid Classical PKI + Decentralised PKI  
**Credential Format**: W3C Verifiable Credentials  

#### Key Technical Requirements Status:
- **DID Issuer Implementation**: Fully deployed across all participants
- **DID Verifier Implementation**: Fully deployed across all participants  
- **DNS Endpoints Available**: Complete availability for cross-border verification
- **Scenarios Templates**: Universally provided
- **Progress Templates**: Up to date across all implementations

### Pilot 3 - Combined Implementation

**Sub-Categories**:

#### Pilot 3 PKI (Classical PKI Component)
**Participating Countries**: Netherlands, Portugal  
**Total Institutions**: 3 organisations  
**Implementation**: SaaS instances by SUNET/SURF

#### Pilot 3 dPKI (Decentralised PKI Component)  
**Participating Countries**: Netherlands, Portugal  
**Total Institutions**: 3 organisations  
**Implementation**: Dockerised solutions by ATOS/Izertis

## Geographic Distribution and Deployment Modalities

### Implementation Approaches by Region

#### Nordic Region (Denmark, Finland, Norway, Sweden)
- **Primary Approach**: Classical PKI (Pilot 1) with SaaS deployment
- **Technical Infrastructure**: SUNET/SURF managed environments
- **National Integration**: Strong alignment with existing NREN infrastructure

#### Central and Southern Europe (Germany, Hungary, Italy, Lithuania, Poland, Portugal, Romania, Spain)
- **Primary Approach**: Decentralised PKI (Pilot 2) 
- **Technical Infrastructure**: Mix of Dockerised solutions and national SaaS instances
- **Special Cases**: Poland operates national SaaS instances through OPI/NASK

#### Netherlands and Portugal (Pilot 3 Participants)
- **Comprehensive Approach**: Dual trust model implementation
- **Infrastructure Requirements**: Both classical and decentralised PKI capabilities

## Technical Progress Indicators

### Cross-Border Verification Readiness

#### DNS Endpoint Availability
- **Pilot 1**: Limited availability (SaaS managed endpoints)
- **Pilot 2**: 100% availability enabling full cross-border verification
- **Pilot 3**: Mixed availability based on component implementation

#### Certificate Infrastructure Status
- **X.509v3 Implementation**: Concentrated in Pilot 1 and Pilot 3 PKI components
- **DID Infrastructure**: Universal deployment in Pilot 2 and Pilot 3 dPKI components
- **Trust Chain Validation**: Operational across decentralised implementations

### Credential Format Implementation

#### SD-JWT Deployment (Pilot 1 & Pilot 3 PKI)
- **Format Compliance**: Standards-compliant implementation
- **Selective Disclosure**: Privacy-preserving capabilities enabled
- **PKI Integration**: Traditional certificate-based trust validation

#### W3C Verifiable Credentials Deployment (Pilot 2 & Pilot 3 dPKI)
- **Standards Compliance**: W3C-VCDM 1.1 & 2.0 alignment
- **Semantic Interoperability**: JSON-LD format implementation
- **EBSI Integration**: European blockchain infrastructure anchoring

## Implementation Quality Assurance

### Scenario Template Compliance
- **Pilot 1**: 100% compliance across all participants
- **Pilot 2**: Universal deployment with comprehensive user journey coverage
- **Pilot 3**: Complete coverage across both PKI and dPKI components

### Progress Template Updates (3.1 Requirements)
- **Current Status**: Universally updated across all active implementations
- **Compliance Level**: Full alignment with latest project requirements
- **Documentation Quality**: Comprehensive implementation evidence provided

## Outstanding Technical Requirements

### Cross-Border Verification Limitations

#### Pilot 1 Constraints
- **RP Certificate Availability**: Limited relying party certificate provisioning
- **Full Trust Chain Validation**: Restricted by current SaaS environment configuration
- **CRL Infrastructure**: Partial deployment affecting real-time status verification

#### Infrastructure Scaling Requirements
- **DNS Resolution**: Enhanced coordination for Pilot 1 SaaS instances
- **Certificate Distribution**: Improved PKI certificate availability for RP verification
- **Revocation Management**: Expanded CRL/OCSP infrastructure deployment

## Regional Implementation Patterns

### Northern European Approach (Nordic States)
- **Infrastructure Preference**: Established NREN infrastructure leverage
- **Trust Model Selection**: Classical PKI alignment with existing systems
- **Implementation Strategy**: Collaborative SaaS deployment through SUNET/SURF

### Southern and Eastern European Approach
- **Infrastructure Preference**: Flexible dockerised deployment
- **Trust Model Selection**: Forward-looking decentralised PKI implementation
- **Implementation Strategy**: National and institutional autonomy with ATOS/Izertis support

### Combined Approach Pioneers (Netherlands, Portugal)
- **Strategic Position**: Dual trust model capability for maximum flexibility
- **Infrastructure Investment**: Comprehensive technical capability development
- **Future Readiness**: Preparation for diverse verification requirements

## Operational Insights and Recommendations

### Successful Implementation Patterns

#### High-Performance Deployments
- **Complete DNS Infrastructure**: Enables full cross-border verification capability
- **Comprehensive DID Implementation**: Provides robust decentralised trust establishment
- **Updated Documentation**: Ensures compliance with latest project requirements

#### Areas Requiring Enhanced Support
- **Classical PKI Scaling**: Enhanced RP certificate provisioning and CRL infrastructure
- **Cross-Pilot Interoperability**: Improved integration between different trust models
- **Regional Coordination**: Strengthened collaboration across implementation approaches

### Strategic Implementation Guidance

#### For New Piloting Agents
1. **Pilot Selection**: Align choice with institutional infrastructure and regulatory requirements
2. **Technical Preparation**: Ensure adequate technical resources for chosen implementation approach
3. **Compliance Planning**: Prepare comprehensive documentation and evidence requirements
4. **Community Engagement**: Leverage existing piloting agent experiences and best practices

#### For Current Participants
1. **Infrastructure Optimisation**: Address outstanding technical requirements systematically
2. **Cross-Border Testing**: Enhance verification capability testing with international partners
3. **Documentation Maintenance**: Ensure continuous alignment with evolving project requirements
4. **User Experience Improvement**: Refine implementation based on operational feedback

## Conclusion

The DC4EU piloting programme demonstrates significant progress across diverse technical implementations and geographical regions. The current status reflects successful deployment of innovative digital credential infrastructure while highlighting specific areas requiring continued attention and development.

The diversity of implementation approaches across Pilot 1 (Classical PKI), Pilot 2 (Decentralised PKI), and Pilot 3 (Combined) provides valuable insights into different pathways for digital credential adoption within the European higher education sector. This comprehensive approach ensures that the DC4EU project can accommodate various institutional requirements, regulatory frameworks, and technical capabilities across participating member states.

## Related Documentation and Cross-References

### Strategic Implementation Documentation
- [**Pilot 1 Classical PKI Implementation**](../../pilot1/README.md) - Traditional PKI deployment approach and current status
- [**Pilot 2 Decentralised PKI Implementation**](../../pilot2/README.md) - Modern decentralised identity deployment and achievements
- [**Pilot 3 Combined Implementation**](../../pilot3/README.md) - Dual trust model deployment strategy and institutional examples

### Operational Framework and Procedures
- [**Deployment Methodology**](../Deployment_methodology.md) - Standardised implementation framework referencing this tracker
- [**Compliance Tracking Framework**](../entities/compliance.md) - Regulatory compliance monitoring utilising tracker data
- [**Entity Implementation Procedures**](../entities/implementation.md) - Technical implementation specifications

### Technical Documentation and Resources
- [**Infrastructure Implementation Standards**](../../elements/README.md) - Technical deployment specifications
- [**Quality Assurance Framework**](../../elements/documents/MyAcademicID/README.md) - Quality management procedures
- [**User Journey Templates**](../../pilot1/userjourneys/README.md) - Standardised user experience documentation

### Institutional Implementation Resources
- [**Pilot 1 Participating Agents**](../../pilot1/PAs/README.md) - Classical PKI institutional implementations
- [**Pilot 2 Participating Agents**](../../pilot2/PAs/README.md) - Decentralised PKI institutional implementations  
- [**Pilot 3 Participating Agents**](../../pilot3/PAs/README.md) - Combined implementation institutional approaches

## Usage Guidelines for Stakeholders

### For Project Management
This status tracker serves as the authoritative source for current implementation progress across all DC4EU pilots. Use this document for:
- **Progress Reporting**: Accurate status updates for European Commission reporting
- **Resource Planning**: Identifying institutions requiring additional support
- **Risk Assessment**: Monitoring technical implementation challenges
- **Success Measurement**: Tracking achievement of cross-border verification capabilities

### For Piloting Agents  
Participating institutions should reference this tracker to:
- **Compare Progress**: Benchmark implementation status against peer institutions
- **Identify Best Practices**: Learn from successful implementations in similar contexts
- **Plan Improvements**: Address gaps in technical requirements or documentation
- **Coordinate Cross-Border Testing**: Identify potential verification partners

### For Technical Partners
Technology providers and integration partners should utilise this tracker for:
- **Implementation Support**: Prioritise assistance based on current implementation status
- **Quality Assurance**: Monitor compliance with technical standards across deployments
- **Innovation Development**: Identify successful patterns for broader implementation
- **Standards Evolution**: Track real-world implementation challenges and successes

### For Policy and Regulatory Stakeholders
European and national policy makers should reference this tracker for:
- **Regulatory Impact Assessment**: Understanding real-world implementation progress
- **Standards Development**: Evidence-based input for European digital identity standards
- **Cross-Border Coordination**: Monitoring international verification capability development
- **Compliance Monitoring**: Tracking adherence to eIDAS 2.0 and GDPR requirements

---

**Data Sources**: DC4EU Tracker PKI Corrected (HTML)  
**Compilation**: Project Knowledge Analysis  
**Distribution**: DSTRL Official Deliverables Structure  
**Cross-References**: Integrated with DSTRL documentation ecosystem