# Chapter 3: formal education achievement EAAs

## Introduction

Formal education achievement electronic attestations of attributes (EAAs) represent the core category of academic credentials within the DC4EU sectoral catalogue. These EAAs document learning outcomes, qualifications, and academic achievements earned through formally recognised educational programmes at institutions authorised by national and European quality assurance frameworks.

Operating under the **trust services legal regime** established by eIDAS2, these credentials provide verifiable proof of educational attainment whilst enabling selective disclosure, cross-border recognition, and seamless integration with European mobility programmes. All formal education EAAs are built upon the European Learning Model (ELM) v3.2 and comply with W3C verifiable credentials data model (VCDM) v1.1 standards.

## Legal and regulatory framework

### European qualifications framework integration

Formal education EAAs align with the European qualifications framework (EQF) and national qualifications frameworks (NQF), ensuring:

- **Standardised level descriptors**: clear mapping to EQF levels 1-8 based on learning complexity and autonomy
- **Learning outcomes focus**: emphasis on knowledge, skills, and competences rather than learning inputs
- **Quality assurance alignment**: integration with European quality assurance frameworks
- **Cross-border recognition**: facilitation of qualification recognition through standardised descriptors

### Bologna Process compliance

Higher education credentials implement Bologna Process principles:

- **Three-cycle structure**: bachelor's, master's, and doctoral level qualifications
- **ECTS credit system**: European credit transfer and accumulation system integration
- **Diploma supplement compatibility**: standardised qualification description format
- **Quality assurance standards**: alignment with European standards and guidelines (ESG)

### Vocational education and training alignment

VET credentials comply with European VET frameworks:

- **Council recommendation on VET**: alignment with European VET policy framework
- **ECVET system**: European credit system for vocational education and training
- **EQAVET framework**: European quality assurance in vocational education and training
- **Skills and competences focus**: emphasis on labour market relevant skills and competences

## Technical architecture and data model foundation

### European Learning Model (ELM) v3.2 implementation

All formal education EAAs implement ELM v3.2 ontology:

```json
{
  "credentialSubject": {
    "type": "Person",
    "hasClaim": [{
      "type": "LearningAchievement",
      "title": {"en": "Master of Science in Computer Science"},
      "awardedBy": {
        "type": "AwardingProcess",
        "awardingBody": {
          "type": "Organisation",
          "legalName": {"en": "University of Example"}
        }
      },
      "specifiedBy": {
        "type": "Qualification",
        "eqfLevel": {"notation": "7"},
        "creditPoint": [{
          "framework": {"notation": "ECTS"},
          "point": "120"
        }]
      }
    }]
  }
}
```

### W3C verifiable credentials compliance

The EDC-W3C format ensures international interoperability:

- **Root-level field structure**: essential VC fields at document root level
- **Standardised proof mechanisms**: support for multiple cryptographic proof types
- **Enhanced status management**: real-time revocation and suspension capabilities
- **Selective disclosure support**: privacy-preserving attribute sharing mechanisms

### Business rule enforcement

Automated validation ensures credential integrity:

- **Credit constraints**: ECTS/ECVET point limitations based on credential type
- **EQF level validation**: appropriate qualification level enforcement
- **Competence mapping**: mandatory alignment with established competence frameworks
- **Quality assurance requirements**: institutional accreditation verification

## 3.1 Higher education credentials

### 3.1.1 European higher education diploma (EUHED)

#### Overview and purpose

The European higher education diploma provides formal certification of completed higher education qualifications, supporting degree recognition across the European higher education area whilst maintaining compatibility with global academic mobility frameworks.

#### Business value and applications

**For higher education institutions:**
- Enhanced institutional trust and international prestige
- Compliance with European and global recognition frameworks
- Automated diploma issuance reducing administrative burden
- Integration with quality assurance and accreditation systems

**For graduates:**
- Portable digital credentials accessible across platforms
- Instant verification capabilities for employment and further study
- Cross-border recognition throughout Europe
- Permanent digital access eliminating document loss concerns

