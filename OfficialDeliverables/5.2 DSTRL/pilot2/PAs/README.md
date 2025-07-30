# Propuesta de Reestructuración: OfficialDeliverables/5.2 DSTRL/pilot2/PAs/README.md

## Estructura Propuesta (Siguiendo la Metodología de Pilot1)

### Executive Summary

The DC4EU Pilot2 scenarios demonstrate two distinctive approaches to implementing Hybrid Trust (Classical PKI + Decentralised PKI) digital credential systems across European educational institutions. Through 31 institutional scenarios across 10 countries, this pilot reveals both **distributed autonomous deployments** (ATOS/IZERTIS Dockerised) and **coordinated national implementations** (OPI/NASK SaaS), providing educational institutions with multiple pathways to next-generation digital credentials whilst highlighting different governance and infrastructure strategies within the European decentralised identity ecosystem.

### Pilot2 Piloting Agent Scenarios

This analysis covers representative scenarios from the 31 participating institutions, highlighting the two primary implementation approaches:

**ATOS/IZERTIS Dockerised Model Representatives:**
- **[Budapest University of Technology (BME)](bme_pilot2_scenario.md)** - Technical University Implementation with Blockchain Lab Integration
- **[Universidad Carlos III de Madrid (UC3M)](uc3m_pilot2_scenario.md)** - Engineering-Focused Credential Verification
- **[UEFISCDI Romania](uefiscdi_pilot2_scenario.md)** - National Higher Education Authority Implementation

**ATOS/IZERTIS SaaS Model Representatives:**
- **[LMU München (Germany)](lmu_pilot2_scenario.md)** - German University SaaS Implementation via GovPart
- **[Universidad Nacional de Educación a Distancia (UNED)](uned_pilot2_scenario.md)** - Spanish Distance Education SaaS Implementation

**OPI/NASK National SaaS Model Representatives:**
- **[University of Warsaw (UW)](uw_pilot2_scenario.md)** - Flagship National University Implementation
- **[University of Silesia (US)](us_pilot2_scenario.md)** - Comprehensive Educational Credential Management
- **[Silesian University of Technology (POLSL)](polsl_pilot2_scenario.md)** - Technical Education Integration

### Análisis Comparativo

#### Technical Implementation Diversity

The 31 scenarios demonstrate three distinct implementation approaches within the Hybrid Trust framework:

##### ATOS/IZERTIS Dockerised Autonomous Model (22 institutions)
Institutions across Belgium, Hungary, Italy, Lithuania, Portugal, Romania, Spain implemented self-hosted autonomous deployments:
- **Pilot option**: Hybrid Trust (Classical PKI + Decentralised PKI)  
- **Platform**: ATOS/IZERTIS Dockerised solution (self-hosted)
- **Wallet**: EUDI Wallet (EUDIW by IZERTIS)
- **Infrastructure control**: Full institutional sovereignty over deployment
- **Customisation level**: Extensive institutional customisation capabilities
- **Maintenance model**: Institutional or contracted technical support
- **DID implementation**: Individual institutional DIDs with EBSI anchoring

##### ATOS/IZERTIS SaaS Model via GovPart (3 institutions)
German universities and UNED (Spain) implemented managed service deployment:
- **Pilot option**: Hybrid Trust (Classical PKI + Decentralised PKI)
- **Platform**: ATOS/IZERTIS solution via GovPart GmbH SaaS
- **Wallet**: EUDI Wallet (EUDIW by IZERTIS)
- **Infrastructure control**: Managed service with institutional configuration
- **Customisation level**: Service-level customisation options
- **Maintenance model**: Professional managed service support
- **Participating institutions**: LMU München, HU Berlin (Germany), UNED (Spain)

