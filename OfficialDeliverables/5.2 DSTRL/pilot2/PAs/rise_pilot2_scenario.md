# DC4EU Deployment and Testing Scenarios Results Library (DTSRL) – Scenario: Research Institutes of Sweden (RISE)

## 1. Scenario Identification

* **Piloting agent name**: Research Institutes of Sweden (RISE)
* **Scenario title**: Research Professional Qualification Digital Credentials with Hybrid Trust Framework (Research-Focused Implementation)
* **Date of submission**: 11 July 2025
* **Point of contact (SPOC)**: Fredrik Nilbrink

---

## 2. Scenario Characterisation

* **User journeys implemented**:
  PID retrieval (completed), Research credential issuance, Professional qualification certification, Academic research certificate issuance, Generic EAA verification (completed)
* **Target groups and end-user roles**:
  Research professionals, academic researchers, institute research staff, research project managers, international research collaborators
* **Electronic Attestations of Attributes (EAAs) involved**:
  PID (Person Identification Data), Research Professional ID, Academic Research Certificates, Professional Research Qualifications, Research Project Certifications
* **Institutional systems/databases connected**:
  RISE research database, Swedish research qualification system, research project management system, international collaboration database
* **Technical components used**:

  * **Pilot option**: Pilot2 (Hybrid Trust: Classical PKI + Decentralised PKI)
  * **Wallet(s)**: EUDI Wallet (EUDIW by IZERTIS)
  * **Issuer platform**: uSelf Issuer Agent (ATOS) - Research-focused implementation
  * **Verifier platform**: uSelf Verifier (ATOS) - Research-focused implementation
  * **PID Retrieval Service**: Swedish national PID provider integration
* **Governance configuration**:

  * **Trust model**: Hybrid (X.509 PKI + DIDs + EBSI Trust Registries)
  * **Issuer DID**:

    ```
    did:ebsi:zZo5kFbZASswkZMypc1V3XQ
    ```
  * **Verifier DID**:

    ```
    did:ebsi:zZo5kFbZASswkZMypc1V3XQ
    ```
  * **Issuer public key reference (PKI)**:

    ```
    Subject CN: lsprise.ri.se
    Organization: Research Institutes of Sweden
    Country: SE
    Algorithm: EC (Elliptic Curve)
    Key Size: 256 bits
    Security Level: Strong (256-bit EC equivalent to 3072-bit RSA)
    Certificate Chain: 3 certificate(s)
    Key Algorithm: EC (prime256v1)
    Signature Algorithm: ecdsa-with-SHA256
    ```
  * **Relying Party certificate**: Provided via DC4EU PKI infrastructure for research qualification verification
  * **Registry references**: EBSI Trust Registry entries, Swedish Research Qualification Registry, European Research Area credentials
* **Monitoring and feedback mechanisms**:
  Online feedback surveys, weekly monitoring reports with research-specific KPIs, managed by SPOC

---

## 3. Legal, Organisational and Operational Details

* **Regulatory context**:

  * GDPR compliance with research data protection
  * eIDAS2 alignment
  * Swedish national regulations
  * European Research Area framework compliance
  * Research ethics and data protection requirements
* **Risk management**:
  Research data integrity protocols; EBSI downtime risk managed through critical research verification backup systems; intellectual property protection protocols established
* **Credential lifecycle management**:

  * Revocation: Implemented via EBSI Trust Registry for research qualification changes
  * Suspension: Implemented for research project status changes and ethical compliance issues
* **Infrastructure readiness**:

  * Production-ready research-focused implementation integrated with RISE research systems
* **Training and onboarding**:
  Research professionals and RISE administrative staff trained on digital research credential management and EUDI Wallet operations for research contexts
* **Issue escalation**:

  * SPOC contact: Fredrik Nilbrink
  * Technical escalation through research-focused support channels
* **Success indicators and KPIs**:

  * Number of research professional credentials issued and verified
  * International research collaboration credential recognition success rate
  * User adoption across Swedish research community

---

## 4. Trust Model Onboarding Evidences

* **Issuer DID and metadata**:

  ```
  did:ebsi:zZo5kFbZASswkZMypc1V3XQ
  ```
