## <a id="_Toc182376687"></a><a id="_Toc184710034"></a>Chapter 6: The education and professional qualifications sectorial rulebook

The education and professional qualifications sectorial rulebook aims to establish a standardised approach for managing digital educational and professional credentials within the European Union\. The rulebook sets the foundation for trusted digital credential management, encompassing identity, trust, data models, and operational processes\. This framework balances member state sovereignty with European integration needs, creating a unified system that supports educational mobility while respecting national and institutional autonomy\.

Each component serves both practical needs and policy goals, creating a system that works for students, institutions, and member states while advancing European educational integration\.

The technical implementations always support policy priorities, making the system both practically useful and politically aligned with European goals for education, privacy, and mobility\.

The complete system brings together European educational priorities:

- Respects member state sovereignty in education
- Maintains institutional independence
- Protects student privacy
- Supports educational mobility
- Links to quality frameworks
- Creates trusted credentials
- Enables automatic recognition
- Supports lifelong learning
- Records formal and informal learning
- Works across European borders

### <a id="_Toc184710035"></a>6\.1 Natural person's identity

The European Digital Identity wallet serves as a harmonised electronic identification method, introducing personal identification data \(PID\) as the preferred option when high security is needed\. This system respects member state authority over identity while creating a consistent European approach\. 

This approach streamlines identity verification in educational contexts, particularly in two main processes:

- Registration and enrolment: When students begin their educational journey, requiring secure identification
- Formal degree issuance: When official qualifications are awarded, needing reliable identity confirmation

### <a id="_Toc184710036"></a>6\.2 Legal entity's identity 

Educational institutions need reliable digital identification through public key infrastructure \(PKI\) with X\.509v3 digital certificates\. This system assigns unique digital identifiers to institutions, linking them with public certificates for seamless identity verification across European systems\. The public key infrastructure \(PKI\) with X\.509v3 digital certificates provides this balance, letting institutions participate in European\-wide systems while keeping their internal processes intact\. 

### <a id="_Toc184710037"></a>6\.3 Identity matching

The combination of personal identification data and member state\-specific matching rules creates a unified approach to identity verification\. The rulebook acknowledges the complexity of European identity systems by combining personal identification data with member state\-specific matching rules\. This approach respects national sovereignty while creating reliable links between national identities and institutional records, making student identification more accurate across borders\.

This system helps educational institutions connect external identities \(issued by national authorities\) with their internal systems, making student identification more accurate and efficient\.

### <a id="_Toc184710038"></a>6\.4 Trusted lists

The system maintains several critical lists to support trust in educational credentials:

- Trusted issuers: Authorised organisations that can issue credentials, ensuring only legitimate institutions can grant qualifications
- Relying parties: Organisations authorised to verify and accept credentials
- Trusted accreditation organisations: Bodies that validate educational institutions, maintaining quality standards
- Data models catalogue: Standardised formats for representing educational credentials
- Trusted schemes: Templates ensuring consistent credential structure

Within the the trust framework, trust lists support European education policy through several interconnected lists:

- Trusted issuers: Maintains academic integrity by authorising legitimate institutions
- Relying parties: Creates clear paths for credential recognition
- Trusted accreditation organisations: Links to European quality frameworks like EQAR
- Data models catalogue: Enables consistent credential representation
- Trusted schemes: Supports automated processing across systems

### <a id="_Toc184710039"></a>6\.5 Lifecycle management

The credential lifecycle system supports educational mobility while protecting credential integrity\. This balance enables institutions to manage qualifications independently while ensuring European\-wide recognition\. The system incorporates privacy\-by\-design principles, letting institutions update credential status without tracking usage patterns\.

Managing educational credentials requires careful tracking from creation through to potential revocation and/or suspension\. The system:

- Tracks credential status changes \(active, suspended, revoked\)
- Maintains verification services that respect privacy
- Provides tools for educational institutions to manage their issued credentials

### <a id="_Toc184710040"></a>6\.6 Data model

The credential data model follows W3C Verifiable Credential standards, structuring educational data in a consistent format\. Each credential includes:

- Context definitions for clear interpretation
- A unique identifier
- The credential type
- The issuing authority's identifier
- Issue date
- Information about the credential holder
- Cryptographic proof of authenticity
- Multi\-language support

### <a id="_Toc184710041"></a>6\.7 Education and professional qualifications Ontology \- European Learning Model \(ELM\)

