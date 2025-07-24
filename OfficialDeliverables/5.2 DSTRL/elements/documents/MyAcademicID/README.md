# MyAcademicID Implementation in DC4EU Pilot2: A Comprehensive Analysis of Federation-Based Digital Identity and Hybrid Trust Architecture

## Executive Summary

The Digital Student Record Library (DSTRL) presents a transformative approach to academic credential management through the implementation of MyAcademicID within the DC4EU (Digital Credentials for Europe) framework. This chapter examines the comprehensive implementation of MyAcademicID in Pilot2, demonstrating how federation-based digital identity systems can be successfully integrated with hybrid trust architectures to address the complex governance requirements of European higher education.

MyAcademicID represents a standardised digital identity credential specifically designed for academic and research communities, enabling seamless mobility across European educational institutions whilst maintaining the highest standards of security, privacy, and interoperability. The implementation within DC4EU Pilot2 showcases an innovative hybrid trust model that combines traditional Public Key Infrastructure (PKI) with decentralised trust mechanisms through the European Blockchain Services Infrastructure (EBSI), creating a robust framework for verifiable academic credentials.

## 1. Introduction: The Evolution of Academic Identity Management

### 1.1 Context and Rationale

The European higher education landscape has undergone significant transformation in recent decades, with increasing emphasis on student mobility, cross-border recognition of qualifications, and the creation of a unified European Education Area. Traditional paper-based credential systems have proven inadequate for supporting these ambitious goals, leading to the development of digital credential frameworks that can provide secure, verifiable, and interoperable academic identity solutions.

MyAcademicID emerges as a critical component of this digital transformation, addressing the fundamental challenge of creating persistent, verifiable academic identities that can be recognised across institutional and national boundaries. The implementation within DC4EU Pilot2 represents a pioneering effort to establish a comprehensive digital credential ecosystem that supports the complex governance structures inherent in European higher education.

### 1.2 The Federation Model Foundation

The current functioning of MyAcademicID is built upon a sophisticated federation model that reflects the hierarchical and distributed nature of European educational governance. This model recognises that academic credential management cannot be centralised under a single authority, but must instead accommodate the diverse regulatory, institutional, and national frameworks that characterise European higher education.

The federation approach enables multiple stakeholders to participate in the credential ecosystem whilst maintaining their autonomy and regulatory compliance. Universities, National Research and Education Networks (NRENs), quality assurance agencies, and professional bodies can all participate in the MyAcademicID ecosystem through clearly defined roles and responsibilities, creating a comprehensive trust network that supports academic mobility and credential recognition.

## 2. MyAcademicID Data Model and Technical Architecture

### 2.1 Core Data Structure

The MyAcademicID data model implements a sophisticated schema designed specifically for academic identity management across European educational institutions. The model incorporates the eduPerson standard attributes and the European Student Identifier (ESI) framework, making it particularly valuable for academic mobility and cross-institutional identity management.

The credential structure follows the W3C Verifiable Credentials Data Model, ensuring interoperability with emerging digital identity standards whilst maintaining compatibility with existing educational directory services. The schema defines a comprehensive set of attributes that capture both personal information and academic affiliations, creating a complete digital identity profile for students, faculty, and researchers.

#### Mandatory Attributes

The MyAcademicID schema defines seven mandatory attributes that form the core of every credential:

| Attribute | Description | Format | OID Reference |
|-----------|-------------|--------|--------------|
| `id` | Unique identifier of the credential subject (typically a DID) | String | N/A |
| `communityUserIdentifier` | Opaque and non-revocable identifier following eduPersonUniqueId syntax | String | 1.3.6.1.4.1.5923.1.1.1.13 |
| `displayName` | User's full name (firstname lastname) | String | 2.16.840.1.113730.3.1.241 |
| `givenName` | Part of person's name that is not their surname | String | 2.5.4 |
| `familyName` | Person's surname | String | 2.5.4.4 |
| `emailAddress` | Email address of the user | String (email format) | 0.9.2342.19200300.100.1.3 |
| `assurance` | Identity assurance level following REFEDS Assurance Framework | Array of URI strings | 1.3.6.1.4.1.5923.1.1.1.11 |

#### Optional Attributes for Enhanced Functionality

The schema also supports optional attributes that provide additional academic context:

**Academic Identification:**
- `europeanStudentIdentifier`: European Student Identifier (ESI) ensuring mobility across institutions
- `organization`: Organization description of the user

**Affiliations and Entitlements:**
- `externalAffiliation`: Affiliations within home organisations following eduPersonScopedAffiliation syntax
- `entitlements`: User's rights and privileges within academic systems

#### Community User Identifier Structure

The `communityUserIdentifier` represents a critical innovation in academic identity management. This identifier:
- Follows the syntax of eduPersonUniqueId attribute: `uniqueID@erasmus.eduteams.org`
- Contains up to 64 hexadecimal digits in the uniqueID portion
- Provides persistent, unique identification within the MyAcademicID namespace
- Enables reliable identity matching across institutional boundaries
- Remains stable throughout the user's academic career

#### Example Credential Structure

```json
{
  "credentialSubject": {
    "id": "did:ebsi:zd6NuZy9JfQV4SeYd3P3L7",
    "communityUserIdentifier": "a2b1c5d8e3f7@erasmus.eduteams.org",
    "europeanStudentIdentifier": ["esi:eac-rew:fr:78e7t6y5432@univ-paris1.fr"],
    "externalAffiliation": ["student@univ-paris1.fr", "member@univ-paris1.fr"],
    "organization": "Université Paris 1 Panthéon-Sorbonne",
    "displayName": "Sophie Martin",
    "givenName": "Sophie",
    "familyName": "Martin",
    "emailAddress": "sophie.martin@student.univ-paris1.fr",
    "entitlements": ["urn:mace:egi.eu:group:vo.geant.org:role=member"],
    "assurance": ["https://refeds.org/assurance/IAP/low", "https://refeds.org/assurance/ATP/ePA-1m"]
  }
}
```