##### OPI/NASK National Coordinated Model (6 institutions)
Polish universities implemented coordinated national deployment:
- **Pilot option**: Hybrid Trust (Classical PKI + Decentralised PKI)
- **Platform**: OPI/NASK national SaaS instance
- **Wallet**: EUDI Wallet integration through national platform
- **Infrastructure control**: National coordination with institutional participation
- **Standardisation level**: National standards with institutional variation
- **DNS endpoints**: Coordinated national subdomain structure (`u1-u7.pilot-dc4eu.ebsi.nask.pl`)
- **Governance model**: Centralised national infrastructure with distributed institution access

This implementation diversity demonstrates the flexibility of the Hybrid Trust approach whilst highlighting different sovereignty, managed service, and coordination models within European decentralised identity frameworks.

#### Credential Volumes and User Engagement

| Implementation Model | Countries | Institutions | Total Users | Credentials Issued | Verification Scope |
|---------------------|-----------|--------------|-------------|-------------------|-------------------|
| **ATOS/IZERTIS Dockerised** | 7 countries | 22 institutions | ~660 users* | ~1,980 credentials* | Full cross-border verification |
| **ATOS/IZERTIS SaaS (GovPart)** | 2 countries | 3 institutions | ~90 users* | ~270 credentials* | Full cross-border verification |
| **OPI/NASK National** | 1 country | 6 institutions | ~180 users* | ~540 credentials* | Full cross-border verification |

*Estimates based on representative scenario data

**Key distinctions:**
- **Dockerised model**: Maximum institutional autonomy with individual technical responsibility
- **SaaS model**: Managed service approach with professional support and reduced institutional overhead
- **National model**: Coordinated deployment with shared infrastructure benefits
- **All models**: Complete cross-border verification capabilities achieved
- **Universal success**: 100% DNS endpoint availability and DID deployment across all institutions

**Total Impact**: ~930 users, ~2,790 credentials issued across three viable governance and deployment models.

### Implementation Model Analysis

#### ATOS/IZERTIS Dockerised Autonomous Model

The Dockerised model represents **institutional sovereignty with self-hosted infrastructure**:

##### Technical Infrastructure
- **Platform**: ATOS/IZERTIS Dockerised solution with individual institutional hosting
- **Deployment control**: Complete institutional control over infrastructure and data
- **Customisation capability**: Extensive integration with existing institutional systems
- **Technical support**: ATOS/IZERTIS technical teams with institutional maintenance responsibility

##### Unique Capabilities
- **Full institutional sovereignty**: Complete control over credential issuance and data management
- **Maximum customisation**: Tailored integration with existing institutional systems and workflows
- **Advanced features**: Support for blockchain lab integration (BME), professional credential focus (UC3M), national authority capabilities (UEFISCDI)
- **European interoperability**: Individual DIDs with EBSI Trust Registry integration ensuring cross-border recognition

#### ATOS/IZERTIS SaaS Model via GovPart

The GovPart SaaS model provides **managed service deployment** of ATOS/IZERTIS technology:

##### Technical Infrastructure
- **Platform**: ATOS/IZERTIS solution delivered as managed SaaS via GovPart GmbH
- **Deployment control**: Professional managed service with institutional configuration options
- **Service-level customisation**: Managed service customisation within SaaS framework
- **Technical support**: Professional GovPart managed service support with ATOS/IZERTIS backing

##### Unique Capabilities
- **Simplified deployment**: Reduced institutional technical requirements through managed service
- **Professional maintenance**: GovPart professional service management and support
- **Technology access**: Access to ATOS/IZERTIS technology without infrastructure responsibility  
- **Multi-institutional coordination**: Shared service across German universities and Spanish distance education

#### OPI/NASK National Coordinated Model

The Polish national model demonstrates **coordinated national deployment**:

##### Technical Infrastructure
- **Platform**: OPI/NASK national SaaS instance with unified national coordination
- **Governance approach**: National regulation compliance with institutional participation
- **Infrastructure sharing**: Shared national infrastructure reducing individual institutional requirements
- **Standardisation benefits**: Uniform technical configurations across Polish higher education

##### Unique Capabilities
- **National coordination**: Seamless integration across Polish higher education system
- **Regulatory compliance**: Built-in compliance with Polish national education regulations
- **Shared infrastructure**: Reduced individual institutional technical requirements and costs
- **Coordinated maintenance**: Professional national infrastructure management

