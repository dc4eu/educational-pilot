# eIDAS2 Supplementary Analysis for T1.6.4 Report: Potential Application of the EUDI Wallet on EWP Services

## Executive Summary

This supplementary document provides an enhanced analysis of the T1.6.4 report ["Potential application of the EUDI Wallet on EWP Services, Including Online Learning Agreement (OLA) and Erasmus+ App"](./DC4EU_Final%20report.pdf) in light of the final eIDAS2 Regulation (EU) 2024/1183. Rather than directly modifying the authors' original work, this document preserves their contributions whilst providing updated content that reflects the significant regulatory developments since the report's completion.

## Motivation for This Supplementary Approach

### Respect for Original Authorship
The T1.6.4 report represents valuable research conducted by the European University Foundation – Campus Europae, Aristotle University of Thessaloniki, and Eötvös Loránd University. Direct modification of their work would not appropriately acknowledge their intellectual contributions and analytical framework.

### Resource Constraints
The original authors lack the resources necessary to undertake a comprehensive revision incorporating the substantial changes introduced by eIDAS2. This supplementary approach allows for timely updates without placing additional burden on the original research team.

### Regulatory Evolution
The publication of eIDAS2 Regulation (EU) 2024/1183 occurred after the completion of the original report, introducing fundamental changes to the digital identity landscape that significantly impact the analysis and recommendations. These changes are too substantial to address through minor amendments.

### Preservation of Original Analysis
The original report's methodology and findings remain valid within their original context. This supplementary document builds upon rather than replaces the foundational analysis, ensuring continuity whilst providing enhanced perspectives.

---

## Section 1: Enhanced Trust Mechanisms Framework

### 1.1 Hybrid Trust Models under eIDAS2

The eIDAS2 Regulation introduces a paradigm shift in trust mechanisms that significantly enhances the potential applications of the EUDI Wallet within EWP services. This section provides a comprehensive analysis of how the dual trust model approach transforms the landscape described in the original report.

#### 1.1.1 Classical PKI Foundation

The existing EWP trust framework, as described in Section 1 of the original report, relies on traditional PKI mechanisms including:
- Client and server authentication between HEI nodes
- Request and response encryption
- Secure communication protocols
- Institutional-level access control

These mechanisms remain essential and continue to provide the foundational security layer for EWP operations. However, eIDAS2 now enables these traditional approaches to be complemented by advanced decentralised trust mechanisms.

#### 1.1.2 Decentralised PKI Enhancement through EBSI

The European Blockchain Services Infrastructure (EBSI), explicitly supported by eIDAS2, introduces a complementary decentralised PKI (dPKI) model that addresses specific limitations of classical PKI in educational governance:

**Granular Authorisation Management**: Unlike traditional PKI, which primarily establishes identity, dPKI enables the verification of specific authorisations. For example, a Spanish university can present verifiable credentials proving it is authorised by the Ministry of Science to issue degrees at EQF Level 7, information that can be validated in real-time by institutions across Europe.

**Dynamic Governance Layer**: The dPKI model supports the hierarchical and federated authorisation structures inherent in European education:
- Ministries authorising universities
- National QA agencies accrediting regional bodies
- NRENs acting as federated identity intermediaries
- Cross-border recognition authorities

**Verifiable Authorisation Credentials**: Root Trusted Accreditation Organisations (such as Ministries, EQAR, or GÉANT) issue Electronic Attestations of Attributes (EAAs) to authorised entities, including statements such as:
- "LicenceToActAtNationalLevel"
- "EQFLevel8Issuer"
- "MyAcademicIDIssuer"
- "QualityAssuranceAtProgrammeLevel"

#### 1.1.3 Implementation Within EWP Services

The hybrid trust model can be integrated into existing EWP workflows in several ways:

**Enhanced Institutional Verification**: When establishing Inter-institutional Agreements (IIA), institutions can present not only their legal identity (via traditional PKI) but also their specific authorisations to offer particular programmes or mobility opportunities (via dPKI).

**Automated Compliance Checking**: The nomination process can incorporate real-time verification of institutional authorisations, ensuring that only appropriately qualified institutions can nominate students for specific programmes.

**Cross-Border Trust Propagation**: Learning Agreements can benefit from automated verification of institutional credentials and authorisations, reducing administrative burden whilst enhancing security.

### 1.2 Issuer Classification and Requirements under eIDAS2

eIDAS2 establishes a clear taxonomy of credential issuers, each with specific regulatory requirements that directly impact EWP service implementation.

#### 1.2.1 Public Sector Bodies (Authentic Sources)

**Definition and Scope**: Public sector bodies responsible for authentic sources represent the highest level of trust within the eIDAS2 framework. In the education context, these include:
- Ministries of Education
- National qualification frameworks authorities
- Public universities (in their capacity as degree-awarding institutions)
- National student mobility agencies

**Regulatory Requirements**:
- Demonstration of legal establishment under Union or national law
- Notification to national supervisory bodies
- Inclusion in EU Commission trusted lists
- Acquisition of qualified electronic signatures or seals
- Implementation of reliability and trustworthiness measures equivalent to QTSPs