### 2.2 European Student Identifier Integration

A particularly innovative aspect of the MyAcademicID implementation is the integration of the European Student Identifier (ESI) framework. The ESI provides a standardised mechanism for identifying students across European higher education institutions, supporting the goals of the European Education Area and facilitating automatic recognition of learning outcomes.

The MyAcademicID schema includes dedicated support for ESI through the europeanStudentIdentifier attribute, which contains an array of ESI values supporting student mobility across institutions. This integration enables students to maintain persistent identity across multiple educational experiences, from undergraduate studies through doctoral research and continuing professional development.

The ESI implementation within MyAcademicID addresses the technical challenges of cross-border student identification whilst respecting the privacy and data protection requirements of the General Data Protection Regulation (GDPR). Students can selectively disclose their ESI information to authorised institutions and services, maintaining control over their personal data whilst enabling seamless academic mobility.

### 2.3 Assurance Framework Integration

The MyAcademicID implementation incorporates comprehensive support for the REFEDS Assurance Framework (RAF), providing standardised mechanisms for expressing identity assurance levels. The assurance attribute contains an array of URIs representing different levels of identity verification, enabling relying parties to make informed decisions about the trustworthiness of presented credentials.

This assurance framework integration is particularly important for cross-border academic interactions, where institutions need to understand the level of identity verification performed by credential issuers. The standardised assurance levels enable automated processing of identity verification requirements whilst maintaining the flexibility necessary for diverse institutional policies and regulatory frameworks.

## 3. Federation-Based Governance Architecture

### 3.1 The Multi-Tiered Trust Model

The MyAcademicID implementation operates within a sophisticated multi-tiered trust model that reflects the hierarchical nature of European educational governance. This model enables the delegation of authority from European-level organisations through national entities to individual institutions, creating a comprehensive trust network that supports both institutional autonomy and cross-border interoperability.

The authorisation model ensures that relying parties (verifiers) can determine the legitimacy of an issuer of verifiable credentials, as well as the authorisation chain that validates the issuer. This structured framework manages authorisations, accreditation, and recognition within educational domains whilst facilitating verification and traceability of authorisations over time.

#### Trust Hierarchy Structure

The model consists of three primary tiers:

1. **Root Trusted Accreditation Organisation (RootTAO)**: At the European level, GÉANT serves as the foundational trust anchor, providing the ultimate source of authority for the MyAcademicID ecosystem.

2. **Trusted Accreditation Organisations (TAOs)**: National Research and Education Networks (NRENs) operate at the national level, accredited by GÉANT and responsible for authorising institutions within their respective countries.

3. **Credential Issuers**: Universities and higher education institutions serve as the primary issuers of MyAcademicID credentials, authorised through their national NREN relationships.

#### Electronic Attestations of Attributes (EAAs)

The authorisation framework utilises Electronic Attestations of Attributes (EAAs) to establish and verify institutional authority. Each EAA contains essential authorisation information:

| Attribute | Description |
|-----------|-------------|
| Authorisation ID | Unique identifier for the specific authorisation |
| Granter ID | Entity issuing the authorisation (e.g., GÉANT, NREN) |
| Grantee ID | Entity receiving the authorisation (e.g., University) |
| Type of EAA | Scope of authorisation (e.g., MyAcademicIDIssuer) |
| Jurisdictional limitations | Geographic or regulatory constraints |
| Issuance date | When the authorisation becomes valid |
| Validity date | Expiration date (if applicable) |
| Evidence | Legal or regulatory proof supporting the authorisation |

#### Verification Process

Verifiers must follow a structured process to ensure the validity of authorisations:

1. **Integrity check**: Ensures data has not been modified and maintains cryptographic proof
2. **Issuer recognition**: Confirms the granter is legally authorised to issue the specific authorisation
3. **Status verification**: Checks if the authorisation is still valid and not revoked or suspended
4. **Jurisdiction & usage compliance**: Verifies geographical or regulatory constraints
5. **Trust anchor resolution**: Establishes confidence in the entire authorisation chain by validating trust anchors

#### Example: Spanish Implementation

In Spain, the authorisation chain for MyAcademicID operates as follows:

- **RootTAO**: GÉANT (European level)
- **TAO**: RedIRIS (Spanish National Research and Education Network)
- **Grantee**: Rovira i Virgili University (URV)
- **Type of EAA**: Authority to issue MyAcademicID credentials
- **Jurisdictional limitations**: Spain
- **Evidence**: Membership in the NREN federation and compliance with eduGAIN rules

This hierarchical structure ensures that URV can demonstrate its authority to issue MyAcademicID credentials through a verifiable chain of trust that extends from the European level through national coordination to institutional implementation.

### 3.2 National Research and Education Networks as TAOs

National Research and Education Networks (NRENs) play a crucial role in the MyAcademicID ecosystem, serving as Trusted Accreditation Organisations (TAOs) at the national level. Examples include RedIRIS in Spain, RENATER in France, JANET in the United Kingdom, and DFN in Germany. These organisations are accredited by GÉANT and, in turn, accredit universities and other higher education institutions within their respective countries.

#### NREN Authorisation Examples

**Spain - RedIRIS Implementation:**
- **Granter**: GÉANT (European RootTAO)
- **Grantee**: RedIRIS (Spanish NREN)
- **Type of EAA**: Authority to accredit MyAcademicID issuers
- **Jurisdictional limitations**: Spain
- **Evidence**: Membership in GÉANT federation and compliance with eduGAIN standards

**France - RENATER Dual Role:**
- **Granter**: GÉANT (European RootTAO)
- **Grantee**: RENATER (French NREN)
- **Type of EAA**: Authority to both accredit and issue MyAcademicID credentials
- **Jurisdictional limitations**: France
- **Evidence**: National mandate for educational network coordination

#### NREN Advantages and Capabilities

The NREN model provides several advantages for MyAcademicID implementation:

