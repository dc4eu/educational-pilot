## <a id="_Toc182376676"></a><a id="_Toc184710023"></a>Chapter 4: Operational Model

The operational model for managing educational and professional credentials across Europe combines robust governance with efficient processes to ensure trust, security, and interoperability\. This chapter first establishes the fundamental trust model and governance framework that underpins all credential operations, then details the specific processes and responsibilities for credential management\.

The framework adopts a non\-delegated trust model where educational institutions and professional bodies maintain direct responsibility for their credentials\. This approach ensures clear accountability while respecting institutional autonomy, supporting both the integrity of credentials and the privacy of individuals\. The governance structure provides clear oversight at European and national levels while enabling efficient operations at the institutional level\.

Building upon this foundation, the chapter explores the complete lifecycle of credentials, from issuance through verification, and details how different stakeholders interact within the framework\. The operational model addresses several critical needs in the European education and professional qualification landscape:

- Trust establishment: Creating and maintaining trusted relationships between credential issuers, holders, and verifiers across borders\.
- Privacy protection: Ensuring individual control over personal data while enabling efficient credential verification\.
- Institutional autonomy: Supporting the independence of educational institutions while maintaining interoperability\.
- Cross\-border recognition: Facilitating qualification recognition and professional mobility throughout Europe\.
- Regulatory compliance: Ensuring alignment with European regulations while supporting national requirements\.

This chapter provides stakeholders with a clear understanding of their roles, responsibilities, and interactions within the trust framework\. Through detailed explanations of governance structures, operational processes, and implementation guidelines, it offers a comprehensive blueprint for implementing trusted credential management across the European education and professional qualification sectors\.

The following sections detail:

- The trust model and governance framework that underpins all operations
- The complete credential lifecycle management process
- Roles and responsibilities of various stakeholders
- Compliance requirements and quality assurance measures
- Benefits and outcomes of the operational model

This operational model provides the foundation for transforming credential management in Europe, supporting increased mobility, lifelong learning, and a more dynamic and efficient labour market\.

### <a id="_Toc182376677"></a><a id="_Toc184710024"></a>4\.1 Trust model and Governance framework

The trust framework for European educational and professional credentials builds upon proven approaches to cross\-border cooperation in education\. Drawing key lessons from the Bologna Process's successful implementation of voluntary standards, it establishes governance mechanisms that respect institutional autonomy while ensuring consistent quality across borders\. Like the Bologna Follow\-up Group \(BFUG\), it creates clear coordination structures while preserving institutional independence in implementation\.

The framework adopts a non\-delegated trust model, mirroring the Bologna Process's approach where common standards are implemented independently by institutions according to their local context\. This model ensures both standardization where needed and flexibility where required, supporting the diverse needs of European education while maintaining interoperability\.

The technical implementation of this trust model is detailed in Section 7\.2, with practical examples demonstrated in Chapter 7\.

#### 4\.1\.1 Trust Framework foundation

The European education and professional qualification sectors require a trust framework that balances institutional autonomy with reliable cross\-border credential verification\. At its core, this framework implements a non\-delegated trust model, where educational institutions and professional bodies maintain direct responsibility and authority over their credentials\.

In this non\-delegated approach, trust flows directly between credential issuers and verifiers, without requiring intermediary authorities to establish credential validity\. This direct trust relationship ensures that the authentic sources of information \-educational institutions and professional bodies\- maintain complete control over their credential issuance and status management processes\.

The trust framework implements a non\-delegated trust model where educational institutions and professional bodies maintain direct responsibility for their credentials\. This approach ensures:

- Direct accountability
	- Each institution remains directly responsible for its credentials
	- Clear lines of authority and responsibility  
	- Immediate control over credential status

These accountability mechanisms are implemented through specific processes detailed in Section 4\.4: Compliance and monitoring framework\.

- Institutional autonomy
	- Organizations implement framework according to their needs
	- Maintenance of institutional identity
	- Support for local requirements

The practical implementation of institutional autonomy within the framework is demonstrated through specific use cases in Section 6\.7\.

- Privacy Protection  
	- Individual control over credential sharing
	- Selective disclosure capabilities
	- Privacy\-preserving verification

Technical implementation of these privacy measures is detailed in Section 7\.2: Core Data Model Architecture\.

This direct trust relationship ensures that the authentic sources of information maintain complete control over their credential issuance and status management processes\. The practical implementation of these processes is detailed in Chapter 5: Natural persons and legal entities onboarding process\.

#### 4\.1\.2 Governance structure

##### European level oversight

At the European level, designated authorities establish and maintain the framework's core requirements\. These authorities:

- Define framework standards and protocols that ensure consistency across implementations\. These standards support interoperability while allowing flexibility in how institutions meet requirements\.
- Monitor framework compliance through regular assessments and audits\. This oversight ensures the framework maintains high standards of trust and security across all participating institutions\.
- Facilitate cross\-border recognition by maintaining alignment with relevant European initiatives and regulations\. This coordination ensures the framework supports broader European objectives for educational and professional mobility\.
- Provide guidance on framework implementation, helping institutions understand and meet requirements while maintaining their autonomy\.

This oversight aligns with European strategies and regulations as outlined in Section 1\.4 and Annex C: Regulatory references\.

##### National level coordination

National authorities serve as coordinators within their jurisdictions, providing a crucial link between European oversight and institutional implementation\. These bodies:

- Maintain authoritative registries of qualified credential issuers within their territory\. These registries provide verifiers with reliable information about authorized institutions\.
- Ensure alignment between framework implementation and national regulations\. This coordination prevents conflicts between European and national requirements\.
- Support national institutions in framework adoption, providing guidance and resources that facilitate effective implementation\.
- Monitor compliance at the national level, ensuring institutions meet both framework requirements and national standards\.

The diverse approaches to national coordination are explored in Section 2\.1: Decentralised authority and Member State autonomy\.

##### Institutional level implementation

Individual institutions—universities, professional bodies, and other authorized organizations—maintain operational control over their credential processes while adhering to framework standards\. At this level, institutions:

- Manage their credential issuance processes according to framework requirements\. This includes maintaining secure systems for credential creation and management\.
- Control credential status information, including updates and revocations\. This direct control ensures immediate response to any required status changes\.
- Implement required security and privacy measures that protect both institutional and individual interests\.
- Maintain compliance with framework standards while preserving their institutional identity and autonomy\.

