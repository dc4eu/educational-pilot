# DC4EU Deployment and Testing Scenarios Results Library (DTSRL) – Scenario: Consejo General de Colegios Oficiales de Médicos (CGCOM)

## 1. Scenario Identification

* **Piloting agent name**: Consejo General de Colegios Oficiales de Médicos (CGCOM)
* **Scenario title**: Professional Medical Qualification Digital Credentials with Hybrid Trust Framework (ATOS/IZERTIS Dockerised Solution)
* **Date of submission**: 11 July 2025
* **Point of contact (SPOC)**: José Antonio Aguado / Laia Bota Porta

---

## 2. Scenario Characterisation

* **User journeys implemented**:
  PID retrieval (completed), Doctor ID issuance, Professional suitability certification,Buen Quehacer Médico (BQM) Training certificate issuance, ECMEC credits accreditation, Generic EAA verification (completed)
* **Target groups and end-user roles**:
  Medical professionals, doctors, medical specialists, healthcare administrators, continuing medical education participants, test users (fake doctors)
* **Electronic Attestations of Attributes (EAAs) involved**:
  PID (Person Identification Data), DoctorID, Certificate of Professional Suitability, BQM Medical Training Certificate, Accreditation of medical training (ECMEC credits certification)
* **Institutional systems/databases connected**:
  CGCOM medical professional database, Spanish medical registry, continuing medical education system
* **Technical components used**:

  * **Pilot option**: Pilot2 (Hybrid Trust: Classical PKI + Decentralised PKI)
  * **Wallet(s)**: EUDI Wallet (EUDIW by IZERTIS)
  * **Issuer platform**: uSelf Issuer Agent (ATOS)
  * **Verifier platform**: uSelf Verifier (ATOS)
  * **PID Retrieval Service**: Spanish national PID provider integration with medical professional context
* **Governance configuration**:

  * **Trust model**: Hybrid (X.509 PKI + DIDs + EBSI Trust Registries)
  * **Issuer DID**:

    ```
    did:ebsi:medical-cgcom-professional-authority
    ```
  * **Verifier DID**:

    ```
    did:ebsi:medical-cgcom-professional-authority
    ```
  * **Issuer public key reference (PKI)**:

    ```
    Subject CN: lspcgcom.cgcom.es
    Organization: Consejo General de Colegios Oficiales de Médicos
    Country: ES
    Algorithm: EC (Elliptic Curve)
    Key Size: 256 bits
    Security Level: Strong (256-bit EC equivalent to 3072-bit RSA)
    Certificate Chain: 3 certificate(s)
    Key Algorithm: EC (prime256v1)
    Signature Algorithm: ecdsa-with-SHA256
    ```
  * **Relying Party certificate**: Provided via DC4EU PKI infrastructure for medical professional verification
  * **Registry references**: EBSI Trust Registry entries, Spanish Medical Professional Registry, SGAD governance framework, EU Medical Qualifications Registry
* **Monitoring and feedback mechanisms**:
  Online feedback surveys, weekly monitoring reports with medical professional KPIs, managed by SPOC

---

## 3. Legal, Organisational and Operational Details

* **Regulatory context**:

  * GDPR compliance with medical data protection
  * eIDAS2 alignment
  * Spanish national medical and professions regulations
  * SGAD governance framework
  * EU Medical Qualifications Directive compliance
  * Medical professional regulatory requirements
* **Risk management**:
  Medical professional identity verification protocols; EBSI downtime risk managed through critical medical verification backup systems; patient safety and medical qualification integrity protocols established
* **Credential lifecycle management**:

  * Revocation: Implemented via EBSI Trust Registry and medical professional authorities for license suspension/revocation
  * Suspension: Implemented for medical license status changes and continuing education lapses
* **Infrastructure readiness**:

  * Production-ready ATOS/IZERTIS Dockerised environment integrated with CGCOM medical professional systems
* **Training and onboarding**:
  Medical professionals and CGCOM administrative staff trained on digital medical credential management and EUDI Wallet operations for healthcare context
* **Issue escalation**:

  * SPOC contacts: José Antonio Aguado / Laia Bota Porta
  * Technical escalation through ATOS/IZERTIS support and CGCOM IT services
* **Success indicators and KPIs**:

  * Number of medical professional credentials issued and verified
  * Cross-border medical qualification recognition success rate
  * User adoption across Spanish medical professional community

---

## 4. Trust Model Onboarding Evidences

* **Issuer DID and metadata**:

  ```
  did:ebsi:medical-cgcom-professional-authority
  ```
* **Verifier DID and metadata**:

  ```
  did:ebsi:medical-cgcom-professional-authority
  ```
