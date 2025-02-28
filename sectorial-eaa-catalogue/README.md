# Sectorial EAA Rulebook for Education and Professional Qualifications

## Overview

This Sectorial Electronic Attestation of Attributes (EAA) Rulebook contains all data models and schemas agreed at the sectorial level for Education and Professional Qualifications. It provides the technical specifications that implement the principles outlined in the [Sectorial Rulebook](../sectorial-rulebook/).

## Structure

The EAA Rulebook is organised into three main categories:

### [Formal Education](./formal-education/)

This section contains data models and schemas for representing formal educational qualifications, including:

- Diploma credentials
- Degree certificates
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

- Student identity cards
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
