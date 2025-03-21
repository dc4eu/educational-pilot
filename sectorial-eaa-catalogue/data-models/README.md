# Data Models

## Overview

This section contains the common data models that support all credential types in the Educational and Professional Qualifications framework. These foundational models provide consistent structure, semantic definitions, and interoperability standards for the entire credential ecosystem.

## Table Data Models


## Core Data Models

### European Learning Model (ELM) Implementation

These schemas implement the European Learning Model for credential data. Our models include:

- Achievement representation
- Learning outcome documentation
- Learning activity description
- Assessment information
- Issuer details
- Holder information
- Recognition elements
- Supporting documentation links

For detailed schema information, see [ELM Implementation Schema](./elm-implementation-schema.md).

### W3C Verifiable Credentials Data Model Adaptations

These schemas adapt the W3C Verifiable Credentials standard for educational use. Our models include:

- Education-specific credential types
- Contextual definitions for educational terms
- Proof formats for educational credentials
- Educational subject identifiers
- Credential status methods

For detailed schema information, see [VC Data Model Adaptations](./vc-model-adaptations.md).

### EDCI (Europass Digital Credentials Infrastructure) Alignment

These schemas ensure alignment with the Europass Digital Credentials Infrastructure. Our models include:

- Europass credential format compatibility
- Diploma Supplement structure
- Europass Certificate Supplement format
- Credential portability support
- Multi-platform presentation

For detailed schema information, see [EDCI Alignment Schema](./edci-alignment-schema.md).

### Multi-language Support Structures

These schemas enable credential representation across European languages. Our models include:

- Multilingual attribute representation
- Language tagging for credential elements
- Translation verification
- Primary language indication
- Language-specific formatting

For detailed schema information, see [Multi-language Support Schema](./multi-language-schema.md).

### Semantic Definitions and Ontologies

These schemas provide consistent meaning for educational terms. Our models include:

- Educational terminology definitions
- Qualification level taxonomies
- Skill classification systems
- Competency frameworks
- Subject area categorisation

For detailed schema information, see [Semantic Definitions Schema](./semantic-definitions-schema.md).

## Implementation Considerations

These data models are designed to:

- Provide a foundation for all credential types
- Ensure semantic consistency across implementations
- Support multiple European languages
- Enable interoperability between systems
- Facilitate cross-border understanding
- Align with European and international standards

## Technical Standards

These data models follow established technical standards:

- JSON-LD for semantic linking
- JSON Schema for validation
- URI-based identifier systems
- ISO language codes for multilingual support
- Standards-based date and time formats

## Extensibility

All data models support extensibility through:

- Well-defined extension points
- Versioned schemas
- Optional property support
- Context extension mechanisms
- Compatibility guidelines

## Versioning

All data models follow a consistent versioning pattern:
- Major versions for breaking changes
- Minor versions for feature additions
- Patch versions for corrections

Current version: 1.0.0