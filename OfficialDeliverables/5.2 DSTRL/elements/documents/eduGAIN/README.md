# eduGAIN and Identity Federations: Ensuring Continued Relevance in the eIDAS2 Era

## Executive Summary

The European research and education identity landscape stands at a pivotal moment. The eduGAIN inter-federation, managed by GÉANT and comprising national research and education federations operated by NRENs, has provided secure, seamless authentication for over 50 million users across more than 10,000 institutions. However, the emergence of eIDAS2 and the European Digital Identity Wallet (EUDIW) presents both unprecedented challenges and remarkable opportunities for the continued relevance of federated identity systems.

This chapter examines the critical inflection point facing eduGAIN and national education federations, identifying key challenges whilst highlighting the transformative potential demonstrated through the DC4EU project. Rather than viewing eIDAS2 as a threat to existing federation models, we present a constructive analysis of how these systems can evolve, adapt, and ultimately thrive within the new European digital identity ecosystem.

## 1. Understanding the Current Landscape and Paradigm Shift

### 1.1 The eduGAIN Foundation: Delegated Authentication Model

eduGAIN has established itself as a cornerstone of European research and education infrastructure, facilitating secure cross-border access to online resources through a hierarchical federation model. The system operates on established SAML protocols, connecting national federations managed by NRENs with a robust trust framework built on institutional agreements and technical standards.

The federation's success stems from its community-driven approach, respecting institutional autonomy whilst enabling seamless collaboration across borders. Universities, research institutions, and education providers participate through their national federations, creating a web of trusted relationships that has underpinned European research collaboration for over a decade.

**Traditional Delegated Authentication Model:**
eduGAIN operates on the principle of delegated authentication, where:
- Users authenticate with their home institution or Identity Provider (IdP)
- The IdP validates credentials in real-time and issues assertions (SAML tokens or OpenID Connect tokens)
- Service Providers (SPs) delegate the responsibility for verifying credentials to the IdP
- This creates a "phone home" pattern where the IdP is actively involved in every authentication transaction
- User credentials never pass through the SP, but every access creates logs and potential tracking

### 1.2 The eIDAS2 Paradigm Shift: From Delegation to User-Centric Credentials

The eIDAS2 Regulation introduces a fundamentally different approach that **breaks from the traditional delegated authentication model** in favour of user-centric verifiable credentials. This represents not merely an evolution, but a transformative shift in how European digital identity operates.

**The New User-Centric Model:**
- **Direct User Control**: Identity attributes and credentials are held directly in the user's EUDI Wallet
- **Offline Verification**: Credentials can be verified without contacting the issuer, using cryptographic proofs
- **Portable Credentials**: Users present verifiable credentials directly to verifiers, eliminating real-time IdP dependency
- **Privacy by Design**: No systematic "phone home" to issuers, preventing usage tracking and enhancing privacy
- **Self-Sovereign Elements**: Users control when, how, and to whom they present their credentials

**Key Distinction - Foundational vs Non-Foundational Identity:**
The regulation's focus on "foundational identity" through Person Identification Data (PID) contrasts with eduGAIN's management of "non-foundational identity" attributes. Under eIDAS2, such attributes become Electronic Attestations of Attributes (EAAs), subject to specific trust services requirements and regulatory oversight, but crucially, they become portable and independently verifiable.

## 2. Critical Challenges and Risks

### 2.1 The Fundamental Paradigm Shift Challenge

The most significant challenge facing eduGAIN is not merely technical interoperability, but a fundamental shift in digital identity paradigm. The traditional delegated authentication model, where users "phone home" to their IdP for every authentication, becomes incompatible with the EUDI Wallet's design principles.

**Core Design Conflict:**
The EUDI Wallet is designed as an active trust agent, not a proxy for delegated authentication. Any implementation that simply relays authentication requests to issuers in real-time would conflict with eIDAS2 requirements:

