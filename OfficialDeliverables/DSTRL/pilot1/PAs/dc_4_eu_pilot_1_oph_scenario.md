# DC4EU Deployment and Testing Scenarios Results Library (DTSRL) – Scenario: Finnish National Agency for Education (OPH)

## 1. Scenario Identification

- **Piloting agent name**: Finnish National Agency for Education (OPH)
- **Scenario title**: PID and Educational Credential Issuance and Verification (Finnish National Solution)
- **Date of submission**: July 2025
- **Point of contact (SPOC)**: Finnish National Agency for Education (OPH)

---

## 2. Scenario Characterisation

- **User journeys implemented**:
  - Wallet installation
  - PID retrieval
  - Educational credential issuance
  - QR-based verification
  - Credential presentation to verifiers (DVV test verifier and DC4EU verifier)
- **Target groups and end-user roles**:
  - Students (test users)
  - Target: 25 test identities issued from the national test identity register
  - Administrative staff
- **Electronic Attestations of Attributes (EAAs) involved**:
  - PID (Person Identification Data)
  - Completed Degrees (vocational, secondary education and tertiary education)
- **Institutional systems/databases connected**:
  - National transfer service for educational data for national registries
  - KOSKI (secondary, vocational education)
  - VIRTA (higher education)
- **Technical components used**:
  - **Pilot option**: Pilot1 (Classical PKI, national sealing certificates)
  - **SaaS environment**: Finnish DVV issuance service and verifier services
  - **Wallet**: Finnish EUDI Wallet Demo (Android)
  - **Issuer platform**: DVV Issuance Service
  - **Verifier platform**: DVV Test Verifier, DC4EU Verifier
  - **Authentic source**: OPH (Studyinfo service)
- **Governance configuration**:
  - **Trust model**: Centralised issuance model (PUB-EAA)
  - Consent-based data transfer
  - Credentials sealed manually (no automated PKI integration)
  - **Issuer certificate**: Sealing certificate (sealing-cert.pem) issued by DVV
  - **Relying Party certificate**: Presentation requests signed by DVV-issued certificates but not validated against trust lists
  - **Decentralised Identifiers (DIDs)**: Not applicable
- **Monitoring and feedback mechanisms**:
  - Manual testing logs for registered wallet users and issued credential transactions
  - Feedback collected from test users from on-site testing session (28 May 2025) and from WP5 common feedback survey

---

## 3. Legal, Organisational and Operational Details

- **Regulatory context**:
  - **GDPR compliance**: The scenario adheres to the General Data Protection Regulation (GDPR), with personal data processing based on user consent and the performance of public tasks
  - **National legislation**:
    - The **Act on Information Management in Public Administration (906/2019)** sets requirements for the uniform, high-quality, and secure management of public sector information assets
    - The **Act on the National Registers of Education Records, Qualifications and Degrees (884/2017)** provides the legal foundation for the KOSKI registry and data transfer services. It enables the secure and centralised electronic collection, processing, and disclosure of educational data for learners and authorised authorities. The disclosure of data requires either a statutory right or the individual's consent. The law ensures the accuracy, consistency, and reliability of educational records and supports lifelong learning, recognition of prior learning, and access to education
- **Risk management**:
  - Risks identified and managed in weekly national coordination meetings with DVV
  - **Identified risks**: delayed implementation and lack of documentation for implementing integrations to ecosystem, manual certificate sealing, no revocation support
  - **Risk mitigations**: manual verification, limited test scope, use of internal validation if interoperability is not achieved before testing phase
- **Credential lifecycle management**:
  - **Revocation**: Not implemented
  - **Suspension**: Not implemented
  - The consent expiration to retrieve data from authentic source 24 hours
- **Infrastructure readiness**:
  - **EUDI Wallet**: Android app available via Google Play Store
  - Issuance service and API between authentic source and issuance service operational in test environment
  - Issuance flow accessible via web in test environment
  - Verifier services accessible via web
- **Training and onboarding**:
  - Test users onboarded via registration form
  - Instructions provided via DVV wiki and attached instructions with the registration response email
  - In on-site testing session (28 May 2025) further training given on eIDAS, European Identity Wallet and the LSP
- **Issue escalation**:
  - **SPOC contact**: Direct email contact (OPH)
  - Technical issues handled by DVV development team
- **Success indicators and KPIs**:
  - **KPIs**: Number of credentials issued and verified
  - **Success indicators**: successful end-to-end flows and positive user feedback on usability and clarity

---

## 4. Trust Model Onboarding Evidences

- **Issuer X.509v3 certificate**:
  - Not integrated with national trust anchor; manually created seal used for demo purposes
  - Test-environment seal certificate (sealing-cert.pem) and its CA-certificate (sealing-ca-cert.pem)
- **Relying party certificate and EAA scope**:
  - DVV EUDI Wallet does not require the relying party (RP) to authenticate itself. However, it does require that the presentation request from the RP is digitally signed. The wallet verifies the signature using the public key included in the certificate embedded in the x5c header of the presentation request
  - The certificate is checked for technical validity and expiration, but no trust chain validation is performed:
    - It is not verified whether the certificate was issued by a specific Certificate Authority (CA)
    - It is not checked against any trust list
    - Revocation status of the certificate is also not verified
