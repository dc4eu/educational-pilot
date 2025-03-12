# **Higher Education Diploma - Digital Credential Specification**

## **Introduction**
The *Higher Education Diploma* is a formal academic qualification issued by recognised higher education institutions. This credential must be verifiable, portable, and compliant with the *European Learning Model (ELM)*. It aligns with the *European Digital Credentials for Learning (EDC)* standard, ensuring compatibility across EU Member States and adherence to *Europass*, *EQF/NQF*, and *UNESCO* guidelines for Diploma Supplements.

This document defines the data model for issuing the *Higher Education Diploma* as a verifiable digital credential, specifying mandatory and optional fields.



## **Data Model**

### **1. Credential Subject Information**
These fields identify the diploma holder.

| **Field**               | **ELM Object** | **Subobject**          | **Comments** |
|-------------------------|---------------|------------------------|-------------|
| **Date of birth**       | `elm:Person`  | `elm:dateOfBirth`      | Mandatory |
| **Family name**         | `elm:Person`  | `foaf:familyName`      | Mandatory |
| **Given name**         | `elm:Person`  | `foaf:givenName`      | Mandatory |
| **Personal identifier** | `elm:Person`  | `elm:Person`          | Optional, institutional/national identifier |


### **2. Awarding Institution Information**
These fields define the institution responsible for issuing the diploma.

| **Field**                                        | **ELM Object**                                   | **Subobject** | **Comments** |
|--------------------------------------------------|-------------------------------------------------|-------------|-------------|
| **Name of awarding tertiary education institution** | `elm:awardingBody, elm:Organisation, elm:LegalIdentifier` |  | Mandatory |



### **3. Qualification Information**
These fields describe the diploma awarded.

| **Field**                                       | **ELM Object**                         | **Subobject**       | **Comments** |
|-------------------------------------------------|----------------------------------------|-------------------|-------------|
| **Name of qualification**                       | `elm:LearningAchievement`             | `dc:title`        | Mandatory |
| **Date of award of academic qualification**     | `elm:AwardingProcess`                 | `elm:awardingDate`| Mandatory |
| **Country of award of academic qualification**  | `dc:Location`                         |                   | Optional, defined according to EC/Europass/UNESCO guidelines for Diploma Supplement |
| **Overall classification of the academic qualification** | `elm:LearningAchievementSpecification` | `elm:Qualification` | Mandatory, aligned with EQF/NQF |
| **Name of qualification study field**           | `elm:LearningAchievementSpecification` | `elm:educationSubject` | Optional |
| **Degree project title**                        | `elm:LearningAchievementSpecification` | `elm:additionalNote` | Optional |



### **4. Entitlements and Additional Information**
These fields define any rights conferred by the diploma and optional information.

| **Field**             | **ELM Object**               | **Subobject**         | **Comments** |
|-----------------------|----------------------------|----------------------|-------------|
| **Entitlement**       | `elm:LearningEntitlement`  |                      | Optional (e.g., nursing qualification) |
| **Other information** | `elm:LearningAchievementSpecification` | `elm:additionalNote` | Optional |



## **Implementation Considerations**
- The *Higher Education Diploma* must be issued in a verifiable digital format, ensuring interoperability with European and international recognition frameworks.
- Institutions must align the classification of academic qualifications with the *European Qualifications Framework (EQF)* or *National Qualifications Frameworks (NQF)*.


