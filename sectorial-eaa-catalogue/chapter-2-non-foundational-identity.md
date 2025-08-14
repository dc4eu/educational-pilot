# Chapter 2: non-foundational identity EAAs

## Introduction

Non-foundational identity electronic attestations of attributes (EAAs) represent a critical category within the DC4EU sectoral catalogue, operating under the **trust services legal regime** established by eIDAS2. Unlike foundational identity credentials such as the person identifier (PID), these EAAs do not establish legal identity but rather provide domain-specific identification, authentication, and authorisation capabilities within educational and professional contexts.

These credentials serve as the bridge between foundational legal identity and specific sectoral activities, enabling users to interact with educational institutions, professional organisations, and related services whilst maintaining appropriate privacy protections and selective disclosure capabilities.

## Legal framework and regulatory context

### Trust services legal regime

Non-foundational identity EAAs operate under the trust services legal regime, which:

- **Complements foundational identity**: builds upon but does not replace PID credentials
- **Enables sectoral applications**: provides domain-specific identity functions
- **Maintains privacy protection**: implements selective disclosure and purpose limitation
- **Supports user control**: empowers users to manage their digital identity across different contexts

### Relationship to foundational identity

All non-foundational identity EAAs within the DC4EU catalogue require binding to a foundational identity credential (PID), ensuring:

- **Verified identity linkage**: connection to legally recognised identity
- **Trust chain integrity**: verifiable relationship between foundational and sectoral identity
- **Accountability**: clear attribution of credentials to verified individuals
- **Privacy balance**: selective sharing of identity information based on context and purpose

## Core characteristics of non-foundational identity EAAs

### Domain-specific functionality

Non-foundational identity EAAs are designed to:

- **Enable context-specific identification**: provide identity functions within defined domains
- **Support role-based access**: facilitate access to services and resources based on user roles
- **Bridge institutional boundaries**: enable recognition across different organisations within sectors
- **Maintain temporal validity**: reflect current status and affiliations with appropriate expiry mechanisms

### Privacy and selective disclosure

These credentials implement advanced privacy protection through:

- **Attribute-level disclosure**: users can share specific attributes rather than complete identity profiles
- **Purpose-driven sharing**: information disclosure aligned with specific verification purposes
- **Verifier authorisation**: requiring verifiers to demonstrate legitimate need for identity information
- **User consent mechanisms**: empowering users to control when and how their identity information is shared

## 2.1 Enrolment status attestation (EAA1)

### Overview and purpose

The enrolment status attestation provides verifiable proof of a learner's current enrolment in formal education programmes. This credential enables access to student services, benefits, and resources whilst protecting sensitive academic information through selective disclosure.

### EAA characterisation

```json
{
  "eaa_id": "EAA1",
  "title": "Enrolment Status",
  "description": "Attestation that confirms the current enrolment status of a learner in a formal education programme.",
  "credential_type": "VerifiableAttestation",
  "sectoral_scope": "FormalEducation",
  "requires_pid": true,
  "disclosure_policy": {
    "restricted_access": true,
    "verifier_role_check": true,
    "confidentiality_level": "confidential"
  }
}
```

### Authorised issuers and verifiers

**Issuable by:**
- Higher education institutions
- Vocational education institutions
- Other formally recognised educational providers

**Usable by:**
- Student unions and representative organisations
- Public transport services (for student discounts)
- Educational service providers
- Accommodation providers
- Cultural and recreational service providers

### Key attributes and data structure

The enrolment status credential includes:

- **Student identity information**: linked to PID for verified identification
- **Institution details**: verified educational institution information
- **Programme information**: course or programme of study
- **Enrolment period**: current academic term or year validity
- **Status indicators**: active, suspended, or other relevant status
- **Access entitlements**: services and benefits associated with student status

### Dynamic lifecycle management

Enrolment status credentials implement dynamic validity:

- **Academic year linkage**: automatically aligned with institutional academic calendars
- **Real-time status updates**: immediate reflection of status changes
- **Suspension capabilities**: temporary credential suspension without revocation
- **Renewal processes**: seamless transition between academic periods

### Use cases and applications

- **Student transport discounts**: verification of student status for reduced fare programmes
- **Library and facility access**: authentication for educational resource access
- **Student housing services**: verification for accommodation applications
- **Cultural institution benefits**: access to student pricing for museums and events
- **Academic mobility programmes**: verification of current student status for exchanges

## 2.2 Educational ID

### Overview and institutional context