- **Established relationships** with higher education institutions in their countries
- **Comprehensive understanding** of national regulatory requirements
- **Technical expertise** in identity federation and network security
- **Existing infrastructure** for supporting cross-border academic collaboration
- **Compliance monitoring** capabilities for ongoing quality assurance

The role of NRENs extends beyond simple accreditation to include ongoing support for credential management, compliance monitoring, and technical integration. NRENs provide the critical link between European-level coordination and national implementation, ensuring that MyAcademicID deployment respects national sovereignty whilst enabling European-wide interoperability.

### 3.3 Universities as Trusted Issuers

Universities and other higher education institutions serve as the primary issuers of MyAcademicID credentials, either directly or through their NREN federation relationships. This distributed issuance model ensures that institutions maintain control over their student and faculty credentials whilst participating in the broader European academic identity ecosystem.

#### University Authorisation Framework

Universities must demonstrate their authority to issue MyAcademicID credentials through verifiable Electronic Attestations of Attributes (EAAs). A typical university authorisation includes:

**Example: Rovira i Virgili University (URV)**
- **Granter**: RedIRIS (Spanish NREN as TAO)
- **Grantee**: Rovira i Virgili University
- **Type of EAA**: MyAcademicIDIssuer authority
- **Jurisdictional limitations**: Spain (with European recognition)
- **Evidence**: University recognition by Ministry of Universities and NREN membership

#### Institutional Integration Requirements

The university-level implementation of MyAcademicID requires careful integration with existing institutional systems:

**Technical Integration:**
- Student information systems for credential data sources
- Human resources databases for faculty and staff credentials
- Identity management infrastructure for authentication
- Academic service platforms for credential usage

**Governance Compliance:**
- Demonstration of authority through verifiable authorisation chains
- Compliance with national higher education regulations
- Adherence to GÉANT governance policies
- Integration with NREN federation requirements

#### Multi-Institutional Scenarios

Universities may participate in multiple authorisation contexts:

**European University Alliances:**
- Universities within European University Alliances can issue AllianceID credentials
- These credentials are governed by alliance statutes rather than NREN involvement
- Enable access to joint services, virtual campuses, and mobility platforms

**Cross-Border Programmes:**
- Universities participating in joint degree programmes may require multiple authorisations
- Credentials may need recognition across multiple national frameworks
- Require coordination between multiple NRENs and national authorities

### 3.4 Dual Role Implementation: TAO and TI

In certain countries, NRENs perform a dual role as both Trusted Accreditation Organisations (TAOs) and Trusted Issuers (TIs). This dual role arrangement recognises the varying national contexts and regulatory frameworks across Europe whilst maintaining the integrity of the overall trust model.

#### Implementation Models

**France - RENATER Dual Role:**
- **Primary Function**: RENATER serves as both TAO and MyAcademicID issuer
- **Rationale**: Centralised nature of French higher education system
- **Benefits**: Standardised credential issuance and streamlined compliance
- **Governance**: Direct relationship with GÉANT whilst maintaining institutional autonomy

**Spain - Distributed Model:**
- **Primary Function**: RedIRIS serves as TAO, universities as issuers
- **Rationale**: Institutional autonomy and distributed governance preference
- **Benefits**: Direct institutional control over credential issuance
- **Governance**: Two-tier authorisation structure with clear accountability

#### Advantages of Dual Role Arrangements

Countries where NRENs serve in dual capacity typically benefit from:

**Operational Efficiency:**
- Reduced complexity in authorisation chains
- Streamlined compliance monitoring
- Unified technical infrastructure
- Consistent policy implementation

**Quality Assurance:**
- Centralised standards enforcement
- Uniform credential quality
- Comprehensive audit capabilities
- Simplified dispute resolution

**Technical Integration:**
- Standardised interfaces and protocols
- Unified key management systems
- Consistent cryptographic standards
- Streamlined upgrade processes

#### Regulatory Considerations

The dual role implementation must address several regulatory requirements:

**National Compliance:**
- Adherence to national higher education legislation
- Compliance with data protection regulations
- Integration with national quality assurance frameworks
- Respect for institutional academic freedom

**European Interoperability:**
- Compliance with GÉANT governance policies
- Integration with European trust frameworks
- Support for cross-border credential recognition
- Adherence to European data protection standards

This flexible approach ensures that MyAcademicID can accommodate diverse national governance structures whilst maintaining the consistency necessary for European-wide interoperability and recognition.

## 4. DC4EU Pilot2 Implementation: Technical Innovation and Governance Integration

### 4.1 The Hybrid Trust Model

The implementation of MyAcademicID within DC4EU Pilot2 represents a significant advancement in digital credential technology through the introduction of a hybrid trust model that combines traditional Public Key Infrastructure (PKI) with decentralised trust mechanisms. This hybrid approach addresses the fundamental limitations of classical PKI in educational governance whilst maintaining compatibility with existing infrastructure and regulatory requirements.

The hybrid trust model enables verification of not only **who** an entity is (traditional PKI functionality) but also **what they are authorised to do** (decentralised governance capabilities). This dual verification capability is essential for educational credential management, where institutions need to demonstrate specific authorisations to issue particular types of credentials or access certain services.

### 4.2 EBSI Integration and Multi-Level Governance Support

The European Blockchain Services Infrastructure (EBSI) plays a crucial role in the Pilot2 implementation, providing the decentralised trust foundation necessary for advanced credential governance. A fundamental innovation of the Pilot2 model is its ability to support multiple governance levels simultaneously through unified Verifiable Data Registries, creating unprecedented flexibility and simplification in verification processes.

#### Multi-Level Governance Architecture

The EBSI-based Verifiable Data Registries in Pilot2 are designed to accommodate three distinct governance levels within a single, cohesive trust model:

**1. Member State Level Governance:**
- National regulatory frameworks and legal requirements
- Ministry-level authorisations and accreditations
- National quality assurance frameworks
- Country-specific compliance and audit requirements

