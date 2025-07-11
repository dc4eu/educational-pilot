# DC4EU Deployment and Testing Scenarios Results Library (DTSRL) – Scenario: University of Bologna (UNIBO)

## 1. Scenario Identification

* **Piloting agent name**: University of Bologna (UNIBO)
* **Scenario title**: EducationalID and Higher Education Diploma Credential Issuance & Verification with Hybrid Trust Framework
* **Date of submission**: 11 July 2025
* **Point of contact (SPOC)**: Sergio Storari, SGAD

---

## 2. Scenario Characterisation

* **User journeys implemented**:
  PID retrieval (completed), Onboarding in education, EducationalID issuance (completed), Higher Education Diploma issuance (completed), Generic EAA verification (completed)
* **Target groups and end-user roles**:
  25 graduate students selected initially from UNIBO, final-year students, administrative staff
* **Electronic Attestations of Attributes (EAAs) involved**:
  PID (Person Identification Data), EducationalID, Higher Education Diploma (HED), Microcredentials, Diploma Supplement, Master degree
* **Institutional systems/databases connected**:
  UNIBO authentic source databases (academic records), identity verification system, Keycloak, PID generator, Verifier GUI, Datastore
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
    did:ebsi:zZUZyjvAjwebjJrXkYTnZLS
    ```
  * **Verifier DID**:

    ```
    did:ebsi:zZUZyjvAjwebjJrXkYTnZLS
    ```
  * **Issuer public key reference (PKI)**:

    ```
    Subject CN: lspdc4edu.unibo.it
    Organization: University of Bologna
    Country: IT
    Algorithm: EC (Elliptic Curve)
    Key Size: 256 bits
    Security Level: Strong (256-bit EC equivalent to 3072-bit RSA)
    Certificate Chain: 3 certificate(s)
    ```
  * **Relying Party certificate**: Provided via DC4EU PKI infrastructure
  * **Registry references**: EBSI Trust Registry entries, Italian Sectorial EAA Catalogue via SGAD
* **Monitoring and feedback mechanisms**:
  Online feedback surveys, weekly monitoring reports with KPIs, managed by SPOC

---

## 3. Legal, Organisational and Operational Details

* **Regulatory context**:

  * GDPR compliance
  * eIDAS2 alignment and regulation
  * Italian national higher education regulations
* **Risk management**:
  Risk of incorrect identity matching (medium likelihood/high impact) mitigated via identity verification protocols; risk of user confusion (medium likelihood/medium impact) mitigated via training and support; credential revocation/removal not yet fully supported in EUDIW
* **Credential lifecycle management**:

  * Revocation: Implemented via EBSI Trust Registry (pending full EUDIW support)
  * Suspension: Implemented via institutional controls
* **Infrastructure readiness**:

  * Test environment operational with ATOS/IZERTIS integration
  * Production readiness: Partial (Datastore with 30 pilot users in demo setup)
* **Training and onboarding**:
  25 graduate students and approximately 5 administrative staff trained, demo session with master's students completed
* **Issue escalation**:

  * SPOC contact: Sergio Storari via SGAD
  * WP5 technical partners support channel
* **Success indicators and KPIs**:

  * Number of credentials issued, verified, and validated cross-border
  * Successful onboarding completion rate
  * EAA issuance rate
  * User satisfaction measured via structured surveys

---

## 4. Trust Model Onboarding Evidences

* **Issuer DID and metadata**:

  ```
  did:ebsi:zZUZyjvAjwebjJrXkYTnZLS
  ```
* **Verifier DID and metadata**:

  ```
  did:ebsi:zZUZyjvAjwebjJrXkYTnZLS
  ```
* **Issuer public key reference (PKI)**:

  ```
  -----BEGIN CERTIFICATE-----
  [PKI Certificate for lspdc4edu.unibo.it - 3 certificate chain]
  Subject: C=IT, O=University of Bologna, CN=lspdc4edu.unibo.it
  Key Algorithm: EC (prime256v1)
  Signature Algorithm: ecdsa-with-SHA256
  -----END CERTIFICATE-----
  ```
* **Relying Party certificate**:
  Provided via DC4EU consolidated PKI infrastructure
* **Registry references**:
  EBSI Trust Registry entries (registered), Italian Sectorial EAA Catalogue managed by SGAD
* **PID credentials used**:
  Italian national eIDAS 2.0 compliant PID credentials via uSelf PID Generator
* **Proof of wallet compatibility tests**:
  Integration testing completed with EUDIW via TestFlight/Google Play

---

## 5. Implementation and Testing Progress

* **Scenario status**: Completed
* **Number of users onboarded**:
  25 graduate students selected and successfully onboarded
* **Credentials issued**:
  PID (Person Identification Data), EducationalID, Higher Education Diploma (HED), Microcredentials, Diploma Supplement
* **Credentials verified**:
  PID verification completed during PID retrieval user journey, EducationalID verified, Higher Education Diploma verified, cross-border verification testing completed
* **Successes**:
  Successful PKI certificate deployment, ATOS/IZERTIS integration completed, EBSI DID registration completed (did:ebsi:zZUZyjvAjwebjJrXkYTnZLS), PID retrieval user journey executed successfully, comprehensive credential issuance and verification workflows demonstrated, demo session with master's students successful
* **Issues encountered**:
  Credential lifecycle management limitations in EUDIW (deletion/removal pending), minor performance considerations for large-scale deployment
* **Deviation from plan**:
  No significant deviations, implementation proceeded as planned with successful demonstration of all key functionalities

---

## 6. Testing Results and Observations

* **What worked as expected**:
  * PKI certificate infrastructure deployment successful
  * ATOS issuer platform integration completed
  * IZERTIS wallet integration functional via TestFlight/Google Play
  * PID retrieval user journey executed successfully with verification
  * EducationalID issuance and verification completed
  * Higher Education Diploma issuance and verification completed
  * Cross-border verification capabilities demonstrated
  * Student onboarding process smooth
  * W3C Verifiable Credentials implementation successful
  * Datastore setup with 30 pilot users functional
* **What did not work and why**:
  * Credential lifecycle management (deletion/removal) limitations in current EUDIW version
  * Some performance optimisation needed for larger-scale deployment
* **Feedback from users**:
  Highly positive response from graduate students participating in demo sessions. Students appreciated the seamless integration of academic credentials with digital wallet technology.
* **Impact on user experience and feasibility**:
  Demonstrates successful feasibility of hybrid trust model approach with complete credential lifecycle management for Italian higher education context. Strong potential demonstrated for enhancing student mobility and credential recognition across Europe.

---

## 7. Evidence Archive and References

* **Screenshots or logs**:
  Available in DC4EU workspace: Italy-UNIBO folder
* **Credential samples**:
  EducationalID, Higher Education Diploma, and Microcredential samples (redacted) available for review
* **Links to shared environment/demo**:
  https://lspdc4eu.unibo.it (DNS endpoint operational)
* **Documents or repositories**:
  UNIBO scenario characterisation documents, technical integration specifications, Datastore configuration
* **KPI data submission details**:
  Weekly reports to WP5 using DC4EU structured templates

---

## 8. Next Steps and Recommendations

* **Pending actions**:
  * Performance optimisation for larger-scale deployment
  * Enhancement of credential lifecycle management capabilities
  * Cross-border verification testing with additional European institutions
  * Preparation for production deployment
* **Recommendations for future pilots or replication**:
  * Early provision of comprehensive credential lifecycle management capabilities
  * Standardise demo session procedures for student engagement
  * Establish clear performance benchmarks for large-scale deployment
  * Implement enhanced monitoring and analytics capabilities

---

## 9. Summary of End-User Feedback

* General impressions:
  Excellent reception from graduate students, strong appreciation for digital transformation of academic credential management
* Ease of use of wallets and services:
  Very positive feedback on EUDIW usability, successful completion of all user journeys
* Challenges encountered:
  Initial learning curve for digital wallet concepts, successfully addressed through demonstration sessions
* Suggestions for improvement:
  Request for enhanced credential lifecycle management features, interest in mobile app optimisation
* Willingness to use again:
  Very high willingness expressed, strong interest in production deployment across university

---

## 10. Summary of Piloting Agent Insights

* Feedback on support received:
  Excellent support from ATOS and IZERTIS technical teams, effective coordination through SGAD, strong collaboration with WP5 technical partners
* Main barriers during implementation:
  Limited credential lifecycle management capabilities in current wallet version, need for performance optimisation
* Lessons learned:
  Importance of comprehensive demo sessions for user engagement, value of hybrid trust model for Italian academic context, need for early performance planning
* Observed impact and value:
  Demonstrates significant potential for transforming Italian higher education credential management, strong foundation for European academic mobility initiatives
* Recommendations for scaling:
  * Enhance credential lifecycle management capabilities across all wallet implementations
  * Establish performance benchmarks and optimisation procedures
  * Develop comprehensive training materials for institutional adoption
  * Create clear integration pathways for Italian higher education institutions