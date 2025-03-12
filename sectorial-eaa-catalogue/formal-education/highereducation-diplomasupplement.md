# **Higher Education Diploma Supplement - Digital Credential Specification**

## **Introduction**
The *Higher Education Diploma Supplement* is an official document issued alongside a diploma to provide additional details about the qualification, its level, content, and the national education system. It facilitates academic and professional recognition within the *European Higher Education Area (EHEA)*.

This document defines the data model for issuing the *Higher Education Diploma Supplement* as a verifiable digital credential, specifying mandatory and optional fields in alignment with *Europass*, *EQF/NQF*, and *UNESCO Diploma Supplement* guidelines.


## **Data Model**

### **1. Credential Subject Information**
These fields identify the diploma holder.

| **Field**                           | **ELM Object**  | **Subobject**         | **Comments** |
|-------------------------------------|---------------|----------------------|-------------|
| **Family name**                     | `elm:Person`  | `foaf:familyName`    | Mandatory |
| **Given name**                      | `elm:Person`  | `foaf:givenName`     | Mandatory |
| **Date of birth**                    | `elm:Person`  | `elm:dateOfBirth`    | Mandatory |
| **Student identification number**   | `elm:Person`  | `elm:Person`         | Optional, institutional/national identifier |


### **2. Qualification and Awarding Institution Information**
These fields define the awarded qualification and the institution responsible.

| **Field**                                        | **ELM Object**                                   | **Subobject**        | **Comments** |
|-------------------------------------------------|-------------------------------------------------|---------------------|-------------|
| **Name of Qualification**                       | `elm:LearningAchievement`                      | `dc:title`          | Mandatory |
| **Main field(s) of study for the qualification** | `elm:LearningAchievementSpecification`         | `elm:educationSubject` | Mandatory |
| **Name of education institution administering the studies** | `elm:awardingBody, elm:Organisation, elm:LegalIdentifier` | | Mandatory |
| **Status of awarding education institution**     | `elm:LearningAssessmentSpecification`          | `elm:additionalNote` | Mandatory |
| **Status of education institution administering the studies** | `elm:LearningAssessmentSpecification`          | `elm:additionalNote` | Mandatory |
| **Language(s) of instruction**                   | `elm:LearningOpportunity`                      | `elm:defaultLanguage` | Mandatory |


### **3. Qualification Level and Study Programme Details**
These fields describe the qualification's level and duration.

| **Field**                                      | **ELM Object**                           | **Subobject**    | **Comments** |
|-----------------------------------------------|----------------------------------------|---------------|-------------|
| **EQF level of the academic qualification**  | `elm:LearningAchievementSpecification` | `elm:Qualification` | Mandatory |
| **NQF level of the academic qualification**  | `elm:LearningAchievementSpecification` | `elm:Qualification` | Mandatory |
| **Study programme (official) duration**      | `elm:LearningOpportunity`               | `elm:duration` | Mandatory |


### **4. Study Programme and Course Details**
These fields detail the mode of study and individual courses within the diploma.

| **Field**                                  | **ELM Object**                           | **Subobject**        | **Comments** |
|-------------------------------------------|----------------------------------------|-------------------|-------------|
| **Mode of study**                         | `elm:LearningAchievementSpecification` | `elm:mode`         | Mandatory |
| **For each course in the diploma**        | `elm:hasPart`                          |                   | Mandatory |
| **Dates of each attended course**         | `elm:LearningOpportunity`               | `dc:PeriodOfTime`  | Mandatory |
| **ECTS credits obtained for each course** | `elm:creditReceived`                    | `Credit Point`     | Mandatory |
| **Grade obtained for each attended course** | `elm:LearningAssessment`               | `elm:grade`        | Mandatory |
| **Name of each attended course**          | `elm:LearningAssessment`               | `dc:title`         | Mandatory |
| **Name of study programme**               | `elm:LearningAchievementSpecification` | `dc:title`         | Mandatory |
| **Study programme duration (in ECTS credits)** | `elm:LearningAchievementSpecification` | `elm:creditPoint` | Mandatory |
| **Grade distribution guidance**           | `elm:LearningAssessment`               | `elm:resultDistribution` | Mandatory |
| **Grading system**                        | `elm:LearningAssessment`               | `elm:GradingScheme` | Mandatory |
| **Overall classification of the academic qualification** | `elm:GradingScheme` | | Mandatory |


### **5. Access to Further Studies and Regulated Professions**
These fields define whether the qualification grants access to further studies or regulated professions.

| **Field**                           | **ELM Object**                      | **Subobject**           | **Comments** |
|-------------------------------------|-----------------------------------|---------------------|-------------|
| **Access to further studies**      | `elm:LearningEntitlementSpecification` | `elm:additionalNote` | Mandatory |
| **Access to a regulated profession** | `elm:LearningEntitlementSpecification` | `elm:limitNationalOccupation` | Mandatory |


### **6. Additional Information**
These fields provide complementary details about the qualification.

| **Field**                          | **ELM Object**                          | **Subobject**        | **Comments** |
|------------------------------------|---------------------------------------|-------------------|-------------|
| **Additional information**         | `elm:LearningAchievementSpecification` | `elm:additionalNote` | Mandatory |
| **Further information sources**    | `elm:LearningAchievementSpecification` | `elm:additionalNote` | Mandatory |


### **7. Awarding Process**
These fields define the official awarding details.

| **Field**                             | **ELM Object**          | **Subobject**    | **Comments** |
|--------------------------------------|----------------------|---------------|-------------|
| **Date of award of academic qualification** | `elm:AwardingProcess` | `elm:awardingDate` | Mandatory |
| **Name of tertiary education institution** | `elm:awardingBody, elm:Organisation, elm:LegalIdentifier` | `elm:awardedBy` | Mandatory |


### **8. National Higher Education System**
This field provides an overview of the national system for understanding the qualification's context.

| **Field**                                           | **ELM Object**                           | **Subobject**        | **Comments** |
|-----------------------------------------------------|----------------------------------------|-------------------|-------------|
| **Information about the national higher education system** | `elm:LearningAchievementSpecification` | `elm:additionalNote` | Mandatory |


## **Implementation Considerations**
- The *Higher Education Diploma Supplement* must be issued in a verifiable digital format to support recognition across *EU Member States*.
- Institutions should align the qualification levels with *European Qualifications Framework (EQF)* and *National Qualifications Frameworks (NQF)*.