**2. Sectoral Level Governance:**
- European-wide sectoral frameworks such as MyAcademicID
- GÉANT coordination and NREN federation structures
- Professional qualification bodies and regulatory authorities
- Cross-border recognition agreements and standards

**3. Institutional Level Governance:**
- University-specific policies and procedures
- Faculty and departmental authorisations
- Internal quality assurance mechanisms
- Institutional academic standards and requirements

#### Unified Trust Model Benefits

This multi-level governance support provides several critical advantages:

**Simplified Verification Process:**
Rather than requiring separate verification mechanisms for each governance level, the Pilot2 model enables verifiers to access all relevant governance information through a single, unified interface. This dramatically reduces complexity and improves efficiency in credential verification scenarios.

**Governance Interoperability:**
The system automatically handles interactions between different governance levels, ensuring that institutional policies align with sectoral requirements and national regulations without requiring manual coordination or separate verification processes.

**Scalability and Flexibility:**
New governance levels or frameworks can be integrated into the existing trust model without disrupting existing operations, enabling the system to evolve with changing regulatory and institutional requirements.

**Reduced Integration Complexity:**
Educational institutions and other stakeholders need to integrate with only one trust infrastructure rather than multiple separate systems for different governance levels, significantly reducing technical complexity and maintenance burden.

#### EBSI Registry Functions

The EBSI integration supports several key functions that enable this multi-level governance capability:

**Unified Trust Registry Management:**
- Maintains hierarchical trust relationships across all governance levels
- Enables automated verification of authorisation chains from institutional to European levels
- Supports cross-level policy validation and compliance checking
- Provides unified discovery mechanisms for all governance entities

**Integrated Schema Registry:**
- Stores credential schemas and semantic definitions for all governance levels
- Ensures consistent interpretation of attributes across different governance contexts
- Supports schema evolution and versioning across multiple governance frameworks
- Enables automated validation of credential conformance to multiple standards simultaneously

**Consolidated Status Management:**
- Tracks credential and authorisation status across all governance levels
- Enables coordinated revocation and suspension actions across multiple authorities
- Provides unified audit trails for compliance across different regulatory frameworks
- Supports real-time status synchronisation between governance levels

**Multi-Level DID Resolution:**
- Resolves decentralised identifiers across all governance contexts
- Enables verification of entity authority at multiple levels simultaneously
- Supports cross-level identity federation and recognition
- Provides unified cryptographic verification across governance boundaries

#### Practical Implementation Example

Consider a Spanish university student using MyAcademicID to access services at a French institution:

**Traditional Multi-System Approach would require:**
- Verification against Spanish national education regulations
- Validation within the MyAcademicID sectoral framework
- Compliance with the issuing university's internal policies
- Separate verification processes for each governance level

**Pilot2 Unified Model enables:**
- Single verification query to EBSI Verifiable Data Registries
- Automatic resolution of all governance level requirements
- Unified response indicating compliance across all levels
- Simplified integration for both issuing and verifying institutions

This unified approach represents a significant advancement in credential verification technology, enabling the complex governance requirements of European higher education to be managed through a single, cohesive technical infrastructure whilst maintaining the autonomy and authority of all governance levels.

### 4.3 Electronic Attestations of Attributes (EAAs)

The Pilot2 implementation introduces Electronic Attestations of Attributes (EAAs) as a key innovation for expressing and verifying institutional authorisations. EAAs provide a standardised mechanism for representing the authority to issue specific types of credentials, enabling fine-grained governance of the credential ecosystem.

Within the MyAcademicID context, EAAs can express various types of authorisations:

**MyAcademicIDIssuer**: Authorisation to issue MyAcademicID credentials to students and faculty
**EQFlevelX**: Authority to issue credentials at specific European Qualifications Framework levels
**HigherEducationInstitution**: Recognition as a legitimate higher education institution
**LicenceToActAtNationalLevel/EuropeanLevel**: Jurisdictional scope of authorisation

The EAA framework enables universities and other institutions to demonstrate their specific authorisations through cryptographically verifiable credentials, supporting automated verification processes whilst maintaining the flexibility necessary for diverse educational contexts.

### 4.4 W3C Verifiable Credentials Implementation

The technical foundation of the Pilot2 implementation relies on the W3C Verifiable Credentials Data Model, ensuring interoperability with emerging digital identity standards whilst providing the security and privacy features necessary for academic credential management. The implementation supports both W3C VCDM 1.1 and W3C VCDM 2.0 standards, enabling forward compatibility with evolving specifications.

#### Technical Standards Compliance

The W3C VC implementation incorporates comprehensive technical standards:

**JSON Schema Foundation:**
- Based on JSON Schema Draft 2020-12 standard
- Extends base W3C Verifiable Credentials Data Model
- Includes comprehensive attribute validation rules
- Supports semantic interoperability through linked data contexts

**Cryptographic Security:**
- EcdsaSecp256k1Signature2019 proof mechanisms
- Comprehensive integrity protection for all credential attributes
- Support for advanced signature suites as standards evolve
- Integration with EBSI trust infrastructure for enhanced verification

#### Complete Credential Structure

A full MyAcademicID credential includes all standard W3C VC components:

```json
{
  "@context": [
    "https://www.w3.org/2018/credentials/v1",
    "https://europa.eu/2023/credentials/myacademicid/v1"
  ],
  "id": "urn:uuid:5e9b4e8a-1dae-4797-86a6-f24392436c7f",
  "type": ["VerifiableCredential", "MyAcademicID"],
  "issuer": "did:ebsi:zbU6M5T5DxcgJiCUT78Fbk",
  "issuanceDate": "2023-09-01T10:15:38Z",
  "validFrom": "2023-09-01T10:15:38Z",
  "expirationDate": "2024-08-31T23:59:59Z",
  "credentialSubject": {
    // MyAcademicID specific attributes as defined in schema
  },
  "proof": {
    "type": "EcdsaSecp256k1Signature2019",
    "created": "2023-09-01T10:15:38Z",
    "proofPurpose": "assertionMethod",
    "verificationMethod": "did:ebsi:zbU6M5T5DxcgJiCUT78Fbk#keys-1",
    "jws": "eyJhbGciOiJFUzI1NksiLCJiNjQiOmZhbHNlLCJjcml0IjpbImI2NCJdfQ.."
  }
}
```

