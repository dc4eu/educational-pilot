# DC4EU sectoral catalogue of electronic attestations of attributes (EAAs)

## Introduction

The DC4EU project has developed a comprehensive sectoral catalogue of electronic attestations of attributes (EAAs) that operates within the framework of the revised eIDAS regulation (eIDAS2) and the European digital identity wallet (EUDIW). This catalogue establishes clear distinctions between different types of digital credentials based on their legal foundations and practical applications.

## Legal framework and regulatory foundations

### The dual legal regime approach

The DC4EU sectoral catalogue operates under two distinct but complementary legal regimes established by eIDAS2:

#### 1. The eID legal regime

This regime governs **foundational identity credentials** that establish the legal identity of individuals. In the DC4EU context, this specifically refers to:

- **Person identification data (PID)**: the foundational identity credential within the EUDIW
- **Legal entity identification**: credentials that establish the identity of organisations and institutions

These credentials serve as the bedrock of trust within the digital identity ecosystem, providing legally recognised identification that enables all subsequent digital interactions.

#### 2. The trust services legal regime

This regime encompasses all other digital credentials that are not foundational identity credentials. Within this framework, credentials are expressed as **electronic attestations of attributes (EAAs)** and include:

- Professional qualifications and certifications
- Educational achievements and degrees  
- Domain-specific identity credentials
- Organisational memberships and affiliations

## EAA typology and classification

### Foundational identity EAAs

**Person identifier (PID)** represents the core foundational identity credential:

- **Legal basis**: eID legal regime under eIDAS2
- **Purpose**: establishes unique, legally recognised identity for natural persons
- **Scope**: cross-sectoral application across all EU member states
- **Integration**: mandatory component of EUDIW implementation
- **Trust level**: qualified electronic attestation of attributes (QEAA)

### Non-foundational EAAs: two primary categories

#### Category 1: domain-specific identity attestations

These EAAs enable identification, authentication, and authorisation within specific domains whilst not serving as foundational legal identity:

**Characteristics**:
- Provide identity functions within defined contexts
- Enable role-based access and permissions  
- Support domain-specific authentication requirements
- Complement but do not replace foundational PID

**Examples from the DC4EU catalogue**:
- **Enrolment status (EAA1)**: confirms current student status for accessing educational services
- **Professional membership credentials**: validates membership in professional bodies or organisations
- **Engineer ID**: provides professional identity for engineering contexts

#### Category 2: academic and professional achievement attestations

These EAAs document learning outcomes, qualifications, and professional competencies:

**Characteristics**:
- Document completed educational programmes
- Validate professional skills and competencies
- Support mobility and recognition processes
- Enable granular disclosure of achievements

**Examples from the DC4EU catalogue**:
- **Degree qualification (EAA2)**: represents formal degree or qualification from authorised institutions
- **Certificate of professional competence (CPC)**: documents professional certifications and competencies
- **Professional qualification credentials**: validates regulated professional qualifications

## Technical architecture and standards

### Data model foundation

All EAAs in the DC4EU catalogue are built upon:

- **W3C verifiable credentials data model (VCDM)**: ensuring international interoperability
- **European learning model (ELM v3.2)**: providing shared ontology for educational credentials
- **JSON-LD schemas**: enabling machine-readable credential definitions
- **StatusList2021**: supporting real-time revocation and suspension

### Trust infrastructure

The catalogue operates within a sophisticated trust infrastructure:

#### Identity trust (classical PKI)
- **Qualified web authentication certificates (QWACs)**: for secure communication
- **Qualified seal certificates (QSealCs)**: for credential signing
- **EU trusted lists (LOTL)**: for trust service discovery
- **Certificate revocation lists (CRLs) and OCSP**: for revocation checking

#### Functional role trust (decentralised PKI and registries)
- **Trusted issuer registry (TIR)**: registers entities authorised to issue specific EAAs
- **Trusted accreditation organisation registry (TAOR)**: lists accreditation authorities
- **Trusted schema registry (TSR)**: maps EAAs to authorised roles and policies

## EAA characterisation framework

Each EAA in the catalogue is comprehensively characterised using standardised metadata:

### Core identification fields
- **eaa_id**: unique identifier for the EAA type
- **title**: human-readable name of the credential
- **description**: semantic meaning and application domain
- **credential_type**: classification as verifiable credential, verifiable attestation, or QEAA

### Technical specifications
- **data_model**: reference to JSON-LD schema and structural standards
- **sectoral_scope**: domain of application (formal education, professional qualifications, etc.)
- **binding_requirements**: cryptographic binding specifications
- **revocation_support**: status management capabilities

### Authorisation framework
- **issuable_by**: entities authorised to issue the EAA
- **usable_by**: entities authorised to verify the EAA  
- **requires_pid**: whether foundational identity binding is mandatory
- **disclosure_policy**: privacy and access control specifications

## Implementation considerations

### Governance and standards alignment

The catalogue requires coordination across multiple stakeholders:

- **DG-EAC**: responsible for primary, secondary, and tertiary education credentials
- **DG-EMPL**: oversees adult education and vocational training credentials
- **Member states**: maintain sovereignty over educational competencies whilst ensuring interoperability
- **Educational institutions**: must register as trust service providers under eIDAS2

### Privacy and selective disclosure

All EAAs support advanced privacy protection:

- **Selective disclosure**: users can share only necessary credential attributes
- **Zero-knowledge proofs**: enable verification without revealing sensitive information
- **Purpose limitation**: verifiers can only access data relevant to declared purposes
- **Consent management**: users maintain control over credential sharing decisions

### Cross-border recognition

The catalogue facilitates seamless cross-border mobility:

- **Mutual recognition**: eIDAS2 mandates acceptance of qualified EAAs across member states
- **Standardised verification**: common technical standards enable automated recognition
- **Legal harmonisation**: aligned legal frameworks support credential portability
- **Quality assurance**: trust registries ensure credential authenticity and validity

## Future development and evolution

### Continuous expansion

The catalogue will evolve to encompass:

- Additional educational sectors and qualification types
- Emerging professional competency frameworks  
- Micro-credentials and alternative learning pathways
- International qualification recognition mechanisms

### Technology advancement

Future enhancements will include:

- Enhanced zero-knowledge proof implementations
- Improved interoperability with international systems
- Advanced privacy-preserving verification mechanisms
- Integration with emerging European digital infrastructure

This comprehensive framework establishes the foundation for secure, interoperable, and privacy-preserving digital credentials that support educational and professional mobility across Europe whilst maintaining the highest standards of trust and legal compliance.

## Document structure and navigation

This document serves as the main introduction to the DC4EU sectoral EAA catalogue. For detailed technical specifications and data models, please refer to the following chapters:

### Chapter 1: foundational identity data models
- [1.1 Person identifier (PID) specification](./chapter-1-foundational-identity.md#11-person-identifier-pid-specification)
- [1.2 Legal entity identification models](./chapter-1-foundational-identity.md#12-legal-entity-identification-models)
- [1.3 Cross-border identity verification](./chapter-1-foundational-identity.md#13-cross-border-identity-verification)

### Chapter 2: non-foundational identity EAAs
- [2.1 Enrolment status attestation (EAA1)](./chapter-2-non-foundational-identity.md#21-enrolment-status-attestation-eaa1)
- [2.2 Educational ID](./chapter-2-non-foundational-identity.md#22-educational-id)
- [2.3 Alliance ID](./chapter-2-non-foundational-identity.md#23-alliance-id)
- [2.4 European student card](./chapter-2-non-foundational-identity.md#24-european-student-card)
- [2.5 MyAcademic ID](./chapter-2-non-foundational-identity.md#25-myacademic-id)
- [2.6 Professional ID](./chapter-2-non-foundational-identity.md#26-professional-id)
- [2.7 Doctor ID](./chapter-2-non-foundational-identity.md#27-doctor-id)

### Chapter 3: formal education achievement EAAs
#### 3.1 Higher education credentials
- [3.1.1 European higher education diploma (EUHED)](./chapter-3-formal-education.md#311-european-higher-education-diploma-euhed)
- [3.1.2 European higher education diploma supplement (EUHEDS)](./chapter-3-formal-education.md#312-european-higher-education-diploma-supplement-euheds)
- [3.1.3 European higher education transcript of records (EUHETOR)](./chapter-3-formal-education.md#313-european-higher-education-transcript-of-records-euhetor)
- [3.1.4 European higher education proof of enrolment (EUHEPOE)](./chapter-3-formal-education.md#314-european-higher-education-proof-of-enrolment-euhepoe)
- [3.1.5 European higher education micro-credential (EUHEMIC)](./chapter-3-formal-education.md#315-european-higher-education-micro-credential-euhemic)

#### 3.2 Vocational education and training credentials
- [3.2.1 European VET micro-credential (EUVETMC)](./chapter-3-formal-education.md#321-european-vet-micro-credential-euvetmc)
- [3.2.2 European VET diploma (EUVETD)](./chapter-3-formal-education.md#322-european-vet-diploma-euvetd)
- [3.2.3 European VET certificate (EUVETC)](./chapter-3-formal-education.md#323-european-vet-certificate-euvetc)

#### 3.3 Generic educational credentials
- [3.3.1 Degree qualification (EAA2)](./chapters/03-formal-education/degree-qualification.md)
- [3.3.2 European digital credential (EDC)](./chapters/03-formal-education/european-digital-credential.md)

### Chapter 4: professional qualifications EAAs
- [4.1 Certificate of professional competence (CPC)](./chapters/04-professional-qualifications/professional-competence.md)
- [4.2 Professional medical certification (PMC)](./chapters/04-professional-qualifications/medical-certification.md)
- [4.3 Certificate of professional suitability (CPS)](./chapters/04-professional-qualifications/professional-suitability.md)
- [4.4 Accreditation medical training (AMT)](./chapters/04-professional-qualifications/medical-training.md)
- [4.5 Continuous professional development (CPD)](./chapters/04-professional-qualifications/continuous-development.md)
- [4.6 Professional training certificate (PTC)](./chapters/04-professional-qualifications/training-certificate.md)

### Chapter 5: quality assurance regimes
- [5.1 Institutional accreditation schemas](./chapter-5-quality-assurance.md#51-institutional-accreditation-schemas)
- [5.2 European quality assurance register (EQAR) alignment](./chapter-5-quality-assurance.md#52-european-quality-assurance-register-eqar-alignment)
- [5.3 National quality framework integration](./chapter-5-quality-assurance.md#53-national-quality-framework-integration)
- [5.4 Quality labels and certification](./chapter-5-quality-assurance.md#54-quality-labels-and-certification)

### Chapter 6: core data model specifications
#### 6.1 European learning model (ELM) implementation
- [6.1.1 ELM v3.2 ontology specification](./chapter-6-core-data-models.md#611-elm-v32-ontology-specification)
- [6.1.2 ELM-to-W3C VCDM mapping](./chapter-6-core-data-models.md#612-elm-to-w3c-vcdm-mapping)

#### 6.2 W3C verifiable credentials adaptations
- [6.2.1 EDC-W3C VCDM compliant schemas](./chapter-6-core-data-models.md#621-edc-w3c-vcdm-compliant-schemas)
- [6.2.2 Education-specific credential types](./chapter-6-core-data-models.md#622-education-specific-credential-types)
- [6.2.3 Proof formats and verification mechanisms](./chapter-6-core-data-models.md#623-proof-formats-and-verification-mechanisms)

#### 6.3 Multi-language and semantic support
- [6.3.1 Multi-language support structures](./chapter-6-core-data-models.md#631-multi-language-support-structures)
- [6.3.2 Semantic definitions and ontologies](./chapter-6-core-data-models.md#632-semantic-definitions-and-ontologies)
- [6.3.3 ESCO skills integration](./chapter-6-core-data-models.md#633-esco-skills-integration)

### Technical annexes
- [Annex A: Complete JSON-LD schemas repository](./annex_a_json_schemas_repository.md)
- [Annex B: Trust registry specifications (TIR, TAOR, TSR)](./annex_b_trust_registries.md)
- [Annex C: Privacy and disclosure policies](./annex_c_privacy_policies.md)
- [Annex D: Implementation guidelines and conversion tools](./annex_d_implementation_guidelines.md)
- [Annex E: EAA characterisation framework](./annex_e_characterisation_framework.md)
- [Annex F: Compliance and audit requirements](./annex_f_compliance_audit.md)
- [Annex G: Registry URLs and schema locations](./annex_g_registry_urls.md)