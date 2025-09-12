## <a id="_Toc182376687"></a><a id="_Toc184710034"></a>Chapter 6: The education and professional qualifications sectorial rulebook

The education and professional qualifications sectorial rulebook aims to establish a standardised approach for managing digital educational and professional credentials within the European Union. The rulebook sets the foundation for trusted digital credential management, encompassing identity, trust, data models, and operational processes. This framework balances member state sovereignty with European integration needs, creating a unified system that supports educational mobility while respecting national and institutional autonomy.

Each component serves both practical needs and policy goals, creating a system that works for students, institutions, and member states while advancing European educational integration.

The technical implementations always support policy priorities, making the system both practically useful and politically aligned with European goals for education, privacy, and mobility.

#### European educational priorities integration:

| Priority Area | Implementation Approach | System Benefits |
|---------------|------------------------|-----------------|
| **Member state sovereignty** | Respect national education authority while enabling interoperability | Countries maintain control over education systems |
| **Institutional independence** | Preserve institutional autonomy within common framework | Universities and schools retain their identity and processes |
| **Student privacy protection** | Privacy-by-design with user control over data sharing | Students control their educational information |
| **Educational mobility support** | Standardised credentials work across European borders | Easy study and work movement across EU |
| **Quality framework integration** | Link to existing European and national quality systems | Maintained educational standards and recognition |
| **Trusted credential creation** | Cryptographic security and verification mechanisms | Tamper-proof, verifiable qualifications |
| **Automatic recognition** | Machine-readable credentials enable automated processing | Faster, more efficient credential verification |
| **Lifelong learning support** | Comprehensive record keeping across formal and informal learning | Complete educational journey documentation |
| **Cross-border functionality** | Seamless operation across European educational systems | True European educational space |

### <a id="_Toc184710035"></a>6.1 Natural person's identity

The European Digital Identity wallet serves as a harmonised electronic identification method, introducing **personal identification data (PID)** as the preferred option when high security is needed. This system respects member state authority over identity while creating a consistent European approach.

#### Educational identity verification scenarios:

| Use Case | Security Requirements | Implementation Method | Benefits |
|----------|---------------------|----------------------|---------|
| **Registration and enrolment** | Medium to high security for student verification | National eID or EUDI wallet with PID | Secure student identification, fraud prevention |
| **Formal degree issuance** | High security for official qualification awarding | EUDI wallet with verified PID, institutional verification | Reliable identity confirmation, credential integrity |

### <a id="_Toc184710036"></a>6.2 Legal entity's identity

Educational institutions need reliable digital identification through **public key infrastructure (PKI)** with **X.509v3 digital certificates**. This system assigns unique digital identifiers to institutions, linking them with public certificates for seamless identity verification across European systems.

#### Institutional identity framework:

| Component | Function | Implementation | Cross-border Benefits |
|-----------|----------|----------------|----------------------|
| **PKI Infrastructure** | Provides cryptographic foundation for institutional identity | X.509v3 digital certificates | Universal recognition across European systems |
| **Unique Digital Identifiers** | Assigns persistent identifiers to institutions | Certificate-based identification system | Reliable institution verification |
| **Public Certificate Linking** | Connects institutions with verifiable certificates | Public key infrastructure integration | Seamless identity verification |
| **Internal Process Integrity** | Maintains institutional processes within European framework | Flexible implementation allowing local adaptation | Preserved institutional autonomy |

### <a id="_Toc184710037"></a>6.3 Identity matching

The combination of personal identification data and member state-specific matching rules creates a unified approach to identity verification. The rulebook acknowledges the complexity of European identity systems by combining personal identification data with member state-specific matching rules.

#### Identity matching framework:

| Component | Purpose | Implementation | Cross-border Impact |
|-----------|---------|----------------|-------------------|
| **Personal Identification Data** | Standardised personal information across EU | Common data elements with privacy protection | Consistent identity verification |
| **Member State Matching Rules** | Accommodate national identity system variations | Flexible rules adapting to national requirements | Respect for national sovereignty |
| **External-Internal Identity Linking** | Connect national identities with institutional records | Secure mapping between identity systems | Accurate student identification across borders |
| **Unified Verification Approach** | Consistent verification while respecting national systems | Standardised process with flexible implementation | Enhanced accuracy and efficiency |

### <a id="_Toc184710038"></a>6.4 Trusted lists

The system maintains several critical lists to support trust in educational credentials:

#### Trusted lists framework:

