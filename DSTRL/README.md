# DC4EU Deployment and Testing Scenarios Results Library (DTSRL)

## Overview

The **Deployment and Testing Scenarios Results Library (DTSRL)** is a comprehensive repository that documents real-world implementation scenarios for digital credentials in the European educational and professional qualifications ecosystem. As part of the **DC4EU (Digital Credentials for Europe)** Large Scale Pilot under the eIDAS 2.0 framework, the DTSRL serves as the central knowledge base for piloting agents implementing verifiable digital credentials across European institutions.

## What is the DTSRL?

The DTSRL is a structured collection of **validated deployment scenarios** that demonstrates how educational and professional institutions across Europe successfully implement digital credential systems using both **Classical PKI** and **Decentralised PKI** trust models. It provides practical guidance, tested user journeys, and proven implementation patterns for widespread adoption of the **EUDI Wallet ecosystem**.

### Key Characteristics

- **Operational Unit**: Each scenario serves as the complete implementation framework for piloting agents
- **Cross-Border Focus**: Scenarios designed for interoperability across EU Member States
- **Multi-Pilot Architecture**: Supports both Pilot 1 (Classical PKI + SD-JWT-VC) and Pilot 2 (Combined Classical PKI + Decentralised PKI - dPKI using EBSI + W3C VC + W3C-VCDM )
- **Compliance Framework**: Aligned with eIDAS 2.0 regulation and EBSI standards
- **Real-World Validation**: Based on actual implementations by participating institutions

## Core Components

### **Scenario Definitions**
Complete structured definitions provided by piloting agents, including:
- Target user journeys (students, professionals, administrative staff)
- Electronic Attestations of Attributes (EAAs) specifications
- Technical component configurations (issuer, verifier, wallet services)
- Governance setup (DIDs, authorisations, trust registrations)
- Monitoring and KPI frameworks

### **User Journey Documentation**
Detailed step-by-step processes covering:
- **DC4EU-001**: Person Identification Data (PID) retrieval
- **DC4EU-002**: Verifiable Educational/Professional ID issuance
- **DC4EU-003**: Education/Professional achievement credentials
- **DC4EU-004**: Cross-border EAA verification

### **Technical Implementation Guides**
Architecture-specific toolkits and components:

#### Pilot 1 (Classical PKI + SD-JWT)
- Traditional Certificate Authority trust chains
- SD-JWT credential format
- Established PKI infrastructure compatibility

#### Pilot 2 (Decentralised PKI + W3C VC)
- EBSI blockchain-based trust
- W3C Verifiable Credentials standard
- Combined classical and decentralised trust models

### **Cross-Border Verification Services**
Public DNS endpoints for credential verification across participating countries:
- **20+ institutions** across Europe
- **Real-time verification endpoints**
- **Multi-language support**
- **Compliance validation**

## Piloting Agent Structure

The DTSRL organises implementation through a structured approach:

### Single Point of Contact (SPOC) Framework
- **5 implementation phases** with clear milestones
- **Progress tracking** through standardised checklists
- **Quality assurance** and validation processes
- **Technical support** and guidance

### Institutional Coverage
Currently includes piloting agents from:
- **Denmark**: DTU, Danish educational institutions
- **Finland**: OPH (Finnish National Agency for Education)
- **Germany**: GovPart, LMU München, Humboldt University
- **Hungary**: Edutus University, BME
- **Italy**: University of Bologna
- **Lithuania**: Vytautas Magnus University, SKS
- **Netherlands**: University of Twente, Saxion, SURF
- **Poland**: University of Warsaw, University of Silesia, and 4 additional institutions
- **Portugal**: University of Porto, COFAC Lusofona
- **Romania**: UPT, UEFISCDI
- **Spain**: UAH, University of Málaga, UC3M, URV, CGCOM, UPM
- **Sweden**: RISE, Skolverket consortium

## Documentation Framework

### Scenario Checklist Template
```markdown
| Element                     | Description                           |
|-----------------------------|---------------------------------------|
| Scenario name               | Unique identifier                     |
| Piloting agent              | Responsible institution               |
| User journey(s) covered     | Specific implementation scope         |
| User types                  | Target stakeholder groups             |
| EAAs involved               | Credential types                      |
| Governance setup            | Trust and authorisation framework     |
| Technical components        | Infrastructure and service stack      |
| Institutional systems       | Connected databases and systems       |
| Feedback & monitoring       | Quality assurance mechanisms          |
| SPOC contact                | Assigned support and validation       |
```

### Progress Tracking
- **PA-checklist.md**: Self-assessment by piloting agents
- **SPOC-checklist.md**: Validation and support tracking
- **KPI Dashboard**: Real-time operational indicators
- **Cross-border verification status**: Live endpoint monitoring

