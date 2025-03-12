# **Higher Education Transcript of Records - Digital Credential Specification**

## **Introduction**
The *Higher Education Transcript of Records* is a formal document issued by higher education institutions that provides a detailed account of the courses taken, grades obtained, and credits earned by a student. This document is crucial for student mobility and recognition within the *European Higher Education Area (EHEA)*.

This specification defines the data model for issuing the *Transcript of Records* as a verifiable digital credential, ensuring compliance with *Europass*, *ECTS*, and the *European Learning Model (ELM)*.


## **Data Model**

### **1. Credential Subject Information**
These fields identify the student to whom the transcript belongs.

| **Field**           | **ELM Object**  | **Subobject**        | **Comments** |
|--------------------|---------------|--------------------|-------------|
| **Date of birth**  | `elm:Person`  | `elm:dateOfBirth`  | Mandatory |
| **Family name**    | `elm:Person`  | `foaf:familyName`  | Mandatory |
| **Given name**     | `elm:Person`  | `foaf:givenName`   | Mandatory |
| **Personal identifier** | `elm:Person` | `elm:Person` | Optional, institutional/national identifier |


### **2. Institution and Study Programme Information**
These fields define the institution issuing the transcript and the programme followed.

| **Field**                                  | **ELM Object**                                    | **Subobject** | **Comments** |
|--------------------------------------------|-------------------------------------------------|-------------|-------------|
| **Name of tertiary education institution** | `elm:awardingBody, elm:Organisation, elm:LegalIdentifier` |  | Mandatory |
| **Name of study programme**                | `elm:LearningAchievementSpecification`         | `dc:title`  | Mandatory |


### **3. Course and Performance Details**
These fields describe the courses attended and the student's academic performance.

| **Field**                                  | **ELM Object**                           | **Subobject**         | **Comments** |
|--------------------------------------------|----------------------------------------|-------------------|-------------|
| **For each course**                        | `elm:hasPart`                          |                   | Mandatory |
| **Grade obtained for each attended course** | `elm:LearningAssessment`               | `elm:grade`        | Mandatory |
| **Name of each attended course**           | `elm:LearningAssessment`               | `dc:title`         | Mandatory |
| **ECTS credits obtained for each attended course** | `elm:creditReceived`            | `Credit Point`     | Mandatory |
| **Start date for each attended course**    | `elm:LearningOpportunity`              | `dc:PeriodOfTime`  | Optional |
| **End date for each attended course**      | `elm:LearningOpportunity`              | `dc:PeriodOfTime`  | Optional |


### **4. Grading System Information**
These fields provide details on the grading system used.

| **Field**                        | **ELM Object**              | **Subobject**         | **Comments** |
|----------------------------------|---------------------------|-------------------|-------------|
| **Grading Scale information**    | `elm:LearningAssessment`  | `elm:GradingScheme` | Mandatory |
| **Grade distribution**           | `elm:LearningAssessment`  | `elm:resultDistribution` | Optional |


## **Implementation Considerations**
- The *Transcript of Records* must be issued in a verifiable digital format to support student mobility and academic recognition within the *European Higher Education Area (EHEA)*.
- Institutions should align course credits with the *European Credit Transfer and Accumulation System (ECTS)* to facilitate international recognition.