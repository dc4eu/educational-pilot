# WP5 T5.2 Onboarding Procedures and Trust Infrastructure - Pilot 1

## Abstract

This document establishes the foundation for developing a "Trust Framework" for **WP5 Pilot 1** within the DC4EU project, specifically focusing on **education and professional qualifications** using **Classical PKI with SD-JWT credentials**. It evaluates the governance impacts, stakeholder roles, traditional PKI ecosystems, eIDAS regulation compliance, and GDPR considerations for educational credential issuance and verification.

By emphasising **SD-JWT-based verifiable credentials** and classical PKI infrastructure, the document seeks to empower educational institutions and professional bodies with reliable, interoperable digital credential management. It serves as an onboarding guide for stakeholders, detailing the processes, benefits, and technical aspects of integrating with the DC4EU WP5 Pilot 1 digital trust framework.

## Keywords

DC4EU, WP5, Pilot1, SD-JWT, Classical PKI, QEAA, PubEAA, EHEA, eID, eIDAS, Educational Credentials, Trust Framework, Onboarding, Verification

---

## EXECUTIVE SUMMARY

One of the main goals of WP5 within the DC4EU project is to create safe and secure credential management services for **education and professional qualifications**, aligning with the revised eIDAS regulation and the European Education Area (EHEA) objectives.

**Pilot 1** implements a **Classical PKI Trust Model** where credentials are issued and verified through hierarchical trust chains using established Certificate Authorities. The credential format follows the **SD-JWT (Selective Disclosure JSON Web Token)** specification, ensuring compatibility with existing digital infrastructures whilst enabling selective disclosure capabilities essential for privacy-preserving credential verification.

To achieve this, a **"Classical PKI Trust Framework"** aligned with the regulatory framework for Education and Professional Qualifications must be designed and implemented, ensuring that every actor can trust the relevant aspects of their interactions whilst maintaining institutional autonomy.

The segment of the Trust Framework that addresses citizens and digital wallets is developed at a higher level within the broader DC4EU architecture. However, educational issuers and professional qualification verifiers must be able to perform basic checks to validate citizens' identities through Person Identification Data (PID) verification.

More directly relevant to WP5 is the need to create and implement Trust Framework building blocks for **educational credential issuers** and **professional qualification verifiers**, which operate within traditional PKI infrastructures. In Educational and Professional Qualification domains, issuer systems and applications initiating the verification process are considered as relying party instances.

This document presents a comprehensive analysis of the onboarding processes for issuers of **electronic attestations of attributes in Education and Professional Qualifications**, as well as for relying parties acting as verifiers, within the framework of Classical PKI and SD-JWT credentials.

---

## CONTENT

### 1 INTRODUCTION

#### 1.1 LEGAL FRAMEWORK

The DC4EU WP5 Pilot 1 operates within the framework of **Regulation (EU) 2024/1183** of the European Parliament and of the Council, which establishes conditions for European Digital Identity Wallets and electronic attestations of attributes (EAAs).

**Educational Attestations of Attributes (EAAs)** are attestations in electronic form that allow educational and professional qualification attributes to be authenticated, where attributes are characteristics, qualifications, rights or competencies of a natural person or educational institution.

Educational institutions and professional bodies are public or semi-public sector entities issuing attestations of attributes to be used in user journeys across Europe involving relying parties from different domains acting as verifiers within the educational and professional ecosystem.

#### 1.2 BACKGROUND AND CONTEXT

**WP5 Pilot 1** represents a pragmatic approach to digital credential management in education and professional qualifications, utilizing **Classical PKI** infrastructure that many educational institutions already possess or can readily adopt.

The **Classical PKI Trust Model** aims to enhance trust in educational transactions within the European Union. Its key objectives include:

□ **Interoperability**: Ensuring that educational credentials and trust services are recognised and accepted across all EU Member States, facilitating cross-border academic and professional mobility.

□ **Security**: Providing a secure environment for educational transactions by setting high standards for credential issuers and verification systems.

□ **Legal Certainty**: Establishing a clear legal framework that defines the rights and obligations of all parties involved in educational credential transactions.

