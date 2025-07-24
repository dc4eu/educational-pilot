# DC4EU Deployment and Testing Scenarios Results Library (DTSRL) – Scenario: University of Silesia in Katowice (US)

## 1. Scenario Identification

* **Piloting agent name**: University of Silesia in Katowice (US)
* **Scenario title**: Educational Credential Issuance and Verification with Hybrid Trust Framework (OPI/NASK SaaS Solution)
* **Date of submission**: 11 July 2025
* **Point of contact (SPOC)**: OPI/NASK Representative

---

## 2. Scenario Characterisation

* **User journeys implemented**:
  PID retrieval (completed), Onboarding in education, EducationalID issuance (completed), Educational achievement issuance (completed), Generic EAA verification (completed)
* **Target groups and end-user roles**:
  University students, academic administrative staff, registry office personnel
* **Electronic Attestations of Attributes (EAAs) involved**:
  PID (Person Identification Data), EducationalID, Educational Achievement (EAAs: University degrees, Academic certificates)
* **Institutional systems/databases connected**:
  US authentic source databases (academic records), identity verification system, student information system
* **Technical components used**:

  * **Pilot option**: Pilot2 (Hybrid Trust: Classical PKI + Decentralised PKI)
  * **Wallet(s)**: EUDI Wallet
  * **Issuer platform**: OPI/NASK SaaS national instance
  * **Verifier platform**: OPI/NASK SaaS Verifier
  * **PID Retrieval Service**: Polish national PID provider integration
* **Governance configuration**:

  * **Trust model**: Hybrid (X.509 PKI + DIDs + EBSI Trust Registries)
  * **Issuer DID**:

    ```
    did:ebsi:zwRA3Y3iBqx1J249in1Li8c
    ```
  * **Verifier DID**:

    ```
    did:ebsi:zwRA3Y3iBqx1J249in1Li8c
    ```
  * **Issuer public key reference (PKI)**:

    ```
    Subject CN: u2.pilot-dc4eu.ebsi.nask.pl
    Organization: University of Silesia in Katowice
    Country: PL
    Algorithm: EC (Elliptic Curve)
    Key Size: 256 bits
    Security Level: Strong (256-bit EC equivalent to 3072-bit RSA)
    Certificate Chain: 3 certificate(s)
    ```
  * **Relying Party certificate**: Provided via DC4EU PKI infrastructure
  * **Registry references**: EBSI Trust Registry entries, Polish Sectorial EAA Catalogue
* **Monitoring and feedback mechanisms**:
  Online feedback surveys, weekly monitoring reports with KPIs, managed by SPOC

---

## 3. Legal, Organisational and Operational Details

* **Regulatory context**:
  * GDPR compliance
  * eIDAS2 alignment and regulation
  * Polish national higher education regulations
* **Risk management**:
  Risk of incorrect identity matching (medium likelihood/high impact) mitigated via identity verification protocols; risk of user confusion (medium likelihood/medium impact) mitigated via training and support
* **Credential lifecycle management**:
  * Revocation: Implemented via EBSI Trust Registry
  * Suspension: Implemented via institutional controls
* **Infrastructure readiness**:
  * Test environment operational with OPI/NASK SaaS integration
  * Production readiness: Achieved
* **Training and onboarding**:
  University students and approximately 4 administrative staff trained
* **Issue escalation**:
  * SPOC contact: OPI/NASK Representative
  * Polish national infrastructure support
* **Success indicators and KPIs**:
  * Successful onboarding completion rate
  * EAA issuance rate
  * EAA verification success rate
  * User satisfaction measured via structured surveys

---

## 4. Trust Model Onboarding Evidences

* **Issuer DID and metadata**:
  ```
  did:ebsi:zwRA3Y3iBqx1J249in1Li8c
  ```
* **Verifier DID and metadata**:
  ```
  did:ebsi:zwRA3Y3iBqx1J249in1Li8c
  ```
* **Issuer public key reference (PKI)**:
  ```
  -----BEGIN CERTIFICATE-----
  [PKI Certificate for u2.pilot-dc4eu.ebsi.nask.pl - 3 certificate chain]
  Subject: C=PL, O=University of Silesia in Katowice, CN=u2.pilot-dc4eu.ebsi.nask.pl
  Key Algorithm: EC (prime256v1)
  Signature Algorithm: ecdsa-with-SHA256
  -----END CERTIFICATE-----
  ```
* **Relying Party certificate**: Provided via DC4EU consolidated PKI infrastructure
* **Registry references**: EBSI Trust Registry entries (registered), Polish Sectorial EAA Catalogue
* **PID credentials used**: Polish national eIDAS 2.0 compliant PID credentials
* **Proof of wallet compatibility tests**: Integration testing completed with OPI/NASK SaaS solution

---

## 5. Implementation and Testing Progress

* **Scenario status**: Completed
* **Number of users onboarded**: University students successfully onboarded for credential testing
* **Credentials issued**: PID (Person Identification Data), EducationalID, Educational Achievement (University degrees)
* **Credentials verified**: PID verification completed during PID retrieval user journey, EducationalID verified, Educational Achievement verified
* **Successes**: Successful PKI certificate deployment, OPI/NASK SaaS integration completed, EBSI DID registration completed, comprehensive educational credential workflows demonstrated
* **Issues encountered**: Minor initial configuration requirements for Polish regulatory context, successfully resolved
* **Deviation from plan**: No significant deviations, implementation proceeded as planned

---

## 6. Testing Results and Observations

* **What worked as expected**:
  * PKI certificate infrastructure deployment successful
  * OPI/NASK SaaS platform integration completed
  * EUDI Wallet integration functional
  * All user journeys executed successfully
  * Polish regulatory compliance achieved
* **What did not work and why**:
  * Minor performance considerations for scaling
  * Initial user training requirements addressed through training
* **Feedback from users**: Positive response from university students, appreciation for digital credential innovation
* **Impact on user experience and feasibility**: Demonstrates successful feasibility of hybrid trust model for Polish university context

---

## 7. Evidence Archive and References

* **Screenshots or logs**: Available in DC4EU workspace: Poland-US folder
* **Credential samples**: EducationalID and University degree samples (redacted) available for review
* **Links to shared environment/demo**: https://u2.pilot-dc4eu.ebsi.nask.pl (DNS endpoint operational)
* **Documents or repositories**: US scenario characterisation documents, OPI/NASK SaaS integration specifications
* **KPI data submission details**: Weekly reports to WP5 using DC4EU structured templates

---

## 8. Next Steps and Recommendations

* **Pending actions**: Performance optimisation, documentation of lessons learned, cross-border verification testing
* **Recommendations for future pilots or replication**: OPI/NASK SaaS solution provides effective implementation pathway for Polish universities

---

## 9. Summary of End-User Feedback

* General impressions: Positive reception from university students
* Ease of use of wallets and services: High usability reported
* Challenges encountered: Initial learning curve successfully addressed through training
* Suggestions for improvement: Request for additional credential types, enhanced Polish language support
* Willingness to use again: High willingness expressed

---

## 10. Summary of Piloting Agent Insights

* Feedback on support received: Excellent support from OPI/NASK technical team
* Main barriers during implementation: Polish regulatory context integration
* Lessons learned: Value of national SaaS solution for rapid deployment
* Observed impact and value: Demonstrates significant potential for transforming Polish higher education
* Recommendations for scaling: Expand OPI/NASK SaaS solution to other Polish universities