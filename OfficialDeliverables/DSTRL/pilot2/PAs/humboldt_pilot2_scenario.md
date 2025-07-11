# DC4EU Deployment and Testing Scenarios Results Library (DTSRL) – Scenario: Humboldt-Universität zu Berlin (HU-BERLIN)

## 1. Scenario Identification

* **Piloting agent name**: Humboldt-Universität zu Berlin (HU-BERLIN)
* **Scenario title**: Educational Credential Issuance and Verification with Hybrid Trust Framework (GovPart SaaS Solution)
* **Date of submission**: 11 July 2025
* **Point of contact (SPOC)**: Tamas Molnar

---

## 2. Scenario Characterisation

* **User journeys implemented**:
  PID retrieval (completed), Onboarding in education, EducationalID issuance (completed), Educational achievement issuance (completed), Generic EAA verification (completed)
* **Target groups and end-user roles**:
  University students, academic administrative staff, registry office personnel
* **Electronic Attestations of Attributes (EAAs) involved**:
  PID (Person Identification Data), EducationalID, Educational Achievement (EAAs: University certificates, Academic records)
* **Institutional systems/databases connected**:
  HU-BERLIN authentic source databases (academic records), identity verification system, student information system
* **Technical components used**:

  * **Pilot option**: Pilot2 (Hybrid Trust: Classical PKI + Decentralised PKI)
  * **Wallet(s)**: EUDI Wallet
  * **Issuer platform**: GovPart SaaS instance
  * **Verifier platform**: GovPart SaaS Verifier
  * **PID Retrieval Service**: German national PID provider integration
* **Governance configuration**:

  * **Trust model**: Hybrid (X.509 PKI + DIDs + EBSI Trust Registries)
  * **Issuer DID**:

    ```
    did:ebsi:zrEmmNaGMfm7rx4u6xaGGjn
    ```
  * **Verifier DID**:

    ```
    did:ebsi:zrEmmNaGMfm7rx4u6xaGGjn
    ```
  * **Issuer public key reference (PKI)**:

    ```
    Subject CN: lsphub.govpart.de
    Organization: Humboldt-Universität zu Berlin
    Country: DE
    Algorithm: EC (Elliptic Curve)
    Key Size: 256 bits
    Security Level: Strong (256-bit EC equivalent to 3072-bit RSA)
    Certificate Chain: 3 certificate(s)
    ```
  * **Relying Party certificate**: Provided via DC4EU PKI infrastructure
  * **Registry references**: EBSI Trust Registry entries, German Sectorial EAA Catalogue
* **Monitoring and feedback mechanisms**:
  Online feedback surveys, weekly monitoring reports with KPIs, managed by SPOC

---

## 3. Legal, Organisational and Operational Details

* **Regulatory context**:

  * GDPR compliance
  * eIDAS2 alignment and regulation
  * German national higher education regulations
  * Berlin state education requirements
* **Risk management**:
  Risk of incorrect identity matching (medium likelihood/high impact) mitigated via identity verification protocols; risk of user confusion (medium likelihood/medium impact) mitigated via training and support
* **Credential lifecycle management**:

  * Revocation: Implemented via EBSI Trust Registry
  * Suspension: Implemented via institutional controls
* **Infrastructure readiness**:

  * Test environment operational with GovPart SaaS integration
  * Production readiness: Achieved
* **Training and onboarding**:
  University students and approximately 4 administrative staff trained
* **Issue escalation**:

  * SPOC contact: Tamas Molnar
  * GovPart technical support integration
* **Success indicators and KPIs**:

  * Successful onboarding completion rate
  * EAA issuance rate
  * EAA verification success rate
  * User satisfaction measured via structured surveys

---

## 4. Trust Model Onboarding Evidences

* **Issuer DID and metadata**:

  ```
  did:ebsi:zrEmmNaGMfm7rx4u6xaGGjn
  ```
* **Verifier DID and metadata**:

  ```
  did:ebsi:zrEmmNaGMfm7rx4u6xaGGjn
  ```
* **Issuer public key reference (PKI)**:

  ```
  -----BEGIN CERTIFICATE-----
  [PKI Certificate for lsphub.govpart.de - 3 certificate chain]
  Subject: C=DE, O=Humboldt-Universität zu Berlin, CN=lsphub.govpart.de
  Key Algorithm: EC (prime256v1)
  Signature Algorithm: ecdsa-with-SHA256
  -----END CERTIFICATE-----
  ```
