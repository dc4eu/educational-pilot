# DC4EU Pilot 2: User Journeys Description

The DC4EU Pilot 2, executed under Work Package 5 (WP5), supports six comprehensive User Journeys using a **Hybrid Trust Model** that combines **Classical PKI and Decentralised PKI (dPKI) with W3C Verifiable Credentials** and **EBSI trust registries** for secure credential issuance and verification. These journeys facilitate European educational mobility and professional qualification scenarios, enabling students and professionals to manage and verify digital credentials across European borders with enhanced trust, privacy, and interoperability.

## Key Actors and Elements

- **Credential Holder**: The individual (e.g., Maria García, Spanish student) who interacts with the EUDI Wallet to manage credentials
- **EUDI Wallet**: The European Digital Identity Wallet application used to store, manage, and present verifiable credentials
- **Issuer**: Educational institutions, professional bodies, or authorities integrated with EBSI infrastructure, responsible for generating various types of credentials from the **Sectorial EAA Catalogue**
- **Relying Party (RP)**: The entity (e.g., employer, university, professional organisation) verifying credentials presented by the credential holder
- **Authentic Source**: Secure repositories holding authoritative data (e.g., academic records, professional qualifications) certified under eIDAS 2.0 Article 45b
- **EBSI Infrastructure**: European Blockchain Services Infrastructure providing decentralised trust registries, schema validation, and cross-border verification services
- **Member State Authorities**: National authorities providing foundational identity (PID) and governance oversight
- **Sectorial EAA Catalogue**: Comprehensive collection of Electronic Attestations of Attributes for education and professional qualifications

## Sectorial EAA Catalogue Overview

Pilot 2 implements the complete **Sectorial EAA Catalogue** containing standardised data models for education and professional qualifications. The catalogue includes:

### Educational Credentials (ELM v3.2 Based)
- **EUHED**: European Higher Education Diploma
- **EUHEMC**: European Higher Education Micro Credentials
- **EUVETMC**: European VET Micro Credentials
- **EUHEPOE**: Higher Education Proof of Enrolment
- **EUHEDS**: Higher Education Diploma Supplement
- **EUHETOR**: Higher Education Transcript of Records
- **EUUSC**: Upper Secondary Education Certificate
- **EUUSTOR**: Upper Secondary Education Transcript of Records

### Professional Qualifications
- **CPS**: Certificate of Professional Suitability
- **AMT**: Accreditation Medical Training
- **CPD**: Continuous Professional Development
- **PTC**: Professional Training Certificate

### Non-Foundational Identity Credentials
- **EducationalID**: Institutional educational identity
- **AllianceID**: European university alliance affiliation
- **EuropeanStudentCard**: Student mobility credential
- **MyAcademicID**: Academic identity for mobility
- **ProfessionalID**: Professional identity credential
- **DoctorID**: Medical professional identity
- **EngineerID**: Engineering professional identity

## User Journeys

### 1. Install Wallet
**Description**: The credential holder installs and configures the EUDI Wallet to manage digital credentials in the European ecosystem.

- **Actors and Elements**:
  - **Credential Holder**: Downloads and installs the EUDI Wallet
  - **EUDI Wallet**: European Digital Identity Wallet with W3C VC support
  - **Setup Guide**: [Detailed installation instructions](setup-guide.md)

- **Interactions**:
  - Download from official sources (Google Play Store or TestFlight for iOS)
  - Complete initial setup: PIN, biometrics, seed phrase backup
  - Generate Decentralised Identifier (DID)
  - Configure privacy and security settings

- **Trust Framework**: EUDI Wallet integrates with EBSI infrastructure for European-wide credential compatibility

### 2. Obtain Foundational Identity (PID)
**Description**: The credential holder obtains their foundational Person Identification Data (PID) credential, which serves as the **mandatory prerequisite** for all other credential issuance.

- **Actors and Elements**:
  - **Credential Holder**: Spanish citizen María García
  - **Member State Authority**: Spanish national identity infrastructure
  - **PID Issuer**: eIDAS 2.0 compliant identity provider
  - **Authentic Source**: National identity registry

- **Critical Requirement**: **All subsequent credential issuance requires verified PID**
- **Detailed Journey**: [Complete PID issuance process](pid_retreival.md)

- **Interactions**:
  - Authenticate with national identity system (Cl@ve for Spain)
  - Undergo high assurance identity verification
  - Receive cryptographically signed PID credential
  - Store securely in EUDI Wallet

- **Trust Framework**: eIDAS 2.0 compliance with Member State sovereignty preservation

### 3. Obtain Non-Foundational Identity Credential
**Description**: The credential holder obtains an educational or professional identity credential that establishes their relationship with an institution or professional body.

- **Example**: EducationalID issuance at Universitat Rovira i Virgili
- **Detailed Journey**: [Complete EducationalID issuance process](onboarding_in_educational_domain.md)

- **Mandatory Prerequisite**: **Valid PID credential must be presented and verified**

- **Actors and Elements**:
  - **Student**: María García with verified PID
  - **University**: Universitat Rovira i Virgili (dual role as Authentic Source and Issuer)
  - **EBSI Infrastructure**: Trust registries and verification services

- **Process Flow**:
  1. **PID Verification**: Mandatory presentation of foundational identity
  2. **Identity Matching**: Correlation between legal identity (PID) and institutional records
  3. **EducationalID Issuance**: Institutional credential following eduGAIN/SCHAC standards
  4. **European Recognition**: EBSI-anchored credential for cross-border validity