Practical examples of institutional implementation are provided in the use cases in Chapter 7, particularly Sections 7\.7\.1 and 7\.7\.2\.

#### 4\.1\.3 Trust Framework components

##### Core requirements

The trust framework is built on four fundamental requirements that drive all operational elements and governance processes\. These core requirements establish the foundation for secure, interoperable, and privacy\-preserving credential management across Europe\.

- Standardization

The framework ensures consistent credential handling across all participating institutions through:

- Credential Format Standardization
	- Implementation of W3C Verifiable Credentials Data Model
	- Alignment with European Learning Model specifications
	- Standardized attribute definitions and structures
	- Common metadata requirements

The choice of the W3C Verifiable Credentials \(VC\) Data Model as the foundational format for credential issuance was driven by its robust support for cross\-border interoperability, privacy\-preserving features, and its alignment with global digital identity standards\. The W3C VC model enables selective disclosure, allowing users to share only the necessary portions of their credentials, thus enhancing user privacy while maintaining data integrity\. This ensures that institutions across the EU can issue, verify, and trust digital credentials uniformly, meeting the diverse regulatory requirements of different member states\. It is also important to remark that European Learning Model \(ELM\) is based on W3C\-VCDM and several European solutions re\-use ELM as a core \(Europass, European Digital Credentials Infrastructure, European Blockchain Services Infrastructure, European Employment Service \- EURES, European Skills Data Space\)\. 

The integration of the European Learning Model \(ELM\) alongside the W3C Verifiable Credentials framework addresses key challenges such as cross\-border recognition and compatibility with varying credential verification processes across EU member states\. The ELM ensures that credentials maintain a standardized, interoperable structure, promoting seamless data exchange between educational institutions and professional bodies\. By employing these data models, the BBP not only adheres to established EU educational frameworks but also supports a scalable, adaptable approach for future credentialing needs\.

Detailed implementation in Section 4\.2: Credential lifecycle management

- Process Standardization
	- Unified credential issuance procedures
	- Common verification protocols
	- Standardized status management processes
	- Consistent privacy protection measures

Detailed implementation in Section 4\.3: Roles and responsibilities

- Interoperability Requirements
	- Cross\-border credential recognition
	- Multi\-system compatibility
	- Standard data exchange formats
	- Common API specifications

Technical details in Section 7\.2: Core data model architecture

- Security

The framework maintains credential integrity and system trust through:

- Credential security
	- Cryptographic protection of credentials
	- Tamper\-evident mechanisms
	- Secure issuance protocols
	- Protected storage requirements

Implementation details in Section 4\.5: Infrastructure requirements

- System security
	- Access control mechanisms
	- Authentication requirements
	- Audit logging
	- Incident response procedures

Detailed in Section 4\.4: Compliance and monitoring framework

- Operational security
	- Secure communication channels
	- Data protection measures
	- Backup procedures
	- Recovery protocols

Technical implementation in Section 7\.5: Implementation guidelines

- Privacy

The framework ensures privacy protection and individual control through:

- Privacy by design
	- Data minimization principles
	- Purpose limitation
	- Storage restrictions
	- Processing safeguards

Alignment with requirements in Annex C: Regulatory references

- Individual control
	- Selective disclosure capabilities
	- Consent management
	- User authorization requirements
	- Data subject rights protection

Implementation in Section 4\.2: Credential lifecycle management

- Privacy\-preserving operations
	- \- Anonymous credential presentation
	- \- Unlikable transactions
	- \- Usage tracking prevention
	- \- Secure deletion procedures

Technical details in Section 7\.3: Model structure

- Quality assurance

The framework maintains high operational standards through:

- Process quality
	- Defined quality standards
	- Process monitoring
	- Performance metrics
	- Continuous improvement procedures

Detailed in Section 4\.4: Compliance and monitoring framework

- Credential quality
	- Issuer verification
	- Credential validation
	- Status accuracy
	- Content integrity

Implementation in Section 4\.2: Credential lifecycle management

- Service quality
	- Performance standards
	- Availability requirements
	- Response time metrics
	- Support procedures

Operational details in Section 4\.5: Infrastructure requirements

These core requirements form the foundation for all operational processes and technical implementations detailed in subsequent sections\. Each requirement is realized through specific operational elements, compliance measures, and technical specifications\. The requirements are designed to be technology\-neutral while ensuring consistent implementation across the framework\.

All core requirements support cross\-border credential recognition and verification while accommodating national requirements and local regulations\. This enables seamless operation across European member states while respecting institutional autonomy and national sovereignty\.

The core requirements are designed to accommodate emerging technologies and evolving needs while maintaining backward compatibility and operational stability\. Regular review processes ensure requirements remain current and effective\.

These requirements are elaborated in detail in Section 4\.5: Infrastructure requirements\.

##### Operational Elements

The trust framework's operational elements define how credentials are managed throughout their lifecycle while maintaining security and institutional autonomy\.

1. Credential management

