# Transcript of Records

## Introduction
This page documents a **Transcript of Records** as a **European Digital Credential (EDC)**, ensuring full compliance with **ELM v3.2** and **W3C Verifiable Credential Data Model (VCDM) 1.1**.

The credential follows **Europass, EQF/NQF, and EBSI** standards, allowing seamless **recognition, portability, and verification** across EU Member States.

---

## Credential Schema
The credential is structured using **ELM v3.2** elements, mapped to **W3C-VCDM 1.1**.

### **Credential Metadata**
| Attribute                 | ELM v3.2 Element | Description |
|--------------------------|----------------|-------------|
| `id` | `VerifiableCredential.id` | Unique identifier of the credential |
| `type` | `EuropeanDigitalCredential` | Defines the credential as an ELM-based European Digital Credential |
| `credentialSchema` | `ShaclValidator2017` | Ensures compliance with validation rules |
| `evidence` | `Evidence` | Details supporting the credential |
| `credentialSubject` | `Person` | Information about the holder of the transcript |

---

### **Academic Records**
| Attribute | ELM v3.2 Element | Description |
|-----------|----------------|-------------|
| `title` | `LearningAchievement.title` | Title of the course or subject |
| `awardedBy` | `AwardingProcess.awardingBody` | Institution that provided the academic record |
| `learningOutcome` | `LearningOutcome` | Description of the knowledge and skills acquired |
| `assessment` | `LearningAssessment` | Evaluation method for the subject/course |
| `workload` | `LearningActivity.workload` | Number of **ECTS credits** earned |
| `gradingScheme` | `GradingScheme` | The grading scale applied |
| `awardingDate` | `AwardingProcess.awardingDate` | Date when the transcript was issued |

---

## Graphical Representation
### **Entity-Relationship Diagram**
```mermaid
flowchart LR
    A[Transcript of Records] -->|Issued by| B[University]
    A -->|Contains| C[Academic Record]
    C -->|Evaluated via| D[Assessment]
    C -->|Has Learning Outcomes| E[Learning Outcome]
    C -->|Credits| F[ECTS Credits]
    C -->|Grading| G[Grading Scheme]
    A -->|Accredited by| H[Accreditation]
```
---

## Verification & Accreditation
The credential is verified using **EBSI trust models**, ensuring:
- **Authenticity** (issuer validation)
- **Integrity** (tamper-proof structure)
- **Accreditation compliance** (linked to DEQAR & national frameworks)

### **Accreditation Data**
| Attribute | ELM v3.2 Element | Description |
|-----------|----------------|-------------|
| `accreditation` | `Accreditation` | Institution's accreditation status |
| `accreditingAgent` | `Accreditation.accreditingAgent` | The accrediting authority |
| `decision` | `Accreditation.decision` | Type of accreditation granted |

---

## Example JSON Data
```json
{
  "id": "urn:credential:da8f9ac5-5283-4602-988f-a4bc03c7713d",
  "type": ["VerifiableCredential", "EuropeanDigitalCredential"],
  "credentialSchema": [{
    "id": "http://data.europa.eu/snb/model/ap/edc-generic-full",
    "type": "ShaclValidator2017"
  }],
  "credentialSubject": {
    "id": "urn:epass:person:1",
    "type": "Person",
    "givenName": {"en": ["Ana"]},
    "familyName": {"en": ["Andromeda"]},
    "hasClaim": [{
      "id": "urn:epass:learningAchievement:11",
      "type": "LearningAchievement",
      "title": {"en": ["Introduction to Artificial Intelligence"]},
      "awardedBy": {
        "id": "urn:epass:org:2",
        "type": "Organisation",
        "legalName": {"en": ["Trinity College Dublin"]}
      },
      "workload": "6 ECTS",
      "assessment": "Written Examination",
      "gradingScheme": "A-F scale",
      "awardingDate": "2022-06-15"
    }]
  }
}
```

---

## Compliance & Future Work
This credential ensures **alignment with SDG, OOTS, and eIDAS regulations** for **cross-border recognition**. Future updates will include **integration with Europass Learning Model (ELM) APIs**.

**For more details, visit:** [ELM v3.2 Documentation](https://europa.eu/europass/elm-browser/)

