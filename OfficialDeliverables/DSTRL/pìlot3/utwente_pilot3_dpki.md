# DC4EU Deployment and Testing Scenarios Results Library (DTSRL) – Scenario: University of Twente - Decentralised PKI

## 1. Scenario Identification

- **Piloting agent name**: University of Twente (UTWENTE)
- **Scenario title**: Technical Education Credential Issuance with Decentralised PKI Trust Framework
- **Date of submission**: 11 July 2025
- **Point of contact (SPOC)**: Helenn Vanderzaag

---

## 2. Scenario Characterisation

- **User journeys implemented**:
  PID retrieval (completed), EducationalID issuance (completed), Educational achievement issuance (completed), Generic EAA verification (completed)
- **Target groups and end-user roles**:
  Engineering students, technical programme graduates, research staff, academic administrative personnel
- **Electronic Attestations of Attributes (EAAs) involved**:
  PID (Person Identification Data), EducationalID, Technical Education Achievement (EAAs: Engineering degrees, Research qualifications, Technical certificates)
- **Institutional systems/databases connected**:
  University of Twente authentic source databases (student records), technical programme registry, research credentials system
- **Technical components used**:
  - **Pilot option**: Pilot3-dPKI (Combined approach - Decentralised PKI component)
  - **Wallet(s)**: EUDI Wallet (EUDIW by IZERTIS)
  - **Issuer platform**: uSelf Issuer Agent (ATOS)
  - **Verifier platform**: uSelf Verifier (ATOS)
  - **PID Retrieval Service**: Dutch national PID provider via dPKI framework
- **Governance configuration**:
  - **Trust model**: Hybrid (X.509 PKI + DIDs + EBSI Trust Registries)
  - **Issuer DID**: `did:ebsi:zkZ45tZchyqA5NwQ5s9jPLN`
  - **Verifier DID**: `did:ebsi:zkZ45tZchyqA5NwQ5s9jPLN`
  - **dPKI DNS**: `lsput.utwente.nl`
  - **Registry references**: EBSI Trust Registry entries, Dutch Sectorial EAA Catalogue
- **Cryptographic Standards**:
  - **Algorithm**: EC (Elliptic Curve)
  - **Key Size**: 256 bits
  - **Security Level**: Strong (256-bit EC equivalent to 3072-bit RSA)
  - **Certificate Chain**: 3 certificate(s)
- **Monitoring and feedback mechanisms**:
  Weekly progress reports with structured KPIs, managed by SPOC Helenn Vanderzaag

---

## 3. Legal, Organisational and Operational Details

- **Regulatory context**:
  - GDPR compliance achieved
  - eIDAS2 alignment completed
  - Dutch national higher education regulations compliance
  - EBSI Trust Registry regulatory framework adherence
- **Risk management**:
  Risk of DID resolution failures (low likelihood/medium impact) mitigated via EBSI infrastructure redundancy; risk of EBSI Trust Registry downtime (low likelihood/high impact) mitigated via cached trust data
- **Credential lifecycle management**:
  - Revocation: Implemented via EBSI Trust Registry updates
  - Suspension: Implemented via DID document status modification
- **Infrastructure readiness**:
  ATOS/IZERTIS Dockerised solution deployed; integration endpoints with EBSI network; secure DID management and key storage systems
- **Training and onboarding**:
  Initial training covering DID principles, EBSI Trust Registry usage, EUDI Wallet integration, and decentralised trust verification protocols
- **Issue escalation**:
  Escalation via SPOC contact, clearly defined response times (SLA 48h), documented resolutions via ATOS/IZERTIS support channels
- **Success indicators and KPIs**:
  Successful DID registration and management, EBSI Trust Registry integration completed, comprehensive credential issuance and verification workflows, regulatory compliance achieved

---

## 4. Trust Model Onboarding Evidences

### **Decentralised PKI Trust Framework Implementation**

- **DID Registration and Management**:
  ```
  Issuer DID: did:ebsi:zkZ45tZchyqA5NwQ5s9jPLN
  Verifier DID: did:ebsi:zkZ45tZchyqA5NwQ5s9jPLN
  DID Method: EBSI
  Key Algorithm: EC (Elliptic Curve)
  Key Size: 256 bits
  Service Endpoint: https://lsput.utwente.nl
  ```

- **EBSI Trust Registry Integration**:
  ```
  Trust Registry Entry: University of Twente - Technical Education Authority
  Authorisation Scope: Engineering Education, Research Qualifications
  Accreditation Status: Verified
  Cross-Border Recognition: EU-wide validity
  ```

- **Governance Documentation**:
  Complete education/professional qualifications governance documentation provided by GovPart, DID-based trust discovery implementation, EBSI network participation agreements

- **Cryptographic Evidence**:
  ```
  Subject CN: lsput.utwente.nl
  Organization: University of Twente - dPKI
  Country: NL
  Algorithm: EC (Elliptic Curve)
  Key Size: 256 bits
  Security Level: Strong (256-bit EC equivalent to 3072-bit RSA)
  Certificate Chain: 3 certificate(s)
  ```

---

## 5. Implementation and Testing Progress

### **Decentralised PKI Infrastructure Deployment**

**DID and EBSI Integration** (Completed):
- ATOS/IZERTIS Dockerised solution successfully deployed
- DID registration in EBSI network completed and operational
- Trust Registry entries configured and validated
- Service endpoint configuration and DNS setup completed

**Integration Testing Results** (Completed):
- EUDI Wallet integration with dPKI infrastructure verified
- PID retrieval via decentralised trust framework operational
- Educational credential issuance through DID-based trust successful
- Cross-border verification via EBSI Trust Registry validated

