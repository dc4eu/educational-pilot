# Sectorial EAA Rulebook for Education and Professional Qualifications

## Overview

This Sectorial Electronic Attestation of Attributes (EAA) Rulebook contains all data models and schemas agreed at the sectorial level for Education and Professional Qualifications. It provides the technical specifications that implement the principles outlined in the [Sectorial Rulebook](../sectorial-rulebook/).

## Diploma vs EAAs

It is important to explain and clarify that there is a distinction between the Diploma itself (for example, in Spain this is legally required to be issued on A3 paper with specific weight and security measures) and an EAA of the diploma. The latter does not replace the former, but holds equivalent legal value

## European Learning Model (ELM)

ELM allows educational institutions, employers, learners, and credential-verifying bodies to communicate clearly and effectively about learning achievements and credentials.

Key benefits include:
- Interoperability across different European systems.
- Easier recognition of qualifications.
- Clear communication about learning outcomes and achievements.
- Standardised descriptions for educational credentials.

For further information on ELM, access [European Learning Model information](./elm/elm.md)

## EAA catalogue governance
For the definition of the EAA catalogue, it is essential to identify, for each entry in the catalogue, the party responsible for its creation and evolution - that is, the 'Attribute schema provider'.
The common thread throughout the entire EAA catalogue is the utilisation of the European Learning Model (ELM v3.2) as a shared ontology.
Given the absence of a central authority in education, yet recognising the necessity to establish this sectoral role, we might consider making an assignment based on competencies, bearing in mind that DG-EAC is responsible for Primary, Secondary and Tertiary education, whilst DG-EMPL oversees Adult education and TVET.

## EDC and ELM, closely realted but not the same

ELM (European Learning Model) is an ontology or conceptual data model describing learning achievements, qualifications, and educational credentials, covering formal, non-formal, and informal education. It is a general framework describing educational data clearly and consistently.
EDC (European Digital Credential) is an application profile that specifically implements the European Learning Model (ELM) to create digital credentials. EDC uses the concepts and structure defined by ELM, adding technical standards and constraints (e.g., SHACL constraints) to ensure data quality, authenticity, and validity specifically for digital credentialing purposes.
In other words:

- ELM provides the underlying conceptual model.
- EDC applies this model specifically to digital credentials, including concrete implementations, validations, and practical usage aligned closely—but not entirely—with standards like W3C Verifiable Credentials.

## Structure

The EAA Rulebook is organised into the following categories:

### [Foundational Identity](./foundational-identity/)

### [Formal Education](./formal-education/)

### [Quality Assurance Regimes](./quality-assurance/)

### [Non-foundational ID](./non-foundational-id/)

## [Schemes for Data Models](./schemes-data-models/)

## Implementation

These data models and schemas are designed to be implemented through the technical components described in the [Toolkits](../toolkits/) section. They support the workflows and use cases outlined there while ensuring compliance with the principles established in the [Sectorial Rulebook](../sectorial-rulebook/).

## Version Control

All data models and schemas in this rulebook are versioned to allow for backward compatibility as the framework evolves. Implementers should always check for the latest versions while maintaining support for existing credentials.
