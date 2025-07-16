# DC4EU Deployment and Testing Scenarios Results Library (DTSRL) – Scenario: Amsterdam University of Applied Sciences (AUAS)

## 1. Scenario Identification

- **Piloting agent name**: Amsterdam University of Applied Sciences (AUAS)
- **Scenario title**: Educational Credential Issuance and Verification with SUNET/SURF SaaS (Classical PKI)
- **Date of submission**: 1 July 2025
- **Point of contact (SPOC)**: SURF

---

## 2. Scenario Characterisation

- **User journeys implemented**:
  - Wallet installation
  - PID issuance (SD-JWT)
  - EducationalID issuance
  - Diploma issuance
  - QR-based verification (integrity checks only)
- **Target groups and end-user roles**:
  - Students (approx. 25 pilot users)
  - Staff involved in credential management
- **Electronic Attestations of Attributes (EAAs) involved**:
  - EducationalID
  - Diploma
- **Institutional systems/databases connected**:
  - None (remote SaaS issuance)
- **Technical components used**:
  - **Pilot option**: Pilot1 (Classical PKI)
  - **SaaS environment**: SUNET/SURF test environment
  - **Wallet**: wwWallet
  - **Issuer platform**: SUNET/SURF SaaS Issuer
  - **Verifier platform**: SUNET/SURF SaaS Verifier
- **Governance configuration**:
  - **Trust model**: Classical PKI
  - **Issuer public key reference**:
    ```
    MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEi3v64MrIKoS9Aofws9Dg3Vd7Ej9ZMBUYJ8DuHxb2mNDiRbrmJ6KqdIsrXWRfzguJUceYWZuo8Fx6RVP+E7Muvg==
    ```
  - **Relying Party certificate**: Not available (cross-border verification not implemented)
  - **Decentralised Identifiers (DIDs)**: Not applicable
- **Monitoring and feedback mechanisms**:
  - Weekly progress updates to WP5

---

## 3. Legal, Organisational and Operational Details

- **Regulatory context**:
  - GDPR compliance
  - Dutch higher education regulations
- **Risk management**:
  - Lifecycle out of scope
  - No cross-border verification
- **Credential lifecycle management**:
  - Revocation: Not implemented (not provided by WP7)
  - Suspension: Not implemented (not provided by WP7)
- **Infrastructure readiness**:
  - SaaS environment provided by SURF/SUNET
- **Training and onboarding**:
  - Approx. 3 staff trained
- **Issue escalation**:
  - SPOC contact: SURF
- **Success indicators and KPIs**:
  - Issuance target: 25 credentials

---

## 4. Trust Model Onboarding Evidences

- **Issuer public key reference**:
  ```
  MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEi3v64MrIKoS9Aofws9Dg3Vd7Ej9ZMBUYJ8DuHxb2mNDiRbrmJ6KqdIsrXWRfzguJUceYWZuo8Fx6RVP+E7Muvg==
  ```
- **Relying Party certificate**: Not applicable
- **Decentralised Identifiers (DIDs)**: Not applicable
- **Registry references**: Not applicable

---

## 5. Implementation and Testing Progress

- **Scenario status**: Completed
- **Number of users onboarded**:\
  53 students
- **Credentials issued**:\
  224 educational credentials
- **Credentials verified**:\
  114 Integrity checks only
- **Successes**:
  - Smooth issuance process
- **Issues encountered**:
  - No RP certificate provisioned
- **Deviation from plan**:
  - Verification limited to integrity checks

---

## 6. Testing Results and Observations

- **What worked as expected**:
  - Credential issuance
- **What did not work and why**:
  - No cross-border verification due to lack of RP certificates
- **Feedback from users**:
  - Positive about simplicity
- **Impact on user experience and feasibility**:
  - Verification limited

---

## 7. Evidence Archive and References

- **Screenshots or logs**:\
  [To be attached]
- **Links to dashboards**:\
  [SUNET/SURF test environment]
- **Documents**:
  - Pilot1 infrastructure
- **KPI submission**:\
  Weekly reports

---

## 8. Next Steps and Recommendations

- **Pending actions**:\
  None
- **Recommendations**:
  - Ensure RP certificates are available in future pilots

---

## 9. Summary of End-User Feedback

- General impressions: Positive
- Ease of use: High
- Challenges: None reported
- Suggestions: Enable full verification
- Willingness to use again: Yes

---

## 10. Summary of Piloting Agent Insights

- Feedback: Support from SURF was sufficient
- Barriers: No RP certificate available
- Lessons: Verification scope to be planned early
- Observed impact: Clear demonstration of issuance
- Recommendations: Clarify verification requirements at start

---

**Disclaimer**\
AUAS has performed all actions technically feasible within the Pilot1 SaaS environment provided by WP7. The limitations (e.g., lack of RP certificates) were outside AUAS's control.

