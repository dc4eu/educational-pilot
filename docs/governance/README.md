# Implementation of the EAA-based Authorisation Model in DC4EU

## Table of contents

- [Implementation of the EAA-based Authorisation Model in DC4EU](#implementation-of-the-eaa-based-authorisation-model-in-dc4eu)
  - [Introduction](#introduction)
  - [Table of contents](#table-of-contents)
  - [1. Formal education](#1-formal-education)
    - [List of potential accreditations:](#list-of-potential-accreditations)
    - [1.1 Spain: national implementation](#11-spain-national-implementation)
      - [1.1.1 Ministry of Science, Research and Universities](#111-ministry-of-science-research-and-universities)
      - [1.1.2 Ministry of Education and Sports](#112-ministry-of-education-and-sports)
      - [1.1.3 Ministry of Employability](#113-ministry-of-employability)
  - [2. MyAcademicID](#2-myacademicid)
    - [Recognised accreditations:](#recognised-accreditations)
    - [2.1 Spain](#21-spain)
    - [2.2 France](#22-france)
  - [3. Quality assurance](#3-quality-assurance)
    - [3.1 Higher Education (HE)](#31-higher-education-he)
      - [Recognised accreditations:](#recognised-accreditations-1)
      - [3.1.1 Spain](#311-spain)
    - [3.2 Vocational Education and Training (VET)](#32-vocational-education-and-training-vet)
  - [Governance implementation in DC4EU](#conclusion)


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

## Detailed Governnace implementation in DC4EU

# EAA-based Authorisation Model by Country, Role and Governance Type

| Country     | Governance Type                    | Role | Entity                                              | Authorisations |
|-------------|-------------------------------------|------|------------------------------------------------------|----------------|
| Hungary     | Formal Education                   | RTAO | DC4EU-Hungary                                        | Delegation of LicenceToActAtNationalLevel, EQFlevel6-8, EducationalID |
| Hungary     | Formal Education                   | TAO  | Ministry of Education (Hungary)                     | Accreditation to HEIs for EQFlevel6-8, EducationalID |
| Hungary     | Formal Education                   | TI   | BME, Edutus                                          | HigherEducationInstitution, EQFlevel6-8, EducationalID |
| Hungary     | Quality Assurance                  | RTAO | EQAR                                                 | Delegation of QAHELicenseToActAtNationalLevel |
| Hungary     | Quality Assurance                  | TAO  | MAB                                                  | Accreditation to HEIs for QAInstitutional, QAProgramme |
| Hungary     | Quality Assurance                  | TI   | MAB                                                  | QualityAssuranceAtInstitutionalLevel, QualityAssuranceAtProgrammeLevel |
| Italy       | Formal Education                   | RTAO | DC4EU-Italy                                          | Delegation of LicenceToActAtNationalLevel, EQFlevel6-8, EducationalID |
| Italy       | Formal Education                   | TAO  | Ministry of Universities and Research               | Accreditation to HEIs for EQFlevel6-8, EducationalID |
| Italy       | Formal Education                   | TI   | UNIBO                                                | HigherEducationInstitution, EQFlevel6-8, EducationalID |
| Italy       | Quality Assurance                  | RTAO | EQAR                                                 | Delegation of QAHELicenseToActAtNationalLevel |
| Italy       | Quality Assurance                  | TAO  | ANVUR                                                | Accreditation to HEIs for QAInstitutional, QAProgramme |
| Italy       | Quality Assurance                  | TI   | ANVUR                                                | QualityAssuranceAtInstitutionalLevel, QualityAssuranceAtProgrammeLevel |
| Netherlands | Formal Education                   | RTAO | DC4EU-Netherlands                                    | Delegation of LicenceToActAtNationalLevel, EQFlevel6-7, EducationalID |
| Netherlands | Formal Education                   | TAO  | Ministry of Education, Culture and Science          | Accreditation to HEIs for EQFlevel6-7, EducationalID |
| Netherlands | Formal Education                   | TI   | Saxion, Twente, AUAS                                 | HigherEducationInstitution, EQFlevel6-7, EducationalID |
| Netherlands | Professional Education / Microcredentials | RTAO | DC4EU-Netherlands                                    | Delegation of ProfessionalID, EQFlevel4-5, MicrocredentialsIssuer |
| Netherlands | Professional Education / Microcredentials | TAO  | VH, MBO Raad, UNL                                    | Accreditation to VET/Professional bodies for EQFlevel4-5, MicrocredentialsIssuer |
| Netherlands | Professional Education / Microcredentials | TI   | AUAS                                                 | ProfessionalID, MicrocredentialsIssuer |
| Netherlands | Quality Assurance                  | RTAO | EQAR                                                 | Delegation of QAHELicenseToActAtNationalLevel |
| Netherlands | Quality Assurance                  | TAO  | NVAO                                                 | Accreditation to HEIs for QAInstitutional, QAProgramme |
| Netherlands | Quality Assurance                  | TI   | NVAO                                                 | QualityAssuranceAtInstitutionalLevel, QualityAssuranceAtProgrammeLevel |
| Romania     | Formal Education                   | RTAO | DC4EU-Romania                                        | Delegation of LicenceToActAtNationalLevel, EQFlevel6-8, EducationalID |
| Romania     | Formal Education                   | TAO  | Ministry of Education                                | Accreditation to HEIs for EQFlevel6-8, EducationalID |
| Romania     | Formal Education                   | TI   | UEFISCDI (on behalf of universities)                | HigherEducationInstitution, EQFlevel6-8, EducationalID |
| Romania     | Quality Assurance                  | RTAO | EQAR                                                 | Delegation of QAHELicenseToActAtNationalLevel |
| Romania     | Quality Assurance                  | TAO  | ARACIS                                               | Accreditation to HEIs for QAInstitutional, QAProgramme |
| Romania     | Quality Assurance                  | TI   | ARACIS                                               | QualityAssuranceAtInstitutionalLevel, QualityAssuranceAtProgrammeLevel |
| Sweden      | Formal Education                   | RTAO | DC4EU-Sweden                                         | Delegation of LicenceToActAtNationalLevel, EQFlevel6-8, EducationalID |
| Sweden      | Formal Education                   | TAO  | Swedish Government / Local Authorities / County Councils | Accreditation to HEIs for EQFlevel6-8, EducationalID |
| Sweden      | Formal Education                   | TI   | Swedish Universities                                 | HigherEducationInstitution, EQFlevel6-8, EducationalID |
| Sweden      | Quality Assurance                  | RTAO | EQAR                                                 | Delegation of QAHELicenseToActAtNationalLevel |
| Sweden      | Quality Assurance                  | TAO  | (Pending identification)                             | Expected accreditation to HEIs for QAInstitutional, QAProgramme |
| Sweden      | Quality Assurance                  | TI   | Swedish Universities                                 | QualityAssuranceAtInstitutionalLevel, QualityAssuranceAtProgrammeLevel |
| Portugal    | Formal Education                   | RTAO | DC4EU-Portugal                                       | Delegation of LicenceToActAtNationalLevel, EQFlevel1-8, All education level roles, EducationalID |
| Portugal    | Formal Education                   | TAO  | Ministry of Education (all levels)                  | Accreditation to institutions for EQFlevel1-8, PreSchool, PrimarySchool, SecondarySchool, VET, HEI |
| Portugal    | Formal Education                   | TI   | Lusófona University                                  | HigherEducationInstitution, EQFlevel6-8, EducationalID |
| Portugal    | Quality Assurance                  | RTAO | EQAR                                                 | Delegation of QAHELicenseToActAtNationalLevel |
| Portugal    | Quality Assurance                  | TAO  | A3ES (National Quality Agency)                      | Accreditation to HEIs for QAInstitutional, QAProgramme |
| Portugal    | Quality Assurance                  | TI   | A3ES (HE), DGES (Primary and Secondary)             | QualityAssuranceAtInstitutionalLevel, QualityAssuranceAtProgrammeLevel |
| Portugal    | MyAcademicID                       | RTAO | GEANT                                                | Delegation of MyAcademicIDTAO |
| Portugal    | MyAcademicID                       | TAO  | FCCN (Portuguese NREN)                               | MyAcademicIDTAO at national level |
| Portugal    | MyAcademicID                       | TI   | Lusófona University                                  | MyAcademicIDIssuer |
| Spain       | Formal Education                   | RTAO | DC4EU-Spain                                          | Delegation of LicenceToActAtNationalLevel, LicenceToActAtEuropeanLevel, EQFlevel1-8, EducationalID, ProfessionalID |
| Spain       | Formal Education                   | TAO  | Ministry of Science, Research and Universities       | Accreditation to HEIs for EQFlevel6-8, EducationalID, LicenceToActAtNationalLevel, LicenceToActAtEuropeanLevel |
| Spain       | Formal Education                   | TAO  | Ministry of Education and Sports                     | Accreditation to schools and VET institutions for PreSchool, PrimarySchool, SecondarySchool, EQFlevel1-5, EducationalID |
| Spain       | Formal Education                   | TAO  | Ministry of Employability                            | Accreditation to professional bodies for EQFlevel4-8, ProfessionalID, LicenceToActAtNationalLevel |
| Spain       | Formal Education                   | TI   | Public and private institutions under Ministry accreditations | Issuance of relevant EducationalID, ProfessionalID, and EQF-level credentials |
| Spain       | Professional Qualifications        | RTAO | DC4EU-Spain                                          | Delegation of ProfessionalID, EQFlevel4-8, LicenceToActAtNationalLevel |
| Spain       | Professional Qualifications        | TAO  | NIMIC (National Internal Market Information Coordinator) | Coordination of regulated professions recognition and qualification flows |
| Spain       | Professional Qualifications        | TI   | CGCOM                                                | Issuance of ProfessionalID, Professional Qualifications |
| Spain       | Quality Assurance (Prof. Qual.)    | TAO  | UEMS                                                 | European coordination of medical CPD/CME quality assurance schemes |
| Spain       | Quality Assurance (Prof. Qual.)    | TI   | CGCOM, FFOMC, SEAFORMEC, EC                          | QualityAssuranceAtInstitutionalLevel, QualityAssuranceAtProgrammeLevel |
| Spain       | DoctorID                           | TAO  | Ministry of Territorial Policy and Democratic Memory | Regulatory validation and attribution of DoctorID |
| Spain       | DoctorID                           | TI   | CGCOM                                                | Issuance of DoctorID |


