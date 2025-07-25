# DC4EU Deployment and Testing Scenarios Results Library (DTSRL) – Scenario: Universidad de Murcia (UM)

## 1. Scenario Identification

* **Piloting agent name**: Universidad de Murcia (UM)
* **Scenario title**: Educational Credential Issuance and Verification with Hybrid Trust Framework (ATOS/IZERTIS Solution)
* **Date of submission**: 11 July 2025
* **Point of contact (SPOC)**: Antonio, SGAD

---

## 2. Scenario Characterisation

* **User journeys implemented**:
  PID retrieval (completed), Onboarding in education, EducationalID issuance (completed), Educational achievement issuance (completed), Generic EAA verification (completed)
* **Target groups and end-user roles**:
  University students selected from Universidad de Murcia, academic administrative staff, registry office personnel
* **Electronic Attestations of Attributes (EAAs) involved**:
  PID (Person Identification Data), EducationalID, Educational Achievement (University credentials, Academic certificates)
* **Institutional systems/databases connected**:
  UM authentic source databases (academic records), identity verification system, student information system
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
    did:ebsi:zy4crCvTaCdyLKHwrmvnxFP
    ```
  * **Verifier DID**:

    ```
    did:ebsi:zy4crCvTaCdyLKHwrmvnxFP
    ```
  * **Issuer public key reference (PKI)**:

    ```
    Subject CN: lspum.um.es
    Organization: Universidad de Múrcia
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
  * Regional Murcia educational governance requirements
* **Risk management**:
  Risk of incorrect identity matching (medium likelihood/high impact) mitigated via identity verification protocols; risk of user confusion (medium likelihood/medium impact) mitigated via training and support
* **Credential lifecycle management**:

  * Revocation: Implemented via EBSI Trust Registry
  * Suspension: Implemented via institutional controls
* **Infrastructure readiness**:

  * Test environment operational with ATOS/IZERTIS integration
  * Production readiness: Partial (awaiting EBSI DID registration completion)
* **Training and onboarding**:
  University students and approximately 5 administrative staff trained
* **Issue escalation**:

  * SPOC contact: Antonio at SGAD
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
  did:ebsi:zy4crCvTaCdyLKHwrmvnxFP
  ```
* **Verifier DID and metadata**:

  ```
  did:ebsi:zy4crCvTaCdyLKHwrmvnxFP
  ```
* **Issuer public key reference (PKI)**:

  ```
  -----BEGIN CERTIFICATE-----
  [PKI Certificate for lspum.um.es - 3 certificate chain]
  Subject: C=ES, O=Universidad de Múrcia, CN=lspum.um.es
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
  30 University students successfully onboarded for credential testing
* **Credentials issued**:
  PID (Person Identification Data), EducationalID, Educational Achievement (European Higher Education Transcript of Records)
* **Credentials verified**:
  PID verification completed during PID retrieval user journey, EducationalID verified, Educational Achievement verified
* **Successes**:
  Successful PKI certificate deployment, ATOS/IZERTIS integration completed, EBSI DID registration completed (did:ebsi:zy4crCvTaCdyLKHwrmvnxFP), PID retrieval user journey executed successfully, comprehensive educational credential issuance and verification workflows demonstrated, effective integration with Spanish governance framework
* **Issues encountered**:
  Minor initial configuration requirements for regional Murcia context, successfully resolved
* **Deviation from plan**:
  No significant deviations, implementation proceeded as planned with successful completion of all key objectives

---

## 6. Testing Results and Observations

* **What worked as expected**:
  * PKI certificate infrastructure deployment successful
  * ATOS issuer platform integration completed
  * IZERTIS wallet integration functional
  * PID retrieval user journey executed successfully
  * EducationalID issuance and verification completed
  * Educational Achievement issuance and verification completed
  * University student onboarding process effective
  * W3C Verifiable Credentials implementation successful
  * Spanish regulatory compliance achieved
  * Regional Murcia requirements met
* **What did not work and why**:
  * Minor performance considerations for scaling beyond pilot scope
  * Some initial user training requirements for digital credential concepts
* **Feedback from users**:
  Positive response from university students, appreciation for digital credential innovation and potential for academic mobility within Spain and Europe
* **Impact on user experience and feasibility**:
  Demonstrates successful feasibility of hybrid trust model approach for Spanish university context. Strong potential demonstrated for enhancing student mobility and credential recognition across Spanish universities and Europe.

---

## 7. Evidence Archive and References

* **Screenshots or logs**:
  Available in DC4EU workspace: Spain-UM folder
* **Credential samples**:
  EducationalID and University credential samples (redacted) available for review
* **Links to shared environment/demo**:
  https://lspum.um.es (DNS endpoint operational)
* **Documents or repositories**:
  UM scenario characterisation documents, technical integration specifications
* **KPI data submission details**:
  Weekly reports to WP5 using DC4EU structured templates

---

## 8. Next Steps and Recommendations

* **Pending actions**:
  * Performance optimisation for larger-scale deployment across university
  * Documentation of lessons learned for other Murcia regional universities
  * Cross-border verification testing with additional European institutions
  * Preparation for full university deployment
* **Recommendations for future pilots or replication**:
  * Early integration with regional Spanish governance frameworks
  * Focus on academic achievement applications for enhanced student flexibility
  * Standardise Spanish university credential formats
  * Implement comprehensive training programmes for Spanish university contexts

---

## 9. Summary of End-User Feedback

* General impressions:
  Positive reception from students, strong appreciation for digital transformation of academic credentials and university innovation
* Ease of use of wallets and services:
  High usability reported, successful completion of all educational credential user journeys
* Challenges encountered:
  Initial learning curve for digital credential concepts, successfully addressed through training
* Suggestions for improvement:
  Request for additional university credential types, interest in enhanced Spanish language support
* Willingness to use again:
  High willingness expressed, strong interest in expanding to other academic credentials and university-wide deployment

---

## 10. Summary of Piloting Agent Insights

* Feedback on support received:
  Excellent support from ATOS and IZERTIS technical teams, effective coordination through SGAD
* Main barriers during implementation:
  EBSI infrastructure dependencies, complexity of hybrid trust model integration, minor configuration requirements for regional Murcia context
* Lessons learned:
  Importance of early technical integration, value of university credential focus for Spanish institutions, need for comprehensive user training, importance of regional compliance
* Observed impact and value:
  Demonstrates significant potential for enhancing student mobility and credential recognition within Murcia region and across Europe, particularly for university-level academic credentials
* Recommendations for scaling:
  * Standardise hybrid trust model deployment procedures for Spanish universities
  * Establish clear governance frameworks for regional compliance
  * Develop comprehensive training materials for Spanish institutional adoption
  * Create clear integration pathways for regional educational authorities
  * Focus on university credential standardisation across Spanish higher education