**For employers and recognition authorities:**
- Real-time tamper-proof qualification verification
- Reduced recruitment risk through guaranteed authenticity
- Automated qualification validation processes
- Integration with HR and recognition systems

#### Data model structure

```json
{
  "@context": [
    "https://www.w3.org/2018/credentials/v1",
    "https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/contexts/european-digital-credential-v3.jsonld"
  ],
  "type": [
    "VerifiableCredential",
    "VerifiableAttestation",
    "EuropeanDigitalCredential",
    "EuropeanHigherEducationDiploma"
  ],
  "credentialSubject": {
    "type": "Person",
    "hasClaim": [{
      "type": "LearningAchievement",
      "title": {"en": "Bachelor of Science in Computer Science"},
      "specifiedBy": {
        "type": "Qualification",
        "eqfLevel": {"notation": "6"},
        "educationSubject": [{"prefLabel": {"en": "Computer Science"}}],
        "creditPoint": [{"framework": {"notation": "ECTS"}, "point": "180"}]
      },
      "awardedBy": {
        "type": "AwardingProcess",
        "awardingDate": "2024-06-30T00:00:00Z",
        "awardingBody": {
          "type": "Organisation",
          "legalName": {"en": "University of Excellence"}
        }
      }
    }]
  }
}
```

#### Key attributes and specifications

**Personal identification:**
- Student name and date of birth in ISO 8601 format
- Optional student identifier for institutional tracking
- DID-based credential subject identification

**Qualification details:**
- Qualification title in multiple languages
- Field of study classification using international standards
- EQF/NQF level designation (typically levels 5-8 for higher education)
- Credit point allocation using ECTS system

**Institutional information:**
- Awarding institution legal name and location
- Awarding date and academic year context
- Jurisdiction and regulatory framework information
- Quality assurance and accreditation details

**Professional entitlements:**
- Access rights to regulated professions where applicable
- Further study entitlements and academic progression pathways
- Professional recognition and licensing implications
- Cross-border recognition status

### 3.1.2 European higher education diploma supplement (EUHEDS)

#### Overview and Bologna Process alignment

The diploma supplement provides detailed academic context for higher education qualifications, implementing the standardised format developed through the Bologna Process whilst enabling digital verification and enhanced international recognition.

#### Structured academic profile components

**Learner academic profile:**
- Comprehensive study programme description
- Individual course-level academic performance data
- Learning achievements with detailed competence mapping
- Academic progression and grade point calculations

**Institutional context information:**
- Education system description and regulatory framework
- Institutional accreditation and quality assurance status
- Grading scale explanation and statistical distribution
- Assessment methodology and academic standards description

#### Data model specifications

```json
{
  "credentialSubject": {
    "hasClaim": [{
      "type": "LearningAchievement",
      "title": {"en": "Bachelor of Arts in European Studies"},
      "description": {"en": "Comprehensive programme covering European integration, politics, economics, and cultural studies"},
      "gradingScheme": {
        "title": {"en": "ECTS Grading Scale"},
        "description": {"en": "A (Excellent) to F (Fail) with statistical distribution"}
      },
      "learningOpportunity": [{
        "type": "LearningOpportunity",
        "title": {"en": "European Economic Integration"},
        "creditReceived": [{"framework": {"notation": "ECTS"}, "point": "6"}],
        "grade": {"notation": "B+"}
      }]
    }]
  }
}
```

#### Enhanced recognition capabilities

The EUHEDS facilitates:
- **Academic mobility**: clear qualification context for international applications
- **Professional qualification recognition**: detailed competence mapping for regulatory authorities
- **Recruitment processes**: comprehensive academic background verification for employers
- **Quality assurance**: transparent academic standards and institutional quality demonstration

### 3.1.3 European higher education transcript of records (EUHETOR)

#### Overview and academic documentation

The transcript of records provides comprehensive documentation of academic coursework, grades, and credit achievements throughout higher education programmes, supporting both academic mobility and employment verification processes.

#### Academic record components

**Course documentation:**
- Individual course titles and descriptions
- Credit point allocations using ECTS system
- Grade achievements with grading scale context
- Academic period and semester information

