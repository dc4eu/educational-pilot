# DC4EU Deployment and Testing Scenarios Results Library (DTSRL) – Scenario: University of Alcalá (UAH)

## 1. Scenario Identification

* **Piloting agent name**: University of Alcalá (UAH)
* **Scenario title**: Multidisciplinary Education Digital Credentials with Hybrid Trust Framework (ATOS/IZERTIS Dockerised Solution)
* **Date of submission**: 11 July 2025
* **Point of contact (SPOC)**: Sergio Caro

---

## 2. Scenario Characterisation

* **User journeys implemented**:
  PID retrieval (completed), EducationalID issuance (completed), Educational achievement issuance (completed), Generic EAA verification (completed)
* **Target groups and end-user roles**:
  Multidisciplinary students, science students, academic staff
* **Electronic Attestations of Attributes (EAAs) involved**:
  PID (Person Identification Data), EducationalID, Educational Achievement, Science qualifications
* **Institutional systems/databases connected**:
  UAH academic management system, student records database, science programme systems
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
    did:ebsi:zf3oZxMRc8gT4CoNzXzH1Kq
    ```
  * **Verifier DID**:

    ```
    did:ebsi:zf3oZxMRc8gT4CoNzXzH1Kq
    ```
  * **Issuer public key reference (PKI)**:

    ```
    Subject CN: lspuah.uah.es
    Organization: University of Alcalá
    Country: ES
    Algorithm: EC (Elliptic Curve)
    Key Size: 256 bits
    Security Level: Strong (256-bit EC equivalent to 3072-bit RSA)
    Certificate Chain: 3 certificate(s)
    Key Algorithm: EC (prime256v1)
    Signature Algorithm: ecdsa-with-SHA256
    ```
  * **Relying Party certificate**: Provided via DC4EU PKI infrastructure
  * **Registry references**: EBSI Trust Registry entries, Spanish Sectorial EAA Catalogue, SGAD governance framework
* **Monitoring and feedback mechanisms**:
  Online feedback surveys, weekly monitoring reports with KPIs, managed by SPOC

---

## 3. Legal, Organisational and Operational Details

* **Regulatory context**:

  * GDPR compliance
  * eIDAS2 alignment
  * Spanish national regulations
  * SGAD governance framework
  * International exchange programme requirements
* **Risk management**:
  Identity correlation failures mitigated via UAH authentication protocols; EBSI downtime risk managed through backup systems; international student data protection protocols established
* **Credential lifecycle management**:

  * Revocation: Implemented via EBSI Trust Registry and SGAD
  * Suspension: Implemented for academic status and exchange programme changes
* **Infrastructure readiness**:

  * Production-ready ATOS/IZERTIS Dockerised environment integrated with UAH multidisciplinary systems
* **Training and onboarding**:
  Multidisciplinary faculty and international office staff trained on digital credential management and EUDI Wallet operations
* **Issue escalation**:

  * SPOC contact: Sergio Caro
  * Technical escalation through ATOS/IZERTIS support and UAH IT services
* **Success indicators and KPIs**:

  * Number of multidisciplinary credentials issued and verified
  * International exchange credential recognition success rate
  * User adoption across diverse academic disciplines

---

## 4. Trust Model Onboarding Evidences

* **Issuer DID and metadata**:

  ```
  did:ebsi:zf3oZxMRc8gT4CoNzXzH1Kq
  ```
* **Verifier DID and metadata**:

  ```
  did:ebsi:zf3oZxMRc8gT4CoNzXzH1Kq
  ```
* **Issuer public key reference (PKI)**:

  ```
  Subject: CN=lspuah.uah.es, O=University of Alcalá, C=ES
  Algorithm: EC (prime256v1)
  Key Size: 256 bits
  Signature Algorithm: ecdsa-with-SHA256
  ```
* **Relying Party certificate**:
  Provided via DC4EU PKI infrastructure
* **Registry references**:
  EBSI Trust Registry entries, Spanish Sectorial EAA Catalogue, SGAD governance framework, International exchange registries
* **PID credentials used**:
  Spanish national PID provider credentials with EUDI Wallet integration for multidisciplinary education contexts
* **Proof of wallet compatibility tests**:
  Comprehensive testing completed with EUDI Wallet for humanities, science, and international exchange credential types

---

## 5. Implementation and Testing Progress

* **Scenario status**: Completed
* **Number of users onboarded**:
  30 multidisciplinary students, 5 faculty members
* **Credentials issued**:
  35 PID credentials, 35 EducationalID credentials, 56 Educational Achievement credentials
* **Credentials verified**:
  All issued credentials successfully verified through cross-border scenarios, including international exchange partnerships
* **Successes**:
  Successful integration with UAH multidisciplinary systems, EBSI DID registration completed, comprehensive international exchange credential workflows
* **Issues encountered**:
  Complexity in managing diverse academic discipline requirements, resolved through flexible credential templates
* **Deviation from plan**:
  Enhanced scope to include additional international partnerships beyond original European focus

---

## 6. Testing Results and Observations

* **What worked as expected**:
  ATOS/IZERTIS Dockerised solution adaptability to diverse disciplines, EUDI Wallet integration, cross-border credential verification for international exchanges
* **What did not work and why**:
  Initial challenges with humanities-specific credential formatting, resolved through customized templates
* **Feedback from users**:
  Positive feedback on credential flexibility for diverse academic backgrounds, efficient verification for international exchanges
* **Impact on user experience and feasibility**:
  Significant improvement in international exchange credential recognition, enhanced trust across diverse academic disciplines

---

## 7. Evidence Archive and References

* **Screenshots or logs**:
  Comprehensive credential issuance and verification logs for multidisciplinary credentials
* **Credential samples**:
  Redacted samples of multidisciplinary PID, EducationalID, and Educational Achievement credentials
* **Links to shared environment/demo**:
  https://uself-issuer-gui.lspuah.uah.es
* **Documents or repositories**:
  Multidisciplinary education documentation, integration guides for diverse academic systems
* **KPI data submission details**:
  Weekly reporting through DC4EU structured templates with multidisciplinary metrics

---

## 8. Next Steps and Recommendations

* **Pending actions**:
  Expansion to additional academic disciplines, enhanced international partnership integration, specialized humanities and science credential development
* **Recommendations for future pilots or replication**:
  Focus on multidisciplinary flexibility, enhanced international exchange support, comprehensive faculty training across diverse departments

---

## 9. Summary of End-User Feedback

* **General impressions**:
  Excellent reception across diverse academic communities, high appreciation for credential flexibility and international recognition
* **Ease of use of wallets and services**:
  EUDI Wallet praised for adaptability to diverse academic contexts and reliability
* **Challenges encountered**:
  Initial complexity in understanding discipline-specific requirements, resolved through comprehensive guidance
* **Suggestions for improvement**:
  Enhanced discipline-specific customization, integration with international academic platforms, additional language certification features
* **Willingness to use again**:
  Very high willingness to continue, strong recommendation across multidisciplinary academic networks

---

## 10. Summary of Piloting Agent Insights

* **Feedback on support received**:
  Excellent technical support from ATOS/IZERTIS team, responsive to multidisciplinary requirements
* **Main barriers during implementation**:
  Spanish regulatory compliance for international exchanges, integration complexity with diverse departmental systems
* **Lessons learned**:
  Importance of multidisciplinary flexibility, value of international office engagement, need for adaptable credential templates
* **Observed impact and value**:
  Enhanced international recognition for diverse academic credentials, improved verification efficiency for exchange programmes, strengthened trust across academic disciplines
* **Recommendations for scaling**:
  Multidisciplinary-focused deployment procedures, enhanced international integration tools, comprehensive training for diverse academic staff