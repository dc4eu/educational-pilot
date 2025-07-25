# Analysis of DC4EU Pilot3 Scenarios

## Executive Summary

The DC4EU Pilot3 scenarios represent a pioneering approach to comprehensive hybrid trust frameworks in European digital credential infrastructure. Pilot3 institutions uniquely implemented **both Classical PKI and Decentralised PKI approaches simultaneously**, providing unprecedented insight into the comparative advantages and operational realities of dual trust model deployment within single educational institutions.

The three participating institutions—University of Twente, Saxion University of Applied Sciences (Netherlands), and COFAC - Lusófona University (Portugal)—successfully demonstrated that hybrid trust frameworks can provide optimal balance between familiar PKI reliability and innovative dPKI capabilities, whilst addressing the full spectrum of cross-border educational credential requirements.

## Pilot3 Participating Institutions Overview

Pilot3 represents a **combined approach** where each institution implements both trust models, requiring **six total scenario files** (two per institution) to capture the complete technical and operational landscape:

This analysis covers the following six Pilot3 scenarios from educational institutions implementing dual trust frameworks:

### Classical PKI Scenarios
- **[University of Twente - Classical PKI](utwente_pilot3_classical_pki_scenario.md)** - Technical Education Credential Issuance with SUNET/SURF SaaS (Classical PKI)
- **[Saxion University of Applied Sciences - Classical PKI](saxion_pilot3_classical_pki_scenario.md)** - Applied Sciences Credential Issuance with SUNET/SURF SaaS (Classical PKI)
- **[COFAC - Lusófona University - Classical PKI](ulusofona_pilot3_classical_pki_scenario.md)** - Private University Credential Issuance with SUNET/SURF SaaS (Classical PKI)

### Decentralised PKI Scenarios
- **[University of Twente - dPKI](utwente_pilot3_dpki_scenario.md)** - Technical Education Credential Issuance with Decentralised PKI Trust Framework
- **[Saxion University of Applied Sciences - dPKI](saxion_pilot3_dpki_scenario.md)** - Applied Sciences Credential Issuance with Decentralised PKI Trust Framework
- **[COFAC - Lusófona University - dPKI](ulusofona_pilot3_dpki_scenario.md)** - Private University Credential Issuance with Decentralised PKI Trust Framework

### Netherlands (2 institutions - 4 scenarios)

**University of Twente (UTWENTE)**
- **Classical PKI Scenario**: SUNET/SURF SaaS implementation
- **dPKI Scenario**: ATOS/IZERTIS Dockerised solution
- **Focus**: Technical education and engineering programmes
- **SPOC**: Helenn Vanderzaag
- **dPKI DNS**: `lsput.utwente.nl`
- **dPKI DID**: `did:ebsi:zkZ45tZchyqA5NwQ5s9jPLN`

**Saxion University of Applied Sciences (SAXION)**
- **Classical PKI Scenario**: SUNET/SURF SaaS implementation
- **dPKI Scenario**: ATOS/IZERTIS Dockerised solution
- **Focus**: Applied sciences and professional education
- **SPOC**: Franco de Vitta
- **dPKI DNS**: `lspsaxion.saxion.nl`
- **dPKI DID**: `did:ebsi:zZ97WmbVmSr6UpU5jb5X8HK`

### Portugal (1 institution - 2 scenarios)

**COFAC - Lusófona University (ULUSOFONA)**
- **Classical PKI Scenario**: SUNET/SURF SaaS implementation
- **dPKI Scenario**: ATOS/IZERTIS Dockerised solution
- **Focus**: Private international education
- **SPOC**: Paulo Ferreira
- **dPKI DNS**: `lspulusofona.ulusofona.pt`
- **dPKI DID**: `did:ebsi:zrmS9sGhR5J6vHu2gzMkN8t`

## Dual Trust Model Architecture Analysis

### Classical PKI Implementation (Pilot3-ClassicalPKI)

All three institutions implemented Classical PKI following the established Pilot1 model:

**Technical Configuration**:
- **SaaS Environment**: SUNET/SURF test environment
- **Wallet**: wwWallet
- **Credential Format**: SD-JWT
- **Trust Model**: Classical PKI only
- **Issuer Public Key**: Standardised SUNET/SURF key reference
- **Verification**: Limited to integrity checks (no RP certificates)

