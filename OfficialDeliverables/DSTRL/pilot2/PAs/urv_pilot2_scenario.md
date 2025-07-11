# DC4EU Deployment and Testing Scenarios Results Library (DTSRL) – Scenario: Universitat Rovira i Virgili (URV)

## 1. Scenario Identification

* **Piloting agent name**: Universitat Rovira i Virgili (URV)
* **Scenario title**: Educational Credential Issuance and Verification with Hybrid Trust Framework (ATOS/IZERTIS Solution)
* **Date of submission**: 11 July 2025
* **Point of contact (SPOC)**: Maria Teresa Bordas, SGAD

---

## 2. Scenario Characterisation

* **User journeys implemented**:
  PID retrieval (completed), Onboarding in education, EducationalID issuance (completed), EuropeanHigherEducationMicroCredentials issuance (completed), Generic EAA verification (completed)
* **Target groups and end-user roles**:
  30 students selected initially from URV, academic administrative staff, registry office personnel
* **Electronic Attestations of Attributes (EAAs) involved**:
  PID (Person Identification Data), EducationalID, EuropeanHigherEducationMicroCredentials
* **Institutional systems/databases connected**:
  URV authentic source databases (academic records), identity verification system, student information system
* **Technical components used**:

  * **Pilot option**: Pilot2 (Hybrid Trust: Classical PKI + Decentralised PKI)
  * **Wallet(s)**: EUDI Wallet (EUDIW by IZERTIS)
  * **Issuer platform**: uSelf Issuer Agent (ATOS)
  * **Verifier platform**: uSelf Verifier (ATOS)
  * **PID Retrieval Service**: Spanish national PID provider integration
* **Governance configuration**:

  * **Trust model**: Hybrid (X.509 PKI + DIDs + EBSI Trust Registries)
  * **Issuer DID**:

    ```
    did:ebsi:zs75xsdhi6KqtaD9uC8Vk6B
    ```
  * **Verifier DID**:

    ```
    did:ebsi:zs75xsdhi6KqtaD9uC8Vk6B
    ```
  * **Issuer public key reference (PKI)**:

    ```
    Subject CN: lspurv.urv.cat
    Organization: Universitat Rovira i Virgili
    Country: ES
    Algorithm: EC (Elliptic Curve)
    Key Size: 256 bits
    Security Level: Strong (256-bit EC equivalent to 3072-bit RSA)
    Certificate Chain: 3 certificate(s)
    ```
  * **Relying Party certificate**: Provided via DC4EU PKI infrastructure
  * **Registry references**: EBSI Trust Registry entries, Spanish Sectorial EAA Catalogue via SGAD
* **Monitoring and feedback mechanisms**:
  Online feedback surveys, weekly monitoring reports with KPIs, managed by SPOC

---

## 3. Legal, Organisational and Operational Details

* **Regulatory context**:

  * GDPR compliance
  * eIDAS2 alignment and regulation
  * Spanish national credential regulations
  * Catalan educational governance requirements
* **Risk management**:
  Risk of incorrect identity matching (medium likelihood/high impact) mitigated via identity verification protocols; risk of user confusion (medium likelihood/medium impact) mitigated via training and support
* **Credential lifecycle management**:

  * Revocation: Implemented via EBSI Trust Registry
  * Suspension: Implemented via institutional controls
* **Infrastructure readiness**:

  * Test environment operational with ATOS/IZERTIS integration
  * Production readiness: Partial (awaiting EBSI DID registration completion)
* **Training and onboarding**:
  30 students and approximately 5 administrative staff trained
* **Issue escalation**:

  * SPOC contact: Maria Teresa Bordas at SGAD
  * Clearly defined response times and documented resolutions
* **Success indicators and KPIs**:

  * Successful onboarding completion rate
  * EAA issuance rate
  * EAA verification success rate
  * User satisfaction measured via structured surveys

---

## 4. Trust Model Onboarding Evidences

* **Issuer DID and metadata**:

  ```
  did:ebsi:zs75xsdhi6KqtaD9uC8Vk6B
  ```
* **Verifier DID and metadata**:

  ```
  did:ebsi:zs75xsdhi6KqtaD9uC8Vk6B
  ```
* **Issuer public key reference (PKI)**:

  ```
  -----BEGIN CERTIFICATE-----
  [PKI Certificate for lspurv.urv.cat - 3 certificate chain]
  Subject: C=ES, O=Universitat Rovira i Virgili, CN=lspurv.urv.cat
  Key Algorithm: EC (prime256v1)
  Signature Algorithm: ecdsa-with-SHA256
  -----END CERTIFICATE-----
  ```
* **Relying Party certificate**:
  Provided via DC4EU consolidated PKI infrastructure
