# DC4EU Deployment and Testing Scenarios Results Library (DTSRL) – Scenario: Saxion University of Applied Sciences - Decentralised PKI

## 1. Scenario Identification

- **Piloting agent name**: Saxion University of Applied Sciences (SAXION)
- **Scenario title**: Applied Sciences Credential Issuance with Decentralised PKI Trust Framework
- **Date of submission**: 11 July 2025
- **Point of contact (SPOC)**: Franco de Vitta

---

## 2. Scenario Characterisation

- **User journeys implemented**:
  PID retrieval (completed), EducationalID issuance (completed), Educational achievement issuance (completed), Generic EAA verification (completed)
- **Target groups and end-user roles**:
  Applied sciences students, professional programme graduates, industry collaboration partners, academic administrative staff
- **Electronic Attestations of Attributes (EAAs) involved**:
  PID (Person Identification Data), EducationalID, Applied Sciences Achievement (EAAs: Professional qualifications, Practical training certificates, Industry collaboration credentials)
- **Institutional systems/databases connected**:
  Saxion authentic source databases (student records), professional programmes registry, industry partnership credentials system
- **Technical components used**:
  - **Pilot option**: Pilot3-dPKI (Combined approach - Decentralised PKI component)
  - **Wallet(s)**: EUDI Wallet (EUDIW by IZERTIS)
  - **Issuer platform**: uSelf Issuer Agent (ATOS)
  - **Verifier platform**: uSelf Verifier (ATOS)
  - **PID Retrieval Service**: Dutch national PID provider via dPKI framework
- **Governance configuration**:
  - **Trust model**: Hybrid (X.509 PKI + DIDs + EBSI Trust Registries)
  - **Issuer DID**: `did:ebsi:zZ97WmbVmSr6UpU5jb5X8HK`
  - **Verifier DID**: `did:ebsi:zZ97WmbVmSr6UpU5jb5X8HK`
  - **dPKI DNS**: `lspsaxion.saxion.nl`
  - **Registry references**: EBSI Trust Registry entries, Dutch Professional Education Sectorial EAA Catalogue
- **Cryptographic Standards**:
  - **Algorithm**: EC (Elliptic Curve)
  - **Key Size**: 256 bits
  - **Security Level**: Strong (256-bit EC equivalent to 3072-bit RSA)
  - **Certificate Chain**: 3 certificate(s)
- **Monitoring and feedback mechanisms**:
  Weekly progress reports with structured KPIs, managed by SPOC Franco de Vitta

---

## 3. Legal, Organisational and Operational Details

- **Regulatory context**:
  - GDPR compliance achieved
  - eIDAS2 alignment completed
  - Dutch national applied sciences education regulations compliance
  - EBSI Trust Registry professional qualifications regulatory framework adherence
- **Risk management**:
  Risk of DID resolution failures for professional credentials (low likelihood/medium impact) mitigated via EBSI infrastructure redundancy; risk of industry partner EBSI compatibility (medium likelihood/low impact) mitigated via hybrid trust approach
- **Credential lifecycle management**:
  - Revocation: Implemented via EBSI Trust Registry updates for professional qualifications
  - Suspension: Implemented via DID document status modification
- **Infrastructure readiness**:
  ATOS/IZERTIS Dockerised solution deployed for applied sciences; integration endpoints with EBSI network; secure DID management for professional credentials
- **Training and onboarding**:
  Initial training covering DID principles for applied sciences, EBSI Trust Registry usage for professional qualifications, EUDI Wallet integration for industry contexts, and decentralised professional trust verification
- **Issue escalation**:
  Escalation via SPOC contact, clearly defined response times (SLA 48h), documented resolutions via ATOS/IZERTIS support channels for applied sciences
- **Success indicators and KPIs**:
  Successful DID registration for applied sciences authority, EBSI Trust Registry integration for professional qualifications, comprehensive applied sciences credential workflows, industry partner dPKI verification capability

---

## 4. Trust Model Onboarding Evidences

### **Decentralised PKI Trust Framework Implementation**

- **DID Registration and Management**:
  ```
  Issuer DID: did:ebsi:zZ97WmbVmSr6UpU5jb5X8HK
  Verifier DID: did:ebsi:zZ97WmbVmSr6UpU5jb5X8HK
  DID Method: EBSI
  Key Algorithm: EC (Elliptic Curve)
  Key Size: 256 bits
  Service Endpoint: https://lspsaxion.saxion.nl
  Professional Education Authority: Registered
  ```

- **EBSI Trust Registry Integration**:
  ```
  Trust Registry Entry: Saxion University of Applied Sciences - Professional Education Authority
  Authorisation Scope: Applied Sciences Education, Professional Qualifications, Industry Collaboration
  Accreditation Status: Verified for Professional Education
  Cross-Border Recognition: EU-wide professional validity
  Industry Partnership Status: Verified
  ```