* **Issuer public key reference (PKI)**:

  ```
  Subject: CN=lspcgcom.cgcom.es, O=Consejo General de Colegios Oficiales de Médicos, C=ES
  Algorithm: EC (prime256v1)
  Key Size: 256 bits
  Signature Algorithm: ecdsa-with-SHA256
  ```
* **Relying Party certificate**:
  Provided via DC4EU PKI infrastructure for medical professional verification
* **Registry references**:
  EBSI Trust Registry entries, Spanish Medical Professional Registry, SGAD governance framework, EU Medical Qualifications Registry
* **PID credentials used**:
  Spanish national PID provider credentials with EUDI Wallet integration for medical professional contexts
* **Proof of wallet compatibility tests**:
  Comprehensive testing completed with EUDI Wallet for medical professional credential types, including test scenarios with fake doctor profiles

---

## 5. Implementation and Testing Progress

* **Scenario status**: Completed
* **Number of users onboarded**:
  25 medical professionals, 8 test users (fake doctors), 5 CGCOM administrative staff
* **Credentials issued**:
  38 PID credentials, 33 DoctorID credentials, 25 Professional Suitability certificates, 20 BQM Training certificates, 5 Accreditation of Medical training (ECMEC) credentials
* **Credentials verified**:
  All issued credentials successfully verified through cross-border scenarios, including international medical qualification recognition
* **Successes**:
  Successful integration with CGCOM medical professional systems, EBSI DID registration completed, comprehensive medical credential workflows, successful test scenarios
* **Issues encountered**:
  Complex integration requirements with Spanish medical registry systems, resolved through specialized API development for medical data
* **Deviation from plan**:
  Enhanced scope to include ECMEC credits and additional medical training certifications beyond original professional suitability focus

---

## 6. Testing Results and Observations

* **What worked as expected**:
  ATOS/IZERTIS Dockerised solution performance for medical credentials, EUDI Wallet integration for healthcare context, cross-border medical qualification verification
* **What did not work and why**:
  Initial challenges with medical data privacy compliance integration, resolved through enhanced encryption and access control protocols
* **Feedback from users**:
  Highly positive feedback on medical credential portability for international practice, efficient verification for medical qualifications across borders
* **Impact on user experience and feasibility**:
  Substantial improvement in international medical qualification recognition, enhanced trust in medical professional credentials, improved patient safety through verified qualifications

---

## 7. Evidence Archive and References

* **Screenshots or logs**:
  Comprehensive credential issuance and verification logs for medical professional credentials (anonymized for patient data protection)
* **Credential samples**:
  Redacted samples of medical PID, DoctorID, Professional Suitability certificates, and Training certificates
* **Links to shared environment/demo**:
  https://lspcgcom.cgcom.es
* **Documents or repositories**:
  Medical professional-specific documentation, integration guides for healthcare systems, privacy compliance documentation
* **KPI data submission details**:
  Weekly reporting through DC4EU structured templates with medical professional metrics

---

## 8. Next Steps and Recommendations

* **Pending actions**:
  Expansion to additional medical specializations, enhanced international medical qualification integration, development of continuing medical education credential pathways
* **Recommendations for future pilots or replication**:
  Focus on medical professional regulatory requirements, enhanced patient safety protocols, comprehensive medical professional training and support

---

## 9. Summary of End-User Feedback

* **General impressions**:
  Outstanding reception among medical professional community, high appreciation for international medical qualification portability and patient safety enhancement
* **Ease of use of wallets and services**:
  EUDI Wallet highly praised for reliability and security in medical professional contexts
* **Challenges encountered**:
  Initial complexity in medical data privacy understanding, resolved through specialized medical professional training sessions
* **Suggestions for improvement**:
  Integration with international medical platforms, additional medical specialization credential types, enhanced patient safety verification features
* **Willingness to use again**:
  Very high willingness to continue, strong recommendation within medical professional networks and international healthcare organizations

---

## 10. Summary of Piloting Agent Insights

* **Feedback on support received**:
  Excellent technical support from ATOS/IZERTIS team, highly responsive to medical professional requirements and regulatory compliance needs
* **Main barriers during implementation**:
  Spanish medical regulatory compliance requirements, integration complexity with medical professional registry systems, patient data protection protocols
* **Lessons learned**:
  Critical importance of medical professional regulatory customization, value of medical community engagement, need for specialized healthcare data protection protocols
* **Observed impact and value**:
  Enhanced international recognition for medical professional credentials, improved patient safety through verified medical qualifications, strengthened trust in Spanish medical professionals internationally
* **Recommendations for scaling**:
  Medical professional-focused deployment procedures, enhanced healthcare integration tools, comprehensive training for medical professionals and regulatory compliance staff
