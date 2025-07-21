# DC4EU Deployment and Testing Scenarios Results Library (DTSRL) – Scenario: COFAC - Lusófona University - Decentralised PKI

## 1. Scenario Identification

- **Piloting agent name**: COFAC - Lusófona University (ULUSOFONA)
- **Scenario title**: Private University Credential Issuance with Decentralised PKI Trust Framework
- **Date of submission**: 11 July 2025
- **Point of contact (SPOC)**: Paulo Ferreira

---

## 2. Scenario Characterisation

- **User journeys implemented**:
  PID retrieval (completed), EducationalID issuance (completed), Educational achievement issuance (completed), Generic EAA verification (completed)
- **Target groups and end-user roles**:
  Private university students, international programme graduates, diverse academic disciplines students, administrative staff
- **Electronic Attestations of Attributes (EAAs) involved**:
  PID (Person Identification Data), EducationalID, Private Education Achievement (EAAs: International qualifications, Diverse academic certificates, Private university credentials)
- **Institutional systems/databases connected**:
  Lusófona authentic source databases (student records), international programmes registry, diverse academic credentials system
- **Technical components used**:
  - **Pilot option**: Pilot3-dPKI (Combined approach - Decentralised PKI component)
  - **Wallet(s)**: EUDI Wallet (EUDIW by IZERTIS)
  - **Issuer platform**: uSelf Issuer Agent (ATOS)
  - **Verifier platform**: uSelf Verifier (ATOS)
  - **PID Retrieval Service**: Portuguese national PID provider via dPKI framework
- **Governance configuration**:
  - **Trust model**: Hybrid (X.509 PKI + DIDs + EBSI Trust Registries)
  - **Issuer DID**: `did:ebsi:zrmS9sGhR5J6vHu2gzMkN8t`
  - **Verifier DID**: `did:ebsi:zrmS9sGhR5J6vHu2gzMkN8t`
  - **dPKI DNS**: `lspulusofona.ulusofona.pt`
  - **Registry references**: EBSI Trust Registry entries, Portuguese Private Education Sectorial EAA Catalogue
- **Cryptographic Standards**:
  - **Algorithm**: EC (Elliptic Curve)
  - **Key Size**: 256 bits
  - **Security Level**: Strong (256-bit EC equivalent to 3072-bit RSA)
  - **Certificate Chain**: 3 certificate(s)
- **Monitoring and feedback mechanisms**:
  Weekly progress reports with structured KPIs, managed by SPOC Paulo Ferreira

---

## 3. Legal, Organisational and Operational Details

- **Regulatory context**:
  - GDPR compliance achieved
  - eIDAS2 alignment completed
  - Portuguese national private higher education regulations compliance
  - EBSI Trust Registry international education regulatory framework adherence
- **Risk management**:
  Risk of DID resolution failures for international credentials (low likelihood/medium impact) mitigated via EBSI infrastructure redundancy; risk of cross-border EBSI compatibility (medium likelihood/low impact) mitigated via hybrid trust approach
- **Credential lifecycle management**:
  - Revocation: Implemented via EBSI Trust Registry updates for international qualifications
  - Suspension: Implemented via DID document status modification
- **Infrastructure readiness**:
  ATOS/IZERTIS Dockerised solution deployed for private education; integration endpoints with EBSI network; secure DID management for international credentials
- **Training and onboarding**:
  Initial training covering DID principles for private education, EBSI Trust Registry usage for international qualifications, EUDI Wallet integration for cross-border contexts, and decentralised international trust verification
- **Issue escalation**:
  Escalation via SPOC contact, clearly defined response times (SLA 48h), documented resolutions via ATOS/IZERTIS support channels for private education
- **Success indicators and KPIs**:
  Successful DID registration for private education authority, EBSI Trust Registry integration for international qualifications, comprehensive private university credential workflows, cross-border dPKI verification capability

---

## 4. Trust Model Onboarding Evidences

### **Decentralised PKI Trust Framework Implementation**

- **DID Registration and Management**:
  ```
  Issuer DID: did:ebsi:zrmS9sGhR5J6vHu2gzMkN8t
  Verifier DID: did:ebsi:zrmS9sGhR5J6vHu2gzMkN8t
  DID Method: EBSI
  Key Algorithm: EC (Elliptic Curve)
  Key Size: 256 bits
  Service Endpoint: https://lspulusofona.ulusofona.pt
  Private Education Authority: Registered
  International Recognition: Verified
  ```