□ **Institutional Control**: Empowering educational institutions and professional bodies by giving them direct control over their credential issuance and verification processes.

□ **Market Development**: Promoting the development of a single digital market for educational services by encouraging the use of electronic trust services.

A key aspect of this trust framework is the emphasis on **mutual authentication of actors**. This involves not only the authentication between the learner and the credential issuer but also the authenticity of all relying parties (including verifiers) towards the holder of a credential.

#### 1.3 PURPOSE AND SCOPE OF THE DOCUMENT

This document outlines the onboarding processes for **Educational EAA providers** in WP5 Pilot 1, the onboarding of relying parties acting as verifiers, and the registration process of schemas and policies within the framework of Classical PKI and SD-JWT credentials.

The core of the trust infrastructure is based on traditional **X.509 public key infrastructures** using **trusted lists**. The primary objective is to define the basic building blocks for establishing trust relationships between educational stakeholders on national and European levels.

#### 1.4 EDUCATIONAL EAAs IN CLASSICAL PKI

The scenario relevant to WP5 Pilot 1 involves **Educational Electronic Attestation Attributes (EAAs)** issued by educational institutions and professional bodies responsible for maintaining authentic sources of educational and professional qualification data.

In this case, the **Classical PKI trust model** is applicable and implies the following:

□ **Educational institutions and professional bodies** design their services ensuring a level of reliability and trustworthiness equivalent to established credential providers, implementing **SD-JWT protocols and interfaces** whilst adhering to applicable formats for educational attestations.

□ **Educational EAA providers** demonstrate to designated national bodies that they fulfil legal requirements for issuing Educational EAAs.

□ **National bodies** notify the European Commission of Educational EAA providers.

□ The **EC includes** Educational EAA providers in trusted lists.

□ **Educational EAA providers** acquire qualified electronic signatures or seals, supported by qualified certificates containing specific sets of certified attributes suitable for automated processing.

□ Educational EAAs benefit from **cross-border recognition** effects, ensuring that credentials issued in one Member State are recognised across all Member States.

#### 1.5 TESTING AND PILOTING

The testing and piloting phases of WP5 Pilot 1 are crucial for validating the capabilities of Classical PKI-based educational credential systems. The primary objectives include:

□ **Assessing feasibility, effectiveness and scalability** of the Classical PKI trust model for educational credentials.

□ **Evaluating potential impact** on governance processes in education and professional qualification domains.

□ **Identifying and addressing** technical, organisational, or business challenges during implementation.

□ **Providing recommendations** on governance of the trust model for Educational and Professional Qualification coordination.

---

### 2 BUILDING TRUST WITH EDUCATIONAL ISSUERS AND VERIFIERS

#### 2.1 INTRODUCTION

When an educational wallet or verification system seeks to retrieve an educational attestation issued by an educational institution (such as a diploma, certificate, or professional qualification), the issuer must present **Issuer Authorisations** through their PKI certificates. These authorisations confirm the issuer's right to issue specific educational EAAs and can be validated electronically through traditional certificate validation processes.

When verifiers need to request information from educational wallet instances, they must authenticate themselves using **X.509 certificates** and may present **Verifier Authorisations** confirming their right to request information from specific Educational EAA types. Educational domains can define disclosure policies to effectively control and limit the sharing of educational or professional information based on the verifier's authorisation within the Classical PKI framework.

The primary requirement directly relevant to WP5 Pilot 1 is to integrate the trust relationships between educational credential issuers and verifiers within the overall Classical PKI trust model.

#### 2.2 ROLES AND RESPONSIBILITIES

The **Classical PKI Trust Framework** for education encompasses various roles essential for ensuring secure and trustworthy educational interactions across the European Union:

□ **Educational Institutions**: Universities, higher education institutions, vocational education providers, and professional education centres that issue primary academic qualifications.

□ **Professional Organisations**: Professional associations, industry certification bodies, and regulatory bodies that provide sector-specific expertise and validation.

□ **Accreditation Bodies**: National accreditors, subject-specific accreditors, and international accreditors providing quality assurance.

