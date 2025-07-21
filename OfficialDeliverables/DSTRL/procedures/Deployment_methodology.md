# DC4EU WP5 User Journey Deployment Methodology

## Overview

The DC4EU (Digital Credentials for Europe) project developed a comprehensive methodology to ensure successful deployment of user journeys across multiple European institutions. This methodology was specifically designed to enable all Work Package 5 (WP5) partners acting as Piloting Agents to deliver digital credential services whilst meeting two primary objectives:

1. **Primary Objective**: Provide user journeys for issuing educational credentials and professional qualifications
2. **Secondary Objective**: Provide cross-border verification services

## Methodology Framework

### Core Principle: Single Point of Contact (SPOC) Model

The methodology centres around a **Single Point of Contact (SPOC)** model that serves as the central organisational and technical hub for institutions managing educational and professional qualifications. The SPOC acts as the national coordinator, ensuring alignment with WP5 methodology, technical standards, and governance procedures.

### Key Success Factors

The methodology was designed with several critical success factors:

- **Structured coordination** across multiple countries and institutions
- **Standardised technical components** whilst allowing local adaptation
- **Governance compliance** with European digital identity frameworks
- **Risk mitigation** through phased implementation
- **Continuous monitoring** and feedback mechanisms

## Actors and Roles

### 1. Single Points of Contact (SPOCs)

**Role**: National/Regional Coordinators

**Key Responsibilities**:
- Monitor and document progress of piloting agents across all required phases
- Collect and validate evidence demonstrating completion of technical, organisational, and governance tasks
- Act as primary contact point for piloting agents seeking clarification or facing issues
- Ensure timely and structured reporting aligned with project KPIs

**SPOC Distribution by Pilot Type**:

#### Pilot 1 (Classical PKI):
- SUNET (Sweden)
- Sikt - Norwegian Agency for Shared Services in Education and Research (Norway)
- SURF (Netherlands)
- Finnish National Agency for Education - OPH (Finland)
- DTU (Denmark)

#### Pilot 2 (Decentralised PKI - EBSI + Classical PKI):
- Walt.ID (Belgium)
- SGAD & CGCOM (Spain)
- Universidade do Porto (Portugal)
- GovPart GmbH (Germany)
- Politechnica University of Timișoara (Romania)
- OPI PIB (Poland)
- RISE (Sweden)
- eDelivery (Lithuania)
- SURF (Netherlands)

### 2. Piloting Agents (PAs)

**Role**: User Journey Providers and Credential Issuers/Verifiers

**Key Responsibilities**:
- Onboard users and deliver user journeys
- Issue and verify digital credentials
- Collect user feedback and operational data
- Report progress to their assigned SPOC

**Team Structure within Piloting Agents**:
- **Project Manager**: Oversees execution and ensures regulatory compliance
- **Educational/Professional Content Specialist**: Designs user journeys and manages end-user processes
- **Technical Lead**: Manages system integration and infrastructure
- **User Support**: Handles inquiries and gathers feedback

### 3. End Users

**Role**: Credential Holders and Service Recipients

**Types**:
- Students receiving educational credentials
- Professionals obtaining qualifications
- Administrative staff managing credential processes

### 4. WP5 Partners

**Role**: Framework Providers and Monitors

**Responsibilities**:
- Provide methodology and technical frameworks
- Monitor overall progress across all piloting agents
- Collect evidence and consolidate reporting
- Facilitate continuous improvement

### 5. Tool Providers

**Role**: Technical Infrastructure Supporters

**Key Providers by Pilot**:

**Pilot 1**:
- SUNET: Issuer/Verifier platforms and basic user journey provisioning
- GUNet: Natural person wallets

**Pilot 2**:
- ATOS: Issuer/Verifier platforms and basic user journey provisioning
- IZERTIS: Natural person wallets
- GovPart & SGAD: Governance and trust framework management

## Conceptual Map of Actor Interactions

The methodology is built around a clear interaction model between key actors, each with defined responsibilities and communication pathways:

### Core Interaction Flow

The **SPOC (Single Point of Contact)** serves as the central coordination hub, facilitating interactions between:

