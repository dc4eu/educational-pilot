# DC4EU Deployment and Testing Scenarios Results Library (DTSRL) – Scenario: Titu Maiorescu University (TMU)

## 1. Scenario Identification

* **Piloting agent name**: Titu Maiorescu University (TMU)
* **Scenario title**: Educational Credential Management with Hybrid Trust Framework (ATOS/IZERTIS Dockerised Solution)
* **Date of submission**: 11 July 2025
* **Point of contact (SPOC)**: Nicolae

---

## 2. Scenario Characterisation

* **User journeys implemented**:
  PID retrieval (completed), EducationalID issuance (completed), Educational achievement issuance (completed), Generic EAA verification (completed)
* **Target groups and end-user roles**:
  University students, graduates, academic administrative staff, registry office personnel
* **Electronic Attestations of Attributes (EAAs) involved**:
  PID (Person Identification Data), EducationalID, Educational Achievement (Bachelor's degrees, Master's degrees, Professional qualifications)
* **Institutional systems/databases connected**:
  TMU authentic source databases (academic records), student information system, identity verification system, academic programme databases
* **Technical components used**:

  * **Pilot option**: Pilot2 (Hybrid Trust: Classical PKI + Decentralised PKI)
  * **Wallet(s)**: EUDI Wallet (EUDIW by IZERTIS)
  * **Issuer platform**: uSelf Issuer Agent (ATOS)
  * **Verifier platform**: uSelf Verifier (ATOS)
  * **PID Retrieval Service**: Romanian national PID provider integration
* **Governance configuration**:

  * **Trust model**: Hybrid (X.509 PKI + DIDs + EBSI Trust Registries)
  * **Issuer DID**:

    ```
    did:ebsi:zyMAqBKZ3oD2gjrXd7ZKtB9
    ```
  * **Verifier DID**:

    ```
    did:ebsi:zyMAqBKZ3oD2gjrXd7ZKtB9
    ```
  * **Issuer public key reference (PKI)**:

    ```
    Subject CN: lsputm.utm.ro
    Organization: Titu Maiorescu University
    Country: RO
    Algorithm: EC (Elliptic Curve)
    Key Size: 256 bits
    Security Level: Strong (256-bit EC equivalent to 3072-bit RSA)
    Certificate Chain: 3 certificate(s)
    Key Algorithm: EC (prime256v1)
    Signature Algorithm: ecdsa-with-SHA256
    ```
  * **Relying Party certificate**: Provided via DC4EU PKI infrastructure
  * **Registry references**: EBSI Trust Registry entries, Romanian Sectorial EAA Catalogue
* **Monitoring and feedback mechanisms**:
  Online feedback surveys, weekly monitoring reports with KPIs, managed by SPOC

---

## 3. Legal, Organisational and Operational Details

* **Regulatory context**:

  * GDPR compliance
  * eIDAS2 alignment
  * Romanian national higher education regulations
* **Risk management**:
  Identity correlation failures mitigated via institutional authentication protocols; EBSI downtime risk managed through fallback procedures; credential revocation processes established
* **Credential lifecycle management**:

  * Revocation: Implemented via EBSI Trust Registry
  * Suspension: Implemented for academic standing changes
* **Infrastructure readiness**:

  * Production-ready ATOS/IZERTIS Dockerised environment
* **Training and onboarding**:
  Academic staff and IT personnel trained on EUDI Wallet operations and credential management
* **Issue escalation**:

  * SPOC contact: Nicolae
  * Technical support through ATOS/IZERTIS integration team
* **Success indicators and KPIs**:

  * Number of credentials issued: PID, EducationalID, Educational Achievement
  * Cross-border verification success rate
  * User satisfaction metrics from structured surveys

---

## 4. Trust Model Onboarding Evidences

* **Issuer DID and metadata**:

  ```
  did:ebsi:zyMAqBKZ3oD2gjrXd7ZKtB9
  ```
* **Verifier DID and metadata**:

  ```
  did:ebsi:zyMAqBKZ3oD2gjrXd7ZKtB9
  ```
* **Issuer public key reference (PKI)**:

  ```
  Subject: CN=lsputm.utm.ro, O=Titu Maiorescu University, C=RO
  Algorithm: EC (prime256v1)
  Key Size: 256 bits
  Signature Algorithm: ecdsa-with-SHA256
  ```
* **Relying Party certificate**:
  Provided via DC4EU PKI infrastructure
* **Registry references**:
  EBSI Trust Registry entries, Romanian Sectorial EAA Catalogue
* **PID credentials used**:
  Romanian national PID provider credentials with EUDI Wallet integration
* **Proof of wallet compatibility tests**:
  Comprehensive testing completed with EUDI Wallet for all credential types

---

## 5. Implementation and Testing Progress

* **Scenario status**: Completed
* **Number of users onboarded**:
  30 students, 5 academic staff members
* **Credentials issued**:
  35 PID credentials, 35 EducationalID credentials, 20 Educational Achievement credentials
* **Credentials verified**:
  All issued credentials successfully verified through cross-border scenarios
* **Successes**:
  Seamless integration with Romanian academic systems, successful EBSI DID registration, comprehensive user journey completion
* **Issues encountered**:
  Initial configuration challenges with Romanian PID integration, resolved through technical support
* **Deviation from plan**:
  No significant deviations; implementation proceeded according to planned timeline

---

## 6. Testing Results and Observations

* **What worked as expected**:
  ATOS/IZERTIS Dockerised solution deployment, EUDI Wallet integration, cross-border credential verification, EBSI Trust Registry operations
* **What did not work and why**:
  Minor delays in Romanian PID provider integration due to national system compatibility requirements
* **Feedback from users**:
  Positive response to digital credential convenience, intuitive EUDI Wallet interface, successful cross-border recognition
* **Impact on user experience and feasibility**:
  Significant improvement in credential portability and verification speed, enhanced trust through hybrid PKI approach

---

## 7. Evidence Archive and References

* **Screenshots or logs**:
  Comprehensive credential issuance and verification logs archived
* **Credential samples**:
  Redacted samples of PID, EducationalID, and Educational Achievement credentials
* **Links to shared environment/demo**:
  https://lsputm.utm.ro
* **Documents or repositories**:
  Technical documentation and integration guides maintained
* **KPI data submission details**:
  Weekly reporting through DC4EU structured templates

---

## 8. Next Steps and Recommendations

* **Pending actions**:
  Expansion to additional academic programmes, integration with more institutional systems
* **Recommendations for future pilots or replication**:
  Early engagement with national PID providers, comprehensive staff training programmes, phased deployment approach

---

## 9. Summary of End-User Feedback

* **General impressions**:
  Very positive reception of digital credential system, appreciation for enhanced security and portability
* **Ease of use of wallets and services**:
  EUDI Wallet praised for user-friendly interface and reliable performance
* **Challenges encountered**:
  Initial learning curve for wallet setup, resolved through guided training sessions
* **Suggestions for improvement**:
  Enhanced integration with existing university portal systems, additional credential types
* **Willingness to use again**:
  High willingness to continue using system, recommend to peers

---

## 10. Summary of Piloting Agent Insights

* **Feedback on support received**:
  Excellent technical support from ATOS/IZERTIS team, responsive issue resolution
* **Main barriers during implementation**:
  Romanian regulatory compliance requirements, coordination with national PID systems
* **Lessons learned**:
  Importance of early stakeholder engagement, value of comprehensive testing phases
* **Observed impact and value**:
  Enhanced credential security, improved verification efficiency, increased international recognition
* **Recommendations for scaling**:
  Standardised deployment procedures, enhanced integration tools, comprehensive training materials