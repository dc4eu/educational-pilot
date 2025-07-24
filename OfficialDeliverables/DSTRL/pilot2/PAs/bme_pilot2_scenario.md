# DC4EU Deployment and Testing Scenarios Results Library (DTSRL) – Scenario: Budapest University of Technology and Economics (BME)

## 1. Scenario Identification

* **Piloting agent name**: Budapest University of Technology and Economics (BME)
* **Scenario title**: Educational Credential Issuance and Verification with Hybrid Trust Framework (ATOS/IZERTIS Solution)
* **Date of submission**: 11 July 2025
* **Point of contact (SPOC)**: Imre Kocsis

---

## 2. Scenario Characterisation

* **User journeys implemented**:
  PID retrieval (completed), Onboarding in education, EducationalID issuance (completed), Educational achievement issuance (completed), Generic EAA verification (completed)
* **Target groups and end-user roles**:
  Graduate students from BME's Critical Systems Research Group, academic administrative staff, blockchain lab personnel
* **Electronic Attestations of Attributes (EAAs) involved**:
  PID (Person Identification Data), EducationalID, Educational Achievement (EAAs: European Higher Education Diploma)
* **Institutional systems/databases connected**:
  BME authentic source databases (academic records), identity verification system.
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
    did:ebsi:zn2SoctQ3TmBgPbiTWftF42
    ```
  * **Verifier DID**:

    ```
    did:ebsi:zn2SoctQ3TmBgPbiTWftF42
    ```
  * **Issuer public key reference (PKI)**:

    ```
    Subject CN: lspbme.cloud.bme.hu
    Organization: Budapest University of Technology and Economics
    Country: HU
    Algorithm: EC (Elliptic Curve)
    Key Size: 256 bits
    Security Level: Strong (256-bit EC equivalent to 3072-bit RSA)
    Certificate Chain: 3 certificate(s)
    ```
  * **Relying Party certificate**: Provided via DC4EU PKI infrastructure
  * **Registry references**: EBSI Trust Registry entries, Hungarian Sectorial EAA Catalogue
* **Monitoring and feedback mechanisms**:
  Online feedback surveys, weekly monitoring reports with KPIs, managed by SPOC with blockchain lab expertise

---

## 3. Legal, Organisational and Operational Details

* **Regulatory context**:

  * GDPR compliance
  * eIDAS2 alignment and regulation
  * Hungarian national higher education regulations
* **Risk management**:
  Risk of incorrect identity matching (medium likelihood/high impact) mitigated via identity verification protocols; risk of user confusion (medium likelihood/medium impact) mitigated via training and support; additional blockchain security considerations addressed through research group expertise
* **Credential lifecycle management**:

  * Revocation: Implemented via EBSI Trust Registry
  * Suspension: Implemented via institutional controls
* **Infrastructure readiness**:

  * Test environment operational with ATOS/IZERTIS integration
  * Production readiness: Achieved with blockchain lab infrastructure support
* **Training and onboarding**:
  Research group members and approximately 3 administrative staff trained, leveraging existing blockchain expertise
* **Issue escalation**:

  * SPOC contact: Imre Kocsis (kocsis.imre@vik.bme.hu)
  * Blockchain lab lead support, Critical Systems Research Group
  * Department of AI and Systems Engineering
* **Success indicators and KPIs**:

  * Successful onboarding completion rate
  * EAA issuance rate
  * EAA verification success rate
  * User satisfaction measured via structured surveys
  * Technical performance metrics from blockchain lab

---

## 4. Trust Model Onboarding Evidences

* **Issuer DID and metadata**:

  ```
  did:ebsi:zn2SoctQ3TmBgPbiTWftF42
  ```
* **Verifier DID and metadata**:

  ```
  did:ebsi:zn2SoctQ3TmBgPbiTWftF42
  ```
* **Issuer public key reference (PKI)**:

  ```
  -----BEGIN CERTIFICATE-----
  [PKI Certificate for lspbme.cloud.bme.hu - 3 certificate chain]
  Subject: C=HU, O=Budapest University of Technology and Economics, CN=lspbme.cloud.bme.hu
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
  Integration testing completed with EUDIW by IZERTIS, enhanced testing through blockchain lab capabilities

---

## 5. Implementation and Testing Progress

* **Scenario status**: Completed
* **Number of users onboarded**:
  Research group members and graduate students successfully onboarded
* **Credentials issued**:
  PID (Person Identification Data), EducationalID, Educational Achievement (Microcredentials)
