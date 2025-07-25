# DC4EU Deployment and Testing Scenarios Results Library (DTSRL) – Scenario: Universidad de Málaga (UMA)

## 1. Scenario Identification

* **Piloting agent name**: Universidad de Málaga (UMA)
* **Scenario title**: Educational Credential Issuance and Verification with Hybrid Trust Framework (ATOS/IZERTIS Solution)
* **Date of submission**: 11 July 2025
* **Point of contact (SPOC)**: Victoriano Giralt, SGAD

---

## 2. Scenario Characterisation

* **User journeys implemented**:
  PID retrieval (completed), Onboarding in education, EducationalID issuance (completed), Educational achievement issuance (completed), Generic EAA verification (completed)
* **Target groups and end-user roles**:
  Students selected from Universidad de Málaga, academic administrative staff, registry office personnel
* **Electronic Attestations of Attributes (EAAs) involved**:
  PID (Person Identification Data), EducationalID, Educational Achievement (EAAs: Microcredentials)
* **Institutional systems/databases connected**:
  UMA authentic source databases (academic records), identity verification system, student information system
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
    did:ebsi:zrfdezKaU79hJREcBXa39gR
    ```
  * **Verifier DID**:

    ```
    did:ebsi:zrfdezKaU79hJREcBXa39gR
    ```
  * **Issuer public key reference (PKI)**:

    ```
    Subject CN: lspuma.uma.es
    Organization: University of Málaga
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
  * Spanish national higher education regulations
  * Andalusian regional education regulations
* **Risk management**:
  Risk of incorrect identity matching (medium likelihood/high impact) mitigated via identity verification protocols; risk of user confusion (medium likelihood/medium impact) mitigated via training and support
* **Credential lifecycle management**:

  * Revocation: Implemented via EBSI Trust Registry
  * Suspension: Implemented via institutional controls
* **Infrastructure readiness**:

  * Test environment operational with ATOS/IZERTIS integration
  * Production readiness: Achieved
* **Training and onboarding**:
  Students and approximately 4 administrative staff trained
* **Issue escalation**:

  * SPOC contact: Victoriano Giralt at SGAD
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
  did:ebsi:zrfdezKaU79hJREcBXa39gR
  ```
* **Verifier DID and metadata**:

  ```
  did:ebsi:zrfdezKaU79hJREcBXa39gR
  ```
* **Issuer public key reference (PKI)**:

  ```
  -----BEGIN CERTIFICATE-----
  [PKI Certificate for lspuma.uma.es - 3 certificate chain]
  Subject: C=ES, O=University of Málaga, CN=lspuma.uma.es
  Key Algorithm: EC (prime256v1)
  Signature Algorithm: ecdsa-with-SHA256
  -----END CERTIFICATE-----
  ```
* **Relying Party certificate**:
  Provided via DC4EU consolidated PKI infrastructure
* **Registry references**:
  EBSI Trust Registry entries (registered), Spanish Sectorial EAA Catalogue managed by SGAD
* **PID credentials used**:
  Spanish national eIDAS 2.0 compliant PID credentials
* **Proof of wallet compatibility tests**:
  Integration testing completed with EUDIW by IZERTIS

---

## 5. Implementation and Testing Progress

* **Scenario status**: Completed
* **Number of users onboarded**:
  33 Staff successfully onboarded for comprehensive credential testing
* **Credentials issued**:
  PID (Person Identification Data), EducationalID, Educational Achievement (Microcredentials)
* **Credentials verified**:
  PID verification completed during PID retrieval user journey, EducationalID verified, Educational Achievement (Microcredentials) verified
* **Successes**:
  Successful PKI certificate deployment, ATOS/IZERTIS integration completed, EBSI DID registration completed (did:ebsi:zrfdezKaU79hJREcBXa39gR), PID retrieval user journey executed successfully, comprehensive educational credential issuance and verification workflows demonstrated, effective integration with Spanish governance framework
* **Issues encountered**:
  Minor initial configuration requirements for Andalusian regional context, successfully resolved
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
  * Educational Achievement (Microcredentials) issuance and verification completed
  * Student onboarding process effective
  * W3C Verifiable Credentials implementation successful
  * Spanish regulatory compliance achieved
  * Andalusian regional requirements met
* **What did not work and why**:
  * Minor performance considerations for scaling beyond pilot scope
  * Some initial user training requirements for digital credential concepts
* **Feedback from users**:
  Positive response from students, particular appreciation for microcredential digitisation and potential for academic mobility within Spain and Europe
* **Impact on user experience and feasibility**:
  Demonstrates successful feasibility of hybrid trust model approach for Spanish university context. Strong potential demonstrated for enhancing student mobility and credential recognition across Andalusian universities and Europe.

---

## 7. Evidence Archive and References

* **Screenshots or logs**:
  Available in DC4EU workspace: Spain-UMA folder
* **Credential samples**:
  EducationalID and Microcredential samples (redacted) available for review
* **Links to shared environment/demo**:
  https://lspuma.uma.es (DNS endpoint operational)
* **Documents or repositories**:
  UMA scenario characterisation documents, technical integration specifications
* **KPI data submission details**:
  Weekly reports to WP5 using DC4EU structured templates

---

## 8. Next Steps and Recommendations

* **Pending actions**:
  * Performance optimisation for larger-scale deployment across university
  * Documentation of lessons learned for other Andalusian universities
  * Cross-border verification testing with additional European institutions
  * Preparation for full university deployment
* **Recommendations for future pilots or replication**:
  * Early integration with regional Spanish governance frameworks
  * Focus on microcredential applications for enhanced student flexibility
  * Standardise Spanish university credential formats
  * Implement comprehensive training programmes for Spanish university contexts

---

## 9. Summary of End-User Feedback

* General impressions:
  Positive reception from students, strong appreciation for digital transformation of academic credentials and microcredential innovations
* Ease of use of wallets and services:
  High usability reported, successful completion of all educational credential user journeys
* Challenges encountered:
  Initial learning curve for digital credential concepts, successfully addressed through training
* Suggestions for improvement:
  Request for additional microcredential types, interest in enhanced Spanish language support
* Willingness to use again:
  High willingness expressed, strong interest in expanding to other academic credentials and university-wide deployment

---

## 10. Summary of Piloting Agent Insights

* Feedback on support received:
  Excellent support from ATOS and IZERTIS technical teams, effective coordination through SGAD, strong collaboration with Spanish and Andalusian regulatory authorities
* Main barriers during implementation:
  Spanish and Andalusian regulatory context integration, minor technical optimisation requirements
* Lessons learned:
  Value of microcredential focus for student engagement, importance of regional regulatory alignment, effectiveness of ATOS/IZERTIS solution for Spanish university environments
* Observed impact and value:
  Demonstrates significant potential for transforming Spanish higher education credential management, strong foundation for enhancing Andalusian and European academic mobility
* Recommendations for scaling:
  * Expand implementation to other Andalusian universities
  * Standardise Spanish university credential formats
  * Develop comprehensive training materials for Spanish university adoption
  * Create clear integration pathways for Spanish higher education institutions
  * Focus on microcredential applications for maximum student engagement and flexibility