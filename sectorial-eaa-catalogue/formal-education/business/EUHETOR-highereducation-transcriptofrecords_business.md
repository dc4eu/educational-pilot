# **Higher Education Transcript of Records (EUHETOR) - Digital Credential Specification**

## Overview

The **European Higher Education Transcript of Records (EUHETOR)** is a digitally verifiable credential that presents an official summary of a student’s academic performance during a specific period of study. It includes detailed records of individual courses, grades obtained, credits earned, and institutional grading schemes. The EUHETOR facilitates academic mobility, supports recognition of learning achievements across borders, and aligns with the European Higher Education Area (ELM), Europass, and ECTS standards.

## Business Value

### For Higher Education Institutions:

- **Mobility Support**: Simplifies academic credit transfer and course recognition in Erasmus+ and joint degree contexts.
- **Quality Assurance and Interoperability**: Ensures alignment with ECTS, Europass, and Bologna Process transparency principles.
- **Digital Transformation**: Reduces administrative verification processes and supports student-oriented digital services.

### For Students:

- **Academic Mobility**: Empowers students to present verifiable records of coursework for international opportunities.
- **Clarity and Structure**: Includes course titles, grades, credit points, and grading system references in a standardised format.
- **Verification Control**: Allows students to manage and share their academic records through digital wallets.

### For Relying Parties (host institutions, employers, credential evaluators):

| **Benefit** | **Description** |
|-------------|-------------|
| **Trusted Record Access** | Enables direct access to official academic records for selection, recognition, and placement. |
| **Comparison Efficiency** | Standardised format facilitates quick understanding of academic progress and performance |
| **Reduced Fraud** | Digital signature and EBSI trust framework protect data integrity and authenticity. |

## Key Features

* **ELM-Aligned Structure**:
  * Identifies the student (name, date of birth in `date-time` format) and issuing institution (with `location`).
  * Includes programme and institutional metadata.
  * Captures individual courses, assessment results, ECTS credits, and period of study. |
  * Describes the grading scheme used and (optionally) the result distribution.
  * Includes `displayParameter` (e.g., language, format) and `credentialProfiles` (e.g., Europass).
* **Modular Course Records**:
  * Each course is represented as a structured unit within the transcript, with title, grade, credit point, and time frame.
* **Interoperable Digital Format**:
  * Issued as a JSON-LD verifiable Credential with types `VerifiableCredential`, `EuropeanDigitalCredential`, `EuropeanHigherEducationTranscriptOfRecords`, and `VerifiableAttestation`.
  * Digitally signed with JAdES D-Zero for secure transmission and validation.

## Use Cases

* **Erasmus+ and International Study Recognition**:
  A student applies to an Erasmus+ host university using their EUHETOR credential to confirm prior academic achievement.
* **Admission to Further Study**:
  Universities review a master’s application using previous academic records provided in EUHETOR format.
* **Employer Verification**:
  Employers confirm the scope and results of courses completed by candidates through a verifiable EUHETOR.

## Why EUHETOR Matters

In a digitally connected world, EUHETOR enables seamless, trustworthy exchange of academic progress data. It enhances transparency, streamlines recognition processes, and reinforces student agency in sharing their verified academic history. By aligning with European standards, it promotes comparability lyricism and ensures credibility of academic performance records.

## **Data Model**

### ELM-based Entity-Relationship Diagram

```mermaid
flowchart LR
    A["EUHETOR"] --> B["Credential Subject (Student)"]
    B --> C["Full Name"]
    B --> D["Date of Birth"]
    B --> E["Personal Identifier (optional)"]
    A --> F["Awarding Institution"]
    F --> G["Institution Name"]
    F --> H["Legal Identifier"]
    A --> I["Study Programme"]
    I --> J["Programme Title"]
    A --> K["Course Records"]
    K --> L["Course Title"]
    K --> M["Grade"]
    K --> N["Credit Points (ECTS)"]
    K --> O["Start Date"]
    K --> P["End Date"]
    A --> Q["Grading Scheme"]
    Q --> R["Grading Scale"]
    Q --> S["Grade Distribution (optional)"]
```

### **1. Credential Subject Information**
These fields identify the student to whom the transcript belongs.

| **Field**           | **ELM Object**  | **Subobject**        | **Comments** |
|--------------------|---------------|--------------------|-------------|
| **Date of birth**  | `elm:Person`  | `elm:dateOfBirth`  | Mandatory, in date-time format (e.g., 1998-01-01T00:00:00+00:00) |
| **Family name**    | `elm:Person`  | `foaf:familyName`  | Mandatory |
| **Given name**     | `elm:Person`  | `foaf:givenName`   | Mandatory |
| **Personal identifier** | `elm:Person` | `elm:Person` | Optional, institutional/national identifier |


### **2. Institution and Study Programme Information**
These fields define the institution issuing the transcript and the programme followed.

| **Field**                                  | **ELM Object**                                    | **Subobject** | **Comments** |
|--------------------------------------------|-------------------------------------------------|-------------|-------------|
| **Name of tertiary education institution** | `elm:awardingBody, elm:Organisation, elm:LegalIdentifier` | | Mandatory |
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


## Implementation Considerations

* Institutions should be synchronised with academic management systems.
* Courses must be aligned with ECTS standards.
* Grading schemes should be referenced transparently |
* EUHETOR credentials must be exportable and integrated with interoperable digital wallets and validation gateways.
* The credential includes displayParameter and credentialProfiles and for consistent rendering and interoperability.