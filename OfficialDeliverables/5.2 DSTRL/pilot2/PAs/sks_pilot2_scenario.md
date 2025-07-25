# DC4EU Deployment and Testing Scenarios Results Library (DTSRL) – Scenario: Skaitos kompiuterių servisas (SKS)

## 1. Scenario Identification

* **Piloting agent name**: Skaitos kompiuterių servisas (SKS)
* **Scenario title**: Professional Qualification Credential Issuance and Verification with Hybrid Trust Framework (ATOS/IZERTIS Solution)
* **Date of submission**: 11 July 2025
* **Point of contact (SPOC)**: Virginijus Jasaitis

---

## 2. Scenario Characterisation

* **User journeys implemented**:
  PID retrieval (completed), Professional qualification EAA verification, Credential issuance (completed), Generic EAA verification (completed)
* **Target groups and end-user roles**:
  Spanish medical doctors engaged by CGCOM, who have received their certificates from CGCOM, administrative staff
* **Electronic Attestations of Attributes (EAAs) involved**:
  PID (Person Identification Data), Professional qualification (EAA: ProfessionalMedicalCertification)
* **Institutional systems/databases connected**:
  SKS owned medications information portal, identity verification system
* **Technical components used**:

  * **Pilot option**: Pilot2 (Hybrid Trust: Classical PKI + Decentralised PKI)
  * **Wallet(s)**: EUDI Wallet (EUDIW by IZERTIS)
  * **Issuer platform**: Verifier (ATOS)
  * **Verifier platform**: uSelf Verifier (ATOS)
  * **PID Retrieval Service**: Lithuanian national PID provider integration
* **Governance configuration**:

  * **Trust model**: Hybrid (X.509 PKI + DIDs + EBSI Trust Registries)
  * **Issuer DID**:

    ```
    [DID to be registered in EBSI network]
    ```
  * **Verifier DID**:

    ```
    [DID to be registered in EBSI network]
    ```
  * **Issuer public key reference (PKI)**:

    ```
    Subject CN: lspsks.sks.lt
    Organization: Skaitos kompiuterių servisas
    Country: LT
    Algorithm: EC (Elliptic Curve)
    Key Size: 256 bits
    Security Level: Strong (256-bit EC equivalent to 3072-bit RSA)
    Certificate Chain: 3 certificate(s)
    ```
  * **Relying Party certificate**: Provided via DC4EU PKI infrastructure
  * **Registry references**: EBSI Trust Registry entries, Lithuanian Sectorial EAA Catalogue
* **Monitoring and feedback mechanisms**:
  Online feedback surveys, weekly monitoring reports with KPIs, managed by SPOC

---

## 3. Legal, Organisational and Operational Details

* **Regulatory context**:

  * GDPR compliance
  * eIDAS2 alignment and regulation
  * Lithuanian national regulations
  * Professional medical qualification regulations
* **Risk management**:
  Risk of incorrect detection of qualification (medium likelihood/high impact) mitigated via wallet's EAA filtering and identity verification protocols; risk of user confusion (medium likelihood/medium impact) mitigated via training and support
* **Credential lifecycle management**:

  * Revocation: Not applicable (verification-focused scenario)
  * Suspension: Not applicable (verification-focused scenario)
* **Infrastructure readiness**:

  * Portal authentication systems, integration endpoints with ATOS and IZERTIS systems, secure databases, hardware/software compliant with DC4EU standards
* **Training and onboarding**:
  Initial basic training covering eIDAS2, PID, EAAs, DC4EU framework, and EUDIW importance; practical training on PID retrieval and wallet setup
* **Issue escalation**:

  * SPOC contact: Virginijus Jasaitis
  * Escalation via SPOC contact, clearly defined response times, and documented resolutions
* **Success indicators and KPIs**:

  * Successful onboarding completion rate
  * EAA verification success rate
  * User satisfaction measured via structured surveys

---

## 4. Trust Model Onboarding Evidences

* **Issuer DID and metadata**:

  ```
  [DID to be registered in EBSI network]
  ```
* **Verifier DID and metadata**:

  ```
  [DID to be registered in EBSI network]
  ```
* **Issuer public key reference (PKI)**:

  ```
  -----BEGIN CERTIFICATE-----
  [PKI Certificate for lspsks.sks.lt - 3 certificate chain]
  Subject: C=LT, O=Skaitos kompiuterių servisas, CN=lspsks.sks.lt
  Key Algorithm: EC (prime256v1)
  Signature Algorithm: ecdsa-with-SHA256
  -----END CERTIFICATE-----
  ```
