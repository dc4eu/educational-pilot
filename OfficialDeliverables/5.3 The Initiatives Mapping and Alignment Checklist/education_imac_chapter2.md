# 2 Education and Professional Qualifications Rulebook

The document titled "EDUCATION AND PROFESSIONAL QUALIFICATIONS RULEBOOK FOR DIGITAL CREDENTIALS COORDINATION" serves as a comprehensive guide for the implementation and governance of educational and professional qualification coordination within the European Union. It is structured to address key aspects such as governance, legal and regulatory frameworks, service descriptions, and technical trust frameworks to ensure cross-border interoperability whilst respecting institutional autonomy.

The Rulebook includes:

- **Introduction**: Outlining the scope and objectives of the framework for digital educational credentials.

- **Governance**: Defining institutional responsibilities, change management, and dispute resolution mechanisms specific to educational contexts, including relationships between ministries, educational institutions, and professional bodies.

- **Legal & Regulatory Framework**: Providing the legal basis for educational credential issuance, data protection, and user rights under EU and national laws, including compliance with eIDAS, GDPR, and education-specific regulations such as the Professional Qualifications Directive.

- **Service Description**: Detailing the nature and scope of educational services to be delivered, including formal qualifications, professional certifications, and continuing professional development credentials.

- **Trust Framework & Interoperability**: Explaining the technical trust models (Classical PKI and EBSI) and requirements for cross-border educational interoperability, supporting both traditional institutional hierarchies and emerging decentralised trust models.

Additionally, the document emphasises semantic and procedural consistency through the European Learning Model (ELM), selective disclosure for privacy protection, and localised validation policies. It supports both Classical PKI and Decentralised PKI approaches, aligning with eIDAS regulations whilst accommodating diverse institutional technical capabilities and educational traditions.

Supporting annexes include schema definitions aligned with EQF levels, ELM v3.2 specifications, references to European educational frameworks, and a comprehensive glossary to aid implementation across diverse educational contexts.

This Rulebook is essential for stakeholders involved in educational and professional qualification coordination, ensuring compliance, interoperability, and effective service delivery across borders whilst maintaining academic freedom and institutional independence.

## Key Components of the Education and Professional Qualifications Rulebook

### Governance Framework

The governance framework establishes a multi-layered approach that respects the principle of subsidiarity whilst enabling European coordination:

**National Level Governance**:
- **Ministries and Public Authorities**: Act as Root Trusted Accreditation Organisations (RootTAOs) with ultimate authority over educational institutions and professional qualifications within their jurisdiction
- **Educational Institution Recognition**: Systematic processes for accrediting and authorising institutions to deliver programmes and issue credentials
- **Professional Body Authorisation**: Frameworks for recognising professional bodies' authority to issue professional qualifications and maintain practitioner registers

**Institutional Level Governance**:
- **Educational Institution Autonomy**: Preservation of academic freedom and institutional independence within the trust framework
- **Professional Body Independence**: Maintenance of professional self-regulation principles whilst ensuring European interoperability
- **Quality Assurance Integration**: Alignment with existing national and European quality assurance mechanisms

**European Level Coordination**:
- **EQF Alignment**: Integration with the European Qualifications Framework for automatic level recognition
- **EHEA Compliance**: Support for European Higher Education Area objectives and Bologna Process principles
- **Professional Mobility**: Facilitation of professional recognition under the Professional Qualifications Directive

### Legal and Regulatory Framework

The legal framework provides comprehensive coverage of educational credential issuance within the European regulatory landscape:

**eIDAS 2.0 Compliance**:
- **Electronic Attestations of Attributes (EAAs)**: Implementation of educational EAAs for institutional authorisation and credential validation
- **Trust Service Provider Classification**: Support for educational institutions as Qualified EAA Providers (QEAA), Public EAA Providers (PubEAA), or standard EAA Providers
- **Cross-Border Legal Recognition**: Ensuring educational credentials maintain legal validity across Member State boundaries