- **EBSI Trust Registry Integration**:
  ```
  Trust Registry Entry: COFAC - Lusófona University - Private Education Authority
  Authorisation Scope: Private Higher Education, International Qualifications, Cross-Border Academic Credentials
  Accreditation Status: Verified for International Private Education
  Cross-Border Recognition: EU-wide and Lusophone academic validity
  International Partnership Status: Verified
  ```

- **Governance Documentation**:
  Complete education/professional qualifications governance documentation provided by GovPart for private education, DID-based trust discovery implementation for international credentials, EBSI network participation agreements for private international education

- **Cryptographic Evidence**:
  ```
  Subject CN: lspulusofona.ulusofona.pt
  Organization: COFAC - Lusófona University - dPKI
  Country: PT
  Algorithm: EC (Elliptic Curve)
  Key Size: 256 bits
  Security Level: Strong (256-bit EC equivalent to 3072-bit RSA)
  Certificate Chain: 3 certificate(s)
  Private Education Designation: International Academic Authority
  ```

---

## 5. Implementation and Testing Progress

### **Decentralised PKI Infrastructure Deployment**

**DID and EBSI Integration** (Completed):
- ATOS/IZERTIS Dockerised solution successfully deployed for private university use cases
- DID registration in EBSI network completed for private international education authority
- Trust Registry entries configured for private education and international qualifications
- Service endpoint configuration and DNS setup completed for cross-border partnerships

**Integration Testing Results** (Completed):
- EUDI Wallet integration with dPKI infrastructure for private education verified
- PID retrieval via decentralised trust framework for international programmes operational
- Private university credential issuance through DID-based trust successful
- Cross-border verification via EBSI Trust Registry validated

**International Qualification Validation** (Completed):
- Private university qualification issuance: 100% success rate with DID-based authentication
- International programme certificate validation: Comprehensive cross-border testing via dPKI
- Diverse academic credentials: Multi-disciplinary verification through EBSI
- Cross-border academic recognition: International private education validation via trust registry

**User Journey Validation** (Completed):
- PID retrieval: 100% success rate with DID-based authentication for Portuguese and international contexts
- EducationalID issuance: Private university programmes comprehensive testing
- International achievement credentials: Cross-border qualifications validated via dPKI
- Generic EAA verification: International and domestic stakeholder scenarios through EBSI

**Interoperability Testing** (Completed):
- Cross-PKI verification with Classical PKI implementation for international credentials
- EBSI network connectivity for private education validated
- International academic trust registry interoperability confirmed
- Cross-border partner dPKI compatibility verified

---

## 6. Testing Results and Observations

### **Decentralised PKI Performance Metrics**

**DID Operations for Private Education**:
- International DID resolution time: Average 2.1 seconds
- EBSI Trust Registry query for international qualifications: Average 2.4 seconds
- Private university credential verification time: Average 2.9 seconds

**Integration Stability**:
- EUDI Wallet dPKI integration for private education: 98.3% uptime
- ATOS/IZERTIS infrastructure availability for international education: 99.2%
- EBSI network response time for international queries: Consistently under 3.5 seconds

**Private Education Specific Performance**:
- International qualification dPKI workflow completion rate: 91%
- Cross-border DID verification success rate: 94%
- International academic recognition via EBSI: 87%

**User Experience Assessment**:
- dPKI workflow completion rate for private education: 87%
- User satisfaction with DID-based international credential management: High
- Cross-border partner confidence with decentralised verification: Very Good

**Cross-Border Academic Recognition**:
- Successful verification with international private universities via EBSI
- International qualification DID validation operational across EU and Lusophone countries
- Cross-border academic credential portability demonstrated through trust registry

**Hybrid Trust Model Benefits for Private Education**:
- Seamless integration between Classical PKI and dPKI for international credentials
- Enhanced cross-border trust establishment through multiple verification paths
- Improved international credential resilience through redundant trust mechanisms

---

## 7. Evidence Archive and References

### **Decentralised PKI Documentation Repository**

**Technical Evidence**:
- DID document specifications for private university international credentials
- ATOS/IZERTIS integration technical documentation for private international education
- EBSI Trust Registry configuration for private education and validation results
- International qualification service endpoint security and performance test outcomes

**Compliance Documentation**:
- Portuguese private higher education regulatory compliance reports for dPKI
- International education authority alignment documentation for decentralised trust
- GDPR compliance assessment for decentralised international identity management
- eIDAS2 alignment documentation for DID-based international credential trust

**Testing Archives**:
- dPKI integration test logs for private university use cases
- EUDI Wallet international credential compatibility validation reports
- Cross-border EBSI academic verification test outcomes
- International partner dPKI interoperability results
- Hybrid trust model international qualification testing results

