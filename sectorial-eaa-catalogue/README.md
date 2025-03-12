# Sectorial EAA Rulebook for Education and Professional Qualifications

## Overview

This Sectorial Electronic Attestation of Attributes (EAA) Rulebook contains all data models and schemas agreed at the sectorial level for Education and Professional Qualifications. It provides the technical specifications that implement the principles outlined in the [Sectorial Rulebook](../sectorial-rulebook/).

## Diploma vs EAA

It is important to explain and clarify that there is a distinction between the Diploma itself (for example, in Spain this is legally required to be issued on A3 paper with specific weight and security measures) and an EAA of the diploma. The latter does not replace the former, but holds equivalent legal value

## EAA catalogue governance
For the definition of the EAA catalogue, it is essential to identify, for each entry in the catalogue, the party responsible for its creation and evolution - that is, the 'Attribute schema provider'.
The common thread throughout the entire EAA catalogue is the utilisation of the European Learning Model (ELM v3.2) as a shared ontology.
Given the absence of a central authority in education, yet recognising the necessity to establish this sectoral role, we might consider making an assignment based on competencies, bearing in mind that DG-EAC is responsible for Primary, Secondary and Tertiary education, whilst DG-EMPL oversees Adult education and TVET.


## Structure

The EAA Rulebook is organised into the following categories:

### [Foundational Identity](./foundational-identity/)

This section covers the foundational identity models that serve as the basis for secure identification across the educational ecosystem:

- Person Identification Data (PID) for natural persons
- Legal Entity Identification for educational institutions
- Identity matching mechanisms
- Cross-border identity verification
- Privacy-preserving identity protocols

### [Formal Education](./formal-education/)

This section contains data models and schemas for representing formal educational qualifications, including:

- Diploma credentials
- Degree certificates
- Microcredentials for HE & VET
- Transcripts of records
- Educational identifiers
- Course certificates
- Learning agreements

### [Quality Assurance Regimes](./quality-assurance/)

This section focuses on the data models and schemas related to quality assurance in education:

- Accreditation information
- Institution verification
- European Quality Assurance Register (EQAR) alignment
- National quality framework integration
- Quality labels and certification

### [Non-foundational ID](./non-foundational-id/)

This section covers identifiers and credentials that are not based on foundational identity but are still relevant in educational contexts:

- EductaionalID for student and academic identification
- AllianceID for European University Alliances participants
- MyAcademicID for student and academic mobility
- European Student Card
- Alumni credentials
- Professional membership attestations
- Continuing education certificates
- Skill badges and micro-credentials

## [Data Models](./data-models/)

This section contains the common data models that support all three categories above:

- European Learning Model (ELM) implementation (./data-models/elm-implementation-schema.md)
- W3C Verifiable Credentials data model adaptations
- EDCI (Europass Digital Credentials Infrastructure) alignment
- Multi-language support structures
- Semantic definitions and ontologies

## Implementation

These data models and schemas are designed to be implemented through the technical components described in the [Toolkits](../toolkits/) section. They support the workflows and use cases outlined there while ensuring compliance with the principles established in the [Sectorial Rulebook](../sectorial-rulebook/).

## Version Control

All data models and schemas in this rulebook are versioned to allow for backward compatibility as the framework evolves. Implementers should always check for the latest versions while maintaining support for existing credentials.
