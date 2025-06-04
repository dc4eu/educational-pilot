# European Vocational Education and Training Microcredential (EUVETMC)

## Overview
The European Vocational Education and Training Microcredential (EUVETMC) is a standardized, digitally verifiable credential certifying short, focused learning outcomes within the European VET ecosystem. Built on the European Learning Model (ELM) 3.2 and aligned with the European Blockchain Services Infrastructure (EBSI), EUVETMC enables VET providers, learners, and employers to share, verify, and leverage vocational skills in a secure, interoperable, and trusted manner.

EUVETMC microcredentials are issued by accredited VET providers (e.g., vocational schools, training centers, or Centres of Vocational Excellence) and are designed to meet labor market demands, support lifelong learning, and facilitate transitions to green and digital economies.

## Business Value
EUVETMC provides significant benefits for stakeholders in the VET and employment sectors:

### For VET Providers:
* **Market Relevance**: Offer targeted training programs (e.g., green skills, digital competences) that attract learners and align with regional skills ecosystems.
* **Revenue Opportunities**: Develop microcredentials as standalone courses or stackable components, creating new funding streams via vouchers or Erasmus+.
* **International Recognition**: Leverage EBSI’s interoperability for credentials recognized across EU member states, enhancing provider reputation.

### For Learners:
* **Employability**: Gain certified skills (e.g., welding, IT support) from trusted providers, improving job prospects and career mobility.
* **Flexibility**: Complete short, work-based or school-based modules (1–15 ECVET points) that fit work schedules, with stackable options toward qualifications.
* **Portability**: Store and share credentials via Europass digital wallets, ensuring employer verification across borders.

### For Employers:
* **Skilled Workforce**: Access candidates with verified, job-specific skills, reducing hiring risks and addressing skills shortages.
* **Upskilling**: Partner with VET providers to create tailored microcredentials for employee training, addressing green and digital transitions.
* **Efficiency**: Verify credentials instantly via EBSI, eliminating fraud and streamlining recruitment.

## Key Features
- **Standardized Structure**: EUVETMC adheres to ELM 3.2, including:
  * A Person (learner) with name, surname, and date of birth (in `date-time` format).
  * At least one Learning Achievement (e.g., completed training) and Learning Assessment (e.g., practical test) with `provenBy` (including `awardedBy`).
  * A Learning Outcome with at least one Competence and optional ESCO skills for labor market alignment.
  * Credits (1–15 ECVET points) with location of awarding, ensuring measurable vocational value.
  * Includes `displayParameter` (e.g., language, format) and `credentialProfiles` (e.g., Europass).
- **Digital and Verifiable**: Issued as JSON-LD Verifiable Credentials with types `VerifiableCredential`, `EuropeanDigitalCredential`, `EuropeanVocationalEducationTrainingMicrocredential`, and `VerifiableAttestation`.
- **Interoperability**: Recognized across EU member states via EBSI and Europass.
- **Quality Assurance**: Aligned with EQAVET framework, ensuring trust and credibility.
- **Flexibility**: Supports work-based learning, apprenticeships, and continuing VET (C-VET).

## Use Cases
* **Work-Based Learning**:  
  A learner completes a 5-ECVET EUVETMC in “Renewable Energy Installation” from a VET center, earning a credential that qualifies them for green energy roles.
* **Upskilling**:  
  A company partners with a VET provider to offer EUVETMC in cybersecurity, enabling employees to gain certified skills, verified by HR via EBSI.
* **Apprenticeship Pathways**:  
  An apprentice earns multiple EUVETMC microcredentials (e.g., 3 ECVET each) that stack toward a full VET qualification, reducing training time.
* **International Mobility**:  
  A learner from Croatia presents an EUVETMC to a German employer, who verifies it via EBSI, ensuring trust in the candidate’s skills.

## Why EUVETMC Matters
EUVETMC addresses the need for agile, market-relevant vocational training in a rapidly changing economy. It empowers VET providers to deliver flexible, high-quality education, equips learners with portable skills, and enables employers to address skills gaps efficiently. By leveraging EBSI and EQAVET, EUVETMC ensures trust, scalability, and alignment with the green and digital transitions.

## **Data Model**