**User Journey Validation** (Completed):
- PID retrieval: 100% success rate with DID-based authentication
- EducationalID issuance: Comprehensive testing with technical programmes
- Educational achievement credentials: Engineering and research qualifications validated
- Generic EAA verification: Multi-stakeholder verification scenarios completed

**Interoperability Testing** (Completed):
- Cross-PKI verification with Classical PKI implementation successful
- EBSI network connectivity and performance validated
- International trust registry interoperability confirmed

---

## 6. Testing Results and Observations

### **Decentralised PKI Performance Metrics**

**DID Operations**:
- DID resolution time: Average 1.8 seconds
- EBSI Trust Registry query time: Average 2.1 seconds
- Credential verification time: Average 2.5 seconds

**Integration Stability**:
- EUDI Wallet dPKI integration: 98.7% uptime
- ATOS/IZERTIS infrastructure availability: 99.5%
- EBSI network response time: Consistently under 3 seconds

**User Experience Assessment**:
- dPKI workflow completion rate: 91%
- User satisfaction with DID-based credential management: High
- Technical staff confidence with decentralised infrastructure: Excellent

**Cross-Border Verification**:
- Successful verification with other dPKI implementations across Europe
- EBSI Trust Registry international validation operational
- EU-wide credential portability demonstrated

**Hybrid Trust Model Benefits**:
- Seamless integration between Classical PKI and dPKI components
- Enhanced trust establishment through multiple verification paths
- Improved resilience through redundant trust mechanisms

---

## 7. Evidence Archive and References

### **Decentralised PKI Documentation Repository**

**Technical Evidence**:
- DID document specifications and key management protocols
- ATOS/IZERTIS integration technical documentation
- EBSI Trust Registry configuration and validation results
- Service endpoint security and performance test outcomes

**Compliance Documentation**:
- Dutch higher education regulatory compliance reports for dPKI
- GDPR compliance assessment for decentralised identity management
- eIDAS2 alignment documentation for DID-based trust

**Testing Archives**:
- dPKI integration test logs and performance metrics
- EUDI Wallet compatibility validation reports
- Cross-border EBSI verification test outcomes
- Hybrid trust model interoperability results

**Operational Procedures**:
- DID lifecycle management protocols
- EBSI Trust Registry monitoring and update procedures
- Decentralised PKI incident response documentation

---

## 8. Next Steps and Recommendations

### **Decentralised PKI Enhancement Roadmap**

**Short-term Objectives** (Q3 2025):
- Expand DID-based credential templates for additional qualification types
- Enhance EBSI Trust Registry integration for faster verification
- Implement advanced DID document management features

**Medium-term Development** (Q4 2025):
- Integration with additional EUDI Wallet implementations
- Enhanced cross-border decentralised trust establishment
- Advanced governance framework refinement for dPKI

**Strategic Considerations**:
- Evaluation of dPKI scalability for increased user volumes
- Assessment of blockchain infrastructure sustainability
- Long-term EBSI network participation strategy

**Recommendations for Other Institutions**:
- ATOS/IZERTIS Dockerised solution provides robust dPKI foundation
- Early EBSI Trust Registry registration streamlines implementation
- Investment in DID management training yields significant operational benefits
- Hybrid approach combining dPKI with Classical PKI maximises trust coverage

---

## 9. Summary of End-User Feedback

### **Decentralised PKI User Experience**

**Positive Feedback**:
- "DID-based credentials provide enhanced privacy and control"
- "EBSI Trust Registry offers transparent and verifiable trust establishment"
- "Decentralised approach reduces dependency on central authorities"
- "Cross-border credential verification works seamlessly"

**Areas for Enhancement**:
- Request for simplified DID management interfaces
- Suggestion for improved EBSI network status visibility
- Interest in enhanced privacy features for credential presentation

**Overall Satisfaction**: 4.1/5.0 with dPKI implementation

**User Confidence**: High trust levels in blockchain-based credential verification

**Adoption Rates**: 86% of target users successfully onboarded to dPKI system

**Comparison with Classical PKI**: Users appreciate having both trust options available

---

## 10. Summary of Piloting Agent Insights

### **Decentralised PKI Implementation Experience**

**Key Successes**:
- ATOS/IZERTIS Dockerised solution significantly simplified dPKI deployment
- DID-based trust model provides excellent international interoperability
- EBSI Trust Registry integration enables transparent trust establishment
- Hybrid approach with Classical PKI provides comprehensive trust coverage

**Technical Insights**:
- Decentralised PKI infrastructure scales effectively for university deployment
- DID resolution and EBSI queries perform reliably at operational scale
- Integration with Dutch national identity systems streamlined through dPKI framework
- Blockchain-based trust registries provide robust revocation mechanisms

**Organisational Learning**:
- DID governance frameworks require specialised technical expertise
- User education in decentralised identity concepts essential for adoption
- Clear service level agreements critical for dPKI operational stability
- Regular EBSI network participation reviews ensure continued compliance

**Strategic Value**:
- Decentralised PKI enables innovative trust establishment models
- International interoperability exceeds traditional PKI capabilities
- User privacy and control enhanced through DID-based credentials
- Combined with Classical PKI, provides comprehensive hybrid trust solution

**Hybrid Trust Model Insights**:
- Dual PKI approach provides optimal balance of familiarity and innovation
- Users appreciate having multiple trust verification options
- Cross-PKI interoperability demonstrates future-ready architecture
- Risk mitigation enhanced through redundant trust mechanisms

**Recommendations for DC4EU**:
- dPKI implementations should leverage established EBSI infrastructure
- Comprehensive DID training programmes essential for successful adoption
- Regular governance framework reviews ensure continued regulatory alignment
- Hybrid trust models provide optimal user experience and risk mitigation
- International collaboration through EBSI enhances credential portability