- **Article 6a Compliance**: The Wallet must enable secure storage and presentation of credentials without issuer involvement
- **Privacy Requirements**: Recital 29 demands that users can prove identity without systematically informing issuers
- **Offline Verification**: The Architecture Reference Framework mandates offline credential verification capability
- **User Sovereignty**: Users must control credential presentation, not delegate to real-time IdP validation

**Risk Assessment:**
- **High Impact**: A proxy-based approach would render the EUDI Wallet non-compliant with eIDAS2
- **Medium Likelihood**: Without understanding the paradigm shift, institutions may attempt proxy solutions
- **Mitigation Strategy**: Embrace the new model through verifiable credentials and offline verification capabilities

### 2.2 Technical Interoperability and Protocol Evolution

Beyond the paradigm shift, eduGAIN faces substantial technical challenges in protocol evolution. Current federation infrastructure relies on SAML-based protocols and established trust frameworks, whilst eIDAS2 introduces new standards including OpenID4VP, ISO/IEC 18013-5, and W3C Verifiable Credentials.

**Technical Transformation Required:**
- **Protocol Migration**: From SAML assertions to W3C Verifiable Credentials
- **Trust Model Evolution**: From federation metadata to cryptographic trust anchors
- **Verification Paradigm**: From real-time IdP queries to offline cryptographic verification
- **Credential Lifecycle**: From session-based access to persistent, portable credentials

**Opportunity Framework:**
This challenge represents an opportunity to enhance the system's capabilities:
- **Enhanced Privacy**: Elimination of usage tracking through offline verification
- **Improved Resilience**: No single points of failure through distributed trust
- **Cross-Sector Interoperability**: Credentials usable beyond educational federations
- **Legal Recognition**: eIDAS2 compliance provides regulatory backing

### 2.2 Regulatory Compliance Burden

Perhaps the most significant challenge emerges from the regulatory requirements imposed on institutions operating as "Authentic Sources" under eIDAS2. Universities and research institutions that currently function as Identity Providers (IdPs) face the prospect of meeting "qualified trust service provider" (QTSP) equivalent standards when issuing authoritative educational attributes.

**Critical Implications:**
- **Increased Compliance Costs**: Substantial investments in cybersecurity infrastructure, audit processes, and compliance monitoring
- **Institutional Capacity Constraints**: Many institutions lack the resources to meet QTSP-equivalent requirements
- **Differentiated Service Levels**: Potential creation of "tiered" federation services based on compliance capabilities

### 2.3 Governance Model Tensions

The shift from agreement-based to legislatively mandated trust frameworks creates fundamental tensions. eduGAIN's success has been built on flexible, community-driven governance that respects institutional autonomy. eIDAS2's regulatory approach demands standardised compliance across all participants, potentially undermining the federated model's core principles.

**Governance Challenges:**
- **Autonomy vs. Standardisation**: Balancing institutional independence with regulatory compliance
- **National vs. European Priorities**: Reconciling national education policies with European digital identity requirements
- **Trust Framework Evolution**: Adapting community-based trust to regulatory mandates

### 2.4 Scalability and Resource Constraints

The federation model faces scalability challenges when confronted with eIDAS2's ambition to serve all European citizens. Current federation infrastructure, designed for the research and education community, must adapt to potentially serve broader populations whilst maintaining security and performance standards.

**Resource Implications:**
- **Technical Infrastructure**: Substantial upgrades required for eIDAS2 compliance
- **Human Resources**: Specialised expertise needed for hybrid trust model implementation
- **Financial Sustainability**: Uncertain funding models for expanded scope operations

## 3. Strategic Opportunities and Pathways Forward

### 3.1 The DC4EU Blueprint: Embracing the New Paradigm

The Digital Credentials for Europe (DC4EU) project provides a compelling blueprint for how eduGAIN and national federations can not only survive but thrive in the eIDAS2 era. Crucially, DC4EU demonstrates that the paradigm shift from delegated authentication to user-centric verifiable credentials creates significant opportunities rather than merely challenges.