The educational ID provides comprehensive identity verification within educational contexts, incorporating standardised attributes from eduGAIN and SCHAC (SCHema for ACademia) frameworks to ensure interoperability across European educational institutions.

### Standards compliance and interoperability

The educational ID schema complies with:

- **eduGAIN**: European research and education identity federation attributes
- **SCHAC**: Standard schema for academia with European-specific extensions
- **EBSI**: European blockchain services infrastructure requirements
- **JSON Schema Draft 2020-12**: Latest JSON schema specification standards

### Core data model structure

```json
{
  "credentialSubject": {
    "id": "did:example:123456789abcdefghi",
    "identifier": "student.identifier@institution.edu",
    "schacPersonalUniqueCode": ["urn:schac:personalUniqueCode:int:esi:institution.edu:123456"],
    "schacHomeOrganization": "institution.edu",
    "eduPersonAffiliation": ["student", "member"],
    "eduPersonScopedAffiliation": ["student@institution.edu"],
    "institutionalEmail": "student@institution.edu"
  }
}
```

### Key attributes and functionality

#### Personal identification
- **Institutional identifier**: unique identifier within educational institution
- **SCHAC personal unique code**: standardised European academic identifier
- **Home organisation**: institution affiliation using SCHAC standards
- **Contact information**: institutional email address for official communications

#### Affiliation and roles
- **Educational affiliations**: student, faculty, staff, alumni, or other roles
- **Scoped affiliations**: role-specific identifiers including institutional scope
- **Access entitlements**: services and resources available based on affiliation
- **Validity periods**: temporal boundaries for institutional relationships

### Privacy and selective disclosure

Educational ID credentials support:

- **Attribute-level sharing**: disclosure of specific identity attributes only
- **Purpose-based access**: sharing aligned with verification purposes
- **Institutional privacy**: protection of sensitive institutional relationships
- **Cross-border privacy**: privacy-preserving verification for international mobility

### Integration with European identity federations

The educational ID leverages existing European infrastructure:

- **eduGAIN compatibility**: seamless integration with European academic identity federation
- **SCHAC attribute support**: comprehensive academic attribute framework
- **Cross-institutional recognition**: standardised identity verification across institutions
- **Mobility support**: facilitation of academic and professional mobility programmes

## 2.3 Alliance ID

### Overview and European university alliances

The alliance ID provides identity credentials specifically designed for participants in European university alliances, supporting the transnational partnerships that characterise modern European higher education cooperation.

### European university alliance context

Alliance ID credentials support:

- **Transnational educational partnerships**: multi-institutional collaboration frameworks
- **European values promotion**: advancement of European identity and educational values
- **Quality enhancement**: improvement of European higher education competitiveness
- **Strategic cooperation**: long-term institutional partnerships across member states

### Key alliance examples

The alliance ID supports major European university alliances including:

- **UNA Europa**: alliance of comprehensive universities across Europe
- **YUFE (Young Universities for the Future of Europe)**: network of young, innovative universities
- **EUTOPIA**: European university alliance promoting civic engagement
- **4EU+ Alliance**: strategic partnership of leading European universities
- **CIVIS**: European civic university alliance

### Data model and attributes

```json
{
  "credentialSubject": {
    "id": "did:example:alliance123456789",
    "allianceIdentifier": "yna-europa:student:987654321",
    "allianceName": "UNA Europa",
    "homeInstitution": "University of Example",
    "allianceRole": ["student", "mobility_participant"],
    "validityPeriod": "2024-2027",
    "accessRights": ["library_access", "course_enrollment", "research_facilities"]
  }
}
```

### Alliance-specific functionality

#### Cross-institutional identity
- **Alliance-wide recognition**: identity verification across all alliance member institutions
- **Standardised identifier format**: consistent identification across different institutional systems
- **Role-based access**: services and resources based on alliance participation role
- **Mobility facilitation**: seamless movement between alliance institutions

#### Collaborative capabilities
- **Joint programme participation**: access to collaborative degree programmes
- **Research collaboration**: verification for cross-institutional research projects
- **Shared resource access**: utilisation of alliance-wide facilities and services
- **Cultural and academic exchange**: participation in alliance-sponsored activities

### Integration with institutional systems

Alliance ID credentials integrate with:

- **Member institution identity systems**: connection with local institutional credentials
- **Alliance-wide service platforms**: access to collaborative digital services
- **Mobility management systems**: support for student and staff exchange programmes
- **Quality assurance frameworks**: alignment with alliance-wide quality standards

## 2.4 European student card

### Overview and DG-EAC integration

