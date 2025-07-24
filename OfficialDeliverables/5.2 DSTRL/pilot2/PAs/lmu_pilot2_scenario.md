# DC4EU Deployment and Testing Scenarios Results Library (DTSRL) – Scenario: Ludwig-Maximilians-Universität München (LMU)

## 1. Scenario Identification

* **Piloting agent name**: Ludwig-Maximilians-Universität München (LMU)
* **Scenario title**: Educational Credential Issuance and Verification with Hybrid Trust Framework
* **Date of submission**: 11 July 2025
* **Point of contact (SPOC)**: LMU Representative

---

## 2. Scenario Characterisation

* **User journeys implemented**:
  PID retrieval (completed), Onboarding in education, EducationalID issuance (completed), Educational achievement issuance (completed), Generic EAA verification (completed)
* **Target groups and end-user roles**:
  University students, academic administrative staff, registry office personnel
* **Electronic Attestations of Attributes (EAAs) involved**:
  PID (Person Identification Data), EducationalID, Educational Achievement (EAAs: University degrees, Academic certificates)
* **Institutional systems/databases connected**:
  LMU authentic source databases (academic records), identity verification system, student information system
* **Technical components used**:

  * **Pilot option**: Pilot2 (Hybrid Trust: Classical PKI + Decentralised PKI)
  * **Wallet(s)**: EUDI Wallet
  * **Issuer platform**: uSelf Issuer Agent
  * **Verifier platform**: uSelf Verifier
  * **PID Retrieval Service**: German national PID provider integration
* **Governance configuration**:

  * **Trust model**: Hybrid (X.509 PKI + DIDs + EBSI Trust Registries)
  * **Issuer DID**:

    ```
    did:ebsi:zh9MNp5mmuYjrLgtuqTZE2C
    ```
  * **Verifier DID**:

    ```
    did:ebsi:zh9MNp5mmuYjrLgtuqTZE2C
    ```
  * **Issuer public key reference (PKI)**:

    ```
    Subject CN: [LMU certificate details]
    Organization: Ludwig-Maximilians-Universität München
    Country: DE
    Algorithm: EC (Elliptic Curve)
    Key Size: 256 bits
    Security Level: Strong (256-bit EC equivalent to 3072-bit RSA)
    Certificate Chain: 3 certificate(s)
    ```
  * **Relying Party certificate**: Provided via DC4EU PKI infrastructure
  * **Registry references**: EBSI Trust Registry entries, German Sectorial EAA Catalogue
* **Monitoring and feedback mechanisms**:
  Online feedback surveys, weekly monitoring reports with KPIs, managed by SPOC

---

## 3. Legal, Organisational and Operational Details

* **Regulatory context**:

  * GDPR compliance
  * eIDAS2 alignment and regulation
  * German national higher education regulations
  * Bavarian state education requirements
* **Risk management**:
  Risk of incorrect identity matching (medium likelihood/high impact) mitigated via identity verification protocols; risk of user confusion (medium likelihood/medium impact) mitigated via training and support
* **Credential lifecycle management**:

  * Revocation: Implemented via EBSI Trust Registry
  * Suspension: Implemented via institutional controls
* **Infrastructure readiness**:

  * Test environment operational
  * Production readiness: Achieved
* **Training and onboarding**:
  University students and approximately 4 administrative staff trained