**Programme progression tracking:**
- Cumulative grade point average calculations
- Academic standing and progression status
- Learning outcome attainment verification
- Competence development documentation

#### Implementation specifications

```json
{
  "credentialSubject": {
    "hasClaim": [{
      "type": "LearningAchievement",
      "title": {"en": "Master of Science in Environmental Engineering - Transcript"},
      "learningOpportunity": [
        {
          "type": "LearningOpportunity",
          "title": {"en": "Advanced Water Treatment Systems"},
          "creditReceived": [{"framework": {"notation": "ECTS"}, "point": "8"}],
          "grade": {"notation": "A"},
          "academicPeriod": "2023-2024 Autumn Semester"
        },
        {
          "type": "LearningOpportunity", 
          "title": {"en": "Environmental Impact Assessment"},
          "creditReceived": [{"framework": {"notation": "ECTS"}, "point": "6"}],
          "grade": {"notation": "B+"},
          "academicPeriod": "2023-2024 Spring Semester"
        }
      ]
    }]
  }
}
```

### 3.1.4 European higher education proof of enrolment (EUHEPOE)

#### Overview and status verification

The proof of enrolment provides current verification of student status within higher education programmes, enabling access to student services, mobility programmes, and various benefits whilst protecting sensitive academic information.

#### Student status documentation

**Enrolment verification:**
- Current programme registration status
- Academic level and degree type confirmation
- Institution affiliation verification
- Expected graduation timeline information

**Service access enablement:**
- Student union membership verification
- Transport and accommodation service access
- Cultural institution benefit eligibility
- Library and academic facility usage rights

#### Data structure and validity

```json
{
  "credentialSubject": {
    "hasClaim": [{
      "type": "LearningAchievement",
      "title": {"en": "Current Enrolment - Master of Business Administration"},
      "awardingDate": "2024-09-01T00:00:00Z",
      "validFrom": "2024-09-01T00:00:00Z",
      "validUntil": "2025-06-30T23:59:59Z",
      "specifiedBy": {
        "type": "Qualification",
        "eqfLevel": {"notation": "7"},
        "educationSubject": [{"prefLabel": {"en": "Business Administration"}}]
      }
    }]
  }
}
```

### 3.1.5 European higher education micro-credential (EUHEMIC)

#### Overview and modular learning

Higher education micro-credentials address the growing importance of modular, skills-focused learning within higher education, providing stackable credentials that can contribute to larger qualifications whilst meeting immediate labour market needs.

#### Business value and market alignment

**For higher education institutions:**
- Market-responsive programme development capabilities
- Revenue diversification through flexible learning offerings
- Industry partnership facilitation
- Lifelong learning market engagement

**For learners:**
- Flexible skill development aligned with career goals
- Stackable credentials contributing to formal qualifications
- Industry-relevant competence development
- Rapid response to changing market demands

**For employers:**
- Targeted skill verification for specific roles
- Reduced training costs through external skill development
- Quality-assured competence verification
- Flexible workforce development support

#### Technical specifications and constraints

**Credit limitations:**
- 1-15 ECTS credits per micro-credential
- EQF levels 5-8 for higher education context
- Mandatory competence mapping to support recognition
- Quality assurance alignment with institutional standards

**Learning outcome requirements:**
```json
{
  "credentialSubject": {
    "hasClaim": [{
      "type": "LearningAchievement",
      "title": {"en": "Digital Marketing Analytics Micro-credential"},
      "creditReceived": [{"framework": {"notation": "ECTS"}, "point": "5"}],
      "specifiedBy": {
        "type": "Qualification",
        "eqfLevel": {"notation": "6"},
        "learningOutcome": [{
          "title": {"en": "Digital Analytics Competence"},
          "relatedESCOSkill": [{"prefLabel": {"en": "Digital marketing analytics"}}]
        }]
      }
    }]
  }
}
```

## 3.2 Vocational education and training credentials

### 3.2.1 European VET micro-credential (EUVETMC)