**Education-Specific Legislation**:
- **Professional Qualifications Directive**: Integration with existing professional recognition mechanisms
- **GDPR in Educational Contexts**: Specific provisions for handling student data and educational records with enhanced privacy protection
- **Single Digital Gateway Regulation**: Alignment with Once-Only Principles for educational administrative procedures

**Institutional Rights and Obligations**:
- **Academic Freedom Protection**: Safeguarding institutional autonomy in curriculum design and assessment methods
- **Student Rights**: Ensuring data portability, credential ownership, and privacy protection throughout the educational journey
- **Professional Standards**: Maintaining professional body authority over practitioner competency requirements

### Service Description Framework

The service framework defines the comprehensive range of educational and professional services supported:

**Formal Educational Credentials**:
- **Academic Degrees**: Bachelor's, Master's, and Doctoral qualifications with EQF level mapping
- **Vocational Qualifications**: VET certificates and professional training credentials
- **Academic Transcripts**: Detailed learning achievement records with selective disclosure capabilities
- **Student Identity Credentials**: Educational ID supporting institutional affiliation and service access

**Professional Qualification Services**:
- **Professional Licences**: Regulated profession authorisations with ongoing validity monitoring
- **Professional Identity Credentials**: Sector-specific identity attestations for professional practice
- **Continuing Professional Development**: CPD records supporting lifelong learning requirements
- **Professional Membership**: Association membership credentials with benefits and obligations

**Supporting Services**:
- **Quality Assurance Information**: Institutional and programme accreditation status
- **Recognition Statements**: Automatic qualification recognition for mobility purposes
- **Learning Analytics**: Privacy-preserving competency and achievement analytics
- **Alumni Services**: Long-term credential maintenance and verification support

### Trust Framework and Technical Interoperability

The technical framework supports multiple trust models to accommodate diverse institutional capabilities and preferences:

**Classical PKI Trust Model**:
- **X.509 Certificate Infrastructure**: Traditional hierarchical trust chains from national education authorities
- **Educational Certificate Authorities**: Specialised CAs for educational credential issuance
- **SD-JWT Implementation**: Selective disclosure JSON Web Tokens for privacy-preserving credential sharing
- **Trust List Management**: Comprehensive trusted lists of educational institutions and professional bodies

**Decentralised PKI (EBSI) Trust Model**:
- **DID-Based Identity**: Decentralised identifiers for institutional and professional identity
- **EBSI Trust Registry**: European Blockchain Services Infrastructure for cross-border trust anchoring
- **W3C Verifiable Credentials**: Standard-compliant credential formats with cryptographic integrity
- **Distributed Trust Verification**: Blockchain-anchored verification reducing reliance on central authorities

**Hybrid Trust Approaches**:
- **Multi-Model Support**: Seamless integration between Classical PKI and Decentralised PKI systems
- **Trust Bridge Mechanisms**: Interoperability protocols enabling cross-model credential verification
- **Migration Pathways**: Support for institutional transition between trust models
- **Backwards Compatibility**: Ensuring existing systems continue to function during framework adoption

The framework emphasises privacy-by-design principles, implementing selective disclosure mechanisms that allow credential holders to share only necessary information whilst maintaining cryptographic integrity and verifiability. This approach supports both educational mobility requirements and professional practice needs whilst protecting individual privacy rights.

## Detailed Framework Components

### Institutional Identity and Registration

**Natural Person Identity Management**:
The European Digital Identity Wallet serves as the harmonised electronic identification method for students and professionals, introducing Personal Identification Data (PID) as the preferred option when high security is required. This system respects Member State authority over identity whilst creating a consistent European approach for educational contexts.

This approach streamlines identity verification in educational processes, particularly in:
- **Registration and Enrolment**: When students begin their educational journey, requiring secure identification
- **Formal Degree Issuance**: When official qualifications are awarded, needing reliable identity confirmation
- **Professional Certification**: When practitioners receive professional qualifications requiring verified identity
- **Cross-Border Recognition**: When qualifications are presented in different Member States

