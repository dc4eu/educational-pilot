# DC4EU Deployment and Testing Scenarios Results Library (DTSRL) – Scenario: Universidad Carlos III de Madrid (UC3M)

## 1. Scenario Identification

* **Piloting agent name**: Universidad Carlos III de Madrid (UC3M)
* **Scenario title**: Engineering Education Digital Credentials with Hybrid Trust Framework (ATOS/IZERTIS Dockerised Solution)
* **Date of submission**: 11 July 2025
* **Point of contact (SPOC)**: Carlos Delgado

---

## 2. Scenario Characterisation

* **User journeys implemented**:
  PID retrieval (completed), EducationalID issuance (completed), Educational achievement issuance (completed), Generic EAA verification (completed)
* **Target groups and end-user roles**:
  Engineering students, computer science graduates, technical staff, academic administrators
* **Electronic Attestations of Attributes (EAAs) involved**:
  PID (Person Identification Data), EducationalID, Educational Achievement (Engineering degrees, Computer Science qualifications, Technical certifications)
* **Institutional systems/databases connected**:
  UC3M academic information system, student records database, identity management platform, engineering programme databases
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
    did:ebsi:zfpHmR5ZAGTcRwpmwatsDWz
    ```
  * **Verifier DID**:

    ```
    did:ebsi:zfpHmR5ZAGTcRwpmwatsDWz
    ```
  * **Issuer public key reference (PKI)**:

    ```
    Subject CN: lspuc3m.uc3m.es
    Organization: Universidad Carlos III de Madrid
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
* **Risk management**:
  Identity correlation failures mitigated via UC3M authentication protocols; EBSI downtime risk managed through redundant systems; credential lifecycle management established
* **Credential lifecycle management**:

  * Revocation: Implemented via EBSI Trust Registry and SGAD
  * Suspension: Implemented for academic status changes
* **Infrastructure readiness**:

  * Production-ready ATOS/IZERTIS Dockerised environment
* **Training and onboarding**:
  Engineering faculty and IT staff trained on digital credential management and EUDI Wallet operations
* **Issue escalation**:

  * SPOC contact: Carlos Delgado
  * Technical escalation through ATOS/IZERTIS support channels
* **Success indicators and KPIs**:

  * Number of engineering credentials issued and verified
  * Cross-border recognition success rate
  * User adoption and satisfaction metrics

---

## 4. Trust Model Onboarding Evidences

* **Issuer DID and metadata**:

  ```
  did:ebsi:zfpHmR5ZAGTcRwpmwatsDWz
  ```
* **Verifier DID and metadata**:

  ```
  did:ebsi:zfpHmR5ZAGTcRwpmwatsDWz
  ```
* **Issuer public key reference (PKI)**:

  ```
  Subject: CN=lspuc3m.uc3m.es, O=Universidad Carlos III de Madrid, C=ES
  Algorithm: EC (prime256v1)
  Key Size: 256 bits
  Signature Algorithm: ecdsa-with-SHA256
  ```
* **Relying Party certificate**:
  Provided via DC4EU PKI infrastructure
* **Registry references**:
  EBSI Trust Registry entries, Spanish Sectorial EAA Catalogue, SGAD governance framework
* **PID credentials used**:
  Spanish national PID provider credentials with EUDI Wallet integration
* **Proof of wallet compatibility tests**:
  Comprehensive testing completed with EUDI Wallet for engineering credential types

---

## 5. Implementation and Testing Progress

* **Scenario status**: Completed
* **Number of users onboarded**:
  40 engineering students, 8 faculty members, 3 administrative staff
* **Credentials issued**:
  51 PID credentials, 51 EducationalID credentials, 35 Educational Achievement credentials
* **Credentials verified**:
  All issued credentials successfully verified through cross-border scenarios
* **Successes**:
  Successful integration with UC3M academic systems, EBSI DID registration completed, comprehensive engineering credential workflows
* **Issues encountered**:
  Initial coordination challenges with Spanish PID systems, resolved through SGAD framework
* **Deviation from plan**:
  Enhanced scope to include additional engineering specializations beyond original plan

---

## 6. Testing Results and Observations

* **What worked as expected**:
  ATOS/IZERTIS Dockerised solution performance, EUDI Wallet integration, cross-border credential verification, SGAD governance compliance
* **What did not work and why**:
  Minor delays in Spanish PID provider synchronization due to national system update cycles
* **Feedback from users**:
  Highly positive feedback on credential portability for international engineering projects, efficient verification processes
* **Impact on user experience and feasibility**:
  Substantial improvement in international credential recognition for engineering professionals, enhanced trust through hybrid approach

---

## 7. Evidence Archive and References

* **Screenshots or logs**:
  Comprehensive credential issuance and verification logs for engineering credentials
* **Credential samples**:
  Redacted samples of engineering PID, EducationalID, and Educational Achievement credentials
* **Links to shared environment/demo**:
  https://lspuc3m.uc3m.es
* **Documents or repositories**:
  Engineering-specific technical documentation and integration guides
* **KPI data submission details**:
  Weekly reporting through DC4EU structured templates with engineering metrics

---

## 8. Next Steps and Recommendations

* **Pending actions**:
  Expansion to additional engineering disciplines, integration with professional engineering bodies
* **Recommendations for future pilots or replication**:
  Focus on domain-specific requirements, enhanced collaboration with professional organizations, comprehensive testing protocols

---

## 9. Summary of End-User Feedback

* **General impressions**:
  Excellent reception among engineering students, appreciation for international credential portability
* **Ease of use of wallets and services**:
  EUDI Wallet praised for reliability and technical precision required in engineering contexts
* **Challenges encountered**:
  Initial setup complexity for technical users, resolved through detailed documentation
* **Suggestions for improvement**:
  Integration with professional engineering software platforms, additional technical certifications
* **Willingness to use again**:
  Very high willingness to continue, strong recommendation to engineering professional networks

---

## 10. Summary of Piloting Agent Insights

* **Feedback on support received**:
  Outstanding technical support from ATOS/IZERTIS team, responsive to engineering-specific requirements
* **Main barriers during implementation**:
  Spanish regulatory compliance coordination, integration with existing UC3M technical systems
* **Lessons learned**:
  Importance of domain-specific customization, value of comprehensive faculty engagement
* **Observed impact and value**:
  Enhanced international recognition for engineering credentials, improved verification efficiency for technical qualifications
* **Recommendations for scaling**:
  Engineering-focused deployment templates, enhanced integration with professional bodies, comprehensive technical training programmes