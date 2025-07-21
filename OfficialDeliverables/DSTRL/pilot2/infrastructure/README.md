# WP5 T5.2 Onboarding Procedures and Trust Infrastructure - Pilot 2

## Abstract

This document establishes the foundation for developing a **"Hybrid Trust Framework"** for **WP5 Pilot 2** within the DC4EU project, specifically focusing on **education and professional qualifications** using a **combined Classical PKI and Decentralised PKI (dPKI) approach with W3C Verifiable Credentials**. It evaluates the governance impacts, stakeholder roles, the EBSI ecosystem integration, the European Commission's digital identity services, and GDPR compliance for educational credential management.

By emphasising **W3C Verifiable Credentials** and **self-sovereign identity systems** supported by **EBSI (European Blockchain Services Infrastructure)**, the document seeks to empower educational institutions and professional bodies with enhanced control over their credentialing processes whilst enabling granular, verifiable authorisations. It serves as an onboarding guide for stakeholders, detailing the processes, benefits, and technical aspects of integrating with the DC4EU WP5 Pilot 2 hybrid trust framework.

## Keywords

DC4EU, WP5, Pilot2, W3C VC, dPKI, Hybrid PKI, EBSI, EAA, Educational Credentials, Professional Qualifications, Trust Framework, Onboarding, Verification, European Learning Model

---

## EXECUTIVE SUMMARY

One of the main goals of WP5 Pilot 2 within the DC4EU project is to create advanced, secure, and **granularly governed** credential management services for **education and professional qualifications**, aligning with the revised eIDAS regulation and the European Education Area (EHEA) objectives through innovative trust mechanisms.

**Pilot 2** implements a **Hybrid Trust Model** where both **Classical PKI** and **Decentralised PKI** mechanisms coexist. Decentralised trust is supported via **trusted ledgers**, particularly the **European Blockchain Services Infrastructure (EBSI)**. The credential format follows the **W3C Verifiable Credentials (VC)** standard using **W3C-VCDM 1.1 & W3C-VCDM 2.0** data models.

This model supports **long-term interoperability**, alignment with the **eIDAS 2.0 Regulation**, and seamless integration with the **EUDI Wallet** ecosystem whilst addressing the **granular governance needs** of education and professional qualifications.

To achieve this, a **"Hybrid Trust Framework"** aligned with both traditional regulatory frameworks and innovative decentralised governance mechanisms must be designed and implemented, ensuring that every actor can trust the relevant aspects of their interactions whilst enabling **verifiable authorisations** and **role-based governance**.

The segment of the Trust Framework addressing citizens and the EUDI Wallet ecosystem operates at a foundational level within the broader DC4EU architecture. Educational issuers and professional qualification verifiers leverage both traditional PKI validation and **EBSI-based verifiable authorisation** systems to perform comprehensive identity and authorisation validation.

More directly relevant to WP5 Pilot 2 is the implementation of **Trust Framework building blocks** for **educational credential issuers** and **professional qualification verifiers** that operate within both traditional PKI infrastructures and **decentralised ledger-based trust registries**. This enables not only **authentication of identity** but also **verification of specific authorisations** to issue or verify particular types of educational and professional credentials.

This document presents a comprehensive analysis of the onboarding processes for issuers of **electronic attestations of attributes in Education and Professional Qualifications** using **W3C Verifiable Credentials**, as well as for relying parties acting as verifiers, within the framework of the Hybrid Trust Model combining Classical PKI and EBSI-based dPKI.

---

## CONTENT

### 1 INTRODUCTION

#### 1.1 LEGAL FRAMEWORK

WP5 Pilot 2 operates within the framework of **Regulation (EU) 2024/1183** of the European Parliament and of the Council, whilst pioneering the implementation of **Electronic Attestations of Attributes (EAAs)** that extend beyond traditional PKI limitations through **verifiable authorisation credentials**.

**Educational EAAs** in Pilot 2 are attestations in electronic form that enable not only authentication of educational and professional qualification attributes but also **verification of the authorisation chain** that validates an issuer's right to issue specific types of credentials.

Educational institutions and professional bodies operate as **qualified entities** issuing attestations that can be validated through both traditional trust mechanisms and **EBSI-based verifiable authorisation systems**, enabling granular governance of educational credentialing processes.

#### 1.2 BACKGROUND AND CONTEXT

**WP5 Pilot 2** represents an advanced approach to digital credential management that addresses the **limitations of Classical PKI** in educational governance whilst maintaining **compatibility with existing infrastructures**.

