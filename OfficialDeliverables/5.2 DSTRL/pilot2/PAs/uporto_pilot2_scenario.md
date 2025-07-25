# DC4EU Deployment and Testing Scenarios Results Library (DTSRL) – Scenario: Universidade do Porto (U.PORTO)

## 1. Scenario Identification

* **Piloting agent name**: Universidade do Porto (U.PORTO)
* **Scenario title**: Student Enrollment and Diploma Issuance with Hybrid Trust Framework
* **Date of submission**: 11 July 2025
* **Point of contact (SPOC)**: Bruno Pereira, José Filipe Alves, Jorge Cunha

---

## 2. Scenario Characterisation

* **User journeys implemented**:
  PID retrieval (completed), Student Enrollment, Issuance of Educational ID (used as Student Card), Issuance of Student Diplomas, Generic EAA verification (completed)
* **Target groups and end-user roles**:
  U.Porto students (New enrollees, Graduates requesting diplomas, Students requesting ID cards), administrative staff
* **Electronic Attestations of Attributes (EAAs) involved**:
  PID (Person Identification Data), EducationalID, Educational Achievement (EAA: Enrollment HE, Diplomas, Diploma Supplements)
* **Institutional systems/databases connected**:
  U.Porto's authentication system and student records database
* **Technical components used**:

  * **Pilot option**: Pilot2 (Hybrid Trust: Classical PKI + Decentralised PKI)
  * **Wallet(s)**: EUDI Wallet (EUDIW)
  * **Issuer platform**: uSelf Issuer Agent
  * **Verifier platform**: uSelf Verifier
  * **PID Retrieval Service**: Portuguese national PID provider integration
