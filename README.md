# Educational and Professional Qualifications Framework

## Overview

This repository provides comprehensive documentation and implementation guidance for the European Educational and Professional Qualifications digital credentials framework. It encompasses sectorial rulebooks, sectorial EAA catalogues, data models, implementation toolkits, and compliance information for creating interoperable systems that respect European values of privacy, institutional autonomy, and cross-border mobility for students and professionals.

## Repository Structure

This repository is organised into several key sections:

- **[Education and professional qualifications Business Bleuprint - BBP](./OfficialDeliverables/DC4EU_D5.1_WP5_Business%20Blueprint_v.2.0.pdf)**: The DC4EU WP5 Business Blueprint is a strategic document developed to guide the integration and adoption of digital credentials across the European Union, enhancing the digital transformation of education and professional qualifications. This blueprint aligns with the European Commission’s 2030 Digital Education Action Plan, focusing on interoperability, accessibility, quality assurance, sustainability, and stakeholder engagement

- **[eIDAS roles](./docs/eIDAS-roles.md)**: Outlines the key roles within the European digital identity framework under eIDAS, detailing their definitions, functions, types of attestations issued, regulatory references, and compliance requirements.
  
- [Trust models](./sectorial-rulebook/trust-models.md): Outlines trust models accepted for **Education and Professional qualifcations** (Classical PKI & Decentralised PKI using EBSI). 

- **[eIDAS scenarios](./eidas-scenarios/)**: Outlines the four trust models for electronic attestation of attributes (EAAs) within the European Digital Ecosystem, explaining how EBSI enhances traditional PKI approaches.

- [Bridge between Classical PKI and dPKI using EBSI](./eidas-scenarios/scenario2/trust_modes_bridge.md): How the trust models of classical PKI and dPKI are combined to enable and support the governance of education and professional qualifications
  
- **[Governance in Education and Professional Qualifications](./governances)**: Understanding existing governance(s)
  
- **[Governance implementation: the EAA-based authorisation model](./eaa-based-authorisation-model/)**: Defines a structured framework for education and professional qualifications' governance, managing authorisations and recognition within educational, professional, and quality assurance domains.

- **[Sectorial rulebook](./sectorial-rulebook/)**: The core framework that establishes standardised approaches for managing digital educational and professional credentials within the European Union.

- **[Sectorial EAA catalogue](./sectorial-eaa-catalogue/)**: Contains all data models and schemas agreed at sectorial level for Education and Professional Qualifications, including formal education, quality assurance regimes, and non-foundational ID.

- **[EAA Characterisation](./sectorial-eaa-catalogue/EAA_Characterisation.md)**: Characterisation of an Electronic Attestation of Attributes (EAA).

- **[Deployment and Testing Scenarios Results Library (DTSRL)](./DTSRL/)**: Comprehensive repository of validated deployment scenarios, user journeys, implementation toolkits, and piloting frameworks for digital credentials implementation across European institutions.
  
- **[Elements](./elements)**: Elements produced/provided by DC4EU to facilitate adoption. Includes data model converters, gateways, reports.

- **[Compliance](./compliance/)**: Information about EBSI and EUDI Wallet compliance tests to ensure interoperability with other issuer, verifier, and wallet solutions.

## DTSRL - Deployment and Testing Scenarios Results Library

The **[DTSRL](./DSTRL/README.md)** serves as the central knowledge base for implementing digital credentials in practice. It contains:

### Core DTSRL Components

- **[User journeys](./DSTRL/user-journeys/README.md)**: Provided user journeys to demonstrate cross-border interaction, ready-to-go infrastructure, and foundation to extend/provide more user journeys and/or EAAs.
  
- **[Scenarios](./DSTRL/scenarios/README.md)**: Complete scenario definitions that detail the elements each piloting agent must provide to characterise, execute, and monitor user journeys in alignment with governance, technical, and reporting requirements.

- **[Piloting](./DSTRL/piloting/README.md)**: Operational framework for piloting agents including progress tracking, SPOC coordination, and implementation validation across the DC4EU Large Scale Pilot.
  
- **[Toolkits](./DSTRL/toolkits/README.md)**: Implementation resources including technical architecture, component descriptions, workflows (RFCs), and specific use cases to help develop user journeys for both Classical PKI and Decentralised PKI approaches.

The DTSRL provides practical, validated implementation patterns based on real deployments across 20+ European institutions, supporting both Pilot 1 (Classical PKI unsng CRLs + SD-JWT) and Pilot 2 (Classical PKI uing CRLs + Decentralised PKI using Verifiable Data Registers + W3C VC) approaches.

## Key Features

This framework brings together European educational and professinal qualifications priorities:

- Respects member state sovereignty in education
- Maintains institutional independence
- Protects student privacy
- Supports educational mobility
- Links to quality frameworks
- Creates trusted credentials
- Enables automatic recognition
- Supports lifelong learning
- Records formal and informal learning
- Works across European borders

## Getting Started

For new users, we recommend starting with:

1. Review the [Governance in Education and Professional Qualifications](./governances): to understand types of governance and legal regimes at cross-border level
2. Review the [Sectorial Rulebook](./sectorial-rulebook/) to understand the framework principles
3. Learn about the [eIDAS scenarios](./eidas-scenarios/) to understand the trust models
4. Explore the [Authorisation Model](./eaa-based-authorisation-model/) to understand how trust chains work
5. Identify your [Role(s)](./docs/eIDAS-roles.md) within the ecosystem
6. **Explore the [DTSRL](./DTSRL/) for practical implementation guidance:**
   - Review [User journeys](./DTSRL/user-journeys/) to understand standard processes
   - Study [Scenarios](./DTSRL/scenarios/) from existing piloting agents
   - Access [Toolkits](./DTSRL/toolkits/) for technical implementation resources
   - Understand the [Piloting](./DTSRL/piloting/) framework for participation
7. Explore the [Elements](./elements) section to identify provided solutions to faciliate adoption with existing services
8. Check the [Compliance](./compliance/) requirements for interoperability information

## Implementation Pathways

### For Educational Institutions
Start with the **[DTSRL](./DTSRL/)** to access proven implementation patterns from peer institutions across Europe. The library provides step-by-step guidance for both technical implementation and governance compliance.

### For Technology Providers
Review the **[Toolkits](./DTSRL/toolkits/)** section for technical specifications, API documentation, and integration guidance supporting both Classical PKI and Decentralised PKI approaches.

### For Policy Makers and Governance Bodies
Explore the **[Governance](./governances)** section and **[Sectorial Rulebook](./sectorial-rulebook/)** to understand the regulatory framework and authorisation models.

## Projects Using This Framework

- **DC4EU**: Digital Credentials for Europe (Grant Agreement 101102611)
- [Other projects to be added as they adopt the framework]

## License and Notice

Copyright © 2025 DC4EU under EUPL-2.0 License 

The content of this repository, except in those sections where explicitly announced otherwise, belongs to DC4EU under EUPL-2.0 licence.

For complete license details, see [License Information](./docs/license.md)