### **ELM-based Entity-Relationship Diagram**
```mermaid
flowchart LR
    A["EUVETMC"] --> B["Learning Achievement<br>(mandatory, min 1)"]
    A --> D["Issuer<br>(mandatory)"]
    A --> E["Quality Assurance<br>(mandatory, EQAVET)"]
    A --> F["Issuer Country<br>(mandatory)"]
    B --> G["Learning Outcomes<br>(mandatory, min 1)"]
    B --> H["ECVET"] Points<br>(mandatory, 1–15)"]
    B --> I["Level<br>(mandatory, EQF)"]
    B --> J["Learning Setting<br>(mandatory, e.g., work-based)"]
    B --> K["Stackability<br>(optional)"]
    B --> C["Learning Assessment<br>(mandatory, min 1)"]
    C --> L["Assessment Type<br>(mandatory, e.g., practical)"]
    G --> M["Competencies<br>(mandatory, min 1)"]
    G --> N["ESCO Skills<br>(optional)"]
```

### 1. Credential Subject Information

|Field	|ELM Object	|Subobject	|Comments|
|Date of birth	|elm:Person	|elm:dateOfBirth	|Mandatory, in date-time format (e.g., 1998-01-01T00:00:00+00:00)|
|Family name	|elm:Person	|foaf:familyName	|Mandatory|
|Given name	|elm:Person	|foaf:givenName	|Mandatory|
|Personal identifier	|elm:Person	|elm:Person	|Optional, typically national ID|

### 2. Awarding Institution Information

|Field	|ELM Object	|Subobject	|Comments|
|Name of awarding institution	|elm:awardingBody, elm:Organisation, elm:LegalIdentifier|	elm:awardedBy	|Mandatory, includes location (e.g., country)|

### 3. Microcredential Information

|Field	|ELM Object	|Subobject	|Comments|
|Name of Microcredential	|elm:LearningAchievement	|dc:title	|Mandatory|
|Date of award of Microcredential	|elm:AwardingProcess	|elm:awardingDate	|Mandatory, in date-time format|
|Country of award	|dc:Location|	|	|Mandatory|
|Overall classification	|elm:LearningAchievementSpecification	|elm:Qualification	|Mandatory, EQF|
|Main field of study	|elm:LearningAchievementSpecification	|elm:educationSubject	|Mandatory|
|Workload (ECVET points)	|elm:LearningAchievementSpecification	|elm:creditPoint	|Mandatory|
|Learning setting	|elm:LearningAchievementSpecification	|elm:mode	|Mandatory, e.g., work-based|

### 4. Learning Activities

|Field	|ELM Object	|Subobject	|Comments|
|Name of learning activity	|elm:LearningOpportunity	|dc:title	|Mandatory|
|Start date	|elm:LearningOpportunity	|dc:PeriodOfTime	|Mandatory|
|End date	|elm:LearningOpportunity	|dc:PeriodOfTime	|Mandatory|
|Workload in hours	|elm:LearningOpportunity	|elm:duration	|Mandatory|

### 5. Learning Outcomes

|Field	|ELM Object	|Subobject	|Comments|
|Title of learning outcome	|elm:LearningOutcome	|dc:title	|Mandatory|
|ESCO competencies	|elm:LearningOutcome	|elm:competence	|Mandatory, includes provenBy with awardedBy|

### 6. Assessment

|Field	|ELM Object	|Subobject	|Comments|
|Assessment type	|elm:LearningAssessment	|elm:grade	|Mandatory, e.g., practical test|
|Assessment method	|elm:LearningAssessment	|elm:mode	|Mandatory|
|Grading scheme	|elm:LearningAssessment	|elm:GradingScheme	|Mandatory|

### 7. Entitlement

|Field	|ELM Object	|Subobject	|Comments|
|Entitlement type	|elm:LearningEntitlement		|Optional, e.g., professional certification|
|Jurisdiction	|elm:LearningEntitlement	|elm:limitNationalOccupation	|Optional|


### Implementation Consideration
* The credential should be issued in a verifiable digital format, ensuring interoperability with European and international recognition frameworks.
* The credential includes displayParameter and credentialProfiles for consistent rendering and verification.