* **Governance configuration**:

  * **Trust model**: Hybrid (X.509 PKI + DIDs + EBSI Trust Registries)
  * **Issuer DID**:

    ```
    did:ebsi:ztpGq6DAAFpsoiejNfswaJe
    ```
  * **Verifier DID**:

    ```
    did:ebsi:ztpGq6DAAFpsoiejNfswaJe
    ```
  * **Issuer public key reference (PKI)**:

    ```
    Subject CN: [U.Porto certificate details]
    Organization: Universidade do Porto
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
  Risk of incorrect identity matching (low likelihood/high impact) mitigated via academic authentication protocols; Risk of user confusion (medium likelihood/medium impact) mitigated via user training and clear guidance; Risk of delayed issuance (medium likelihood/medium impact) mitigated via clear processing timelines
* **Credential lifecycle management**:

  * Revocation: Processes defined for issuance, updates, revocation, renewal, and suspension of credentials
  * Suspension: Implemented via institutional controls
* **Infrastructure readiness**:

  * U.Porto SSO; secure databases; integration endpoints for ID issuance and diploma requests using a VM with the dockers for VC issuance and verification, according to the user journey; landing pages for simulating credential lifecycle, connected to the wallet and the internal U.Porto platforms
* **Training and onboarding**:
  Initial training covering eIDAS2, PID, Educational Achievements, and the U.Porto authentication system; User guidance on requesting and using the student card; Practical training on using eIDAS for student enrollment and digital diploma issuance using the EUDIW; Graduate guidance on diploma request process and digital access
* **Issue escalation**:

  * SPOC contacts: Bruno Pereira (bdpereira@uporto.pt), José Filipe Alves (josealves@uporto.pt), Jorge Cunha (jcunha@uporto.pt)
  * Escalation via SPOC contact, clearly defined response times (SLA 48h), and documented resolutions. Later the escalation will be made via Helpdesk of U.Porto, upon full deployment and User Journeys in production
* **Success indicators and KPIs**:

  * Successful student enrollment rate
  * ID card issuance rate
  * Diploma issuance and retrieval success rate
  * User satisfaction measured via structured survey

---

## 4. Trust Model Onboarding Evidences

* **Issuer DID and metadata**:

  ```
  did:ebsi:ztpGq6DAAFpsoiejNfswaJe
  ```
* **Verifier DID and metadata**:

  ```
  did:ebsi:ztpGq6DAAFpsoiejNfswaJe
  ```
* **Issuer public key reference (PKI)**:

  ```
  -----BEGIN CERTIFICATE-----
  [PKI Certificate for U.Porto - 3 certificate chain]
  Subject: C=PT, O=Universidade do Porto
  Key Algorithm: EC (prime256v1)
  Signature Algorithm: ecdsa-with-SHA256
  -----END CERTIFICATE-----
  ```
* **Relying Party certificate**:
  Provided via DC4EU consolidated PKI infrastructure
* **Registry references**:
  EBSI Trust Registry entries (registered), Portuguese Sectorial EAA Catalogue managed by SGAD
* **PID credentials used**:
  Portuguese national eIDAS 2.0 compliant PID credentials
* **Proof of wallet compatibility tests**:
  Integration testing completed with EUDIW

---

## 5. Implementation and Testing Progress

* **Scenario status**: Completed
* **Number of users onboarded**:
  25 - New enrollees, graduates requesting diplomas, students requesting ID cards successfully onboarded
* **Credentials issued**:
  PID (Person Identification Data), EducationalID, Educational Achievement (Enrollment HE, Diplomas, Diploma Supplements)
* **Credentials verified**:
  PID verification completed during PID retrieval user journey, EducationalID verified, Educational Achievement verified
* **Successes**:
  Successful PKI certificate deployment, U.Porto system integration completed, EBSI DID registration completed (did:ebsi:ztpGq6DAAFpsoiejNfswaJe), PID retrieval user journey executed successfully, comprehensive student lifecycle credential workflows demonstrated, effective integration with Portuguese governance framework
* **Issues encountered**:
  Minor initial configuration requirements for Portuguese regulatory context, successfully resolved
* **Deviation from plan**:
  No significant deviations, implementation proceeded as planned with successful completion of all key student lifecycle objectives

---

## 6. Testing Results and Observations

* **What worked as expected**:
  * PKI certificate infrastructure deployment successful
  * Platform integration completed
  * EUDIW integration functional
  * All user journeys executed successfully
  * W3C Verifiable Credentials implementation successful
  * Portuguese regulatory compliance achieved
* **What did not work and why**:
  * Minor performance considerations for scaling beyond pilot scope
  * Some initial user training requirements for digital credential concepts
* **Feedback from users**:
  Positive response from students across all lifecycle stages, particular appreciation for digital diploma and student card integration, potential for international academic mobility
* **Impact on user experience and feasibility**:
  Demonstrates successful feasibility of hybrid trust model approach for comprehensive Portuguese university student lifecycle management. Strong potential demonstrated for enhancing student services and international mobility.

---

## 7. Evidence Archive and References

* **Screenshots or logs**:
  Available in DC4EU workspace: Portugal-UPORTO folder
* **Credential samples**:
  EducationalID(Student Card), and Diploma samples (redacted) available for review
* **Links to shared environment/demo**:
  [U.Porto DNS endpoint]
* **Documents or repositories**:
  U.Porto scenario characterisation documents, technical integration specifications
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
  * Standardise Portuguese university credential formats
  * Implement comprehensive training programmes for Portuguese university contexts

---

## 9. Summary of End-User Feedback

* General impressions:
  Excellent reception from students across all lifecycle stages, strong appreciation for comprehensive digital transformation of student services
* Ease of use of wallets and services:
  High usability reported, successful completion of all student lifecycle user journeys
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
  Value of complete student lifecycle approach for maximum institutional impact, importance of Portuguese regulatory alignment, effectiveness of SIGARRA integration
* Observed impact and value:
  Demonstrates significant potential for transforming Portuguese higher education student services and international mobility
* Recommendations for scaling:
  * Expand comprehensive student lifecycle approach to other Portuguese universities
  * Standardise Portuguese university credential formats across all student services
  * Develop comprehensive training materials for Portuguese university adoption
  * Create clear integration pathways for Portuguese higher education institutions
  * Focus on complete student lifecycle for maximum institutional transformation impact