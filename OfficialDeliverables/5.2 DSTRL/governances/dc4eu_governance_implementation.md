# DC4EU Implementation of Governance Models in Education and Professional Qualifications

## Introduction

The DC4EU Large Scale Pilot has developed and implemented a comprehensive Electronic Attestation of Attributes (EAA)-based authorisation model to digitally represent and verify the governance structures identified in European education and professional qualifications. This implementation translates the complex multi-level governance arrangements described in European frameworks into a practical, interoperable digital trust system.

The model reflects structured feedback from 23 consortium members and is designed to be extensible to all Member States and associated countries of the European Union, supporting full alignment with the eIDAS 2.0 framework, the European Education Area (EEA), and the European Qualifications Framework (EQF).

## Core Implementation Framework

### Electronic Attestation of Attributes (EAA) Model

The DC4EU implementation is built around EAAs - verifiable credentials that define an entity's rights, authorisations, and capabilities within specific governance domains. These EAAs enable:

- **Digital verification** of issuer legitimacy and authorisation chains
- **Cross-border recognition** of institutional mandates and qualifications
- **Temporal validation** ensuring historical accuracy of authorisations
- **Compliance with regulatory frameworks** including eIDAS 2.0 and GDPR

### Three-tier Trust Architecture

The implementation follows a structured three-tier model:

**Root Trusted Accreditation Organisations (RootTAOs)**
- Ultimate trust anchors for specific governance domains
- Typically national-level bodies or European organisations
- Issue EAAs delegating authority to lower levels

**Trusted Accreditation Organisations (TAOs)**
- Intermediate trust entities receiving delegation from RootTAOs
- Usually ministries, agencies, or recognised European bodies
- Grant specific authorisations to operational entities

**Trusted Issuers (TIs)**
- Operational entities that issue credentials to end users
- Educational institutions, professional bodies, quality assurance agencies
- Must hold valid EAAs proving their authorisation scope

## 1. Formal Education Governance Implementation

### National-level Implementation Structure

Each participating Member State has established national RootTAOs that serve as the ultimate trust anchors for formal education within their jurisdiction:

**RootTAO Examples:**
- DC4EU-Spain (Spain)
- DC4EU-Italy (Italy)
- DC4EU-Netherlands (Netherlands)
- DC4EU-Hungary (Hungary)
- DC4EU-Romania (Romania)
- DC4EU-Sweden (Sweden)
- DC4EU-Portugal (Portugal)

### Authorisation Categories

The DC4EU implementation defines two main categories of final authorisations that institutions can receive to issue specific types of credentials:

#### Non-foundational Digital Identity Authorisations

These authorisations enable institutions to issue domain-specific identity credentials:

- `EducationalID` - For pupils, students, and learners in educational institutions
- `MyAcademicIDIssuer` - For federated academic identity within higher education
- `MyAllianceID` - For identity within European University Alliances
- `ProfessionalIdCredential` - For registered professionals in regulated sectors
- `DoctorIdCredential` - For medical professionals
- `EngineerIdCredential` - For engineering professionals
- `EuropeanStudentCard` - For student mobility and services access

#### Academic and Professional Achievement Authorisations

These authorisations enable institutions to issue specific types of academic and professional credentials:

**Higher Education Credentials:**
- `EuropeanHigherEducationMicrocredential` - For focused learning achievements
- `EuropeanHigherEducationProofOfEnrolment` - For current student status verification
- `EuropeanHigherEducationDiploma` - For degree completion
- `EuropeanHigherEducationDiplomaSupplement` - For detailed qualification information
- `EuropeanHigherEducationTranscriptOfRecords` - For academic achievement records

**Secondary and Vocational Education Credentials:**
- `EuropeanUpperSecondaryEducationCertificate` - For secondary education completion
- `EuropeanUpperSecondaryEducationTranscriptOfRecords` - For secondary education records
- `EuropeanVocationalEducationTrainingMicrocredential` - For VET-focused achievements

**Professional Development and Qualification Credentials:**
- `ProfessionalSuitabilityCredential` - For professional competence verification
- `ContinuousMedicalTrainingAccreditation` - For ongoing medical education
- `ContinuousProfessionalDevelopmentCredential` - For professional development activities
- `ProfessionalTrainingCredential` - For professional skills and training

These specific authorisations replace the generic educational level and EQF level authorisations, providing more precise and targeted credential issuance capabilities aligned with European frameworks and mobility requirements.

### Country-specific Implementation Examples

