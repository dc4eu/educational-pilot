# DC4EU Deployment and Testing Scenarios Results Library (DTSRL) – Scenario: Edutus University (EDUTUS)

## 1. Scenario Identification

* **Piloting agent name**: Edutus University (EDUTUS)
* **Scenario title**: Educational Credential Issuance and Verification with Hybrid Trust Framework (ATOS/IZERTIS Solution)
* **Date of submission**: 11 July 2025
* **Point of contact (SPOC)**: Laki Balazs

---

## 2. Scenario Characterisation

* **User journeys implemented**:
  PID retrieval (completed), Onboarding in education, EducationalID issuance (completed), Educational achievement issuance (completed), Generic EAA verification (completed)
* **Target groups and end-user roles**:
  University students, academic administrative staff, registry office personnel
* **Electronic Attestations of Attributes (EAAs) involved**:
  PID (Person Identification Data), EducationalID, Educational Achievement (EAAs: University credentials, Professional certificates)
* **Institutional systems/databases connected**:
  Edutus University authentic source databases (academic records), identity verification system, student information system
* **Technical components used**:

  * **Pilot option**: Pilot2 (Hybrid Trust: Classical PKI + Decentralised PKI)
  * **Wallet(s)**: EUDI Wallet (EUDIW by IZERTIS)
  * **Issuer platform**: uSelf Issuer Agent (ATOS)
  * **Verifier platform**: uSelf Verifier (ATOS)
  * **PID Retrieval Service**: Hungarian national PID provider integration
* **Governance configuration**:

  * **Trust model**: Hybrid (X.509 PKI + DIDs + EBSI Trust Registries)
  * **Issuer DID**:

    ```
    did:ebsi:zoScne48KYqeJ4rJrfX8vXF
    ```
  * **Verifier DID**:

    ```
    did:ebsi:zoScne48KYqeJ4rJrfX8vXF
    ```
  * **Issuer public key reference (PKI)**:

    ```
    Subject CN: lspedutus.edutus.hu
    Organization: Edutus University
    Country: HU
    Algorithm: EC (Elliptic Curve)
    Key Size: 256 bits
    Security Level: Strong (256-bit EC equivalent to 3072-bit RSA)
    Certificate Chain: 3 certificate(s)
    ```
  * **Relying Party certificate**: Provided via DC4EU PKI infrastructure
  * **Registry references**: EBSI Trust Registry entries, Hungarian Sectorial EAA Catalogue
* **Monitoring and feedback mechanisms**:
  Online feedback surveys, weekly monitoring reports with KPIs, managed by SPOC

---

## 3. Legal, Organisational and Operational Details

* **Regulatory context**:

  * GDPR compliance
  * eIDAS2 alignment and regulation
  * Hungarian national higher education regulations
* **Risk management**:
  Risk of incorrect identity matching (medium likelihood/high impact) mitigated via identity verification protocols; risk of user confusion (medium likelihood/medium impact) mitigated via training and support
* **Credential lifecycle management**:

  * Revocation: Implemented via EBSI Trust Registry
  * Suspension: Implemented via institutional controls
* **Infrastructure readiness**:

  * Test environment operational with ATOS/IZERTIS integration
  * Production readiness: Achieved
* **Training and onboarding**:
  University students and approximately 3 administrative staff trained