#### Key Implementation Advantages

**Cryptographic Verification**: All credentials are cryptographically signed, enabling tamper detection and authenticity verification without requiring connection to issuing systems.

**Selective Disclosure**: Students and faculty can selectively disclose credential attributes, maintaining privacy whilst providing necessary information for specific interactions. This addresses GDPR requirements for data minimisation and user consent.

**Interoperability**: The standardised format ensures compatibility with diverse wallet implementations and verification systems across the European digital identity ecosystem, including EUDI Wallet integration.

**Comprehensive Lifecycle Management**: The implementation includes advanced credential lifecycle management capabilities, enabling institutions to issue, update, suspend, revoke, and renew MyAcademicID credentials throughout their validity period. This represents a significant advancement over traditional credential systems that lack granular lifecycle control.

#### Relationship to eduPerson and REFEDS Standards

The MyAcademicID schema maintains strong alignment with established academic identity standards:

- **eduPersonUniqueId**: Foundation for communityUserIdentifier structure
- **eduPersonScopedAffiliation**: Syntax model for externalAffiliation attributes
- **REFEDS Assurance Framework**: Direct integration through assurance attribute
- **eduPerson Attribute Definitions**: Comprehensive OID mappings for all attributes

This alignment ensures seamless integration with existing academic identity infrastructure whilst providing the enhanced capabilities necessary for European-wide credential management.

## 5. Governance Implementation in Pilot2

### 5.1 GÉANT's Role as European RootTAO and Multi-Level Coordination

GÉANT's designation as the Root Trusted Accreditation Organisation for MyAcademicID reflects its unique position in the European research and education community. As the organisation responsible for coordinating pan-European research and education networking, GÉANT possesses the technical expertise, institutional relationships, and governance experience necessary to serve as the trust anchor for a European-wide academic identity system.

#### Enhanced RootTAO Responsibilities in Multi-Level Governance

The multi-level governance capability of Pilot2 expands GÉANT's role beyond traditional trust anchor functions:

**Cross-Level Policy Coordination:**
- Ensures alignment between European sectoral policies and national regulatory requirements
- Facilitates integration of institutional governance frameworks with broader European standards
- Coordinates dispute resolution across multiple governance levels
- Maintains consistency whilst respecting subsidiary and institutional autonomy

**Unified Standards Development:**
- Develops technical standards that accommodate multiple governance levels simultaneously
- Ensures interoperability between national, sectoral, and institutional requirements
- Coordinates schema evolution across different governance contexts
- Maintains backward compatibility whilst enabling governance innovation

**Multi-Level Trust Anchoring:**
- Serves as the ultimate trust anchor for sectoral governance whilst respecting national sovereignty
- Enables institutional governance integration without compromising higher-level requirements
- Provides unified verification mechanisms across all governance levels
- Maintains accountability and transparency across complex governance hierarchies

#### Governance Simplification Benefits

GÉANT's role in the unified trust model provides significant benefits for all stakeholders:

**For National Governments:**
- Simplified oversight of sectoral governance compliance
- Unified interface for cross-border educational cooperation
- Reduced complexity in international recognition processes
- Enhanced transparency in European educational integration

**For Educational Institutions:**
- Single point of integration for European-level compliance
- Simplified verification processes for international students and faculty
- Reduced administrative burden for cross-border programmes
- Enhanced capability for international collaboration

**For Students and Faculty:**
- Seamless credential recognition across governance levels
- Simplified verification processes for international mobility
- Enhanced privacy protection through unified disclosure mechanisms
- Improved user experience across different educational contexts

### 5.2 National Implementation Strategies

The Pilot2 implementation recognises that different European countries have varying regulatory frameworks, institutional structures, and technical capabilities. The governance model accommodates this diversity through flexible implementation strategies that enable countries to adapt MyAcademicID to their specific contexts whilst maintaining interoperability with the broader European ecosystem.

**Spain**: The Spanish implementation involves RedIRIS as the national TAO, with universities receiving MyAcademicIDIssuer authorisations through the established eduGAIN federation infrastructure. This approach leverages existing trust relationships and technical infrastructure whilst introducing the enhanced governance capabilities of the hybrid trust model.

**France**: RENATER serves as both TAO and issuer in the French implementation, reflecting the more centralised nature of the French higher education system. This dual role arrangement enables standardised credential issuance whilst maintaining institutional autonomy within the national framework.

**Multi-National Coordination**: The Pilot2 implementation includes comprehensive mechanisms for coordinating MyAcademicID deployment across multiple countries, ensuring that credentials issued in one country can be verified and recognised in others whilst respecting national sovereignty and regulatory requirements.

### 5.3 Institutional Onboarding and Integration

The successful implementation of MyAcademicID requires comprehensive onboarding processes that enable universities and other institutions to integrate the system with their existing infrastructure whilst meeting the governance requirements of the hybrid trust model. The Pilot2 implementation provides detailed guidance and support for institutional adoption.

**Technical Integration**: Institutions must integrate MyAcademicID with their existing student information systems, identity management infrastructure, and academic service platforms. The implementation provides standardised APIs and integration guidelines that simplify this process whilst ensuring security and compliance.

**Governance Compliance**: Universities must demonstrate their authority to issue MyAcademicID credentials through verifiable authorisation chains that can be traced back to their national NREN. The implementation includes comprehensive verification procedures that ensure institutional compliance whilst minimising administrative burden.

**Training and Support**: The Pilot2 implementation includes extensive training programmes and ongoing support services that enable institutional staff to effectively manage MyAcademicID deployment and operation. This support encompasses technical training, governance guidance, and user experience optimisation.

