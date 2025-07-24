# DC4EU Deployment and Testing Scenarios Results Library (DTSRL) – Scenario: Unitatea Executivă pentru Finanțarea Învățământului Superior (UEFISCDI)

## 1. Scenario Identification

* **Piloting agent name**: Unitatea Executivă pentru Finanțarea Învățământului Superior (UEFISCDI)
* **Scenario title**: Higher Education Financing Credential Issuance and Verification with Hybrid Trust Framework (ATOS/IZERTIS Dockerised Solution)
* **Date of submission**: 11 July 2025
* **Point of contact (SPOC)**: Cosmin Cioranu

---

## 2. Scenario Characterisation

* **User journeys implemented**:
  PID retrieval (completed), Onboarding in education, EducationalID issuance (completed), Educational achievement issuance (completed), Generic EAA verification (completed)
* **Target groups and end-user roles**:
  Higher education stakeholders, academic administrative staff, registry office personnel, education financing beneficiaries
* **Electronic Attestations of Attributes (EAAs) involved**:
  PID (Person Identification Data), EducationalID, Educational Achievement (EAAs: Higher education financing certificates, Academic achievement records)
* **Institutional systems/databases connected**:
  UEFISCDI authentic source databases (financing records), identity verification system, higher education information systems
* **Technical components used**:

  * **Pilot option**: Pilot2 (Hybrid Trust: Classical PKI + Decentralised PKI)
  * **Wallet(s)**: EUDI Wallet (EUDIW by IZERTIS)
  * **Issuer platform**: uSelf Issuer Agent (ATOS) - Dockerised solution
  * **Verifier platform**: uSelf Verifier (ATOS) - Dockerised solution
  * **PID Retrieval Service**: Romanian national PID provider integration
* **Governance configuration**:

  * **Trust model**: Hybrid (X.509 PKI + DIDs + EBSI Trust Registries)
  * **Issuer DID**:

    ```
    did:ebsi:zjYYLbf3EvzpNMPcDYSy8JS
    ```
  * **Verifier DID**:

    ```
    did:ebsi:zjYYLbf3EvzpNMPcDYSy8JS
    ```
  * **Issuer public key reference (PKI)**:

    ```
    Subject CN: lsp.dc4eu.runidas.rei.gov.ro
    Organization: Unitatea Executivă pentru Finanțarea Învățământului Superior
    Country: RO
    Algorithm: EC (Elliptic Curve)
    Key Size: 256 bits
    Security Level: Strong (256-bit EC equivalent to 3072-bit RSA)
    Certificate Chain: 3 certificate(s)
    ```
  * **Relying Party certificate**: Provided via DC4EU PKI infrastructure
  * **Registry references**: EBSI Trust Registry entries, Romanian Sectorial EAA Catalogue via SGAD
* **Monitoring and feedback mechanisms**:
  Online feedback surveys, weekly monitoring reports with KPIs, managed by SPOC

---

## 3. Legal, Organisational and Operational Details

* **Regulatory context**:
  * GDPR compliance
  * eIDAS2 alignment and regulation
  * Romanian national higher education regulations
  * Higher education financing regulations
* **Risk management**:
  Risk of incorrect identity matching (medium likelihood/high impact) mitigated via identity verification protocols; risk of user confusion (medium likelihood/medium impact) mitigated via training and support
* **Credential lifecycle management**:
  * Revocation: Implemented via EBSI Trust Registry
  * Suspension: Implemented via institutional controls
* **Infrastructure readiness**:
  * Test environment operational with ATOS/IZERTIS Dockerised solution
  * Production readiness: Achieved
* **Training and onboarding**:
  Higher education stakeholders and approximately 4 administrative staff trained
* **Issue escalation**:
  * SPOC contact: Cosmin Cioranu
  * Clearly defined response times and documented resolutions via SGAD
* **Success indicators and KPIs**:
  * Successful onboarding completion rate
  * EAA issuance rate
  * EAA verification success rate
  * User satisfaction measured via structured surveys

---

## 4. Trust Model Onboarding Evidences

* **Issuer DID and metadata**:
  ```
  did:ebsi:zjYYLbf3EvzpNMPcDYSy8JS
  ```