* **Credentials verified**:
  PID verification completed during PID retrieval user journey, EducationalID verified, Educational Achievement (Microcredentials) verified, enhanced verification testing through blockchain lab
* **Successes**:
  Successful PKI certificate deployment, ATOS/IZERTIS integration completed, EBSI DID registration completed (did:ebsi:zn2SoctQ3TmBgPbiTWftF42), PID retrieval user journey executed successfully, comprehensive educational credential issuance and verification workflows demonstrated, blockchain lab expertise enhanced implementation quality
* **Issues encountered**:
  Minor initial integration considerations for Hungarian regulatory context, successfully resolved through research group expertise
* **Deviation from plan**:
  No significant deviations, implementation proceeded as planned with enhanced technical validation through blockchain lab capabilities

---

## 6. Testing Results and Observations

* **What worked as expected**:
  * PKI certificate infrastructure deployment successful
  * ATOS issuer platform integration completed
  * IZERTIS wallet integration functional
  * PID retrieval user journey executed successfully
  * EducationalID issuance and verification completed
  * Educational Achievement (Microcredentials) issuance and verification completed
  * Research group onboarding process efficient
  * W3C Verifiable Credentials implementation successful
  * Hungarian regulatory compliance achieved
  * Enhanced technical validation through blockchain lab expertise
* **What did not work and why**:
  * Minor performance considerations for very large-scale deployment
  * Some optimisation opportunities identified through blockchain lab analysis
* **Feedback from users**:
  Highly positive response from research group members, particular appreciation for technical sophistication and blockchain-related credential applications
* **Impact on user experience and feasibility**:
  Demonstrates successful feasibility of hybrid trust model approach enhanced by blockchain expertise. Strong potential demonstrated for advanced technical education credential applications and research collaboration credentials.

---

## 7. Evidence Archive and References

* **Screenshots or logs**:
  Available in DC4EU workspace: Hungary-BME folder
* **Credential samples**:
  EducationalID and Microcredential samples (redacted) available for review
* **Links to shared environment/demo**:
  https://lspbme.cloud.bme.hu (DNS endpoint operational)
* **Documents or repositories**:
  BME scenario characterisation documents, technical integration specifications, blockchain lab analysis reports
* **KPI data submission details**:
  Weekly reports to WP5 using DC4EU structured templates, enhanced with blockchain lab metrics

---

## 8. Next Steps and Recommendations

* **Pending actions**:
  * Performance optimisation for larger-scale deployment
  * Documentation of blockchain lab insights for other technical institutions
  * Cross-border verification testing with additional European technical universities
  * Research collaboration credential development
* **Recommendations for future pilots or replication**:
  * Leverage blockchain lab expertise for enhanced technical validation
  * Focus on research collaboration credentials for international technical cooperation
  * Early integration with Hungarian higher education regulatory framework
  * Standardise technical education credential formats with blockchain considerations
  * Develop advanced training programmes for technical university contexts

---

## 9. Summary of End-User Feedback

* General impressions:
  Excellent reception from research group members, strong appreciation for technical sophistication and blockchain technology integration
* Ease of use of wallets and services:
  Very high usability reported, successful completion of all technical credential user journeys
* Challenges encountered:
  Minimal challenges due to technical expertise of user base, some interest in advanced customisation features
* Suggestions for improvement:
  Request for research collaboration credential types, interest in blockchain analytics integration, advanced technical features
* Willingness to use again:
  Very high willingness expressed, strong interest in expanding to research collaboration and advanced technical credential applications

---

## 10. Summary of Piloting Agent Insights

* Feedback on support received:
  Excellent support from ATOS and IZERTIS technical teams, enhanced by internal blockchain lab expertise, effective coordination for technical university context
* Main barriers during implementation:
  Hungarian regulatory context integration, minor optimisation opportunities identified through technical analysis
* Lessons learned:
  Value of blockchain lab expertise for enhanced implementation, importance of technical user base for advanced credential applications, effectiveness of ATOS/IZERTIS solution for technical university environments
* Observed impact and value:
  Demonstrates significant potential for transforming technical higher education credential management, strong foundation for research collaboration and advanced technical education credentials
* Recommendations for scaling:
  * Leverage blockchain lab expertise for other technical university implementations
  * Develop research collaboration credential frameworks
  * Standardise technical education credential formats with blockchain considerations
  * Create advanced training materials for technical university adoption
  * Establish clear integration pathways for Central European technical institutions
  * Focus on advanced technical credential applications for maximum innovation impact