The **Hybrid Trust Model** combines the strengths of established PKI systems with the **governance capabilities** of decentralised verifiable credentials. Key objectives include:

□ **Enhanced Interoperability**: Ensuring educational credentials are recognised across diverse trust systems, from traditional PKI to emerging decentralised networks.

□ **Granular Governance**: Providing **verifiable authorisations** that specify not just **who** an entity is, but **what they are authorised to do** in educational and professional contexts.

□ **Legal and Technical Certainty**: Establishing frameworks that satisfy both traditional regulatory requirements and emerging digital governance needs.

□ **Institutional Empowerment**: Enabling educational institutions to demonstrate their **specific authorisations** (e.g., "EQF Level 7 Issuer", "MyAcademicID Provider") in machine-readable, verifiable formats.

□ **European Integration**: Supporting the goals of the **European Education Area**, **EQF implementation**, and **automatic recognition** of learning outcomes through verifiable governance structures.

A key aspect of this hybrid framework is the emphasis on **verifiable authorisation chains**. Unlike traditional PKI which proves identity, the hybrid model enables verification of **role-based authorisations** such as:
- Ministry authorising universities
- National QA agencies accrediting regional bodies  
- NRENs validating federated identity providers
- Professional bodies certifying training providers

#### 1.3 PURPOSE AND SCOPE OF THE DOCUMENT

This document outlines the onboarding processes for **Educational EAA providers** in WP5 Pilot 2, the onboarding of relying parties acting as verifiers, and the registration process of schemas and policies within the framework of **Hybrid Trust** combining Classical PKI and EBSI-based dPKI.

The core infrastructure integrates **traditional X.509 PKI** with **EBSI trust registries** and **W3C Verifiable Credentials**, enabling both identity authentication and **granular authorisation verification**. The primary objective is to establish trust relationships that address the **hierarchical and federated authorisation structures** required in Europe's diverse educational landscape.

#### 1.4 HYBRID EDUCATIONAL EAAS

The scenario relevant to WP5 Pilot 2 involves **Educational Electronic Attestation Attributes (EAAs)** that combine traditional identity validation with **verifiable authorisation credentials** managed through EBSI infrastructure.

In this hybrid approach:

□ **Educational institutions** maintain traditional PKI certificates for identity authentication whilst also holding **verifiable authorisation credentials** issued by competent authorities (e.g., Ministries, National QA agencies).

□ **Authorisation credentials** are issued as **W3C Verifiable Credentials** containing specific authorisation statements such as:
   - `"EQFLevel7Issuer"` - Authority to issue Bachelor's degrees
   - `"MyAcademicIDProvider"` - Authority to issue educational identity credentials  
   - `"ProfessionalCertificationBody"` - Authority to issue professional qualifications
   - `"QualityAssuranceAtProgrammeLevel"` - Authority to conduct educational quality assurance

□ **EBSI Trust Registries** maintain records of root Trust Authority Organisations (TAOs) such as Ministries, EQAR, and GEANT, enabling **verification of authorisation chains**.

□ **Relying parties** can verify both the **identity** of credential issuers (via traditional PKI) and their **specific authorisations** (via EBSI-based verifiable credential validation).

□ The system supports **temporal validation**, ensuring authorisations can be verified **at the time of credential issuance** even if authorisation status changes subsequently.

#### 1.5 TESTING AND PILOTING

The testing and piloting phases of WP5 Pilot 2 focus on validating the capabilities of **Hybrid Trust** systems for educational credentials. Primary objectives include:

□ **Assessing feasibility and scalability** of combined Classical PKI and dPKI systems for educational governance.

□ **Evaluating governance impact** on educational and professional qualification management, including **verifiable authorisation** implementation.

□ **Testing interoperability** between traditional PKI-based systems and EBSI-based decentralised verification.

□ **Validating user journeys** including institutional onboarding, non-foundational identity issuance, diploma issuance, and cross-border verification.

□ **Demonstrating European integration** capabilities supporting automatic recognition and cross-border educational mobility.

---

### 2 BUILDING TRUST WITH HYBRID EDUCATIONAL SYSTEMS

#### 2.1 INTRODUCTION

In WP5 Pilot 2, when an educational wallet or verification system seeks to retrieve educational attestations, **two layers of validation** occur:

1. **Identity Authentication**: Traditional PKI validation confirms **who** the issuer is
2. **Authorisation Verification**: EBSI-based validation confirms **what** the issuer is authorised to issue

Educational institutions present both **PKI certificates** for identity authentication and **verifiable authorisation credentials** from EBSI registries. These authorisations specify rights such as issuing **EQF Level 7 diplomas**, **MyAcademicID credentials**, or **professional certifications**.