* **Verifier DID and metadata**:

  ```
  did:ebsi:zZo5kFbZASswkZMypc1V3XQ
  ```
* **Issuer public key reference (PKI)**:

  ```
  Subject: CN=lsprise.ri.se, O=Research Institutes of Sweden, C=SE
  Algorithm: EC (prime256v1)
  Key Size: 256 bits
  Signature Algorithm: ecdsa-with-SHA256
  ```
* **Relying Party certificate**:
  Provided via DC4EU PKI infrastructure for research qualification verification
* **Registry references**:
  EBSI Trust Registry entries, Swedish Research Qualification Registry, European Research Area credentials
* **PID credentials used**:
  Swedish national PID provider credentials with EUDI Wallet integration for research professional contexts
* **Proof of wallet compatibility tests**:
  Comprehensive testing completed with EUDI Wallet for research professional credential types

---

## 5. Implementation and Testing Progress

* **Scenario status**: Completed
* **Number of users onboarded**:
  30 research professionals, 8 research project managers, 4 administrative staff
* **Credentials issued**:
  42 PID credentials, 38 Research Professional ID credentials, 30 Research Certificates, 25 Professional Research Qualifications
* **Credentials verified**:
  All issued credentials successfully verified through cross-border scenarios, including international research collaboration partnerships
* **Successes**:
  Successful integration with RISE research systems, EBSI DID registration completed, comprehensive research credential workflows
* **Issues encountered**:
  Complex integration requirements with Swedish research qualification systems, resolved through specialized API development for research data
* **Deviation from plan**:
  Enhanced scope to include international research collaboration credentials beyond original domestic research focus

---

## 6. Testing Results and Observations

* **What worked as expected**:
  Research-focused implementation performance, EUDI Wallet integration for research contexts, cross-border research qualification verification
* **What did not work and why**:
  Initial challenges with research data privacy compliance integration, resolved through enhanced encryption and access control protocols
* **Feedback from users**:
  Highly positive feedback on research credential portability for international collaborations, efficient verification for research qualifications
* **Impact on user experience and feasibility**:
  Substantial improvement in international research collaboration credential recognition, enhanced trust in research professional qualifications

---

## 7. Evidence Archive and References

* **Screenshots or logs**:
  Comprehensive credential issuance and verification logs for research professional credentials
* **Credential samples**:
  Redacted samples of research PID, Research Professional ID, and Research Certificates
* **Links to shared environment/demo**:
  https://lsprise.ri.se
* **Documents or repositories**:
  Research professional-specific documentation, integration guides for research systems
* **KPI data submission details**:
  Weekly reporting through DC4EU structured templates with research-specific metrics

---

## 8. Next Steps and Recommendations

* **Pending actions**:
  Expansion to additional research disciplines, enhanced international research collaboration integration, development of research project certification pathways
* **Recommendations for future pilots or replication**:
  Focus on research-specific requirements, enhanced international collaboration protocols, comprehensive research professional training

---

## 9. Summary of End-User Feedback

* **General impressions**:
  Outstanding reception among research professional community, high appreciation for international research collaboration credential portability
* **Ease of use of wallets and services**:
  EUDI Wallet highly praised for reliability and precision required in research contexts
* **Challenges encountered**:
  Initial complexity in research credential understanding, resolved through specialized research professional training sessions
* **Suggestions for improvement**:
  Integration with international research platforms, additional research specialization credential types, enhanced research collaboration features
* **Willingness to use again**:
  Very high willingness to continue, strong recommendation within research professional networks and international research organizations

---

## 10. Summary of Piloting Agent Insights

* **Feedback on support received**:
  Excellent technical support, highly responsive to research professional requirements and compliance needs
* **Main barriers during implementation**:
  Swedish regulatory compliance requirements, integration complexity with research qualification systems
* **Lessons learned**:
  Critical importance of research professional customization, value of research community engagement, need for specialized research data protection protocols
* **Observed impact and value**:
  Enhanced international recognition for research professional credentials, improved research collaboration efficiency, strengthened trust in Swedish research professionals internationally
* **Recommendations for scaling**:
  Research professional-focused deployment procedures, enhanced research integration tools, comprehensive training for research professionals and compliance staff