#### Overview and labour market alignment

VET micro-credentials provide targeted vocational skill certification aligned with labour market demands, supporting both initial vocational education and continuing professional development within rapidly evolving economic sectors.

#### Business value for stakeholders

**For VET providers:**
- Market-relevant training programme development
- Partnership opportunities with employers and industry
- International recognition through EBSI infrastructure
- Flexible delivery model support

**For learners:**
- Employability enhancement through certified skills
- Flexible learning that accommodates work schedules
- Stackable credentials toward full qualifications
- International mobility with portable credentials

**For employers:**
- Skilled workforce development
- Verified job-specific competences
- Reduced hiring risk through quality-assured skills
- Partnership opportunities for customised training

#### Technical framework and standards

**EQAVET alignment:**
- Quality assurance framework compliance
- Trust and credibility through recognised standards
- Cross-border quality recognition
- Continuous improvement support

**ECVET integration:**
```json
{
  "credentialSubject": {
    "hasClaim": [{
      "type": "LearningAchievement",
      "title": {"en": "Renewable Energy Installation Micro-credential"},
      "creditReceived": [{"framework": {"notation": "ECVET"}, "point": "5"}],
      "specifiedBy": {
        "type": "Qualification",
        "eqfLevel": {"notation": "4"},
        "learningOutcome": [{
          "title": {"en": "Solar Panel Installation Competence"},
          "relatedESCOSkill": [{"prefLabel": {"en": "Solar energy systems installation"}}]
        }]
      },
      "learningOpportunity": {
        "type": "LearningOpportunity",
        "title": {"en": "Work-based Solar Installation Training"},
        "mode": "work-based learning"
      }
    }]
  }
}
```

#### Use cases and applications

**Work-based learning scenarios:**
- Apprenticeship programmes with stackable micro-credentials
- Company-specific skills training with external certification
- Green and digital transition skill development
- Industry 4.0 competence development

**Career progression pathways:**
- Upskilling for existing workers
- Career transition support
- Professional development in emerging sectors
- International mobility facilitation

### 3.2.2 European VET diploma (EUVETD)

#### Overview and formal qualification

VET diplomas provide comprehensive certification of completed vocational programmes, offering full qualification recognition for skilled professional practice across European labour markets.

#### Qualification characteristics

**Programme completion verification:**
- Full vocational programme certification
- Professional competence comprehensive assessment
- Industry standard alignment
- Quality framework compliance

**Labour market recognition:**
- Professional practice authorisation where applicable
- Cross-border professional mobility support
- Industry recognition and acceptance
- Career progression pathway enablement

### 3.2.3 European VET certificate (EUVETC)

#### Overview and competence certification

VET certificates provide focused competence certification for specific professional skills or knowledge areas, supporting both initial training and continuing professional development.

#### Competence-based structure

**Skill-specific certification:**
- Targeted professional competence verification
- Industry-standard skill assessment
- Quality-assured training programme completion
- Professional development pathway support

**Integration capabilities:**
- Stackability toward larger qualifications
- Professional portfolio building
- Continuing education documentation
- Industry-specific skill verification

## 3.3 Generic educational credentials

### 3.3.1 Degree qualification (EAA2)

#### Overview and sectoral recognition

The degree qualification EAA provides generic qualification certification that can accommodate various types of formal educational qualifications whilst ensuring appropriate trust framework integration and cross-border recognition.

#### EAA characterisation framework