When verifiers request information from educational wallets, they similarly authenticate through **dual mechanisms**: traditional certificates for identity and **EBSI-registered authorisations** for specific verification rights. This **hybrid approach** enables granular control over who can request what types of educational information.

The primary innovation of WP5 Pilot 2 is integrating **verifiable governance structures** that reflect the **hierarchical and federated nature** of European educational authority into the technical trust infrastructure.

##### Technical Validation Status
- **ATOS/IZERTIS Solution Validation**: ✅ Complete - Validated using GRNet validation scripts
- **Profile Compliance**: ✅ Verified - Full interoperability compliance confirmed
- **Validation Framework**: [DC4EU Technical Validation Methodology](../../procedures/validation/validation-methodology.md)

#### 2.2 ROLES AND RESPONSIBILITIES

The **Hybrid Trust Framework** encompasses traditional PKI roles enhanced with **decentralised governance capabilities**:

□ **Educational Institutions**: Universities, higher education institutions, and vocational providers that hold both PKI certificates and verifiable authorisation credentials for issuing specific types of educational qualifications.

□ **Professional Organisations**: Certification bodies and professional associations authorised to issue professional qualifications through verifiable credentials chains linked to regulatory authorities.

□ **Trust Authority Organisations (TAOs)**: Root governance entities including:
   - **National Ministries** (Education, Science)
   - **EQAR** (European Quality Assurance Register)
   - **GEANT** (Research and Education Network)
   - **National QA Agencies**

□ **EBSI Infrastructure**: Decentralised registries maintaining:
   - **Trust Registry** - Records of TAOs and their authorisation hierarchies
   - **Schema Registry** - Educational credential schemas and validation rules
   - **DID Registry** - Decentralised identifiers for educational entities

□ **Certificate Authorities**: Traditional PKI providers for identity authentication, integrated with EBSI for enhanced governance.

□ **Relying Parties**: Verification services with both PKI certificates and EBSI-registered verification authorisations for specific educational credential types.

#### 2.3 HYBRID PKI AND EBSI INTEGRATION

**WP5 Pilot 2** implements a sophisticated integration between **Classical PKI** and **EBSI-based dPKI** that addresses the governance needs of educational systems.

##### 2.3.1 DUAL-LAYER AUTHENTICATION

**Identity Layer (Classical PKI)**:
- X.509 certificates for entity identification
- Traditional CA hierarchies for legal entity validation
- eIDAS-compliant electronic signatures and seals

**Authorisation Layer (EBSI dPKI)**:
- W3C Verifiable Credentials for role-based authorisations
- EBSI Trust Registry for TAO validation
- Decentralised identifier (DID) resolution for service discovery

##### 2.3.2 EBSI TRUST REGISTRIES

**Educational Trust Registries** maintained on EBSI include:

□ **TAO Registry**: Root Trust Authority Organisations authorised to issue educational authorisations:
   - National Ministries of Education
   - EQAR and National QA agencies
   - GEANT and National Research Networks

□ **Educational Institution Registry**: Institutions authorised by TAOs to issue specific credential types with verifiable authorisation chains.

□ **Professional Body Registry**: Professional organisations and certification bodies with validated authorisation to issue professional qualifications.

□ **Schema Registry**: Educational credential schemas ensuring consistency across Member States while supporting national variations.

#### 2.4 TRUST RELATIONS IN HYBRID SYSTEMS

Implementing hybrid trust infrastructure requires sophisticated onboarding processes that establish both traditional PKI relationships and **verifiable authorisation chains**.

##### 2.4.1 EDUCATIONAL ISSUERS ONBOARDING

**Enhanced Onboarding Process for Educational Institutions**:

□ **Traditional PKI Registration**: Educational institutions obtain X.509 certificates from recognised Certificate Authorities for identity authentication.

□ **Authorisation Credential Acquisition**: Institutions request **verifiable authorisation credentials** from competent TAOs specifying:
   - Specific types of qualifications they may issue (e.g., "EQFLevel7Issuer")
   - Jurisdictional scope of their authority
   - Temporal validity of authorisations
   - Compliance requirements and audit obligations

□ **EBSI Registration**: Institutions register their DIDs and authorisation credentials in EBSI Trust Registry, enabling decentralised verification.

□ **Multi-format Capability Declaration**: Institutions declare capability to issue both traditional certificates and W3C Verifiable Credentials.

□ **Governance Integration**: Integration with national educational databases and quality assurance systems for ongoing authorisation validation.