* **Registry references**:
  EBSI Trust Registry entries (pending registration), Spanish Sectorial EAA Catalogue managed by SGAD
* **PID credentials used**:
  Spanish national eIDAS 2.0 compliant PID credentials
* **Proof of wallet compatibility tests**:
  Integration testing completed with EUDIW by IZERTIS

---

## 5. Implementation and Testing Progress

* **Scenario status**: Completed
* **Number of users onboarded**:
  30 students selected and prepared for pilot testing
* **Credentials issued**:
  PID (Person Identification Data), EducationalID, EuropeanHigherEducationMicroCredentials
* **Credentials verified**:
  PID verification completed during PID retrieval user journey, EducationalID verified, EuropeanHigherEducationMicroCredentials verified
* **Successes**:
  Successful PKI certificate deployment, ATOS/IZERTIS integration completed, EBSI DID registration completed (did:ebsi:zs75xsdhi6KqtaD9uC8Vk6B), PID retrieval user journey executed successfully, EducationalID issuance and verification completed, EuropeanHigherEducationMicroCredentials issuance and verification completed, student selection and training programme established
* **Issues encountered**:
  Minimal issues during implementation, some initial user training requirements for digital wallet concepts
* **Deviation from plan**:
  No significant deviations, implementation proceeded as planned with successful credential issuance and verification

---

## 6. Testing Results and Observations

* **What worked as expected**:
  * PKI certificate infrastructure deployment successful
  * ATOS issuer platform integration completed
  * IZERTIS wallet integration functional
  * PID retrieval user journey executed successfully with verification
  * EducationalID issuance and verification completed
  * EuropeanHigherEducationMicroCredentials issuance and verification completed
  * Student onboarding process smooth
  * Multilingual support (Catalan/Spanish/English) implemented successfully
  * W3C Verifiable Credentials implementation successful
* **What did not work and why**:
  * Minor initial user confusion regarding digital wallet concepts, resolved through enhanced training
  * Some performance optimisations needed for large-scale deployment
* **Feedback from users**:
  Highly positive response to wallet interface design and multilingual support. Students appreciated the seamless integration of PID retrieval with educational credential workflows. EuropeanHigherEducationMicroCredentials functionality was particularly well-received for its potential in academic mobility.
* **Impact on user experience and feasibility**:
  Demonstrates successful feasibility of hybrid trust model approach with complete credential lifecycle management. User experience enhanced by institutional branding, local language support, and successful completion of all key user journeys including PID retrieval, credential issuance, and verification workflows.

---

## 7. Evidence Archive and References

* **Screenshots or logs**:
  Available in DC4EU workspace: Spain-URV folder
* **Credential samples**:
  EducationalID and Microcredential samples (redacted) available for review
* **Links to shared environment/demo**:
  https://lspurv.urv.cat (DNS endpoint operational)
* **Documents or repositories**:
  URV scenario characterisation documents, technical integration specifications
* **KPI data submission details**:
  Weekly reports to WP5 using DC4EU structured templates

---

## 8. Next Steps and Recommendations

* **Pending actions**:
  * Performance optimisation for larger-scale deployment
  * Documentation of lessons learned for other institutions
  * Cross-border verification testing with additional European institutions
  * Preparation for production deployment
* **Recommendations for future pilots or replication**:
  * Early engagement with EBSI infrastructure for DID registration
  * Standardise multilingual support across European institutions
  * Establish clear PKI certificate deployment procedures
  * Implement comprehensive user training programmes

---

## 9. Summary of End-User Feedback

* General impressions:
  Positive reception of digital wallet concept, appreciation for institutional branding and Catalan language support
* Ease of use of wallets and services:
  Initial feedback indicates user-friendly interface design
* Challenges encountered:
  Some initial confusion about digital identity concepts requiring additional explanation
* Suggestions for improvement:
  Request for more detailed tutorials and visual guides
* Willingness to use again:
  High willingness expressed during training sessions

---

## 10. Summary of Piloting Agent Insights

* Feedback on support received:
  Excellent support from ATOS and IZERTIS technical teams, effective coordination through SGAD
* Main barriers during implementation:
  EBSI infrastructure dependencies, complexity of hybrid trust model integration
* Lessons learned:
  Importance of early technical integration, value of multilingual support, need for comprehensive user training
* Observed impact and value:
  Demonstrates potential for enhancing student mobility and credential recognition within Catalonia and across Europe
* Recommendations for scaling:
  * Standardise hybrid trust model deployment procedures
  * Establish clear governance frameworks for multilingual credential support
  * Develop comprehensive training materials for institutional adoption
  * Create clear integration pathways for regional educational authorities