The ELM creates a shared understanding of educational achievements across Europe\. Supporting and facilitating quality assurance information, links to European and National qualification frameworks and cross\-border recognition support, the model covers:

- Achievement records:
	- Qualification titles and descriptions
	- Classification of the achievement
	- European Qualification Framework alignment
	- Issue dates
	- Issuing institution details
- Learning outcomes:
	- Knowledge gained
	- Skills developed
	- Competences achieved
	- Links to European skills frameworks
- Learning activities:
	- Type of education received
	- Duration of study
	- Learning delivery method
- Assessment details:
	- Evaluation methods used
	- Grading systems
	- Assessment authority
- Issuer information:
	- Legal institution name
	- Accreditation status
	- Contact information
	- Digital identification
- Holder details:
	- Personal identification compliant with privacy laws
	- Educational profile linkage
- Recognition elements:
	- Cross\-border agreements
	- Framework alignments
	- European Education Area mobility support
- Supporting data:
	- Links to course documentation
	- Language of instruction
	- Geographic context

### <a id="_Toc184710042"></a>6\.8 Issuance

The issuance process varies based on the type of attestation:

- Qualified electronic attestation of attributes \(QEAA\):
	- Provided by qualified trust service providers
	- Requires citizen consent
	- Needs data validation through member state mechanisms
- Public sector body electronic attestation of attributes \(PSBEAA\):
	- Issued by public sector bodies
	- Must meet specific regulatory requirements
	- Public sector bodies act as both authentic source and issuer
- Electronic attestation of attributes \(EAA\) issuance follows these steps:

1. Secure connection with the European Digital Identity Wallet
2. Identity verification when required
3. Identity matching processes
4. Data gathering from authentic sources
5. Credential creation using trusted schemas
6. Addition of quality assurance information
7. Digital identifier selection
8. Direct or deferred issuance to the wallet

### <a id="_Toc184710043"></a>6\.9 Selective disclosure

The system enables users to share only necessary credential data, meeting privacy requirements through:

- Technical implementations like SD\-JWS, SD\-JWT and BBS\+
- Issuer\-defined disclosure policies
- Privacy\-preserving verification methods

### <a id="_Toc184710044"></a>6\.10 Sharing mechanisms

The credential sharing framework supports European mobility through:

- Cross\-border credential recognition
- Privacy\-protected verification
- Quality assurance validation
- Institutional trust verification

The credential sharing system uses OpenID for Verifiable Presentations to:

- Establish secure connections with wallets
- Verify proof of possession
- Check relying party trustworthiness
- Validate information proportionality
- Enable credential combination
- Support selective disclosure policies

### <a id="_Toc184710045"></a>6\.11 Verification

The verification process ensures credential validity while protecting privacy:

- Key characteristics:
- Distributed system to avoid single points of failure
- Privacy protection from issuer monitoring
- Time\-based validation linked to credential issuance
- The verification process follows these steps:

1. Secure wallet connection and proof of possession
2. Credential request
3. Integrity verification
4. Metadata checking \(expiration dates\)
5. Issuer verification:

- Digital identifier validation
- Educational accreditation checking
- Accreditation issuer verification
- Status verification

1. Identity information analysis
2. Schema compliance checking
3. Quality assurance verification:

- Issuer entitlement checking
- Expiration verification
- Status checking

1. Credential status verification
2. Record keeping for audit purposes

### <a id="_Toc184710046"></a>6\.12 Enforcement policy agent

The wallet's policy enforcement role implements European privacy principles in practical ways:

- Students control their educational records
- Institutions request only necessary data
- Systems prevent excessive data collection
- Privacy protection becomes automatic
- Cross\-border rights remain protected

Digital wallets act as policy enforcers by:

- Detecting disproportionate information requests
- Warning users about excessive data sharing
- Blocking unauthorised information access
- Maintaining user control over personal data

To fully respect individual's rights, "Blocking" won't be applied at sectorial level\.

### <a id="_Toc184710047"></a>6\.13 Supporting infrastructure

This infrastructure supports the entire credential ecosystem while maintaining security, privacy, and usability across European educational systems\. The underlying system requires:

- Multi\-domain and sector support
- Distributed architecture
- Pan\-European coverage
- Privacy\-enhanced verification
- Data protection compliance
- Security audit mechanisms
- Verification record keeping
- Service discovery tools
- Cross\-country legal entity mandatory recognition