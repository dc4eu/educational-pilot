# DC4EU Deployment and Testing Scenarios Results Library (DTSRL) – Scenario: Vytautas Magnus University (VMU)

## 1. Scenario Identification

* **Piloting agent name**: Vytautas Magnus University (VMU)
* **Scenario title**: Diploma Issuance and Verification with Hybrid Trust Framework (ATOS/IZERTIS Solution)
* **Date of submission**: 11 July 2025
* **Point of contact (SPOC)**: Tomas Krilavicius

---

## 2. Scenario Characterisation

* **User journeys implemented**:
  PID retrieval (completed), Diploma issuance (completed), Generic EAA verification (completed)
* **Target groups and end-user roles**:
  25 students selected for diploma issuance simulation, academic administrative staff, registry office personnel
* **Electronic Attestations of Attributes (EAAs) involved**:
  PID (Person Identification Data), Diploma
* **Institutional systems/databases connected**:
  VMU authentic source databases (academic records), identity verification system, student information system
* **Technical components used**:

  * **Pilot option**: Pilot2 (Hybrid Trust: Classical PKI + Decentralised PKI)
  * **Wallet(s)**: EUDI Wallet (EUDIW by IZERTIS)
  * **Issuer platform**: uSelf Issuer Agent (ATOS)
  * **Verifier platform**: uSelf Verifier (ATOS)
  * **PID Retrieval Service**: Lithuanian national PID provider integration via ATOS
* **Governance configuration**:

  * **Trust model**: Hybrid (X.509 PKI + DIDs + EBSI Trust Registries)
  * **Issuer DID**:

    ```
    did:ebsi:zgJUpxRiLEhzA5iLKABoanw
    ```
  * **Verifier DID**:

    ```
    did:ebsi:zgJUpxRiLEhzA5iLKABoanw
    ```
  * **Issuer public key reference (PKI)**:

    ```
    Subject CN: lspvdu.vdu.lt
    Organization: Vytautas Magnus University
    Country: LT
    Algorithm: EC (Elliptic Curve)
    Key Size: 256 bits
    Security Level: Strong (256-bit EC equivalent to 3072-bit RSA)
    Certificate Chain: 3 certificate(s)
    ```
  * **Relying Party certificate**: Provided via DC4EU PKI infrastructure
  * **Registry references**: EBSI Trust Registry entries, Lithuanian Sectorial EAA Catalogue
* **Monitoring and feedback mechanisms**:
  Weekly monitoring reports with KPIs, structured feedback collection, managed by SPOC

---

## 3. Legal, Organisational and Operational Details

* **Regulatory context**:

  * GDPR compliance
  * eIDAS2 alignment and regulation
  * Lithuanian national higher education regulations
* **Risk management**:
  Risk of incorrect identity matching (medium likelihood/high impact) mitigated via identity verification protocols; risk of user confusion (medium likelihood/medium impact) mitigated via training and support
* **Credential lifecycle management**:

  * Revocation: Implemented via EBSI Trust Registry
  * Suspension: Implemented via institutional controls
* **Infrastructure readiness**:

  * Test environment operational with ATOS/IZERTIS integration
  * Production readiness: Achieved for diploma issuance workflows
* **Training and onboarding**:
  25 students and approximately 4 administrative staff trained
* **Issue escalation**:

  * SPOC contact: Tomas Krilavicius
  * Clearly defined response times and documented resolutions
* **Success indicators and KPIs**:

  * Successful diploma issuance completion rate
  * EAA verification success rate
  * User satisfaction measured via structured surveys

---

## 4. Trust Model Onboarding Evidences

* **Issuer DID and metadata**:

  ```
  did:ebsi:zgJUpxRiLEhzA5iLKABoanw
  ```
* **Verifier DID and metadata**:

  ```
  did:ebsi:zgJUpxRiLEhzA5iLKABoanw
  ```
* **Issuer public key reference (PKI)**:

  ```
  -----BEGIN CERTIFICATE-----
  [PKI Certificate for lspvdu.vdu.lt - 3 certificate chain]
  Subject: C=LT, O=Vytautas Magnus University, CN=lspvdu.vdu.lt
  Key Algorithm: EC (prime256v1)
  Signature Algorithm: ecdsa-with-SHA256
  -----END CERTIFICATE-----
  ```
* **Relying Party certificate**:
  Provided via DC4EU consolidated PKI infrastructure
