# Implementation in DC4EU

This section describes how the EAA-based authorisation model is being implemented in the **DC4EU Large Scale Pilot** for the domains of education and professional qualifications.

The model is already applied in real-world scenarios across Member States, demonstrating its cross-border potential and adaptability to various governance structures.

---

## An illustrartive example - Spain – Formal Education

### RootTAO: DC4EU-SPAIN  
Acts on behalf of national public authorities to delegate trust.

#### TAO: Ministry of Science, Research and Universities  
Authorises Higher Education Institutions with EAAs such as:
- HigherEducationInstitution  
- EQFlevel6–8  
- EducationalID  
- LicenceToActAtNationalLevel / EuropeanLevel

#### TAO: Ministry of Education and Sports  
Authorises:
- Primary/Secondary Schools and VET Institutions  
- EQFlevel1–5  
- EducationalID  
- LicenceToActAtNationalLevel

#### TAO: Ministry of Employability  
Authorises:
- Professional Bodies (e.g. medical councils)  
- EQFlevel4–8  
- ProfessionalID  
- ProfessionalBody

---

## 🧪 Spain – Quality Assurance

### RootTAO: ENQA / EQAR  
Recognised EU-level QA authorities.

#### TAO: ANECA (National QA agency)  
- Receives QAHELicenseToActAtNationalLevel  
- Authorises AQU Catalunya with QAHELicenseToActAtRegionalLevel

#### Issuer: AQU Catalunya  
- Issues QualityAssuranceAtInstitutionalLevel and QualityAssuranceAtProgrammeLevel EAAs to universities

---

## 🩺 Spain – Professional Qualifications

### RootTAO: Ministry of Health  
Authorises CGCOM (medical council) to issue:

- ProfessionalBody  
- EQFlevel6–8  
- ProfessionalID  
- eCIP (Certificate of Professional Suitability)

---

## MyAcademicID – Cross-border Implementation

### RootTAO: GEANT (European level)

#### Spain:
- GEANT accredits RedIRIS as MyAcademicIDTAO
- RedIRIS accredits URV as MyAcademicIDIssuer

#### France:
- GEANT accredits Renater as MyAcademicIDTAO
- Renater acts as both TAO and MyAcademicIDIssuer for French HEIs

---

## Key Pilot Contributions

- Demonstrated **hybrid trust models** (PKI + dPKI)
- Applied the **EAA framework to real credentials**
- Integrated with **EBSI trust registries** and **wallet interoperability specs**
- Produced governance mappings and onboarding guides

---

## Road to Deployment

The pilot is building:
- Operational infrastructure for onboarding and registry publication
- Machine-readable governance metadata
- Testing environments for wallet-verifier interaction
- Interoperability with European networks (e.g. EMREX, Europass)
