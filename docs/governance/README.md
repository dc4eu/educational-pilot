# Implementation of the EAA-based Authorisation Model in DC4EU

## Introduction

This document introduces the implementation of the Electronic Attestation of Attributes (EAA)-based authorisation model within the DC4EU Large Scale Pilot for the domains of education and professional qualifications. The model reflects the structured feedback from the 23 consortium members and is designed to be extendable to all Member States and associated countries of the European Union. It supports full alignment with the eIDAS 2.0 framework, the European Education Area (EEA), and the European Qualifications Framework (EQF).

This structured authorisation model allows for scalable, decentralised trust management across education and professional qualifications, making use of interoperable EAAs and fully aligned with the European Digital Identity and related European strategies.

This model will enable Member States and European institutions to verify issuer legitimacy, accreditation, and scope of recognition over time and across borders, improving transparency, mobility, and trust within the European Education and Qualifications ecosystem.


## 1. Formal education

Root Trusted Accreditation Organisations (RootTAOs), such as national-level bodies (e.g. DC4EU-SPAIN), will issue EAAs authorising or accrediting one or more Ministries as Trusted Accreditation Organisations (TAOs). These ministries will in turn be able to grant specific authorisations to educational institutions.

### List of potential accreditations:

- LicenceToActAtEuropeanLevel  
- LicenceToActAtNationalLevel  
- PreSchool  
- PrimarySchool  
- LowerSecondarySchool  
- UpperSecondarySchool  
- VocationalEducationInstitution  
- HigherEducationInstitution  
- AdultEducationInstitution  
- ProfessionalBody  
- EQFlevel1 to EQFlevel8  
- EducationalID  
- ProfessionalID  


### [Educational and Professional qualifications governance](./formal-education.md)

## 2. MyAcademicID

GEANT will act as RootTAO at the European (and international) level for MyAcademicID.

### Recognised accreditations:
- MyAcademicIDTAO (assigned to national NRENs)
- MyAcademicIDIssuer (assigned to Higher Education Institutions or NRENs acting on behalf of HEIs)


### [MyAcademicID governance](./myacademicID.md)

## 3. Quality assurance

### 3.1 Higher Education (HE)
ENQA, and technically EQAR, serve as RootTAO for quality assurance in HE.

#### Recognised accreditations:
- QAHELicenseToActAtNationalLevel (to national QA agencies)
- QAHELicenseToActAtRegionalLevel (to regional QA agencies)
- QualityAssuranceAtInstitutionalLevel (to HEIs)
- QualityAssuranceAtProgrammeLevel (to HEIs)

### 3.2 Vocational Education and Training (VET)
The equivalent bodies are:
- EQAVET (instead of ENQA)
- CEDEFOP (instead of EQAR)

These organisations will follow a similar hierarchy of accreditation and recognition at the national and regional level for VET quality assurance.

### [Quality assurance regimes governance](./quality-assurance.md)


## Authrositaion model in a nutshell

For a comprehensive overview of the authorizations identified for all governments, please read the document [Authorizations in a Nutshell](./authorisations-in-a-nutshell.md)
