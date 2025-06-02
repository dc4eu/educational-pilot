---
country: Italy
pilot: Pilot 2
---

# University of Bologna (UNIBO) - Pilot 2 - Combined dPKI (EBSI) & classical PKI (Trust Lists)

## Scenario Description

The University of Bologna (UNIBO) scenario involves digital credential implementation focusing on education onboarding, academic achievement issuance, and verification of educational attestations. UNIBO intends to pilot this scenario initially with 25 final-year undergraduate students, using tools and services from Pilot 2 provided by IZERTIS.

## Key Steps per User Journey

### 1. Onboarding in Education
- Select 25 final-year undergraduate students.
- Conduct initial basic training covering eIDAS2, PID, EAAs, the DC4EU framework, and the significance of the EUDIW.
- Ensure each student obtains and configures the EUDIW wallet provided by IZERTIS.
- Individually verify each student's identity, providing access credentials for PID retrieval.
- Guide students through the PID retrieval process, ensuring wallets are fully operational.
- Students carry out the "EducationalID request" validated through the presentation and verification of PID.
- Successful validation results in issuance of EducationalID, officially confirming the student's affiliation with UNIBO.

### 2. Educational Achievement Issuance
- Students who completed onboarding request academic achievements issuance.
- Students utilise their EducationalID in the EUDIW wallet to securely access an achievement request portal.
- System executes identity matching against institutional academic databases to provide a personalised list of available achievements.
- Students select and confirm achievements for issuance as Electronic Attestations of Attributes (EAA).
- After final confirmation, the selected EAAs are issued, accepted by students, and securely stored in their EUDIW wallets.

### 3. Generic EAA Verification
- Public verification service accessible for holders of educational EAAs stored in EUDIW.
- Users present their educational EAA, selecting from sectoral catalogues via the EUDIW wallet.
- The system verifies the presented EAA's integrity and compliance with governance criteria.
- The verification process includes validation of issuer legitimacy, appropriate identification of the education issuer, and confirmation of authorisation from educational governance authorities.
- Upon successful verification, confirmation of EAA validity and authenticity is provided.

## Scenario Details

| Element                                   | Description                                                                                                  |
|-------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| **Scenario Name**                         | Digital credentials in higher education – UNIBO                                                              |
| **Piloting Agent**                        | University of Bologna (UNIBO), Italy                                                                         |
| **User Journeys Covered**                 | 1. Onboarding in education<br>2. Educational achievement issuance<br>3. Generic EAA verification             |
| **End Users Identification**              | 25 final-year undergraduate students from UNIBO                                                              |
| **EAAs Involved**                         | PID, EducationalID, Educational Achievement (EAA)                                                            |
| **Institutional Systems Involved**        | UNIBO academic databases, institutional identity verification systems                                        |
| **Technical Components**                  | Issuer (ATOS), verifier (ATOS), wallet (EUDIW by IZERTIS), PID retrieval services                            |
| **Governance Setup**                      | DID issuance and registration, authorisation templates, trust registrations                                  |
| **Feedback & Monitoring Mechanism**       | Online surveys, KPI-based weekly monitoring reports managed by SPOC                                          |
| **Regulatory Context**                    | GDPR compliance, Italian national regulations, eIDAS2 regulations                                            |
| **Risk Management Considerations**        | Risks of incorrect identity matching (medium/high) mitigated through robust verification; user confusion (medium/medium) mitigated through training and support |
| **Credential Lifecycle Management**       | Established procedures for credential issuance, updating, renewal, revocation, and suspension                |
| **Infrastructure Readiness**              | Institutional authentication systems, integrated endpoints with ATOS and IZERTIS, secure databases, compliant hardware/software |
| **Onboarding and Training Plan**          | Structured basic training covering eIDAS2, PID, EAAs, DC4EU, and EUDIW; practical PID retrieval and wallet setup guidance |
| **Progress Tracking and Reporting Plan**  | Weekly reporting and KPI tracking through DC4EU structured templates                                         |
| **Issue Escalation Procedure**            | Clearly defined escalation via SPOC contacts with documented response times and resolution protocols         |
| **Success Metrics and KPIs**              | Onboarding completion rate, EAA issuance success rate, verification success rate, user satisfaction scores   |
| **SPOC Contact and Validation Status**    | Assigned SPOC contact; scenario validation pending initial review                                            |