#### Spain Implementation
Spain demonstrates a comprehensive multi-ministry approach with specific credential authorisations:

**Ministry of Science, Research and Universities (TAO)**
- Authorised for higher education institutions to issue:
  - `EuropeanHigherEducationDiploma`
  - `EuropeanHigherEducationDiplomaSupplement`
  - `EuropeanHigherEducationTranscriptOfRecords`
  - `EuropeanHigherEducationProofOfEnrolment`
  - `EuropeanHigherEducationMicrocredential`
  - `EducationalID`
  - `MyAcademicIDIssuer`

**Ministry of Education and Sports (TAO)**
- Authorised for primary, secondary, and VET institutions to issue:
  - `EuropeanUpperSecondaryEducationCertificate`
  - `EuropeanUpperSecondaryEducationTranscriptOfRecords`
  - `EuropeanVocationalEducationTrainingMicrocredential`
  - `EducationalID`

**Ministry of Employability (TAO)**
- Authorised for professional bodies to issue:
  - `ProfessionalIdCredential`
  - `ProfessionalSuitabilityCredential`
  - `ContinuousProfessionalDevelopmentCredential`
  - `ProfessionalTrainingCredential`

**Ministry of Health (specific for medical sector)**
- Authorised CGCOM to issue:
  - `DoctorIdCredential`
  - `ContinuousMedicalTrainingAccreditation`

#### Netherlands Implementation
The Netherlands shows a focused approach on higher education and professional credentials:

**Ministry of Education, Culture and Science (TAO)**
- Authorised for higher education institutions (Saxion, University of Twente, AUAS) to issue:
  - `EuropeanHigherEducationDiploma`
  - `EuropeanHigherEducationDiplomaSupplement`
  - `EuropeanHigherEducationTranscriptOfRecords`
  - `EuropeanHigherEducationMicrocredential`
  - `EducationalID`
  - `MyAcademicIDIssuer`

**Professional Bodies Coordination (TAO)**
- Involves VH, MBO Raad, UNL as intermediary TAOs
- Authorised AUAS and other institutions to issue:
  - `EuropeanVocationalEducationTrainingMicrocredential`
  - `ProfessionalIdCredential`

#### Portugal Implementation
Portugal demonstrates comprehensive coverage with specific credential types:

**Ministry of Education (TAO)**
- Authorised Lusófona University and other institutions across all levels to issue:
  - Complete range of education credentials from secondary to higher education
  - `EuropeanHigherEducationDiploma`, `EuropeanHigherEducationMicrocredential`
  - `EuropeanUpperSecondaryEducationCertificate`
  - `EuropeanVocationalEducationTrainingMicrocredential`
  - `EducationalID`
  - `MyAcademicIDIssuer`

### Institutional Implementation

Trusted Issuers in formal education receive specific authorisations to issue targeted credential types:

**Higher Education Institutions:**
- BME, Edutus (Hungary) - authorised to issue higher education diplomas, transcripts, and microcredentials
- UNIBO (Italy) - comprehensive higher education credential issuance
- Saxion, Twente, AUAS (Netherlands) - focused on higher education and professional credentials
- Lusófona University (Portugal) - full range of higher education credentials
- Spanish universities - comprehensive higher education credential portfolio

**Secondary and VET Institutions:**
- Authorised under appropriate ministry TAOs to issue:
  - `EuropeanUpperSecondaryEducationCertificate`
  - `EuropeanVocationalEducationTrainingMicrocredential`
  - `EducationalID` for students

**Professional Bodies:**
- CGCOM (Spain) - authorised to issue `DoctorIdCredential` and medical training accreditation
- Engineering professional bodies - authorised to issue `EngineerIdCredential`
- Various professional bodies across countries - authorised to issue professional identity and suitability credentials

**European University Alliances:**
- Participating universities within alliances - authorised to issue `MyAllianceID`
- Enables joint programme participation and shared service access

## 2. Quality Assurance Governance Implementation

### Higher Education Quality Assurance

The DC4EU implementation recognises the European-level coordination role whilst maintaining national authority structures:

**European Root Trust Anchor:**
- **EQAR** serves as RootTAO for higher education quality assurance
- Delegates `QAHELicenseToActAtNationalLevel` to recognised national agencies

**National Quality Assurance TAOs:**
- **ANECA** (Spain) - national level authority
- **ANVUR** (Italy) - national level authority
- **NVAO** (Netherlands) - national level authority
- **MAB** (Hungary) - national level authority
- **ARACIS** (Romania) - national level authority
- **A3ES** (Portugal) - national level authority

