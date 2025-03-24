# Implementation of the EAA-based Authorisation Model in DC4EU

## Introduction

This document introduces the implementation of the Electronic Attestation of Attributes (EAA)-based authorisation model within the DC4EU Large Scale Pilot for the domains of education and professional qualifications. The model reflects the structured feedback from the 23 consortium members and is designed to be extendable to all Member States and associated countries of the European Union. It supports full alignment with the eIDAS 2.0 framework, the European Education Area (EEA), and the European Qualifications Framework (EQF).



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

### 1.1 Spain: national implementation

#### 1.1.1 Ministry of Science, Research and Universities
Able to accredit/authorise:
- HigherEducationInstitution
- LicenceToActAtNationalLevel (for HEIs)
- LicenceToActAtEuropeanLevel (for HEIs)
- EQFlevel6 to EQFlevel8 (for HEIs)
- EducationalID (for HEIs)

#### 1.1.2 Ministry of Education and Sports
Able to accredit/authorise:
- PreSchool
- PrimarySchool
- LowerSecondarySchool
- UpperSecondarySchool
- VocationalEducationInstitution
- LicenceToActAtNationalLevel (for primary, secondary and VET institutions)
- EQFlevel1 (Primary)
- EQFlevel2 (Lower Secondary)
- EQFlevel3–4 (Upper Secondary and VET)
- EQFlevel5 (VET)
- EducationalID (for primary, secondary and VET institutions)

#### 1.1.3 Ministry of Employability
Able to accredit/authorise:
- ProfessionalBody
- LicenceToActAtNationalLevel (for professional bodies)
- EQFlevel4–8 (for professional bodies)
- ProfessionalID



## 2. MyAcademicID

GEANT will act as RootTAO at the European (and international) level for MyAcademicID.

### Recognised accreditations:
- MyAcademicIDTAO (assigned to national NRENs)
- MyAcademicIDIssuer (assigned to Higher Education Institutions or NRENs acting on behalf of HEIs)

### 2.1 Spain
- GEANT accredits RedIRIS as MyAcademicIDTAO
- RedIRIS authorises Rovira i Virgili University (URV) as MyAcademicIDIssuer

### 2.2 France
- GEANT accredits Renater as MyAcademicIDTAO
- Renater self-authorises as MyAcademicIDIssuer (acting on behalf of French universities)



## 3. Quality assurance

### 3.1 Higher Education (HE)
ENQA, and technically EQAR, serve as RootTAO for quality assurance in HE.

#### Recognised accreditations:
- QAHELicenseToActAtNationalLevel (to national QA agencies)
- QAHELicenseToActAtRegionalLevel (to regional QA agencies)
- QualityAssuranceAtInstitutionalLevel (to HEIs)
- QualityAssuranceAtProgrammeLevel (to HEIs)

#### 3.1.1 Spain
- ENQA/EQAR accredits ANECA as TAO (QAHELicenseToActAtNationalLevel)
- ANECA accredits AQU as TAO (QAHELicenseToActAtRegionalLevel)
- AQU issues QA authorisations to HEIs at institutional and programme levels
- ENQA/EQAR may also directly issue QA authorisations to HEIs

### 3.2 Vocational Education and Training (VET)
The equivalent bodies are:
- EQAVET (instead of ENQA)
- CEDEFOP (instead of EQAR)

These organisations will follow a similar hierarchy of accreditation and recognition at the national and regional level for VET quality assurance.


## Conclusion

This structured authorisation model allows for scalable, decentralised trust management across education and professional qualifications, making use of interoperable EAAs and fully aligned with the European Digital Identity and related European strategies.

This model will enable Member States and European institutions to verify issuer legitimacy, accreditation, and scope of recognition over time and across borders, improving transparency, mobility, and trust within the European Education and Qualifications ecosystem.