```json
{
  "eaa_id": "EAA2",
  "title": "Degree Qualification",
  "description": "Credential representing a degree or qualification officially conferred by an authorised education provider.",
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

#### Authorisation and verification framework

**Authorised issuers:**
- Higher education institutions with appropriate accreditation
- Vocational education institutions within regulatory scope
- Professional education providers with quality assurance compliance

**Authorised verifiers:**
- Recognition authorities for qualification validation
- Public employment services for labour market integration
- Educational institutions for admission processes
- Professional bodies for licensing and registration

### 3.3.2 European digital credential (EDC)

#### Overview and flexible application

The European digital credential provides a flexible framework supporting various types of educational achievements whilst maintaining compliance with European standards and international interoperability requirements.

#### Implementation versatility

**Multiple qualification types:**
- Formal educational qualifications across all levels
- Non-formal learning achievement documentation
- Professional development certification
- Lifelong learning pathway support

**Standards compliance:**
- ELM v3.2 ontology implementation
- W3C VCDM v1.1 technical compliance
- EBSI infrastructure integration
- Quality assurance framework alignment

## Implementation considerations

### Quality assurance and accreditation

#### Institutional requirements

Implementing formal education EAAs requires:

**Accreditation verification:**
- National quality assurance body recognition
- European quality framework alignment
- Sector-specific accreditation where applicable
- Ongoing compliance monitoring and audit

**Trust service provider registration:**
- eIDAS2 compliance for credential issuance
- DID registration in EBSI infrastructure
- Certificate-DID binding for hybrid trust model
- Revocation and status management capabilities

#### Cross-border recognition framework

**European recognition mechanisms:**
- Automatic recognition where applicable under EU directives
- ENIC-NARIC network integration for information and advice
- Quality assurance framework mutual recognition
- Professional qualification directive compliance

### Technical implementation requirements

#### System integration capabilities

**EUDIW compatibility:**
- OpenID4VCI protocol implementation for credential issuance
- OpenID4VP protocol support for credential presentation
- ISO 18013-5 compliance for international interoperability
- Selective disclosure and privacy protection mechanisms

**Trust registry connectivity:**
- Trusted issuer registry integration for authorisation verification
- Trusted schema registry access for credential type validation
- Status list management for real-time revocation support
- Cross-border verification infrastructure

#### Data protection and privacy

**Privacy by design implementation:**
- Selective disclosure at attribute level
- Purpose limitation for information sharing
- User consent management and control
- Data minimisation principles throughout credential lifecycle

**GDPR compliance:**
- Lawful basis establishment for credential processing
- Data subject rights implementation
- Cross-border data protection safeguards
- Retention and deletion policy enforcement

### User experience and adoption

#### Student and learner empowerment

**Digital literacy support:**
- Credential management training and resources
- Privacy protection education and tools
- Cross-border mobility guidance
- Service access facilitation

**Control and transparency:**
- Clear information about credential capabilities and limitations
- Granular control over information sharing
- Transparent audit trails for credential usage
- Appeal and correction processes for credential errors

#### Institutional change management

**Staff training and development:**
- Technical system operation and management
- Quality assurance and compliance monitoring
- Student support and guidance
- Cross-border recognition procedures

**Process redesign:**
- Credential issuance workflow optimisation
- Verification process automation
- Student service integration
- Quality assurance procedure enhancement

## Future evolution and enhancement

### Emerging technology integration

#### Advanced verification capabilities

**Artificial intelligence integration:**
- Automated fraud detection and prevention
- Intelligent credential verification routing
- Anomaly detection in credential usage patterns
- Enhanced user experience through automation

**Blockchain and distributed ledger innovation:**
- Enhanced trust and transparency mechanisms
- Decentralised verification infrastructure
- Smart contract automation for credential lifecycle
- Immutable audit trails for compliance verification

#### Enhanced privacy protection

**Zero-knowledge proof advancement:**
- Sophisticated privacy-preserving verification
- Attribute verification without information disclosure
- Advanced cryptographic protocol implementation
- User sovereignty enhancement through technical privacy

### International standards alignment

#### Global interoperability

**International framework integration:**
- UNESCO recognition framework alignment
- OECD skills framework integration
- Global professional mobility support
- Third country recognition facilitation

**Technology standards evolution:**
- W3C verifiable credentials v2.0 adoption preparation
- ISO standards compliance and enhancement
- Emerging cryptographic standard integration
- International best practice adoption

This comprehensive framework of formal education achievement EAAs establishes the essential infrastructure for verified, portable, and privacy-preserving educational credentials that support European educational mobility, employment, and lifelong learning whilst maintaining the highest standards of quality, trust, and regulatory compliance.