### 5.4 Quality Assurance and Compliance Monitoring

The MyAcademicID implementation includes comprehensive quality assurance mechanisms that ensure ongoing compliance with governance requirements whilst supporting the evolution of the system over time. These mechanisms address both technical and governance aspects of the credential ecosystem.

**Continuous Monitoring**: The implementation includes automated monitoring systems that track credential issuance, verification activities, and system performance across the entire ecosystem. This monitoring enables proactive identification of issues and supports continuous improvement of the system.

**Compliance Auditing**: Regular audits ensure that participating institutions maintain compliance with MyAcademicID governance requirements and technical standards. These audits are conducted by qualified assessors and include both technical evaluations and governance reviews.

**Feedback Integration**: The implementation includes mechanisms for collecting and incorporating feedback from users, institutions, and other stakeholders. This feedback drives continuous improvement of the system and ensures that it continues to meet the evolving needs of the European higher education community.

## 6. Technical Architecture and Implementation Details

### 6.1 Cryptographic Standards and Security

The Pilot2 implementation employs state-of-the-art cryptographic standards to ensure the security and integrity of MyAcademicID credentials. The system uses Elliptic Curve Cryptography (ECC) with the prime256v1 curve, providing 256-bit security that is equivalent to 3072-bit RSA whilst offering improved performance and reduced storage requirements.

All credentials are signed using ECDSA with SHA-256, providing tamper detection and authenticity verification. The implementation includes comprehensive key management procedures that ensure the security of signing keys whilst enabling efficient credential verification. Certificate chains include full intermediate certificates, ensuring that credentials can be verified even in distributed environments.

### 6.2 Privacy and Data Protection

The MyAcademicID implementation incorporates comprehensive privacy protection mechanisms that ensure compliance with the General Data Protection Regulation (GDPR) and other relevant data protection frameworks. The system supports selective disclosure, enabling users to share only the minimum information necessary for specific interactions.

The implementation includes sophisticated consent management mechanisms that enable users to control how their personal information is shared and used. Users can grant and revoke consent for specific data uses, and the system maintains comprehensive audit trails of all consent decisions and data sharing activities.

### 6.3 Interoperability and Standards Compliance

The Pilot2 implementation ensures interoperability with existing European educational infrastructure through comprehensive standards compliance. The system integrates with eduGAIN, EMREX, and other established educational service frameworks, enabling seamless integration with existing institutional systems and services.

The implementation supports the European Learning Model (ELM) for educational credential representation, ensuring compatibility with emerging European digital credential frameworks. This standards compliance enables MyAcademicID to serve as a foundation for broader digital transformation in European higher education.

### 6.4 Advanced Credential Lifecycle Management

One of the most significant innovations introduced in the Pilot2 implementation is the comprehensive credential lifecycle management system for MyAcademicID. This system addresses a critical limitation of traditional credential systems by enabling granular control over credential status throughout their entire lifecycle.

#### Credential Status Management

The MyAcademicID system supports multiple credential states that reflect real-world academic scenarios:

**Active Status:**
- Credential is valid and fully functional
- Can be used for authentication and service access
- Subject to standard verification processes
- Maintains full attribute disclosure capabilities

**Suspended Status:**
- Temporary suspension of credential validity
- Maintains credential integrity whilst preventing usage
- Enables reinstatement without reissuance
- Supports scenarios such as academic sanctions or administrative holds

**Revoked Status:**
- Permanent invalidation of credential
- Cannot be reinstated or reused
- Maintains audit trail for compliance purposes
- Supports scenarios such as academic misconduct or identity compromise

**Expired Status:**
- Natural expiration based on validity period
- Can be renewed through appropriate processes
- Maintains historical record of credential existence
- Supports long-term academic record management

#### Revocation and Suspension Mechanisms

The Pilot2 implementation provides sophisticated mechanisms for credential status management:

**Immediate Revocation:**
- Real-time revocation capability for security incidents
- Cryptographic proof of revocation status
- Distributed notification to all relying parties
- Integration with EBSI trust registries for verification

**Temporary Suspension:**
- Reversible suspension for administrative purposes
- Maintains credential cryptographic integrity
- Enables automatic reinstatement based on conditions
- Supports academic process requirements (e.g., disciplinary procedures)

**Scheduled Expiration:**
- Automatic expiration based on credential validity periods
- Proactive renewal notifications to credential holders
- Seamless transition between credential generations
- Maintains continuity of academic services

#### Trusted Status Registry Integration (TSRI)

The credential lifecycle management system integrates with the Trusted Status Registry Infrastructure (TSRI) to provide:

**Real-time Status Verification:**
- Immediate status checks during credential presentation
- Cryptographic proof of current credential state
- Historical validation for audit and compliance purposes
- Cross-border status synchronisation

**Audit Trail Maintenance:**
- Complete history of credential status changes
- Timestamps and authorisation records for all modifications
- Compliance documentation for regulatory requirements
- Forensic capabilities for security investigations

#### Governance and Authority Management

The lifecycle management system respects the established governance hierarchy:

**Institutional Authority:**
- Universities can suspend or revoke credentials they have issued
- Must follow established governance procedures
- Subject to NREN oversight and monitoring
- Maintains accountability through audit trails

**NREN Oversight:**
- NRENs can suspend institutional issuing privileges
- Authority to revoke credentials in exceptional circumstances
- Coordination with GÉANT for cross-border implications
- Dispute resolution and mediation capabilities

**GÉANT Coordination:**
- European-level coordination for major incidents
- Policy development for lifecycle management
- Cross-border impact assessment and response
- Standards development for interoperability

#### Practical Implementation Scenarios

**Academic Misconduct:**
- University suspends student's MyAcademicID pending investigation
- Credential cannot be used for academic services during suspension
- Upon resolution, credential can be reinstated or permanently revoked
- Complete audit trail maintained for legal compliance