□ **Public Authorities**: Education ministries, professional regulators, and quality oversight bodies establishing regulatory frameworks.

□ **Certificate Authorities**: Traditional PKI CAs that issue and manage X.509 certificates for educational institutions and professional bodies.

□ **Trusted List Providers**: Entities maintaining and distributing lists of trusted educational and professional qualification providers.

#### 2.3 PUBLIC KEY INFRASTRUCTURES AND TRUSTED LISTS

**Classical Public Key Infrastructure (PKI)** is the foundational framework securing digital communications in WP5 Pilot 1, using **X.509 digital certificates** to authenticate the identity of educational institutions, professional bodies, and verification systems.

PKIs play a crucial role in relation to trusted lists for educational credentials. Educational trusted lists, as specified under eIDAS Regulation adaptations for education, are essential for ensuring the legality and trustworthiness of educational identification and trust services across EU Member States.

##### 2.3.1 KEY COMPONENTS OF CLASSICAL PKI

In the context of Classical PKI for education, the following roles are particularly important:

1. **Educational Certificate Authorities**
2. **Conformity Assessment Bodies for Education**
3. **National Educational Accreditation Bodies**
4. **Educational Trusted List Providers**

##### 2.3.2 TRUSTED LISTS FOR EDUCATION

An **Educational Trusted List** is a publicly accessible resource that includes qualified educational institutions, professional bodies, and the trust services they provide (e.g., issuing of Educational EAAs such as diplomas, certificates, and professional qualifications).

**Trust Anchors** serve as foundational elements within Educational Trusted List entries, representing highly reliable educational entities or certificates used to verify signatures created by educational institutions.

**Educational relying parties** acting as verifiers can use the trust framework to:
- Check the issuer's certificate
- Validate the signature on the Educational EAA
- Confirm the role of the issuer (ensuring they are authorised to issue specific types of educational credentials)

The following trusted lists are necessary for integrating **Education and Professional Qualifications** within Classical PKI:

□ **Educational Institution Providers Trusted List**: Contains qualified educational institutions registered with their respective national educational authorities.

□ **Professional Body Providers Trusted List**: Includes professional organisations and certification bodies authorised to issue professional qualifications.

□ **Educational Relying Parties (Verifiers) Trusted List**: Contains verification services and platforms authorised to verify educational credentials.

#### 2.4 TRUST RELATIONS

Implementing a digital and interoperable trust infrastructure for Education and Professional Qualifications within Classical PKI is paramount for WP5 Pilot 1.

##### 2.4.1 EDUCATIONAL ISSUERS ONBOARDING

Educational credential issuance is a carefully regulated domain with responsibilities clearly defined through legal mandates and institutional accreditations. Educational institutions maintain repositories of trusted actors, including official Institution IDs, validity statuses, and direct rules regarding authorisations to issue certain educational credentials.

**Onboarding Process for Educational Institutions:**

□ **Registration**: Educational institutions register with their national educational authority or designated PKI provider.

□ **Certificate Issuance**: Educational Certificate Authority issues X.509 certificates to verified educational institutions.

□ **Trusted List Inclusion**: Successfully registered institutions are included in Educational Institution Trusted Lists.

□ **Capability Declaration**: Institutions declare their capability to issue specific types of educational credentials (degrees, diplomas, certificates, etc.).

□ **SD-JWT Implementation**: Institutions implement SD-JWT issuance capabilities for privacy-preserving credential sharing.

Educational institutions within this Classical PKI model benefit from **institutional autonomy** - they are trusted by other actors to issue only those credentials they are legally authorised to provide, operating within regulated frameworks subject to regular audits.

##### 2.4.2 EDUCATIONAL RELYING PARTY ONBOARDING

**Educational Relying Parties** are natural or legal persons that rely upon educational credentials for various purposes such as:
- Academic admission processes
- Professional licensing
- Employment verification
- Continuing education validation

**Onboarding Process for Educational Verifiers:**

□ **Registration**: Relying parties register with Educational Relying Party Registrars in their Member State.

□ **Purpose Declaration**: Clear declaration of verification purposes and legal basis for credential verification.

