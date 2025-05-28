# Educational and Professional Qualifications Framework

## Overview

This repository provides comprehensive documentation and implementation guidance for the European Educational and Professional Qualifications digital credentials framework. It encompasses sectorial rulebooks, sectorial EAA catalogues, data models, implementation toolkits, and compliance information for creating interoperable systems that respect European values of privacy, institutional autonomy, and cross-border mobility for students and professionals.

## Repository Structure

This repository is organised into several key sections:

- **[eIDAS roles](./docs/eIDAS-roles.md)**: Outlines the key roles within the European digital identity framework under eIDAS, detailing their definitions, functions, types of attestations issued, regulatory references, and compliance requirements.
  
- [Trust models](./sectorial-rulebook/trust-models.md): Outlines trsut models accepted for **Edcuation and Professional qualifcations** (Classical PKI & Decentralised PKI using EBSI). 

- **[eIDAS scenarios](./eidas-scenarios/)**: Outlines the four trust models for electronic attestation of attributes (EAAs) within the European Digital Ecosystem, explaining how EBSI enhances traditional PKI approaches.

- [Bridge between Classical PKI and dPKI using EBSI](./eidas-scenarios/scenario2/trust_modes_bridge.md): How the trust models of classical PKI and dPKI can be combined to enable and support the governance of education and professional qualifications
  
- **[Governance in Education and Professional Qualifications](./governances)**: Understanding existing governnace(s)
  
- **[Governance implementation: the EAA-based authorisation model](./eaa-based-authorisation-model/)**: Defines a structured framework for education and professional qualifications' governance, managing authorisations and recognition within educational, professional, and quality assurance domains.

- **[Sectorial rulebook](./sectorial-rulebook/)**: The core framework that establishes standardised approaches for managing digital educational and professional credentials within the European Union.

- **[Sectorial EAA catalogue](./sectorial-eaa-catalogue/)**: Contains all data models and schemas agreed at sectorial level for Education and Professional Qualifications, including formal education, quality assurance regimes, and non-foundational ID.

- **[EAA Characterisation](./sectorial-eaa-catalogue/EAA_Characterisation.md)**: Characterisation of an Electronic Attestation of Attributes (EAA).

- **[User journeys](./user-journeys/)**: Provided user journeys to demonstrate cross-border interaction, ready-to go infrastructure, and foundation to extend/provide more user journeys and/or EAAs
  
- **[Scenarios](./scenarios/README.md)**: A scenario within DC4EU, details the elements each piloting agent must provide to characterise, execute, and monitor user journeys in alignment with governance, technical, and reporting requirements.

- **[Pilots](./piloting/README.md)**: A scenario within DC4EU, details the elements each piloting agent must provide to characterise, execute, and monitor user journeys in alignment with governance, technical, and reporting requirements.
  
- **[Toolkits](./toolkits/README.md)**: Implementation resources including technical architecture, component descriptions, workflows (RFCs), and specific use cases to help develop user journeys.

- **[Elements](./elements)**: Elements produced/provided by DC4EU to facilitate adoption. Includes data model converters, gateways, reports.

- **[Compliance](./compliance/)**: Information about EBSI and EUDI Wallet compliance tests to ensure interoperability with other issuer, verifier, and wallet solutions.

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

1. Review the [Governance in Education and Professional Qualifications](./governances): to understand types of governnaces and legal regimes at cross-border level
2. Review the [Sectorial Rulebook](./sectorial-rulebook/) to understand the framework principles
3. Learn about the [eIDAS scenarios](./eidas-scenarios/) to understand the trust models
4. Explore the [Authorisation Model](./eaa-based-authorisation-model/) to understand how trust chains work
5. Identify your [Role(s)](./docs/eIDAS-roles.md) within the ecosystem
6. Explore the [Toolkits](./toolkits/README.md) section for implementation guidance
7. Explore the [Elements](./elements) section to identify provided solutions to faciliate adoption with existing services.
8. Understand the [User journeys](./user-journeys/) provided
9. Characterise your [Piloting scenario](./scenarios/README.md)
10. Check the [Compliance](./compliance/) requirements for interoperability information

## Projects Using This Framework

- **DC4EU**: Digital Credentials for Europe (Grant Agreement 101102611)
- [Other projects to be added as they adopt the framework]

## License and Notice

Copyright © 2025 DC4EU under EUPL-2.0 License 

The content of this repository, except in those sections where explicitly announced otherwise, belongs to DC4EU under EUPL-2.0 licence.

For complete license details, see [License Information](./docs/license.md).