**Impact on EWP Services**: Public sector bodies can issue attestations with the strongest legal recognition, benefiting from cross-border equivalence principles. This significantly enhances the value of credentials within mobility processes.

#### 1.2.2 Qualified Trust Service Providers (QTSPs)

**Definition and Scope**: QTSPs provide the highest level of commercial trust services and must meet stringent regulatory requirements. Educational institutions seeking QTSP status must demonstrate:
- Compliance with Article 24 requirements of eIDAS2
- Appropriate financial and technical resources
- Qualified personnel and secure facilities
- Comprehensive risk management procedures

**Regulatory Process**:
- Formal application to national supervisory bodies
- Comprehensive assessment of technical and organisational measures
- Ongoing supervision and audit requirements
- Inclusion in trusted lists with QTSP designation

**Impact on EWP Services**: QTSP-issued credentials provide the highest level of assurance for critical educational processes, particularly suitable for final qualifications and professional certifications.

#### 1.2.3 Non-Qualified Trust Service Providers

**Definition and Scope**: The most accessible category, allowing educational institutions to begin issuing EAAs with minimal regulatory burden whilst still benefiting from EUDI Wallet integration.

**Regulatory Requirements**:
- Registration with national supervisory bodies
- Basic compliance with EUDI Wallet protocols
- Implementation of standard formats (ISO/IEC 18013-5:2021, W3C Verifiable Credentials)
- Relying party registration for wallet access

**Impact on EWP Services**: This category enables rapid adoption of EAA-based services whilst institutions develop capacity for higher trust levels.

---

## Section 2: Electronic Attestations of Attributes (EAAs) in EWP Context

### 2.1 Transformative Impact on Student Data Verification

The introduction of EAAs represents a fundamental shift in how student data is verified within EWP services, moving from document-based to credential-based verification systems.

#### 2.1.1 Enhanced Privacy Protection

EAAs implement privacy-by-design principles that significantly improve upon current EWP practices:

**Selective Disclosure**: Students can share only the specific attributes required for each interaction, rather than providing complete documents. For example, when applying for mobility, a student might share only their language proficiency level rather than the entire language certificate.

**Minimised Data Exposure**: EAAs reduce the circulation of sensitive personal information across EWP networks, limiting exposure to only verified, necessary attributes.

**Consent Management**: Students maintain granular control over their data sharing, with explicit consent required for each attribute disclosed.

#### 2.1.2 Automated Recognition Capabilities

EAAs enable automated recognition processes that dramatically reduce administrative burden:

**Real-Time Verification**: Receiving institutions can instantly verify student credentials without manual document processing or extended validation periods.

**Cross-Border Standardisation**: EAAs issued in one Member State are automatically recognisable across Europe, eliminating the need for country-specific validation processes.

**Quality Assurance Integration**: Credentials can embed information about accreditation status and quality frameworks, enabling automated compliance checking.

### 2.2 Enhanced Erasmus+ App Integration

Building upon Section 2.2.1 of the original report, EAAs significantly expand the potential applications within the Erasmus+ App ecosystem.

#### 2.2.1 Comprehensive Profile Automation

The original report identified limited potential for wallet integration in profile information. EAAs fundamentally change this assessment:

**Academic Credentials**: Students can populate their profiles using verified academic transcripts, eliminating manual data entry and reducing errors.

**Language Certifications**: Rather than uploading certificate images, students can present verifiable language credentials that automatically populate competency levels.

**Institutional Verification**: Student institutional affiliations can be verified through EAAs, ensuring accurate home institution identification.

#### 2.2.2 Streamlined Application Processes

EAAs transform the mobility application process described in the original report:

**Credential Verification**: The distinction between Type 1 (credential-suitable) and Type 2 (full content) documentation becomes less relevant as EAAs can embed rich metadata whilst maintaining verification capabilities.

**Automated Eligibility Checking**: Host institutions can automatically verify student eligibility based on EAA-embedded academic standing and programme requirements.

**Reduced Administrative Burden**: The elimination of document upload, storage, and manual verification processes significantly reduces processing time and administrative costs.

### 2.3 Learning Agreement Transformation

Whilst the original report concluded that Learning Agreements' mutable nature made them unsuitable for wallet integration, EAAs introduce new possibilities for enhancing the LA process.

#### 2.3.1 Supporting Credential Integration

Rather than storing the LA itself in the wallet, EAAs can provide verified supporting information:

**Academic Standing Verification**: Students can present verified academic records that automatically populate LA prerequisites and course eligibility information.

**Programme Compatibility**: EAAs can embed programme-specific information that enables automated compatibility checking between sending and receiving institutions.

**Quality Assurance Information**: Learning Agreements can reference EAA-embedded quality assurance information, providing transparent accreditation details.

#### 2.3.2 Enhanced Approval Workflows

EAAs can streamline the approval process without replacing the LA document:

**Automated Pre-Approval**: Initial LA approval can be automated based on EAA-verified student standing and programme compatibility.

**Reduced Verification Time**: Coordinators can focus on academic content rather than credential verification, as student eligibility is pre-verified through EAAs.

