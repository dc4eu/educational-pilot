# DC4EU Deployment and Testing Scenarios Results Library (DTSRL) – Scenario: HOWEST University College of Applied Science

## 1. Scenario Identification

* **Piloting agent name**: HOWEST University College of Applied Science & Walt.ID
* **Scenario title**: Campus Access Control System using Verifiable Credentials with Walt.ID Solution
* **Date of submission**: 11 July 2025
* **Point of contact (SPOC)**: Daniel Du Seuil

---

## 2. Scenario Characterisation

* **User journeys implemented**:
  User authentication through Keycloak credentials, Student card ID request as VC offer with access claims, VC offer import into compliant wallet, VC presentation as QR code to verifier (Raspberry Pi), Physical access control validation
* **Target groups and end-user roles**:
  Researchers and interns (approximately 10 users selected for pilot testing)
* **Electronic Attestations of Attributes (EAAs) involved**:
  AccessCredential (VerifiableCredential with AccessCredential claims)
* **Institutional systems/databases connected**:
  Keycloak OIDC authentication system, none for institutional academic systems
* **Technical components used**:

  * **Pilot option**: Pilot2 (Decentralised PKI)
  * **Wallet(s)**: Walt.ID web wallet (provided as part of PoC)
  * **Issuer platform**: Walt.ID Issuer
  * **Verifier platform**: Walt.ID Verifier (Raspberry Pi with camera)
  * **Authentication**: Keycloak OIDC
  * **Infrastructure**: Dell R450 servers, Proxmox cluster, nginx reverse proxy
* **Governance configuration**:

  * **Trust model**: Decentralised PKI (dPKI)
  * **DNS endpoint**: lsphowest.cyber3lab.be
  * **Issuer DID**: Registered in EBSI Trust Registry
  * **Verifier DID**: Registered in EBSI Trust Registry
  * **Issuer public key reference (PKI)**:

    ```
    Subject CN: WIP
    Organization: Howest University
    Country: BE
    Algorithm: EC (Elliptic Curve)
    Key Size: 256 bits
    Security Level: Strong (256-bit EC equivalent to 3072-bit RSA)
    Certificate Chain: PKI certificate deployment pending
    ```
  * **Relying Party certificate**: Decentralised PKI approach - not applicable
  * **Registry references**: EBSI Trust Registry entries for DID registration
* **Monitoring and feedback mechanisms**:
  Weekly in-person feedback surveys, weekly progress reporting to WP5

---

## 3. Legal, Organisational and Operational Details

* **Regulatory context**:

  * GDPR compliance maintained
  * Belgian educational governance requirements
  * Campus security and access control regulations
* **Risk management**:

  * System unavailability (low likelihood/high impact) mitigated by fallback to existing RFID access control system
  * PII leaks (low likelihood/high impact) mitigated by using Keycloak instead of Microsoft Entra (no PII stored in system)
* **Credential lifecycle management**:

  * Standard VC lifetime: 365 days unless revoked
  * Revocation: Supported through Walt.ID infrastructure
  * Suspension: Implemented via Keycloak access controls
* **Infrastructure readiness**:

  * Keycloak OIDC authentication operational
  * Walt.ID stack deployed and functional
  * Dell R450 servers with Proxmox cluster infrastructure ready
  * Physical access control mechanism (Raspberry Pi with camera) installed
* **Training and onboarding**:
  Instructional demo sessions conducted in-person with selected researchers and interns
* **Issue escalation**:

  * SPOC contact: Daniel Du Seuil
  * Technical escalation via Walt.ID support channels
  * Legal SPOC assigned for compliance matters
* **Success indicators and KPIs**:

  * Successful onboarding completion rate
  * VC issuance success rate
  * Physical access verification success rate (green/red LED indication)
  * User satisfaction measured via weekly surveys

---

## 4. Trust Model Onboarding Evidences

* **Issuer DID and metadata**:
  Registered in EBSI Trust Registry (specific DID pending final registration)
* **Verifier DID and metadata**:
  Registered in EBSI Trust Registry (specific DID pending final registration)
* **Issuer public key reference (PKI)**:

  ```
  Subject: C=BE, O=Howest University, CN=WIP
  Key Algorithm: EC (prime256v1)
  Key Size: 256 bits
  Security Assessment: Strong (256-bit EC equivalent to 3072-bit RSA)
  Format: PEM
  Certificate Chain: Pending completion
  ```
* **Relying Party certificate**:
  Not applicable (decentralised PKI approach with Walt.ID solution)
* **Registry references**:
  EBSI Trust Registry entries for DID registration
* **PID credentials used**:
  Not applicable (access control scenario without PID requirement)
* **Proof of wallet compatibility tests**:
  Integration testing completed with Walt.ID web wallet