- **Applicable to All Non-Foundational IDs**: EducationalID, AllianceID, EuropeanStudentCard, MyAcademicID, ProfessionalID, DoctorID, EngineerID

### 4. Issue Academic/Professional Achievement Credential
**Description**: The credential holder obtains a learning achievement or professional qualification credential representing completed education or training.

- **Example**: EUHED (European Higher Education Diploma) for Computer Science degree
- **Detailed Journey**: [Complete diploma issuance process](diploma_issuance.md)

- **Prerequisites**: 
  - **Non-foundational identity credential** (e.g., EducationalID) - **mandatory**
  - **May also require PID** depending on institutional requirements

- **Actors and Elements**:
  - **Graduate**: María García with verified EducationalID
  - **University**: Universitat Rovira i Virgili with EAA authorisation
  - **Academic Registry**: Authentic source for academic achievements
  - **EBSI Trust Network**: European-wide validation infrastructure

- **Process Flow**:
  1. **EducationalID Verification**: Mandatory institutional identity validation
  2. **Academic Achievement Validation**: Degree completion verification
  3. **ELM v3.2 Compliance**: European Learning Model standards application
  4. **Credential Issuance**: EUHED diploma with European recognition

- **Applicable to All EAA Types**: Any credential from the Sectorial EAA Catalogue can be issued following this pattern, with specific business rules for each credential type

### 5. Verify Academic/Professional Credential
**Description**: A relying party verifies the credential holder's academic or professional qualifications for employment, further education, or professional practice.

- **Example**: TechCorp Barcelona verifying María's EUHED diploma
- **Detailed Journey**: [Complete credential verification process](verify_diploma.md)

- **Actors and Elements**:
  - **Employer**: James Thompson at TechCorp Barcelona
  - **Graduate**: María García with EUHED diploma
  - **Verification Infrastructure**: EBSI trust registries and cryptographic validation
  - **Original Issuer**: Universitat Rovira i Virgili for status verification

- **Process Flow**:
  1. **Verification Request**: Employer initiates credential verification
  2. **Credential Presentation**: Graduate shares selected credential
  3. **Cryptographic Validation**: EBSI verifies digital signatures and trust chains
  4. **Status Confirmation**: Real-time validation of credential validity
  5. **Recognition Decision**: Instant qualification verification for hiring/admission

- **Universal Verification**: This process applies to verification of any credential from the Sectorial EAA Catalogue

### 6. Cross-Border Recognition and Mobility
**Description**: The credential holder uses their European credentials for cross-border mobility, whether for education, employment, or professional practice.

- **Actors and Elements**:
  - **Mobile Citizen**: María García with portfolio of European credentials
  - **Foreign Institution/Employer**: European entity in different Member State
  - **EBSI Infrastructure**: Cross-border trust propagation
  - **Recognition Frameworks**: Bologna Process, Professional Qualifications Directive

- **Process Flow**:
  1. **Credential Portfolio**: Present relevant credentials from EUDI Wallet
  2. **European Validation**: EBSI provides instant trust verification
  3. **Standards Recognition**: ELM v3.2 and European frameworks ensure compatibility
  4. **Automatic Processing**: Streamlined recognition reducing bureaucratic barriers

## Technical Architecture

### Trust Model
- **Hybrid PKI**: Combines Classical PKI with Decentralised PKI via EBSI
- **W3C Verifiable Credentials**: Standard format for all credentials
- **eIDAS 2.0 Compliance**: Full regulatory alignment
- **European Learning Model v3.2**: Standardised educational data representation

### Infrastructure Components
- **EBSI Trust Registries**: DID Registry, Trusted Issuer Registry, Schema Registry
- **Authentic Sources**: eIDAS 2.0 Article 45b compliant data repositories
- **Member State Integration**: National identity and educational systems
- **Cross-Border Protocols**: European-wide verification and recognition

### Security and Privacy
- **High Assurance**: eIDAS Level of Assurance High for foundational identity
- **Selective Disclosure**: Granular control over shared information
- **Cryptographic Integrity**: ES256 signatures with DID-based authentication
- **Privacy by Design**: GDPR compliance with data minimisation

## Key Innovations

1. **Comprehensive EAA Catalogue**: Complete sectorial coverage for education and professional qualifications
2. **Mandatory Identity Foundation**: All credentials anchored to verified foundational identity (PID)
3. **Layered Identity Architecture**: Foundational → Non-foundational → Achievement credentials
4. **Universal Verification**: Single verification pattern for all credential types
5. **European Interoperability**: Standards-based approach ensuring cross-border compatibility
6. **Hybrid Trust Model**: Combining traditional and innovative trust mechanisms

## Implementation Notes

- **Credential Variety**: While examples focus on specific credentials (EUHED, EducationalID), the framework supports **all credentials defined in the Sectorial EAA Catalogue**
- **Prerequisites**: Clear hierarchy - PID required for non-foundational identity; non-foundational identity (and sometimes PID) required for achievement credentials
- **Scalability**: Architecture designed to accommodate all European educational institutions and professional bodies
- **Compliance**: Full alignment with eIDAS 2.0, European Learning Model, and national regulations

This pilot demonstrates the practical implementation of European digital credentials for education and professional qualifications, providing a foundation for large-scale adoption across all EU Member States.
