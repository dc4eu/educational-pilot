# DC4EU Deployment and Testing Scenarios Results Library (DTSRL) – Scenario: DTU (Denmark)

## 1. Scenario Identification

- **Piloting agent name**: Danmarks Tekniske Universitet (DTU)
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
  - University administrative staff
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
  - Weekly updates to DC4EU WP5

---

## 3. Legal, Organisational and Operational Details

- **Regulatory context**:
  - GDPR compliance
  - Danish education regulations
- **Risk management**:
  - Lifecycle out of scope
  - No cross-border verification
- **Credential lifecycle management**:
  - Revocation: Not implemented (not provided by WP7)
  - Suspension: Not implemented (not provided by WP7)
- **Infrastructure readiness**:
  - SaaS environment provisioned
- **Training and onboarding**:
  - Approx. 3 staff trained
- **Issue escalation**:
  - SPOC contact: SURF
- **Success indicators and KPIs**:
  - Target issuance: 25 credentials

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
  25 students
- **Credentials issued**:\
  25 EducationalIDs and 25 Diplomas
- **Credentials verified**:\
  Integrity checks only
- **Successes**:
  - Issuance workflow successfully demonstrated
- **Issues encountered**:
  - No RP certificate provisioned
- **Deviation from plan**:
  - Partial verification coverage

---

## 6. Testing Results and Observations

- **What worked as expected**:
  - Credential issuance
- **What did not work and why**:
  - No cross-border verification (infrastructure limitation)
- **Feedback from users**:
  - Positive about wallet experience
- **Impact on user experience and feasibility**:
  - Verification limited to integrity check

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
  - Early provision of RP certificates in future pilots

---

## 9. Summary of End-User Feedback

- General impressions: Positive
- Ease of use: High
- Challenges: None reported
- Suggestions: Enable full verification capabilities
- Willingness to use again: Yes

---

## 10. Summary of Piloting Agent Insights

- Feedback: Support from SURF was adequate
- Barriers: No RP certificate
- Lessons: Verification scope must be confirmed early
- Observed impact: Successful demonstration of issuance
- Recommendations: Ensure verification infrastructure readiness

---

**Disclaimer**\
DTU has performed all actions technically feasible within the Pilot1 SaaS provided by WP7. Limitations (e.g., no RP certificates) were outside DTU's control.