* **Registry references**:
  EBSI Trust Registry entries (registered), Lithuanian Sectorial EAA Catalogue
* **PID credentials used**:
  Lithuanian national eIDAS 2.0 compliant PID credentials
* **Proof of wallet compatibility tests**:
  Integration testing completed with EUDIW by IZERTIS

---

## 5. Implementation and Testing Progress

* **Scenario status**: Completed
* **Number of users onboarded**:
  25 students successfully onboarded for diploma issuance simulation
* **Credentials issued**:
  PID (Person Identification Data), Diploma credentials
* **Credentials verified**:
  PID verification completed during PID retrieval user journey, Diploma credentials successfully verified
* **Successes**:
  Successful PKI certificate deployment, ATOS/IZERTIS integration completed, EBSI DID registration completed (did:ebsi:zgJUpxRiLEhzA5iLKABoanw), PID retrieval user journey executed successfully, diploma issuance process successfully simulated and completed, verification workflows demonstrated
* **Issues encountered**:
  Minor initial setup considerations for Lithuanian regulatory context, successfully resolved
* **Deviation from plan**:
  No significant deviations, implementation proceeded as planned with successful completion of diploma issuance focus

---

## 6. Testing Results and Observations

* **What worked as expected**:
  * PKI certificate infrastructure deployment successful
  * ATOS issuer platform integration completed
  * IZERTIS wallet integration functional
  * PID retrieval user journey executed successfully
  * Diploma issuance process completed successfully
  * Diploma verification workflows functional
  * Student onboarding process efficient
  * W3C Verifiable Credentials implementation successful
  * Lithuanian regulatory compliance achieved
* **What did not work and why**:
  * Minor performance considerations for very large credential volumes
  * Some initial user training requirements for digital diploma concepts
* **Feedback from users**:
  Positive response to digital diploma issuance process, students appreciated the innovation in academic credential management and potential for academic mobility
* **Impact on user experience and feasibility**:
  Demonstrates successful feasibility of hybrid trust model approach specifically for diploma issuance in Lithuanian higher education context. Strong potential for enhancing academic mobility and credential recognition.

---

## 7. Evidence Archive and References

* **Screenshots or logs**:
  Available in DC4EU workspace: Lithuania-VMU folder
* **Credential samples**:
  Diploma credential samples (redacted) available for review
* **Links to shared environment/demo**:
  https://lspvdu.vdu.lt (DNS endpoint operational)
* **Documents or repositories**:
  VMU scenario characterisation documents, technical integration specifications
* **KPI data submission details**:
  Weekly reports to WP5 using DC4EU structured templates

---

## 8. Next Steps and Recommendations

* **Pending actions**:
  * Performance optimisation for larger-scale deployment
  * Documentation of lessons learned for other Lithuanian institutions
  * Cross-border verification testing expansion
  * Preparation for full university deployment
* **Recommendations for future pilots or replication**:
  * Focus on diploma-specific workflows can provide clear value demonstration
  * Early engagement with national regulatory frameworks
  * Standardise diploma credential schemas across European institutions
  * Implement comprehensive user training programmes for digital diploma concepts

---

## 9. Summary of End-User Feedback

* General impressions:
  Very positive reception of digital diploma concept, appreciation for innovation in academic credential management
* Ease of use of wallets and services:
  High usability reported, successful completion of diploma-focused user journeys
* Challenges encountered:
  Initial conceptual learning for digital diploma management, successfully addressed through training
* Suggestions for improvement:
  Request for enhanced diploma presentation features, interest in additional credential types
* Willingness to use again:
  Very high willingness expressed, strong interest in expanding to other academic credentials

---

## 10. Summary of Piloting Agent Insights

* Feedback on support received:
  Excellent support from ATOS and IZERTIS technical teams, effective coordination for diploma-focused implementation
* Main barriers during implementation:
  Lithuanian regulatory context considerations, minor technical optimisation requirements
* Lessons learned:
  Value of focused diploma issuance approach, importance of regulatory alignment, effectiveness of ATOS/IZERTIS integration
* Observed impact and value:
  Demonstrates significant potential for transforming Lithuanian higher education diploma management, strong foundation for Baltic academic mobility initiatives
* Recommendations for scaling:
  * Expand diploma-focused approach to other Lithuanian higher education institutions
  * Standardise diploma credential formats across Baltic region
  * Develop comprehensive training materials for institutional adoption
  * Create clear integration pathways for Lithuanian academic institutions