**Legal Entity Identity Infrastructure**:
Educational institutions require reliable digital identification through Public Key Infrastructure (PKI) with X.509v3 digital certificates. This system assigns unique digital identifiers to institutions, linking them with public certificates for seamless identity verification across European systems. The PKI infrastructure provides the necessary balance, enabling institutions to participate in European-wide systems whilst maintaining their internal processes intact.

### Trust List Management and Verification

**Educational Institution Trusted Lists**:
Comprehensive registries of qualified educational institutions registered with their respective national educational authorities, including:
- University and higher education institution registries
- Vocational education and training provider lists
- Professional training organisation directories
- Quality assurance agency registrations

**Professional Body Trusted Lists**:
Authoritative directories of professional organisations and certification bodies authorised to issue professional qualifications, covering:
- National professional councils and chambers
- Industry-specific certification bodies
- Continuing professional development providers
- International professional recognition authorities

**Relying Party Verification Lists**:
Registries of verification services and platforms authorised to verify educational credentials, ensuring that only legitimate entities can access and verify sensitive educational information whilst maintaining privacy protections.

### Data Models and Semantic Interoperability

**European Learning Model (ELM) Integration**:
The framework incorporates ELM v3.2 specifications to ensure semantic consistency across European educational systems. This includes:
- Standardised learning outcome descriptions
- Competency framework mappings
- Achievement level classifications
- Credit transfer and accumulation mechanisms

**EQF Level Mapping Framework**:
Systematic integration with the European Qualifications Framework enabling:
- Automatic qualification level recognition across borders
- Transparent competency level comparisons
- Simplified academic and professional mobility
- Enhanced employer understanding of qualification levels

**Selective Disclosure Implementation**:
Privacy-preserving mechanisms allowing credential holders to share only necessary information:
- Granular attribute sharing capabilities
- Context-specific information disclosure
- Zero-knowledge proof implementations
- Minimal data exposure principles

### Lifecycle Management and Governance

**Credential Lifecycle Tracking**:
Comprehensive management of credentials from creation through potential revocation, including:
- Issuance workflow management
- Validation and verification processes
- Renewal and update mechanisms
- Revocation and suspension procedures

**Change Management Procedures**:
Systematic approaches to managing changes in institutional status, accreditation, or authorisation:
- Real-time status updates
- Automated notification systems
- Impact assessment procedures
- Stakeholder communication protocols

**Dispute Resolution Mechanisms**:
Structured processes for resolving conflicts related to credential validity, institutional authority, or cross-border recognition:
- Multi-level arbitration procedures
- Technical validation mechanisms
- Legal compliance verification
- Stakeholder mediation processes

## Implementation Considerations

### Stakeholder Onboarding

**Educational Institution Integration**:
Systematic procedures for bringing educational institutions into the digital credential ecosystem:
- Technical capability assessment
- Security compliance verification
- Staff training and support
- Phased implementation approaches

**Professional Body Engagement**:
Tailored approaches for professional organisations:
- Regulatory compliance alignment
- Professional practice integration
- Member communication strategies
- Continuing education coordination

**Student and Professional Preparation**:
User-centric approaches ensuring smooth adoption:
- Digital literacy support
- Privacy education programmes
- Technical assistance services
- Multi-language support provision

### Technical Infrastructure Requirements

**Security and Privacy Measures**:
Comprehensive security frameworks protecting sensitive educational data:
- End-to-end encryption implementations
- Multi-factor authentication requirements
- Regular security auditing procedures
- Privacy impact assessment protocols

**Interoperability Standards**:
Technical specifications ensuring seamless system integration:
- API standardisation requirements
- Data format compatibility specifications
- Protocol harmonisation guidelines
- Cross-platform integration capabilities

**Scalability and Performance**:
Infrastructure design supporting large-scale European deployment:
- Load balancing and distribution mechanisms
- Performance monitoring and optimisation
- Capacity planning and expansion procedures
- Service availability and reliability standards

This comprehensive rulebook provides the foundation for a trusted, interoperable, and privacy-preserving digital credential ecosystem that serves the diverse needs of European education and professional qualification stakeholders whilst respecting national sovereignty and institutional autonomy.