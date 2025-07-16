# DC4EU Deployment and Testing Scenarios Results Library (DTSRL) – Scenario: COFAC - Lusófona University - Classical PKI

## 1. Scenario Identification

- **Piloting agent name**: COFAC - Lusófona University (ULUSOFONA)
- **Scenario title**: Private University Credential Issuance with SUNET/SURF SaaS (Classical PKI)
- **Date of submission**: 11 July 2025
- **Point of contact (SPOC)**: Paulo Ferreira

---

## 2. Scenario Characterisation

- **User journeys implemented**:
  Wallet installation, PID issuance (SD-JWT), EducationalID issuance, Diploma issuance, QR-based verification (integrity checks only)
- **Target groups and end-user roles**:
  Private university students (approx. 25 pilot users), international programme graduates, administrative staff
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
  Weekly progress reports tracked via Lusófona University project management tools and regular updates to DC4EU WP5

---

## 3. Legal, Organisational and Operational Details

- **Regulatory context**:
  - GDPR compliance
  - Portuguese national private higher education regulations
  - International education regulatory requirements
- **Risk management**:
  Limited credential lifecycle (revocation out of scope for Classical PKI component), no cross-border trust verification for international credentials
- **Credential lifecycle management**:
  - Revocation: Not implemented (functionality not provided by WP7 for Classical PKI)
  - Suspension: Not implemented (functionality not provided by WP7 for Classical PKI)
- **Infrastructure readiness**:
  Remote SUNET/SURF SaaS environment provisioned for private education use cases
- **Training and onboarding**:
  Approximately 3 private education staff trained on wwWallet usage and Classical PKI issuance workflows for international programmes
- **Issue escalation**:
  SPOC contact: Paulo Ferreira, with escalation to SUNET/SURF support
- **Success indicators and KPIs**:
  Number of private education credentials issued: target 25, user feedback on wwWallet usability for international education contexts

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
- **Number of users onboarded**: 25 private university students and international programme participants
- **Credentials issued**: 25 EducationalID credentials and 25 Private University Diplomas (SD-JWT format)
- **Credentials verified**: Verification limited to local integrity checks (no full trust chain validation due to Classical PKI infrastructure limitations)
- **Successes**:
  - Successful wwWallet installation and private university credential issuance
  - Effective demonstration of Classical PKI approach for international education
- **Issues encountered**:
  - No RP certificate available for Classical PKI, preventing full cross-border verification of international qualifications
- **Deviation from plan**:
  - Partial testing of verification flows only for private education credentials

---

## 6. Testing Results and Observations

- **What worked as expected**:
  - Private university credential issuance from SUNET/SURF SaaS
  - wwWallet storage and display of international qualifications
  - SD-JWT format compatibility with private education requirements
- **What did not work and why**:
  - No RP certificate provisioned by WP7 for Classical PKI trust chain validation
  - Cross-border verification of international qualifications limited
- **Feedback from users**:
  - Positive regarding ease of international credential receipt
  - Private university students appreciated familiar PKI-based approach
- **Impact on user experience and feasibility**:
  - Limited without cross-border verification for international academic mobility
  - Classical PKI approach familiar to private education stakeholders

---

## 7. Evidence Archive and References

- **Screenshots or logs**: Private university credential issuance workflows documented
- **Links to SaaS environment or dashboards**: SUNET/SURF test environment for COFAC - Lusófona University
- **Documents or repositories**:
  - Pilot3-ClassicalPKI SaaS infrastructure description
  - Private education user journeys documentation
  - International programme credential templates
- **KPI data submission details**: Weekly updates to WP5 team with private education metrics

---

## 8. Next Steps and Recommendations

- **Pending actions**: None for Classical PKI component
- **Recommendations**:
  - Future Classical PKI pilots should prioritise cross-border verification readiness for international qualifications
  - Availability of RP certificates essential for international private education recognition
  - Private education sector would benefit from enhanced Classical PKI trust infrastructure

---

## 9. Summary of End-User Feedback

- **General impressions**: Positive overall for Classical PKI approach in private international education
- **Ease of use of wallet or platform**: High satisfaction with wwWallet for international education contexts
- **Challenges encountered**: None reported in private university credential issuance process
- **Suggestions for improvement**: Enable cross-border verification capabilities for international academic mobility
- **Willingness to use again**: Yes, particularly for international education programmes

---

## 10. Summary of Piloting Agent Insights

- **Feedback on support received**: Good support from SUNET/SURF and WP7 for private education requirements
- **Main barriers during implementation**: Relying party certificate availability for Classical PKI trust chains
- **Lessons learned**: Early provisioning of verification certificates essential for international education cross-border recognition
- **Observed impact and value**: Clear demonstration of Classical PKI issuance process for private international education
- **Recommendations for scaling**: Clarify cross-border verification flows early for international qualifications, ensure Classical PKI infrastructure readiness for academic mobility

---

**Disclaimer**

COFAC - Lusófona University has performed all actions that were technically and operationally feasible within the scope of the Pilot3-ClassicalPKI SaaS environment provided by WP7. The limitations described (e.g., lack of RP certificates and lifecycle management) were due to constraints of the WP7-provided Classical PKI infrastructure and were not under the control of Lusófona University. This Classical PKI implementation complements the institution's Pilot3-dPKI approach, providing a comprehensive hybrid trust framework for private international education.