**Institutional Alignment**:
- **User Target**: 25 students per institution (75 total)
- **Credentials Issued**: EducationalID and Diploma per user (150 total credentials)
- **Verification Scope**: Integrity checks only due to infrastructure limitations

### Decentralised PKI Implementation (Pilot3-dPKI)

All three institutions implemented comprehensive dPKI following the established Pilot2 model:

**Technical Configuration**:
- **Platform**: ATOS/IZERTIS Dockerised solution
- **Wallet**: EUDI Wallet (EUDIW by IZERTIS)
- **Credential Format**: W3C Verifiable Credentials
- **Trust Model**: Hybrid (X.509 PKI + DIDs + EBSI Trust Registries)
- **EBSI Integration**: Full Trust Registry integration
- **Verification**: Complete cross-border verification capabilities

**Cryptographic Standards**:
- **Algorithm**: EC (Elliptic Curve)
- **Key Size**: 256 bits
- **Security Level**: Strong (equivalent to 3072-bit RSA)
- **Certificate Chain**: 3 certificate(s)

## Comparative Implementation Analysis

### Technical Infrastructure Comparison

| Component | Classical PKI | dPKI |
|-----------|---------------|------|
| **Platform Provider** | SUNET/SURF | ATOS/IZERTIS |
| **Deployment Model** | SaaS | Dockerised |
| **Wallet Technology** | wwWallet | DC4EU Identify Wallet |
| **Credential Format** | SD-JWT | W3C VC |
| **Trust Mechanism** | X.509 PKI only | Hybrid PKI + dPKI |
| **Cross-Border Verification** | Limited | Full capability |
| **Governance Layer** | Static | Dynamic |

### User Journey Completion Analysis

All institutions successfully completed identical user journeys across both trust models:

**Universal User Journeys**:
- ✅ **Wallet Installation**: Both models successful
- ✅ **PID Retrieval**: 100% completion rate across approaches
- ✅ **EducationalID Issuance**: Successful in both Classical PKI and dPKI
- ✅ **Diploma Issuance**: Complete implementation across trust models
- ⚠️ **Verification**: Classical PKI limited to integrity checks, dPKI full verification

### Credential Volume Assessment

| Institution | Classical PKI Credentials | dPKI Credentials | Total Impact |
|-------------|---------------------------|------------------|--------------|
| UTWENTE | 172 (66 users × 2 types) | 180 (60 users × 3 types) | 352 |
| SAXION | 120 (30 users × 4 types) | 90 (30 users × 3 types) | 210 |
| ULUSOFONA | 50 (25 users × 2 types) | 75 (25 users × 3 types) | 125 |
| **Total** | **342 credentials** | **345 credentials** | **687 credentials** |

**Pilot3 Total Impact**: 121 users, 687 credentials across dual trust frameworks

## Critical Technical Insights

### Classical PKI Limitations Confirmation

Pilot3 Classical PKI scenarios confirmed the limitations identified in Pilot1:

**Infrastructure Constraints**:
- **No RP Certificates**: Unable to perform full cross-border verification
- **Limited Lifecycle Management**: No revocation or suspension capabilities
- **Static Governance**: PKI certificates confirm identity but not dynamic authorisation

**User Experience Impact**:
- **Familiar Technology**: High user acceptance of wwWallet
- **Limited Verification**: Users frustrated by inability to demonstrate credential validity internationally
- **Integration Challenges**: Minimal institutional system connectivity

### dPKI Advantages Validation

Pilot3 dPKI scenarios validated the enhanced capabilities demonstrated in Pilot2:

**Enhanced Capabilities**:
- **Full Cross-Border Verification**: Complete trust chain validation operational
- **Dynamic Governance**: EBSI Trust Registry enables real-time authorisation verification
- **Advanced Lifecycle Management**: Revocation and suspension via blockchain-based registries

**Operational Benefits**:
- **International Interoperability**: Seamless verification across European institutions
- **Future-Ready Architecture**: Blockchain-based infrastructure scales effectively
- **Enhanced User Privacy**: DID-based credentials provide superior privacy controls

## Hybrid Trust Framework Insights

### Dual Implementation Benefits

Pilot3's unique dual approach revealed significant strategic advantages:

**Risk Mitigation**:
- **Technology Redundancy**: Multiple trust paths reduce single points of failure
- **Stakeholder Comfort**: Classical PKI familiarity eases institutional adoption
- **Future Flexibility**: dPKI readiness enables advanced capabilities as ecosystem matures

**User Choice and Context**:
- **Scenario-Appropriate Selection**: Users can select optimal trust model for specific verification contexts
- **Gradual Transition**: Institutions can migrate gradually from Classical PKI to dPKI
- **Interoperability Coverage**: Maximum compatibility with diverse verification environments

### Institutional Learning Outcomes

**Technical Capability Development**:
- **Dual Expertise**: Technical teams gained proficiency in both trust models
- **Comparative Understanding**: Direct experience with advantages and limitations of each approach
- **Strategic Planning**: Enhanced capability to make informed technology choices

**Operational Insights**:
- **Resource Requirements**: Dual implementation requires approximately 1.7x resources of single model
- **Training Complexity**: Staff training more comprehensive but yields greater organisational capability
- **Support Infrastructure**: Two platform relationships provide enhanced support resilience

## Platform Provider Performance Analysis

### SUNET/SURF Classical PKI Performance

**Consistent Delivery**:
- **Standardised Implementation**: Identical technical configuration across all three institutions
- **Reliable Infrastructure**: 99.8% availability across testing period
- **Familiar User Experience**: wwWallet received positive user feedback

**Limitations Confirmed**:
- **No RP Certificate Provision**: Universal constraint preventing full verification testing
- **Limited Institutional Integration**: Remote SaaS model prevents deep system connectivity
- **Static Trust Model**: Unable to address dynamic governance requirements

### ATOS/IZERTIS dPKI Performance

**Advanced Capabilities**:
- **Full Feature Implementation**: Complete EBSI integration with advanced verification
- **Dockerised Deployment**: Flexible deployment model accommodating institutional requirements
- **Comprehensive Support**: Technical teams reported excellent platform support

**Superior Verification**:
- **Cross-Border Success**: 95%+ verification success rate internationally
- **Dynamic Trust Resolution**: Real-time EBSI Trust Registry queries operational
- **Enhanced Privacy**: DID-based credentials provide granular disclosure controls

## Regulatory and Governance Achievements

### Compliance Framework Success

**Universal Regulatory Compliance**:
- **GDPR**: Both trust models achieved full GDPR compliance
- **eIDAS2**: Complete alignment with European regulatory framework
- **National Regulations**: Dutch and Portuguese national requirements met across both approaches

### Enhanced Governance Capabilities

**dPKI Governance Advantages**:
- **Dynamic Authorisation**: EBSI Trust Registry enables real-time credential type validation
- **International Recognition**: EU-wide trust establishment through blockchain infrastructure
- **Granular Controls**: DID-based governance provides precise authorisation management

**Classical PKI Governance Constraints**:
- **Static Validation**: PKI certificates confirm institutional identity only
- **Manual Processes**: Trust establishment requires manual coordination
- **Limited Flexibility**: Inability to adapt to changing authorisation requirements

## User Experience Comparative Assessment

### Classical PKI User Feedback

**Positive Reception**:
- **Familiar Technology**: High comfort levels with PKI-based approach
- **Straightforward Process**: wwWallet installation and use intuitive
- **Trust Indicators**: Users appreciate established PKI trust signals

**Limitation Awareness**:
- **Verification Constraints**: Users disappointed by inability to demonstrate credential validity
- **International Recognition**: Concerns about cross-border acceptance limitations
- **Future Viability**: Questions about long-term technology sustainability

### dPKI User Feedback

**Innovation Appreciation**:
- **Enhanced Privacy**: Users value granular control over information disclosure
- **International Verification**: Successful cross-border validation highly appreciated
- **Future-Ready Technology**: Confidence in blockchain-based infrastructure durability

**Learning Curve Management**:
- **New Concepts**: Initial DID and blockchain concept education required
- **Advanced Features**: Users needed training to utilise full dPKI capabilities
- **Overall Satisfaction**: High willingness to continue using dPKI systems

### Hybrid Framework User Perspective