**Key DC4EU Innovations:**
- **Disintermediated Verification**: EBSI enables credentials to be verified offline without "phoning home" to issuers
- **User-Centric Control**: Citizens hold verifiable credentials in their EUDI Wallet, controlling when and how they're presented
- **Privacy by Design**: No systematic issuer notification when credentials are used, enhancing privacy protection
- **Cross-Border Portability**: Credentials work across sectors and borders without federation agreements
- **Cryptographic Trust**: Verification based on cryptographic proofs rather than real-time issuer queries

**Paradigm Alignment Benefits:**
DC4EU's approach aligns perfectly with eIDAS2 requirements:
- **Offline Verification Capability**: Credentials can be verified without issuer availability
- **Unlinkability**: No central logging of credential usage, protecting user privacy
- **User Sovereignty**: Users control credential presentation without delegation to IdPs
- **Legal Recognition**: Automatic evidentiary value across Europe through eIDAS2 compliance

### 3.2 EBSI's Strategic Advantages: Beyond Traditional Federation Limitations

The European Blockchain Services Infrastructure (EBSI) addresses fundamental limitations of traditional federation models whilst providing enhanced capabilities for the new paradigm:

**Addressing Federation Constraints:**
- **Eliminates "Phone Home" Dependency**: EBSI credentials contain cryptographic proofs for offline validation
- **Reduces Single Points of Failure**: Distributed ledger architecture removes central metadata dependencies
- **Enables Universal Verification**: Any entity can verify credentials without joining specific federations
- **Provides Legal Recognition**: eIDAS2 compliance grants automatic evidentiary value across Europe

**Enhanced Capabilities:**
- **Transparent Governance**: Public, auditable trust anchors and policies published on the ledger
- **Scalable Architecture**: Designed for millions of credentials with decentralised verification
- **Cross-Sector Interoperability**: Works across education, employment, public administration, and healthcare
- **Privacy Protection**: Selective disclosure and minimal data sharing without usage tracking

**Institutional Autonomy Enhancement:**
Contrary to perceptions of centralised control, EBSI actually enhances institutional autonomy:
- **Independent Credential Definition**: Institutions can define their own schemas and issuance policies
- **Transparent Publication**: All policies and trust anchors are publicly auditable
- **Flexible Assurance Levels**: Support for all levels of assurance from low to high eIDAS levels
- **Innovation Enablement**: Open APIs and testing environments support experimentation

### 3.3 Strategic Reframing: From Threat to Opportunity

The paradigm shift from delegated authentication to user-centric verifiable credentials should be viewed not as a threat to eduGAIN, but as a strategic opportunity to enhance its capabilities and expand its relevance:

**Enhanced User Experience:**
- **Seamless Cross-Border Access**: Credentials work automatically across European institutions
- **Reduced Friction**: No need to establish federation agreements for each new service
- **Privacy Enhancement**: Users control their data without creating usage logs
- **Offline Capability**: Credentials work even when issuers are unavailable

**Institutional Benefits:**
- **Reduced Operational Overhead**: Less maintenance of federation metadata and agreements
- **Enhanced Security**: Cryptographic verification provides stronger assurance than real-time queries
- **Broader Recognition**: eIDAS2 compliance provides legal backing beyond education sector
- **Innovation Potential**: New credential types and use cases become possible

**Federation Evolution Opportunities:**
- **Hybrid Service Model**: Combine traditional SSO for legacy services with verifiable credentials for new use cases
- **Enhanced Trust Services**: Leverage EBSI trust anchors for improved key management
- **Cross-Sector Integration**: Enable educational credentials to work in employment and public services
- **Privacy-First Design**: Align with European data protection principles and user expectations

### 3.4 Authentic Source Differentiation

Rather than viewing "Authentic Source" requirements as a burden, forward-thinking institutions can leverage this designation for competitive advantage. Institutions that achieve eIDAS2 compliance for critical educational attributes gain enhanced credibility and broader European recognition.

**Strategic Advantages:**
- **Market Differentiation**: Enhanced institutional reputation through regulatory compliance
- **Broader Service Reach**: Ability to serve public sector and private sector relying parties
- **Future-Proofing**: Preparation for evolving European digital identity requirements