- **Decentralised Identifiers (DIDs)**: Not applicable
- **Registry references**: Not applicable

---

## 5. Implementation and Testing Progress

- **Scenario status**: Implementation and testing completed
- **Testing period**: 20 May – 15 June 2025. One on-site testing session (28 May 2025)
- **Users onboarded**: 25 registered testers
- **Credentials issued**: 22 educational credentials
- **Credentials verified**: Successfully presented to DC4EU (interoperability testing) and DVV verifiers (10 credentials verified)
- **Summary of operations executed**: Wallet installation, PID issuance, Credential issuance, Credential presentation (DVV verifier and DC4EU verifier). In addition technical interoperability testing issuing educational credential from DVV issuance service to reference wallet (March 2025)
- **Successes**:
  - Designed credential issuance and presentation flows in DVV verifier
  - Consent-based data retrieval from Authentic source
  - Basic technical interoperability with DC4EU verifier (with adjustments) and technical interoperability between DVV issuance service and reference wallet (tested in March 2025)
- **Issues encountered**:
  - Interoperability issues between credential and DC4EU verifier
  - Attribute-level interoperability with DC4EU verifier
  - No revocation support
- **Deviation from plan**:
  - Trust list and revocation not implemented due to time and infrastructure delays
  - Verifier service API to OPH application service not implemented due to infrastructure and documentation delays

---

## 6. Testing Results and Observations

- **What worked as expected**:
  - Designed credential issuance and presentation flows in DVV verifier
  - Consent-based data retrieval from Authentic source
  - Basic technical interoperability with DC4EU verifier (with adjustments)
- **What did not work and why**:
  - Attribute-level interoperability with DC4EU verifier
  - No revocation or trust chain validation
- **Feedback from users**:
  - Generally positive on usability
  - Some confusion around attribute issuance flow due to many steps and multiple consent requests on different services
  - Some feedback on credential visibility in the wallet
- **Impact on user experience and feasibility**:
  - Demonstrated technical feasibility – most feasible trust model still unclear
  - User experience impacted by several consent requests during issuance – need for legal review to streamline steps
  - Identified key areas for standardisation and technical interoperability on credential structure and attribute details
  - Need to discuss the scale of selective disclosure in educational credentials (individual attributes are interconnected)

---

## 7. Evidence Archive and References