**Operational Procedures**:
- International DID lifecycle management protocols for private education
- EBSI Trust Registry monitoring for international qualifications
- Private education specific decentralised PKI incident response documentation

---

## 8. Next Steps and Recommendations

### **Decentralised PKI Enhancement Roadmap**

**Short-term Objectives** (Q3 2025):
- Expand DID-based credential templates for additional international qualifications
- Enhance EBSI Trust Registry integration for faster private education verification
- Implement advanced international DID document management features

**Medium-term Development** (Q4 2025):
- Integration with additional international EUDI Wallet implementations
- Enhanced cross-border decentralised trust for private education recognition
- Advanced international governance framework refinement for dPKI

**Private Education Specific Enhancements**:
- Lusophone academic DID-based credential development
- Enhanced international programme certificate verification via EBSI
- Advanced cross-border academic verification workflows through decentralised trust

**Strategic Considerations**:
- Evaluation of dPKI scalability for increased international programme volumes
- Assessment of blockchain infrastructure sustainability for private education
- Long-term EBSI network international education participation strategy

**Recommendations for Private Education Institutions**:
- ATOS/IZERTIS Dockerised solution provides robust dPKI foundation for international private education
- Early EBSI Trust Registry registration for international qualifications streamlines implementation
- Investment in international DID management training yields significant operational benefits
- Hybrid approach combining dPKI with Classical PKI maximises international trust coverage
- Cross-border partnership engagement essential for successful dPKI adoption

---

## 9. Summary of End-User Feedback

### **Decentralised PKI User Experience for Private Education**

**Positive Feedback**:
- "DID-based international credentials provide enhanced cross-border privacy and control"
- "EBSI Trust Registry offers transparent international qualification verification"
- "Decentralised approach reduces dependency on central international authorities"
- "Cross-border private education credential verification works seamlessly"

**Private Education Specific Feedback**:
- "International programme credentials maintain privacy while enabling global verification"
- "Cross-border academic collaboration benefits from decentralised trust establishment"
- "Private university qualifications gain international recognition through EBSI"

**Areas for Enhancement**:
- Request for simplified international DID management interfaces
- Suggestion for improved EBSI network status visibility for international contexts
- Interest in enhanced privacy features for cross-border credential presentation

**Overall Satisfaction**: 3.9/5.0 with dPKI implementation for private education

**International Partner Confidence**: High trust levels in blockchain-based international credential verification

**Adoption Rates**: 82% of target users successfully onboarded to private education dPKI system

**Comparison with Classical PKI**: Private education users appreciate having both international trust options available

---

## 10. Summary of Piloting Agent Insights

### **Decentralised PKI Implementation Experience for Private Education**

**Key Successes**:
- ATOS/IZERTIS Dockerised solution significantly simplified dPKI deployment for private education
- DID-based international trust model provides excellent cross-border academic interoperability
- EBSI Trust Registry integration enables transparent international qualification trust establishment
- Hybrid approach with Classical PKI provides comprehensive international trust coverage

**Private Education Specific Insights**:
- Decentralised PKI infrastructure scales effectively for international private university deployment
- International DID resolution and EBSI queries perform reliably for cross-border contexts
- Integration with Portuguese private education systems streamlined through dPKI framework
- Blockchain-based international trust registries provide robust qualification revocation mechanisms

**Organisational Learning**:
- International DID governance frameworks require specialised private education expertise
- Cross-border partner education in decentralised international identity concepts essential
- Clear international service level agreements critical for dPKI operational stability
- Regular EBSI network international participation reviews ensure continued compliance

**International Education Strategic Value**:
- Decentralised PKI enables innovative international trust establishment models
- Cross-border private education interoperability exceeds traditional PKI capabilities
- International privacy and academic control enhanced through DID-based credentials
- Combined with Classical PKI, provides comprehensive international hybrid trust solution

**Cross-Border Partnership Benefits**:
- DID-based credentials facilitate innovative international academic collaboration models
- International qualification blockchain verification enhances graduate global mobility
- Cross-border private education recognition significantly improved through decentralised credential infrastructure
- International academic partnership enhanced through EBSI interoperability

**Hybrid Trust Model Insights for Private Education**:
- Dual PKI approach provides optimal balance of international familiarity and innovation
- Cross-border partners appreciate having multiple international trust verification options
- Cross-PKI interoperability demonstrates future-ready international education architecture
- International risk mitigation enhanced through redundant trust mechanisms

**Recommendations for DC4EU Private Education Sector**:
- dPKI implementations should leverage established EBSI international infrastructure