## 4. DC4EU Implementation Insights

### 4.1 Practical Implementation Models

DC4EU has successfully implemented multiple scenarios demonstrating how educational institutions can operate within the eIDAS2 framework:

**Scenario 1: Closed Ecosystem**
- Internal credential issuance for institutional purposes
- Minimal eIDAS2 compliance requirements, no EUDIW interaction
- Suitable for basic educational identity needs

**Scenario 2: Non-Qualified TSP Integration**
- Partnership with non-qualified trust service providers
- Enhanced trust through EBSI anchoring
- Optimal for most educational use cases

**Scenario 3: Public Sector Body Operation**
- Direct public sector body credential issuance
- Full eIDAS2 compliance requirements
- Suitable for authoritative educational credentials

**Scenario 4: Qualified TSP Partnership**
- Collaboration with qualified trust service providers
- Maximum trust and legal recognition
- Appropriate for high-value credentials

### 4.2 Technical Architecture Insights

The DC4EU technical implementation reveals practical approaches to hybrid trust models:

**Hybrid PKI/DID Architecture:**
- Traditional PKI for established trust relationships
- EBSI DIDs for enhanced authorisation verification
- W3C Verifiable Credentials for standardised credential formats
- European Learning Model (ELM) for educational data interoperability

**Integration Capabilities:**
- Seamless wallet interoperability with EUDIW
- Cross-border verification through EBSI trust registries
- Automated credential lifecycle management
- Privacy-preserving selective disclosure

### 4.3 Governance Framework Application

DC4EU's governance model demonstrates how educational institutions can maintain autonomy whilst achieving eIDAS2 compliance:

**Authorisation Chain Example:**
```
Ministry of Education (RootTAO)
  ↓ [Issues EAA - Authentic Source Authority]
University (Authentic Source + Issuer)
  ↓ [Issues Educational Credentials]
Student (Credential Holder)
  ↓ [Presents Credentials]
European Institution (Relying Party)
```

This structure preserves institutional independence whilst ensuring regulatory compliance and European recognition.

## 5. Risk Mitigation Strategies

### 5.1 Embracing the Paradigm Shift: Phased Transition Strategy

Rather than wholesale system replacement, successful adaptation requires a carefully orchestrated transition that embraces the new paradigm whilst maintaining continuity of service:

**Phase 1: Understanding and Preparation (Months 1-6)**
- **Paradigm Education**: Train technical and governance teams on the shift from delegated authentication to verifiable credentials
- **Use Case Identification**: Identify high-value scenarios where offline verification provides immediate benefits
- **Technical Assessment**: Evaluate current infrastructure's readiness for W3C Verifiable Credentials and EBSI integration
- **Compliance Planning**: Map eIDAS2 requirements to institutional capabilities and identify gaps

**Phase 2: Hybrid Implementation (Months 7-18)**
- **Parallel Service Deployment**: Implement verifiable credential services alongside existing SAML-based federation
- **EBSI Integration**: Connect to EBSI infrastructure for trust anchor management and credential verification
- **User Experience Design**: Create seamless user journeys that leverage both authentication models
- **Privacy Enhancement**: Implement selective disclosure and offline verification capabilities

**Phase 3: Service Evolution (Months 19-36)**
- **Credential Migration**: Gradually migrate high-value use cases from delegated authentication to verifiable credentials
- **Cross-Sector Integration**: Enable educational credentials to work in employment and public sector contexts
- **Advanced Features**: Implement sophisticated credential lifecycle management and privacy features
- **Legal Recognition**: Achieve full eIDAS2 compliance for regulated credential types

**Phase 4: Paradigm Completion (Months 37-48)**
- **Full User-Centric Operation**: Complete transition to user-controlled credential presentation
- **Legacy Support**: Maintain minimal delegated authentication for legacy systems
- **Innovation Acceleration**: Leverage the new paradigm for innovative educational credential use cases
- **European Integration**: Full participation in European digital identity ecosystem

