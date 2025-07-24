# DC4EU Deployment and Testing Scenarios Results Library (DTSRL) – Scenario: Politehnica University of Timisoara (UPT)

## 1. Scenario Identification

* **Piloting agent name**: Politehnica University of Timisoara (UPT)
* **Scenario title**: Educational Credential Issuance and Verification with Hybrid Trust Framework (ATOS/IZERTIS Solution)
* **Date of submission**: 23 July 2025
* **Point of contact (SPOC)**: Diana Andone

---

## 2. Scenario Characterisation

* **User journeys implemented**:
  PID retrieval (completed), Onboarding in education, EducationalID issuance (completed), Educational achievement issuance (completed), Generic EAA verification (completed)
* **Target groups and end-user roles**:
  28 students who have completed all the activities in the E³UDRES² – Ent-r-e-novators PhD Summer School at UPT and agreed to the GDPR and the EBSI information and done the minimum training
* **Electronic Attestations of Attributes (EAAs) involved**:
  PID (Person Identification Data), EducationalID, Educational Achievement (EAA: Micro-credential)
* **Institutional systems/databases connected**:
  UPT authentic source databases (academic records), identity verification system, student information system
* **Technical components used**:

  * **Pilot option**: Pilot2 (Hybrid Trust: Classical PKI + Decentralised PKI)
  * **Wallet(s)**: EUDI Wallet (EUDIW by IZERTIS)
  * **Issuer platform**: uSelf Issuer Agent (ATOS)
  * **Verifier platform**: uSelf Verifier (ATOS)
  * **PID Retrieval Service**: uSelf PID Generator
* **Governance configuration**:

  * **Trust model**: Hybrid (X.509 PKI + DIDs + EBSI Trust Registries)
  * **Issuer DID**:

    ```
    did:ebsi:ztoPE2wdSYBuzGt7r8g5wAX
    ```
  * **Verifier DID**:

    ```
    did:ebsi:ztoPE2wdSYBuzGt7r8g5wAX
    ```
  * **Issuer public key reference (PKI)**:

    ```
    Subject CN: lspupt.upt.ro
    Organization: Politehnica University of Timisoara
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
* **Risk management**:
  * Risk of incorrect identity matching (medium likelihood/high impact) mitigated via identity verification protocols; risk of user confusion (medium likelihood/medium impact) mitigated via training and support

* **Credential lifecycle management**:
  * Revocation: Implemented via EBSI Trust Registry
  * Suspension: Implemented via institutional controls

* **Infrastructure readiness**:
  * Test environment operational with ATOS/IZERTIS integration
  * Production readiness: Achieved

* **Training and onboarding**:
  28 students and 3 administrative staff trained

* **Issue escalation**:
  * SPOC contact: Diana Andone [diana.andone@upt.ro](mailto:diana.andone@upt.ro)
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
  did:ebsi:ztoPE2wdSYBuzGt7r8g5wAX
  ```
* **Verifier DID and metadata**:

  ```
  did:ebsi:ztoPE2wdSYBuzGt7r8g5wAX
  ```
* **Issuer public key reference (PKI)**:

  ```
  -----BEGIN CERTIFICATE-----
  [PKI Certificate for lspupt.upt.ro - 3 certificate chain]
  Subject: C=RO, O=Politehnica University of Timisoara, CN=lspupt.upt.ro
  Key Algorithm: EC (prime256v1)
  Signature Algorithm: ecdsa-with-SHA256
  -----END CERTIFICATE-----
  ```
* **Relying Party certificate**:
  Provided via DC4EU consolidated PKI infrastructure
* **Registry references**:
  EBSI Trust Registry entries (registered), Romanian Sectorial EAA Catalogue managed by SGAD
* **PID credentials used**:
  Romanian national eIDAS 2.0 compliant PID credentials
* **Proof of wallet compatibility tests**:
  Integration testing completed with EUDIW by IZERTIS

---

## 5. Implementation and Testing Progress

* **Scenario status**: Completed
* **Number of users onboarded**:
  28 students who have completed all the activities in the E³UDRES² – Ent-r-e-novators PhD Summer School at UPT and agreed to the GDPR and the EBSI information and done the minimum training
