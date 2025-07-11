# DC4EU Deployment and Testing Scenarios Results Library (DTSRL) – Scenario: Sikt (Norway)

## 1. Scenario Identification

- **Piloting agent name**: Sikt – Norwegian Agency for Shared Services in Education and Research
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
  - QR-based verification (limited to integrity checks)
- **Target groups and end-user roles**:
  - Students (approx. 25 pilot users)
  - Administrative staff
- **Electronic Attestations of Attributes (EAAs) involved**:
  - EducationalID
  - Diploma
- **Institutional systems/databases connected**:
  - None (credentials issued via remote SaaS platform)
- **Technical components used**:
  - **Pilot option**: Pilot1 (Classical PKI)
  - **SaaS environment**: SUNET/SURF test environment
  - **Wallet**: wwWallet
  - **Issuer platform**: SUNET/SURF SaaS Issuer
  - **Verifier platform**: SUNET/SURF SaaS Verifier (integrity verification only)
- **Governance configuration**:
  - **Trust model**: Classical PKI
  - **Issuer public key reference**:
    ```
    MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEi3v64MrIKoS9Aofws9Dg3Vd7Ej9ZMBUYJ8DuHxb2mNDiRbrmJ6KqdIsrXWRfzguJUceYWZuo8Fx6RVP+E7Muvg==
    ```
  - **Relying Party certificate**: Not available (cross-border RP verification was not implemented)
  - **Decentralised Identifiers (DIDs)**: Not applicable for Pilot1
- **Monitoring and feedback mechanisms**:
  - Scenario progress tracked via Sikt project management tools and weekly updates to DC4EU WP5

---

## 3. Legal, Organisational and Operational Details

- **Regulatory context**:
  - GDPR compliance
  - Norwegian regulations for educational data processing
- **Risk management**:
  - Limited credential lifecycle (revocation out of scope)
  - No cross-border trust verification
- **Credential lifecycle management**:
  - Revocation: Not implemented (functionality not provided by WP7)
  - Suspension: Not implemented (functionality not provided by WP7)
- **Infrastructure readiness**:
  - Remote SaaS environment provisioned by SUNET/SURF
- **Training and onboarding**:
  - Approx. 3 staff trained on wallet usage and issuance workflows
- **Issue escalation**:
  - SPOC contact: SURF
- **Success indicators and KPIs**:
  - Number of credentials issued: target 25
  - User feedback on wallet usability

---

## 4. Trust Model Onboarding Evidences

- **Issuer public key reference**:
  ```
  MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEi3v64MrIKoS9Aofws9Dg3Vd7Ej9ZMBUYJ8DuHxb2mNDiRbrmJ6KqdIsrXWRfzguJUceYWZuo8Fx6RVP+E7Muvg==
  ```
- **Relying Party certificate**: Not applicable (not provided by WP7)
- **Decentralised Identifiers (DIDs)**: Not applicable
- **Registry references**: Not applicable (Classical PKI only)

---

## 5. Implementation and Testing Progress

- **Scenario status**: Completed
- **Number of users onboarded**:\
  25 students
- **Credentials issued**:\
  25 EducationalID credentials and 25 Diplomas (SD-JWT)
- **Credentials verified**:\
  Verification limited to local integrity checks (no full trust chain validation)
- **Successes**:
  - Successful wallet installation and credential issuance
- **Issues encountered**:
  - No RP certificate available, preventing full verification
- **Deviation from plan**:
  - Partial testing of verification flows only

---

## 6. Testing Results and Observations

- **What worked as expected**:
  - Issuance of credentials from SaaS
  - Wallet storage and display
- **What did not work and why**:
  - No RP certificate provisioned by WP7
- **Feedback from users**:
  - Positive regarding ease of credential receipt
- **Impact on user experience and feasibility**:
  - Limited without cross-border verification

---

## 7. Evidence Archive and References

- **Screenshots or logs**:\
  [To be attached]
- **Links to SaaS environment or dashboards**:\
  [SUNET/SURF test environment URL]
- **Documents or repositories**:
  - Pilot1 SaaS infrastructure description
  - Pilot1 user journeys
- **KPI data submission details**:\
  Weekly updates to WP5 team

---

## 8. Next Steps and Recommendations

- **Pending actions**:
  - None
- **Recommendations**:
  - Future pilots should prioritise cross-border verification readiness and availability of RP certificates

---

## 9. Summary of End-User Feedback

- General impressions:\
  Positive overall
- Ease of use of wallet or platform:\
  High
- Challenges encountered:\
  None reported in issuance
- Suggestions for improvement:\
  Enable verification capabilities
- Willingness to use again:\
  Yes

---

## 10. Summary of Piloting Agent Insights

- Feedback on support received:\
  Good support from SUNET/SURF and WP7
- Main barriers during implementation:\
  Relying party certificate availability
- Lessons learned:\
  Early provisioning of verification certificates essential
- Observed impact and value:\
  Clear demonstration of issuance process
- Recommendations for scaling:\
  Clarify cross-border verification flows early

---

**Disclaimer**\
Sikt has performed all actions that were technically and operationally feasible within the scope of the Pilot1 SaaS environment provided by WP7. The limitations described (e.g., lack of RP certificates and lifecycle management) were due to constraints of the WP7-provided infrastructure and were not under the control of Sikt.