* **Issue escalation**:

  * SPOC contact: Laki Balazs
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
  did:ebsi:zoScne48KYqeJ4rJrfX8vXF
  ```
* **Verifier DID and metadata**:

  ```
  did:ebsi:zoScne48KYqeJ4rJrfX8vXF
  ```
* **Issuer public key reference (PKI)**:

  ```
  -----BEGIN CERTIFICATE-----
  [PKI Certificate for lspedutus.edutus.hu - 3 certificate chain]
  Subject: C=HU, O=Edutus University, CN=lspedutus.edutus.hu
  Key Algorithm: EC (prime256v1)
  Signature Algorithm: ecdsa-with-SHA256
  -----END CERTIFICATE-----
  ```
* **Relying Party certificate**:
  Provided via DC4EU consolidated PKI infrastructure
* **Registry references**:
  EBSI Trust Registry entries (registered), Hungarian Sectorial EAA Catalogue
* **PID credentials used**:
  Hungarian national eIDAS 2.0 compliant PID credentials
* **Proof of wallet compatibility tests**:
  Integration testing completed with EUDIW by IZERTIS

---

## 5. Implementation and Testing Progress

* **Scenario status**: Completed
* **Number of users onboarded**:
  25 University students successfully onboarded for credential testing
* **Credentials issued**:
  PID (Person Identification Data), EducationalID, Educational Achievement (European Higher Education Diploma)
* **Credentials verified**:
  PID verification completed during PID retrieval user journey, EducationalID verified, Educational Achievement verified
* **Successes**:
  Successful PKI certificate deployment, ATOS/IZERTIS integration completed, EBSI DID registration completed (did:ebsi:zoScne48KYqeJ4rJrfX8vXF), PID retrieval user journey executed successfully, comprehensive educational credential issuance and verification workflows demonstrated, effective integration with Hungarian governance framework
* **Issues encountered**:
  Minor initial configuration requirements for Hungarian regulatory context, successfully resolved
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
  * Hungarian regulatory compliance achieved
* **What did not work and why**:
  * Minor performance considerations for scaling beyond pilot scope
  * Some initial user training requirements for digital credential concepts
* **Feedback from users**:
  Positive response from university students, appreciation for digital credential innovation and potential for academic mobility within Hungary and Europe
* **Impact on user experience and feasibility**:
  Demonstrates successful feasibility of hybrid trust model approach for Hungarian university context. Strong potential demonstrated for enhancing student mobility and credential recognition.

---

## 7. Evidence Archive and References

* **Screenshots or logs**:
  Available in DC4EU workspace: Hungary-EDUTUS folder
* **Credential samples**:
  EducationalID and University credential samples (redacted) available for review
* **Links to shared environment/demo**:
  https://lspedutus.edutus.hu (DNS endpoint operational)
* **Documents or repositories**:
  Edutus University scenario characterisation documents, technical integration specifications
* **KPI data submission details**:
  Weekly reports to WP5 using DC4EU structured templates

---

## 8. Next Steps and Recommendations

* **Pending actions**:
  * Performance optimisation for larger-scale deployment across university
  * Documentation of lessons learned for other Hungarian universities
  * Cross-border verification testing with additional European institutions
  * Preparation for full university deployment
* **Recommendations for future pilots or replication**:
  * Early integration with Hungarian governance frameworks
  * Standardise Hungarian university credential formats
  * Implement comprehensive training programmes for Hungarian university contexts

---

## 9. Summary of End-User Feedback

* General impressions:
  Positive reception from university students, strong appreciation for digital transformation of academic credentials
* Ease of use of wallets and services:
  High usability reported, successful completion of all educational credential user journeys
* Challenges encountered:
  Initial learning curve for digital credential concepts, successfully addressed through training
* Suggestions for improvement:
  Request for additional credential types, interest in enhanced Hungarian language support
* Willingness to use again:
  High willingness expressed, strong interest in expanding across university

---

## 10. Summary of Piloting Agent Insights

* Feedback on support received:
  Excellent support from ATOS and IZERTIS technical teams, effective coordination for Hungarian university context
* Main barriers during implementation:
  Hungarian regulatory context integration, minor technical optimisation requirements
* Lessons learned:
  Importance of Hungarian regulatory alignment, effectiveness of ATOS/IZERTIS solution for Hungarian university environments
* Observed impact and value:
  Demonstrates significant potential for transforming Hungarian higher education credential management
* Recommendations for scaling:
  * Expand implementation to other Hungarian universities
  * Standardise Hungarian university credential formats
  * Develop comprehensive training materials for Hungarian university adoption
  * Create clear integration pathways for Hungarian higher education institutions