## Benefits for the Digital Credentials Ecosystem

### For Educational Institutions
- **Streamlined Implementation**: Proven deployment patterns reduce risk and development time
- **Cross-Border Mobility**: Enable seamless student and professional mobility across Europe
- **Compliance Assurance**: Built-in adherence to eIDAS 2.0 and GDPR requirements
- **Future-Ready Infrastructure**: Alignment with emerging EUDI Wallet standards

### For Students and Professionals
- **Portable Credentials**: Verifiable qualifications that work across all EU Member States
- **Privacy Control**: Self-sovereign identity with selective disclosure capabilities
- **Reduced Bureaucracy**: Automated verification reduces administrative overhead
- **Lifetime Learning Records**: Comprehensive credential portfolio management

### For Verifiers and Employers
- **Instant Verification**: Real-time credential validation across borders
- **Trust Assurance**: Cryptographically secure and governance-compliant credentials
- **Integration Ready**: Standard APIs and protocols for system integration
- **Cost Efficiency**: Reduced manual verification processes

## Repository Structure

```
/DTSRL/
├── scenarios/
│   ├── pilot1/                    # Classical PKI implementations
│   ├── pilot2/                    # Decentralised PKI implementations
│   └── pilot3/                    # Combined pilot approaches
├── user-journeys/
│   ├── dc4eu-001-pid.md          # PID retrieval process
│   ├── dc4eu-002-educational-id.md # Educational ID issuance
│   ├── dc4eu-003-achievements.md  # Achievement credentials
│   └── dc4eu-004-verification.md  # Cross-border verification
├── technical/
│   ├── governance-templates/      # Trust framework configurations
│   ├── integration-guides/        # Technical implementation guides
│   └── api-specifications/        # Service interface documentation
├── monitoring/
│   ├── kpi-dashboard/            # Performance indicators
│   ├── feedback-forms/           # User experience collection
│   └── verification-endpoints/    # Live service monitoring
└── legal/
    ├── gdpr-templates/           # Privacy compliance documents
    ├── eidas-alignment/          # Regulatory compliance guides
    └── cross-border-agreements/  # International cooperation frameworks
```

## Getting Started

### For New Piloting Agents
1. **Review Scenario Templates**: Understand the complete implementation framework
2. **Select Pilot Track**: Choose between Pilot 1, Pilot 2, or combined approach
3. **Define User Journeys**: Map specific institutional needs to standard patterns
4. **Contact SPOC**: Engage with assigned Single Point of Contact for guidance
5. **Implement & Test**: Deploy using provided toolkits and validation frameworks

### For Integration Partners
1. **Explore Technical Documentation**: Review API specifications and integration guides
2. **Access Verification Endpoints**: Test cross-border verification capabilities
3. **Implement Trust Framework**: Configure governance and authorisation templates
4. **Join Monitoring Network**: Participate in KPI tracking and feedback collection

## Quality Assurance

The DTSRL maintains high standards through:
- **Peer Review Process**: All scenarios validated by technical experts
- **Interoperability Testing**: Cross-border verification testing between institutions
- **User Experience Validation**: Feedback collection from real end-users
- **Regulatory Compliance**: Legal review for eIDAS 2.0 and GDPR alignment
- **Continuous Monitoring**: Real-time service availability and performance tracking

## Future Developments

The DTSRL evolves to support:
- **Extended Pilot Coverage**: Additional institutions and countries
- **Enhanced Interoperability**: Integration with other European digital identity initiatives
- **Advanced Use Cases**: Professional qualifications, micro-credentials, and lifelong learning
- **Production Readiness**: Transition from pilot to operational deployment
- **Standards Contribution**: Input to European and international standardisation efforts

## Contact and Support

**DC4EU DTSRL Team**  
📧 Email: [dtsrl-support@dc4eu.eu](mailto:lluisalfons.arino@urv.cat)  
🌐 Website: [dc4eu.eu/dtsrl](https://www.dc4eu.eu/wp5/dtsrl)  
📚 Documentation: [docs.dc4eu.eu](https://www.dc4eu.eu/wp5)  

**Technical Support**  
For implementation guidance and technical assistance, contact your assigned SPOC or reach out to the coordination team.

**Contribution**  
The DTSRL welcomes contributions from piloting agents, technical partners, and the broader digital credentials community. Please follow our contribution guidelines and review processes.

---

> **Note**: This library represents a collaborative effort by the DC4EU consortium and participating European institutions to accelerate the adoption of interoperable digital credentials in education and professional qualifications. All scenarios are validated through real-world implementations and compliance testing.

*Last Updated: June 2025 | Version: 2.0 | Status: Active Development*