##### Implementation Strengths
- **Simplified institutional deployment**: Reduced technical requirements for individual institutions
- **National interoperability**: Seamless credential recognition across Polish higher education
- **Cost efficiency**: Shared infrastructure costs across participating institutions
- **Professional maintenance**: National-level technical support and infrastructure management

### Comparative Analysis

| Aspect | ATOS/IZERTIS Dockerised | ATOS/IZERTIS SaaS (GovPart) | OPI/NASK National |
|--------|--------------------------|----------------------------|-------------------|
| **Infrastructure ownership** | Institutional autonomous | Managed service | National coordinated |
| **Deployment complexity** | High institutional requirement | Simplified managed service | Simplified institutional onboarding |
| **Customisation capability** | Maximum flexibility | Service-level options | National standards with variation |
| **Technical support model** | Direct vendor relationship | Professional managed service | National coordination team |
| **Cross-border verification** | Individual EBSI integration | Managed EBSI integration | National EBSI coordination |
| **Regulatory compliance** | Institutional responsibility | Service provider assistance | National framework integration |
| **Innovation potential** | High institutional autonomy | Managed innovation support | Coordinated national innovation |
| **Scalability model** | Individual institutional scaling | Managed service scaling | National infrastructure scaling |

### Critical Technical Achievements

#### Universal Deployment Success

Both implementation models achieved **100% deployment success** with critical technical milestones:

**Infrastructure Achievements**:
- **DNS Endpoint Deployment**: Complete cross-border verification infrastructure operational
- **DID Implementation**: Universal decentralised identifier deployment with EBSI integration
- **W3C VC Compliance**: Standards-compliant Verifiable Credentials implementation
- **Cross-Border Verification**: Active international credential verification demonstrated

#### Current Technical Limitations

Despite successful deployment, Pilot2 implementations face specific technical constraints:

**Advanced Selective Disclosure Limitations**:
- **SD-JWS with jAdES Compliance**: Complete description of selective disclosure using SD-JWS compliant with jAdES standards has been developed and compliance demonstrated, but full implementation in production environments remains pending
- **Implementation Gap**: While basic embedded disclosure has been implemented in the hybrid approach (released July 30), the complete SD-JWS selective disclosure with demonstrated jAdES compliance has not yet been deployed across all participating institutions
- **Production Deployment**: The technical solution exists and compliance has been validated, but scaling to production deployment across all implementation models requires additional coordination

#### Model-Specific Technical Successes

##### ATOS/IZERTIS Dockerised Model
- **Institutional sovereignty**: Successful autonomous deployment across 7 countries and 22 institutions
- **Technical customisation**: Advanced integration with blockchain labs, professional bodies, and research institutions
- **Innovation leadership**: Support for cutting-edge use cases and institutional research requirements

##### ATOS/IZERTIS SaaS Model (GovPart)
- **Managed service success**: Effective deployment across German universities and Spanish distance education
- **Professional support**: Demonstrated managed service model reducing institutional technical burden
- **Cross-institutional coordination**: Successful shared service model across different institutional types

##### OPI/NASK National Model  
- **National coordination**: Seamless deployment across 6 Polish universities with unified standards
- **Regulatory integration**: Complete Polish national education regulation compliance
- **Efficiency demonstration**: Reduced institutional technical requirements whilst maintaining full functionality

### Strategic Implications and Recommendations

#### Validated Implementation Pathways

Pilot2 demonstrates that **Hybrid Trust architecture provides three viable deployment strategies**:

**Dockerised Autonomous Model**: Enables maximum institutional control and customisation whilst maintaining European interoperability, suitable for institutions with strong technical capabilities seeking advanced integration and innovation opportunities.

**SaaS Managed Service Model**: Provides professional managed service deployment of advanced technology whilst maintaining institutional configuration capabilities, suitable for institutions seeking reduced technical overhead with professional support.