### 5.2 Financial Sustainability Models

The transition to eIDAS2 compliance requires sustainable funding approaches:

**Funding Strategies:**
- **European Programme Participation**: Leveraging Horizon Europe and Digital Europe funding
- **National Government Support**: Securing dedicated funding for digital identity infrastructure
- **Institutional Investment**: Collaborative funding models across federation members
- **Value-Added Services**: Revenue generation through enhanced credential services

### 5.3 Capacity Building Initiatives

Successful implementation requires comprehensive capacity building:

**Training Programmes:**
- Technical staff development in eIDAS2 technologies
- Governance and compliance training for administrators
- User experience design for wallet integration
- Security and privacy management

**Knowledge Sharing:**
- Cross-institutional collaboration networks
- Best practice documentation and dissemination
- Regular technical workshops and conferences
- Peer learning and support groups

## 6. Future Opportunities and Benefits

### 6.1 Transformative Benefits of the New Paradigm

The shift to user-centric verifiable credentials creates unprecedented opportunities for European research and education:

**Enhanced User Experience:**
- **Seamless Mobility**: Students and researchers can present credentials instantly at any European institution
- **Privacy Protection**: No usage tracking or "phone home" requirements preserve user privacy
- **Offline Capability**: Credentials work even when original issuers are unavailable
- **Selective Disclosure**: Users can choose exactly what information to share for each interaction

**Institutional Advantages:**
- **Reduced Operational Costs**: Less maintenance of federation metadata and real-time IdP services
- **Enhanced Security**: Cryptographic verification provides stronger assurance than session-based authentication
- **Broader Recognition**: eIDAS2 compliance enables credentials to work across all European sectors
- **Innovation Potential**: New types of micro-credentials, competency attestations, and research collaboration credentials

**Systemic Improvements:**
- **Resilience**: No single points of failure through distributed verification
- **Scalability**: System can handle millions of credentials without performance degradation
- **Interoperability**: Universal verification standards enable cross-sector credential use
- **Legal Certainty**: Regulatory framework provides clear legal status for digital credentials

**Research and Education Specific Benefits:**
- **Automatic Qualification Recognition**: Bologna Process credentials automatically recognised across Europe
- **Competency Transparency**: Detailed skill and learning outcome representation
- **Career Continuity**: Credentials accumulate throughout lifelong learning journey
- **Research Collaboration**: Verifiable research affiliations and project participations

### 6.2 Innovation Catalyst

The eIDAS2 transition creates opportunities for innovative service development:

**New Service Categories:**
- Lifelong learning credential portfolios
- Professional development tracking
- Research collaboration credentials
- Cross-sectoral skill recognition

**Technical Innovation:**
- Advanced privacy-preserving technologies
- Automated credential verification systems
- Intelligent attribute mapping and translation
- Enhanced user experience design

### 6.3 Competitive Positioning

Institutions and federations that successfully navigate the eIDAS2 transition gain significant competitive advantages:

**Market Position:**
- Enhanced credibility through regulatory compliance
- Broader service market access
- Improved international recognition
- Future-ready infrastructure

**Operational Efficiency:**
- Streamlined credential management processes
- Reduced manual verification requirements
- Enhanced security and trust mechanisms
- Improved user experience

## 7. Recommendations for Action

### 7.1 For GÉANT and eduGAIN

**Immediate Actions:**
1. Establish a dedicated eIDAS2 transition programme
2. Develop comprehensive technical integration roadmaps
3. Create training and support resources for member federations
4. Initiate pilot projects with willing institutions

**Medium-term Objectives:**
1. Implement hybrid trust architectures supporting both SAML and eIDAS2 protocols
2. Develop standardised attribute mapping between eduGAIN and EAA schemas
3. Establish relationships with European trust service providers
4. Create governance frameworks for eIDAS2 compliance

### 7.2 For National NRENs

