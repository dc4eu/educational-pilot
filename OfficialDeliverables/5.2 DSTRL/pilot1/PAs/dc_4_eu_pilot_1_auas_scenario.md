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
  - EHIC issuance
  - Diploma issuance
  - Micocredential issuance
  - QR-based verification of all EAA's, including selective disclosure
- **Target groups and end-user roles**:
  - Students (approx. 25 pilot users)
  - Staff involved in credential management
- **Electronic Attestations of Attributes (EAAs) involved**:
  - PID
  - Diploma
  - Microcredential
  - EHIC
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
  - Weekly progress updates to WP5, filled in readyness tracker, filled in KPI results

---

## 3. Legal, Organisational and Operational Details

- **Regulatory context**:
  - GDPR compliance
  - Dutch higher education regulations
- **Risk management**:
  - availability/performance SaaS solution + effect on perceived reliability of wallet, feasability end-users for testsessions.
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
  324 educational credentials
- **Credentials verified**:\
  114 credentials verified in SaaS testenvironment (amount lower then amount issued, only because lack of time)
- **Successes**:
  - activating process wallet, Smooth issuance and verification process after initial hickups, functionality of verification for both student and institutions, positive about possibility of selective disclosure in verification process
- **Issues encountered**:
  - technical and user experience challenges (slow performance)
  - usability limited (lack of visual guidance)
- **Deviation from plan**:
  - delay in piloting with the result of cancelling 6 testsessions; adding EHIC; having to skip both EducationalID and revoking process of credentials as those services were not available

---

## 6. Testing Results and Observations

- **What worked as expected**:
  - after initial hickups, most features worked as planned: credential issuance, activating wallets, verification process, and selective disclosure in verif process (above expectations) within the SaaS environment of WP7
- **What did not work and why**:
  - revocation process did not work as it was not available in the interop lab, the same goes for EducationalID
- **Feedback from users**:
- Positive about simplicity, selective disclosure and the idea behind this testwallet.
- **Impact on user experience and feasibility**:
  - users recommending improvements in performance, clarity, and accessibility as they believe in the principle of the wwwallet and digital credentials

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
 - Improvements in performance and usability (fit for purpose) are essential to the success of EUDI-wallets. 
 - Recommendations for future pilots or replication: higher performance and UX-levels before starting testphase; planning testmaterials more timely. Changes proposed to methodology or components: improved survey end-users, based on industry standard questionnaires concerning UX.

---

## 9. Summary of End-User Feedback

- General impressions: Positive
- Ease of use: medium to high after initial hickups
- Challenges: None 
- Suggestions: Enable revoking of credentials; improve usability (tool-tips, explaining the ecosystem behind (what happens with my data, where am i in the process))
- Willingness to use again: Yes

---

## 10. Summary of Piloting Agent Insights

- Feedback: Support from SURF and WP7 was more then sufficient and quick
- Barriers: planning issues
- Lessons: testmaterials to be planned early
- Observed impact: Clear demonstration of issuance and verification process, including selective disclosure
- Recommendations: timely planning of testmaterials and environment

---

**Disclaimer**\
AUAS has performed all actions technically feasible within the Pilot1 SaaS environment provided by WP7. The limitations (e.g., lack of RP certificates) were outside AUAS's control.