- **Governance Documentation**:
  Complete education/professional qualifications governance documentation provided by GovPart for applied sciences, DID-based trust discovery implementation for professional credentials, EBSI network participation agreements for professional education

- **Cryptographic Evidence**:
  ```
  Subject CN: lspsaxion.saxion.nl
  Organization: Saxion University of Applied Sciences - dPKI
  Country: NL
  Algorithm: EC (Elliptic Curve)
  Key Size: 256 bits
  Security Level: Strong (256-bit EC equivalent to 3072-bit RSA)
  Certificate Chain: 3 certificate(s)
  Professional Education Designation: Applied Sciences Authority
  ```

---

## 5. Implementation and Testing Progress

### **Decentralised PKI Infrastructure Deployment**

**DID and EBSI Integration** (Completed):
- ATOS/IZERTIS Dockerised solution successfully deployed for applied sciences use cases
- DID registration in EBSI network completed for professional education authority
- Trust Registry entries configured for applied sciences and professional qualifications
- Service endpoint configuration and DNS setup completed for industry partnerships

**Integration Testing Results** (Completed):
- EUDI Wallet integration with dPKI infrastructure for applied sciences verified
- PID retrieval via decentralised trust framework for professional programmes operational
- Applied sciences credential issuance through DID-based trust successful
- Industry partner verification via EBSI Trust Registry validated

**Professional Qualification Validation** (Completed):
- Applied sciences qualification issuance: 100% success rate with DID-based authentication
- Professional training certificate validation: Comprehensive industry testing via dPKI
- Industry collaboration credentials: Multi-stakeholder verification through EBSI
- Cross-border professional recognition: International applied sciences validation via trust registry

**User Journey Validation** (Completed):
- PID retrieval: 100% success rate with DID-based authentication for professional contexts
- EducationalID issuance: Applied sciences programmes comprehensive testing
- Professional achievement credentials: Industry-relevant qualifications validated via dPKI
- Generic EAA verification: Professional and academic stakeholder scenarios through EBSI

**Interoperability Testing** (Completed):
- Cross-PKI verification with Classical PKI implementation for professional credentials
- EBSI network connectivity for applied sciences validated
- International professional trust registry interoperability confirmed
- Industry partner dPKI compatibility verified

---

## 6. Testing Results and Observations

### **Decentralised PKI Performance Metrics**

**DID Operations for Applied Sciences**:
- Professional DID resolution time: Average 1.9 seconds
- EBSI Trust Registry query for professional qualifications: Average 2.2 seconds
- Applied sciences credential verification time: Average 2.7 seconds

**Integration Stability**:
- EUDI Wallet dPKI integration for applied sciences: 98.5% uptime
- ATOS/IZERTIS infrastructure availability for professional education: 99.4%
- EBSI network response time for professional queries: Consistently under 3.2 seconds

**Applied Sciences Specific Performance**:
- Professional qualification dPKI workflow completion rate: 93%
- Industry partner DID verification success rate: 96%
- Cross-border professional recognition via EBSI: 89%

**User Experience Assessment**:
- dPKI workflow completion rate for applied sciences: 89%
- User satisfaction with DID-based professional credential management: High
- Industry partner confidence with decentralised verification: Very Good

**Cross-Border Professional Recognition**:
- Successful verification with international applied sciences institutions via EBSI
- Professional qualification DID validation operational across EU
- Industry collaboration credential portability demonstrated through trust registry

**Hybrid Trust Model Benefits for Applied Sciences**:
- Seamless integration between Classical PKI and dPKI for professional credentials
- Enhanced industry trust establishment through multiple verification paths
- Improved professional credential resilience through redundant trust mechanisms

---

## 7. Evidence Archive and References

### **Decentralised PKI Documentation Repository**

**Technical Evidence**:
- DID document specifications for applied sciences professional credentials
- ATOS/IZERTIS integration technical documentation for professional education
- EBSI Trust Registry configuration for applied sciences and validation results
- Professional qualification service endpoint security and performance test outcomes

**Compliance Documentation**:
- Dutch applied sciences education regulatory compliance reports for dPKI
- Professional qualifications authority alignment documentation for decentralised trust
- GDPR compliance assessment for decentralised professional identity management
- eIDAS2 alignment documentation for DID-based professional credential trust

**Testing Archives**:
- dPKI integration test logs for applied sciences use cases
- EUDI Wallet professional credential compatibility validation reports
- Cross-border EBSI professional verification test outcomes
- Industry partner dPKI interoperability results
- Hybrid trust model professional qualification testing results

**Operational Procedures**:
- Professional DID lifecycle management protocols for applied sciences
- EBSI Trust Registry monitoring for professional qualifications
- Applied sciences specific decentralised PKI incident response documentation

---

## 8. Next Steps and Recommendations