**Identity Compromise:**
- Immediate revocation of compromised credentials
- Notification to all relying parties through TSRI
- Reissuance process with enhanced security measures
- Forensic investigation support through audit trails

**Administrative Changes:**
- Temporary suspension for student status changes
- Automatic reinstatement upon status confirmation
- Seamless transition between academic programmes
- Maintains continuity of academic services

**Mobility Programme Management:**
- Credential lifecycle aligned with mobility period
- Automatic expiration upon programme completion
- Renewal support for extended programmes
- Cross-border status coordination

#### Technical Implementation

The lifecycle management system utilises advanced cryptographic techniques:

**Status Proof Generation:**
- Cryptographic proofs of credential status
- Non-repudiation of status changes
- Tamper-evident status records
- Integration with blockchain infrastructure

**Revocation List Management:**
- Distributed revocation lists for offline verification
- Efficient status checking algorithms
- Minimal privacy impact for status verification
- Scalable architecture for European-wide deployment

### 6.5 Performance and Scalability

The technical architecture of the Pilot2 implementation is designed to support the scale and performance requirements of European higher education. The system supports millions of users across thousands of institutions, with response times suitable for interactive applications and batch processing capabilities for large-scale credential operations.

The implementation includes comprehensive monitoring and alerting systems that ensure system availability and performance. Load balancing and redundancy mechanisms provide high availability whilst supporting the geographic distribution necessary for European-wide deployment.

## 7. User Experience and Stakeholder Impact

### 7.1 Student Experience Enhancement

The MyAcademicID implementation significantly enhances the student experience by providing seamless access to academic services across European institutions. Students can use their MyAcademicID credentials to access library resources, register for courses, apply for student mobility programmes, and interact with academic services without the need for separate registration processes at each institution.

The implementation supports multilingual interfaces, accommodating the linguistic diversity of European higher education whilst providing consistent functionality across different languages and cultural contexts. Students can manage their credentials through user-friendly interfaces that abstract the technical complexity of the underlying systems.

### 7.2 Institutional Benefits

Universities and other higher education institutions benefit from MyAcademicID through reduced administrative burden, improved security, and enhanced capability to support international students and faculty. The standardised identity framework eliminates the need for institutions to develop and maintain separate identity management systems for cross-border interactions.

The implementation provides institutions with comprehensive tools for managing student and faculty credentials, including issuance, verification, and revocation capabilities. These tools integrate with existing institutional systems whilst providing the additional functionality necessary for European-wide interoperability.

### 7.3 National and European Impact

The MyAcademicID implementation contributes to the broader goals of the European Education Area by providing the digital infrastructure necessary for automatic recognition of learning outcomes and seamless academic mobility. The system supports the European Qualifications Framework (EQF) and other initiatives aimed at creating a unified European higher education system.

The implementation demonstrates the feasibility of large-scale digital credential systems that respect national sovereignty whilst enabling European-wide interoperability. This demonstration provides a foundation for broader digital transformation initiatives in European higher education and professional qualifications.

## 8. Challenges and Lessons Learned

### 8.1 Technical Challenges

The Pilot2 implementation addressed several significant technical challenges in developing a hybrid trust model that combines traditional PKI with decentralised trust mechanisms. The complexity of integrating multiple trust systems whilst maintaining performance and usability required innovative approaches to credential verification and trust resolution.

The implementation of EBSI integration required careful coordination with European blockchain infrastructure development, including adaptation to evolving standards and infrastructure capabilities. The team successfully navigated these challenges through close collaboration with EBSI development teams and proactive adaptation to changing requirements.

### 8.2 Governance Complexity

The multi-tiered governance model presents significant complexity in terms of policy coordination, compliance monitoring, and dispute resolution. The implementation required careful balance between European-level coordination and national autonomy, accommodating diverse regulatory frameworks whilst maintaining interoperability.

The development of governance policies that could accommodate the diversity of European higher education systems whilst providing sufficient consistency for technical interoperability required extensive stakeholder consultation and iterative refinement of policy frameworks.

### 8.3 Stakeholder Engagement

The successful implementation of MyAcademicID required extensive stakeholder engagement across multiple levels of the European higher education system. This engagement included universities, national governments, European institutions, and technology providers, each with different priorities and requirements.

The implementation team developed comprehensive stakeholder engagement strategies that included regular consultation meetings, collaborative policy development processes, and extensive feedback collection mechanisms. This engagement was essential for ensuring that the final implementation met the needs of all stakeholders whilst maintaining technical feasibility.

### 8.4 Credential Lifecycle Management Challenges

The implementation of advanced credential lifecycle management presented unique challenges that required innovative solutions:

**Real-time Status Synchronisation:**
- Ensuring immediate propagation of status changes across distributed systems
- Maintaining consistency between EBSI registries and local institutional systems
- Balancing performance requirements with security and reliability needs
- Addressing network latency and availability issues in cross-border scenarios

**Governance Complexity:**
- Defining clear authority boundaries for credential lifecycle management
- Establishing dispute resolution mechanisms for cross-border credential issues
- Balancing institutional autonomy with European-wide consistency requirements
- Addressing legal and regulatory variations across Member States

**Technical Integration:**
- Integrating lifecycle management with existing institutional systems
- Ensuring backward compatibility with legacy credential systems
- Maintaining security and privacy throughout the credential lifecycle
- Developing user-friendly interfaces for credential status management

### 8.5 Scaling and Sustainability

The transition from pilot implementation to operational deployment presents significant challenges in terms of scaling, sustainability, and long-term governance. The implementation team developed comprehensive plans for transitioning from project-based funding to sustainable operational models that can support European-wide deployment.

The sustainability planning includes consideration of technical infrastructure maintenance, governance structure evolution, and ongoing stakeholder support. These plans provide a foundation for long-term success of the MyAcademicID ecosystem.

## 9. Future Developments and Roadmap

### 9.1 Technological Evolution and Multi-Level Governance Enhancement

