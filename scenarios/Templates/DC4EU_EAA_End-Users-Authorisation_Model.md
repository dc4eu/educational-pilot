
# DC4EU - EAA-Based Authorisation Model

**Co-funded by the European Union’s Digital Europe Programme (Grant Agreement no. 101102611)**

---

## Introduction

- defines trusted processes for verifying authorisations
- supports hierarchical trust chains (e.g. Ministry → University)
- applies to education, professional qualifications, and quality assurance

---

## Purpose and Scope

- defines essential elements for trusted authorisation processes
- domain-agnostic: focuses on generic concepts
- does not cover end-user credentials issuance

---

## Key Principles

- RFC2119 terminology (MUST, MAY, etc.)
- Unique ID for each authorisation (ETSI TS 119 472-1 requirement EAA-4.2.3-01)
- Objects must be:
  - publicly accessible
  - immutable
  - verifiable over time
- Lifecycle managed through new object creation (no in-place modification)

---

## Model Structure

### 1. Entity Information

| Field | Cardinality | Type | Description |
|------|--------------|------|-------------|
| id | 1 | string | Unique identifier (local/global) |
| name | 1 | array | Legal name (entities) or full name (persons) |
| address | 0..* | complex | Full address |
| establishment_Date | 1 | dateTime | Establishment date |
| role | 1..* | array | Granter or grantee |

---

### 2. Role Information

| Field | Cardinality | Type | Description |
|------|--------------|------|-------------|
| role_Id | 1 | string | Unique role identifier |
| role_name | 1 | code | Granter or Grantee |

---

### 3. Authorisation Information

| Field | Cardinality | Type | Description |
|------|--------------|------|-------------|
| authorisation_Id | 1 | string | Unique authorisation ID |
| granter_Id | 1 | string | Issuer entity ID |
| grantee_Id | 1 | string | Receiver entity ID |
| eaa_Type | 1..* | ref | Type of EAA authorised |
| limit_Jurisdiction | 0..* | string or array | Jurisdictional limits |
| issuance_Date | 1 | dateTime | When issued |
| valid_From | 1 | dateTime | Validity start |
| expiration_Date | 0..1 | dateTime | Validity end |
| terms_Of_Use | 0..* | string | Usage conditions |
| evidence | 1 | ref | Evidence reference (mandatory in special cases) |

---

## Temporal Aspects

- **Validity periods**
- **Historical preservation**
- **Lifecycle traceability**
- **Change management through new object creation**

---

## Verification of Authorisations

### Step 1: Integrity check
- verify all required attributes
- cryptographic proof validation
- correct linkage granter ↔ grantee

### Step 2: Issuer recognition
- identify granter
- verify its authorisation

### Step 3: Status verification
- check `valid_From` and `expiration_Date`
- check revocation/suspension status

### Step 4: Compliance
- verify `limit_Jurisdiction`
- respect `terms_Of_Use`

### Step 5: Trust anchor resolution
- trace and validate full authorisation chain

---

## Entity-Relationship Diagram Overview

```
[Entity]
  └── (has Role) → [Role]
      └── (grants) → [Authorisation]
          └── (linked to) → [Granter] / [Grantee]
              └── (eaa_Type) → [Electronic Attestation of Attributes]
```

---

## Glossary

- **Accreditation**: Formal recognition (e.g., Regulation 765/2008)
- **Authorisation**: Permission granting
- **Entity**: Participant (legal/public/natural)
- **Granter**: Authority issuing authorisation
- **Grantee**: Entity receiving authorisation
- **Issuer / Holder / Verifier**: Standard roles (aligned with W3C-VC model)
- **Trust Framework**: Set of rules and standards

---

## Examples

### Formal Education

| Granter | Grantee | eaa_Type |
|---------|---------|----------|
| Spanish Ministry of Universities | URV | Public university, degree issuing |
| EHEA Framework | URV | EHEA-compliant degree issuing |

---

### Quality Assurance

| Granter | Grantee | eaa_Type |
|---------|---------|----------|
| Ministry of Universities | ANECA | QA Agencies Coordination |
| ANECA | AQU Catalunya | QA Evaluations |
| EHEA Ministerial Conference | EQAR | ESG-compliant QA registration |
| EQAR | AQU Catalunya | ESG compliance registration |

---

### Professional Qualifications - Physicians

| Granter | Grantee | eaa_Type |
|---------|---------|----------|
| IMI | Ministry of Health | Competent Authority for Health |
| Ministry of Health | CGCOM | Medical Profession Regulation |
| NIMIC | CGCOM | Membership info provision |

---

### MyAcademicID Example

| Granter | Grantee | eaa_Type |
|---------|---------|----------|
| Geant | Italian NREN | Recognise MyAcademicID Issuers |
| Italian NREN | UNIBO | Issue MyAcademicID |

---

### EducationalID Example

| Granter | Grantee | eaa_Type |
|---------|---------|----------|
| Authority | Educational institution | EducationalID Issuance |

---

## Attribution

© 2023-2025 DC4EU

DC4EU project is co-funded by the European Union’s Digital Europe Programme under Grant Agreement no. 101102611