---

## 5. Implementation and Testing Progress

* **Scenario status**: Completed
* **Number of users onboarded**:
  10 researchers and interns selected and trained for pilot testing
* **Credentials issued**:
  AccessCredential (VerifiableCredential with access permissions)
* **Credentials verified**:
  Physical access verification through QR code presentation to Raspberry Pi verifier
* **Successes**:

  * Walt.ID stack successfully deployed and integrated
  * Keycloak OIDC authentication functioning properly
  * Physical access control mechanism (Raspberry Pi) operational
  * VC issuance and verification workflow completed successfully
  * User onboarding and training programme established
  * Proof of concept demonstration successful with LED indication system
* **Issues encountered**:
  Minor setup challenges with Raspberry Pi camera integration, resolved through technical support
* **Deviation from plan**:
  No significant deviations; implementation proceeded as planned with successful access control demonstration

---

## 6. Testing Results and Observations

* **What worked as expected**:

  * Keycloak OIDC authentication integration successful
  * Walt.ID issuer and verifier platform functionality confirmed
  * VC issuance workflow through web portal operating smoothly
  * Walt.ID web wallet integration functional
  * QR code generation and scanning mechanism working properly
  * Physical access control with LED indication (green/red light) functioning as designed
  * User training and onboarding process effective
* **What did not work and why**:

  * Initial Raspberry Pi camera calibration required fine-tuning for optimal QR code scanning
  * Minor performance considerations for scaling beyond proof of concept
* **Feedback from users**:
  Positive response to the innovative access control approach using verifiable credentials. Users appreciated the seamless integration between digital wallet and physical access systems. The proof of concept nature was well understood, with enthusiasm for potential full deployment.
* **Impact on user experience and feasibility**:
  Demonstrates successful feasibility of decentralised identity approach for campus access control. User experience enhanced by familiar authentication (Keycloak) combined with innovative VC-based access verification. Proof of concept successfully validates technical approach for broader institutional deployment.

---

## 7. Evidence Archive and References

* **Screenshots or logs**:
  Available in DC4EU workspace: Belgium-HOWEST folder
* **Credential samples**:
  AccessCredential samples (redacted) available for technical review
* **Links to shared environment/demo**:
  https://lsphowest.cyber3lab.be (DNS endpoint operational)
* **Documents or repositories**:
  HOWEST scenario characterisation documents, Walt.ID integration specifications, Raspberry Pi setup documentation
* **KPI data submission details**:
  Weekly reports to WP5 using DC4EU structured templates

---

## 8. Next Steps and Recommendations

* **Pending actions**:

  * Performance optimisation for larger-scale campus deployment
  * Integration with existing campus management systems
  * Documentation of lessons learned for other institutions
  * Exploration of additional use cases beyond access control
  * Preparation for production deployment beyond proof of concept
* **Recommendations for future pilots or replication**:

  * Early engagement with Walt.ID technical team for infrastructure setup
  * Standardise physical verification mechanisms across educational institutions
  * Establish clear integration procedures with existing authentication systems
  * Implement comprehensive user training programmes for VC concepts
  * Consider integration with institutional student information systems

---

## 9. Summary of End-User Feedback

* **General impressions**:
  Highly positive reception of innovative access control concept, appreciation for seamless integration between digital and physical systems
* **Ease of use of wallets and services**:
  Walt.ID web wallet interface found intuitive and user-friendly
* **Challenges encountered**:
  Initial understanding of verifiable credential concepts required explanation, minor learning curve for QR code presentation process
* **Suggestions for improvement**:
  Request for mobile wallet options, suggestions for broader campus integration beyond research lab access
* **Willingness to use again**:
  High willingness expressed, with interest in expanded use cases across campus facilities

---

## 10. Summary of Piloting Agent Insights

* **Feedback on support received**:
  Excellent technical support from Walt.ID team, effective coordination with DC4EU project partners
* **Main barriers during implementation**:
  Initial hardware setup complexities, integration of physical verification components with digital infrastructure
* **Lessons learned**:

  * Importance of early hardware testing for physical verification components
  * Value of proof of concept approach for demonstrating feasibility
  * Need for clear user education on verifiable credential concepts
  * Benefits of decentralised approach for institutional autonomy
* **Observed impact and value**:
  Demonstrates potential for modernising campus access control systems, validates technical feasibility of VC-based physical access, provides foundation for broader digital identity initiatives within educational institutions
* **Recommendations for scaling**:

  * Standardise decentralised PKI deployment procedures for educational institutions
  * Develop clear integration pathways for existing campus management systems
  * Create comprehensive training materials for institutional adoption
  * Establish best practices for physical verification mechanism deployment
  * Build institutional capacity for managing decentralised identity infrastructure