- **WP5 Partners** → **SPOCs**: Define common rules, architecture, and standards
- **SPOCs** → **Piloting Agents**: Coordinate national/sectoral implementation, validate governance, and monitor deployment
- **Piloting Agents** → **End Users**: Implement user journeys, engage with users, and issue credentials
- **Technical Partners** → **Piloting Agents**: Provide technical support (issuer SDKs, wallet apps, verifier platforms)
- **End Users** → **System**: Interact with wallets and participate in credential issuance and verification
- **All Actors** → **Reporting System**: Provide feedback, progress updates, and performance data

### Key Interaction Patterns

1. **Hierarchical Coordination**: WP5 → SPOC → Piloting Agents ensures consistent methodology application whilst allowing national/institutional flexibility

2. **Technical Support Network**: Specialised technical partners provide infrastructure and tools, with SPOCs facilitating access and issue resolution

3. **Feedback Loops**: Multi-directional communication ensures continuous improvement through user experience data, technical performance metrics, and governance compliance reporting

4. **Cross-Border Verification**: Piloting Agents provide public endpoints enabling verification of credentials issued by institutions in other member states

This interaction model ensures that local execution aligns with European-level coordination whilst maintaining clear accountability and support structures.

### Visual Representation
``` mermaid
graph TB
    %% Core Actors
    WP5[WP5 Partners<br/>Framework Providers]
    SPOC[SPOCs<br/>National Coordinators]
    PA[Piloting Agents<br/>User Journey Providers]
    EU[End Users<br/>Students & Professionals]
    TP[Tool Providers<br/>Technical Infrastructure]
    REP[Reporting System<br/>KPI & Evidence Collection]

    %% Primary coordination flows
    WP5 -->|Define methodology<br/>& standards| SPOC
    SPOC -->|Coordinate & validate<br/>governance| PA
    PA -->|Deploy user journeys<br/>& issue credentials| EU
    
    %% Technical support flows
    TP -->|Provide issuer/verifier<br/>platforms & wallets| PA
    TP -.->|Technical guidance<br/>via SPOC| PA
    
    %% Feedback and reporting flows
    PA -->|Progress reports<br/>& evidence| SPOC
    SPOC -->|Consolidated reporting<br/>& KPIs| WP5
    EU -->|User feedback<br/>& satisfaction| PA
    PA -->|Operational data<br/>& metrics| REP
    SPOC -->|Monitoring data<br/>& validations| REP
    
    %% Cross-border verification
    PA -.->|Cross-border<br/>verification endpoints| PA
    
    %% Issue escalation
    PA -.->|Technical issues<br/>& support requests| SPOC
    SPOC -.->|Complex issues<br/>& improvements| WP5
    
    %% Styling
    classDef primary fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef secondary fill:#f3e5f5,stroke:#4a148c,stroke-width:2px
    classDef support fill:#e8f5e8,stroke:#1b5e20,stroke-width:2px
    
    class WP5,SPOC,PA primary
    class EU,REP secondary
    class TP support
``` 

## Implementation Methodology

### Five-Phase Approach

The methodology follows a structured five-phase approach to ensure consistency, comparability, and readiness:

#### Phase 1: Preparation
**Objective**: Understanding and Planning

**Key Actions**:
- Understand SPOC role and governance requirements
- Identify piloting agents within national/institutional scope
- Register governance data and DID information
- Assess infrastructure requirements
- Establish communication channels with assigned SPOC

#### Phase 2: Readiness
**Objective**: Technical and Organisational Setup

**Key Actions**:
- Deploy issuer and verifier platforms
- Set up digital wallets for end users
- Test technical flows and integration points
- Complete readiness checklist validation
- Register in trust frameworks (Classical PKI or DID-based)
- Develop training materials

#### Phase 3: Controlled Pilot
**Objective**: Testing and Refinement

**Key Actions**:
- Simulate selected user journeys with real users
- Collect evidence and identify technical/process gaps
- Execute first user journeys in controlled environment
- Implement real-time monitoring and issue resolution
- Provide weekly reporting to SPOC

#### Phase 4: Full Rollout
**Objective**: Scaling and Institutional Adoption

**Key Actions**:
- Extend participation to larger user groups
- Implement credential lifecycle management
- Establish ongoing performance tracking
- Ensure regulatory validation and compliance
- Deploy comprehensive support mechanisms

#### Phase 5: Continuous Monitoring
**Objective**: Maintenance and Optimisation

**Key Actions**:
- Track weekly KPIs and performance metrics
- Report incidents and user feedback systematically
- Align outputs with broader WP3 objectives
- Propose and implement continuous improvements
- Maintain long-term operational capability

