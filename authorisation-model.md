# Authorisation Model Based on EAAs

## Overview

This document defines an authorisation model aimed at establishing trusted verification and validation processes across different contexts within education and professional qualifications. It ensures that relying parties (verifiers) can determine the legitimacy of an issuer of verifiable credentials, as well as the authorisation chain that validates the issuer.

The model provides a structured framework for managing authorisations, accreditation, and recognition within educational, professional, and quality assurance domains. It does not cover end-user credentials issued by a trusted issuer but focuses on the framework that establishes trust in issuers and their authorisation chains.

## Key benefits

- Ensures trust in the authorisation and accreditation process
- Provides a structured, interoperable model applicable to different domains
- Facilitates verification and traceability of authorisations over time
- Enables compliance with regulatory frameworks such as eIDAS and the European Education Area (EEA)
- Supports historical validation of authorisations to ensure long-term reliability

## Structure of the model

The model consists of two primary components:

### 1. Entity information

Defines attributes of entities involved in authorisation, either as granting authorities (granters) or recipients of authorisation (grantees).

#### Key attributes:

| Attribute | Description |
|-----------|-------------|
| ID | Unique identifier of the entity |
| Name | Legal name (for organisations) or full name (for individuals) |
| Address | Physical location (if applicable) |
| Establishment date | When the entity was created |
| Role | Defines whether the entity is a granter or grantee (or both) |

### 2. Authorisation information

Defines how authorisations are issued, managed, and verified. Each authorisation must contain the following attributes:

| Attribute | Description |
|-----------|-------------|
| Authorisation ID | Unique identifier |
| Granter ID | Entity that issues the authorisation |
| Grantee ID | Entity that receives the authorisation |
| Type of EAA | Specifies the scope of authorisation |
| Jurisdictional limitations | Defines geographic or regulatory scope |
| Issuance date | When the authorisation becomes valid |
| Validity date | When the authorisation expires (if applicable) |
| Evidence | Legal or regulatory proof supporting the authorisation |

## Verification of authorisations

Verifiers must follow a structured process to ensure the validity of authorisations:

1. **Integrity check**: Ensures data has not been modified and maintains cryptographic proof
2. **Issuer recognition**: Confirms the granter is legally authorised to issue the specific authorisation
3. **Status verification**: Checks if the authorisation is still valid and not revoked or suspended
4. **Jurisdiction & usage compliance**: Verifies geographical or regulatory constraints
5. **Trust anchor resolution**: Establishes confidence in the entire authorisation chain by validating trust anchors (e.g., government agencies)

## Typologies of authorisations

The authorisation model applies to various contexts within education and professional qualifications. Below are practical examples of authorisation structures in different domains:

### 1. Formal education

**Example**: A university (e.g., Rovira i Virgili University - URV) is authorised by the Ministry of Universities to issue degrees compliant with the European Higher Education Area (EHEA).

In this scenario:
- **Granter**: Ministry of Universities (trust anchor)
- **Grantee**: Rovira i Virgili University
- **Type of EAA**: Authority to issue EHEA-compliant degrees
- **Jurisdictional limitations**: Spain
- **Evidence**: National legislation on university recognition

### 2. Quality assurance

**Example**: A regional quality assurance agency (e.g., AQU Catalunya) must be authorised by the national agency (ANECA) and comply with European Standards and Guidelines (ESG).

In this scenario:
- **Granter**: National Agency for Quality Assessment and Accreditation (ANECA)
- **Grantee**: Agency for Quality of the University System of Catalonia (AQU)
- **Type of EAA**: Authority to conduct quality assessments
- **Jurisdictional limitations**: Catalonia region
- **Evidence**: Official appointment by the regional government and recognition by ANECA

### 3. Professional qualifications

**Example**: The National Professional Body (NPB) for Physicians (e.g., CGCOM in Spain) is authorised by the Ministry of Health to regulate and manage the practice of medicine, issue professional IDs, and oversee training accreditation.

In this scenario:
- **Granter**: Ministry of Health (trust anchor)
- **Grantee**: General Council of Official Medical Associations (CGCOM)
- **Type of EAA**: Authority to regulate medical practice
- **Jurisdictional limitations**: Spain
- **Evidence**: National legislation on healthcare professionals

**Cross-border example**: A Spanish doctor seeking to work in France may require an Electronic Certificate of Professional Suitability (eCIP) issued by CGCOM, recognised through the Internal Market Information System (IMI).

### 4. Training accreditation & CPD

**Example**: A Spanish healthcare training provider seeking recognition at the national level (via the National Health System credits) and European level (via ECMEC credits) must be authorised by the UEMS (European Union of Medical Specialists).

In this scenario:
- **Granter**: European Union of Medical Specialists (UEMS)
- **Grantee**: Healthcare training provider
- **Type of EAA**: Authority to offer accredited continuing medical education
- **Jurisdictional limitations**: Europe
- **Evidence**: UEMS accreditation certificate

### 5. Digital identities

**Educational ID**: Universities issuing MyAcademicID must be recognised by a National Research & Education Network (NREN) and comply with eduGAIN rules.

In this scenario:
- **Granter**: National Research & Education Network (e.g., RedIRIS in Spain)
- **Grantee**: University
- **Type of EAA**: Authority to issue MyAcademicID credentials
- **Evidence**: Membership in the NREN federation

**Professional ID**: A Professional Body (e.g., CGCOM for doctors) must be authorised to issue professional identity credentials.

In this scenario:
- **Granter**: Ministry of Health
- **Grantee**: CGCOM
- **Type of EAA**: Authority to issue professional identity credentials
- **Evidence**: National legislation on healthcare professionals' identification

## Entity-relationship diagram

The authorisation model can be visualised through an entity-relationship diagram that illustrates how entities, authorisations, and trust anchors interact:

- Legal entities, public organisations, and individuals as actors
- Authorisation relationships between granters and grantees
- Temporal constraints for ensuring historical validation
- Interoperability with European regulatory frameworks

## Implementation in the EAA framework

The authorisation model has been designed to be implemented using Electronic Attestation of Attributes (EAAs) within the European Digital Identity framework. Key implementation considerations include:

1. **Serialisation**: Authorisations are serialised as Verifiable Credentials using the W3C VC Data Model
2. **Trust anchors**: Root authorisations are typically linked to public sector bodies or qualified trust service providers
3. **Verification**: Authorisation chains can be verified using the EBSI verification model
4. **Temporal validation**: The model supports point-in-time verification for historical validation
5. **Revocation**: Authorisations can be revoked using standard revocation mechanisms

## Glossary

- **Accreditation** (Regulation 765/2008): Official recognition that an entity meets required standards
- **Authorisation**: Permission granted by a competent authority to act
- **Electronic Attestation of Attributes (EAA)**: A verifiable credential defining an entity's rights and authorisations
- **Trust framework**: The set of rules and standards governing digital identity systems
- **Verifier**: The entity responsible for validating an authorisation or credential
- **Trust anchor**: An entity that is inherently trusted within a specific context (typically a public authority)

# Governnace identified and modeled for Edcuation and professional Qualifcations

[DC4EU governnace](./docs/governance/README.md)

# Conclusion

This authorisation model provides a robust, interoperable framework for ensuring trusted authorisation processes in education and professional qualifications. By defining clear structures, attributes, and verification methods, it facilitates compliance, interoperability, and long-term validation of authorisations across different domains and jurisdictions.

The model complements the broader Sectorial EAA Catalogue by providing the trust framework within which educational and professional credentials can be issued, verified, and recognised across European borders.