The European student card (ESC) provides standardised student identification supporting mobility across the European higher education area, based on the European Commission's DG-EAC service framework.

### Core functionality and benefits

The ESC enables:

- **Cross-border student recognition**: standardised student identification across Europe
- **Mobility programme support**: facilitation of Erasmus+ and other exchange programmes
- **Service access standardisation**: common approach to student service access
- **Digital-first student experience**: comprehensive digital student identity management

### Technical specifications

#### European student identifier (ESI)
- **Unique identification**: globally unique identifier for European student mobility
- **Mobility-specific validity**: lifetime limited to student mobility periods
- **Privacy protection**: designed to prevent unauthorised tracking or correlation
- **Standards compliance**: alignment with European student mobility requirements

#### European student card number (ESCN)
- **UUID format**: universally unique identifier in standard UUID format
- **Interoperable design**: compatible across different institutional systems
- **Revocation support**: capability for immediate invalidation when necessary
- **Status tracking**: real-time monitoring of card validity and status

### Data model structure

```json
{
  "credentialSubject": {
    "id": "did:example:student123456789",
    "givenName": "Maria",
    "familyName": "García",
    "email": "maria.garcia@student.example.edu",
    "esi": "ESI-EU-2024-123456789",
    "escn": "550e8400-e29b-41d4-a716-446655440000",
    "institutionPIC": "999999999",
    "academicLevel": "Master",
    "cardType": "Digital",
    "status": "active"
  }
}
```

### Integration with European infrastructure

#### Participant identification code (PIC) integration
- **Institutional verification**: connection to official EU institutional identifiers
- **Programme eligibility**: verification of institution participation in EU programmes
- **Quality assurance**: institutional accreditation and quality framework alignment
- **Cross-border recognition**: facilitation of institutional recognition across member states

#### Status management and lifecycle
- **Real-time status checking**: immediate verification of card validity
- **Lifecycle management**: comprehensive management from issuance to expiry
- **Revocation capabilities**: immediate invalidation for security or policy reasons
- **Renewal processes**: seamless transition for continuing students

### Service integration and access

The ESC facilitates access to:

- **Educational services**: libraries, laboratories, and academic facilities
- **Administrative services**: registration, certification, and academic record access
- **Student support services**: counselling, health services, and accommodation
- **Cultural and recreational services**: museums, sports facilities, and entertainment venues

## 2.5 MyAcademic ID

### Overview and eduGAIN integration

MyAcademic ID provides standardised academic non-foundational identity for students and staff across European higher education institutions, leveraging the eduGAIN infrastructure for seamless academic mobility and collaboration.

### Technical foundation and standards

#### eduGAIN infrastructure integration
- **European identity federation**: seamless integration with eduGAIN identity framework
- **Cross-institutional authentication**: standardised authentication across European institutions
- **Attribute sharing protocols**: secure and privacy-preserving attribute exchange
- **Trust framework alignment**: compliance with European academic trust frameworks

#### REFEDS assurance framework alignment
- **Identity assurance levels**: standardised confidence levels for identity verification
- **Trust indicators**: clear communication of identity verification quality
- **Risk-based access**: appropriate access control based on assurance levels
- **International compatibility**: alignment with global academic identity standards

### Core attribute framework

#### Community user identifier
```json
{
  "communityUserIdentifier": "a1b2c3d4e5f6@erasmus.eduteams.org"
}
```

- **Opaque identifier format**: privacy-preserving persistent identifier
- **eduPersonUniqueId syntax**: compliance with established academic identity standards
- **Global uniqueness**: unique identification within MyAcademicId namespace
- **Persistent identity**: stable identifier across academic career and mobility

#### Academic affiliations and entitlements
```json
{
  "externalAffiliation": ["student@university.edu", "researcher@institute.org"],
  "entitlements": ["library_access", "research_facility_access", "course_enrollment"],
  "europeanStudentIdentifier": ["ESI-EU-2024-987654321"]
}
```

### Data model specification

#### Required attributes
| Attribute | Description | Format | Standards reference |
|-----------|-------------|--------|-------------------|
| `communityUserIdentifier` | Persistent opaque identifier | String | eduPersonUniqueId (OID 1.3.6.1.4.1.5923.1.1.1.13) |
| `displayName` | Full name for display | String | displayName (OID 2.16.840.1.113730.3.1.241) |
| `givenName` | First name | String | givenName (OID 2.5.4) |
| `familyName` | Surname | String | sn (OID 2.5.4.4) |
| `emailAddress` | Email address | String (email) | mail (OID 0.9.2342.19200300.100.1.3) |
| `assurance` | Identity assurance level | Array of URIs | eduPersonAssurance (OID 1.3.6.1.4.1.5923.1.1.1.11) |