| List Type | Purpose | Managed By | Educational Policy Impact |
|-----------|---------|-----------|--------------------------|
| **Trusted issuers** | Authorised organisations that can issue credentials | National/European authorities | Maintains academic integrity by authorising only legitimate institutions |
| **Relying parties** | Organisations authorised to verify and accept credentials | Regulatory bodies | Creates clear paths for credential recognition |
| **Trusted accreditation organisations** | Bodies that validate educational institutions | Quality assurance agencies | Links to European quality frameworks like EQAR |
| **Data models catalogue** | Standardised formats for representing educational credentials | Technical governance bodies | Enables consistent credential representation |
| **Trusted schemes** | Templates ensuring consistent credential structure | Standards organisations | Supports automated processing across systems |

### <a id="_Toc184710039"></a>6.5 Lifecycle management

The credential lifecycle system supports educational mobility while protecting credential integrity. This balance enables institutions to manage qualifications independently while ensuring European-wide recognition.

#### Credential lifecycle management features:

| Lifecycle Stage | Management Capabilities | Privacy Features | Educational Mobility Support |
|-----------------|------------------------|------------------|----------------------------|
| **Creation** | Institutional control over credential generation | Privacy-by-design implementation | Standardised format for cross-border recognition |
| **Status tracking** | Real-time status updates (active, suspended, revoked) | Status updates without usage tracking | Reliable verification across borders |
| **Verification services** | Distributed verification maintaining privacy | No tracking of usage patterns | Instant verification for European mobility |
| **Institution management** | Tools for credential lifecycle control | Privacy-preserving status management | Independent management with European compatibility |

### <a id="_Toc184710040"></a>6.6 Data model

The credential data model follows **W3C Verifiable Credential standards**, structuring educational data in a consistent format.

#### Credential data model components:

| Component | Purpose | Implementation | Interoperability Benefits |
|-----------|---------|----------------|--------------------------|
| **Context definitions** | Clear interpretation of credential content | Standardised context vocabularies | Universal understanding across systems |
| **Unique identifier** | Persistent credential identification | Cryptographically secure identifiers | Reliable credential tracking |
| **Credential type** | Classification of credential category | Standardised type definitions | Automated processing and recognition |
| **Issuing authority identifier** | Verification of credential source | Institutional digital signatures | Trust verification across borders |
| **Issue date** | Temporal credential validity | Standardised date formats | Clear validity periods |
| **Credential holder information** | Subject identification data | Privacy-preserving personal data | Secure holder verification |
| **Cryptographic proof** | Tamper-evident security | Digital signatures and proofs | Fraud prevention and integrity |
| **Multi-language support** | Accessibility across European languages | Localised content with common structure | European-wide accessibility |

### <a id="_Toc184710041"></a>6.7 Education and professional qualifications Ontology - European Learning Model (ELM)

The ELM creates a shared understanding of educational achievements across Europe, supporting quality assurance information, links to European and National qualification frameworks, and cross-border recognition support.

#### ELM ontology structure:

| Category | Components | Educational Value | Cross-border Support |
|----------|------------|-------------------|---------------------|
| **Achievement records** | • Qualification titles and descriptions<br>• Classification of achievement<br>• EQF alignment<br>• Issue dates<br>• Issuing institution details | Official recognition of educational accomplishments | Standardised achievement representation |
| **Learning outcomes** | • Knowledge gained<br>• Skills developed<br>• Competences achieved<br>• European skills frameworks links | Clear competency documentation | Skills recognition across borders |
| **Learning activities** | • Type of education received<br>• Duration of study<br>• Learning delivery method | Comprehensive educational context | Study method recognition |
| **Assessment details** | • Evaluation methods used<br>• Grading systems<br>• Assessment authority | Quality assurance and evaluation transparency | Assessment method comparability |
| **Issuer information** | • Legal institution name<br>• Accreditation status<br>• Contact information<br>• Digital identification | Institution verification and trust | Reliable institutional recognition |
| **Holder details** | • Privacy-compliant personal identification<br>• Educational profile linkage | Secure individual identification | Privacy-preserving identity verification |
| **Recognition elements** | • Cross-border agreements<br>• Framework alignments<br>• European Education Area mobility support | Formal recognition mechanisms | Enhanced European mobility |
| **Supporting data** | • Course documentation links<br>• Language of instruction<br>• Geographic context | Additional contextual information | Comprehensive educational context |

### <a id="_Toc184710042"></a>6.8 Issuance

The issuance process varies based on the type of attestation:

#### Electronic attestation types comparison:

| Attestation Type | Provider | Requirements | Characteristics |
|------------------|----------|--------------|----------------|
| **Qualified electronic attestation of attributes (QEAA)** | Qualified trust service providers | • Citizen consent<br>• Data validation through member state mechanisms | Highest legal recognition, strict regulatory compliance |
| **Public sector body electronic attestation of attributes (PSBEAA)** | Public sector bodies | • Specific regulatory compliance<br>• Public sector bodies as authentic source and issuer | Government-backed credentials, regulatory authority |
| **Electronic attestation of attributes (EAA)** | Authorised educational/professional bodies | • Framework compliance<br>• Institutional authorisation | Flexible implementation, institutional control |

#### Electronic Attestation of Attributes (EAA) issuance process:

| Step | Process Activity | Security Measures | Quality Assurance |
|------|------------------|-------------------|-------------------|
| **1. Secure connection** | Establish connection with European Digital Identity Wallet | Encrypted communication, authentication protocols | Secure channel verification |
| **2. Identity verification** | Verify individual identity when required | Multi-factor authentication, privacy protection | Identity assurance levels |
| **3. Identity matching** | Match identity across systems | Privacy-preserving matching algorithms | Accurate identity correlation |
| **4. Data gathering** | Collect information from authentic sources | Authorised data access, audit logging | Source authenticity verification |
| **5. Credential creation** | Generate credential using trusted schemas | Standardised formats, validation rules | Schema compliance checking |
| **6. Quality assurance** | Add quality assurance information | Accreditation data, compliance verification | Quality framework integration |
| **7. Digital identifier** | Select appropriate digital identifier | Cryptographic security, unique identification | Persistent identifier assignment |
| **8. Issuance to wallet** | Direct or deferred issuance to wallet | Secure delivery, acceptance confirmation | Successful credential delivery |

### <a id="_Toc184710043"></a>6.9 Selective disclosure

The system enables users to share only necessary credential data, meeting privacy requirements through advanced technical implementations.

#### Selective disclosure implementation framework:

| Technology | Purpose | Privacy Benefits | Technical Implementation |
|------------|---------|------------------|--------------------------|
| **SD-JWS (Selective Disclosure JSON Web Signature)** | Enable selective information sharing in JSON Web Signatures | Users control which claims to reveal | JSON-based selective disclosure with cryptographic proofs |
| **SD-JWT (Selective Disclosure JSON Web Token)** | Provide selective disclosure for JSON Web Tokens | Granular control over token claims | Token-based selective information sharing |
| **BBS+ (Boneh-Boyen-Shacham)** | Zero-knowledge proof selective disclosure | Mathematical privacy guarantees | Advanced cryptographic selective disclosure |
| **Issuer-defined disclosure policies** | Institutional control over permissible disclosures | Balanced privacy and institutional requirements | Policy-based disclosure management |
| **Privacy-preserving verification** | Verification without exposing unnecessary data | Minimal data exposure during verification | Technical privacy protection mechanisms |

### <a id="_Toc184710044"></a>6.10 Sharing mechanisms

The credential sharing framework supports European mobility through comprehensive sharing and verification capabilities.

#### Credential sharing framework using OpenID for Verifiable Presentations:

| Sharing Component | Function | Security Features | Mobility Benefits |
|-------------------|----------|-------------------|-------------------|
| **Secure wallet connections** | Establish authenticated communication channels | Cryptographic authentication, secure protocols | Reliable cross-border credential sharing |
| **Proof of possession verification** | Confirm credential holder authenticity | Cryptographic proof mechanisms | Prevention of credential misuse |
| **Relying party trustworthiness** | Verify credential verifier legitimacy | Trust list verification, authorisation checking | Secure credential acceptance |
| **Information proportionality validation** | Ensure minimal necessary data sharing | Privacy impact assessment, data minimisation | GDPR compliance and privacy protection |
| **Credential combination** | Enable multiple credential presentation | Composite credential verification | Comprehensive qualification presentation |
| **Selective disclosure policy support** | Implement privacy-preserving sharing | User-controlled information revelation | Enhanced privacy in cross-border sharing |

### <a id="_Toc184710045"></a>6.11 Verification

The verification process ensures credential validity while protecting privacy through a distributed, comprehensive verification system.

#### Verification process framework:

| Verification Stage | Process Steps | Security Measures | Privacy Protection |
|-------------------|---------------|-------------------|-------------------|
| **Initial connection** | 1. Secure wallet connection<br>2. Proof of possession verification | Encrypted communication, authentication protocols | No tracking of verification requests |
| **Credential validation** | 3. Credential request processing<br>4. Integrity verification<br>5. Metadata checking (expiration dates) | Cryptographic verification, tamper detection | Minimal data exposure during validation |
| **Issuer verification** | 6. Digital identifier validation<br>7. Educational accreditation checking<br>8. Accreditation issuer verification<br>9. Status verification | Trust list verification, authority validation | Distributed verification without central monitoring |
| **Compliance checking** | 10. Identity information analysis<br>11. Schema compliance verification | Standards compliance, format validation | Privacy-preserving compliance verification |
| **Quality assurance** | 12. Issuer entitlement checking<br>13. Expiration verification<br>14. Status checking | Quality framework integration, validity confirmation | Quality verification without usage tracking |
| **Audit and completion** | 15. Credential status verification<br>16. Record keeping for audit purposes | Audit trail maintenance, compliance logging | Privacy-compliant audit logging |

#### Key verification characteristics:

- **Distributed system**: Avoids single points of failure through distributed verification architecture
- **Privacy protection**: Prevents issuer monitoring while maintaining verification integrity
- **Time-based validation**: Links verification to credential issuance timing for enhanced security

### <a id="_Toc184710046"></a>6.12 Enforcement policy agent

The wallet's policy enforcement role implements European privacy principles in practical ways, ensuring comprehensive privacy protection and user control.

#### Digital wallet policy enforcement mechanisms:

| Enforcement Function | Implementation | User Benefits | Privacy Protection |
|---------------------|----------------|---------------|-------------------|
| **Educational record control** | Students maintain complete control over their educational data | Empowerment through data ownership | Personal data sovereignty |
| **Proportional data requests** | Institutions request only necessary information | Protection from excessive data collection | GDPR compliance enforcement |
| **Excessive collection prevention** | Systems actively prevent unnecessary data gathering | Automatic privacy protection | Proactive privacy safeguards |
| **Automated privacy protection** | Privacy protection becomes seamless and automatic | User-friendly privacy experience | Transparent privacy mechanisms |
| **Cross-border rights protection** | European privacy rights maintained across borders | Consistent privacy protection | Harmonised privacy standards |

#### Wallet enforcement capabilities:

| Capability | Function | User Experience | Technical Implementation |
|------------|----------|-----------------|-------------------------|
| **Disproportionate request detection** | Identify excessive information requests | Warning notifications to users | Automated policy analysis |
| **Data sharing warnings** | Alert users about potential over-sharing | Clear, understandable privacy notices | User-friendly privacy interfaces |
| **Unauthorised access blocking** | Prevent unauthorised information access | Automatic protection without user intervention | Technical access controls |
| **Personal data control maintenance** | Ensure user control over personal information | Intuitive data management interfaces | User-centric control mechanisms |

*Note: "Blocking" functionality is implemented at technical level while respecting sectorial requirements and individual rights.*

### <a id="_Toc184710047"></a>6.13 Supporting infrastructure

This infrastructure supports the entire credential ecosystem while maintaining security, privacy, and usability across European educational systems.

#### Supporting infrastructure requirements:

| Infrastructure Component | Purpose | Implementation Requirements | European Integration Benefits |
|--------------------------|---------|---------------------------|------------------------------|
| **Multi-domain and sector support** | Enable credentials across different educational domains | Flexible architecture supporting various educational sectors | Comprehensive European education coverage |
| **Distributed architecture** | Prevent single points of failure | Resilient, redundant system design | Reliable European-wide service |
| **Pan-European coverage** | Ensure system availability across all EU member states | Network infrastructure spanning all European countries | True European educational space |
| **Privacy-enhanced verification** | Maintain privacy during credential verification | Privacy-preserving cryptographic protocols | GDPR-compliant verification across borders |
| **Data protection compliance** | Ensure adherence to European data protection standards | Built-in privacy protection mechanisms | Consistent privacy protection |
| **Security audit mechanisms** | Enable comprehensive security monitoring | Automated security auditing and monitoring tools | Maintained security standards |
| **Verification record keeping** | Maintain audit trails while protecting privacy | Privacy-compliant logging and audit systems | Accountability with privacy protection |
| **Service discovery tools** | Enable automatic discovery of credential services | Distributed service discovery protocols | Seamless service integration |
| **Cross-country legal entity recognition** | Ensure mutual recognition of educational institutions | Legal framework for institutional recognition | Simplified cross-border institutional trust |

#### System architecture characteristics:

**Scalability**: Designed to handle millions of credentials and verifications across Europe
**Interoperability**: Compatible with existing national educational systems
**Sustainability**: Long-term operational model supporting continuous European educational evolution
**Resilience**: Fault-tolerant design ensuring continuous service availability