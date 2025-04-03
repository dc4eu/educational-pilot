# Sectorial EAA Catalogue for Education and Professional Qualifications

## Overview

This Sectorial Electronic Attestation of Attributes (EAA) Rulebook contains all data models and schemas agreed at the sectorial level for Education and Professional Qualifications. It provides the technical specifications that implement the principles outlined in the [Sectorial Rulebook](../sectorial-rulebook/).

## EAA catalogue governance
For the definition of the EAA catalogue, it is essential to identify, for each entry in the catalogue, the party responsible for its creation and evolution - that is, the 'Attribute schema provider'.
The common thread throughout the entire EAA catalogue is the utilisation of the European Learning Model (ELM v3.2) as a shared ontology.
Given the absence of a central authority in education, yet recognising the necessity to establish this sectoral role, we might consider making an assignment based on competencies, bearing in mind that **DG-EAC** is responsible for Primary, Secondary and Tertiary education, whilst **DG-EMPL** oversees Adult education and TVET. OF course, Member States, as key satkeholders and comptencies' owners, should also be members of such governance.

## EAAs are not Diplómas

It is important to explain and clarify that there is a distinction between the Diploma itself and an EAA of the diploma (for example, in Spain this is legally required to be issued on A3 paper with specific weight and security measures, or, using digital means, the Diploma is stored, curated and preserved in a database record). 
The EAA does not replace the former, but holds equivalent legal value.

## European Learning Model (ELM)

ELM allows educational institutions, employers, learners, and credential-verifying bodies to communicate clearly and effectively about learning achievements and credentials.

Key benefits include:
- Interoperability across different European systems.
- Easier recognition of qualifications.
- Clear communication about learning outcomes and achievements.
- Standardised descriptions for educational credentials.

For further information on ELM, access [European Learning Model information](./elm/elm.md)


## EDC and ELM, closely realted but not the same

ELM (European Learning Model) is an ontology or conceptual data model describing learning achievements, qualifications, and educational credentials, covering formal, non-formal, and informal education. It is a general framework describing educational data clearly and consistently.
EDC (European Digital Credential) is an application profile that specifically implements the European Learning Model (ELM) to create digital credentials. EDC uses the concepts and structure defined by ELM, adding technical standards and constraints (e.g., SHACL constraints) to ensure data quality, authenticity, and validity specifically for digital credentialing purposes.
In other words:

- ELM provides the underlying conceptual model.
- EDC applies this model specifically to digital credentials, including concrete implementations, validations, and practical usage aligned closely —but not entirely— with W3C Verifiable Credentials.

## EDC-W3C

- EDC fully compliant with W3C-VCDM in aligmnent to implementing acts

## Table with available schemes

| Scope                        | Data model name          | Brief explanation                                                                 | Schema URL                                                                                                                                             | Registry URL                                                                                         |
|-----------------------------|--------------------------|------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| Foundational identity       | PID (Natural Person)     | Person Identification Data (PID) for foundational credentials compliant with eIDAS 2.0 and ARF | [Schema](https://code.europa.eu/ebsi/json-schema/-/tree/main/schemas/vcdm1.1/vid/natural-person)                 | [Registry](https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/z2bTCgjmBDY5kwNWGL3hfSQUZP6d8AZUnLFXe8coTa3zK) |
| Academic and professional achievements       |  EDC-W3C credential  | European Digital Credential compliant with W3C-VCDM v1.1 credential format based on ELM v3.2 in alignment to 1st batch of implementing acts, supports any type of educational and professional qualifications | [Schema](https://code.europa.eu/ebsi/json-schema/-/tree/main/schemas/vcdm1.1/europass/edc)                        | [Registry](https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/z5P8ebAhZjuvypiSXSHoba6vstbhTwnLhVuULWKenuiNJ) |
| Non-foundational identity   | EducationalID           | Identifies the natural person in the context of an educational organisation, including national extensions | [Schema](https://code.europa.eu/ebsi/json-schema/-/tree/main/schemas/vcdm1.1/education/verifiable-education-id) | [Registry](https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/zEmFZquJtANNz7XNE46thRi1E2cAfpQiXVLSBdDgLyfGP) |
| Non-foundational identity   | AllianceID               | Identifies a student or staff member as affiliated with a European university alliance | [Schema](https://code.europa.eu/ebsi/json-schema/-/tree/main/schemas/vcdm1.1/alliance-id)                       | [Registry](https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/zCHc3ZfYg2871W2WftjLu4QNMQrDzG57oG5pvGoyHcagB) |
| Non-foundational identity   | MyAcademicID             | Identity credential for student mobility, based on MyAcademicID and eduGAIN infrastructure | [Schema](https://code.europa.eu/ebsi/json-schema/-/tree/main/schemas/vcdm1.1/multi-uni-pilot/my-academic-id)     | [Registry](https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/z3XDm4kDtztE8DzLsVdhfshYvx2upnfLmqHtyVjkaXM1g) |


## Table with available datamodels based on EDC-W3C

| Scope                        | Data model name          | Brief explanation                                                                 | Schema URL                                                                                                                                             | Registry URL                                                                                         |
|-----------------------------|--------------------------|------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| Education  | Higher Education Micro Credentials            | Educational achievement microcrdential for   | [Schema](https://code.europa.eu/ebsi/json-schema/-/tree/main/schemas/vcdm1.1/europass/edc)     | [Registry](https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/zAEUqPUrQVE7yiesF8xUVHYh4AnqjfHFxCv6GhZ3uvjkW) |
| Professional qualifications  | ProfessionalMedicalCertification             | Professional achievement credential for  | [Schema](https://code.europa.eu/ebsi/json-schema/-/tree/main/schemas/vcdm1.1/medical-certifications/professional-medical-certification)     | [Registry](https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/zAEUqPUrQVE7yiesF8xUVHYh4AnqjfHFxCv6GhZ3uvjkW) |
| Professional qualifications  | CertificateProfessionalCompetence             | Professional achievement credential for  | [Schema](https://code.europa.eu/ebsi/json-schema/-/tree/main/schemas/vcdm1.1/medical-certifications/certificate-professional-competence)     | [Registry](https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/zFkbzRiX4Q7vcaMtNpgq7RzkvkhvRTt9KqMHqGWXrGn85) |



## Detailed information per category or type

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
