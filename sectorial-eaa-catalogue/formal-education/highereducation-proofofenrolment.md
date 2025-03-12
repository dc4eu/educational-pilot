# **Higher Education Proof of Enrolment - Digital Credential Specification**

## **Introduction**
The *Higher Education Proof of Enrolment* is an official document issued by a higher education institution to confirm a student’s enrolment in a study programme. This document is used for administrative, financial, and mobility-related purposes within the *European Higher Education Area (EHEA)*.

This specification defines the data model for issuing the *Proof of Enrolment* as a verifiable digital credential, ensuring compliance with *Europass*, *ECTS*, and the *European Learning Model (ELM)*.

## **Data Model**

### **1. Credential Subject Information**
These fields identify the enrolled student.

| **Field**          | **ELM Object**  | **Subobject**        | **Comments** |
|-------------------|---------------|--------------------|-------------|
| **Date of birth** | `elm:Person`  | `elm:dateOfBirth`  | Mandatory |
| **Family name**   | `elm:Person`  | `foaf:familyName`  | Mandatory |
| **Given name**    | `elm:Person`  | `foaf:givenName`   | Mandatory |
| **Personal identifier** | `elm:Person` | `elm:Person` | Optional, institutional/national identifier |


### **2. Institution and Study Programme Information**
These fields define the institution issuing the enrolment confirmation and the related study programme.

| **Field**                                  | **ELM Object**                                    | **Subobject** | **Comments** |
|--------------------------------------------|-------------------------------------------------|-------------|-------------|
| **Name of tertiary education institution** | `elm:awardingBody, elm:Organisation, elm:LegalIdentifier` |  | Mandatory |
| **Name of study programme**                | `elm:LearningAchievementSpecification`         | `dc:title`  | Mandatory |


### **3. Enrolment and Study Programme Details**
These fields confirm the student’s enrolment and provide details on the study programme.

| **Field**                                             | **ELM Object**                           | **Subobject**        | **Comments** |
|------------------------------------------------------|----------------------------------------|-------------------|-------------|
| **Date of enrolment**                                | `elm:LearningOpportunity`              | `dc:PeriodOfTime` | Mandatory |
| **Country of academic institution**                 | `elm:LearningOpportunity`              | `elm:location`    | Optional |
| **Study programme (official) duration in years/months** | `elm:LearningOpportunity`              | `elm:duration`    | Optional |
| **Study programme (official) duration in ECTS credits** | `elm:LearningAchievementSpecification` | `elm:creditPoint` | Mandatory |


## **Implementation Considerations**
- The *Proof of Enrolment* must be issued in a verifiable digital format to support administrative, financial, and mobility-related use cases within the *European Higher Education Area (EHEA)*.
- Institutions should ensure alignment with the *European Credit Transfer and Accumulation System (ECTS)* where applicable.