The MyAcademicID implementation is designed to evolve with advancing technology and changing requirements in European higher education. The multi-level governance capability of Pilot2 provides a foundation for future technological developments that can accommodate increasingly complex governance requirements whilst maintaining simplicity for end users.

#### Future Multi-Level Governance Capabilities

**Dynamic Governance Integration:**
- Automatic integration of new governance levels as they emerge
- Real-time policy synchronisation across governance hierarchies
- Adaptive verification mechanisms that adjust to changing requirements
- Intelligent conflict resolution between governance levels

**Enhanced Cross-Level Analytics:**
- Comprehensive governance analytics across all levels
- Predictive modelling for governance evolution and impact
- Automated compliance monitoring and reporting
- Cross-level performance optimisation and improvement

**Advanced Multi-Level Privacy:**
- Sophisticated privacy controls that respect all governance levels
- Granular consent management across governance hierarchies
- Zero-knowledge proofs for cross-level verification
- Privacy-preserving analytics for governance optimisation

#### Expansion of Governance Support

Future developments will extend the multi-level governance model to additional domains:

**Professional Qualification Integration:**
- Seamless integration of professional body governance with educational frameworks
- Cross-sector recognition and verification capabilities
- Unified approach to lifelong learning and professional development
- Enhanced support for professional mobility and recognition

**Regional and Local Governance:**
- Support for regional educational authorities and governance frameworks
- Integration with local quality assurance mechanisms
- Enhanced support for federal and devolved governance structures
- Flexible accommodation of diverse European governance models

**International Governance Coordination:**
- Integration with global educational governance frameworks
- Support for international recognition agreements and treaties
- Enhanced capability for worldwide educational mobility
- Coordination with international standards organisations

This evolutionary approach ensures that the MyAcademicID system can adapt to changing governance requirements whilst maintaining the fundamental benefits of unified, simplified verification processes across multiple governance levels.

### 9.2 Expanded Scope and Coverage

Future development plans include expansion of MyAcademicID coverage to additional European countries and integration with professional qualification frameworks. This expansion will extend the benefits of the system to broader segments of the European education and professional development community.

The implementation provides a foundation for integration with other European digital identity initiatives, including the European Digital Identity Wallet (EUDI Wallet) and broader digital government services. This integration will enable MyAcademicID to serve as a component of comprehensive digital identity solutions for European citizens.

### 9.3 Research and Innovation

The MyAcademicID implementation continues to serve as a platform for research and innovation in digital credential technology. Ongoing research projects explore advanced privacy technologies, improved user experience design, and innovative governance models for distributed digital identity systems.

The implementation includes mechanisms for incorporating research outcomes into operational systems, ensuring that academic research in digital identity can contribute to practical improvements in the MyAcademicID ecosystem.

## 10. Conclusion

The implementation of MyAcademicID within DC4EU Pilot2 represents a significant milestone in the digital transformation of European higher education. The successful deployment of a hybrid trust model that combines traditional PKI with decentralised trust mechanisms demonstrates the feasibility of advanced digital credential systems that can meet the complex governance requirements of European educational institutions.

A particularly innovative aspect of the Pilot2 implementation is its unified approach to multi-level governance through Verifiable Data Registries. The system's ability to simultaneously support Member State governance frameworks, sectoral requirements such as MyAcademicID, and institutional policies within a single trust model represents a fundamental advancement in credential verification technology. This unified approach dramatically simplifies verification processes whilst maintaining the integrity and autonomy of all governance levels.

The federation-based approach, with GÉANT serving as the European RootTAO and National Research and Education Networks as national TAOs, provides a scalable and sustainable model for European-wide academic identity management. The flexibility to accommodate universities as direct issuers and NRENs in dual TAO/TI roles ensures that the system can adapt to diverse national contexts whilst maintaining interoperability through the unified trust infrastructure.

The technical innovations introduced in Pilot2, including EBSI integration, Electronic Attestations of Attributes, comprehensive credential lifecycle management, and W3C Verifiable Credentials implementation, provide a foundation for future developments in digital credential technology. The multi-level governance capability ensures that these technical capabilities can be deployed safely and effectively across the European higher education landscape regardless of the complexity of underlying governance structures.

The successful implementation of MyAcademicID demonstrates that complex, multi-stakeholder digital identity systems can be deployed successfully when supported by appropriate governance frameworks, technical standards, and unified trust infrastructures. The ability to handle multiple governance levels through a single verification mechanism represents a paradigm shift in how educational credentials can be managed and verified across diverse regulatory and institutional contexts.

The MyAcademicID implementation within DC4EU Pilot2 thus represents not only a successful technical deployment but also a model for how European institutions can collaborate effectively to create digital infrastructure that serves the needs of the European Education Area whilst respecting national sovereignty, sectoral requirements, and institutional autonomy. The unified trust model eliminates the complexity traditionally associated with multi-level governance verification, creating a more efficient and user-friendly system for all stakeholders.

As European higher education continues to evolve towards greater integration and digital transformation, the MyAcademicID implementation provides a proven framework for addressing the complex challenges of academic credential management in a diverse, multi-national, and multi-level governance context. The success of this implementation demonstrates the potential for European collaboration in digital identity whilst showcasing how sophisticated governance requirements can be managed through elegant technical solutions.

The comprehensive nature of the implementation, from technical architecture through multi-level governance frameworks to user experience design, ensures that MyAcademicID can serve as a sustainable foundation for European academic identity management for years to come. The system's ability to evolve with changing requirements whilst maintaining stability and supporting increasingly complex governance structures positions it as a key component of the future European digital identity ecosystem.

Through its successful implementation of MyAcademicID with unified multi-level governance support, DC4EU Pilot2 has demonstrated that the vision of seamless European academic mobility supported by secure, interoperable digital credentials is not only feasible but ready for operational deployment. The system provides a model for how European institutions can work together to create digital infrastructure that serves the needs of students, faculty, and institutions whilst supporting the broader goals of European integration and educational excellence, all whilst maintaining the simplicity and efficiency that comes from unified governance verification processes.