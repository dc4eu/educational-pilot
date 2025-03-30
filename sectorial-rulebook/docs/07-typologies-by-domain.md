# Typologies by Domain

The authorisation model defined in DC4EU supports a wide range of use cases in education and professional qualifications. Each domain has distinct actors, trust anchors, and authorisation hierarchies, which are expressed through Electronic Attestations of Attributes (EAAs).

This section outlines the main typologies by domain and provides practical examples.

---

## 1. Formal Education

Authorisations to issue official academic credentials (e.g. diplomas, degrees) aligned with EQF levels.

### Example: Spain
- **Granter:** Ministry of Science, Research and Universities  
- **Grantee:** Rovira i Virgili University (URV)  
- **EAAs:**  
  - HigherEducationInstitution  
  - EQFlevel6, EQFlevel7, EQFlevel8  
  - EducationalID  
  - LicenceToActAtNationalLevel / EuropeanLevel  

---

## 2. Quality Assurance (QA)

Covers institutional and programme accreditation by recognised QA agencies.

### Example: Spain
- **RootTAO:** ENQA or EQAR  
- **TAO:** ANECA (national QA agency)  
- **Grantee:** AQU Catalunya (regional QA agency)  
- **EAAs:**  
  - QAHELicenseToActAtRegionalLevel  
  - QualityAssuranceAtInstitutionalLevel  
  - QualityAssuranceAtProgrammeLevel  

---

## 3. Professional Qualifications

Applies to regulated professions where practice requires licensing or membership in a professional body.

### Example: Medical profession in Spain
- **RootTAO:** Ministry of Health  
- **Grantee:** CGCOM (General Council of Medical Colleges)  
- **EAAs:**  
  - ProfessionalBody  
  - LicenceToActAtNationalLevel  
  - ProfessionalID  
  - EQFlevel6–8 (linked to medical specialisation)

**Cross-border note:**  
CGCOM may issue an Electronic Certificate of Professional Suitability (eCIP) verifiable in other EU countries.

---

## 4. Training Accreditation & Continuing Professional Development (CPD)

Covers bodies accredited to offer EU-recognised professional development (e.g. CME, CPD).

### Example: UEMS for medical training
- **Granter:** UEMS (European Union of Medical Specialists)  
- **Grantee:** National or regional training provider  
- **EAAs:**  
  - AuthorityToDeliverAccreditedTraining  
  - ECMEC-aligned accreditation

---

## 5. Digital Non-foudnational Identity Credential Issuance

Authorisation to issue digital identifiers used for authentication and identity federation (e.g. MyAcademicID, ProfessionalID).

### Examples:
- **GEANT** accredits RedIRIS in Spain → issues MyAcademicIDIssuer to universities  
- **Ministry of Health** authorises CGCOM → issues ProfessionalID to medical professionals

---

## Reusability Across Domains

The EAA types (e.g. LicenceToAct, EQFlevelX, QualityAssuranceAt...) are **domain-agnostic** and can be reused for:
- National implementation scaling  
- Future interoperability with Micro-credentials, Europass, EMREX  
- Inclusion in sector-specific trust frameworks (e.g. justice, social security)