- **Screenshots and demo videos**: 
  - Demo videos were captured during wallet installation, PID issuance, credential issuance, and verification
  - Videos on wallet installation and PID issuance available in: [https://wiki.dvv.fi/spaces/EDI/pages/235522018/1.+DVV+n+esimerkkisovellus+Finnish+EUDI+Wallet+Demo+mobile+application](https://wiki.dvv.fi/spaces/EDI/pages/235522018/1.+DVV+n+esimerkkisovellus+Finnish+EUDI+Wallet+Demo+mobile+application)
  - Completed degree credential issuance and verification demo videos added to DC4EU workspace: [Finland-OPH](https://sites.ey.com/:f:/r/sites/DC4EU-EBSINE/Shared%20Documents/General/DC4EU/WP5/03%20Piloting%20agents/05%20Piloting/Pilot1/Finland-OPH?csf=1&web=1&e=PKRG0V)
- **Wallet demo documentation**:
  - DVV Wallet Demo documentation: [https://wiki.dvv.fi/spaces/EDI/pages/235522018/1.+DVV+n+esimerkkisovellus+Finnish+EUDI+Wallet+Demo+mobile+application](https://wiki.dvv.fi/spaces/EDI/pages/235522018/1.+DVV+n+esimerkkisovellus+Finnish+EUDI+Wallet+Demo+mobile+application)
- **Credential samples**:
  - Stored in OPH internal repository
- **KPI submission**:
  - Logs for issuance and verifications interaction collected and stored in DC4EU workspace: [Finland-OPH](https://sites.ey.com/:f:/r/sites/DC4EU-EBSINE/Shared%20Documents/General/DC4EU/WP5/03%20Piloting%20agents/05%20Piloting/Pilot1/Finland-OPH?csf=1&web=1&e=PKRG0V)

---

## 8. Next Steps and Recommendations

- **Pending actions**:
  - Integration with trust framework
  - Implementation of revocation and update mechanisms
  - Support for standardised selective disclosure and attribute-level presentation
- **Recommendations for future pilots**:
  - Ensure early availability of trust infrastructure (API documentation, certificates, revocation, trust lists)
  - Align credential and attribute naming conventions across issuers and verifiers
- **Proposed changes**:
  - More national wallet actors included
  - Early technical implementation of different solutions and more time to cooperate to produce interoperability testing and technical alignment implementation

---

## 9. Summary of End-User Feedback

- **General impressions**: Users found the wallet easy to install and use. Credential issuance was smooth and understandable
- **Ease of use**: The app was intuitive, though some steps like starting the journey to add educational credential to wallet and different consent requests in different steps could be better explained
- **Challenges**: Confusion around what data is shared and how. Lack of visibility into credential structure
- **Suggestions**: Clarify flows and simplify steps
- **Overall readiness**: Positive reception; users expressed interest in using such services in real life if usability is improved and clear use cases where they can use their data
- **Willingness to use again**: Yes

---

## 10. Summary of Piloting Agent Insights

- **Feedback on support**: Common implementation materials (e.g. end user survey, KPI collection) were delayed and materials provided incrementally. Clear compilation of materials and timetable when provided would have been needed
- **Main barriers**: Technical trust infrastructure (WP7) was delayed, limiting full implementation. Credential structure and attribute inconsistencies. Limited time for interoperability testing
- **Lessons learned**: 
  - Consent-based flows need streamlining and legal clarification on the need of consent when issuing to wallet (data transfer to the person themselves, not third party)
  - Interoperability requires strict alignment on data models structure and attribute naming – ELM is usable but interoperability requires deep-level understanding of the data model
  - Early alignment of schemas critical
- **Observed impact**: Demonstrated feasibility of national wallet integration. Identified clear feasible implementation for production-level deployment
- **Recommendations**: 
  - Standardise attribute naming and credential structures
  - Expand pilot to include private sector entities as verifiers to have more use cases based on actual user needs outside academic sector
  - Expand pilots to more verifiers and production readiness

---

**Disclaimer**\
OPH has performed all actions technically feasible within the Pilot1 framework and national infrastructure. Limitations (e.g., no revocation, no trust list integration) were outside OPH's control.

---

## Additional Information: User Journey Details

### Key Actors and Elements

#### Wallet Holder (End-User/Student)
A Finnish citizen or resident who uses the Finnish EUDI Wallet Demo to receive and present educational credentials.

#### Wallet
The Finnish EUDI Wallet Demo, a mobile application developed by the Digital and Population Data Services Agency (DVV). Currently available for Android, it supports SD-JWT-VC credentials and OpenID4VP presentations.

#### Issuer
The Digital and Population Data Services Agency (DVV), which operates the credential issuance service. It converts educational data into verifiable credentials and issues them to the wallet.

#### Relying Party (RP)
Services or organisations that verify the credentials presented by the wallet holder. In this pilot, the DC4EU Verifier and DVV's own test verifier are used.

#### Authentic Source Data Store
The Studyinfo service, governed by the Finnish National Agency for Education (OPH), acts as the authentic source of educational data.

#### Database with Educational Records
KOSKI (primary, secondary, vocational), Virta (higher education), Matriculation Examination Register, and Student Admission Register.

#### Schemes (ELM Schemas)
Educational data is mapped from the national data model to the Europass Learning Model (ELM) and issued in SD-JWT-VC format.

#### Support Channels
- DVV EUDI Wallet Demo documentation: [https://wiki.dvv.fi/spaces/EDI/pages/235522018/1.+DVV+n+esimerkkisovellus+Finnish+EUDI+Wallet+Demo+mobile+application](https://wiki.dvv.fi/spaces/EDI/pages/235522018/1.+DVV+n+esimerkkisovellus+Finnish+EUDI+Wallet+Demo+mobile+application)
- Contact: Kristiina Laipio, Finnish National Agency for Education


### User Journey Flows

#### 1. Credential Issuance Journey
**Objective**: Enable a wallet holder to receive an educational credential from the authentic source via the national issuance service.

**Steps**:
1. The wallet holder opens the Finnish EUDI Wallet Demo and selects: My Documents → Add Document → Completed Degrees
2. The wallet redirects the user to the Studyinfo service
3. The user authenticates using Suomi.fi e-Identification
4. The user consents to the transfer of their educational data
5. KOSKI stores the consent and verifies it upon request
6. DVV's issuance service queries KOSKI using OAuth-based API
7. If consent is valid, KOSKI returns the educational data
8. DVV maps the data to the ELM schema and issues a credential in SD-JWT-VC format
9. The credential is delivered to the wallet

#### 2. Credential Presentation Journey
**Objective**: Allow the wallet holder to present their credential to a verifier (RP) for validation.

**Steps**:
1. The wallet holder accesses a verifier service (e.g., via QR code or direct link)
2. The verifier sends a presentation request (e.g., for completed degrees)
3. The wallet prompts the user to approve the request
4. Upon approval, the wallet sends the credential to the verifier
5. The verifier checks the credential's structure, signature, and content
6. The result is displayed to the verifier (e.g., confirmation of degree)

#### 3. Interoperability Testing Journey
**Objective**: Test the compatibility of Finnish-issued credentials with the DC4EU verifier and reference wallet.

**Steps**:
1. DVV issues credentials to test identities using the Finnish EUDI Wallet Demo
2. Wallet holders present credentials to the DC4EU verifier
3. Compatibility issues are identified:
   - Attribute naming mismatches (e.g., givenName.und vs givenName)
   - Lack of selective disclosure support
   - Credential structure differences (e.g., bulk "has claim" vs individual attributes)
4. Manual adjustments are made to enable partial verification