* **Relying Party certificate**:
  Provided via DC4EU consolidated PKI infrastructure
* **Registry references**:
  EBSI Trust Registry entries (pending registration), Lithuanian Sectorial EAA Catalogue
* **PID credentials used**:
  Lithuanian national eIDAS 2.0 compliant PID credentials
* **Proof of wallet compatibility tests**:
  Integration testing completed with EUDIW by IZERTIS

---

## 5. Implementation and Testing Progress

* **Scenario status**: Completed
* **Number of users onboarded**:
  Spanish medical doctors (25) successfully onboarded for professional qualification verification
* **Credentials issued**:
  Not applicable (verification-focused scenario)
* **Credentials verified**:
  PID verification completed during PID retrieval user journey, Professional qualification (ProfessionalMedicalCertification) verified
* **Successes**:
  Successful PKI certificate deployment, ATOS/IZERTIS integration completed, PID retrieval user journey executed successfully, professional qualification verification workflows demonstrated, effective cross-border professional credential recognition
* **Issues encountered**:
  DID registration pending, minor technical optimisation requirements for professional verification context
* **Deviation from plan**:
  EBSI DID registration timing adjustments, implementation proceeded as planned with successful verification functionality

---

## 6. Testing Results and Observations

* **What worked as expected**:
  * PKI certificate infrastructure deployment successful
  * ATOS verifier platform integration completed
  * IZERTIS wallet integration functional
  * PID retrieval user journey executed successfully
  * Professional qualification verification completed
  * Cross-border professional credential recognition functional
  * Medical professional onboarding process effective
  * W3C Verifiable Credentials verification successful
  * Lithuanian regulatory compliance achieved
* **What did not work and why**:
  * DID registration process still in progress
  * Some performance optimisation needed for large-scale professional verification
* **Feedback from users**:
  Positive response from Spanish medical professionals, appreciation for cross-border professional qualification recognition and potential for professional mobility
* **Impact on user experience and feasibility**:
  Demonstrates successful feasibility of hybrid trust model approach for professional qualification verification across borders. Strong potential demonstrated for enhancing professional mobility and qualification recognition.

---

## 7. Evidence Archive and References

* **Screenshots or logs**:
  Available in DC4EU workspace: Lithuania-SKS folder
* **Credential samples**:
  Professional qualification verification samples (redacted) available for review
* **Links to shared environment/demo**:
  https://lspsks.sks.lt (DNS endpoint operational)
* **Documents or repositories**:
  SKS scenario characterisation documents, technical integration specifications
* **KPI data submission details**:
  Weekly reports to WP5 using DC4EU structured templates

---

## 8. Next Steps and Recommendations

* **Pending actions**:
  * Complete EBSI DID registration
  * Performance optimisation for larger-scale professional verification
  * Cross-border verification testing expansion
  * Professional qualification verification scaling
* **Recommendations for future pilots or replication**:
  * Early completion of DID registration processes
  * Focus on professional qualification verification provides clear value for cross-border professional mobility
  * Standardise professional qualification credential formats
  * Implement comprehensive training programmes for professional verification contexts

---

## 9. Summary of End-User Feedback

* General impressions:
  Positive reception from Spanish medical professionals, strong appreciation for cross-border professional qualification recognition
* Ease of use of wallets and services:
  High usability reported for professional verification workflows
* Challenges encountered:
  Initial learning curve for digital professional qualification concepts, successfully addressed through training
* Suggestions for improvement:
  Request for additional professional qualification types, interest in enhanced verification features
* Willingness to use again:
  High willingness expressed, strong interest in expanding to other professional contexts

---

## 10. Summary of Piloting Agent Insights

* Feedback on support received:
  Excellent support from ATOS and IZERTIS technical teams, effective coordination for professional verification context
* Main barriers during implementation:
  DID registration process timing, minor technical optimisation requirements for professional verification
* Lessons learned:
  Value of professional qualification verification for cross-border mobility, importance of early DID registration, effectiveness of ATOS/IZERTIS solution for professional contexts
* Observed impact and value:
  Demonstrates significant potential for transforming professional qualification verification and cross-border professional mobility
* Recommendations for scaling:
  * Complete DID registration infrastructure for all professional verification scenarios
  * Expand professional qualification verification to other professional domains
  * Standardise professional qualification credential formats across European countries
  * Develop comprehensive training materials for professional verification adoption
  * Create clear integration pathways for professional qualification authorities