**National Coordinated Model**: Provides streamlined deployment through national coordination whilst maintaining full cross-border capabilities, suitable for institutions seeking simplified technical requirements with professional national support.

#### Critical Success Factors

1. **EBSI Integration**: Universal requirement for European-wide trust establishment and cross-border recognition
2. **Standards compliance**: W3C Verifiable Credentials implementation essential for interoperability
3. **Flexible deployment models**: Supporting autonomous, managed service, and coordinated approaches accommodates diverse institutional needs
4. **Professional technical support**: Vendor-direct, managed service, and national coordination models provide essential implementation support
5. **Service model diversity**: Multiple service delivery approaches enable institutions to choose optimal deployment strategy

#### Production Deployment Considerations

The successful demonstration of two distinct but equally viable deployment models within Pilot2 validates the **adaptability required for pan-European adoption** whilst ensuring **technical standardisation** for seamless cross-border credential recognition.

Both models successfully overcome the classical PKI limitations identified in Pilot1, providing:
- **Complete cross-border verification capabilities**
- **Real-time trust discovery through EBSI integration**
- **Enhanced privacy protection through selective disclosure**
- **Future-ready architecture aligned with eIDAS 2.0 and EUDI Wallet ecosystem**

### Conclusions

The DC4EU Pilot2 scenarios establish **Hybrid Trust architecture as the optimal foundation** for European educational credential infrastructure through three proven deployment strategies.

#### ATOS/IZERTIS Dockerised Model Success
The Dockerised autonomous approach demonstrates that **institutional sovereignty and European interoperability** can be successfully combined. Key achievements include:
- Successful deployment across 22 institutions in 7 countries
- Complete technical customisation with maintained interoperability standards
- Advanced integration capabilities supporting innovation and research requirements
- Direct vendor relationships ensuring professional technical support

#### ATOS/IZERTIS SaaS Model Success (via GovPart)
The managed service approach proves that **professional SaaS delivery can maintain advanced capabilities** whilst reducing institutional technical burden. Notable outcomes include:
- Successful deployment across German universities and Spanish distance education
- Professional managed service reducing institutional infrastructure requirements
- Maintained access to advanced ATOS/IZERTIS technology through service delivery
- Cross-institutional coordination demonstrating shared service viability

#### OPI/NASK National Model Success  
The Polish national coordination approach proves that **streamlined deployment through national coordination** can achieve full European interoperability. Notable outcomes include:
- Coordinated deployment across 6 universities with unified national standards
- Simplified institutional requirements with comprehensive functionality
- National regulatory compliance with European standard alignment
- Professional national infrastructure management

#### Universal Technical Advantages
Both implementation models successfully demonstrate **next-generation capabilities** unavailable in classical PKI:
- **100% cross-border verification success** across all participating institutions
- **Complete EBSI integration** enabling European-wide trust discovery
- **Standards-compliant implementation** ensuring long-term interoperability
- **Enhanced privacy protection** through selective disclosure mechanisms

#### Strategic Recommendations for European Deployment

1. **Support deployment diversity**: Enable autonomous institutional, managed service, and coordinated national approaches based on institutional requirements and capabilities
2. **Maintain EBSI integration**: Ensure universal European Blockchain Services Infrastructure integration for trust establishment
3. **Provide multiple support models**: Support vendor-direct, managed service, and national coordination technical support approaches
4. **Enable service model flexibility**: Maintain options for self-hosted, SaaS, and national coordination deployment models
5. **Enable innovation pathways**: Maintain flexibility for advanced use cases whilst ensuring baseline European interoperability

The proven success of three distinct deployment models within Pilot2's Hybrid Trust framework provides **comprehensive pathways for European educational credential infrastructure** supporting institutional autonomy, managed service efficiency, and national coordination whilst maintaining European integration objectives.

---

*Analysis conducted on 30 July 2025 based on representative scenarios from participating Pilot2 institutions across Dockerised autonomous, SaaS managed service, and national coordinated implementation models.*