* **Issue escalation**:

  * SPOC contact: LMU Representative
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
  did:ebsi:zh9MNp5mmuYjrLgtuqTZE2C
  ```
* **Verifier DID and metadata**:

  ```
  did:ebsi:zh9MNp5mmuYjrLgtuqTZE2C
  ```
* **Issuer public key reference (PKI)**:

  ```
  -----BEGIN CERTIFICATE-----
  [PKI Certificate for LMU - 3 certificate chain]
  Subject: C=DE, O=Ludwig-Maximilians-Universität München
  Key Algorithm: EC (prime256v1)
  Signature Algorithm: ecdsa-with-SHA256
  -----END CERTIFICATE-----
  ```
* **Relying Party certificate**:
  Provided via DC4EU consolidated PKI infrastructure
* **Registry references**:
  EBSI Trust Registry entries (registered), German Sectorial EAA Catalogue
* **PID credentials used**:
  German national eIDAS 2.0 compliant PID credentials
* **Proof of wallet compatibility tests**:
  Integration testing completed with EUDI Wallet

---

## 5. Implementation and Testing Progress

* **Scenario status**: Completed
* **Number of users onboarded**:
  University students successfully onboarded for credential testing
* **Credentials issued**:
  PID (Person Identification Data), EducationalID, Educational Achievement (University degrees)
* **Credentials verified**:
  PID verification completed during PID retrieval user journey, EducationalID verified, Educational Achievement verified
* **Successes**:
  Successful PKI certificate deployment, platform integration completed, EBSI DID registration completed (did:ebsi:zh9MNp5mmuYjrLgtuqTZE2C), PID retrieval user journey executed successfully, comprehensive educational credential issuance and verification workflows demonstrated
* **Issues encountered**:
  Minor initial configuration requirements for Bavarian regulatory context, successfully resolved
* **Deviation from plan**:
  No significant deviations, implementation proceeded as planned

---

## 6. Testing Results and Observations

* **What worked as expected**:
  * PKI certificate infrastructure deployment successful
  * Platform integration completed
  * EUDI Wallet integration functional
  * PID retrieval user journey executed successfully
  * EducationalID issuance and verification completed
  * Educational Achievement issuance and verification completed
  * University student onboarding process effective
  * W3C Verifiable Credentials implementation successful
  * German regulatory compliance achieved
* **What did not work and why**:
  * Minor performance considerations for scaling beyond pilot scope
  * Some initial user training requirements for digital credential concepts
* **Feedback from users**:
  Positive response from university students, appreciation for digital credential innovation and potential for academic mobility
* **Impact on user experience and feasibility**:
  Demonstrates successful feasibility of hybrid trust model approach for German university context. Strong potential demonstrated for enhancing student mobility and credential recognition.

---

## 7. Evidence Archive and References

* **Screenshots or logs**:
  Available in DC4EU workspace: Germany-LMU folder
* **Credential samples**:
  EducationalID and University degree samples (redacted) available for review
* **Links to shared environment/demo**:
  [LMU DNS endpoint]
* **Documents or repositories**:
  LMU scenario characterisation documents, technical integration specifications
* **KPI data submission details**:
  Weekly reports to WP5 using DC4EU structured templates

---

## 8. Next Steps and Recommendations

* **Pending actions**:
  * Performance optimisation for larger-scale deployment across university
  * Documentation of lessons learned for other German universities
  * Cross-border verification testing with additional European institutions
  * Preparation for full university deployment
* **Recommendations for future pilots or replication**:
  * Early integration with German governance frameworks
  * Standardise German university credential formats
  * Implement comprehensive training programmes for German university contexts

---

## 9. Summary of End-User Feedback

* General impressions:
  Positive reception from university students, strong appreciation for digital transformation of academic credentials
* Ease of use of wallets and services:
  High usability reported, successful completion of all educational credential user journeys
* Challenges encountered:
  Initial learning curve for digital credential concepts, successfully addressed through training
* Suggestions for improvement:
  Request for additional credential types, interest in enhanced German language support
* Willingness to use again:
  High willingness expressed, strong interest in expanding across university

---

## 10. Summary of Piloting Agent Insights

* Feedback on support received:
  Excellent support from technical teams, effective platform deployment
* Main barriers during implementation:
  German regulatory context integration, minor technical optimisation requirements
* Lessons learned:
  Importance of German regulatory alignment, effectiveness of hybrid trust model
* Observed impact and value:
  Demonstrates significant potential for transforming German higher education credential management
* Recommendations for scaling:
  * Expand implementation to other German universities
  * Standardise German university credential formats
  * Develop comprehensive training materials for German university adoption
  * Create clear integration pathways for German higher education institutions