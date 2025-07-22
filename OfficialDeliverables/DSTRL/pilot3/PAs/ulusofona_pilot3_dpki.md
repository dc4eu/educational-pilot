
# DC4EU Deployment and Testing Scenarios Results Library (DTSRL) – Scenario: Universidade Lusófona (COFAC)

## 1. Scenario Identification

* **Piloting agent name**: Lusófona University (COFAC)
* **Scenario title**: Student EDUCATIONAL ID and European Student Card Issuance with Hybrid Trust Framework (ATOS/IZERTIS Dockerised Solution)
* **Date of submission**: 22 July 2025
* **Point of contact (SPOC)**: Paulo Ferreira, Manuel Pereira

---

## 2. Scenario Characterisation

* **User journeys implemented**:
  PID retrieval (completed), Issuance of EDUCATIONAL ID (completed), Issuance of European Student Card (completed), Generic EAA verification (completed)
* **Target groups and end-user roles**:
  University students from Computing Engineering and administrative staff
* **Electronic Attestations of Attributes (EAAs) involved**:
  PID (Person Identification Data), EducationalID, European Student Card
* **Institutional systems/databases connected**:
  All records were manually uploaded using the Source of Truth interface. 
* **Technical components used**:

  * **Pilot option**: Pilot2 (Hybrid Trust: Classical PKI + Decentralised PKI)
  * **Wallet(s)**: EUDI Wallet (EUDIW by IZERTIS)
  * **Issuer platform**: uSelf Issuer Agent (ATOS)
  * **Verifier platform**: uSelf Verifier (ATOS)
  * **PID Retrieval Service**: uSelf PID Agent
* **Governance configuration**:

  * **Trust model**: Hybrid (X.509 PKI + DIDs + EBSI Trust Registries)
  * **Issuer DID**:

    ```
    did:ebsi:zrmS9sGhR5J6vHu2gzMkN8t
    ```
  * **Verifier DID**:

    ```
    did:ebsi:zrmS9sGhR5J6vHu2gzMkN8t
    ```
  * **Issuer public key reference (PKI)**:

    ```
    Subject CN: lspulusofona.ulusofona.pt
    Organization: Universidade Lusófona
    Country: PT
    Algorithm: EC (Elliptic Curve)
    Key Size: 256 bits
    Security Level: Strong (256-bit EC equivalent to 3072-bit RSA)
    Certificate Chain: 3 certificate(s)
    ```
  * **Relying Party certificate**: Provided via DC4EU PKI infrastructure
  * **Registry references**: EBSI Trust Registry entries, Portuguese Sectorial EAA Catalogue via SGAD
* **Monitoring and feedback mechanisms**:
  Online feedback surveys, biweekly monitoring reports with KPIs, managed by SPOC

---

## 3. Legal, Organisational and Operational Details

* **Regulatory context**:

  * GDPR compliance
  * Portuguese national and higher education regulations (AE3S, DGES)
  * eIDAS2 framework alignment
* **Risk management**:
  Risk of incorrect identity matching (medium likelihood/high impact) mitigated via identity verification protocols; risk of user confusion (medium likelihood/medium impact) mitigated via training and support; credential revocation/removal not yet fully supported in EUDIW
* **Credential lifecycle management**:

  * Revocation: Processes defined for issuance, updates, revocation, renewal, and suspension of credentials
  * Suspension: Implemented via Source of Truth from Docker (Issuer interface)
* **Infrastructure readiness**:

  * Integration with SAML / SSO was not possible through keycloak. All test data was prepared from our system and uploaded into the test enviroment.
  * 
* **Training and onboarding**:
  Training was provided on site before pilot sessions. Students and staff were presented with the EUDI wallet, digital credentials and eiDAS2. The goal of the pilot was explained. 
* **Issue escalation**:

  * SPOC contacts: Paulo Ferreira (paulo.ferreira@ulusofona.pt)
  * WP5 technical partners support channel
* **Success indicators and KPIs**:

  * Successful PID issuance
  * ID card issuance rate (25)
  * EDUCATIONAL ID (25)
  * European Student Card issuance (25) 
  * User satisfaction measured via structured survey

---

## 4. Trust Model Onboarding Evidences

* **Issuer DID and metadata**:

  ```
  did:ebsi:zrmS9sGhR5J6vHu2gzMkN8t
  ```
* **Verifier DID and metadata**:

  ```
  did:ebsi:zrmS9sGhR5J6vHu2gzMkN8t
  ```
* **Issuer public key reference (PKI)**:

  ```
  -----BEGIN CERTIFICATE-----
  [PKI Certificate for lspulusofona.ulusofona.pt - 3 certificate chain]
  Subject: C=PT, O=Universidade Lusófona
  Key Algorithm: EC (prime256v1)
  Signature Algorithm: ecdsa-with-SHA256
  -----END CERTIFICATE-----
  ```
* **Relying Party certificate**:
  Provided via DC4EU consolidated PKI infrastructure
* **Registry references**:
  EBSI Trust Registry entries (registered), Portuguese Sectorial EAA Catalogue managed by SGAD
