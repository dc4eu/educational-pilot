# Educational Domain Onboarding: Complete EducationalID Issuance User Journey

## Executive Summary

This document presents the comprehensive narrative for EducationalID issuance within the DC4EU Pilot 2 framework, implementing a No Authorise OpenID VCI flow with **mandatory Verifiable Presentation of PID credentials**. The journey demonstrates sophisticated orchestration between multiple actors, systems, and trust mechanisms that enable secure, interoperable educational credential issuance across European borders.

**Critical Prerequisite**: Before any EducationalID can be issued, the citizen's **Person Identification Data (PID)** must be verified through the eIDAS 2.0 framework. This foundational identity verification is the cornerstone upon which all educational credentials are built.

**Key Innovation**: This implementation showcases the world's first production-ready dPKI system for educational credentials, integrating EBSI trust registries with traditional educational infrastructure to create a seamless, trustworthy credential ecosystem built upon verified foundational identity.

**Bottom Line**: Maria García, a Spanish student, successfully obtains her EducationalID from Universitat Rovira i Virgili through a process that validates her foundational identity via Spanish PID, matches it with university records, and issues a cryptographically secure educational credential recognisable across all European universities.

---

## Table of Contents

1. [Quick Reference Guide](#1-quick-reference-guide)
2. [Infrastructure Prerequisites](#2-infrastructure-prerequisites)
3. [The Story: Maria's Educational Identity Journey](#3-the-story-marias-educational-identity-journey)
4. [Actor Ecosystem and Roles](#4-actor-ecosystem-and-roles)
5. [Technical Architecture Overview](#5-technical-architecture-overview)
6. [Detailed User Journey Flow](#6-detailed-user-journey-flow)
7. [Trust Verification Mechanisms](#7-trust-verification-mechanisms)
8. [Technical Message Details](#8-technical-message-details)
9. [Implementation Insights](#9-implementation-insights)
10. [Appendices](#10-appendices)

---

## 1. Quick Reference Guide

### 1.1 Process Overview

1. **Prerequisites**: University data preparation and identity matching infrastructure
2. **PID Verification**: Mandatory foundational identity validation (Steps 1-22)
3. **Educational ID Issuance**: Institutional credential creation (Steps 23-33)
4. **Cross-Border Recognition**: European-wide validity and trust

### 1.2 Key Actors

- **Student**: Maria García (credential holder)
- **University**: Universitat Rovira i Virgili (dual role: Authentic Source + Issuer)
- **Infrastructure**: EBSI trust registries and verification services
- **Governance**: Spanish Ministry (root trust anchor)

### 1.3 Technical Standards

- **PID Schema**: eIDAS 2.0 Person Identification Data (EU Regulation 2024/2977)
- **EducationalID Schema**: eduGAIN/SCHAC standards for institutional identity
- **Protocols**: OpenID4VCI, W3C Verifiable Credentials, EBSI trust framework

### 1.4 Critical Success Factors

- **Mandatory PID Verification**: No EducationalID can be issued without verified foundational identity
- **Identity Correlation**: Robust matching between legal identity (PID) and institutional records
- **eIDAS 2.0 Compliance**: Full regulatory alignment with European digital identity frameworks
- **Cross-Border Interoperability**: Standards-based approach ensuring European-wide recognition

---

## 2. Infrastructure Prerequisites

### 2.1 Critical Foundation Requirements

Before any EducationalID can be issued, institutions must complete essential infrastructure preparation. This is not optional—it's a **mandatory prerequisite** for participation in the DC4EU framework.

### 2.2 Data Store Preparation for EAA Issuance

#### Student Registry Population

- **Complete enrolment database**: All active students with validated enrolment data
- **Historical records**: Previous academic years and graduation records
- **Programme metadata**: Detailed information about academic programmes and levels
- **Status management**: Real-time enrolment status tracking and updates

#### Identity Correlation Infrastructure

**Core Challenge**: Bridging the gap between **legal identity** (Spanish PID with DNI) and **institutional identity** (university student records)

**Technical Implementation Requirements**:

- **Primary key mapping**: DNI numbers from PID mapped to student database records
- **Validation algorithms**: Automated matching of PID attributes with student records
- **Conflict resolution procedures**: Handling name variations, address changes, etc.
- **Audit trail systems**: Complete logging of all identity matching operations

**Example Data Preparation**:
```
Spanish National Identity → University Student Database
├── DNI: 12345678A → Primary Key: student_id: URV-2023-CS-001234
├── Apellidos: García → family_name: García
├── Nombre: Maria → given_name: Maria
├── Fecha Nacimiento: 2004-03-15 → birth_date: 2004-03-15
└── Estado: Activo → enrolment_status: ACTIVE
```

### 2.3 Identity Matching Mechanisms

#### Multi-Layer Validation Process

1. **Primary Key Correlation**: DNI from PID serves as primary matching key
2. **Attribute Verification**: Name and birth date provide additional confirmation
3. **Enrolment Validation**: Current student status and credential authorisation
4. **Temporal Verification**: Enrolment dates and validity periods

#### Real-Time Matching Infrastructure

- **API-based correlation**: Standardised endpoints for identity resolution
- **Confidence scoring**: Mathematical confidence levels for matching accuracy
- **Exception handling**: Procedures for handling matching conflicts or failures
- **Performance optimisation**: Sub-second response times for user experience

### 2.4 eIDAS 2.0 Compliance Infrastructure

#### Authentic Source Certification

- **Article 45b compliance**: Official certification as eIDAS 2.0 Authentic Source
- **Data quality assurance**: Verified accuracy and completeness of student records
- **API standardisation**: eIDAS 2.0 compliant interfaces for data access
- **Security measures**: Encryption, access control, and audit capabilities

#### Dual Role Architecture

Universities must implement **clear separation** between:

- **Authentic Source function**: Authoritative data repository
- **Issuer function**: Credential creation and issuance
- **API gateway**: Standardised access layer between roles

---

## 3. The Story: Maria's Educational Identity Journey

### 3.1 Setting the Scene

**Meet Maria García**: A 20-year-old computer science student at Universitat Rovira i Virgili (URV) in Catalonia, Spain. Maria is about to begin her second year and needs to establish her digital educational identity to access university services, participate in international exchange programmes, and eventually apply for graduate studies across Europe.

It's Monday morning, September 2025. Maria sits in her dormitory room, smartphone in hand, ready to embark on a digital journey that will transform how she interacts with educational institutions across Europe. Little does she know that behind the simple act of "getting her student ID" lies a sophisticated dance of cryptographic protocols, trust verification systems, and international cooperation frameworks.

### 3.2 The Human Story

**The Challenge**: Maria needs more than just a physical student card. In the digital age of European education, she requires a **Verifiable Educational ID** that:

- Proves her authentic enrolment at URV
- Enables automatic recognition across EU universities
- Integrates with the EUDI Wallet ecosystem
- Supports future mobility and academic recognition

**The Solution**: Through the DC4EU framework, Maria will receive a cryptographically secure, EBSI-anchored Educational ID that serves as her digital passport to the European Education Area. **However, this credential can only be issued after her foundational identity has been verified through her Spanish Person Identification Data (PID)**—a mandatory prerequisite that ensures the highest levels of trust and security.

### 3.3 The Journey Begins

Maria opens her **EUDI Wallet** application, a sleek interface that hides the complexity of European digital identity infrastructure. She taps on "Add Educational Credential" and selects "Universitat Rovira i Virgili" from a list of participating institutions.

What happens next is a masterpiece of digital orchestration, involving multiple actors across different systems, countries, and trust domains.

---

## 4. Actor Ecosystem and Roles

### 4.1 Primary Actors

#### 🎓 Maria García (Natural Person/Student)

- **Role**: Credential holder and primary user
- **Systems**: EUDI Wallet (Mobile Application)
- **Responsibilities**:
  - Initiate credential request
  - Provide consent for data sharing
  - Present PID for verification
  - Accept issued credential into wallet

#### 🏛️ Universitat Rovira i Virgili (Dual Role Institution)

- **Primary Role**: Educational credential issuer
- **Secondary Role**: **eIDAS 2.0 Authentic Source** for student data
- **Systems**: 
  - Student Information System (Authentic Source function)
  - Credential Issuance Infrastructure (Issuer function)
- **Key Personnel**: Registrar Office, Academic Secretary
- **Critical Architecture Note**: URV operates in **dual capacity**:
  - **As Authentic Source**: Maintains authoritative student records under eIDAS 2.0 Article 45b
  - **As Issuer**: Consumes data from its own Authentic Source via standardised APIs
- **Responsibilities**:
  - Verify student enrolment and academic standing (Authentic Source role)
  - Issue cryptographically secure Educational IDs (Issuer role)
  - Maintain clear separation between data provision and credential issuance
  - Integrate with European trust frameworks

### 4.2 Technical Infrastructure Actors

#### 🔐 uSelf Issuer Agent (Credential Issuance Service)

- **Role**: Technical orchestrator for credential issuance
- **Location**: University infrastructure (`lspurv.urv.cat`)
- **Responsibilities**:
  - Manage OpenID4VCI protocol flows
  - Coordinate with EBSI infrastructure
  - Handle cryptographic operations
  - Generate QR codes and credential offers

#### 📊 Authentic Source (Official eIDAS 2.0 Role)

- **Role**: **Official eIDAS 2.0 Authentic Source** - Authoritative repository of verified student information
- **Played by**: Universitat Rovira i Virgili (in dual capacity)
- **System**: Standardised API-accessible student registry with encrypted records
- **eIDAS 2.0 Compliance**: Certified authentic source for educational data under Article 45b
- **Critical Prerequisites**:
  - **Data Store Preparation**: Pre-population of educational data repositories for potential EAA issuance
  - **Identity Matching Infrastructure**: Mechanisms to correlate legal identity (PID) with institutional identity (EducationalID)
  - **Cross-Reference Systems**: Linking Spanish DNI numbers with university student records
- **Responsibilities**:
  - Maintain authoritative student enrolment records
  - Provide standardised API access to verified data
  - Execute real-time identity matching between PID and educational records
  - Ensure data integrity and audit compliance
  - Support continuous synchronisation between legal and institutional identities

#### 🌐 EBSI Infrastructure Ecosystem

**EBSI DID Registry**
- **Role**: Decentralised identifier resolution
- **Function**: Resolve DIDs to cryptographic keys and service endpoints

**EBSI Trust Registry**
- **Role**: Institutional authorisation validation
- **Function**: Verify university's authority to issue educational credentials

**EBSI Schema Registry**
- **Role**: Credential schema validation
- **Function**: Ensure credential format compliance with European standards

**EBSI Proxy**
- **Role**: EBSI integration gateway
- **Function**: Bridge university infrastructure with EBSI services

#### 🆔 uSelf PID Issuer Agent

- **Role**: Personal Identity Data validation service
- **Function**: Verify student's foundational identity credentials

### 4.3 Governance and Oversight Actors

#### 🏛️ Spanish Ministry of Universities and Research

- **Role**: Root Trust Anchor (RootTAO)
- **Authority**: Issues EAA credentials authorising URV to issue Educational IDs
- **Scope**: National level governance and compliance

#### 🇪🇺 European Blockchain Services Infrastructure (EBSI)

- **Role**: European-level trust infrastructure
- **Function**: Provide decentralised trust registry and schema validation
- **Governance**: Multi-national consortium ensuring European standards

### 4.4 Supporting Systems

#### 📱 Student GUI (Web Interface)

- **Role**: User-facing interface for credential requests
- **Location**: `https://uself-verifier-gui.lspurv.urv.cat/`
- **Function**: Generate QR codes and facilitate user interactions

#### 🔗 Mobile Wallet (EUDI Wallet)

- **Role**: Credential storage and presentation
- **Standards**: W3C Verifiable Credentials, OpenID4VP
- **Features**: Multi-format support, selective disclosure, cross-border compatibility

---

## 5. Technical Architecture Overview

### 5.1 System Architecture Diagram

```
┌─────────────────────────┐
│   Student Domain       │
├─────────────────────────┤
│ 👩‍🎓 Maria García        │
│ 📱 EUDI Wallet          │
└─────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────────────────────┐
│   University Infrastructure (lspurv.urv.cat)           │
├─────────────────────────────────────────────────────────┤
│ 🖥️ Student GUI                                         │
│ 🔧 uSelf Issuer Agent                                   │
│ 📊 Authentic Source (eIDAS 2.0 Official Role)          │
│ 🗄️ Student Registry DB                                  │
│ 🔗 Standardised APIs (eIDAS 2.0 Compliant)             │
└─────────────────────────────────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────────────────────┐
│   EBSI Infrastructure                                   │
├─────────────────────────────────────────────────────────┤
│ 🆔 DID Registry                                         │
│ 🛡️ Trust Registry                                       │
│ 📋 Schema Registry                                      │
│ 🌐 EBSI Proxy                                           │
│ 🔐 PID Issuer Agent                                     │
└─────────────────────────────────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────────────────────┐
│   Trust Governance                                      │
├─────────────────────────────────────────────────────────┤
│ 🏛️ Spanish Ministry                                     │
│ 📜 EAA Credentials (Authentic Source Authority)         │
└─────────────────────────────────────────────────────────┘
```

**Key Architectural Principle**: The university operates in **dual capacity** under eIDAS 2.0:

1. **As Authentic Source**: Authoritative holder of student data (Article 45b compliance)
2. **As Issuer**: Consumer of authentic source data via standardised APIs for credential creation

### 5.2 Trust Flow Architecture

The system implements a sophisticated **multi-layer trust model**:

1. **Foundational Layer**: Spanish national identity infrastructure provides PID
2. **Institutional Layer**: URV's authorisation via Spanish Ministry EAA credentials
3. **European Layer**: EBSI trust registries validate cross-border recognition
4. **Technical Layer**: Cryptographic proofs ensure credential integrity

### 5.3 Protocol Stack

- **Application Layer**: OpenID for Verifiable Credentials (OID4VCI)
- **Credential Layer**: W3C Verifiable Credentials Data Model
- **Trust Layer**: EBSI trust registries and EAA framework
- **Cryptographic Layer**: ES256 signatures, DID-based authentication
- **Transport Layer**: HTTPS with additional security headers

---

## 6. Detailed User Journey Flow

### 6.1 Phase 1: Journey Initiation (Steps 1-6)

#### Step 1: The Request
*Monday, 9:15 AM - Maria's dormitory*

Maria opens her web browser and navigates to the URV student portal. The interface is clean and multilingual, supporting both Catalan and Spanish as befitting the region's linguistic diversity.

**Technical Action**: 
```http
GET https://student-web/issue
```

**Behind the Scenes**: The student GUI system initialises, checking server status and preparing the credential issuance infrastructure.

#### Step 2: Credential Offer Generation
*The system springs into action*

The Student GUI communicates with the uSelf Issuer Agent to generate a credential offer specifically tailored for Educational ID issuance.

**Technical Exchange**:
```http
GET https://uself-agent/issuer/credential-offer
```

**Response**: The agent generates a unique credential offer containing:
- Credential type: `VerifiableEducationalID`
- Supported formats: `jwt_vc` (W3C Verifiable Credentials)
- Issuer identity: URV's DID
- Security nonce for replay protection

#### Step 3: QR Code Magic
*The bridge between digital and physical*

The Student GUI receives the credential offer and transforms it into a QR code—a visual bridge between the web interface and Maria's mobile wallet.

**Technical Implementation**:
```bash
openid-credential-offer://?credential_offer_uri=https://issuer.eu/issuer/offers/719307744250317677
```

The QR code contains not the full credential offer (which would be too large) but a secure URI pointing to the offer details. This follows EBSI recommendations for optimal user experience.

#### Step 4: Mobile Engagement
*Maria scans the QR code*

Maria holds up her EUDI Wallet and scans the QR code. The wallet's sophisticated parsing engine recognises the OpenID credential offer format and prepares for the issuance flow.

**User Experience**: The wallet displays a clear, user-friendly interface:
- "Universitat Rovira i Virgili wants to issue your Educational ID"
- "This credential will allow you to access university services and participate in European student mobility"
- "Tap to continue"

#### Step 5: Protocol Handshake Initiation
*Behind the scenes coordination*

The mobile wallet processes the QR code and initiates the OpenID4VCI flow, establishing a secure communication channel with the university's systems.

**Technical Flow**:
```http
HTTP 302 Redirect to Authorization Endpoint
```

#### Step 6: Authorization Request
*Establishing trust*

The wallet constructs a formal authorisation request, following the OpenID4VCI "No Authorize" flow pattern. **Crucially, this flow requires mandatory presentation of a PID (Person Identification Data) credential to verify Maria's foundational identity.**

**Why PID Verification is Mandatory**:
- **Legal Requirement**: eIDAS 2.0 mandates foundational identity verification for official credentials
- **Trust Foundation**: Educational credentials must be anchored to verified national identity
- **Cross-Border Recognition**: PID provides the common trust baseline across all EU Member States
- **Fraud Prevention**: Prevents identity theft and credential misuse

**Authorization URL Construction**:
```http
GET https://uself-agent/auth/authorize?
client_id=https://issuer.eu/auth
&response_type=vp_token
&response_mode=direct_post  
&scope=openid
&presentation_definition={MANDATORY_PID_PRESENTATION_REQUIREMENTS}
```

**Technical Note**: The `presentation_definition` specifically requires a valid PID credential—no EducationalID can be issued without this foundational verification step.

### 6.2 Phase 2: Foundational Identity Verification - The Mandatory PID Process (Steps 7-22)

**Critical Process Note**: This phase represents the **absolute prerequisite** for EducationalID issuance. Under eIDAS 2.0 regulations and DC4EU framework requirements, **no educational credential can be issued without verified foundational identity**. The PID verification process ensures that Maria's educational credentials are anchored to her legally verified national identity.

#### Step 7: The Trust Challenge
*Proving who you are at the foundational level*

The uSelf Issuer Agent responds with a **direct_post** challenge, requesting Maria to present her PID credential. This is not optional—it's a **mandatory step** that forms the foundation of all subsequent trust relationships.

**User Experience**: Maria's wallet displays:
- "⚠️ **Identity Verification Required**: To issue your Educational ID, the university must verify your foundational identity"
- "🆔 **Spanish PID Required**: Please present your Person Identification Data (PID) issued by Spanish authorities"
- "🔒 **Security Notice**: This verification is mandatory under eIDAS 2.0 regulations"
- "ℹ️ This information will be used only for identity verification purposes"

#### Step 8: Consent and Privacy
*Maria takes control - but verification is mandatory*

This is a crucial moment in the user journey. While Maria must provide explicit consent to share her PID with the university, **she cannot proceed without this verification**. The EUDI Wallet presents clear information about:

**Mandatory Requirements**:
- ✅ **PID Verification**: Required for all educational credentials under eIDAS 2.0
- ✅ **Identity Attributes**: Minimum necessary data for foundational verification
- ✅ **Legal Basis**: Regulatory requirement, not optional preference

**User Control Elements**:
- 🎛️ **Selective Disclosure**: Choose which PID attributes to share beyond the minimum required
- 🕐 **One-Time Use**: PID data used only for this verification, not stored
- 🚫 **Right to Refuse**: Maria can decline, but no EducationalID will be issued

**Privacy Innovation**: The system implements selective disclosure, allowing Maria to share only the **minimum necessary PID attributes** beyond the eIDAS 2.0 required fields. For EducationalID issuance, typically only these attributes are shared:

**Mandatory for Educational Credential**:
- ✅ `family_name`, `given_name` (identity verification)
- ✅ `birth_date` (age verification and identity matching)
- ✅ `nationality` (eligibility verification)
- ✅ `personal_administrative_number` (unique identification)
- ✅ `issuing_country`, `issuing_authority` (credential validation)

**Optional/Privacy-Protected**:
- 🔒 `resident_address`, `resident_street`, `resident_house_number` (not needed)
- 🔒 `portrait` (photo - only if required by institution)
- 🔒 `email_address`, `mobile_phone_number` (contact info - optional)
- 🔒 `sex` (not relevant for educational credentials)

#### Steps 9-10: The Digital Handshake
*Secure credential presentation - foundational identity proven*

Maria taps "Share PID" and the wallet constructs a **Verifiable Presentation containing her mandatory PID credential**. This presentation is cryptographically signed and includes:
- **The PID credential** issued by Spanish national authorities (mandatory)
- **A presentation proof** signed by Maria's wallet (mandatory)
- **Metadata** about the presentation context (mandatory)
- **Selective attributes** chosen by Maria (optional beyond minimum)

**Technical Exchange**:
```http
POST https://uself-agent/direct_post
Content-Type: application/json

{
  "vp_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiJ9...",
  "presentation_submission": {
    "id": "pid-verification-submission",
    "definition_id": "mandatory-pid-presentation",
    "descriptor_map": [{
      "id": "spanish-pid-requirement",
      "path": "$.verifiableCredential[0]",
      "format": "jwt_vc"
    }]
  },
  "state": "92b6e05c-5c3b-4194-bba8-1da1b2a5dd62"
}
```

**Maria's PID Credential Structure** (eIDAS 2.0 Compliant):

Maria's PID credential follows the official eIDAS 2.0 Person Identification Data schema, containing essential identity attributes such as:
- **Core Identity**: Family name (García), given name (Maria), birth date, birth place
- **Legal Status**: Spanish nationality, personal administrative number (DNI)
- **Administrative Details**: Issuing authority, country (ES), jurisdiction (ES-CT for Catalonia)
- **Validity**: Expiry date and document number

**Key eIDAS 2.0 PID Attributes**:
- **Required Core Identity**: `family_name`, `given_name`, `birth_date`, `birth_place`
- **Nationality & Residence**: `nationality` (ES), `resident_country`, `resident_state`
- **Administrative**: `personal_administrative_number` (Spanish DNI)
- **Validity**: `expiry_date`, `issuing_authority`, `issuing_country`
- **Jurisdiction**: `issuing_jurisdiction` (ES-CT for Catalonia)

#### Steps 11-21: The Foundational Trust Verification Symphony
*EBSI infrastructure validates Maria's foundational identity*

What happens next is invisible to Maria but represents **the most critical trust verification process** in the entire digital credential ecosystem. The uSelf Issuer Agent orchestrates a **comprehensive verification of Maria's foundational identity** across multiple EBSI services:

**Steps 11-12: PID DID Resolution**
```http
GET https://ebsi-did-registry/did/{maria-pid-issuer-did}
```
**Purpose**: Resolve the DID of the Spanish authority that issued Maria's PID to verify the cryptographic keys and ensure the PID credential is properly signed by legitimate national authorities.

**Steps 13-14: National Authority Trust Registry Verification**
```http
GET https://ebsi-tr-registry/tr
```
**Purpose**: Check the EBSI Trust Registry to verify that the Spanish national identity authorities are officially authorised to issue Person Identification Data credentials under eIDAS 2.0.

**Steps 15-16: PID Schema Validation**
```http
GET https://ebsi-schema-registry/schema
```
**Purpose**: Validate that Maria's PID credential conforms to the official European PID schema and data format requirements.

**Steps 17-20: Comprehensive PID Verification**
```http
GET https://ebsi-proxy/verify
```
**Purpose**: The EBSI Proxy performs the **complete foundational identity verification**, including:
- ✅ **Cryptographic signature validation** of the PID credential
- ✅ **Revocation status checking** to ensure the PID hasn't been revoked
- ✅ **Trust chain verification** back to Spanish national authorities
- ✅ **eIDAS 2.0 compliance verification** for regulatory alignment
- ✅ **Temporal validity checking** to ensure the PID is currently valid

**Steps 21-22: Foundational Identity Verification Success**
The comprehensive verification process completes successfully, **confirming Maria's foundational identity**, and the system issues an authorization code to proceed with Educational ID issuance.

**Verification Result**: The system now has **cryptographic proof** that:
- Maria is who she claims to be (verified by Spanish national authorities)
- Her identity credential is valid and not revoked
- The verification complies with all eIDAS 2.0 requirements
- She is legally authorised to receive educational credentials in Spain

### 6.3 Phase 3: Credential Issuance (Steps 23-33)

#### Steps 23-24: Access Token Exchange
*Authorization to proceed*

The wallet receives the authorization code and exchanges it for an access token, following OAuth 2.0 security patterns.

**Technical Exchange**:
```http
POST https://uself-agent/auth/token
Content-Type: application/x-www-form-urlencoded

grant_type=authorization_code
&client_id=did:key:z2dmzD81cgPx8Vki7JbuuMmFYrWPgYoytykUZ3eyqht1j9Kbndi4FzE7bq9irPGQVyZG7SWHy8iqpKMjjhmtB7JF3eFYnM67SxNd4gjT3DsKUb7NKeKLcNTEocYUf2kpBQRQqCvGMCvC87F8jgydShFCPTwrDpvJKrZMdq8zjQLQxwW2kL
&code=glkFFoisdfEui4312
```

#### Steps 25-26: The Moment of Truth
*Credential creation*

With valid authorization, the wallet sends the formal credential request. This triggers the creation of Maria's Educational ID.

**Credential Request**:
```http
POST https://uself-agent/issuer/credential
Authorization: Bearer access_token
Content-Type: application/json

{
  "credential_definition": {
    "type": ["VerifiableCredential", "VerifiableEducationalID"],
    "format": "jwt_vc"
  },
  "proof": {
    "proof_type": "jwt",
    "jwt": "wallet_proof_jwt"
  }
}
```

#### Steps 27-30: Authentic Source Data Retrieval via Standardised APIs
*The crucial eIDAS 2.0 separation of roles*

This step represents a **critical architectural principle** of eIDAS 2.0 implementation and demonstrates the **pre-established identity matching infrastructure**. Although URV operates both as the **Authentic Source** and the **Issuer**, these roles are clearly separated:

**eIDAS 2.0 Compliance**: The university's Authentic Source function operates independently of its Issuer function, ensuring:
- **Data integrity**: Authoritative student records maintained separately from credential issuance
- **Identity correlation**: Pre-established matching between PID legal identity and educational records
- **Audit compliance**: Clear separation between data provision and credential creation
- **Regulatory alignment**: Full compliance with eIDAS 2.0 Article 45b requirements

**Identity Matching Process**: The critical moment where **legal identity meets institutional identity**:

1. **PID Identity Extraction**: From Maria's verified PID:
   - `personal_administrative_number`: "12345678A" (Spanish DNI)
   - `family_name`: "García"
   - `given_name`: "Maria"
   - `birth_date`: "2004-03-15"

2. **Authentic Source Lookup**: Using the DNI as primary key:
   ```http
   GET https://auth-source/educationalId/12345678A
   Authorization: Bearer authentic_source_token
   Content-Type: application/json
   X-eIDAS-Authentic-Source: true
   X-Identity-Matching-Required: true
   ```

3. **Identity Validation**: The authentic source performs **automatic identity matching**:
   - **Primary Match**: DNI "12345678A" → Student ID in database
   - **Name Verification**: "García, Maria" → Student record validation
   - **Birth Date Confirmation**: "2004-03-15" → Additional identity verification
   - **Enrolment Verification**: Current active enrolment status

**Database Query (Internal to Authentic Source)**:
```sql
SELECT s.studentId, s.enrolmentStatus, s.programme, s.level, 
       s.enrolmentDate, s.expectedGraduation, s.institution,
       p.dni, p.apellidos, p.nombre, p.fecha_nacimiento
FROM students s 
INNER JOIN personas p ON s.persona_id = p.id
WHERE p.dni = '12345678A'
  AND p.apellidos = 'García'
  AND p.nombre = 'Maria'
  AND p.fecha_nacimiento = '2004-03-15'
  AND s.status = 'ACTIVE'
  AND s.authorizedCredentialIssuance = true
```

**Authentic Source Response**:

The authentic source provides a comprehensive response that demonstrates successful **identity matching** between Maria's legal identity (PID) and her institutional identity (student record). This response includes both the verified correlation and the educational data needed for EducationalID issuance.

```json
{
  "authenticSourceMetadata": {
    "sourceId": "urn:es:urv:authentic-source:students",
    "certification": "eIDAS-2.0-compliant",
    "lastUpdated": "2025-09-02T09:15:00Z",
    "dataClassification": "official-educational-record",
    "apiVersion": "v2.1",
    "complianceFramework": "eIDAS-2.0-Article-45b",
    "identityMatchingPerformed": true,
    "matchingAlgorithmVersion": "v3.2"
  },
  "identityMatchingResults": {
    "pidToStudentMapping": {
      "primaryKeyMatch": {
        "pidAttribute": "personal_administrative_number",
        "pidValue": "12345678A",
        "studentRecordField": "dni",
        "matchStatus": "EXACT_MATCH",
        "confidence": 1.0
      },
      "nameValidation": {
        "pidFamilyName": "García",
        "pidGivenName": "Maria",
        "studentFamilyName": "García",
        "studentGivenName": "Maria",
        "matchStatus": "EXACT_MATCH",
        "confidence": 1.0
      },
      "birthDateValidation": {
        "pidBirthDate": "2004-03-15",
        "studentBirthDate": "2004-03-15",
        "matchStatus": "EXACT_MATCH",
        "confidence": 1.0
      },
      "overallMatchResult": {
        "status": "VERIFIED",
        "confidence": 1.0,
        "verificationTimestamp": "2025-09-02T09:29:43Z"
      }
    }
  },
  "studentRecord": {
    "pidMapping": {
      "family_name": "García",
      "given_name": "Maria",
      "personal_administrative_number": "12345678A",
      "nationality": "ES",
      "birth_date": "2004-03-15"
    },
    "institutionalIdentity": {
      "identifier": "maria.garcia@estudiants.urv.cat",
      "enrolmentStatus": "ACTIVE",
      "schacPersonalUniqueCode": [
        "urn:schac:personalUniqueCode:int:esi:urv.cat:12345678A",
        "urn:schac:personalUniqueCode:int:esi:ES:12345678A"
      ],
      "schacPersonalUniqueID": "urn:schac:personalUniqueID:ES:12345678A",
      "schacHomeOrganization": "urv.cat",
      "familyName": "García",
      "firstName": "Maria",
      "displayName": "Maria García",
      "dateOfBirth": "2004-03-15",
      "commonName": "Maria García",
      "mail": "maria.garcia@estudiants.urv.cat",
      "eduPersonPrincipalName": "maria.garcia@estudiants.urv.cat",
      "eduPersonPrimaryAffiliation": "student",
      "eduPersonAffiliation": ["member", "student"],
      "eduPersonScopedAffiliation": ["student@urv.cat", "member@urv.cat"],
      "eduPersonAssurance": [
        "https://refeds.org/assurance/IAP/low",
        "https://refeds.org/assurance/ID/unique"
      ]
    },
    "enrolmentDetails": {
      "institution": "Universitat Rovira i Virgili",
      "institutionCode": "ES-URV-25025",
      "enrolmentDate": "2023-09-15",
      "expectedGraduation": "2027-06-30",
      "credentialIssuanceAuthorised": true,
      "lastVerificationDate": "2025-09-01T00:00:00Z"
    }
  },
  "verificationProof": {
    "signedBy": "authentic-source-signing-key",
    "timestamp": "2025-09-02T09:29:45Z",
    "integrityHash": "sha256:a1b2c3d4e5f6789abcdef1234567890",
    "auditTrail": "urn:audit:es:urv:2025:09:02:09:29:45:maria-garcia",
    "identityMatchingAudit": "urn:audit:es:urv:identity-matching:2025:09:02:09:29:43:12345678A"
  }
}
```

**Critical Identity Matching Results**:
- ✅ **DNI Match**: 12345678A found in student database
- ✅ **Name Match**: García, Maria confirmed in enrolment records  
- ✅ **Birth Date Match**: 2004-03-15 validated against university records
- ✅ **Enrolment Verified**: Active student status confirmed
- ✅ **Credential Authorisation**: Student authorised for EducationalID issuance

**Architectural Innovation**: This design demonstrates how eIDAS 2.0 enables institutional **dual roles** while maintaining:
- **Trust boundaries**: Clear separation of functions even within the same organisation
- **Identity correlation**: Robust matching between legal and institutional identity
- **Interoperability**: Standardised APIs that work across organisational boundaries
- **Compliance**: Full regulatory alignment with European digital identity frameworks

#### Step 31: Credential Generation
*The digital birth certificate*

The agent constructs Maria's Educational ID credential using the **eduGAIN/SCHAC-based schema** rather than ELM. This credential follows the specific EducationalID schema designed for non-foundational identity in educational contexts.

The generated EducationalID credential incorporates:
- **Verified Identity Data**: From the PID verification process
- **Educational Attributes**: Following eduGAIN/SCHAC standards
- **Institutional Affiliation**: URV-specific organisational data
- **Assurance Levels**: REFEDS framework compliance

**Generated EducationalID Credential**:
```json
{
  "@context": [
    "https://www.w3.org/2018/credentials/v1",
    "https://ebsi.eu/schemas/v1",
    "https://schema.org"
  ],
  "id": "urn:uuid:6ba7b810-9dad-11d1-80b4-00c04fd430c8",
  "type": ["VerifiableCredential", "VerifiableEducationalID"],
  "issuer": {
    "id": "did:ebsi:zNKuKosKmLHBfWcfBsXXkYQRGStVQLYL5DcJgzN1VJ2S2",
    "name": "Universitat Rovira i Virgili",
    "description": "Official Educational Credential Issuer"
  },
  "issuanceDate": "2025-09-02T09:30:00Z",
  "expirationDate": "2027-06-30T23:59:59Z",
  "credentialSubject": {
    "id": "did:key:z2dmzD81cgPx8Vki7JbuuMmFYrWPgYoytykUZ3eyqht1j9Kbh4",
    "identifier": "maria.garcia@estudiants.urv.cat",
    "schacPersonalUniqueCode": [
      "urn:schac:personalUniqueCode:int:esi:urv.cat:12345678A",
      "urn:schac:personalUniqueCode:int:esi:ES:12345678A"
    ],
    "schacPersonalUniqueID": "urn:schac:personalUniqueID:ES:12345678A",
    "schacHomeOrganization": "urv.cat",
    "familyName": "García",
    "firstName": "Maria",
    "displayName": "Maria García",
    "dateOfBirth": "2004-03-15",
    "mail": "maria.garcia@estudiants.urv.cat",
    "eduPersonPrincipalName": "maria.garcia@estudiants.urv.cat",
    "eduPersonPrimaryAffiliation": "student",
    "eduPersonAffiliation": ["member", "student"],
    "eduPersonScopedAffiliation": ["student@urv.cat", "member@urv.cat"],
    "eduPersonAssurance": [
      "https://refeds.org/assurance/IAP/low",
      "https://refeds.org/assurance/ID/unique"
    ]
  },
  "credentialSchema": {
    "id": "https://api.preprod.ebsi.eu/trusted-schemas-registry/v1/schemas/0xbf78fc08a7a9f28f5479f58dea269d3657f54f13ca37d380cd4e92237fb691dd",
    "type": "JsonSchemaValidator2018"
  },
  "evidence": [
    {
      "id": "urn:evidence:pid-verification:12345678A",
      "type": ["DocumentVerification"],
      "verifier": "did:ebsi:spanish-national-authority",
      "evidenceDocument": "eIDAS-2.0-PID",
      "subjectPresence": "Digital",
      "documentPresence": "Digital"
    }
  ],
  "proof": {
    "type": "JsonWebSignature2020",
    "created": "2025-09-02T09:30:00Z",
    "proofPurpose": "assertionMethod",
    "verificationMethod": "did:ebsi:zNKuKosKmLHBfWcfBsXXkYQRGStVQLYL5DcJgzN1VJ2S2#keys-1",
    "jws": "eyJhbGciOiJFUzI1NiIsImI2NCI6ZmFsc2UsImNyaXQiOlsiYjY0Il19.."
  }
}
```

#### Step 32: Event Notification
*System coordination*

The agent sends a `credential_issued` event to the Student GUI, enabling real-time updates to any connected systems and maintaining audit trails for compliance purposes.

#### Step 33: Delivery to Maria
*The moment of completion*

The Educational ID credential is delivered to Maria's EUDI Wallet. The wallet validates the credential signature, stores it securely, and notifies Maria of successful issuance.

**User Experience**: Maria sees a success notification:
- "✅ Your Educational ID has been issued successfully!"
- "🎓 You can now access university services and participate in international programmes"
- "📅 This credential is valid until 30 June 2027"
- "🔒 Your credential is cryptographically secured and recognised across Europe"

---

## 7. Trust Verification Mechanisms

### 7.1 Multi-Layer Trust Architecture with eIDAS 2.0 Compliance

The EducationalID issuance process implements sophisticated **multi-layer trust verification** with full eIDAS 2.0 regulatory alignment, **built upon mandatory foundational identity verification**:

#### Layer 1: Foundational Identity (PID) - MANDATORY PREREQUISITE
- **Role**: **Absolute prerequisite** for all educational credentials
- **Source**: Spanish national identity infrastructure
- **Verification**: eIDAS-compliant digital identity (mandatory)
- **Assurance Level**: High (Level of Assurance 3)
- **Cryptographic Standard**: ES256 signatures
- **Legal Basis**: eIDAS 2.0 Article 3 - foundational identity requirement
- **Process**: **Complete EBSI verification of PID before any educational credential issuance**

#### Layer 2: Authentic Source Authority (eIDAS 2.0 Article 45b)
- **Role**: URV as certified eIDAS 2.0 Authentic Source
- **Authority**: Spanish Ministry EAA credentials authorising authentic source function
- **Data Integrity**: Authoritative student records with cryptographic proofs
- **API Standards**: eIDAS 2.0 compliant standardised access protocols
- **Dependency**: **Only operates after Layer 1 (PID) verification is complete**

#### Layer 3: Institutional Issuance Authority (EAA)
- **Source**: Spanish Ministry of Universities and Research
- **Mechanism**: Electronic Attestation of Attributes (EAA)
- **Scope**: Authorises URV to issue Educational IDs based on authentic source data
- **Validation**: EBSI Trust Registry verification
- **Prerequisite**: **Requires verified foundational identity from Layer 1**

#### Layer 4: European Recognition (EBSI)
- **Framework**: European Blockchain Services Infrastructure
- **Function**: Cross-border trust propagation
- **Standards**: W3C Verifiable Credentials, eduGAIN/SCHAC
- **Governance**: Multi-national European cooperation
- **Foundation**: **Built upon verified PID from Layer 1**

#### Layer 5: Technical Integrity
- **Cryptography**: Multiple signature verification
- **Revocation**: Real-time status checking
- **Audit**: Comprehensive logging and traceability
- **Privacy**: Selective disclosure and data minimisation
- **Anchor**: **All technical integrity traces back to verified PID**

### 7.2 Trust Chain Example with eIDAS 2.0 Roles

```
🇪🇺 European Union (eIDAS 2.0 Regulatory Framework)
  ↓
🇪🇸 Spanish Ministry of Universities (Root Trust Anchor)
  ↓ [Issues EAA - Authentic Source Authority]
🏛️ URV as Authentic Source (eIDAS 2.0 Article 45b Role)
  ↓ [Standardised API provides verified data]
🔧 URV as Issuer (EAA-Authorised Credential Issuer)
  ↓ [Issues Educational ID based on authentic source data]
👩‍🎓 Maria García (Credential Holder)
  ↓ [Presents Credential]
🏫 Any European University (Relying Party)
```

**Key Innovation**: The dual role architecture demonstrates how institutions can operate as both **Authentic Source** and **Issuer** under eIDAS 2.0 whilst maintaining clear functional separation and regulatory compliance.

### 7.3 Security Properties

- **Authenticity**: Cryptographically proven issuer identity
- **Integrity**: Tamper-evident credential structure  
- **Non-repudiation**: Immutable audit trail
- **Privacy**: Minimal data disclosure with consent
- **Availability**: Distributed verification infrastructure
- **Interoperability**: European standards compliance

---

## 8. Technical Message Details

### 8.1 Credential Offer Response (Complete)

The credential offer provides comprehensive metadata about the EducationalID credential, including display parameters and supported credential subject attributes:

```json
{
   "credential_issuer":"https://lspurv.urv.cat/issuer",
   "credentials":[
      {
         "format":"jwt_vc",
         "types":[
            "VerifiableCredential",
            "VerifiableEducationalID"
         ],
         "trust_framework":{
            "name":"URV Educational Credential Issuer",
            "type":"VerifiableEducationalID",
            "uri":"https://dc4eu.eu/schemas/educational-id"
         },
         "display":[
            {
               "name":"Educational ID",
               "description":"Verifiable Educational Identity for European Student Mobility",
               "locale":"en-GB"
            },
            {
               "name":"Identificació Educativa",
               "description":"Identitat Educativa Verificable per a la Mobilitat Estudiantil Europea",
               "locale":"ca"
            }
         ],
         "credentialSubject":{
            "identifier":{
               "display":[
                  {
                     "name":"Student Identifier",
                     "description":"Unique educational identifier"
                  }
               ]
            },
            "schacPersonalUniqueCode":{
               "display":[
                  {
                     "name":"SCHAC Unique Code",
                     "description":"Standardised unique identifier for European educational systems"
                  }
               ]
            },
            "familyName":{
               "display":[
                  {
                     "name":"Family Name",
                     "description":"Student's family name"
                  }
               ]
            },
            "firstName":{
               "display":[
                  {
                     "name":"First Name",
                     "description":"Student's given name"
                  }
               ]
            },
            "eduPersonScopedAffiliation":{
               "display":[
                  {
                     "name":"Educational Affiliation",
                     "description":"Student's role within the educational institution"
                  }
               ]
            }
         }
      }
   ]
}
```

**Key Features**:
- **Credential Type**: `VerifiableEducationalID` with `jwt_vc` format
- **Display Configuration**: URV branding and multilingual support (English, Catalan)
- **Attribute Mapping**: Complete eduGAIN/SCHAC attribute support
- **Cryptographic Binding**: ES256 algorithm with DID-based binding

### 8.2 Authorization Request (Complete)

The authorization request demonstrates sophisticated presentation definition validation ensuring only valid **eIDAS 2.0 compliant PID credentials** are accepted:

```http
GET https://lspurv.urv.cat/auth/authorize?
client_id=https://issuer.eu/auth
&response_type=vp_token
&response_mode=direct_post
&scope=openid
&presentation_definition={
  "id": "mandatory-pid-presentation",
  "input_descriptors": [
    {
      "id": "spanish-pid-requirement",
      "name": "Spanish Person Identification Data",
      "purpose": "Foundational identity verification required under eIDAS 2.0",
      "constraints": {
        "fields": [
          {
            "path": ["$.type"],
            "filter": {
              "type": "array",
              "contains": {
                "const": "PersonIdentificationData"
              }
            }
          },
          {
            "path": ["$.credentialSubject.family_name"],
            "filter": {
              "type": "string"
            }
          },
          {
            "path": ["$.credentialSubject.given_name"],
            "filter": {
              "type": "string"
            }
          },
          {
            "path": ["$.credentialSubject.birth_date"],
            "filter": {
              "type": "string",
              "format": "date"
            }
          },
          {
            "path": ["$.credentialSubject.personal_administrative_number"],
            "filter": {
              "type": "string"
            }
          },
          {
            "path": ["$.credentialSubject.issuing_country"],
            "filter": {
              "const": "ES"
            }
          }
        ]
      }
    }
  ]
}
```

**Key Validation Requirements**:
- ✅ **Credential Type**: Must be `PersonIdentificationData` (eIDAS 2.0 PID)
- ✅ **Required Fields**: `family_name`, `given_name`, `birth_date`, `nationality`
- ✅ **Administrative Number**: `personal_administrative_number` for unique identification
- ✅ **Issuing Country**: Must be "ES" (Spain) for this university
- ✅ **Cryptographic Validation**: ES256 signature algorithm required

### 8.3 Final Credential Response

The final credential response delivers the completed EducationalID to Maria's EUDI Wallet in JWT format, cryptographically signed by URV's institutional key:

```json
{
   "credential": "eyJ0eXAiOiJ2YytsZCtqc29uIiwiYWxnIjoiRVMyNTYiLCJraWQiOiJkaWQ6ZWJzaTp6TktuS29zS21MSEJmV2NmQnNYWGtZUVJHU3RWUUVZD5dGNDNnZ3pOMVZKMlMyI2tleXMtMSJ9.eyJpc3MiOiJkaWQ6ZWJzaTp6TktuS29zS21MSEJmV2NmQnNYWGtZUVJHU3RWUUFMWTQ3Y2pnekA1aUoyUzIiLCJuYmYiOjE2OTExMzI4MDAsImV4cCI6MTc1NDM3ODc5OSwiaWF0IjoxNjkxMTMyODAwLCJ2YyI6eyJAY29udGV4dCI6WyJodHRwczovL3d3dy53My5vcmcvMjAxOC9jcmVkZW50aWFscy92MSIsImh0dHBzOi8vZWJzaS5ldS9zY2hlbWFzL3YxIl0sImlkIjoidXJuOnV1aWQ6NmJhN2I4MTAtOWRhZC0xMWQxLTgwYjQtMDBjMDRmZDQzMGM4IiwidHlwZSI6WyJWZXJpZmlhYmxlQ3JlZGVudGlhbCIsIlZlcmlmaWFibGVFZHVjYXRpb25hbElEIl0sImlzc3VlciI6eyJpZCI6ImRpZDplYnNpOnpOS25Lb3NLbUxIQmZXY2ZCc1hYa1lRUkdTdFZRQUFMWTQ3Y2pnek01VnE2UzIiLCJuYW1lIjoiVW5pdmVyc2l0YXQgUm92aXJhIGkgVmlyZ2lsaSIsImRlc2NyaXB0aW9uIjoiT2ZmaWNpYWwgRWR1Y2F0aW9uYWwgQ3JlZGVudGlhbCBJc3N1ZXIifSwiaXNzdWFuY2VEYXRlIjoiMjAyNS0wOS0wMlQwOTozMDowMFoiLCJleHBpcmF0aW9uRGF0ZSI6IjIwMjctMDYtMzBUMjM6NTk6NTlaIiwiY3JlZGVudGlhbFN1YmplY3QiOnsiaWQiOiJkaWQ6a2V5OnoyZG16RDgxY2dQeDhWa2k3SmJ1dU1tRllyV1BnWW95dHlrVVozZXlxaHQxajlLYmg0IiwiaWRlbnRpZmllciI6Im1hcmlhLmdhcmNpYUBlc3R1ZGlhbnRzLnVydi5jYXQiLCJzY2hhY1BlcnNvbmFsVW5pcXVlQ29kZSI6WyJ1cm46c2NoYWM6cGVyc29uYWxVbmlxdWVDb2RlOmludDplc2k6dXJ2LmNhdDoxMjM0NTY3OEEiLCJ1cm46c2NoYWM6cGVyc29uYWxVbmlxdWVDb2RlOmludDplc2k6RVM6MTIzNDU2NzhBIl0sInNjaGFjUGVyc29uYWxVbmlxdWVJRCI6InVybjpzY2hhYzpwZXJzb25hbFVuaXF1ZUlEOkVTOjEyMzQ1Njc4QSIsInNjaGFjSG9tZU9yZ2FuaXphdGlvbiI6InVydi5jYXQiLCJmYW1pbHlOYW1lIjoiR2FyY8OtYSIsImZpcnN0TmFtZSI6Ik1hcmlhIiwiZGlzcGxheU5hbWUiOiJNYXJpYSBHYXJjw61hIiwiZGF0ZU9mQmlydGgiOiIyMDA0LTAzLTE1IiwibWFpbCI6Im1hcmlhLmdhcmNpYUBlc3R1ZGlhbnRzLnVydi5jYXQiLCJlZHVQZXJzb25QcmluY2lwYWxOYW1lIjoibWFyaWEuZ2FyY2lhQGVzdHVkaWFudHMudXJ2LmNhdCIsImVkdVBlcnNvblByaW1hcnlBZmZpbGlhdGlvbiI6InN0dWRlbnQiLCJlZHVQZXJzb25BZmZpbGlhdGlvbiI6WyJtZW1iZXIiLCJzdHVkZW50Il0sImVkdVBlcnNvblNjb3BlZEFmZmlsaWF0aW9uIjpbInN0dWRlbnRAdXJ2LmNhdCIsIm1lbWJlckB1cnYuY2F0Il0sImVkdVBlcnNvbkFzc3VyYW5jZSI6WyJodHRwczovL3JlZmVkcy5vcmcvYXNzdXJhbmNlL0lBUC9sb3ciLCJodHRwczovL3JlZmVkcy5vcmcvYXNzdXJhbmNlL0lEL3VuaXF1ZSJdfSwiZXZpZGVuY2UiOlt7ImlkIjoidXJuOmV2aWRlbmNlOnBpZC12ZXJpZmljYXRpb246MTIzNDU2NzhBIiwidHlwZSI6WyJEb2N1bWVudFZlcmlmaWNhdGlvbiJdLCJ2ZXJpZmllciI6ImRpZDplYnNpOnNwYW5pc2gtbmF0aW9uYWwtYXV0aG9yaXR5Iiwic3ViamVjdFByZXNlbmNlIjoiRGlnaXRhbCIsImRvY3VtZW50UHJlc2VuY2UiOiJEaWdpdGFsIn1dfSwic3ViIjoiZGlkOmtleTp6MmRtekQ4MWNnUHg4VmtpN0pidXVNbUZZcldQZ1lveXR5a1VaM2V5cWh0MWo5S2JoNCJ9.BjH8_GqN9cTM8hf0XyJK4UR3jN8_P4xGqMc7dYwZL9uRk6-U8sQ2vN3_LmBdCf7K8YxJ9hNpA4rS6fGqM8vC_w",
   "c_nonce": "8450206689214712015",
   "c_nonce_expires_in": 86400
}
```

**Response Components**:
- **JWT-encoded Credential**: Complete EducationalID in W3C VC format
- **Digital Signature**: ES256 signature by URV's DID key
- **EBSI Anchoring**: Schema and trust registry references
- **Expiration Management**: Validity period and renewal information

---

## 9. Implementation Insights

### 9.1 Schema Architecture: eIDAS 2.0 PID vs. eduGAIN EducationalID

**Critical Distinction**: The EducationalID journey demonstrates the **architectural separation** between different credential types in the DC4EU framework:

#### Foundational Identity (PID) - eIDAS 2.0 Regulation Compliant
- **Schema Base**: Official eIDAS 2.0 Person Identification Data schema
- **Legal Reference**: EU Regulation 2024/2977 (eIDAS 2.0)
- **Purpose**: Foundational legal identity for all EU digital services
- **Standards**: ISO 3166-1 (country codes), ISO/IEC 5218 (sex values)
- **Focus**: "Who you are legally according to national authorities"
- **Key Attributes**: 
  - Core identity: `family_name`, `given_name`, `birth_date`, `birth_place`
  - Legal status: `nationality`, `personal_administrative_number`
  - Administrative: `issuing_authority`, `issuing_country`, `expiry_date`
  - Privacy-sensitive: `resident_address`, `portrait`, `email_address`

#### Non-Foundational Identity Credentials (EducationalID)
- **Schema Base**: eduGAIN/SCHAC standards, not ELM
- **Purpose**: Institutional identity and affiliation
- **Standards**: REFEDS, eduGAIN, SCHAC
- **Focus**: "Who you are within an educational context"
- **Key Attributes**: 
  - Educational identity: `eduPersonPrincipalName`, `eduPersonScopedAffiliation`
  - Institutional affiliation: `schacPersonalUniqueCode`, `schacHomeOrganization`
  - Assurance: REFEDS Assurance Framework compliance

#### Academic Achievement Credentials (ELM-Based)
- **Schema Base**: European Learning Model (ELM) 3.2
- **Purpose**: Learning outcomes and qualifications
- **Standards**: ELM, EDCI, Europass
- **Focus**: "What you have learned and achieved"
- **Key Attributes**:
  - Learning achievements, qualifications
  - Assessment results, credit systems
  - Quality assurance information

### 9.2 eIDAS 2.0 PID Integration Benefits

The PID's use of **official eIDAS 2.0 standards** provides:

1. **Legal Certainty**: Direct compliance with EU Regulation 2024/2977
2. **Cross-Border Recognition**: Automatic recognition across all EU Member States
3. **High Assurance**: Highest level of identity verification available in EU
4. **Standardised Format**: Common structure across all European identity providers
5. **Privacy Protection**: Built-in selective disclosure capabilities
6. **Administrative Integration**: Direct link to national identity systems

### 9.3 Identity Verification Chain

**Complete Identity Verification Flow**:
```
🇪🇸 Spanish National Identity (DNI) 
  ↓ [Digital Transformation]
🆔 eIDAS 2.0 PID Credential (PersonIdentificationData)
  ↓ [Verification & Validation]
🎓 EducationalID Credential (eduGAIN/SCHAC)
  ↓ [Institutional Affiliation]
📜 Academic Achievement Credentials (ELM)
```

This structure ensures that **every educational credential** can be traced back to **verified national identity**, providing the highest levels of trust and legal certainty across European borders.

### 9.4 Technical Innovation: Identity Matching Infrastructure

The DC4EU framework's **identity matching infrastructure** represents a critical innovation in European digital identity:

#### Pre-Deployment Data Preparation
Before any credential can be issued, institutions must establish:

1. **Comprehensive Data Stores**: Complete population of student databases with verified enrolment information
2. **Identity Correlation Systems**: Cross-reference tables linking national identity numbers (DNI) to institutional records
3. **Validation Algorithms**: Automated matching procedures for PID attributes against educational records
4. **Temporal Synchronisation**: Systems to maintain up-to-date correlation between legal and institutional identity

#### Identity Matching Process
**The Critical Bridge**: Connecting **legal identity** (Spanish PID) with **institutional identity** (EducationalID)

**Three-Layer Validation**:
- **Primary Key Match**: DNI from PID directly correlates to student database primary key
- **Attribute Verification**: Name and birth date provide multi-factor identity confirmation
- **Enrolment Validation**: Current student status and credential issuance authorisation

#### Technical Architecture Benefits
- **Separation of Concerns**: Legal identity management vs. institutional identity management
- **Real-time Correlation**: Instant matching between PID and educational records
- **Audit Compliance**: Complete traceability of identity matching decisions
- **Privacy Protection**: Minimum necessary data correlation with selective disclosure
- **Scalability**: Standardised patterns applicable across all European educational institutions

This infrastructure ensures that **every educational credential** is properly anchored to **verified legal identity** whilst maintaining the flexibility needed for diverse institutional requirements across Europe.

### 9.5 European Digital Sovereignty

This implementation represents **European digital sovereignty** in action:

- **European standards**: W3C VC, EBSI, eIDAS 2.0
- **European infrastructure**: EBSI trust registries and verification
- **European governance**: Member State cooperation and recognition
- **European values**: Privacy, security, and citizen control

---

## 10. Appendices

### 10.1 Appendix A: Schema Specifications

#### A.1 eIDAS 2.0 PID Schema

The official Person Identification Data schema as defined by EU Regulation 2024/2977:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Person Identification Data for the Natural Person",
  "description": "Reference: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202402977",
  "type": "object",
  "allOf": [
    {
      "$ref": "./node_modules/@cef-ebsi/vcdm1.1-attestation-schema/schema.json"
    },
    {
      "type": "object",
      "properties": {
        "credentialSubject": {
          "type": "object",
          "properties": {
            "family_name": {
              "type": "string",
              "description": "Current last name(s) or surname(s) of the user to whom the person identification data relates.",
              "minLength": 1
            },
            "given_name": {
              "type": "string",
              "description": "Current first name(s), including middle name(s) where applicable, of the user to whom the person identification data relates.",
              "minLength": 1
            },
            "birth_date": {
              "type": "string",
              "format": "date",
              "description": "Day, month, and year on which the user to whom the person identification data relates was born."
            },
            "birth_place": {
              "type": "string",
              "description": "The country as an alpha-2 country code as specified in ISO 3166-1, or the state, province, district, or local area or the municipality, city, town, or village where the user to whom the person identification data relates was born."
            },
            "nationality": {
              "type": "array",
              "items": {
                "type": "string",
                "pattern": "^[A-Z]{2}$"
              },
              "description": "One or more alpha-2 country codes as specified in ISO 3166-1, representing the nationality of the user to whom the person identification data relates."
            },
            "personal_administrative_number": {
              "type": "string",
              "description": "A value assigned to the natural person that is unique among all personal administrative numbers issued by the provider of person identification data."
            },
            "expiry_date": {
              "type": "string",
              "format": "date-time",
              "description": "Date (and if possible time) when the person identification data will expire."
            },
            "issuing_authority": {
              "type": "string",
              "description": "Name of the administrative authority that issued the person identification data."
            },
            "issuing_country": {
              "type": "string",
              "pattern": "^[A-Z]{2}$",
              "description": "Alpha-2 country code, as specified in ISO 3166-1, of the country or territory of the provider of the person identification data."
            },
            "issuing_jurisdiction": {
              "type": "string",
              "description": "Jurisdiction identifier for sub-national authorities (e.g., ES-CT for Catalonia)"
            }
          },
          "required": [
            "family_name",
            "given_name",
            "birth_date",
            "birth_place",
            "nationality",
            "expiry_date",
            "issuing_authority",
            "issuing_country"
          ]
        }
      }
    }
  ]
}
```

#### A.2 EducationalID Schema

The eduGAIN/SCHAC-based schema for non-foundational educational identity:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Verifiable Educational ID",
  "description": "Schema of a Verifiable Educational ID for a natural person participating in the educational use cases",
  "type": "object",
  "allOf": [
    {
      "$ref": "./node_modules/@cef-ebsi/vcdm1.1-attestation-schema/schema.json"
    },
    {
      "properties": {
        "credentialSubject": {
          "description": "Defines additional properties on credentialSubject to describe IDs that do not have a substantial level of assurance.",
          "type": "object",
          "properties": {
            "id": {
              "description": "Defines a unique identifier of the credential subject. DID:Key value, generated by the user wallet and associated to the credential holder.",
              "type": "string"
            },
            "identifier": {
              "description": "Defines an alternative identifier for the credential subject and has as value the value of eduPersonPrincipalName attribute.",
              "type": "string"
            },
            "schacPersonalUniqueCode": {
              "description": "schacPersonalUniqueCode can have different forms urn:schac:personalUniqueCode:int:esi:<sHO>:<code>",
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "schacPersonalUniqueID": {
              "description": "value is different in different countries, mostly urn:schac:personalUniqueID:<country-code>:<code>.",
              "type": "string"
            },
            "schacHomeOrganization": {
              "description": "Specifies the home organisation of the credential subject",
              "type": "string"
            },
            "familyName": {
              "description": "Defines current family name(s) of the credential subject which corresponds to the eduGAIN attribute sn",
              "type": "string"
            },
            "firstName": {
              "description": "Defines current first name(s) of the credential subject which corresponds to the eduGAIN attribute givenName",
              "type": "string"
            },
            "displayName": {
              "description": "The name(s) that should appear in white-pages-like applications",
              "type": "string"
            },
            "dateOfBirth": {
              "description": "Defines date of birth of the credential subject (format: yyyyMMdd)",
              "type": "string",
              "format": "date"
            },
            "mail": {
              "description": "(primary) e-mail address of the credential subject as registered by the educational institution",
              "type": "string"
            },
            "eduPersonPrincipalName": {
              "description": "Unique, persistent identifier of the credential subject",
              "type": "string"
            },
            "eduPersonPrimaryAffiliation": {
              "description": "Primary Affiliation within Home Organisation",
              "type": "string"
            },
            "eduPersonAffiliation": {
              "description": "Affiliation within Home Organisation. It can contain multiple values such as member, student, employee, faculty, staff, affiliate, alumni, etc.",
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "eduPersonScopedAffiliation": {
              "description": "The person's affiliations within Home Organisation scoped with the Home Organisation",
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "eduPersonAssurance": {
              "description": "represents identity assurance profiles (IAPs) https://wiki.refeds.org/display/ASS/REFEDS+Assurance+Framework+ver+1.0",
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          },
          "required": ["id", "identifier", "eduPersonScopedAffiliation"]
        }
      }
    }
  ]
}
```

### 10.2 Appendix B: Technical Reference Materials

#### B.1 Complete OpenID4VCI Flow Messages

**Credential Offer URI Resolution**:
```http
GET https://lspurv.urv.cat/issuer/offers/719307744250317677
Accept: application/json

Response:
{
  "credential_issuer": "https://lspurv.urv.cat/issuer",
  "credentials": [
    {
      "format": "jwt_vc",
      "types": ["VerifiableCredential", "VerifiableEducationalID"]
    }
  ]
}
```

**Token Exchange**:
```http
POST https://lspurv.urv.cat/auth/token
Content-Type: application/x-www-form-urlencoded

grant_type=authorization_code
&client_id=did:key:z2dmzD81cgPx8Vki7JbuuMmFYrWPgYoytykUZ3eyqht1j9Kbndi4FzE7bq9irPGQVyZG7SWHy8iqpKMjjhmtB7JF3eFYnM67SxNd4gjT3DsKUb7NKeKLcNTEocYUf2kpBQRQqCvGMCvC87F8jgydShFCPTwrDpvJKrZMdq8zjQLQxwW2kL
&code=authorization_code_value
```

#### B.2 EBSI Service Endpoints

**Trust Registry Verification**:
```http
GET https://api.preprod.ebsi.eu/trusted-issuers-registry/v3/issuers/{issuer-did}
Authorization: Bearer {ebsi-access-token}
```

**Schema Registry Validation**:
```http
GET https://api.preprod.ebsi.eu/trusted-schemas-registry/v1/schemas/{schema-id}
Authorization: Bearer {ebsi-access-token}
```

**DID Resolution**:
```http
GET https://api.preprod.ebsi.eu/did-registry/v3/identifiers/{did}
Accept: application/did+ld+json
```

#### B.3 Error Handling and Status Codes

**Common Error Responses**:

| Error Code | Description | Resolution |
|------------|-------------|------------|
| `invalid_presentation` | PID verification failed | User must present valid eIDAS 2.0 PID |
| `identity_mismatch` | PID doesn't match student records | Contact university registrar |
| `credential_suspended` | Student enrolment suspended | Resolve enrolment status |
| `trust_verification_failed` | EBSI verification failed | System maintenance required |

### 10.3 Appendix C: Compliance and Regulatory Framework

#### C.1 eIDAS 2.0 Compliance Checklist

**Mandatory Requirements**:
- ✅ **Article 3**: Foundational identity verification through PID
- ✅ **Article 45b**: Authentic Source certification and operation
- ✅ **Annex VI**: Technical specifications for credential formats
- ✅ **Recital 12**: Cross-border recognition requirements

**Privacy and Data Protection**:
- ✅ **GDPR Article 6**: Lawful basis for processing (public task)
- ✅ **GDPR Article 5**: Data minimisation and purpose limitation
- ✅ **GDPR Article 25**: Privacy by design implementation
- ✅ **GDPR Article 32**: Technical and organisational security measures

#### C.2 Educational Standards Alignment

**SCHAC (Schema for Academia)**:
- ✅ Personal unique identifiers
- ✅ Organisational affiliations
- ✅ Educational context attributes

**eduGAIN Federation Standards**:
- ✅ Cross-border attribute release
- ✅ Privacy-preserving identity federation
- ✅ Multi-lateral trust agreements

**REFEDS Assurance Framework**:
- ✅ Identity assurance profiles
- ✅ Authentication context classification
- ✅ Risk-based assurance levels

### 10.4 Appendix D: Implementation Roadmap

#### D.1 Phase 1: Infrastructure Preparation (Months 1-3)
- **Data Store Population**: Complete student database preparation
- **Identity Matching Setup**: Implement correlation algorithms
- **eIDAS 2.0 Certification**: Obtain Authentic Source certification
- **API Development**: Build standardised access interfaces

#### D.2 Phase 2: Pilot Implementation (Months 4-6)
- **Limited Rollout**: Test with select student cohorts
- **User Experience Testing**: Refine wallet interactions
- **Trust Registry Integration**: Complete EBSI connectivity
- **Cross-Border Validation**: Test with partner universities

#### D.3 Phase 3: Full Production (Months 7-12)
- **Complete Rollout**: All eligible students
- **Monitoring and Analytics**: Performance tracking
- **Continuous Improvement**: Based on usage patterns
- **European Expansion**: Additional university partnerships

#### D.4 Success Metrics

**Technical Metrics**:
- Credential issuance success rate: >99.5%
- Average issuance time: <30 seconds
- Identity matching accuracy: >99.9%
- System availability: >99.9%

**User Experience Metrics**:
- User satisfaction score: >4.5/5
- Completion rate: >95%
- Support ticket volume: <1% of issuances
- Cross-border usage: >20% of credentials

**Compliance Metrics**:
- eIDAS 2.0 compliance: 100%
- Privacy incident rate: 0
- Audit findings: 0 critical
- Data protection compliance: 100%

---

## Conclusion

The EducationalID issuance journey represents a landmark achievement in European digital identity infrastructure. By successfully integrating eIDAS 2.0 foundational identity verification with educational credential issuance, this implementation establishes a new paradigm for trusted, interoperable digital credentials across European borders.

**Key Achievements**:

1. **Mandatory PID Integration**: Ensuring all educational credentials are anchored to verified national identity
2. **Dual Role Architecture**: Demonstrating how institutions can operate as both Authentic Source and Issuer under eIDAS 2.0
3. **Identity Matching Innovation**: Creating robust infrastructure to correlate legal and institutional identity
4. **European Interoperability**: Establishing standards-based credentials recognised across all EU Member States
5. **Privacy by Design**: Implementing selective disclosure and data minimisation throughout the process

This comprehensive framework not only serves the immediate needs of European students like Maria García but also establishes the foundation for a truly integrated European Education Area where digital credentials enable seamless mobility, recognition, and opportunity across all Member States.

The journey from foundational identity verification through educational credential issuance represents more than a technical achievement—it embodies the European values of privacy, security, citizen empowerment, and cross-border cooperation that will define the digital future of European education.