* **Verifier DID and metadata**:
  ```
  did:ebsi:zjYYLbf3EvzpNMPcDYSy8JS
  ```
* **Issuer public key reference (PKI)**:
  ```
  -----BEGIN CERTIFICATE-----
  [PKI Certificate for lsp.dc4eu.runidas.rei.gov.ro - 3 certificate chain]
  Subject: C=RO, O=Unitatea Executivă pentru Finanțarea Învățământului Superior, CN=lsp.dc4eu.runidas.rei.gov.ro
  Key Algorithm: EC (prime256v1)
  Signature Algorithm: ecdsa-with-SHA256
  -----END CERTIFICATE-----
  ```
* **Relying Party certificate**: Provided via DC4EU consolidated PKI infrastructure
* **Registry references**: EBSI Trust Registry entries (registered), Romanian Sectorial EAA Catalogue managed by SGAD
* **PID credentials used**: Romanian national eIDAS 2.0 compliant PID credentials
* **Proof of wallet compatibility tests**: Integration testing completed with EUDIW by IZERTIS

---

## 5. Implementation and Testing Progress

* **Scenario status**: Completed
* **Number of users onboarded**: Higher education stakeholders successfully onboarded for credential testing
* **Credentials issued**: PID (Person Identification Data), EducationalID, Educational Achievement (Higher education financing certificates)
* **Credentials verified**: PID verification completed during PID retrieval user journey, EducationalID verified, Educational Achievement verified
* **Successes**: Successful PKI certificate deployment, ATOS/IZERTIS Dockerised solution integration completed, EBSI DID registration completed, comprehensive higher education financing credential workflows demonstrated
* **Issues encountered**: Minor initial configuration requirements for Romanian regulatory context, successfully resolved
* **Deviation from plan**: No significant deviations, implementation proceeded as planned with Dockerised solution

---

## 6. Testing Results and Observations

* **What worked as expected**:
  * PKI certificate infrastructure deployment successful
  * ATOS/IZERTIS Dockerised solution integration completed
  * IZERTIS wallet integration functional
  * All higher education financing user journeys executed successfully
  * Romanian regulatory compliance achieved
  * Higher education financing credential workflows successful
* **What did not work and why**:
  * Minor performance considerations for scaling
  * Initial user training requirements addressed through specialized training
* **Feedback from users**: Positive response from higher education stakeholders, appreciation for digitisation of financing credentials and transparency
* **Impact on user experience and feasibility**: Demonstrates successful feasibility of hybrid trust model for Romanian higher education financing context

---

## 7. Evidence Archive and References

* **Screenshots or logs**: Available in DC4EU workspace: Romania-UEFISCDI folder
* **Credential samples**: EducationalID and Higher education financing certificate samples (redacted) available for review
* **Links to shared environment/demo**: https://lsp.dc4eu.runidas.rei.gov.ro (DNS endpoint operational)
* **Documents or repositories**: UEFISCDI scenario characterisation documents, ATOS/IZERTIS Dockerised solution integration specifications
* **KPI data submission details**: Weekly reports to WP5 using DC4EU structured templates

---

## 8. Next Steps and Recommendations

* **Pending actions**: Performance optimisation, documentation of lessons learned for higher education financing authorities, cross-border verification testing
* **Recommendations for future pilots or replication**: ATOS/IZERTIS Dockerised solution provides effective implementation pathway for Romanian higher education authorities

---

## 9. Summary of End-User Feedback

* General impressions: Positive reception from higher education stakeholders
* Ease of use of wallets and services: High usability reported for higher education financing workflows
* Challenges encountered: Initial learning curve successfully addressed through specialized training
* Suggestions for improvement: Request for additional financing credential types, enhanced transparency features
* Willingness to use again: High willingness expressed

---

## 10. Summary of Piloting Agent Insights

* Feedback on support received: Excellent support from ATOS and IZERTIS technical teams
* Main barriers during implementation: Romanian regulatory context integration for higher education financing
* Lessons learned: Value of Dockerised solution for higher education authority rapid deployment
* Observed impact and value: Demonstrates significant potential for transforming Romanian higher education financing transparency
* Recommendations for scaling: Expand ATOS/IZERTIS Dockerised solution to other Romanian higher education authorities