* **Credentials issued**:
  PID (Person Identification Data), EducationalID, Educational Achievement (Micro-credential)
* **Credentials verified**:
  PID verification completed during PID retrieval user journey, EducationalID verified, Educational Achievement (Micro-credential) verified
  11 users successfully verified the credentials
* **Successes**:
  Successful PKI certificate deployment, ATOS/IZERTIS integration completed, EBSI DID registration completed (did:ebsi:ztoPE2wdSYBuzGt7r8g5wAX), PID retrieval user journey executed successfully, comprehensive educational credential issuance and verification workflows demonstrated, effective graduate student engagement
* **Issues encountered**:
  Minor initial configuration requirements for Romanian regulatory context, successfully resolved
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
  * Educational Achievement (Micro-credential) issuance and verification completed
  * Graduate student onboarding process effective
  * W3C Verifiable Credentials implementation successful
  * Romanian regulatory compliance achieved
* **What did not work and why**:
  * Minor performance considerations for scaling beyond pilot scope
  * Some initial user familiarisation requirements for digital credential concepts
* **Feedback from users**:
  Positive response from graduate students, particular appreciation for Micro-credential digitisation and potential for international academic mobility, negative for the complicated method for those with minimum digital skills, without training only a few could have succeeded
* **Impact on user experience and feasibility**:
  Demonstrates successful feasibility of hybrid trust model approach for Romanian technical university context. Strong potential demonstrated for enhancing graduate student mobility and credential recognition across Europe.

---

## 7. Evidence Archive and References

* **Screenshots or logs**:
  Available at the following links: 
  * [DC4EU Workspace romania-upt folder](../../../../DSTRL/scenarios/Pilot2/pilot2-central/romania-upt/)
  * UPT proofs (larger files) - upon request
* **Credential samples**:
  EducationalID and Micro-credential samples (redacted) available for review
* **Links to shared environment/demo**:
  https://lspupt.upt.ro (DNS endpoint operational)
* **Documents or repositories**:
  UPT scenario characterisation documents, technical integration specifications
* **KPI data submission details**:
  Weekly reports to WP5 using DC4EU structured templates

---

## 8. Next Steps and Recommendations

* **Pending actions**:
  * Performance optimisation for larger-scale deployment across university
  * Documentation of lessons learned for other Romanian technical universities
  * Cross-border verification testing with additional European institutions
  * Preparation for full university deployment
* **Recommendations for future pilots or replication**:
  * Focus on graduate students provides clear value demonstration for international mobility
  * Early integration with Romanian higher education regulatory framework
  * Standardise Micro-credential digital formats across European technical universities
  * Implement comprehensive training programmes for technical university contexts

---

## 9. Summary of End-User Feedback

* General impressions:
  Very positive reception from students, strong appreciation for digital transformation of academic credentials
* Ease of use of wallets and services:
  High usability reported, successful completion of all educational credential user journeys
* Challenges encountered:
  Initial learning curve for digital credential concepts and method, successfully addressed through training
* Suggestions for improvement:
  Request for additional credential types (research certificates, project portfolios), interest in enhanced mobile features
* Willingness to use again:
  Very high willingness expressed, strong interest in expanding to other academic credentials and university-wide deployment

---

## 10. Summary of Piloting Agent Insights

* Feedback on support received:
  Excellent support from ATOS and IZERTIS technical teams, effective coordination through SGAD, strong collaboration with Romanian regulatory authorities
* Main barriers during implementation:
  Romanian regulatory context integration, minor technical optimisation requirements for technical university context
* Lessons learned:
  Value of focusing on students for international mobility use cases, importance of Micro-credential digitisation, effectiveness of ATOS/IZERTIS solution for technical university environments
* Observed impact and value:
  Demonstrates significant potential for transforming Romanian technical higher education credential management, strong foundation for enhancing European technical education mobility
* Recommendations for scaling:
  * Expand implementation to other Romanian technical universities
  * Expand implementation for the E³UDRES² European Universities Alliance and implementation in its Arena
  * Standardise technical education credential formats across European technical universities
  * Develop comprehensive training materials for technical university adoption
  * Create clear integration pathways for Romanian higher education institutions
  * Focus on graduate-level credentials for maximum international mobility impact