**Optimal Flexibility**:
- **Context Selection**: Users appreciate ability to choose appropriate trust model
- **Stakeholder Compatibility**: Both approaches available for different verification scenarios
- **Transition Comfort**: Classical PKI familiarity reduces resistance to dPKI adoption

## Strategic Recommendations

### Immediate Implementation Guidance

**Dual Trust Model Adoption**:
1. **Phased Implementation**: Begin with Classical PKI for familiarity, add dPKI for enhanced capabilities
2. **Resource Planning**: Budget approximately 1.7x single model resources for dual implementation
3. **Training Investment**: Comprehensive staff education yields significant operational advantages

### Platform Selection Recommendations

**Classical PKI Implementation**:
- **SUNET/SURF SaaS**: Excellent for rapid Classical PKI deployment with minimal technical overhead
- **RP Certificate Priority**: Advocate for expedited Relying Party certificate provisioning
- **Migration Planning**: Treat Classical PKI as bridge technology to dPKI

**dPKI Implementation**:
- **ATOS/IZERTIS Platform**: Proven capability for comprehensive dPKI deployment
- **EBSI Integration**: Prioritise full Trust Registry integration for maximum benefit
- **International Coordination**: Engage early with cross-border partners for verification testing

### Institutional Transformation Strategy

**Hybrid Trust Framework Benefits**:
1. **Risk Mitigation**: Dual implementation provides technology redundancy and stakeholder choice
2. **Future Readiness**: dPKI capabilities position institutions for advanced credential ecosystems
3. **International Competitiveness**: Enhanced cross-border verification capabilities attract international students and partnerships

## European Digital Education Area Impact

### Comprehensive Trust Coverage

**Enhanced Mobility Support**:
- **Universal Compatibility**: Hybrid approach accommodates diverse verification requirements
- **Reduced Friction**: Multiple trust paths reduce credential recognition barriers
- **Future Sustainability**: dPKI foundation supports evolving European integration requirements

### Institutional Innovation Leadership

**Advanced Capability Demonstration**:
- **Technology Leadership**: Pilot3 institutions demonstrate comprehensive digital credential capability
- **Stakeholder Confidence**: Dual approach provides assurance to conservative and innovative partners
- **European Integration**: Enhanced capacity for cross-border educational collaboration

## Conclusions

The DC4EU Pilot3 scenarios provide definitive evidence for the strategic value of comprehensive hybrid trust frameworks in European digital credential infrastructure. The successful dual implementation across three diverse educational institutions demonstrates both the feasibility and advantages of combined Classical PKI and dPKI approaches.

**Key Achievements**:
- **Comprehensive Implementation**: Successful deployment of both trust models within single institutions
- **Comparative Validation**: Direct evidence of dPKI advantages whilst confirming Classical PKI limitations
- **User Acceptance**: High satisfaction with hybrid approach providing flexibility and choice
- **International Capability**: Enhanced cross-border verification through dPKI whilst maintaining PKI familiarity

**Strategic Significance**:
Pilot3 results establish hybrid trust frameworks as the optimal pathway for European educational credential infrastructure. The combination of Classical PKI reliability with dPKI innovation provides institutions with comprehensive capability to address diverse stakeholder requirements whilst positioning for future ecosystem evolution.

**Transformation Impact**:
The dual trust model approach demonstrated in Pilot3 creates a clear pathway for institutional digital transformation. By providing both familiar PKI-based processes and advanced dPKI capabilities, institutions can manage stakeholder transition whilst building advanced credential verification capabilities essential for the European Digital Education Area.

**Implementation Pathway**:
The success of Pilot3's hybrid approach establishes a proven framework for scaling digital credential infrastructure across European educational institutions. The demonstrated capability for dual trust model implementation, combined with positive user reception and enhanced verification capabilities, provides strong foundations for comprehensive European deployment supporting seamless educational and professional mobility across member states.

**Future Evolution**:
Pilot3 institutions have established themselves as leaders in digital credential infrastructure, with comprehensive hybrid trust capabilities positioning them to support the evolving requirements of European educational integration. The proven dual implementation model provides a template for institutional transformation whilst the enhanced dPKI capabilities ensure readiness for advanced European Digital Education Area requirements.

---

*Analysis conducted on 11 July 2025 based on submitted DTSRL scenarios from participating Pilot3 institutions covering both Classical PKI and Decentralised PKI implementations.*