**Example Authorisation Chain**:
- **Spanish Ministry of Universities** issues authorisation credential to **Universitat Rovira i Virgili**
- Credential specifies: `"EQFLevel7Issuer"`, `"EducationalIDProvider"`, `"AllianceIDIssuer"`
- URV can demonstrate these specific authorisations to any relying party via EBSI verification

##### 2.4.2 EDUCATIONAL RELYING PARTY ONBOARDING

**Enhanced Onboarding for Verification Services**:

□ **Identity Certification**: Relying parties obtain PKI certificates for identity authentication.

□ **Verification Authorisation**: Acquisition of verifiable credentials specifying:
   - Types of educational credentials they may verify
   - Purposes for which verification is authorised (e.g., admissions, employment, mobility)
   - Data protection and privacy compliance capabilities

□ **EBSI Integration**: Registration of verification services in EBSI Trust Registry with clear specification of authorisation scope.

□ **Cross-border Recognition**: Integration with European recognition networks and automatic recognition systems.

##### 2.4.3 SCHEMA AND GOVERNANCE ONBOARDING

**European Learning Model (ELM) Integration**:

□ **Standardised Schemas**: Educational credentials implement **European Learning Model** schemas registered in EBSI Schema Registry, ensuring European-wide consistency.

□ **National Extensions**: Support for country-specific requirements whilst maintaining core interoperability.

□ **Quality Assurance Integration**: Schemas incorporate QA requirements ensuring credentials meet national and European quality standards.

□ **Automatic Recognition Support**: Schema design facilitates automatic recognition processes as envisioned in European legislation.

**Governance Structure Registration**:

□ **TAO Validation**: Trust Authority Organisations undergo validation processes before registration in EBSI Trust Registry.

□ **Authorisation Chain Documentation**: Clear documentation of who can authorise whom for what types of educational activities.

□ **Temporal Management**: Support for time-limited authorisations and historical validation capabilities.

##### 2.4.4 DISCLOSURE POLICIES AND PRIVACY

**Enhanced Privacy through Selective Disclosure**:

□ **Granular Disclosure Policies**: W3C Verifiable Credentials enable fine-grained control over information sharing based on:
   - Verifier authorisation level
   - Purpose of verification
   - Learner consent preferences
   - Regulatory requirements

□ **European Learning Model Compliance**: Disclosure policies align with ELM semantic frameworks ensuring consistent privacy protection.

□ **Cross-border Privacy**: Harmonised privacy policies supporting GDPR compliance across Member States.

□ **Learner Control**: Enhanced learner control over credential sharing with granular consent mechanisms.

##### 2.4.5 INTEROPERABILITY CONSIDERATIONS

**Multi-System Integration**:

□ **Legacy System Support**: Bridges enabling traditional PKI-only systems to interact with hybrid infrastructure.

□ **Progressive Enhancement**: Educational institutions can adopt hybrid capabilities incrementally without disrupting existing operations.

□ **European Network Integration**: Seamless integration with existing European educational networks including EMREX, eduGAIN, and national student information systems.

□ **Quality Assurance Integration**: Integration with European and national quality assurance frameworks ensuring credential validity.

---

### 3 USER JOURNEYS IN WP5 PILOT 2

#### 3.1 INSTITUTIONAL ONBOARDING JOURNEY

**University Registration and Authorisation Process**:

1. **Initial Registration**: Educational institution registers with national authority and obtains traditional PKI certificates
2. **Authorisation Request**: Institution requests specific authorisation credentials from Trust Authority Organisation
3. **Verification Process**: TAO validates institution's authority to issue requested credential types
4. **Credential Issuance**: TAO issues W3C Verifiable Credential specifying authorisations
5. **EBSI Registration**: Institution registers in EBSI Trust Registry with validated authorisations
6. **System Integration**: Institution integrates hybrid trust capabilities into credentialing systems

#### 3.2 NON-FOUNDATIONAL IDENTITY ISSUANCE JOURNEY

**Student Educational Identity Creation**:

1. **PID Verification**: Student provides Person Identification Data for foundational identity verification
2. **Institution Validation**: Educational institution validates student enrollment and academic standing
3. **Authorisation Check**: System verifies institution's authorisation to issue educational identity credentials
4. **Credential Creation**: Institution issues W3C Verifiable Credential for educational identity
5. **Wallet Storage**: Credential stored in student's EUDI Wallet with selective disclosure capabilities
6. **Cross-border Recognition**: Credential recognised across European educational networks

#### 3.3 DIPLOMA ISSUANCE JOURNEY