**Regional Quality Assurance:**
- **AQU Catalunya** (Spain) - receives `QAHELicenseToActAtRegionalLevel` from ANECA
- Demonstrates multi-level delegation within Member States

**Quality Assurance Credentials:**
- `QualityAssuranceAtInstitutionalLevel`
- `QualityAssuranceAtProgrammeLevel`

### Vocational Education and Training Quality Assurance

The VET quality assurance implementation reflects the more diverse European landscape:

**Framework Coordination:**
- **EQAVET** provides guidelines and coordination
- **CEDEFOP** supports with analysis and tools
- No single accreditation registry unlike higher education

**National Implementation:**
- National and regional agencies accredit VET providers
- Sectoral bodies and chambers have supervisory roles
- Awarding bodies may be separate from training providers

**Professional Qualifications Quality Assurance:**
Spain provides a specific example with medical professional development:

**European Coordination (TAO):**
- **UEMS** (European Union of Medical Specialists)
- Coordinates medical CPD/CME quality assurance schemes

**National Implementation (TI):**
- **CGCOM, FFOMC, SEAFORMEC, EC** (Spain)
- Provide quality assurance at institutional and programme levels

## 3. Professional Qualifications Governance Implementation

### National Professional Bodies Structure

The DC4EU implementation recognises the national competence for professional regulation whilst enabling cross-border recognition:

**Spain Professional Qualifications Example:**

**RootTAO:** DC4EU-Spain
- Delegates professional qualification authority

**TAO:** NIMIC (National Internal Market Information Coordinator)
- Coordinates regulated professions recognition
- Interfaces with EU-level IMI system

**Trusted Issuer:** CGCOM (General Council of Official Medical Associations)
- Issues `ProfessionalID` and professional qualifications
- Authorised by Ministry of Health framework

**Specialised Implementation: Medical Professional Credentials**
Spain demonstrates comprehensive medical professional credential implementation:

**TAO:** Ministry of Territorial Policy and Democratic Memory
- Provides regulatory validation for medical professional credentials

**TI:** CGCOM (General Council of Official Medical Associations)
- Issues `DoctorIdCredential` under ministry authorisation
- Issues `ContinuousMedicalTrainingAccreditation` for ongoing professional development
- Enables medical professional identification, verification, and competence tracking

**Engineering Professional Implementation:**
Various Member States have implemented engineering professional credentials:

**Professional Engineering Bodies (TIs):**
- Issue `EngineerIdCredential` for registered engineers
- Provide `ProfessionalSuitabilityCredential` for cross-border recognition
- Support `ContinuousProfessionalDevelopmentCredential` for ongoing competence

## 4. Non-foundational Digital Identity Implementation

### MyAcademicID Implementation

The MyAcademicID implementation demonstrates European-level coordination with national implementation:

**European RootTAO:**
- **GEANT** serves as European-level trust anchor
- Delegates `MyAcademicIDTAO` authority to National Research and Education Networks (NRENs)

**National TAO Implementation:**
- **RedIRIS** (Spain) - Spanish NREN
- **Renater** (France) - French NREN (also acts as issuer)
- **FCCN** (Portugal) - Portuguese NREN
- **GARR** (Italy) - Italian NREN (planned)
- **SURF** (Netherlands) - Dutch NREN (planned)
- Additional NRENs across participating countries

**Institutional Issuers:**
- Universities receive `MyAcademicIDIssuer` authorisation from their national NRENs
- Can issue MyAcademicID credentials to students for cross-border academic service access
- Examples include:
  - Spanish universities through RedIRIS
  - Portuguese universities through FCCN  
  - French universities through Renater (which also acts as direct issuer)

### Comprehensive Digital Identity Implementation

**Educational ID Implementation:**
- Issued by schools, VET centres, higher education institutions
- Authorised through formal education governance chains
- Enables identity matching and service access within education systems across all levels

**Professional ID Implementation:**
- `ProfessionalIdCredential` issued by professional bodies under ministry authorisation
- `DoctorIdCredential` for medical professionals through CGCOM (Spain)
- `EngineerIdCredential` for engineering professionals through relevant bodies
- Supports professional verification and cross-border recognition

**Alliance ID Implementation:**
- `MyAllianceID` issued by universities participating in European University Alliances
- Governed by alliance-specific statutes and agreements
- Enables access to joint programmes, shared services, and collaborative initiatives