* **PID credentials used**:
  uSelf PID Agent
* **Proof of wallet compatibility tests**:
  Integration testing completed with EUDIW by IZERTIS

---

## 5. Implementation and Testing Progress

* **Scenario status**: Completed
* **Number of users onboarded**:
  25 students successfully onboarded for diploma issuance simulation
* **Credentials issued**:
  PID (Person Identification Data), EducationalID, European Student Card.
* **Credentials verified**:
  PID (Person Identification Data), EducationalID, European Student Card.
* **Successes**:
Successful PKI certificate deployment, ATOS/IZERTIS integration completed, EBSI DID registration completed (did:ebsi:zrmS9sGhR5J6vHu2gzMkN8t), PID retrieval user journey executed successfully
* **Issues encountered**:
  The European Student Card was sucessfully issued by the issuer agent but an error (500) prevent it to be issued to the user wallet after PID verification.
* **Deviation from plan**:
  No significant deviations, implementation proceeded as planned with successful completion of all key student lifecycle objectives

---

## 6. Testing Results and Observations

* **What worked as expected**:
  * PKI certificate infrastructure deployment successful
  * EUDIW integration functional
  * PID retrieval user journey executed successfully
  * Educatinal ID credential issuance completed
  * European Student Card sucessfully created
  * W3C Verifiable Credentials implementation successful
* **What did not work and why**:
  * The availability of the test enviroment was done later than expected. The classes were over and was difficult to find available students for the testing sessions. 
  * The test enviroment was sometimes instable leading to errors during the test sessions
  * The inferface was not friendly
* **Feedback from users**:
  The students were motivated and curious about the process, wallets and credentials. They felt that by beeing part of the pilot they were also helping to build the future of credentials and trust in Europe.
* **Impact on user experience and feasibility**:
  Demonstrates successful feasibility of hybrid trust model approach for comprehensive Portuguese university student lifecycle management. Strong potential demonstrated for enhancing student services and international mobility.

---

## 7. Evidence Archive and References

* **Screenshots or logs**:
  Available in DC4EU workspace
* **Credential samples**:
  EducationalID, Student Card, and European Student Card available for review
* **Links to shared environment/demo**:
https://uself-keycloak.lspulusofona.ulusofona.pt/
https://uself-agent-web.lspulusofona.ulusofona.pt/
https://uself-issuer-agent.lspulusofona.ulusofona.pt/
https://uself-issuer-gui.lspulusofona.ulusofona.pt/
https://uself-verifier-gui.lspulusofona.ulusofona.pt/
https://uself-authentic-source.lspulusofona.ulusofona.pt/
https://uself-pid-generator.lspulusofona.ulusofona.pt/
https://uself-redis.lspulusofona.ulusofona.pt/
https://uself-postgres.lspulusofona.ulusofona.pt/
* **Documents or repositories**:
  Lusófona University scenario characterisation documents
* **KPI data submission details**:
  Biweekly progress reports with KPI tracking, using structured templates

---

## 8. Next Steps and Recommendations

* **Pending actions**:
  * Performance optimisation for larger-scale deployment across university
  * Documentation of lessons learned for other Portuguese universities
  * Cross-border verification testing with additional European institutions
  * Preparation for full university deployment via Helpdesk integration
* **Recommendations for future pilots or replication**:
  * Focus on complete student lifecycle provides comprehensive value demonstration
  * Early integration with Portuguese governance frameworks
  * Standardise university credential formats 
  * Implement comprehensive training programmes

---

## 9. Summary of End-User Feedback

* General impressions:
  Excellent reception from students across all lifecycle stages, strong appreciation for comprehensive digital transformation of student services
* Ease of use of wallets and services:
  Moderate to High usability reported, successful completion of all student lifecycle user journeys
* Challenges encountered:
  Initial learning curve for digital credential concepts, successfully addressed through comprehensive training and guidance
* Suggestions for improvement:
  Request for additional student service integrations, interest in enhanced Portuguese language support
* Willingness to use again:
  Very high willingness expressed, strong interest in expanding across all university services

---

## 10. Summary of Piloting Agent Insights

* Feedback on support received:
  Excellent support from technical teams, effective coordination for comprehensive student lifecycle implementation
* Main barriers during implementation:
  Portuguese regulatory context integration, minor technical optimisation requirements for comprehensive student services
* Lessons learned:
* Observed impact and value:
  Demonstrates significant potential for transforming Portuguese higher education student services and international mobility
* Recommendations for scaling:
  * Expand comprehensive student lifecycle approach to other Portuguese universities
  * Standardise European and Portuguese level university credential (should be the same) formats across all student services
  * Develop comprehensive training materials for university adoption and governance / policy makers awareness 
  * Create clear integration pathways for Portuguese higher education institutions aligned with National Agencies and National Ministeries
  * Focus on complete student lifecycle for maximum institutional transformation impact
  * Work closely with stakeholders and third parties involved with Higher Education ecosystem to improve interoperability of data and processes among Europe. 