**Strategic Priorities:**
1. Assess institutional readiness for eIDAS2 compliance
2. Develop national implementation plans aligned with government policies
3. Establish partnerships with qualified trust service providers
4. Create funding strategies for infrastructure upgrades

**Operational Requirements:**
1. Implement technical infrastructure supporting hybrid trust models
2. Develop training programmes for institutional members
3. Create support services for eIDAS2 compliance
4. Establish monitoring and evaluation frameworks

### 7.3 For Educational Institutions

**Institutional Strategies:**
1. Evaluate the business case for Authentic Source designation
2. Assess technical and financial requirements for eIDAS2 compliance
3. Develop institutional policies for credential issuance and management
4. Create user engagement strategies for wallet adoption

**Implementation Approaches:**
1. Pilot eIDAS2 integration with high-value credentials
2. Develop partnerships with other institutions for shared infrastructure
3. Invest in staff training and capacity building
4. Create user support and engagement programmes

## 8. Conclusion: Embracing the Paradigm Shift for Enhanced Relevance

The emergence of eIDAS2 and the European Digital Identity Wallet represents a fundamental transformation in how European digital identity operates. The shift from delegated authentication to user-centric verifiable credentials is not merely a technical evolution—it is a paradigm shift that offers eduGAIN and national education federations unprecedented opportunities to enhance their relevance and impact.

Rather than viewing this transformation as a threat to existing federation models, we have demonstrated that it presents a strategic opportunity to address long-standing limitations whilst opening new possibilities for innovation and service enhancement. The traditional "phone home" model of delegated authentication, whilst effective for its time, creates privacy concerns, single points of failure, and limits cross-sector interoperability. The new paradigm eliminates these constraints whilst empowering users with greater control over their digital identities.

The DC4EU project provides compelling evidence that this transformation is not only feasible but beneficial. Through practical implementation across multiple European countries, it demonstrates that educational institutions can successfully operate within the eIDAS2 framework whilst maintaining their autonomy and enhancing their capabilities. The EBSI infrastructure, rather than constraining institutional freedom, actually enhances it by providing transparent, auditable, and universally verifiable trust mechanisms.

**Key Success Factors:**
- **Understanding the Paradigm Shift**: Recognising that the change is fundamental, not merely technical
- **Embracing User-Centric Design**: Placing users in control of their credentials and privacy
- **Leveraging Cryptographic Trust**: Moving from real-time validation to offline verification
- **Maintaining Institutional Autonomy**: Using eIDAS2 compliance to enhance rather than constrain independence
- **Enabling Cross-Sector Integration**: Expanding beyond education to serve broader European digital identity needs

The path forward requires coordinated action across all stakeholders. GÉANT must lead the technical integration and provide guidance to member federations. NRENs must develop national implementation strategies that align with government policies whilst serving institutional needs. Educational institutions must assess their readiness and invest in the necessary technical and organisational adaptations.

Most importantly, all stakeholders must embrace the fundamental shift from delegated authentication to user-centric verifiable credentials. This is not a choice between eduGAIN and EBSI, but rather an evolution of eduGAIN that leverages EBSI's capabilities to create a more robust, privacy-preserving, and broadly applicable identity infrastructure.

The future of European research and education identity lies not in defending the status quo, but in embracing the opportunities presented by this paradigm shift. By doing so, eduGAIN and national federations can emerge as stronger, more relevant, and more valuable components of European digital infrastructure, serving their communities better whilst contributing to the broader European digital identity ecosystem.

The time for action is now. The paradigm shift is underway, and the institutions that embrace it will be best positioned to serve their users and contribute to European digital sovereignty. The lessons learned from DC4EU provide a clear roadmap for success, and the regulatory framework of eIDAS2 provides the legal foundation for long-term sustainability.

Success in this endeavour will ensure that the robust, community-driven identity systems that have served European education and research so well will continue to do so for generations to come—now enhanced with user-centric design, privacy protection, cryptographic trust, and the legal recognition that eIDAS2 provides. The paradigm shift is not an ending, but a beginning of a new era of enhanced capabilities and expanded opportunities.