**Cross-Border Confidence**: The standardised verification provided by EAAs reduces the need for manual validation of student credentials across different educational systems.

---

## Section 3: Relying Party Obligations and Implementation Framework

### 3.1 Legal Entity Registration Requirements

eIDAS2 introduces comprehensive obligations for relying parties accessing EUDI Wallet credentials, with specific implications for EWP services.

#### 3.1.1 Registration Framework

**Mandatory Registration**: All legal entities seeking to access EUDI Wallet credentials must register with competent national authorities and obtain appropriate certificates.

**Entitlement Specification**: Registration must clearly specify the types of credentials and attributes the entity is entitled to access, aligned with legitimate business purposes.

**Ongoing Compliance**: Registered entities must maintain compliance with data protection regulations and demonstrate appropriate technical and organisational measures.

#### 3.1.2 Authentication and Identification

**Mutual Authentication**: EWP services must implement mutual authentication mechanisms when requesting credentials from students' EUDI Wallets.

**Identity Verification**: Relying parties must prove their identity and authorisation to access specific credential types before wallet interactions.

**Audit Trail Maintenance**: Comprehensive logging of all wallet interactions must be maintained for regulatory compliance and security monitoring.

### 3.2 Implementation Roadmap for EWP Services

#### 3.2.1 Phase 1: Foundation (Months 1-6)

**Regulatory Compliance Assessment**: EWP service providers must evaluate their current compliance status against eIDAS2 requirements and identify necessary upgrades.

**Technical Infrastructure Development**: Implementation of EUDI Wallet integration capabilities, including support for EAA verification and selective disclosure mechanisms.

**Pilot Programme Initiation**: Limited rollout with select institutions to test integration capabilities and user experience.

#### 3.2.2 Phase 2: Integration (Months 7-12)

**Full EAA Integration**: Complete integration of EAA verification capabilities within existing EWP workflows, including nominations, learning agreements, and transcript processing.

**Cross-Border Testing**: Extensive testing of cross-border functionality with partner institutions across multiple Member States.

**User Training and Support**: Comprehensive training programmes for institutional users and students on new capabilities and workflows.

#### 3.2.3 Phase 3: Optimisation (Months 13-18)

**Automated Recognition**: Implementation of automated recognition capabilities for standard mobility scenarios, reducing manual processing requirements.

**Advanced Trust Features**: Integration of advanced trust mechanisms, including verifiable authorisation chains and dynamic governance features.

**Performance Monitoring**: Continuous monitoring and optimisation of system performance, user satisfaction, and regulatory compliance.

---

## Section 4: Revised Conclusions and Recommendations

### 4.1 Fundamental Shift in Assessment

The analysis provided in this supplementary document demonstrates that eIDAS2 fundamentally transforms the conclusions of the original T1.6.4 report. Where the original analysis identified limited use cases for EUDI Wallet integration, the introduction of EAAs and enhanced trust mechanisms creates substantial opportunities for transformation.

### 4.2 Key Opportunities

**Erasmus+ App Enhancement**: EAAs enable comprehensive transformation of the student mobility application process, moving from document-based to credential-based verification with significant improvements in efficiency, security, and user experience.

**Learning Agreement Streamlining**: Whilst LAs themselves may not be suitable for wallet storage, EAAs can dramatically improve the supporting processes, enabling automated verification and reducing administrative burden.

**Cross-Border Trust**: The hybrid trust model combining classical PKI with EBSI-based decentralised trust enables unprecedented levels of cross-border confidence in educational credentials.

### 4.3 Implementation Recommendations

**Immediate Actions**: EWP service providers should begin assessment of eIDAS2 compliance requirements and initiate pilot programmes for EAA integration.

**Strategic Planning**: Development of comprehensive implementation roadmaps that align with institutional capacity and regulatory timelines.

**Stakeholder Engagement**: Active participation in European-level discussions on EAA standardisation and interoperability frameworks.

### 4.4 Future Research Directions

**User Experience Studies**: Comprehensive research on student and institutional user experiences with EAA-enhanced mobility processes.

**Interoperability Standards**: Development of sector-specific standards for educational EAAs that ensure seamless cross-border recognition.

**Impact Assessment**: Quantitative analysis of efficiency gains, cost reductions, and quality improvements resulting from EAA integration.

---

## Conclusion

This supplementary analysis demonstrates that eIDAS2 significantly expands the potential for EUDI Wallet integration within EWP services, moving from limited use cases to comprehensive transformation opportunities. The introduction of EAAs, enhanced trust mechanisms, and regulatory frameworks creates a foundation for more efficient, secure, and user-friendly student mobility processes.

The original T1.6.4 report provides valuable foundational analysis that remains relevant within its original context. This supplementary document builds upon that foundation to provide updated guidance that reflects the transformative potential of eIDAS2 implementation.

**Key Takeaway**: The question is no longer whether EUDI Wallet integration is feasible within EWP services, but rather how quickly and effectively these transformative capabilities can be implemented to benefit the European education community.

---

*This supplementary document is provided to enhance understanding of eIDAS2 implications for EWP services whilst preserving the integrity and value of the original T1.6.4 research contributions.*