### **Decentralised PKI Enhancement Roadmap**

**Short-term Objectives** (Q3 2025):
- Expand DID-based credential templates for additional professional qualifications
- Enhance EBSI Trust Registry integration for faster applied sciences verification
- Implement advanced professional DID document management features

**Medium-term Development** (Q4 2025):
- Integration with additional professional EUDI Wallet implementations
- Enhanced cross-border decentralised trust for applied sciences recognition
- Advanced professional governance framework refinement for dPKI

**Applied Sciences Specific Enhancements**:
- Industry 4.0 DID-based credential development
- Enhanced professional training certificate verification via EBSI
- Advanced industry collaboration verification workflows through decentralised trust

**Strategic Considerations**:
- Evaluation of dPKI scalability for increased professional programme volumes
- Assessment of blockchain infrastructure sustainability for applied sciences
- Long-term EBSI network professional education participation strategy

**Recommendations for Applied Sciences Institutions**:
- ATOS/IZERTIS Dockerised solution provides robust dPKI foundation for professional education
- Early EBSI Trust Registry registration for professional qualifications streamlines implementation
- Investment in professional DID management training yields significant operational benefits
- Hybrid approach combining dPKI with Classical PKI maximises professional trust coverage
- Industry partnership engagement essential for successful dPKI adoption

---

## 9. Summary of End-User Feedback

### **Decentralised PKI User Experience for Applied Sciences**

**Positive Feedback**:
- "DID-based professional credentials provide enhanced industry privacy and control"
- "EBSI Trust Registry offers transparent professional qualification verification"
- "Decentralised approach reduces dependency on central professional authorities"
- "Cross-border applied sciences credential verification works seamlessly"

**Professional Programme Specific Feedback**:
- "Professional training credentials maintain privacy while enabling verification"
- "Industry collaboration benefits from decentralised trust establishment"
- "Applied sciences qualifications gain international recognition through EBSI"

**Areas for Enhancement**:
- Request for simplified professional DID management interfaces
- Suggestion for improved EBSI network status visibility for professional contexts
- Interest in enhanced privacy features for industry credential presentation

**Overall Satisfaction**: 4.0/5.0 with dPKI implementation for applied sciences

**Industry Partner Confidence**: High trust levels in blockchain-based professional credential verification

**Adoption Rates**: 84% of target users successfully onboarded to applied sciences dPKI system

**Comparison with Classical PKI**: Applied sciences users appreciate having both professional trust options available

---

## 10. Summary of Piloting Agent Insights

### **Decentralised PKI Implementation Experience for Applied Sciences**

**Key Successes**:
- ATOS/IZERTIS Dockerised solution significantly simplified dPKI deployment for applied sciences
- DID-based professional trust model provides excellent international industry interoperability
- EBSI Trust Registry integration enables transparent professional qualification trust establishment
- Hybrid approach with Classical PKI provides comprehensive professional trust coverage

**Applied Sciences Specific Insights**:
- Decentralised PKI infrastructure scales effectively for professional education deployment
- Professional DID resolution and EBSI queries perform reliably for applied sciences contexts
- Integration with Dutch professional education systems streamlined through dPKI framework
- Blockchain-based professional trust registries provide robust qualification revocation mechanisms

**Organisational Learning**:
- Professional DID governance frameworks require specialised applied sciences expertise
- Industry partner education in decentralised professional identity concepts essential
- Clear professional service level agreements critical for dPKI operational stability
- Regular EBSI network professional participation reviews ensure continued compliance

**Professional Education Strategic Value**:
- Decentralised PKI enables innovative professional trust establishment models
- International applied sciences interoperability exceeds traditional PKI capabilities
- Professional privacy and industry control enhanced through DID-based credentials
- Combined with Classical PKI, provides comprehensive professional hybrid trust solution

**Industry Partnership Benefits**:
- DID-based credentials facilitate innovative industry collaboration models
- Professional qualification blockchain verification enhances graduate employability
- Industry 4.0 readiness significantly improved through decentralised credential infrastructure
- Cross-border professional recognition enhanced through EBSI interoperability

**Hybrid Trust Model Insights for Applied Sciences**:
- Dual PKI approach provides optimal balance of professional familiarity and innovation
- Industry partners appreciate having multiple professional trust verification options
- Cross-PKI interoperability demonstrates future-ready applied sciences architecture
- Professional risk mitigation enhanced through redundant trust mechanisms

**Recommendations for DC4EU Applied Sciences Sector**:
- dPKI implementations should leverage established EBSI professional infrastructure
- Comprehensive professional DID training programmes essential for successful adoption
- Regular applied sciences governance framework reviews ensure continued regulatory alignment
- Hybrid professional trust models provide optimal industry experience and risk mitigation
- International professional collaboration through EBSI enhances credential portability
- Industry 4.0 integration significantly benefits from decentralised trust approaches