### Technical Infrastructure Framework

The methodology defines standardised technical components whilst allowing for local adaptation:

#### Common Elements (Both Pilots):
- Governance templates for credential registration
- Feedback collection systems
- KPI monitoring dashboards
- User onboarding procedures

#### Pilot-Specific Components:

**Pilot 1 (Classical PKI)**:
- X.509v3 PKI certificates for issuers
- PKI-based trust validation
- SD-JWT credential format
- Classical certificate revocation lists (CRL)

**Pilot 2 (Decentralised PKI + Classical PKI)**:
- DID-based trust discovery
- EBSI-compatible governance documentation
- Verifiable credentials in W3C format
- Combined trust model implementation

### Governance and Compliance Framework

#### Trust Framework Integration
- **Pilot 1**: Integration with classical PKI infrastructure including X.509 certificates
- **Pilot 2**: Integration with decentralised identity systems and EBSI infrastructure
- **Pilot 3**: Combined approach utilising both classical and decentralised trust models

#### Compliance Requirements
- GDPR compliance for data protection
- eIDAS2 regulation alignment
- National higher education regulations
- European interoperability standards

### Quality Assurance and Risk Management

#### Risk Categories and Mitigation:
1. **Technical Risks**: Integration issues, security vulnerabilities
   - Mitigation: Phased testing, technical validation checkpoints

2. **Operational Risks**: Resource constraints, training gaps
   - Mitigation: Structured training programmes, SPOC support

3. **Compliance Risks**: GDPR breaches, credential validity issues
   - Mitigation: Governance validation, regular compliance reviews

#### Success Metrics and KPIs:
- Number of institutions successfully deploying user journeys
- Credential issuance and verification success rates
- User satisfaction scores
- Cross-border verification capability demonstration
- System uptime and reliability metrics

## User Journey Categories

The methodology defines standardised user journey categories that all piloting agents must implement:

### Core User Journeys:
1. **Wallet Setup and User Onboarding**
2. **Personal Identification (PID) Retrieval**
3. **Credential Issuance (Academic & Professional)**
4. **Quality Assurance Attestation Issuance**
5. **Credential Verification by Third Parties**
6. **Credential Lifecycle Management**
7. **Support and Issue Resolution**

### Cross-Border Verification Requirement:
Each piloting agent must demonstrate cross-border verification capability by providing public endpoints that can verify credentials issued by institutions in other member states.

## Monitoring and Reporting Framework

### Structured Reporting Mechanism:
- **Weekly Progress Reports** from Piloting Agents to SPOCs
- **Evidence Collection** and validation against requirements
- **Issue Escalation** procedures for technical and governance challenges
- **KPI Alignment Monitoring** to ensure contribution to project objectives

### Key Performance Indicators:
- 10 wallet issuing countries involved
- 1,000 wallet users across WP5
- 25 education domain institutions interfacing with wallets
- 5,000 wallet transactions in pre-production environment
- Cross-border verification demonstrations

## Success Outcomes

This methodology successfully enabled:

### Technical Achievements:
- Deployment of interoperable digital credential infrastructure across multiple European countries
- Demonstration of both classical PKI and decentralised identity approaches
- Cross-border verification capability between different national systems

### Organisational Achievements:
- Coordinated implementation across diverse educational and professional institutions
- Standardised governance frameworks whilst respecting national sovereignty
- Effective knowledge transfer and capacity building

### Strategic Achievements:
- Practical validation of European digital identity infrastructure
- Evidence base for scaling digital credentials across the EU
- Foundation for future European Digital Identity Wallet deployment

## Conclusion

The DC4EU WP5 user journey deployment methodology represents a comprehensive approach to coordinating complex, multi-national digital infrastructure deployment. By combining structured project management, technical standardisation, and flexible local adaptation, the methodology successfully enabled diverse European institutions to collaborate in creating an interoperable digital credentials ecosystem.

The SPOC model proved particularly effective in balancing central coordination with national autonomy, whilst the five-phase implementation approach ensured systematic readiness and risk mitigation. The methodology's emphasis on continuous monitoring, feedback collection, and iterative improvement established a foundation for sustainable operations and future expansion.

This methodology serves as a replicable framework for similar large-scale European digital infrastructure initiatives, demonstrating how careful coordination, clear governance, and structured implementation can achieve ambitious interoperability objectives across diverse national contexts.