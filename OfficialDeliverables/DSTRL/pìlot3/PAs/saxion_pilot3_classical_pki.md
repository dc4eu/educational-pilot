# DC4EU Deployment and Testing Scenarios Results Library (DTSRL) – Scenario: Saxion University of Applied Sciences - Classical PKI

## 1. Scenario Identification

- **Piloting agent name**: Saxion University of Applied Sciences (SAXION)
- **Scenario title**: Applied Sciences Credential Issuance with SUNET/SURF SaaS (Classical PKI)
- **Date of submission**: 11 July 2025
- **Point of contact (SPOC)**: Franco de Vitta

---

## 2. Scenario Characterisation

- **User journeys implemented**:
  Wallet installation, PID issuance (SD-JWT), EducationalID issuance, Diploma issuance, QR-based verification (integrity checks only)
- **Target groups and end-user roles**:
  Applied sciences students (approx. 25 pilot users), professional programme graduates, administrative staff
- **Electronic Attestations of Attributes (EAAs) involved**:
  EducationalID, Diploma
- **Institutional systems/databases connected**:
  None (credentials issued via SUNET/SURF SaaS platform)
- **Technical components used**:
  - **Pilot option**: Pilot3-ClassicalPKI (Combined approach - Classical PKI component)
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
  - **Relying Party certificate**: Not available (cross-border RP verification not implemented)
  - **Decentralised Identifiers (DIDs)**: Not applicable for Pilot3-ClassicalPKI
- **Monitoring and feedback mechanisms**:
  Weekly progress reports tracked via Saxion project management tools and regular updates to DC4EU WP5

---

## 3. Legal, Organisational and Operational Details

- **Regulatory context**:
  - GDPR compliance
  - Dutch national applied sciences education regulations
  - Professional qualifications regulatory requirements
- **Risk management**:
  Limited credential lifecycle (revocation out of scope for Classical PKI component), no cross-border trust verification for professional credentials
- **Credential lifecycle management**:
  - Revocation: Not implemented (functionality not provided by WP7 for Classical PKI)
  - Suspension: Not implemented (functionality not provided by WP7 for Classical PKI)
- **Infrastructure readiness**:
  Remote SUNET/SURF SaaS environment provisioned for applied sciences use cases
- **Training and onboarding**:
  Approximately 3 applied sciences staff trained on wwWallet usage and Classical PKI issuance workflows for professional programmes
- **Issue escalation**:
  SPOC contact: Franco de Vitta, with escalation to SUNET/SURF support
- **Success indicators and KPIs**:
  Number of applied sciences credentials issued: target 25, user feedback on wwWallet usability for professional education contexts

---

## 4. Trust Model Onboarding Evidences

- **Issuer public key reference**:
  ```
  MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEi3v64MrIKoS9Aofws9Dg3Vd7Ej9ZMBUYJ8DuHxb2mNDiRbrmJ6KqdIsrXWRfzguJUceYWZuo8Fx6RVP+E7Muvg==
  ```
- **Relying Party certificate**: Not applicable (not provided by WP7 for Classical PKI implementation)
- **Decentralised Identifiers (DIDs)**: Not applicable for Classical PKI approach
- **Registry references**: Not applicable (Classical PKI only)

---

## 5. Implementation and Testing Progress

- **Scenario status**: Completed
- **Number of users onboarded**: 30 applied sciences students and professional programme participants
- **Credentials issued**: 120 Educational credentials (SD-JWT format)
- **Credentials verified**: Verification limited to local integrity checks (no full trust chain validation due to Classical PKI infrastructure limitations)
- **Successes**:
  - Successful wwWallet installation and applied sciences credential issuance
  - Effective demonstration of Classical PKI approach for professional education
- **Issues encountered**:
  - No RP certificate available for Classical PKI, preventing full cross-border verification of professional qualifications
- **Deviation from plan**:
  - Partial testing of verification flows only for applied sciences credentials

---

## 6. Testing Results and Observations

- **What worked as expected**:
  - Applied sciences credential issuance from SUNET/SURF SaaS
  - wwWallet storage and display of professional qualifications
  - SD-JWT format compatibility with applied sciences requirements
- **What did not work and why**:
  - No RP certificate provisioned by WP7 for Classical PKI trust chain validation
  - Cross-border verification of professional qualifications limited
- **Feedback from users**:
  - Positive regarding ease of professional credential receipt
  - Applied sciences students appreciated familiar PKI-based approach
- **Impact on user experience and feasibility**:
  - Limited without cross-border verification for international professional mobility
  - Classical PKI approach familiar to applied sciences stakeholders

---

## 7. Evidence Archive and References

- **Screenshots or logs**: Applied sciences credential issuance workflows documented
- **Links to SaaS environment or dashboards**: SUNET/SURF test environment for Saxion University
- **Documents or repositories**:
  - Pilot3-ClassicalPKI SaaS infrastructure description
  - Applied sciences user journeys documentation
  - Professional programme credential templates
- **KPI data submission details**: Weekly updates to WP5 team with applied sciences metrics

---

## 8. Next Steps and Recommendations

- **Pending actions**: None for Classical PKI component
- **Recommendations**:
  - Future Classical PKI pilots should prioritise cross-border verification readiness for professional qualifications
  - Availability of RP certificates essential for international applied sciences recognition
  - Professional education sector would benefit from enhanced Classical PKI trust infrastructure

---

## 9. Summary of End-User Feedback

- **General impressions**: Positive overall for Classical PKI approach in applied sciences education
- **Ease of use of wallet or platform**: High satisfaction with wwWallet for professional education contexts
- **Challenges encountered**: None reported in applied sciences credential issuance process
- **Suggestions for improvement**: Enable cross-border verification capabilities for international professional mobility
- **Willingness to use again**: Yes, particularly for applied sciences programmes

---

## 10. Summary of Piloting Agent Insights

- **Feedback on support received**: Good support from SUNET/SURF and WP7 for applied sciences requirements
- **Main barriers during implementation**: Relying party certificate availability for Classical PKI trust chains
- **Lessons learned**: Early provisioning of verification certificates essential for professional education cross-border recognition
- **Observed impact and value**: Clear demonstration of Classical PKI issuance process for applied sciences education
- **Recommendations for scaling**: Clarify cross-border verification flows early for professional qualifications, ensure Classical PKI infrastructure readiness for professional mobility

---

**Disclaimer**

Saxion University of Applied Sciences has performed all actions that were technically and operationally feasible within the scope of the Pilot3-ClassicalPKI SaaS environment provided by WP7. The limitations described (e.g., lack of RP certificates and lifecycle management) were due to constraints of the WP7-provided Classical PKI infrastructure and were not under the control of Saxion University. This Classical PKI implementation complements the institution's Pilot3-dPKI approach, providing a comprehensive hybrid trust framework for applied sciences education.