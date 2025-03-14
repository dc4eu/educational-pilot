# **Higher Education Microcredential - Digital Credential Specification**

## **Introduction**
A **Higher Education Microcredential** is a verifiable digital credential that certifies the completion of a short learning experience in a specific subject area. Microcredentials aim to support lifelong learning, upskilling, and reskilling, ensuring alignment with **Europass**, **EQF/NQF**, and the **European Learning Model (ELM)**.

This specification defines the data model for issuing a **Microcredential** as a verifiable digital credential, ensuring compliance with **Europass Digital Credentials for Learning (EDC)** and supporting recognition across EU Member States.


## **Data Model**

### **ELM-based Entity-Relationship diagram**
```mermaid
flowchart LR
    A["Credential"] --> B["1 Achievement<br>(mandatory)"]
    A --> C["Accreditation<br>(SAIC-mandatory)"]
    B --> D["Learning Outcomes<br>(mandatory)"]
    B --> E["Assessment<br>(mandatory)"]
    B --> F["Activities<br>(optional)"]
    B --> G["Entitlement<br>(optional)"]
    D --> H["Competencies<br>(mandatory)"]

### **1. Credential Subject Information**
These fields identify the holder of the Microcredential.

| **Field**           | **ELM Object**  | **Subobject**        | **Comments** |
|--------------------|---------------|--------------------|-------------|
| **Date of birth**  | `elm:Person`  | `elm:dateOfBirth`  | Mandatory |
| **Family name**    | `elm:Person`  | `foaf:familyName`  | Mandatory |
| **Given name**     | `elm:Person`  | `foaf:givenName`   | Mandatory |
| **Personal identifier** | `elm:Person` | `elm:Person` | Optional, institutional/national identifier |


### **2. Awarding Institution Information**
These fields define the institution responsible for issuing the Microcredential.

| **Field**                                  | **ELM Object**                                    | **Subobject** | **Comments** |
|--------------------------------------------|-------------------------------------------------|-------------|-------------|
| **Name of awarding institution**          | `elm:awardingBody, elm:Organisation, elm:LegalIdentifier` |  | Mandatory |


### **3. Microcredential Information**
These fields describe the awarded Microcredential.

| **Field**                                       | **ELM Object**                         | **Subobject**       | **Comments** |
|------------------------------------------------|----------------------------------------|-------------------|-------------|
| **Name of Microcredential**                    | `elm:LearningAchievement`             | `dc:title`        | Mandatory |
| **Date of award of Microcredential**           | `elm:AwardingProcess`                 | `elm:awardingDate` | Mandatory |
| **Country of award**                           | `dc:Location`                         |                   | Mandatory |
| **Overall classification of the Microcredential** | `elm:LearningAchievementSpecification` | `elm:Qualification` | Mandatory, EQF/NQF |
| **Main field of study**                        | `elm:LearningAchievementSpecification` | `elm:educationSubject` | Mandatory |
| **Microcredential workload (ECTS credits)**    | `elm:LearningAchievementSpecification` | `elm:creditPoint` | Mandatory |
| **Mode of study**                              | `elm:LearningAchievementSpecification` | `elm:mode` | Mandatory |


### **4. Learning Activities**
These fields provide details about the activities included in the Microcredential.

| **Field**                                  | **ELM Object**                           | **Subobject**        | **Comments** |
|--------------------------------------------|----------------------------------------|-------------------|-------------|
| **Name of learning activity**              | `elm:LearningOpportunity`               | `dc:title`         | Mandatory |
| **Start date of learning activity**        | `elm:LearningOpportunity`               | `dc:PeriodOfTime`  | Mandatory |
| **End date of learning activity**          | `elm:LearningOpportunity`               | `dc:PeriodOfTime`  | Mandatory |
| **Workload in hours**                      | `elm:LearningOpportunity`               | `elm:duration`     | Mandatory |


### **5. Learning Outcomes**
These fields define the knowledge, skills, and competences acquired upon completing the Microcredential.

| **Field**                           | **ELM Object**               | **Subobject**           | **Comments** |
|-------------------------------------|---------------------------|---------------------|-------------|
| **Title of learning outcome**       | `elm:LearningOutcome`     | `dc:title`         | Mandatory |
| **ESCO competencies**               | `elm:LearningOutcome`     | `elm:competence`   | Mandatory |


### **6. Assessment**
These fields describe how the holder's knowledge and skills were assessed.

| **Field**                                  | **ELM Object**                           | **Subobject**        | **Comments** |
|--------------------------------------------|----------------------------------------|-------------------|-------------|
| **Assessment type**                        | `elm:LearningAssessment`               | `elm:grade`        | Mandatory |
| **Assessment method**                      | `elm:LearningAssessment`               | `elm:mode`         | Mandatory |
| **Grading scheme**                         | `elm:LearningAssessment`               | `elm:GradingScheme` | Mandatory |


### **7. Entitlement**
These fields define any rights or privileges conferred by the Microcredential.

| **Field**             | **ELM Object**               | **Subobject**         | **Comments** |
|----------------------|----------------------------|----------------------|-------------|
| **Entitlement type** | `elm:LearningEntitlement`  |                      | Optional (e.g., license to practice) |
| **Jurisdiction of entitlement** | `elm:LearningEntitlement`  | `elm:limitNationalOccupation` | Optional |


## **Implementation Considerations**
- The **Higher Education Microcredential** must be issued in a **verifiable digital format**, ensuring **portability** and **trustworthiness** across *EU Member States*.
- The qualification must align with the **European Qualifications Framework (EQF)** and **National Qualifications Frameworks (NQF)**.