#### Optional attributes
- **European student identifier**: ESI for mobility support
- **Organisational information**: institutional affiliation details
- **External affiliations**: multi-institutional relationships
- **Service entitlements**: access rights and service permissions

### Academic mobility support

MyAcademic ID facilitates:

- **Cross-institutional identity**: recognised identity across European institutions
- **Mobility programme integration**: seamless integration with exchange programmes
- **Research collaboration**: identity verification for cross-institutional research
- **Service access**: standardised access to academic services and resources

### Privacy and data protection

#### Selective disclosure capabilities
- **Attribute-level control**: granular control over shared information
- **Purpose limitation**: sharing aligned with specific verification purposes
- **Consent management**: user control over information sharing decisions
- **Data minimisation**: sharing only necessary information for specific purposes

#### GDPR compliance
- **Lawful basis**: clear legal basis for identity information processing
- **Data subject rights**: comprehensive support for individual rights
- **Cross-border transfers**: appropriate safeguards for international data sharing
- **Retention limitations**: appropriate data retention and deletion policies

## 2.6 Professional ID

### Overview and professional context

Professional ID credentials provide verified identity within professional contexts, enabling practitioners to demonstrate their professional status, qualifications, and regulatory compliance across different professional environments and jurisdictions.

### Regulatory framework and compliance

#### Professional body integration
- **Regulatory authority verification**: connection to official professional regulatory bodies
- **Professional board registration**: verification of registration with regional professional bodies
- **Legal entitlement verification**: confirmation of legal authority to practice
- **Speciality certification**: verification of professional specialisations and competencies

#### Cross-border professional mobility
- **European professional recognition**: facilitation of professional recognition across EU member states
- **Qualification verification**: standardised verification of professional qualifications
- **Regulatory compliance**: alignment with European professional qualification directives
- **Mutual recognition support**: technical support for professional qualification mutual recognition

### Data model and attributes

```json
{
  "credentialSubject": {
    "id": "did:example:professional123456789",
    "givenName": "Elena",
    "familyName": "Rodriguez",
    "personalAdministrativeNumber": "PROF-ES-987654321",
    "legallyEntitled": true,
    "professionalBoard": ["Madrid Professional Board"],
    "professionalSpeciality": ["Corporate Law", "International Trade Law"],
    "documentNumber": "DOC-2024-567890"
  }
}
```

### Key attribute specifications

#### Professional identification
- **Personal administrative number**: unique identifier assigned by professional regulatory body
- **Document number**: specific document reference for professional registration
- **Legal entitlement indicator**: boolean verification of legal authority to practice
- **Professional board affiliation**: regional or national professional body registration

#### Professional competencies
- **Professional specialities**: array of verified professional specialisations
- **Competency areas**: specific areas of professional expertise
- **Regulatory scope**: jurisdictions and contexts where professional activity is authorised
- **Validity periods**: temporal boundaries for professional authorisation

### Integration with professional ecosystems

#### Professional service verification
- **Client identity verification**: verified professional identity for client services
- **Regulatory compliance checking**: automated verification of professional standing
- **Inter-professional collaboration**: verified identity for professional team collaboration
- **Insurance and liability**: identity verification for professional insurance purposes

#### Cross-jurisdictional practice
- **Multi-jurisdiction verification**: identity verification across different regulatory jurisdictions
- **Temporary practice authorisation**: verification for temporary professional practice permits
- **International collaboration**: identity verification for cross-border professional projects
- **Professional mobility**: facilitation of professional practice mobility within Europe

## 2.7 Doctor ID

### Overview and medical profession context

Doctor ID credentials provide specialised identity verification for medical professionals, incorporating specific requirements for medical practice regulation, patient safety, and healthcare service delivery across European healthcare systems.

### Medical regulatory framework

#### Medical board integration
- **Medical board registration**: verification of registration with regional medical boards
- **Medical licence verification**: confirmation of valid medical practice licence
- **Speciality certification**: verification of medical specialisations and sub-specialities
- **Continuing education compliance**: verification of ongoing professional development requirements

#### Patient safety and regulatory compliance
- **Legal practice authority**: verification of legal authority to practice medicine
- **Scope of practice**: specific medical procedures and treatments authorised
- **Regulatory standing**: current status with medical regulatory authorities
- **Quality assurance**: alignment with medical quality and safety standards

### Data model and medical attributes

