# DC4EU Deployment and Testing Scenarios Results Library (DTSRL) – Scenario: Universidad Politécnica de Madrid (UPM)

## 1. Scenario Identification

* **Piloting agent name**: Universidad Politécnica de Madrid (UPM)
* **Scenario title**: Technical Education Digital Credentials with Hybrid Trust Framework (ATOS/IZERTIS Dockerised Solution)
* **Date of submission**: 11 July 2025
* **Point of contact (SPOC)**: Fernando Pescador

---

## 2. Scenario Characterisation

* **User journeys implemented**:
  PID retrieval (completed), EducationalID issuance (completed), Educational achievement issuance (completed), Generic EAA verification (completed)
* **Target groups and end-user roles**:
  Technical students, engineering graduates, polytechnic staff, research personnel, academic administrators
* **Electronic Attestations of Attributes (EAAs) involved**:
  PID (Person Identification Data), EducationalID, Educational Achievement (Technical degrees, Engineering qualifications, Research certifications, Professional competencies)
* **Institutional systems/databases connected**:
  UPM academic management system, polytechnic student records, research database, technical programme information systems
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
    did:ebsi:zn4TkeWRBMovc6PPMFBuKD1
    ```
  * **Verifier DID**:

    ```
    did:ebsi:zn4TkeWRBMovc6PPMFBuKD1
    ```
  * **Issuer public key reference (PKI)**:

    ```
    Subject CN: lspupm.dc4eu.upm.es
    Organization: Universidad Politécnica de Madrid
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
  * Technical education regulatory requirements
* **Risk management**:
  Identity correlation failures mitigated via UPM authentication protocols; EBSI downtime risk managed through backup verification systems; research data protection protocols established
* **Credential lifecycle management**:

  * Revocation: Implemented via EBSI Trust Registry and SGAD
  * Suspension: Implemented for academic and research status changes
* **Infrastructure readiness**:

  * Production-ready ATOS/IZERTIS Dockerised environment integrated with UPM technical infrastructure
* **Training and onboarding**:
  Technical faculty and research staff trained on digital credential management, EUDI Wallet operations, and research credential protocols
* **Issue escalation**:

  * SPOC contact: Fernando Pescador
  * Technical escalation through ATOS/IZERTIS support and UPM IT services
* **Success indicators and KPIs**:

  * Number of technical credentials issued and verified
  * Research credential cross-border recognition success rate
  * User adoption across technical and research communities

---

## 4. Trust Model Onboarding Evidences

* **Issuer DID and metadata**:

  ```
  did:ebsi:zn4TkeWRBMovc6PPMFBuKD1
  ```
* **Verifier DID and metadata**:

  ```
  did:ebsi:zn4TkeWRBMovc6PPMFBuKD1
  ```
* **Issuer public key reference (PKI)**:

  ```
  Subject: CN=lspupm.dc4eu.upm.es, O=Universidad Politécnica de Madrid, C=ES
  Algorithm: EC (prime256v1)
  Key Size: 256 bits
  Signature Algorithm: ecdsa-with-SHA256
  ```
* **Relying Party certificate**:
  Provided via DC4EU PKI infrastructure
* **Registry references**:
  EBSI Trust Registry entries, Spanish Sectorial EAA Catalogue, SGAD governance framework, Technical education registries
* **PID credentials used**:
  Spanish national PID provider credentials with EUDI Wallet integration for technical education context
* **Proof of wallet compatibility tests**:
  Comprehensive testing completed with EUDI Wallet for technical and research credential types

---

## 5. Implementation and Testing Progress

* **Scenario status**: Completed
* **Number of users onboarded**:
  45 technical students, 12 research staff, 6 academic administrators
* **Credentials issued**:
  63 PID credentials, 63 EducationalID credentials, 42 Educational Achievement credentials
* **Credentials verified**:
  All issued credentials successfully verified through cross-border scenarios, including research collaborations
* **Successes**:
  Successful integration with UPM technical systems, EBSI DID registration completed, comprehensive technical credential workflows, research credential management
* **Issues encountered**:
  Complex integration requirements with existing UPM research systems, resolved through custom API development
* **Deviation from plan**:
  Extended scope to include research credentials beyond initial technical education focus

---

## 6. Testing Results and Observations

* **What worked as expected**:
  ATOS/IZERTIS Dockerised solution performance, EUDI Wallet integration, cross-border credential verification, technical credential accuracy
* **What did not work and why**:
  Initial challenges with research database integration due to legacy system compatibility, resolved through API middleware
* **Feedback from users**:
  Exceptional feedback on research credential portability, positive response to technical qualification verification efficiency
* **Impact on user experience and feasibility**:
  Significant improvement in international research collaboration credential recognition, enhanced trust for technical qualifications

---

## 7. Evidence Archive and References

* **Screenshots or logs**:
  Comprehensive credential issuance and verification logs for technical and research credentials
* **Credential samples**:
  Redacted samples of technical PID, EducationalID, and Educational Achievement credentials, research qualification samples
* **Links to shared environment/demo**:
  https://lspupm.dc4eu.upm.es
* **Documents or repositories**:
  Technical and research-specific documentation, integration guides for polytechnic systems
* **KPI data submission details**:
  Weekly reporting through DC4EU structured templates with technical education and research metrics

---

## 8. Next Steps and Recommendations

* **Pending actions**:
  Expansion to additional technical disciplines, enhanced research credential integration, international collaboration framework development
* **Recommendations for future pilots or replication**:
  Focus on technical education specifics, enhanced research collaboration features, comprehensive faculty and research staff engagement

---

## 9. Summary of End-User Feedback

* **General impressions**:
  Outstanding reception among technical and research communities, high appreciation for credential precision and international recognition
* **Ease of use of wallets and services**:
  EUDI Wallet highly praised for technical accuracy and reliability in research contexts
* **Challenges encountered**:
  Initial complexity in research credential setup, resolved through specialized training sessions
* **Suggestions for improvement**:
  Integration with international research platforms, additional technical certification types, enhanced research collaboration features
* **Willingness to use again**:
  Very high willingness to continue, strong recommendation to technical and research professional networks

---

## 10. Summary of Piloting Agent Insights

* **Feedback on support received**:
  Excellent technical support from ATOS/IZERTIS team, responsive to technical education and research requirements
* **Main barriers during implementation**:
  Spanish regulatory compliance for research credentials, integration complexity with UPM legacy technical systems
* **Lessons learned**:
  Importance of technical education customization, value of research community engagement, need for comprehensive API integration
* **Observed impact and value**:
  Enhanced international recognition for technical credentials, improved research collaboration efficiency, strengthened trust in polytechnic qualifications
* **Recommendations for scaling**:
  Technical education-focused deployment procedures, enhanced research integration tools, comprehensive training for technical and research staff