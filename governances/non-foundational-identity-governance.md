# Non-Foundational Digital Identity Governance

This section provides a business-focused explanation of how non-foundational digital identities—such as EducationalID, ProfessionalID, MyAcademicID, and AllianceID—are governed in the domains of education and professional qualifications through the DC4EU framework.

---

## What are non-foundational digital identities?

Non-foundational digital identities are **domain-specific credentials** that identify an individual within a particular context, such as education or a regulated profession. These IDs:

- Are **not linked to a civil register** or national eID  
- Represent affiliation, authorisation, or status in a sectoral system  
- Are used for **authentication**, **access to services**, and **digital interactions**

---

## Key Types of Non-Foundational IDs

| ID Type           | Purpose                                                       | Issued By                                  |
|------------------|----------------------------------------------------------------|---------------------------------------------|
| **EducationalID** | Recognised ID for pupils, students, or learners               | Schools, VET centres, HEIs                  |
| **ProfessionalID**| Identity for registered professionals in regulated sectors     | Professional bodies (e.g. CGCOM)            |
| **MyAcademicID**  | Federated student identity for academic services              | Universities via NRENs                      |
| **AllianceID**    | Identity within European University Alliances                 | Universities participating in the alliance  |

These digital IDs are issued by **trusted actors**, under **public mandate or statutory governance**, and governed via **Electronic Attestations of Attributes (EAAs)**.

---

## Is there a central European authority?

No — but there are **European-level frameworks** enabling interoperability:

- **GEANT / eduGAIN**: Coordinates cross-border student identity federations  
- **DC4EU**: Aligns identity credentials with the **EUDI Wallet architecture**  
- **Sector-specific trust frameworks**: Guide issuance by ministries, professional bodies, or educational authorities

These frameworks ensure that IDs are:
- **Verifiable** across borders  
- Issued by **recognised and trusted** institutions  
- Technically interoperable

---

## Governance Structure

The governance model follows a **federated and delegated model**:

#### 1. For EducationalID and ProfessionalID
- **Ministries or public regulators** act as **RootTAOs**  
- **Schools, universities, and professional bodies** act as **TAOs and issuers**  
  - Educational institutions issue `EducationalID` to learners  
  - Professional bodies issue `ProfessionalID` to registered professionals  

#### 2. For MyAcademicID
- **GEANT** acts as **RootTAO** at the European level  
- **NRENs** (e.g. RedIRIS in Spain, RENATER in France) are accredited as **TAOs**  
- **Universities** are authorised to issue `MyAcademicID` to higher education students  
  - Either directly or through their NREN federation

#### 3. For AllianceID
- **European University Alliances** are governed by their **own statutes**
- **Any member university** within the alliance can issue an `AllianceID`
- Used for access to joint services, virtual campuses, or mobility platforms
- Does **not require NREN involvement**

---

## Benefits of this governance model

- Supports **cross-border recognition** of identity attributes  
- Enables **privacy-preserving authentication** in line with GDPR and eIDAS 2.0  
- Enhances access to services in:
  - Higher education  
  - Healthcare  
  - Public administration  
  - Professional networks and registries  
  - European University Alliances  
- Ensures credentials are:
  - Legally anchored  
  - Cryptographically verifiable  
  - Discoverable via registries or metadata

---

## Example in practice

Let’s say:
- **Marta is a student** at URV and receives an **EducationalID**  
- After graduating, she qualifies and registers with **CGCOM**, which issues her a **ProfessionalID**  
- While participating in Erasmus+, she uses her **MyAcademicID** to access academic services abroad  
- She also takes part in a joint programme through a **European University Alliance**, where **URV issues her an AllianceID**  
- All four credentials are stored in her **EUDI Wallet**, and can be verified instantly across Europe
