# **Upper Secondary Education Transcript of Records - Digital Credential Specification**

## **Introduction**
The *Upper Secondary Education Transcript of Records* is an official document issued by secondary education institutions that provides a detailed account of the courses attended, grades obtained, and workload or credits earned by a student. It supports recognition, mobility, and academic progression within the *European Education Area (EEA)*.

This specification defines the data model for issuing the *Transcript of Records* as a verifiable digital credential, ensuring compliance with *Europass* and the *European Learning Model (ELM)*.


## **Data Model**

### **1. Credential Subject Information**
These fields identify the student to whom the transcript belongs.

| **Field**           | **ELM Object**  | **Subobject**        | **Comments** |
|-------------------|---------------|--------------------|-------------|
| **Date of birth** | `elm:Person`  | `elm:dateOfBirth`  | Mandatory |
| **Given name**    | `elm:Person`  | `foaf:givenName`   | Mandatory |
| **Family name**   | `elm:Person`  | `foaf:familyName`  | Mandatory |
| **Personal identifier** | `elm:Person` | `elm:Person` | Optional, institutional/national identifier |


### **2. Institution and Study Programme Information**
These fields define the secondary education institution issuing the transcript.

| **Field**                                     | **ELM Object**                                    | **Subobject** | **Comments** |
|-----------------------------------------------|-------------------------------------------------|-------------|-------------|
| **Name of secondary education institution**  | `elm:awardingBody, elm:Organisation, elm:LegalIdentifier` |  | Mandatory |


### **3. Course and Performance Details**
These fields describe the courses attended and the student's academic performance.

| **Field**                                  | **ELM Object**                           | **Subobject**         | **Comments** |
|--------------------------------------------|----------------------------------------|-------------------|-------------|
| **Dates of each attended course**         | `elm:LearningOpportunity`              | `dc:PeriodOfTime`  | Mandatory |
| **Grade obtained for each attended course** | `elm:LearningAssessment`               | `elm:grade`        | Mandatory |
| **Name of each attended course**          | `elm:LearningAssessment`               | `dc:title`         | Mandatory |
| **Grading scheme description**            | `elm:LearningAssessment`               | `elm:GradingScheme` | Mandatory |
| **Workload, credits**                      | `elm:LearningAchievementSpecification` | `elm:creditPoint` | Mandatory |


## **Implementation Considerations**
- The *Upper Secondary Education Transcript of Records* must be issued in a verifiable digital format to support student mobility and academic progression within the *European Education Area (EEA)*.
- Institutions should ensure that the workload or credits are aligned with national education frameworks and compatible with the *European Qualifications Framework (EQF)*.