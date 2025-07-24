# DC4EU Deployment and Testing Scenarios Results Library (DTSRL) – Scenario: University of Maia (UMAIA)

## 1. Scenario Identification

* **Piloting agent name**: University of Maia (UMAIA)
* **Scenario title**: Educational Credential Issuance and Verification with Hybrid Trust Framework
* **Date of submission**: 11 July 2025
* **Point of contact (SPOC)**: UMAIA Representative

---

## 2. Scenario Characterisation

* **User journeys implemented**:
  PID retrieval (completed), Onboarding in education, EducationalID issuance (completed), Educational achievement issuance (completed), Generic EAA verification (completed)
* **Target groups and end-user roles**:
  University students, academic administrative staff, registry office personnel
* **Electronic Attestations of Attributes (EAAs) involved**:
  PID (Person Identification Data), EducationalID, Educational Achievement (EAAs: University degrees, Academic certificates)
* **Institutional systems/databases connected**:
  UMAIA authentic source databases (academic records), identity verification system, student information system
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
    did:ebsi:z23iKdgVPusLvDSMna87dgM8
    ```
  * **Verifier DID**:

    ```
    did:ebsi:z23iKdgVPusLvDSMna87dgM8
    ```
  * **Issuer public key reference (PKI)**:

    ```
    Subject CN: [UMAIA certificate details]
    Organization: University of Maia
    Country: PT
    Algorithm: EC (Elliptic Curve)
    Key Size: 256 bits
    Security Level: Strong (256-bit EC equivalent to 3072-bit RSA)
    Certificate Chain: 3 certificate(s)
    ```
  * **Relying Party certificate**: Provided via DC4EU PKI infrastructure
  * **Registry references**: EBSI Trust Registry entries, Portuguese Sectorial EAA Catalogue via SGAD
* **Monitoring and feedback mechanisms**:
  Online feedback surveys, weekly monitoring reports with KPIs, managed by SPOC

---

## 3. Legal, Organisational and Operational Details

* **Regulatory context**:
  * GDPR compliance
  * Portuguese national and higher education regulations
  * eIDAS2 framework alignment
* **Risk management**:
  Risk of incorrect identity matching (medium likelihood/high impact) mitigated via identity verification protocols; risk of user confusion (medium likelihood/medium impact) mitigated via training and support
* **Credential lifecycle management**:
  * Revocation: Implemented via EBSI Trust Registry
  * Suspension: Implemented via institutional controls
* **Infrastructure readiness**:
  * Test environment operational
  * Production readiness: Achieved
* **Training and onboarding**:
  University students and approximately 3 administrative staff trained
* **Issue escalation**:
  * SPOC contact: UMAIA Representative
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
  did:ebsi:z23iKdgVPusLvDSMna87dgM8
  ```
* **Verifier DID and metadata**:
  ```
  did:ebsi:z23iKdgVPusLvDSMna87dgM8
  ```
* **Issuer public key reference (PKI)**:
  ```
  -----BEGIN CERTIFICATE-----
  [PKI Certificate for UMAIA - 3 certificate chain]
  Subject: C=PT, O=University of Maia
  Key Algorithm: EC (prime256v1)
  Signature Algorithm: ecdsa-with-SHA256
  -----END CERTIFICATE-----
  ```
* **Relying Party certificate**: Provided via DC4EU consolidated PKI infrastructure
* **Registry references**: EBSI Trust Registry entries (registered), Portuguese Sectorial EAA Catalogue managed by SGAD
* **PID credentials used**: Portuguese national eIDAS 2.0 compliant PID credentials
* **Proof of wallet compatibility tests**: Integration testing completed with EUDIW

---

## 5. Implementation and Testing Progress

* **Scenario status**: Completed
* **Number of users onboarded**: University students successfully onboarded for credential testing
* **Credentials issued**: PID (Person Identification Data), EducationalID, Educational Achievement (University degrees)
* **Credentials verified**: PID verification completed during PID retrieval user journey, EducationalID verified, Educational Achievement verified
* **Successes**: Successful PKI certificate deployment, platform integration completed, EBSI DID registration completed, comprehensive educational credential workflows demonstrated
* **Issues encountered**: Minor initial configuration requirements for Portuguese regulatory context, successfully resolved
* **Deviation from plan**: No significant deviations, implementation proceeded as planned

---

## 6. Testing Results and Observations

* **What worked as expected**:
  * PKI certificate infrastructure deployment successful
  * Platform integration completed
  * EUDIW integration functional
  * All user journeys executed successfully
  * Portuguese regulatory compliance achieved
* **What did not work and why**:
  * Minor performance considerations for scaling
  * Initial user training requirements addressed through training
* **Feedback from users**: Positive response from university students, appreciation for digital credential innovation
* **Impact on user experience and feasibility**: Demonstrates successful feasibility of hybrid trust model for Portuguese university context

---

## 7. Evidence Archive and References

* **Screenshots or logs**: Available in DC4EU workspace: Portugal-UMAIA folder
* **Credential samples**: EducationalID and University degree samples (redacted) available for review
* **Links to shared environment/demo**: [UMAIA DNS endpoint]
* **Documents or repositories**: UMAIA scenario characterisation documents, technical integration specifications
* **KPI data submission details**: Weekly reports to WP5 using DC4EU structured templates

---

## 8. Next Steps and Recommendations

* **Pending actions**: Performance optimisation, documentation of lessons learned, cross-border verification testing
* **Recommendations for future pilots or replication**: Early integration with Portuguese governance frameworks, standardise Portuguese university credential formats

---

## 9. Summary of End-User Feedback

* General impressions: Positive reception from university students
* Ease of use of wallets and services: High usability reported
* Challenges encountered: Initial learning curve successfully addressed through training
* Suggestions for improvement: Request for additional credential types, enhanced Portuguese language support
* Willingness to use again: High willingness expressed

---

## 10. Summary of Piloting Agent Insights

* Feedback on support received: Excellent support from technical teams
* Main barriers during implementation: Portuguese regulatory context integration
* Lessons learned: Importance of Portuguese regulatory alignment
* Observed impact and value: Demonstrates significant potential for transforming Portuguese higher education
* Recommendations for scaling: Expand implementation to other Portuguese universities