# DC4EU Deployment and Testing Scenarios Results Library (DTSRL) – Scenario: Finnish National Agency for Education (OPH)

## 1. Scenario Identification

- **Piloting agent name**: Finnish National Agency for Education (OPH)
- **Scenario title**: PID and Educational Credential Issuance and Verification (Finnish National Solution)
- **Date of submission**: 1 July 2025
- **Point of contact (SPOC)**: OPH

---

## 2. Scenario Characterisation

- **User journeys implemented**:
  - Wallet installation
  - PID retrieval
  - Educational credential issuance
  - Credential presentation to verifiers (DVV test verifier and DC4EU verifier)
- **Target groups and end-user roles**:
  - 25 registered student test users
  - Administrative staff
- **Electronic Attestations of Attributes (EAAs) involved**:
  - PID (Person Identification Data)
  - Educational qualifications (vocational, secondary, and higher education degrees)
- **Institutional systems/databases connected**:
  - KOSKI (vocational and secondary education)
  - VIRTA (higher education)
- **Technical components used**:
  - **Pilot option**: Pilot1 (Classical PKI, national sealing certificates)
  - **SaaS environment**: Finnish DVV issuance service and verifier services
  - **Wallet**: Finnish EUDI Wallet Demo (Android)
  - **Issuer platform**: DVV Issuance Service
  - **Verifier platform**: DVV Test Verifier, DC4EU Verifier
- **Governance configuration**:
  - **Trust model**: Centralised sealing with manually created certificates (no integration with national trust lists)
  - **Issuer certificate**: Sealing certificate (sealing-cert.pem) issued by DVV
  - **Relying Party certificate**: Presentation requests signed by DVV-issued certificates but not validated against trust lists
  - **Decentralised Identifiers (DIDs)**: Not applicable
- **Monitoring and feedback mechanisms**:
  - Manual logs of issuance and verification
  - User surveys collected after test sessions

---

## 3. Legal, Organisational and Operational Details

- **Regulatory context**:
  - GDPR compliance (consent-based data transfers)
  - Act on Information Management in Public Administration (906/2019)
  - Act on National Registers of Education Records (884/2017)
- **Risk management**:
  - Risks: delayed trust infrastructure, manual sealing, lack of revocation
  - Mitigations: limited scope testing, internal validation, fallback processes
- **Credential lifecycle management**:
  - Revocation: Not implemented
  - Suspension: Not implemented
- **Infrastructure readiness**:
  - Wallet and issuance service operational
  - Verifier services functional
- **Training and onboarding**:
  - Test user instructions provided via DVV wiki and email
  - On-site training (28 May 2025)
- **Issue escalation**:
  - SPOC contact: OPH, technical support via DVV
- **Success indicators and KPIs**:
  - Number of credentials issued and verified
  - Positive user feedback

---

## 4. Trust Model Onboarding Evidences

- **Issuer X.509v3 certificate**:
  ```
  OPH sealing-cert.pem
  ```
- **CA certificate**:
  ```
  OPH sealing-ca-cert.pem
  ```
- **Relying Party certificate**:
  - Used in presentation requests (checked for technical validity but no trust list verification)
- **Decentralised Identifiers (DIDs)**: Not applicable
- **Registry references**: Not applicable

---

## 5. Implementation and Testing Progress

- **Scenario status**: Completed
- **Testing period**: 20 May – 15 June 2025
- **Users onboarded**: 22 test users
- **Credentials issued**: 22 educational credentials
- **Credentials verified**: 10 successfully verified with DVV and DC4EU verifiers
- **Successes**:
  - Issuance flows completed end-to-end
- **Issues encountered**:
  - Attribute-level interoperability gaps with DC4EU verifier
  - No revocation support
- **Deviation from plan**:
  - Trust list and revocation not implemented

---

## 6. Testing Results and Observations

- **What worked as expected**:
  - Consent-based data retrieval
  - Credential issuance with manual sealing
- **What did not work and why**:
  - Attribute-level interoperability with DC4EU verifier
  - No revocation or trust chain validation
- **Feedback from users**:
  - Positive overall; confusion around multiple consent steps
- **Impact on user experience and feasibility**:
  - Demonstrated feasibility with limitations

---

## 7. Evidence Archive and References

- **Screenshots and videos**:
  - Available in DC4EU workspace: Finland-OPH
- **Wallet demo documentation**:
  - [https://wiki.dvv.fi/spaces/EDI/pages/235522018/1.+DVV+n+esimerkkisovellus+Finnish+EUDI+Wallet+Demo+mobile+application](https://wiki.dvv.fi/spaces/EDI/pages/235522018/1.+DVV+n+esimerkkisovellus+Finnish+EUDI+Wallet+Demo+mobile+application)
- **Credential samples**:
  - Stored in OPH internal repository
- **KPI submission**:
  - Logs collected and submitted to WP5

---

## 8. Next Steps and Recommendations

- **Pending actions**:
  - Integration with trust lists and revocation mechanisms
- **Recommendations**:
  - Standardise credential schemas and attribute naming
  - Align selective disclosure models

---

## 9. Summary of End-User Feedback

- General impressions: Positive, wallet easy to install and use
- Ease of use: High, though some steps confusing
- Challenges: Understanding consent and data visibility
- Suggestions: Clarify flows and simplify steps
- Willingness to use again: Yes

---

## 10. Summary of Piloting Agent Insights

- Feedback on support: WP5 materials were delayed; clearer guidance needed
- Main barriers: No trust infrastructure ready
- Lessons learned: Early alignment of schemas critical
- Observed impact: Demonstrated feasibility of national wallet use
- Recommendations: Expand pilots to more verifiers and production readiness

---

**Disclaimer**\
OPH has performed all actions technically feasible within the Pilot1 framework and national infrastructure. Limitations (e.g., no revocation, no trust list integration) were outside OPH's control.