**European Student Card Implementation:**
- `EuropeanStudentCard` implemented within European Student Card Initiative
- Coordinates with national education authorities and institutional systems
- Facilitates comprehensive student mobility and service access across Europe

## 5. Technical Implementation Framework

### EAA Structure and Verification

Each EAA contains essential attributes enabling verification:

**Entity Information:**
- Unique identifier
- Legal name and address
- Establishment date
- Role definition (RootTAO, TAO, or TI)

**Authorisation Information:**
- Unique authorisation identifier
- Granter and grantee identities
- Specific EAA type and scope
- Jurisdictional limitations
- Validity periods
- Supporting evidence and legal basis

### Verification Process

The implementation defines a structured verification process:

1. **Integrity Check:** Cryptographic verification of EAA authenticity
2. **Issuer Recognition:** Validation of granter's authority
3. **Status Verification:** Current validity and revocation status
4. **Jurisdiction Compliance:** Geographic and regulatory scope verification
5. **Trust Anchor Resolution:** Chain validation to recognised RootTAOs

### Interoperability Standards

**W3C Verifiable Credentials:**
- EAAs serialised using W3C VC Data Model
- Ensures interoperability across platforms and systems

**eIDAS 2.0 Alignment:**
- Full compliance with European Digital Identity framework
- Integration with EUDI Wallet architecture

**EBSI Integration:**
- Utilises European Blockchain Services Infrastructure
- Supports decentralised verification and trust

## 6. Cross-country Implementation Analysis

### Coverage and Participation

The DC4EU implementation includes comprehensive coverage across participating Member States:

**Active Implementations:**
- Hungary, Italy, Netherlands, Romania, Sweden, Portugal, Spain
- Each with national RootTAOs and ministry-level TAOs
- Institutional participation from universities and professional bodies

**Planned Extensions:**
- Framework designed for all EU Member States and associated countries
- Scalable architecture supporting diverse national governance structures

### Governance Type Distribution

**Formal Education:** Universal implementation across all participating countries
**Quality Assurance:** Higher education focus with EQAR coordination
**Professional Qualifications:** Demonstrated through medical profession examples
**Digital Identity:** MyAcademicID with GEANT coordination, national NREN implementation

### Authorisation Scope Variations

Different countries demonstrate varying approaches:

**Comprehensive Coverage:** Portugal covers all education levels through single ministry
**Distributed Authority:** Spain uses multiple ministries for different education sectors
**Higher Education Focus:** Some countries initially focus on university-level implementation
**Professional Integration:** Netherlands includes professional and microcredentials emphasis

## 7. Implementation Benefits and Outcomes

### Trust and Verification

The DC4EU implementation enables:
- **Instant verification** of institutional authority and credential authenticity
- **Cross-border recognition** without manual verification processes
- **Historical validation** ensuring long-term credential reliability
- **Fraud prevention** through cryptographic integrity and authorisation chains

### Mobility and Recognition

Implementation outcomes include:
- **Enhanced student mobility** through trusted credential verification
- **Professional recognition** streamlined across Member State boundaries
- **Quality assurance transparency** enabling informed decisions by students and employers
- **Digital-first processes** reducing administrative burden

### Compliance and Standards

The implementation ensures:
- **eIDAS 2.0 compliance** with European digital identity requirements
- **GDPR alignment** for privacy-preserving credential management
- **European Education Area support** for policy coordination
- **EQF integration** for qualification level recognition

### Scalability and Extensibility

The model provides:
- **Flexible architecture** accommodating diverse national governance structures
- **Incremental implementation** allowing phased deployment across countries
- **Extensible authorisation types** supporting new qualification types and governance models
- **Interoperability standards** ensuring cross-platform compatibility

## Conclusion

The DC4EU implementation represents a comprehensive digitalisation of European education and professional qualifications governance. By translating complex multi-level governance arrangements into verifiable digital credentials, the project enables enhanced trust, mobility, and recognition whilst preserving the fundamental principles of national competence and European coordination.

The EAA-based authorisation model provides a practical framework for implementing the sophisticated governance structures identified in European education and professional systems. Through careful mapping of authority relationships and technical implementation of verification mechanisms, DC4EU creates a foundation for truly interoperable European digital credentials that respect both institutional autonomy and cross-border recognition requirements.

This implementation serves as a blueprint for extending digital trust mechanisms across the European Education Area, supporting the vision of seamless mobility and recognition whilst maintaining the diversity and quality that characterise European education and professional systems.