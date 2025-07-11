# DC4EU Deployment and Testing Scenarios Results Library (DTSRL) – Scenario: Universidad Española a Distancia (UNED)

## 1. Scenario Identification

* **Piloting agent name**: Universidad Española a Distancia (UNED)
* **Scenario title**: Distance Learning Digital Credentials with Hybrid Trust Framework (ATOS/IZERTIS Dockerised Solution)
* **Date of submission**: 11 July 2025
* **Point of contact (SPOC)**: José Emilio Permuy

---

## 2. Scenario Characterisation

* **User journeys implemented**:
  PID retrieval (completed), EducationalID issuance (completed), Educational achievement issuance (completed), Generic EAA verification (completed)
* **Target groups and end-user roles**:
  Distance learning students, online graduates, remote academic staff, digital education administrators, international students
* **Electronic Attestations of Attributes (EAAs) involved**:
  PID (Person Identification Data), EducationalID, Educational Achievement (Distance learning degrees, Online qualifications, Continuing education certificates, Professional development credentials)
* **Institutional systems/databases connected**:
  UNED student management system, distance learning platform, online assessment database, international student records system
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
    did:ebsi:zrztS5QwWJu1MCgJaAJLj7y
    ```
  * **Verifier DID**:

    ```
    did:ebsi:zrztS5QwWJu1MCgJaAJLj7y
    ```
  * **Issuer public key reference (PKI)**:

    ```
    Subject CN: lspuned.govpart.de
    Organization: Universidad Española a Distancia
    Country: ES
    Algorithm: EC (Elliptic Curve)
    Key Size: 256 bits
    Security Level: Strong (256-bit EC equivalent to 3072-bit RSA)
    Certificate Chain: 3 certificate(s)
    Key Algorithm: EC (prime256v1)
    Signature Algorithm: ecdsa-with-SHA256
    ```
  * **Relying Party certificate**: Provided via DC4EU PKI infrastructure
  * **Registry references**: EBSI Trust Registry entries, Spanish Sectorial EAA Catalogue, SGAD governance framework, Distance learning registries
* **Monitoring and feedback mechanisms**:
  Online feedback surveys, weekly monitoring reports with KPIs, managed by SPOC

---

## 3. Legal, Organisational and Operational Details

* **Regulatory context**:

  * GDPR compliance
  * eIDAS2 alignment
  * Spanish national regulations
  * SGAD governance framework
  * Distance learning regulatory requirements
* **Risk management**:
  Identity verification challenges in remote learning mitigated via enhanced authentication protocols; EBSI downtime risk managed through redundant systems; online credential security protocols established
* **Credential lifecycle management**:

  * Revocation: Implemented via EBSI Trust Registry and SGAD
  * Suspension: Implemented for academic status and programme changes
* **Infrastructure readiness**:

  * Production-ready ATOS/IZERTIS Dockerised environment optimized for distance learning infrastructure
* **Training and onboarding**:
  Distance learning faculty and support staff trained on digital credential management, EUDI Wallet operations for remote education
* **Issue escalation**:

  * SPOC contact: José Emilio Permuy
  * Technical escalation through ATOS/IZERTIS support and UNED IT services
* **Success indicators and KPIs**:

  * Number of distance learning credentials issued and verified
  * International recognition success rate for online qualifications
  * User adoption across geographically distributed student base

---

## 4. Trust Model Onboarding Evidences

* **Issuer DID and metadata**:

  ```
  did:ebsi:zrztS5QwWJu1MCgJaAJLj7y
  ```
* **Verifier DID and metadata**:

  ```
  did:ebsi:zrztS5QwWJu1MCgJaAJLj7y
  ```
* **Issuer public key reference (PKI)**:

  ```
  Subject: CN=lspuned.govpart.de, O=Universidad Española a Distancia, C=ES
  Algorithm: EC (prime256v1)
  Key Size: 256 bits
  Signature Algorithm: ecdsa-with-SHA256
  ```
* **Relying Party certificate**:
  Provided via DC4EU PKI infrastructure
* **Registry references**:
  EBSI Trust Registry entries, Spanish Sectorial EAA Catalogue, SGAD governance framework, Distance learning quality assurance registries
* **PID credentials used**:
  Spanish national PID provider credentials with EUDI Wallet integration for distance learning contexts
* **Proof of wallet compatibility tests**:
  Comprehensive testing completed with EUDI Wallet for distance learning and online qualification credential types

---

## 5. Implementation and Testing Progress

* **Scenario status**: Completed
* **Number of users onboarded**:
  60 distance learning students, 10 remote faculty members, 4 academic administrators
* **Credentials issued**:
  74 PID credentials, 74 EducationalID credentials, 55 Educational Achievement credentials
* **Credentials verified**:
  All issued credentials successfully verified through cross-border scenarios, including international distance learning partnerships
* **Successes**:
  Successful integration with UNED distance learning systems, EBSI DID registration completed, comprehensive online credential workflows
* **Issues encountered**:
  Initial challenges with international student identity verification, resolved through enhanced authentication procedures
* **Deviation from plan**:
  Expanded scope to include international distance learning partnerships beyond original domestic focus

---

## 6. Testing Results and Observations

* **What worked as expected**:
  ATOS/IZERTIS Dockerised solution performance for distance learning, EUDI Wallet integration, cross-border credential verification for online qualifications
* **What did not work and why**:
  Initial complications with international student PID integration due to varying national systems, resolved through flexible authentication approaches
* **Feedback from users**:
  Highly positive feedback on credential portability for international distance learning, efficient verification for online qualifications
* **Impact on user experience and feasibility**:
  Substantial improvement in international recognition for distance learning credentials, enhanced trust in online education qualifications

---

## 7. Evidence Archive and References

* **Screenshots or logs**:
  Comprehensive credential issuance and verification logs for distance learning credentials
* **Credential samples**:
  Redacted samples of distance learning PID, EducationalID, and Educational Achievement credentials
* **Links to shared environment/demo**:
  https://lspuned.govpart.de
* **Documents or repositories**:
  Distance learning-specific documentation, integration guides for remote education systems
* **KPI data submission details**:
  Weekly reporting through DC4EU structured templates with distance learning metrics

---

## 8. Next Steps and Recommendations

* **Pending actions**:
  Expansion to additional distance learning programmes, enhanced international partnership integration, mobile-optimized credential access
* **Recommendations for future pilots or replication**:
  Focus on remote education specifics, enhanced international student support, comprehensive online faculty training

---

## 9. Summary of End-User Feedback

* **General impressions**:
  Excellent reception among distance learning community, high appreciation for international credential recognition
* **Ease of use of wallets and services**:
  EUDI Wallet praised for accessibility and reliability in remote learning contexts
* **Challenges encountered**:
  Initial setup complexity for international students, resolved through multilingual support and guidance
* **Suggestions for improvement**:
  Enhanced mobile accessibility, integration with international education platforms, additional continuing education credential types
* **Willingness to use again**:
  Very high willingness to continue, strong recommendation within distance learning professional networks

---

## 10. Summary of Piloting Agent Insights

* **Feedback on support received**:
  Outstanding technical support from ATOS/IZERTIS team, responsive to distance learning requirements
* **Main barriers during implementation**:
  Spanish regulatory compliance for international students, integration complexity with diverse international systems
* **Lessons learned**:
  Importance of distance learning customization, value of international student community engagement, need for flexible authentication approaches
* **Observed impact and value**:
  Enhanced international recognition for distance learning credentials, improved verification efficiency for online qualifications, strengthened trust in remote education
* **Recommendations for scaling**:
  Distance learning-focused deployment procedures, enhanced international integration tools, comprehensive training for remote education staff