**Academic Qualification Credential Process**:

1. **Qualification Completion**: Student completes academic programme meeting institutional and regulatory requirements
2. **Authorisation Verification**: System confirms institution's authorisation to issue specific qualification level
3. **Quality Assurance**: Validation against national and European quality frameworks
4. **Credential Generation**: Institution issues W3C Verifiable Credential containing qualification details
5. **Governance Embedding**: Credential includes verifiable authorisation chain and compliance evidence
6. **Learner Control**: Student receives credential with granular sharing controls

#### 3.4 CROSS-BORDER VERIFICATION JOURNEY

**International Credential Recognition**:

1. **Credential Presentation**: Student presents educational credential to foreign institution/employer
2. **Dual Verification**: Verifier validates both issuer identity (PKI) and authorisation (EBSI)
3. **Authorisation Chain**: System traces authorisation back to recognised TAO
4. **Compliance Check**: Verification confirms credential meets European standards
5. **Recognition Decision**: Automated or assisted recognition based on verifiable governance
6. **Audit Trail**: Complete verification process recorded for compliance and appeals

---

### 4 IMPLEMENTATION ROADMAP FOR WP5 PILOT 2

#### 4.1 PHASE 1: PREPARATION AND ASSESSMENT

**Hybrid Infrastructure Planning**:
- **Partner Ecosystem Mapping**: Identify WP5 Pilot 2 partners and their dual PKI/EBSI integration capabilities
- **EBSI Integration Assessment**: Evaluate EBSI readiness and integration requirements for educational use cases
- **Governance Mapping**: Document existing educational governance structures and their digital transformation requirements
- **User Journey Validation**: Comprehensive analysis of complex user journeys involving multiple trust systems

#### 4.2 PHASE 2: PILOT IMPLEMENTATION PREPARATION

**Technical Integration Preparation**:
- **EBSI Node Deployment**: Establish EBSI infrastructure connections for participating institutions
- **Hybrid Certificate Management**: Implement dual PKI/DID certificate management systems
- **W3C VC Implementation**: Deploy W3C Verifiable Credential issuance and verification capabilities
- **European Learning Model Integration**: Implement ELM-compliant credential schemas
- **Cross-border Testing Infrastructure**: Establish testing networks spanning multiple Member States

#### 4.3 PHASE 3: FULL-SCALE ROLLOUT

**Production Hybrid Deployment**:
- **Multi-national Coordination**: Coordinate hybrid trust infrastructure across participating Member States
- **TAO Integration**: Full integration of Trust Authority Organisations in EBSI registries
- **Educational Network Integration**: Connect with existing European educational networks (EMREX, eduGAIN)
- **Quality Assurance Integration**: Full integration with national and European QA frameworks
- **Performance Optimisation**: Optimise hybrid verification processes for real-time educational scenarios

#### 4.4 PHASE 4: ONGOING MANAGEMENT

**Sustained Hybrid Operations**:
- **Governance Evolution**: Ongoing adaptation of governance structures as European educational integration deepens
- **Technology Updates**: Regular updates to maintain compatibility with evolving EBSI and W3C standards
- **Cross-border Harmonisation**: Continuous work toward automatic recognition and seamless European educational mobility
- **Research and Development**: Ongoing research into advanced trust mechanisms for educational governance

---

### 5 CONCLUSION

WP5 Pilot 2 establishes a sophisticated **Hybrid Trust Framework** that addresses the fundamental limitation of Classical PKI in educational governance - the inability to verify not just **who** an entity is, but **what they are authorised to do**. 

By combining traditional PKI for identity authentication with **EBSI-based verifiable authorisations**, Pilot 2 creates a trust system that reflects the **hierarchical and federated nature** of European educational governance whilst supporting technical interoperability and legal compliance.

The framework enables **granular, verifiable governance** where educational institutions can demonstrate specific authorisations (e.g., "EQF Level 7 Issuer", "MyAcademicID Provider") through machine-readable, cryptographically verifiable credentials. This supports the **European Education Area** goals of automatic recognition, seamless mobility, and trusted cross-border educational interactions.

Through sophisticated onboarding processes for both issuers and verifiers, comprehensive schema management using the **European Learning Model**, and thoughtful privacy-preserving disclosure policies, WP5 Pilot 2 creates a sustainable model for next-generation educational credentials that can serve as a foundation for the future of European educational integration.

The hybrid approach ensures **backward compatibility** with existing PKI systems whilst providing a **forward path** toward fully decentralised, governed educational trust systems that respect institutional autonomy while enabling European-wide interoperability and automatic recognition.