* **Relying Party certificate**:
  Provided via DC4EU consolidated PKI infrastructure
* **Registry references**:
  EBSI Trust Registry entries (registered), German Sectorial EAA Catalogue
* **PID credentials used**:
  German national eIDAS 2.0 compliant PID credentials
* **Proof of wallet compatibility tests**:
  Integration testing completed with GovPart SaaS solution

---

## 5. Implementation and Testing Progress

* **Scenario status**: Completed
* **Number of users onboarded**:
  University students successfully onboarded for credential testing
* **Credentials issued**:
  PID (Person Identification Data), EducationalID, Educational Achievement (University certificates)
* **Credentials verified**:
  PID verification completed during PID retrieval user journey, EducationalID verified, Educational Achievement verified
* **Successes**:
  Successful PKI certificate deployment, GovPart SaaS integration completed, EBSI DID registration completed (did:ebsi:zrEmmNaGMfm7rx4u6xaGGjn), PID retrieval user journey executed successfully, comprehensive educational credential issuance and verification workflows demonstrated, effective integration with German governance framework
* **Issues encountered**:
  Minor initial configuration requirements for German regulatory context, successfully resolved
* **Deviation from plan**:
  No significant deviations, implementation proceeded as planned with successful completion via GovPart SaaS

---

## 6. Testing Results and Observations

* **What worked as expected**:
  * PKI certificate infrastructure deployment successful
  * GovPart SaaS platform integration completed
  * EUDI Wallet integration functional
  * PID retrieval user journey executed successfully
  * EducationalID issuance and verification completed
  * Educational Achievement issuance and verification completed
  * University student onboarding process effective
  * W3C Verifiable Credentials implementation successful
  * German regulatory compliance achieved
* **What did not work and why**:
  * Minor performance considerations for scaling beyond pilot scope
  * Some initial user training requirements for digital credential concepts
* **Feedback from users**:
  Positive response from university students, appreciation for digital credential innovation and potential for academic mobility within Germany and Europe
* **Impact on user experience and feasibility**:
  Demonstrates successful feasibility of hybrid trust model approach for German university context using GovPart SaaS solution. Strong potential demonstrated for enhancing student mobility and credential recognition.

---

## 7. Evidence Archive and References

* **Screenshots or logs**:
  Available in DC4EU workspace: Germany-HU-BERLIN folder
* **Credential samples**:
  EducationalID and University certificate samples (redacted) available for review
* **Links to shared environment/demo**:
  https://lsphub.govpart.de (DNS endpoint operational)
* **Documents or repositories**:
  HU-BERLIN scenario characterisation documents, GovPart SaaS integration specifications
* **KPI data submission details**:
  Weekly reports to WP5 using DC4EU structured templates

---

## 8. Next Steps and Recommendations

* **Pending actions**:
  * Performance optimisation for larger-scale deployment across university
  * Documentation of lessons learned for other German universities
  * Cross-border verification testing with additional European institutions
  * Preparation for full university deployment
* **Recommendations for future pilots or replication**:
  * GovPart SaaS solution provides effective implementation pathway
  * Early integration with German governance frameworks
  * Standardise German university credential formats
  * Implement comprehensive training programmes for German university contexts

---

## 9. Summary of End-User Feedback

* General impressions:
  Positive reception from university students, strong appreciation for digital transformation of academic credentials
* Ease of use of wallets and services:
  High usability reported, successful completion of all educational credential user journeys
* Challenges encountered:
  Initial learning curve for digital credential concepts, successfully addressed through training
* Suggestions for improvement:
  Request for additional credential types, interest in enhanced German language support
* Willingness to use again:
  High willingness expressed, strong interest in expanding across university

---

## 10. Summary of Piloting Agent Insights

* Feedback on support received:
  Excellent support from GovPart technical team, effective SaaS solution deployment
* Main barriers during implementation:
  German regulatory context integration, minor technical optimisation requirements
* Lessons learned:
  Value of SaaS solution for rapid deployment, importance of German regulatory alignment, effectiveness of GovPart platform
* Observed impact and value:
  Demonstrates significant potential for transforming German higher education credential management
* Recommendations for scaling:
  * Expand GovPart SaaS solution to other German universities
  * Standardise German university credential formats
  * Develop comprehensive training materials for German university adoption
  * Create clear integration pathways for German higher education institutions