- Issuance
	- Verification of qualification completion before issuance
	- Creation of credentials according to framework standards \(providing composed complex credentials if needed: e\.g\. Master credential including a programme' quality assurance credential\)
	- Application of institutional authorization
	- Secure delivery to recipient's EUDI wallet
- Storage
	- Secure maintenance in authorized EUDI wallets
	- Institutional record\-keeping of issued credentials
	- Privacy controls protecting credential information
	- Regular status information updates
- Presentation
	- Selective sharing of credential information
	- Privacy\-preserving presentation methods
	- Prevention of unauthorized tracking
	- Cross\-border sharing support
- Verification
	- Direct confirmation of issuer authority
	- Real\-time status verification
	- Privacy\-preserving verification methods
	- Cross\-border verification support

The technical implementation of these credential management processes is detailed in Section 7\.3: Model structure\.

1. Status management

- Active status maintenance
	- Regular confirmation procedures
	- Automated monitoring systems
	- Timely status updates
	- Clear validity indicators
- Suspension mechanisms
	- Defined suspension criteria
	- Immediate status update capabilities
	- Clear reinstatement procedures
	- Transparent communication processes
- Revocation processes
	- Strict revocation protocols
	- Immediate status updates
	- Clear documentation requirements
	- Permanent record maintenance

Specific status management scenarios are demonstrated in use cases 6\.7\.3\.1 through 6\.7\.3\.5\.

1. Quality controls

- Process monitoring
	- Regular assessment of operations
	- Performance metrics tracking
	- Stakeholder feedback collection
	- Continuous improvement procedures
- Security measures
	- Access control systems
	- Encryption requirements
	- Audit logging
	- Incident response procedures

These controls are aligned with the quality assurance standards described in Section 2\.10\.

1. Cross\-border operations

- Recognition support
	- Standardized format implementation
	- Clear status communication
	- Efficient verification processes
	- Multi\-jurisdiction support
- Jurisdictional alignment
	- National system compatibility
	- Regulatory compliance
	- Language support
	- Local requirement accommodation

Implementation challenges and solutions for cross\-border operations are discussed in Section 3\.2: Recognition of Qualifications\.

1. Privacy framework

- Data protection
	- Minimization principles
	- Selective disclosure mechanisms
	- Access control systems
	- Audit capabilities
- User control
	- Individual authorization requirements
	- Usage tracking prevention
	- Secure storage mechanisms
	- Clear sharing permissions

Technical implementation of privacy measures is detailed in Section 7\.5: Implementation guidelines\.

1. Integration components

- System connections
	- Educational management systems
	- Professional body platforms
	- Verification services
	- Digital wallet interfaces
- Data exchange
	- Standardized protocols
	- Secure transmission methods
	- Privacy\-preserving mechanisms
	- Cross\-system compatibility

Specific integration requirements are elaborated in Section 4\.5\.4: Integration requirements\.

The operational elements described here are implemented through specific processes detailed in Chapter 5 and demonstrated through use cases in Chapter 7\.

##### Compliance framework

This framework implements regulatory requirements outlined in section 1\.4 and detailed in Annex C\. The compliance framework ensures trust framework integrity through comprehensive oversight while respecting institutional autonomy and privacy requirements\.

1. Regulatory compliance

- European Level Requirements
	- eIDAS Regulation alignment
		- Trust service requirements
		- Electronic identification standards
		- Legal recognition provisions
		- Cross\-border validity
	- GDPR Implementation
		- Privacy by design principles
		- Data processing requirements
		- Individual rights protection
		- Cross\-border data transfer rules
	- Single Digital Gateway Support
		- Once\-only principles' implementation
		- Cross\-border service access
		- Administrative simplification
		- Interoperability requirements
- National level requirements
	- Education regulations alignment
		- National qualification standards
		- Professional licensing requirements
		- Local accreditation rules
		- Institutional autonomy respect
	- Data protection compliance
		- National privacy laws
		- Sector\-specific regulations
		- Local security standards
		- Jurisdictional requirements

1. Quality assurance

- Operational standards
	- Process requirements
		- Credential issuance procedures
		- Verification protocols
		- Status management rules
		- Documentation standards
	- Security measures
		- Access control requirements
		- Data protection standards
		- System security protocols
		- Incident response procedures
	- Privacy standards
		- Data minimization principles
		- Consent management requirements
		- Information sharing rules
		- Rights protection measures
- Implementation requirements
	- Technical standards
		- Infrastructure requirements
		- Integration specifications
		- Security protocols
		- Performance standards
	- Process standards
		- Operational procedures
		- Workflow requirements
		- Documentation rules
		- Quality metrics

1. Monitoring framework

- Continuous Monitoring
	- System performance tracking
		- Operational metrics
		- Security indicators
		- Privacy compliance
		- Service levels
	- Compliance verification
		- Regular checks
		- Automated monitoring
		- Issue detection
		- Response tracking
- Audit programs
	- Internal audits
		- Regular self\-assessments
		- Process reviews
		- Compliance checks
		- Performance evaluation
	- External audits
		- Independent verification
		- Compliance validation
		- Security assessment
		- Privacy review

1. Risk management

- Assessment framework
	- Risk identification
		- Threat analysis
		- Vulnerability assessment
		- Impact evaluation
		- Probability assessment
	- Mitigation planning
		- Control measures
		- Response procedures
		- Recovery plans
		- Prevention strategies
- Security controls
	- Access management
		- Authentication requirements
		- Authorization controls
		- Access logging
		- Audit trails
	- Data protection
		- Encryption standards
		- Storage requirements
		- Transmission security
		- Backup procedures

1. Improvement framework

- Performance Analysis
	- Metric tracking
		- Key performance indicators
		- Success measures
		- Issue tracking
		- Trend analysis
	- Feedback management
		- Stakeholder input
		- User experience data
		- Issue reports
		- Improvement suggestions
- Enhancement process
	- Planning
		- Priority setting
		- Resource allocation
		- Timeline development
		- Impact assessment
	- Implementation
		- Change management
		- Testing procedures
		- Deployment controls
		- Validation measures

1. Reporting framework

- Regular Reporting
	- Performance reports
		- Operational metrics
		- Compliance status
		- Security incidents
		- Privacy compliance
	- Status updates
		- System health
		- Issue tracking
		- Resolution progress
		- Improvement initiatives
- Communication
	- Stakeholder updates
		- Regular briefings
		- Issue notifications
		- Change communications
		- Progress reports
	- Transparency measures
		- Public reporting
		- Stakeholder access
		- Information sharing
		- Feedback channels

The practical implementation of these compliance requirements is demonstrated through the use cases in Chapter 7, particularly in sections 6\.7\.3\.4 and 6\.7\.3\.5 for professional qualifications\.

Through this comprehensive trust model and governance framework, the system ensures reliable credential management while supporting institutional autonomy and individual privacy\. The non\-delegated trust model, combined with clear governance structures and robust accountability mechanisms, provides a solid foundation for secure and efficient credential operations across Europe\.

### <a id="_Toc182376678"></a><a id="_Toc184710025"></a>4\.2 Credential lifecycle management

#### 4\.2\.1 Overview

The credential lifecycle encompasses all stages from initial issuance through eventual expiration or revocation\. Operating within the non\-delegated trust model established in Section 4\.1, this lifecycle ensures secure, efficient credential management while maintaining privacy and institutional control\.

Each stage of the lifecycle requires careful management to maintain credential integrity, protect privacy, and support efficient verification\. Educational institutions and professional bodies maintain direct control throughout the lifecycle, ensuring immediate response to any required changes while supporting cross\-border recognition and mobility\.

The technical framework supporting these processes is detailed in Section 7\.3, whilst implementation guidance is provided in Chapter 8\.

#### 4\.2\.2 Core lifecycle stages

##### Issuance

The credential lifecycle begins with issuance by an authorized institution\. During this stage, the institution:

- Verifies qualification completion or achievement of required standards\. This verification ensures credentials accurately reflect earned qualifications\.
- Creates the credential according to framework standards\. This includes all required information while maintaining data minimization principles\.
- Applies institutional authorization, establishing the credential's authenticity\. This step creates a direct trust relationship between the issuing institution and the credential\.
- Delivers the credential to the recipient securely\. This transfer gives the recipient control over their credential while maintaining its integrity\.

##### Storage and management

Once issued, credentials require secure storage and ongoing management:

- Recipients maintain their credentials in authorized EUDI wallets\. These wallets give individuals control over their credentials while ensuring security\.
- Institutions maintain authoritative records of issued credentials\. These records support status management and verification processes\.
- Privacy controls protect credential information throughout its lifecycle\. These controls prevent unauthorized access while enabling legitimate use\.
- Regular status updates ensure credential information remains current\. These updates maintain the credential's reliability for verification purposes\.

##### Presentation and sharing

Credential holders’ control when and how to share their credentials:

- Selective sharing allows holders to reveal only necessary information\. This capability protects privacy while meeting verification needs\. Issuer's disclosure policies shall be taken into account, to avoid non\-desired or non\-properly contextualized usage of legal binding issued Electronic Attestations of Attributes\.
- Secure presentation methods prevent credential tampering\. These methods ensure credentials remain reliable for verification\.
- Privacy\-preserving protocols prevent tracking of credential usage\. This protection ensures individual privacy while maintaining credential utility\.
- Cross\-border sharing supports educational and professional mobility\. This capability enables credential recognition across European borders\.

##### Verification

Authorized parties can verify credentials efficiently while respecting privacy:

- Direct verification confirms credential authenticity\. This process checks the issuing institution's authorization through official registries\.
- Status checking ensures current validity\. This verification confirms the credential has not been revoked or suspended\.
- Privacy\-preserving methods protect individual interests\. These methods prevent creation of usage traces while enabling legitimate verification\.
- Cross\-border verification supports mobility\. This capability enables credential recognition throughout Europe\.

#### 4\.2\.3 Status Management

Throughout the credential lifecycle, status management ensures current validity information remains available:

##### Active status

Credentials in active status indicate current validity:

- Regular confirmation maintains active status\. This process ensures credentials remain reliable for verification\.
- Automated monitoring identifies any issues requiring attention\. This surveillance supports early problem detection\.
- Status updates reflect any relevant changes\. These updates maintain credential reliability\.

##### Suspension

Temporary suspension may occur under specific circumstances:

- Clear procedures guide suspension decisions\. These procedures ensure fair and consistent handling of suspension cases\.
- Immediate status updates reflect suspension\. These updates prevent reliance on suspended credentials\.
- Defined processes govern reinstatement\. These processes ensure appropriate handling of suspension resolution\.

##### Revocation

Permanent revocation occurs in cases of serious issues:

- Strict protocols govern revocation decisions\. These protocols ensure appropriate use of revocation\.
- Immediate status updates reflect revocation\. These updates prevent continued use of revoked credentials\.
- Clear documentation supports revocation decisions\. This documentation maintains accountability for revocation actions\.

#### 4\.2\.4 Privacy protection

Privacy protection remains paramount throughout the credential lifecycle:

##### Data minimization

The framework implements data minimization principles:

- Only essential information appears in credentials\. This limitation protects individual privacy\.
- Selective disclosure enables controlled information sharing\. This capability gives individuals control over their data\.
- Privacy\-preserving verification prevents unnecessary data exposure\. These methods protect privacy during verification\.

##### Usage control

Credential holders maintain control over their information:

- Individual authorization required for sharing\. This requirement ensures controlled credential use\.
- No tracking of credential usage patterns\. This protection prevents creation of behaviour profiles\.
- Secure storage prevents unauthorized access\. This security protects credential confidentiality\.

#### 4\.2\.5 Cross\-border considerations

The credential lifecycle supports European mobility through:

##### Recognition support

The framework facilitates credential recognition across borders:

- Standardized formats support consistent interpretation\. These standards enable understanding across jurisdictions\.
- Clear status information supports recognition decisions\. This clarity facilitates cross\-border acceptance\.
- Efficient verification enables quick recognition\. This capability supports mobility and opportunity\.

##### Jurisdictional alignment

The framework maintains alignment with varying requirements:

- Respect for national education systems\. This consideration supports institutional autonomy\.
- Compliance with local regulations\. This alignment ensures legal operation across borders\.
- Support for multiple languages\. This capability enables broad understanding\.

#### 4\.2\.6 Quality assurance

Quality assurance throughout the lifecycle ensures:

##### Operational excellence

Continuous monitoring maintains high standards:

- Regular assessment of lifecycle processes\. These reviews ensure continued effectiveness\.
- Performance metrics track system operation\. These measurements support improvement efforts\.
- Stakeholder feedback informs enhancements\. This input ensures the system meets user needs\.

##### Compliance verification

Regular audits confirm framework adherence:

- Assessment of institutional practices\. These reviews ensure standard compliance\.
- Verification of privacy protection\. These checks confirm privacy safeguards\.
- Evaluation of security measures\. These assessments maintain system integrity\.

The credential lifecycle management system ensures reliable, efficient operation while protecting privacy and supporting mobility\. Through careful attention to each stage, the system maintains credential integrity while enabling legitimate use and verification\.

### <a id="_Toc182376679"></a><a id="_Toc184710026"></a>4\.3 Roles and responsibilities

#### 4\.3\.1 Overview

Within the non\-delegated trust framework, each participant holds specific responsibilities that support the integrity and efficiency of the credential ecosystem\. These roles reflect both the direct trust relationships and the need for clear accountability in credential management\. Understanding these roles and their interrelationships proves essential for effective framework operation\.

#### 4\.3\.2 Educational institutions

Universities and other educational institutions serve as primary credential issuers, maintaining direct responsibility for their credentials throughout their lifecycle\.

##### Core responsibilities

Educational institutions maintain comprehensive responsibility for credential management:

- They verify the completion of academic requirements and achievement of qualifications before issuing any credentials\. This verification ensures credentials accurately reflect educational accomplishments\.
- They maintain authoritative records of all issued credentials, including current status information\. This record\-keeping supports efficient verification while maintaining credential integrity\.
- They implement and manage status changes, including suspension or revocation when necessary\. This control ensures immediate response to any required credential status updates\.
- They protect the privacy of credential information while supporting legitimate verification needs\. This balance maintains individual rights while enabling necessary credential validation\.

##### Quality assurance

Institutions must maintain high standards in their credentialing processes:

- They establish and follow clear procedures for credential issuance and management\. These procedures ensure consistent, reliable credential handling\.
- They conduct regular internal audits of credentialing processes\. These reviews maintain operational excellence and identify improvement opportunities\.
- They participate in external quality assurance programs that validate their credentialing practices\. This participation ensures alignment with framework standards\.

##### Operational management

Daily operations require careful attention to several areas:

- They maintain secure systems for credential management that protect both institutional and individual interests\. These systems support efficient operations while ensuring security\.
- They train staff in proper credential handling procedures, including privacy protection requirements\. This training ensures consistent, appropriate credential management\.
- They respond promptly to verification requests while maintaining privacy protections\. This responsiveness supports credential utility while protecting individual rights\.

#### 4\.3\.3 Professional bodies

Professional organizations issuing qualifications and certifications maintain similar responsibilities to educational institutions, with additional focus on professional standards\.

##### Core responsibilities

Professional bodies maintain specific obligations:

- They verify professional qualifications and continuing education requirements before issuing credentials\. This verification ensures credentials reflect current professional standing\.
- They maintain current records of professional credentials and status information\. These records support verification of professional qualifications\.
- They manage credential status changes based on professional standing and conduct\. This management ensures credentials accurately reflect current professional status\.

##### Industry alignment

Professional bodies must maintain alignment with industry requirements:

- They ensure credentials reflect current professional standards and requirements\. This alignment maintains credential value for professional practice\.
- They coordinate with industry stakeholders to maintain relevant credentialing standards\. This coordination ensures credentials serve professional needs\.
- They adapt credentialing practices to evolving professional requirements\. This adaptation maintains credential utility over time\.

#### 4\.3\.4 Regulatory authorities

Regulatory bodies at national and European levels provide essential oversight and coordination\.

##### European level

European authorities maintain framework oversight:

- They establish and maintain framework standards that ensure consistent implementation across jurisdictions\. These standards support cross\-border credential recognition\.
- They monitor framework operation to ensure it serves European mobility objectives\. This monitoring supports continuous improvement\.
- They coordinate with national authorities to maintain framework alignment\. This coordination ensures consistent framework operation\.

##### National level

National authorities provide crucial coordination within their jurisdictions:

- They maintain registries of authorized credential issuers within their territory\. These registries support reliable verification of issuer authority\.
- They ensure alignment between framework implementation and national regulations\. This alignment prevents regulatory conflicts\.
- They support national institutions in framework adoption and operation\. This support facilitates effective implementation\.

#### 4\.3\.5 Credential holders

Individuals holding credentials maintain specific rights and responsibilities within the framework\.

##### Rights management

Credential holders maintain important rights:

- They control access to their credential information, determining when and how to share credentials\. This control protects individual privacy while enabling legitimate credential use\.
- They receive clear information about how their credentials function within the framework\. This information enables informed credential management\.
- They maintain the ability to present their credentials for verification throughout Europe\. This capability supports educational and professional mobility\.

##### Responsibilities

Credential holders must meet certain obligations:

- They maintain the security of their credential access mechanisms\. This security prevents unauthorized credential use\.
- They report any suspected unauthorized credential use promptly\. This reporting helps maintain system integrity\.
- They use their credentials in accordance with framework policies\. This compliance supports proper framework operation\.

#### 4\.3\.6 Verifying parties

Organizations verifying credentials must operate within framework requirements\.

##### Verification procedures

Verifiers follow established procedures:

- They confirm issuer authority through official registries before accepting credentials\. This verification ensures reliance on authorized credentials\.
- They check current credential status during verification\. This checking prevents reliance on invalid credentials\.
- They protect privacy during verification processes\. This protection prevents unauthorized tracking of credential use\.

##### Data protection

Verifiers maintain privacy protections:

- They collect only necessary information during verification processes\. This minimization protects individual privacy\.
- They maintain appropriate security for any retained verification records\. This security protects sensitive information\.
- They follow data retention policies that protect individual privacy\. These policies prevent unnecessary data accumulation\.

#### 4\.3\.7 Technology providers

Organizations providing technical solutions must support framework requirements while maintaining security and privacy\.

##### System requirements

Providers ensure their solutions:

- Support all required framework functions while maintaining security and privacy\. This support enables effective framework operation\.
- Implement privacy\-protecting features that prevent unauthorized tracking\. These features protect individual rights\.
- Maintain compatibility with framework standards that ensure interoperability\. This compatibility supports system\-wide operation\.

##### Service management

Providers maintain operational excellence:

- They ensure system reliability and availability that supports framework operation\. This reliability maintains system utility\.
- They provide necessary technical support to framework participants\. This support enables effective system use\.
- They maintain security measures that protect framework operation\. These measures prevent system compromise\.

#### 4\.3\.8 Collaborative responsibilities

All participants share certain responsibilities:

##### Framework support

Shared obligations include:

- Contributing to framework improvement through feedback and suggestions\. This contribution supports continuous enhancement\.
- Reporting security or operational issues promptly\. This reporting enables quick problem resolution\.
- Maintaining awareness of framework updates and requirements\. This awareness ensures continued effective operation\.

##### Privacy protection

All parties must:

- Implement required privacy protection measures\. These measures protect individual rights\.
- Follow data minimization principles in their operations\. This practice prevents unnecessary data collection\.
- Maintain appropriate security for framework\-related information\. This security protects system integrity\.

Through clear definition and execution of these roles and responsibilities, the framework maintains efficient operation while protecting all participants' interests\. This clarity supports effective credential management while enabling educational and professional mobility across Europe\.

### <a id="_Toc182376680"></a><a id="_Toc184710027"></a>4\.4 Compliance and monitoring framework

#### 4\.4\.1 Overview

The compliance and monitoring framework ensures the integrity, security, and effectiveness of credential management across Europe\. Operating within the non\-delegated trust model, this framework establishes mechanisms for maintaining high standards while respecting institutional autonomy and protecting individual privacy\.

#### 4\.4\.2 Regulatory compliance

##### European level requirements

The framework ensures alignment with key European regulations:

- eIDAS Regulation requirements shape credential trust services and electronic identification\. This alignment ensures legal recognition of credentials across member states and establishes clear requirements for qualified and non\-qualified trust services in educational credentialing\.
- General Data Protection Regulation \(GDPR\) principles govern all personal data handling within the framework\. Educational institutions and professional bodies must implement privacy by design, maintain clear legal bases for data processing, and ensure individual rights protection throughout the credential lifecycle\.
- Single Digital Gateway Regulation supports efficient cross\-border credential recognition\. The framework enables once\-only submission of credentials while maintaining privacy and security requirements\.

##### National level requirements

Framework implementation must accommodate national regulations:

- National education laws and professional qualification requirements guide credential issuance and recognition\. This alignment ensures credentials meet local legal and regulatory standards\.
- Data protection regulations at national level complement European requirements\. Implementation must satisfy both European and national privacy protection standards\.
- Professional practice regulations influence credential management for regulated professions\. The framework supports specific requirements for professional credential verification and status management\.

#### 4\.4\.3 Standards compliance

##### Operational standards

The framework establishes clear operational requirements:

- Quality assurance standards ensure consistent credential management across institutions\. These standards cover issuance, verification, and status management processes\.
- Security standards protect credential integrity and system operation\. These requirements ensure appropriate protection for credential information and operations\.
- Privacy standards maintain individual rights protection throughout credential processes\. These standards ensure privacy\-preserving operation at all stages\.

##### Implementation standards

Participating organizations must meet specific standards:

- Technical infrastructure requirements ensure reliable system operation\. These standards support secure, efficient credential management\.
- Process requirements establish consistent operational practices\. These standards ensure reliable credential handling across organizations\.
- Staff qualification requirements ensure proper system operation\. These standards maintain operational quality through appropriate training\.

#### 4\.4\.4 Monitoring framework

##### Continuous monitoring

Regular monitoring ensures framework effectiveness:

- Regular system checks ensure smooth operations\. These checks help identify and resolve potential problems before they impact service delivery\.
- Regular compliance checks verify adherence to framework requirements\. These checks maintain high operational standards across participating organizations\.
- Performance metrics track framework effectiveness\. These measurements support continuous improvement efforts\.

##### Audit programs

Comprehensive auditing ensures framework integrity:

- Regular internal audits verify organizational compliance\. These reviews ensure consistent adherence to framework requirements\.
- External audits provide independent verification of framework operation\. These assessments validate framework effectiveness\.
- Specialized audits address specific aspects of framework operation\. These reviews ensure thorough evaluation of critical functions\.

#### 4\.4\.5 Quality management

##### Process management

Quality management ensures consistent, reliable operation:

- Documented procedures guide all framework operations\. These procedures ensure consistent handling of credentials and related processes\.
- Change management processes control system evolution\. These processes ensure orderly implementation of necessary changes\.
- Incident management procedures address operational issues\. These procedures ensure appropriate handling of any problems\.

##### Performance management

Regular assessment maintains operational excellence:

- Performance indicators track system effectiveness\. These metrics enable objective evaluation of framework operation\.
- User satisfaction monitoring ensures framework utility\. This feedback helps identify improvement opportunities\.
- Operational efficiency assessment supports optimization\. These evaluations help enhance framework operation\.

#### 4\.4\.6 Risk management

##### Risk Assessment

Continuous risk evaluation protects framework operation:

- Regular risk assessments identify potential threats\. These evaluations ensure comprehensive risk awareness\.
- Impact analysis determines potential consequence severity\. This analysis supports appropriate risk mitigation\.
- Mitigation planning addresses identified risks\. These plans ensure appropriate risk management\.

##### Security management

Comprehensive security measures protect framework operation:

- Access control systems protect credential operations\. These controls prevent unauthorized system access\.
- Encryption protects credential information\. These measures ensure data confidentiality\.
- Security monitoring identifies potential threats\. This surveillance enables quick response to security issues\.

#### 4\.4\.7 Incident management

##### Response procedures

Clear procedures guide incident handling:

- Incident classification determines appropriate responses\. This classification ensures proper handling of different issue types\.
- Response protocols guide incident management\. These protocols ensure appropriate incident handling\.
- Escalation procedures address serious issues\. These procedures ensure proper handling of significant problems\.

##### Recovery processes

Framework resilience requires robust recovery capabilities:

- Business continuity plans ensure continued operation\. These plans maintain essential services during disruptions\.
- Disaster recovery procedures address serious incidents\. These procedures enable system recovery after significant issues\.
- Service restoration priorities guide recovery efforts\. These priorities ensure appropriate focus during system restoration\.

#### 4\.4\.8 Improvement framework

##### Continuous improvement

Regular enhancement maintains framework effectiveness:

- Performance analysis identifies improvement opportunities\. This analysis supports systematic enhancement\.
- Stakeholder feedback informs improvement efforts\. This input ensures changes address actual needs\.
- Implementation planning guides enhancement efforts\. These plans ensure effective improvement implementation\.

##### Innovation management

Framework evolution requires managed innovation:

- Technology assessment evaluates new capabilities\. This evaluation identifies valuable innovations\.
- Pilot programs test new features\. These tests ensure proper operation before full implementation\.
- Staged rollout manages implementation risk\. This approach ensures controlled introduction of changes\.

#### 4\.4\.9 Reporting framework

##### Regular Reporting

Systematic reporting maintains transparency:

- Performance reports track system operation\. These reports provide clear operational visibility\.
- Compliance reports verify requirement adherence\. These reports document framework compliance\.
- Incident reports document operational issues\. These reports ensure proper incident documentation\.

##### Stakeholder communication

Clear communication supports framework operation:

- Status updates inform stakeholders of system operation\. These updates maintain operational awareness\.
- Change notifications announce system modifications\. These notifications ensure stakeholder awareness of changes\.
- Issue alerts communicate operational problems\. These alerts ensure appropriate awareness of issues\.

This comprehensive compliance and monitoring framework ensures reliable, efficient credential management while protecting all participants' interests\. Through systematic oversight and continuous improvement, the framework maintains high operational standards while supporting educational and professional mobility across Europe\.

### <a id="_Toc182376681"></a><a id="_Toc184710028"></a>4\.5 Infrastructure requirements

#### 4\.5\.1 Overview

The infrastructure supporting educational and professional credentials must provide secure, reliable, and efficient operations while protecting privacy and supporting institutional autonomy\. These requirements define the essential capabilities needed to support the trust framework's operations without prescribing specific technical implementations\.

#### 4\.5\.2 Core infrastructure components

##### Trust list infrastructure

The framework requires authoritative information about participating organizations:

- A list of authorized credential issuers must maintain current information about educational institutions and professional bodies authorized to issue credentials\. This list enables reliable verification of issuer authority while supporting institutional autonomy\.
- Status information for authorized issuers must remain current and readily accessible\. This availability ensures verifiers can confirm issuer authority during credential verification\.
- Regular updates must maintain list accuracy as institutional status changes\. This maintenance ensures reliable issuer verification throughout the framework\.

##### Credential management infrastructure

Institutions require robust systems for credential operations:

- Credential issuance capabilities must support secure creation and delivery of credentials to recipients\. These capabilities ensure reliable credential distribution while maintaining security\.
- Status management systems must enable immediate updates to credential validity information\. This immediacy ensures current information availability for verification processes\.
- Revocation mechanisms must support immediate invalidation of credentials when necessary\. This capability ensures proper control over credential validity\.

##### Privacy protection infrastructure

Privacy protection requires specific capabilities:

- Selective disclosure mechanisms must enable credential holders to share only necessary information\. Issuers disclosures' policies shall be considered, as EAA's become legal binding documents issued and to be used under specific scopes\. This control protects privacy while enabling legitimate credential use\.
- Data minimization tools must support privacy\-preserving credential operations\. These tools ensure appropriate privacy protection throughout credential processes\.
- Consent management systems must maintain individual control over credential sharing\. These systems protect individual rights while enabling necessary credential verification\.

#### 4\.5\.3 Operational requirements

##### Availability requirements

Infrastructure must maintain reliable operation:

- High availability systems must support continuous credential operations\. This reliability ensures framework utility for all participants\.
- Disaster recovery capabilities must protect against service interruption\. These capabilities ensure framework resilience\.
- Load management systems must handle peak processing requirements\. This capacity ensures reliable operation under all conditions\.

##### Performance requirements

Infrastructure must maintain efficient operation:

- Response time requirements ensure quick system operation\. This performance supports efficient credential processes\.
- Throughput capabilities must handle expected transaction volumes\. This capacity ensures reliable framework operation\.
- Scalability features must accommodate growing system usage\. This flexibility supports framework evolution\.

##### Security requirements

Infrastructure must protect framework operation:

- Security measures ensure only authorized users can access the system\. These measures protect the credibility of all credentials issued\.
- The system keeps detailed records of all activities\. These records help maintain transparency and accountability\.
- Encryption must protect credential information throughout its lifecycle\. This protection ensures data confidentiality\.

#### 4\.5\.4 Integration requirements

##### Internal integration

Systems must support institutional operations:

- Integration with academic management systems must support efficient credential issuance\. This integration streamlines institutional processes\.
- Connection to professional qualification systems must enable efficient credential management\. This capability supports professional credentialing processes\.
- Links to administrative systems must support operational management\. These connections enable efficient framework operation\.

##### External integration

Systems must support cross\-border operations:

- Integration with European\-level systems must support credential recognition\. These connections enable cross\-border mobility\.
- Links to national systems must support local operations\. These connections enable framework operation within national contexts\.
- Professional body connections must support qualification verification\. These links enable professional credential verification\.

#### 4\.5\.5 Data management requirements

##### Data storage

Infrastructure must support appropriate data management:

- Storage systems must maintain credential information securely\. This security protects sensitive data\.
- Archive capabilities must preserve historical information appropriately\. These capabilities support long\-term credential validity\.
- Backup systems must protect against data loss\. This protection ensures operational continuity\.

##### Data protection

Infrastructure must ensure appropriate data security:

- Access controls must protect stored information\. These controls prevent unauthorized data access\.
- Encryption must protect sensitive information\. This protection ensures data confidentiality\.
- Monitoring must identify potential security issues\. This surveillance enables quick response to threats\.

#### 4\.5\.6 Support requirements

##### Operational support

Infrastructure must include support capabilities:

- Help desk systems must support framework participants\. This support ensures effective framework use\.
- Problem management capabilities must address operational issues\. These capabilities ensure reliable framework operation\.
- Change management systems must control framework evolution\. These systems ensure orderly implementation of changes\.

##### User support

Infrastructure must support framework participants:

- User assistance systems must help credential holders manage their credentials\. This support ensures effective credential use\.
- Verifier support must enable efficient credential verification\. This assistance ensures proper credential verification\.
- Issuer support must enable effective credential management\. This support ensures proper credential handling\.

#### 4\.5\.7 Quality assurance requirements

##### Monitoring capabilities

Infrastructure must support quality management:

- Performance monitoring must track system operation\. This monitoring ensures framework effectiveness\.
- Compliance checking must verify framework adherence\. These checks maintain operational standards\.
- Security monitoring must identify potential threats\. This surveillance protects framework operation\.

##### Testing capabilities

Infrastructure must support quality maintenance:

- Test environments must support feature validation\. These environments ensure proper system operation\.
- Integration testing must verify system interactions\. These tests ensure reliable framework operation\.
- Security testing must verify protection measures\. These tests ensure appropriate security maintenance\.

#### 4\.5\.8 Evolution requirements

##### Adaptability

Infrastructure must support framework evolution:

- Flexible architecture must accommodate changing requirements\. This flexibility ensures framework sustainability\.
- Modular design must enable component updates\. This modularity supports framework evolution\.
- Extensible capabilities must support new features\. This extensibility enables framework enhancement\.

##### Innovation support

Infrastructure must enable framework advancement:

- Pilot program support must enable new feature testing\. This capability ensures proper feature validation\.
- Evaluation environments must support innovation assessment\. These environments enable feature testing\.
- Staged deployment capabilities must support controlled implementation\. These capabilities ensure orderly framework evolution\.

These requirements align with the technical framework detailed in Chapter 8 and support the use cases presented in Chapter 7\.

This infrastructure framework establishes essential capabilities while maintaining implementation flexibility\. By focusing on required capabilities rather than specific technologies, it enables effective credential management while supporting framework evolution and institutional autonomy\.

### <a id="_Toc182376682"></a><a id="_Toc184710029"></a>4\.6 Benefits of the operational model

#### 4\.6\.1 Overview

The operational model offers significant advantages for the European education and professional qualification landscape\. These benefits are derived from the non\-delegated trust model, an inclusive governance structure, and a privacy\-respecting approach to credential management\. By addressing the challenges of fragmented systems and cross\-border recognition, the model supports seamless mobility and trust within the EU\. This section outlines the benefits tailored to different stakeholder groups and the alignment with European objectives for educational and professional mobility\.

#### 4\.6\.2 Strategic value

1. Enhanced trust in qualifications

- Secure, verifiable credentials that ensure authenticity across EU borders\.
- Standardised digital verification provides a reliable framework for recognising qualifications, reducing confusion and disputes\.
- Verification directly from authorised institutions eliminates the need for third\-party intermediaries, simplifying processes and ensuring accuracy\.
- Cryptographic security safeguards credentials from tampering, reinforcing the trustworthiness of educational and professional records\. For example, universities issuing digitally verifiable diplomas can assure employers of their legitimacy\.

1. Improved Educational and Professional mobility

- Streamlined qualification recognition ensures that students and professionals can easily present and have their credentials recognised throughout EU member states\.
- Accelerated verification processes support faster admissions, job applications, and licensing, enhancing opportunities for individuals\.
- Lower barriers to cross\-border education and employment foster an environment where skills and knowledge transfer seamlessly\.
- Enhanced portability of qualifications and certifications simplifies transitions, such as a nurse from Spain being able to quickly present verified credentials when applying to work in Germany\.

1. Support for lifelong learning

- Digital records that include both traditional and non\-traditional credentials create a comprehensive, accessible repository for lifelong learning achievements\.
- Integration of micro\-credentials allows for recognition of smaller, modular learning experiences that contribute to professional growth\.
- Recognising informal learning and additional certifications helps individuals maintain continuous career development and adaptability in changing job markets\.
- For example, professionals who earn new skills through workshops or online courses can have these micro\-credentials verified alongside formal education\.

#### 4\.6\.3 Operational excellence

1. Administrative efficiency

- Significant reduction in manual verification processes frees up resources and reduces processing times, enabling institutions to focus on strategic tasks\.
- Automated credential validation and issuance lead to more streamlined workflows and reduced risk of errors\.
- Digital processes lower operational costs by eliminating redundant paperwork and manual record\-keeping\.
- For example, universities can streamline admissions by automating the validation of incoming students’ credentials, reducing administrative workloads\.

1. Enhanced security and fraud prevention

- Cryptographically secured credentials ensure tamper\-proof records, building trust in the validity of shared information\.
- Clear audit trails for all credential actions provide transparency and accountability\.
- Immediate status verification capabilities enable quick identification of suspended or revoked credentials, preventing fraudulent use\.
- Selective disclosure ensures individuals share only necessary information, protecting personal data and enhancing privacy\.

1. Optimised resource utilisation

- Reduced time spent on routine verification tasks allows staff to focus on core educational missions and strategic initiatives\.
- Improved allocation of resources results in better service delivery and enhanced data management capabilities\.
- Digital systems facilitate comprehensive data analytics, supporting informed decision\-making and policy planning\.
- Compliance and reporting processes become more straightforward, saving institutions time and effort\.

#### 4\.6\.4 Stakeholder benefits

1. Educational institutions

- Institutional autonomy: Full control over credential issuance and management aligns with existing practices, enabling customisation according to institutional policies\. The ability to implement the model according to unique needs preserves the institution’s identity and credibility\.
- Operational efficiency: Automated processes reduce administrative overhead, allowing staff to allocate more resources to student\-focused services\. Improved data management supports efficient and secure handling of academic records\.
- Enhanced service quality: Faster credential processing ensures better service for students and external partners\. Institutions can foster better international collaboration by ensuring that their issued credentials are easily verifiable and recognisable abroad\.

1. Professional Bodies

- Enhanced oversight:  Reliable systems allow professional bodies to monitor and verify the credentials of their members, ensuring adherence to quality standards\. Enhanced tracking of ongoing professional development maintains a high level of competency within regulated fields\.
- Efficient operations: Automation in verification processes reduces administrative tasks, streamlining membership and licensing\. Cost\-effective operations support long\-term sustainability\.
- International recognition: Simplified cross\-border recognition processes enhance professional mobility, making it easier for professionals to practise in different EU countries\. For example, an engineer certified in Italy can seamlessly present credentials for recognition in other member states\.

1. Individuals

- Enhanced control:  Individuals manage their personal credentials securely and share them as needed, protecting their privacy through selective data disclosure\.  The model ensures that users remain in charge of their data, with the flexibility to present credentials in various contexts\.
- Simplified processes: Easy access and sharing of verified credentials reduce time spent on application procedures\. Faster application and enrolment processes enable students and professionals to focus on their growth without bureaucratic delays\.
- Improved opportunities: Broader access to education and employment opportunities is facilitated by the ease of verifying credentials across borders\. Clearer career development paths encourage lifelong learning and professional advancement\.

1. Society

- Increased access to education: Lower barriers make education more accessible, supporting inclusion and lifelong learning\. Efficient qualification recognition promotes a fairer system where skills and knowledge are valued consistently\.
- Workforce mobility: Simplified professional qualification verification supports free movement, allowing talent to flow where it is needed most\. Skills recognition boosts employability and matches labour market demands\.
- Economic efficiency: Cost savings through streamlined verification processes benefit not only institutions but the broader economy\. Better skills matching ensures more effective workforce development, driving economic growth\.

#### 4\.6\.5 Implementation Benefits

1. Technical integration

- Seamless integration with existing digital infrastructure reduces the burden of adoption\.
- Standardised interfaces make connecting systems simpler, facilitating interoperability\.
- Flexible implementation options allow stakeholders to adapt the model to their specific needs\.
- Future\-proof architecture ensures compatibility with new technological advancements, supporting continuous improvement\.

1. Compliance and governance

- Adherence to EU regulatory standards ensures alignment with legal and privacy obligations\.
- Strong data protection measures maintain user trust\.
- Transparent governance models foster accountability, providing clear mechanisms for oversight and trust\.

1. Support for evolution

- Adaptability to emerging credential types and evolving requirements ensures that the system can grow with new educational trends\.
- Continuous improvement frameworks encourage ongoing innovation and system optimisation\.
- For example, as new types of digital learning experiences develop, the system can accommodate and certify these credentials efficiently\.

The operational model, with its well\-defined benefits for all stakeholders, advances the EU’s objectives for educational and professional mobility, while upholding high standards of privacy and security\. By maintaining context and illustrating practical applications, stakeholders can better appreciate the value this model brings in supporting trust, efficiency, and transparency\.