```json
{
  "credentialSubject": {
    "id": "did:example:doctor123456789",
    "givenName": "Dr. Maria",
    "familyName": "Santos",
    "personalAdministrativeNumber": "MED-PT-123456789",
    "legallyEntitled": true,
    "medicalBoard": "Lisbon Medical Board",
    "medicalSpeciality": ["Cardiology", "Interventional Cardiology"],
    "documentNumber": "MED-LIC-2024-987654"
  }
}
```

### Medical-specific attribute framework

#### Medical identification and authorisation
- **Medical board affiliation**: specific medical regulatory body registration
- **Medical specialities**: verified medical specialisations and competencies
- **Practice authorisation**: legal authority to practice medicine
- **Medical licence documentation**: reference to official medical licence documents

#### Healthcare system integration
- **Hospital affiliation**: verification of hospital and clinic affiliations
- **Insurance network participation**: verification of healthcare insurance network participation
- **Telemedicine authorisation**: verification of authority for remote medical practice
- **Cross-border practice**: authorisation for medical practice across EU member states

### Integration with healthcare ecosystems

#### Healthcare service delivery
- **Patient authentication**: verified medical professional identity for patient services
- **Medical team collaboration**: verified identity for multi-professional healthcare teams
- **Hospital system integration**: seamless integration with hospital information systems
- **Emergency response**: rapid identity verification for emergency medical situations

#### Medical education and research
- **Medical education verification**: identity verification for medical training and education
- **Research collaboration**: verified identity for medical research projects
- **Clinical trial participation**: identity verification for clinical research activities
- **Academic medical practice**: integration with medical education institutions

### Patient safety and privacy protection

#### Medical ethics compliance
- **Patient confidentiality**: appropriate privacy protections for medical practice
- **Informed consent**: identity verification supporting informed consent processes
- **Medical ethics standards**: compliance with medical professional ethics requirements
- **Data protection**: enhanced data protection for sensitive medical contexts

#### Healthcare data integration
- **Electronic health record integration**: verified identity for EHR access and management
- **Medical device integration**: identity verification for medical device operation
- **Prescription systems**: verified identity for electronic prescription systems
- **Healthcare analytics**: identity verification for healthcare data analysis and research

## Implementation considerations

### Technical requirements

Implementing non-foundational identity EAAs requires:

#### System integration capabilities
- **EUDIW compatibility**: seamless integration with European digital identity wallet protocols
- **Trust registry connectivity**: connection to trusted issuer, verifier, and schema registries
- **Real-time verification**: capability for immediate credential status verification
- **Cross-border interoperability**: technical standards supporting European-wide recognition

#### Security and privacy implementation
- **Selective disclosure mechanisms**: technical capability for attribute-level information sharing
- **Zero-knowledge proof support**: advanced cryptographic privacy protection capabilities
- **Consent management systems**: robust user consent capture and management
- **Audit and compliance logging**: comprehensive audit trails for regulatory compliance

### Governance and quality assurance

#### Institutional responsibilities
- **Issuer accreditation**: verification of authorisation to issue specific non-foundational identity EAAs
- **Ongoing compliance monitoring**: continuous verification of issuer adherence to standards
- **Quality assurance processes**: regular auditing and quality verification procedures
- **Cross-border coordination**: alignment with other member states' implementation approaches

#### User empowerment and control
- **Transparent information practices**: clear communication about credential capabilities and limitations
- **User consent mechanisms**: robust consent capture and management for information sharing
- **Appeal and correction processes**: procedures for users to challenge or correct credential information
- **Digital literacy support**: educational resources to support user understanding and effective use

### Future evolution and standards alignment

#### Emerging technology integration
- **Artificial intelligence**: AI-assisted verification and fraud detection capabilities
- **Blockchain innovations**: leverage of emerging blockchain and distributed ledger technologies
- **Biometric integration**: enhanced biometric verification for high-assurance applications
- **Quantum-resistant cryptography**: preparation for post-quantum cryptographic migration

#### Sectoral expansion and enhancement
- **Additional professional sectors**: extension to other regulated professional domains
- **Enhanced attribute frameworks**: development of more sophisticated attribute and competency models
- **International alignment**: integration with global professional and educational identity standards
- **Service ecosystem growth**: expansion of services and applications leveraging non-foundational identity credentials

This comprehensive framework of non-foundational identity EAAs provides the essential building blocks for domain-specific identity verification across European educational and professional contexts, enabling secure, privacy-preserving, and user-controlled digital identity whilst maintaining the highest standards of trust and regulatory compliance.