□ **Access Certificates**: Issuance of X.509 certificates enabling authentication with educational wallet systems.

□ **Authorisation Certificates**: Specific certificates defining rights and authorisations for different types of educational credential verification.

□ **Disclosure Policy Compliance**: Agreement to comply with selective disclosure policies embedded in educational credentials.

##### 2.4.3 EDUCATIONAL SCHEMA ONBOARDING AND CATALOGUES

Educational and Professional Qualification coordination must publish **attribute schemas** describing the structure of Educational EAAs issued, including identifiers, semantics, and encoding of all educational attributes.

**Educational Rulebooks** will be defined where all educational stakeholders are represented, preventing unnecessary differences in syntax and semantics between similar educational attestations.

A **catalogue of published Educational Rulebooks** will enable entities such as Educational Relying Parties to discover which educational attestations exist within the Classical PKI ecosystem.

**WP5 Pilot 1** will deliver rulebooks for key educational credentials implemented as Educational EAAs:
- Academic degrees and diplomas
- Professional certifications
- Vocational qualifications
- Micro-credentials and digital badges

##### 2.4.4 DISCLOSURE POLICY ONBOARDING AND ACCESS RIGHTS

During educational credential issuance, Educational EAA Providers embed **disclosure policies** containing rules determining which types of Relying Parties may receive specific attributes from educational credentials.

**Implementation considerations for educational selective disclosure:**

□ **Institutional Privacy Policies**: Each educational institution defines privacy policies for their credentials.

□ **Regulatory Compliance**: Policies ensure compliance with educational data protection regulations.

□ **Learner Consent**: Final decisions on information sharing remain with the credential holder.

□ **Granular Control**: Different disclosure levels for academic records, personal information, and achievement details.

##### 2.4.5 INTEROPERABILITY CONSIDERATIONS

Ensuring interoperability between various educational systems and actors is crucial for creating a trustworthy educational credential ecosystem:

□ **Common Standards**: Establishing standards and protocols for educational data exchange and communication.

□ **Cross-border Recognition**: Facilitating recognition and acceptance of educational credentials across Member States.

□ **System Integration**: Enabling seamless integration with existing national and EU-level educational systems.

□ **Compliance**: Ensuring compliance with relevant educational regulations and standards to maintain data privacy and security.

---

### 3 IMPLEMENTATION ROADMAP FOR WP5 PILOT 1

#### 3.1 PHASE 1: PREPARATION AND ASSESSMENT

**Partner Ecosystem Mapping**: Identify all WP5 Pilot 1 partners and their roles within the educational sector, including education providers, accreditation issuers, and technology providers.

**Classical PKI Infrastructure Assessment**: Evaluate existing PKI capabilities and requirements for SD-JWT implementation.

**User Journey Mapping**: Collect and analyse current educational credential user journeys to understand existing processes and pain points.

#### 3.2 PHASE 2: PILOT IMPLEMENTATION PREPARATION

**Selection of Piloting Agents**: Choose educational institutions and professional bodies representing diverse educational environments for Classical PKI implementation.

**Technical Integration Preparation**: Identify necessary technical integrations for SD-JWT credential lifecycle management, including issuers, verifiers, and educational databases.

**PKI Certificate Deployment**: Establish X.509 certificate infrastructure for participating educational institutions.

**Training and Support**: Develop training materials for stakeholders involved in Classical PKI-based credential management.

#### 3.3 PHASE 3: FULL-SCALE ROLLOUT

**Production Deployment**: Deploy Classical PKI trust infrastructure across participating educational institutions.

**Cross-border Testing**: Validate cross-border educational credential verification capabilities.

**Performance Monitoring**: Monitor system performance including verification times, user adoption rates, and system reliability.

#### 3.4 PHASE 4: ONGOING MANAGEMENT

**Maintenance**: Ongoing maintenance of PKI certificates, trusted lists, and educational schemas.

**Compliance Monitoring**: Regular compliance assessments for participating educational institutions.

**Framework Evolution**: Continuous improvement based on feedback and emerging requirements.

