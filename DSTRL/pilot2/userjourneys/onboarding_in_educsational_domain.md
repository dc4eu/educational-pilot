# Onboarding on educational/professional qualifications domain - EducationalID Issuance: Complete User Journey Narrative with Technical Implementation

## Executive Summary

This document presents the complete narrative for EducationalID issuance within the DC4EU Pilot 2 framework, implementing a No Authorize OpenID VCI flow with **mandatory Verifiable Presentation of PID credentials**. The journey demonstrates the sophisticated orchestration between multiple actors, systems, and trust mechanisms that enable secure, interoperable educational credential issuance across European borders.

**Critical Prerequisite**: Before any EducationalID can be issued, the citizen's **Person Identification Data (PID)** must be verified through the eIDAS 2.0 framework. This foundational identity verification is the cornerstone upon which all educational credentials are built.

**Key Innovation**: This implementation showcases the world's first production-ready dPKI system for educational credentials, integrating EBSI trust registries with traditional educational infrastructure to create a seamless, trustworthy credential ecosystem built upon verified foundational identity.

**Bottom Line**: Maria García, a Spanish student, successfully obtains her EducationalID from Universitat Rovira i Virgili through a process that validates her foundational identity via Spanish PID, matches it with university records, and issues a cryptographically secure educational credential recognizable across all European universities.

---

## Quick Reference Guide

### Process Overview
1. **Prerequisites**: University data preparation and identity matching infrastructure
2. **PID Verification**: Mandatory foundational identity validation (Steps 1-22)
3. **Educational ID Issuance**: Institutional credential creation (Steps 23-33)
4. **Cross-Border Recognition**: European-wide validity and trust

### Key Actors
- **Student**: Maria García (credential holder)
- **University**: Universitat Rovira i Virgili (dual role: Authentic Source + Issuer)
- **Infrastructure**: EBSI trust registries and verification services
- **Governance**: Spanish Ministry (root trust anchor)

### Technical Standards
- **PID Schema**: eIDAS 2.0 Person Identification Data (EU Regulation 2024/2977)
- **EducationalID Schema**: eduGAIN/SCHAC standards for institutional identity
- **Protocols**: OpenID4VCI, W3C Verifiable Credentials, EBSI trust framework

---

## Table of Contents

1. [Infrastructure Prerequisites](#1-infrastructure-prerequisites)
2. [The Story: Maria's Educational Identity Journey](#2-the-story-marias-educational-identity-journey)
3. [Actor Ecosystem and Roles](#3-actor-ecosystem-and-roles)
4. [Technical Architecture Overview](#4-technical-architecture-overview)
5. [Detailed User Journey Flow](#5-detailed-user-journey-flow)
6. [Trust Verification Mechanisms](#6-trust-verification-mechanisms)
7. [Technical Message Details](#7-technical-message-details)
8. [Implementation Insights](#8-implementation-insights)
9. [**Appendix A: Schema Specifications**](#appendix-a-schema-specifications)
10. [**Appendix B: Technical Reference Materials**](#appendix-b-technical-reference-materials)

---

## 1. Infrastructure Prerequisites

### 1.1 Critical Foundation Requirements

**Before any EducationalID can be issued**, institutions must complete essential infrastructure preparation. This is not optional—it's a **mandatory prerequisite** for participation in the DC4EU framework.

### 1.2 Data Store Preparation for EAA Issuance

#### **Student Registry Population**
- **Complete enrollment database**: All active students with validated enrollment data
- **Historical records**: Previous academic years and graduation records
- **Programme metadata**: Detailed information about academic programmes and levels
- **Status management**: Real-time enrollment status tracking and updates

#### **Identity Correlation Infrastructure**
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
└── Estado: Activo → enrollment_status: ACTIVE
```

### 1.3 Identity Matching Mechanisms

#### **Multi-Layer Validation Process**
1. **Primary Key Correlation**: DNI from PID serves as primary matching key
2. **Attribute Verification**: Name and birth date provide additional confirmation
3. **Enrollment Validation**: Current student status and credential authorization
4. **Temporal Verification**: Enrollment dates and validity periods

#### **Real-Time Matching Infrastructure**
- **API-based correlation**: Standardized endpoints for identity resolution
- **Confidence scoring**: Mathematical confidence levels for matching accuracy
- **Exception handling**: Procedures for handling matching conflicts or failures
- **Performance optimization**: Sub-second response times for user experience

### 1.4 eIDAS 2.0 Compliance Infrastructure

#### **Authentic Source Certification**
- **Article 45b compliance**: Official certification as eIDAS 2.0 Authentic Source
- **Data quality assurance**: Verified accuracy and completeness of student records
- **API standardization**: eIDAS 2.0 compliant interfaces for data access
- **Security measures**: Encryption, access control, and audit capabilities

#### **Dual Role Architecture**
Universities must implement **clear separation** between:
- **Authentic Source function**: Authoritative data repository
- **Issuer function**: Credential creation and issuance
- **API gateway**: Standardized access layer between roles

---

## 2. The Story: Maria's Educational Identity Journey

### 2.1 Setting the Scene

**Meet Maria García**: A 20-year-old computer science student at Universitat Rovira i Virgili (URV) in Catalonia, Spain. Maria is about to begin her second year and needs to establish her digital educational identity to access university services, participate in international exchange programmes, and eventually apply for graduate studies across Europe.

It's Monday morning, September 2025. Maria sits in her dormitory room, smartphone in hand, ready to embark on a digital journey that will transform how she interacts with educational institutions across Europe. Little does she know that behind the simple act of "getting her student ID" lies a sophisticated dance of cryptographic protocols, trust verification systems, and international cooperation frameworks.

### 2.2 The Human Story

**The Challenge**: Maria needs more than just a physical student card. In the digital age of European education, she requires a **Verifiable Educational ID** that:
- Proves her authentic enrollment at URV
- Enables automatic recognition across EU universities
- Integrates with the EUDI Wallet ecosystem
- Supports future mobility and academic recognition

**The Solution**: Through the DC4EU framework, Maria will receive a cryptographically secure, EBSI-anchored Educational ID that serves as her digital passport to the European Education Area. **However, this credential can only be issued after her foundational identity has been verified through her Spanish Person Identification Data (PID)**—a mandatory prerequisite that ensures the highest levels of trust and security.

### 2.3 The Journey Begins

Maria opens her **EUDI Wallet** application, a sleek interface that hides the complexity of European digital identity infrastructure. She taps on "Add Educational Credential" and selects "Universitat Rovira i Virgili" from a list of participating institutions.

What happens next is a masterpiece of digital orchestration, involving multiple actors across different systems, countries, and trust domains.

---

## 3. Actor Ecosystem and Roles

### 3.1 Primary Actors

#### **🎓 Maria García (Natural Person/Student)**
- **Role**: Credential holder and primary user
- **Systems**: EUDI Wallet (Mobile Application)
- **Responsibilities**:
  - Initiate credential request
  - Provide consent for data sharing
  - Present PID for verification
  - Accept issued credential into wallet

#### **🏛️ Universitat Rovira i Virgili (Dual Role Institution)**
- **Primary Role**: Educational credential issuer
- **Secondary Role**: **eIDAS 2.0 Authentic Source** for student data
- **Systems**: 
  - Student Information System (Authentic Source function)
  - Credential Issuance Infrastructure (Issuer function)
- **Key Personnel**: Registrar Office, Academic Secretary
- **Critical Architecture Note**: URV operates in **dual capacity**:
  - **As Authentic Source**: Maintains authoritative student records under eIDAS 2.0 Article 45b
  - **As Issuer**: Consumes data from its own Authentic Source via standardized APIs
- **Responsibilities**:
  - Verify student enrollment and academic standing (Authentic Source role)
  - Issue cryptographically secure Educational IDs (Issuer role)
  - Maintain clear separation between data provision and credential issuance
  - Integrate with European trust frameworks

### 3.2 Technical Infrastructure Actors

#### **🔐 uSelf Issuer Agent (Credential Issuance Service)**
- **Role**: Technical orchestrator for credential issuance
- **Location**: University infrastructure (`lspurv.urv.cat`)
- **Responsibilities**:
  - Manage OpenID4VCI protocol flows
  - Coordinate with EBSI infrastructure
  - Handle cryptographic operations
  - Generate QR codes and credential offers

#### **📊 Authentic Source (Official eIDAS 2.0 Role)**
- **Role**: **Official eIDAS 2.0 Authentic Source** - Authoritative repository of verified student information
- **Played by**: Universitat Rovira i Virgili (in dual capacity)
- **System**: Standardized API-accessible student registry with encrypted records
- **eIDAS 2.0 Compliance**: Certified authentic source for educational data under Article 45b
- **Critical Prerequisites**:
  - **Data Store Preparation**: Pre-population of educational data repositories for potential EAA issuance
  - **Identity Matching Infrastructure**: Mechanisms to correlate legal identity (PID) with institutional identity (EducationalID)
  - **Cross-Reference Systems**: Linking Spanish DNI numbers with university student records
- **Responsibilities**:
  - Maintain authoritative student enrollment records
  - Provide standardized API access to verified data
  - Execute real-time identity matching between PID and educational records
  - Ensure data integrity and audit compliance
  - Support continuous synchronization between legal and institutional identities

#### **🌐 EBSI Infrastructure Ecosystem**

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

#### **🆔 uSelf PID Issuer Agent**
- **Role**: Personal Identity Data validation service
- **Function**: Verify student's foundational identity credentials

### 3.3 Governance and Oversight Actors

#### **🏛️ Spanish Ministry of Universities and Research**
- **Role**: Root Trust Anchor (RootTAO)
- **Authority**: Issues EAA credentials authorising URV to issue Educational IDs
- **Scope**: National level governance and compliance

#### **🇪🇺 European Blockchain Services Infrastructure (EBSI)**
- **Role**: European-level trust infrastructure
- **Function**: Provide decentralised trust registry and schema validation
- **Governance**: Multi-national consortium ensuring European standards

### 3.4 Supporting Systems

#### **📱 Student GUI (Web Interface)**
- **Role**: User-facing interface for credential requests
- **Location**: `https://uself-verifier-gui.lspurv.urv.cat/`
- **Function**: Generate QR codes and facilitate user interactions

#### **🔗 Mobile Wallet (EUDI Wallet)**
- **Role**: Credential storage and presentation
- **Standards**: W3C Verifiable Credentials, OpenID4VP
- **Features**: Multi-format support, selective disclosure, cross-border compatibility

---

## 4. Technical Architecture Overview

### 4.1 System Architecture Diagram

```mermaid
graph TB
    subgraph "Student Domain"
        Student[👩‍🎓 Maria García]
        Mobile[📱 EUDI Wallet]
    end
    
    subgraph "University Infrastructure (lspurv.urv.cat)"
        GUI[🖥️ Student GUI]
        Agent[🔧 uSelf Issuer Agent]
        AuthSource[📊 Authentic Source<br/>**eIDAS 2.0 Official Role**]
        DB[🗄️ Student Registry DB]
        API[🔗 Standardized APIs<br/>**eIDAS 2.0 Compliant**]
    end
    
    subgraph "EBSI Infrastructure"
        DIDR[🆔 DID Registry]
        TRR[🛡️ Trust Registry] 
        SR[📋 Schema Registry]
        Proxy[🌐 EBSI Proxy]
        PIDAgent[🔐 PID Issuer Agent]
    end
    
    subgraph "Trust Governance"
        Ministry[🏛️ Spanish Ministry]
        EAA[📜 EAA Credentials<br/>**Authentic Source Authority**]
    end

    Student --> Mobile
    Mobile <--> GUI
    GUI <--> Agent
    Agent <--> API
    API <--> AuthSource
    AuthSource <--> DB
    
    Agent <--> DIDR
    Agent <--> TRR
    Agent <--> SR
    Agent <--> Proxy
    Proxy <--> PIDAgent
    
    Ministry --> EAA
    EAA --> TRR
    TRR --> Agent
    
    classDef eidas fill:#e1f5fe,stroke:#01579b,stroke-width:3px
    class AuthSource,API,EAA eidas
```

**Key Architectural Principle**: The university operates in **dual capacity** under eIDAS 2.0:
1. **As Authentic Source**: Authoritative holder of student data (Article 45b compliance)
2. **As Issuer**: Consumer of authentic source data via standardized APIs for credential creation

### 4.2 Trust Flow Architecture

The system implements a sophisticated **multi-layer trust model**:

1. **Foundational Layer**: Spanish national identity infrastructure provides PID
2. **Institutional Layer**: URV's authorisation via Spanish Ministry EAA credentials
3. **European Layer**: EBSI trust registries validate cross-border recognition
4. **Technical Layer**: Cryptographic proofs ensure credential integrity

### 4.3 Protocol Stack

- **Application Layer**: OpenID for Verifiable Credentials (OID4VCI)
- **Credential Layer**: W3C Verifiable Credentials Data Model
- **Trust Layer**: EBSI trust registries and EAA framework
- **Cryptographic Layer**: ES256 signatures, DID-based authentication
- **Transport Layer**: HTTPS with additional security headers

---

## 5. Detailed User Journey Flow

### 5.1 Phase 1: Journey Initiation (Steps 1-6)

#### **Step 1: The Request**
*Monday, 9:15 AM - Maria's dormitory*

Maria opens her web browser and navigates to the URV student portal. The interface is clean and multilingual, supporting both Catalan and Spanish as befitting the region's linguistic diversity.

**Technical Action**: 
```http
GET https://student-web/issue
```

**Behind the Scenes**: The student GUI system initialises, checking server status and preparing the credential issuance infrastructure.

#### **Step 2: Credential Offer Generation**
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

#### **Step 3: QR Code Magic**
*The bridge between digital and physical*

The Student GUI receives the credential offer and transforms it into a QR code—a visual bridge between the web interface and Maria's mobile wallet.

**Technical Implementation**:
```bash
openid-credential-offer://?credential_offer_uri=https://issuer.eu/issuer/offers/719307744250317677
```

The QR code contains not the full credential offer (which would be too large) but a secure URI pointing to the offer details. This follows EBSI recommendations for optimal user experience.

#### **Step 4: Mobile Engagement**
*Maria scans the QR code*

Maria holds up her EUDI Wallet and scans the QR code. The wallet's sophisticated parsing engine recognises the OpenID credential offer format and prepares for the issuance flow.

**User Experience**: The wallet displays a clear, user-friendly interface:
- "Universitat Rovira i Virgili wants to issue your Educational ID"
- "This credential will allow you to access university services and participate in European student mobility"
- "Tap to continue"

#### **Step 5: Protocol Handshake Initiation**
*Behind the scenes coordination*

The mobile wallet processes the QR code and initiates the OpenID4VCI flow, establishing a secure communication channel with the university's systems.

**Technical Flow**:
```http
HTTP 302 Redirect to Authorization Endpoint
```

#### **Step 6: Authorization Request**
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

### 5.2 Phase 2: Foundational Identity Verification - The Mandatory PID Process (Steps 7-22)

**Critical Process Note**: This phase represents the **absolute prerequisite** for EducationalID issuance. Under eIDAS 2.0 regulations and DC4EU framework requirements, **no educational credential can be issued without verified foundational identity**. The PID verification process ensures that Maria's educational credentials are anchored to her legally verified national identity.

#### **Step 7: The Trust Challenge**
*Proving who you are at the foundational level*

The uSelf Issuer Agent responds with a **direct_post** challenge, requesting Maria to present her PID credential. This is not optional—it's a **mandatory step** that forms the foundation of all subsequent trust relationships.

**User Experience**: Maria's wallet displays:
- "⚠️ **Identity Verification Required**: To issue your Educational ID, the university must verify your foundational identity"
- "🆔 **Spanish PID Required**: Please present your Person Identification Data (PID) issued by Spanish authorities"
- "🔒 **Security Notice**: This verification is mandatory under eIDAS 2.0 regulations"
- "ℹ️ This information will be used only for identity verification purposes"

#### **Step 8: Consent and Privacy**
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

#### **Step 9-10: The Digital Handshake**
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

**Maria's PID Credential Structure** (eIDAS 2.0 Compliant - See [Appendix A.1](#a1-eidas-20-pid-schema)):

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

#### **Steps 11-21: The Foundational Trust Verification Symphony**
*EBSI infrastructure validates Maria's foundational identity*

What happens next is invisible to Maria but represents **the most critical trust verification process** in the entire digital credential ecosystem. The uSelf Issuer Agent orchestrates a **comprehensive verification of Maria's foundational identity** across multiple EBSI services:

**Step 11-12: PID DID Resolution**
```http
GET https://ebsi-did-registry/did/{maria-pid-issuer-did}
```
**Purpose**: Resolve the DID of the Spanish authority that issued Maria's PID to verify the cryptographic keys and ensure the PID credential is properly signed by legitimate national authorities.

**Step 13-14: National Authority Trust Registry Verification**
```http
GET https://ebsi-tr-registry/tr
```
**Purpose**: Check the EBSI Trust Registry to verify that the Spanish national identity authorities are officially authorised to issue Person Identification Data credentials under eIDAS 2.0.

**Step 15-16: PID Schema Validation**
```http
GET https://ebsi-schema-registry/schema
```
**Purpose**: Validate that Maria's PID credential conforms to the official European PID schema and data format requirements.

**Step 17-20: Comprehensive PID Verification**
```http
GET https://ebsi-proxy/verify
```
**Purpose**: The EBSI Proxy performs the **complete foundational identity verification**, including:
- ✅ **Cryptographic signature validation** of the PID credential
- ✅ **Revocation status checking** to ensure the PID hasn't been revoked
- ✅ **Trust chain verification** back to Spanish national authorities
- ✅ **eIDAS 2.0 compliance verification** for regulatory alignment
- ✅ **Temporal validity checking** to ensure the PID is currently valid

**Step 21-22: Foundational Identity Verification Success**
The comprehensive verification process completes successfully, **confirming Maria's foundational identity**, and the system issues an authorization code to proceed with Educational ID issuance.

**Verification Result**: The system now has **cryptographic proof** that:
- Maria is who she claims to be (verified by Spanish national authorities)
- Her identity credential is valid and not revoked
- The verification complies with all eIDAS 2.0 requirements
- She is legally authorised to receive educational credentials in Spain

### 5.3 Phase 3: Credential Issuance (Steps 23-33)

#### **Step 23-24: Access Token Exchange**
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

#### **Step 25-26: The Moment of Truth**
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

#### **Step 27-30: Authentic Source Data Retrieval via Standardized APIs**
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
   - **Enrollment Verification**: Current active enrollment status

**Database Query (Internal to Authentic Source)**:
```sql
SELECT s.studentId, s.enrollmentStatus, s.programme, s.level, 
       s.enrollmentDate, s.expectedGraduation, s.institution,
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

**Authentic Source Response** (via standardized API - See [Appendix B.1](#b1-authentic-source-api-response)):

The authentic source provides a comprehensive response that demonstrates successful **identity matching** between Maria's legal identity (PID) and her institutional identity (student record). This response includes both the verified correlation and the educational data needed for EducationalID issuance.

**Critical Identity Matching Results**:
- ✅ **DNI Match**: 12345678A found in student database
- ✅ **Name Match**: García, Maria confirmed in enrollment records  
- ✅ **Birth Date Match**: 2004-03-15 validated against university records
- ✅ **Enrollment Verified**: Active student status confirmed
- ✅ **Credential Authorization**: Student authorized for EducationalID issuance

**Architectural Innovation**: This design demonstrates how eIDAS 2.0 enables institutional **dual roles** while maintaining:
- **Trust boundaries**: Clear separation of functions even within the same organization
- **Identity correlation**: Robust matching between legal and institutional identity
- **Interoperability**: Standardized APIs that work across organizational boundaries
- **Compliance**: Full regulatory alignment with European digital identity frameworks

#### **Step 31: Credential Generation**
*The digital birth certificate*

The agent constructs Maria's Educational ID credential using the **eduGAIN/SCHAC-based schema** (See [Appendix A.2](#a2-educationalid-schema)) rather than ELM. This credential follows the specific EducationalID schema designed for non-foundational identity in educational contexts.

The generated EducationalID credential incorporates:
- **Verified Identity Data**: From the PID verification process
- **Educational Attributes**: Following eduGAIN/SCHAC standards
- **Institutional Affiliation**: URV-specific organizational data
- **Assurance Levels**: REFEDS framework compliance

**Key Schema Features** (detailed in [Appendix A.2](#a2-educationalid-schema)):
- **SCHAC Unique Codes**: For cross-institutional identity resolution
- **eduGAIN Attributes**: Standard educational federation attributes
- **REFEDS Assurance**: Identity assurance framework compliance
- **Multi-value Support**: Arrays for affiliations and assurance levels

#### **Step 32: Event Notification**
*System coordination*

The agent sends a `credential_issued` event to the Student GUI, enabling real-time updates to any connected systems and maintaining audit trails for compliance purposes.

#### **Step 33: Delivery to Maria**
*The moment of completion*

The Educational ID credential is delivered to Maria's EUDI Wallet. The wallet validates the credential signature, stores it securely, and notifies Maria of successful issuance.

**User Experience**: Maria sees a success notification:
- "Your Educational ID has been issued successfully!"
- "You can now access university services and participate in international programmes"
- "This credential is valid until June 30, 2027"

---

## 6. Trust Verification Mechanisms

### 6.1 Multi-Layer Trust Architecture with eIDAS 2.0 Compliance

The EducationalID issuance process implements sophisticated **multi-layer trust verification** with full eIDAS 2.0 regulatory alignment, **built upon mandatory foundational identity verification**:

#### **Layer 1: Foundational Identity (PID) - MANDATORY PREREQUISITE**
- **Role**: **Absolute prerequisite** for all educational credentials
- **Source**: Spanish national identity infrastructure
- **Verification**: eIDAS-compliant digital identity (mandatory)
- **Assurance Level**: High (Level of Assurance 3)
- **Cryptographic Standard**: ES256 signatures
- **Legal Basis**: eIDAS 2.0 Article 3 - foundational identity requirement
- **Process**: **Complete EBSI verification of PID before any educational credential issuance**

#### **Layer 2: Authentic Source Authority (eIDAS 2.0 Article 45b)**
- **Role**: URV as certified eIDAS 2.0 Authentic Source
- **Authority**: Spanish Ministry EAA credentials authorizing authentic source function
- **Data Integrity**: Authoritative student records with cryptographic proofs
- **API Standards**: eIDAS 2.0 compliant standardized access protocols
- **Dependency**: **Only operates after Layer 1 (PID) verification is complete**

#### **Layer 3: Institutional Issuance Authority (EAA)**
- **Source**: Spanish Ministry of Universities and Research
- **Mechanism**: Electronic Attestation of Attributes (EAA)
- **Scope**: Authorizes URV to issue Educational IDs based on authentic source data
- **Validation**: EBSI Trust Registry verification
- **Prerequisite**: **Requires verified foundational identity from Layer 1**

#### **Layer 4: European Recognition (EBSI)**
- **Framework**: European Blockchain Services Infrastructure
- **Function**: Cross-border trust propagation
- **Standards**: W3C Verifiable Credentials, eduGAIN/SCHAC
- **Governance**: Multi-national European cooperation
- **Foundation**: **Built upon verified PID from Layer 1**

#### **Layer 5: Technical Integrity**
- **Cryptography**: Multiple signature verification
- **Revocation**: Real-time status checking
- **Audit**: Comprehensive logging and traceability
- **Privacy**: Selective disclosure and data minimization
- **Anchor**: **All technical integrity traces back to verified PID**

### 6.2 Trust Chain Example with eIDAS 2.0 Roles

```
🇪🇺 European Union (eIDAS 2.0 Regulatory Framework)
  ↓
🇪🇸 Spanish Ministry of Universities (Root Trust Anchor)
  ↓ [Issues EAA - Authentic Source Authority]
🏛️ URV as Authentic Source (eIDAS 2.0 Article 45b Role)
  ↓ [Standardized API provides verified data]
🔧 URV as Issuer (EAA-Authorized Credential Issuer)
  ↓ [Issues Educational ID based on authentic source data]
👩‍🎓 Maria García (Credential Holder)
  ↓ [Presents Credential]
🏫 Any European University (Relying Party)
```

**Key Innovation**: The dual role architecture demonstrates how institutions can operate as both **Authentic Source** and **Issuer** under eIDAS 2.0 while maintaining clear functional separation and regulatory compliance.

### 6.3 Security Properties

- **Authenticity**: Cryptographically proven issuer identity
- **Integrity**: Tamper-evident credential structure  
- **Non-repudiation**: Immutable audit trail
- **Privacy**: Minimal data disclosure with consent
- **Availability**: Distributed verification infrastructure
- **Interoperability**: European standards compliance

---

## 7. Technical Message Details

### 7.1 Credential Offer Response (Complete)

The credential offer provides comprehensive metadata about the EducationalID credential, including display parameters and supported credential subject attributes (detailed structure in [Appendix B.2](#b2-credential-offer-response)).

**Key Features**:
- **Credential Type**: `VerifiableEducationalID` with `jwt_vc` format
- **Display Configuration**: URV branding and multilingual support
- **Attribute Mapping**: Complete eduGAIN/SCHAC attribute support
- **Cryptographic Binding**: ES256 algorithm with DID-based binding

### 7.2 Authorization Request (Complete)

The authorization request demonstrates sophisticated presentation definition validation ensuring only valid **eIDAS 2.0 compliant PID credentials** are accepted (complete technical details in [Appendix B.3](#b3-authorization-request)).

**Key Validation Requirements**:
- ✅ **Credential Type**: Must be `PersonIdentificationData` (eIDAS 2.0 PID)
- ✅ **Required Fields**: `family_name`, `given_name`, `birth_date`, `nationality`
- ✅ **Administrative Number**: `personal_administrative_number` for unique identification
- ✅ **Issuing Country**: Must be "ES" (Spain) for this university
- ✅ **Cryptographic Validation**: ES256 signature algorithm required

### 7.3 Final Credential Response

The final credential response delivers the completed EducationalID to Maria's EUDI Wallet in JWT format, cryptographically signed by URV's institutional key (complete response structure in [Appendix B.4](#b4-final-credential-response)).

**Response Components**:
- **JWT-encoded Credential**: Complete EducationalID in W3C VC format
- **Digital Signature**: ES256 signature by URV's DID key
- **EBSI Anchoring**: Schema and trust registry references
- **Expiration Management**: Validity period and renewal information

---

## 8. Implementation Insights

### 8.1 Schema Architecture: eIDAS 2.0 PID vs. eduGAIN EducationalID

**Critical Distinction**: The EducationalID journey demonstrates the **architectural separation** between different credential types in the DC4EU framework:

#### **Foundational Identity (PID) - eIDAS 2.0 Regulation Compliant**
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

#### **Non-Foundational Identity Credentials (EducationalID)**
- **Schema Base**: eduGAIN/SCHAC standards, not ELM
- **Purpose**: Institutional identity and affiliation
- **Standards**: REFEDS, eduGAIN, SCHAC
- **Focus**: "Who you are within an educational context"
- **Key Attributes**: 
  - Educational identity: `eduPersonPrincipalName`, `eduPersonScopedAffiliation`
  - Institutional affiliation: `schacPersonalUniqueCode`, `schacHomeOrganization`
  - Assurance: REFEDS Assurance Framework compliance

#### **Academic Achievement Credentials (ELM-Based)**
- **Schema Base**: European Learning Model (ELM) 3.2
- **Purpose**: Learning outcomes and qualifications
- **Standards**: ELM, EDCI, Europass
- **Focus**: "What you have learned and achieved"
- **Key Attributes**:
  - Learning achievements, qualifications
  - Assessment results, credit systems
  - Quality assurance information

### 8.2 eIDAS 2.0 PID Integration Benefits

The PID's use of **official eIDAS 2.0 standards** provides:

1. **Legal Certainty**: Direct compliance with EU Regulation 2024/2977
2. **Cross-Border Recognition**: Automatic recognition across all EU Member States
3. **High Assurance**: Highest level of identity verification available in EU
4. **Standardized Format**: Common structure across all European identity providers
5. **Privacy Protection**: Built-in selective disclosure capabilities
6. **Administrative Integration**: Direct link to national identity systems

### 8.3 Identity Verification Chain

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

### 8.4 Technical Innovation: Identity Matching Infrastructure

The DC4EU framework's **identity matching infrastructure** represents a critical innovation in European digital identity:

#### **Pre-Deployment Data Preparation**
Before any credential can be issued, institutions must establish:

1. **Comprehensive Data Stores**: Complete population of student databases with verified enrollment information
2. **Identity Correlation Systems**: Cross-reference tables linking national identity numbers (DNI) to institutional records
3. **Validation Algorithms**: Automated matching procedures for PID attributes against educational records
4. **Temporal Synchronization**: Systems to maintain up-to-date correlation between legal and institutional identity

#### **Identity Matching Process**
**The Critical Bridge**: Connecting **legal identity** (Spanish PID) with **institutional identity** (EducationalID)

**Three-Layer Validation**:
- **Primary Key Match**: DNI from PID directly correlates to student database primary key
- **Attribute Verification**: Name and birth date provide multi-factor identity confirmation
- **Enrollment Validation**: Current student status and credential issuance authorization

#### **Technical Architecture Benefits**
- **Separation of Concerns**: Legal identity management vs. institutional identity management
- **Real-time Correlation**: Instant matching between PID and educational records
- **Audit Compliance**: Complete traceability of identity matching decisions
- **Privacy Protection**: Minimum necessary data correlation with selective disclosure
- **Scalability**: Standardized patterns applicable across all European educational institutions

This infrastructure ensures that **every educational credential** is properly anchored to **verified legal identity** while maintaining the flexibility needed for diverse institutional requirements across Europe.

### 8.5 European Digital Sovereignty

This implementation represents **European digital sovereignty** in action:

- **European standards**: W3C VC, EBSI, eIDAS 2.0
- **European infrastructure**: EBSI trust registries and verification
- **European governance**: Member State cooperation and recognition
- **European values**: Privacy, security, and citizen control

---

## Appendix A: Schema Specifications

### A.1 eIDAS 2.0 PID Schema

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
                "enum": ["AF", "AX", "AL", "DZ", "AS", "AD", "AO", "AI", "AQ", "AG", "AR", "AM", "AW", "AU", "AT", "AZ", "BS", "BH", "BD", "BB", "BY", "BE", "BZ", "BJ", "BM", "BT", "BO", "BQ", "BA", "BW", "BV", "BR", "IO", "BN", "BG", "BF", "BI", "CV", "KH", "CM", "CA", "KY", "CF", "TD", "CL", "CN", "CX", "CC", "CO", "KM", "CD", "CG", "CK", "CR", "CI", "HR", "CU", "CW", "CY", "CZ", "DK", "DJ", "DM", "DO", "EC", "EG", "SV", "GQ", "ER", "EE", "SZ", "ET", "FK", "FO", "FJ", "FI", "FR", "GF", "PF", "TF", "GA", "GM", "GE", "DE", "GH", "GI", "GR", "GL", "GD", "GP", "GU", "GT", "GG", "GN", "GW", "GY", "HT", "HM", "VA", "HN", "HK", "HU", "IS", "IN", "ID", "IR", "IQ", "IE", "IM", "IL", "IT", "JM", "JP", "JE", "JO", "KZ", "KE", "KI", "KP", "KR", "KW", "KG", "LA", "LV", "LB", "LS", "LR", "LY", "LI", "LT", "LU", "MO", "MG", "MW", "MY", "MV", "ML", "MT", "MH", "MQ", "MR", "MU", "YT", "MX", "FM", "MD", "MC", "MN", "ME", "MS", "MA", "MZ", "MM", "NA", "NR", "NP", "NL", "NC", "NZ", "NI", "NE", "NG", "NU", "NF", "MK", "MP", "NO", "OM", "PK", "PW", "PS", "PA", "PG", "PY", "PE", "PH", "PN", "PL", "PT", "PR", "QA", "RE", "RO", "RU", "RW", "BL", "SH", "KN", "LC", "MF", "PM", "VC", "WS", "SM", "ST", "SA", "SN", "RS", "SC", "SL", "SG", "SX", "SK", "SI", "SB", "SO", "ZA", "GS", "SS", "ES", "LK", "SD", "SR", "SJ", "SE", "CH", "SY", "TW", "TJ", "TZ", "TH", "TL", "TG", "TK", "TO", "TT", "TN", "TR", "TM", "TC", "TV", "UG", "UA", "AE", "GB", "US", "UM", "UY", "UZ", "VU", "VE", "VN", "VG", "VI", "WF", "EH", "YE", "ZM", "ZW"]
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

### A.2 EducationalID Schema

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
              "description": "Specifies the home organization of the credential subject",
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
              "description": "Primary Affiliation within Home Organization",
              "type": "string"
            },
            "eduPersonAffiliation": {
              "description": "Affiliation within Home Organization. It can contain multiple values such as member, student, employee, faculty, staff, affiliate, alumni, etc.",
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "eduPersonScopedAffiliation": {
              "description": "The person's affiliations within Home Organization scoped with the Home Organization",
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

---

## Appendix B: Technical Reference Materials

### B.1 Authentic Source API Response

Complete API response from URV's authentic source service demonstrating successful **identity matching** between PID and educational records:

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
      "enrollmentStatus": "ACTIVE",
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
    "enrollmentDetails": {
      "institution": "Universitat Rovira i Virgili",
      "institutionCode": "ES-URV-25025",
      "enrollmentDate": "2023-09-15",
      "expectedGraduation": "2027-06-30",
      "credentialIssuanceAuthorized": true,
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

**Key Identity Matching Components**:

1. **Primary Key Correlation**: DNI from PID directly matches student database primary key
2. **Multi-Factor Validation**: Name and birth date provide additional identity confirmation  
3. **Confidence Scoring**: Mathematical confidence levels for each matching element
4. **Audit Trail**: Complete logging of identity matching process for compliance
5. **Institutional Identity Mapping**: Translation from legal identity to educational identity attributes

### B.2 Credential Offer Response

Complete OpenID4VCI credential offer with full metadata:

```json
{
  "credential_issuer": "https://issuer.eu/issuer",
  "credentials": [
    {
      "format": "jwt_vc",
      "types": [
        "VerifiableCredential",
        "VerifiableEducationalID"
      ],
      "credentialDefinition": {
        "type": [
          "VerifiableCredential",
          "VerifiableEducationalID"
        ]
      },
      "cryptographic_binding_methods_supported": [
        "did:ebsi"
      ],
      "credential_signing_alg_values_supported": [
        "ES256"
      ],
      "credential_display": {
        "name": "Educational ID",
        "description": "Official educational identity credential based on eduGAIN/SCHAC standards",
        "background_color": "#1f4788",
        "text_color": "#ffffff",
        "logo": {
          "url": "https://urv.cat/logo.png",
          "alt_text": "URV Logo"
        },
        "locale": "en-US"
      },
      "credential_subject": {
        "identifier": {
          "display": [{"name": "Principal Name", "locale": "en-US"}]
        },
        "schacPersonalUniqueCode": {
          "display": [{"name": "Personal Unique Code", "locale": "en-US"}]
        },
        "schacPersonalUniqueID": {
          "display": [{"name": "Personal Unique ID", "locale": "en-US"}]
        },
        "schacHomeOrganization": {
          "display": [{"name": "Home Organization", "locale": "en-US"}]
        },
        "familyName": {
          "display": [{"name": "Family Name", "locale": "en-US"}]
        },
        "firstName": {
          "display": [{"name": "First Name", "locale": "en-US"}]
        },
        "displayName": {
          "display": [{"name": "Display Name", "locale": "en-US"}]
        },
        "dateOfBirth": {
          "display": [{"name": "Date of Birth", "locale": "en-US"}]
        },
        "mail": {
          "display": [{"name": "Email", "locale": "en-US"}]
        },
        "eduPersonPrincipalName": {
          "display": [{"name": "Educational Principal Name", "locale": "en-US"}]
        },
        "eduPersonPrimaryAffiliation": {
          "display": [{"name": "Primary Affiliation", "locale": "en-US"}]
        },
        "eduPersonAffiliation": {
          "display": [{"name": "Affiliations", "locale": "en-US"}]
        },
        "eduPersonScopedAffiliation": {
          "display": [{"name": "Scoped Affiliations", "locale": "en-US"}]
        },
        "eduPersonAssurance": {
          "display": [{"name": "Assurance Levels", "locale": "en-US"}]
        }
      }
    }
  ],
  "grants": {
    "authorization_code": {
      "issuer_state": "eyJraWQiOiJkaWQ6ZWJzaTp6dFJvWXlKTmRHcjh0bU# EducationalID Issuance: Complete User Journey Narrative with Technical Implementation

**Document Version:** 1.0  
**Status:** Production Ready - Approved for v1.0  
**Authors:** Angel Palomares (angel.palomares@eviden.com)  
**Reviewers:** Lluis Ariño (lluisalfons.arino@urv.cat)  
**Implementation:** Pilot 2 - dPKI with EBSI Integration  
**Date:** June 2025  
**Project:** DC4EU - Digital Credentials for Europe

---

## Executive Summary

This document presents the complete narrative for EducationalID issuance within the DC4EU Pilot 2 framework, implementing a No Authorize OpenID VCI flow with **mandatory Verifiable Presentation of PID credentials**. The journey demonstrates the sophisticated orchestration between multiple actors, systems, and trust mechanisms that enable secure, interoperable educational credential issuance across European borders.

**Critical Prerequisite**: Before any EducationalID can be issued, the citizen's **Person Identification Data (PID)** must be verified through the eIDAS 2.0 framework. This foundational identity verification is the cornerstone upon which all educational credentials are built.

**Key Innovation**: This implementation showcases the world's first production-ready dPKI system for educational credentials, integrating EBSI trust registries with traditional educational infrastructure to create a seamless, trustworthy credential ecosystem built upon verified foundational identity.

**Bottom Line**: Maria García, a Spanish student, successfully obtains her EducationalID from Universitat Rovira i Virgili through a process that validates her foundational identity via Spanish PID, matches it with university records, and issues a cryptographically secure educational credential recognizable across all European universities.

---

## Quick Reference Guide

### Process Overview
1. **Prerequisites**: University data preparation and identity matching infrastructure
2. **PID Verification**: Mandatory foundational identity validation (Steps 1-22)
3. **Educational ID Issuance**: Institutional credential creation (Steps 23-33)
4. **Cross-Border Recognition**: European-wide validity and trust

### Key Actors
- **Student**: Maria García (credential holder)
- **University**: Universitat Rovira i Virgili (dual role: Authentic Source + Issuer)
- **Infrastructure**: EBSI trust registries and verification services
- **Governance**: Spanish Ministry (root trust anchor)

### Technical Standards
- **PID Schema**: eIDAS 2.0 Person Identification Data (EU Regulation 2024/2977)
- **EducationalID Schema**: eduGAIN/SCHAC standards for institutional identity
- **Protocols**: OpenID4VCI, W3C Verifiable Credentials, EBSI trust framework

---

## Table of Contents

1. [Infrastructure Prerequisites](#1-infrastructure-prerequisites)
2. [The Story: Maria's Educational Identity Journey](#2-the-story-marias-educational-identity-journey)
3. [Actor Ecosystem and Roles](#3-actor-ecosystem-and-roles)
4. [Technical Architecture Overview](#4-technical-architecture-overview)
5. [Detailed User Journey Flow](#5-detailed-user-journey-flow)
6. [Trust Verification Mechanisms](#6-trust-verification-mechanisms)
7. [Technical Message Details](#7-technical-message-details)
8. [Implementation Insights](#8-implementation-insights)
9. [**Appendix A: Schema Specifications**](#appendix-a-schema-specifications)
10. [**Appendix B: Technical Reference Materials**](#appendix-b-technical-reference-materials)

---

## 1. Infrastructure Prerequisites

### 1.1 Critical Foundation Requirements

**Before any EducationalID can be issued**, institutions must complete essential infrastructure preparation. This is not optional—it's a **mandatory prerequisite** for participation in the DC4EU framework.

### 1.2 Data Store Preparation for EAA Issuance

#### **Student Registry Population**
- **Complete enrollment database**: All active students with validated enrollment data
- **Historical records**: Previous academic years and graduation records
- **Programme metadata**: Detailed information about academic programmes and levels
- **Status management**: Real-time enrollment status tracking and updates

#### **Identity Correlation Infrastructure**
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
└── Estado: Activo → enrollment_status: ACTIVE
```

### 1.3 Identity Matching Mechanisms

#### **Multi-Layer Validation Process**
1. **Primary Key Correlation**: DNI from PID serves as primary matching key
2. **Attribute Verification**: Name and birth date provide additional confirmation
3. **Enrollment Validation**: Current student status and credential authorization
4. **Temporal Verification**: Enrollment dates and validity periods

#### **Real-Time Matching Infrastructure**
- **API-based correlation**: Standardized endpoints for identity resolution
- **Confidence scoring**: Mathematical confidence levels for matching accuracy
- **Exception handling**: Procedures for handling matching conflicts or failures
- **Performance optimization**: Sub-second response times for user experience

### 1.4 eIDAS 2.0 Compliance Infrastructure

#### **Authentic Source Certification**
- **Article 45b compliance**: Official certification as eIDAS 2.0 Authentic Source
- **Data quality assurance**: Verified accuracy and completeness of student records
- **API standardization**: eIDAS 2.0 compliant interfaces for data access
- **Security measures**: Encryption, access control, and audit capabilities

#### **Dual Role Architecture**
Universities must implement **clear separation** between:
- **Authentic Source function**: Authoritative data repository
- **Issuer function**: Credential creation and issuance
- **API gateway**: Standardized access layer between roles

---

## 2. The Story: Maria's Educational Identity Journey

### 2.1 Setting the Scene

**Meet Maria García**: A 20-year-old computer science student at Universitat Rovira i Virgili (URV) in Catalonia, Spain. Maria is about to begin her second year and needs to establish her digital educational identity to access university services, participate in international exchange programmes, and eventually apply for graduate studies across Europe.

It's Monday morning, September 2025. Maria sits in her dormitory room, smartphone in hand, ready to embark on a digital journey that will transform how she interacts with educational institutions across Europe. Little does she know that behind the simple act of "getting her student ID" lies a sophisticated dance of cryptographic protocols, trust verification systems, and international cooperation frameworks.

### 2.2 The Human Story

**The Challenge**: Maria needs more than just a physical student card. In the digital age of European education, she requires a **Verifiable Educational ID** that:
- Proves her authentic enrollment at URV
- Enables automatic recognition across EU universities
- Integrates with the EUDI Wallet ecosystem
- Supports future mobility and academic recognition

**The Solution**: Through the DC4EU framework, Maria will receive a cryptographically secure, EBSI-anchored Educational ID that serves as her digital passport to the European Education Area. **However, this credential can only be issued after her foundational identity has been verified through her Spanish Person Identification Data (PID)**—a mandatory prerequisite that ensures the highest levels of trust and security.

### 2.3 The Journey Begins

Maria opens her **EUDI Wallet** application, a sleek interface that hides the complexity of European digital identity infrastructure. She taps on "Add Educational Credential" and selects "Universitat Rovira i Virgili" from a list of participating institutions.

What happens next is a masterpiece of digital orchestration, involving multiple actors across different systems, countries, and trust domains.

---

## 3. Actor Ecosystem and Roles

### 3.1 Primary Actors

#### **🎓 Maria García (Natural Person/Student)**
- **Role**: Credential holder and primary user
- **Systems**: EUDI Wallet (Mobile Application)
- **Responsibilities**:
  - Initiate credential request
  - Provide consent for data sharing
  - Present PID for verification
  - Accept issued credential into wallet

#### **🏛️ Universitat Rovira i Virgili (Dual Role Institution)**
- **Primary Role**: Educational credential issuer
- **Secondary Role**: **eIDAS 2.0 Authentic Source** for student data
- **Systems**: 
  - Student Information System (Authentic Source function)
  - Credential Issuance Infrastructure (Issuer function)
- **Key Personnel**: Registrar Office, Academic Secretary
- **Critical Architecture Note**: URV operates in **dual capacity**:
  - **As Authentic Source**: Maintains authoritative student records under eIDAS 2.0 Article 45b
  - **As Issuer**: Consumes data from its own Authentic Source via standardized APIs
- **Responsibilities**:
  - Verify student enrollment and academic standing (Authentic Source role)
  - Issue cryptographically secure Educational IDs (Issuer role)
  - Maintain clear separation between data provision and credential issuance
  - Integrate with European trust frameworks

### 3.2 Technical Infrastructure Actors

#### **🔐 uSelf Issuer Agent (Credential Issuance Service)**
- **Role**: Technical orchestrator for credential issuance
- **Location**: University infrastructure (`lspurv.urv.cat`)
- **Responsibilities**:
  - Manage OpenID4VCI protocol flows
  - Coordinate with EBSI infrastructure
  - Handle cryptographic operations
  - Generate QR codes and credential offers

#### **📊 Authentic Source (Official eIDAS 2.0 Role)**
- **Role**: **Official eIDAS 2.0 Authentic Source** - Authoritative repository of verified student information
- **Played by**: Universitat Rovira i Virgili (in dual capacity)
- **System**: Standardized API-accessible student registry with encrypted records
- **eIDAS 2.0 Compliance**: Certified authentic source for educational data under Article 45b
- **Critical Prerequisites**:
  - **Data Store Preparation**: Pre-population of educational data repositories for potential EAA issuance
  - **Identity Matching Infrastructure**: Mechanisms to correlate legal identity (PID) with institutional identity (EducationalID)
  - **Cross-Reference Systems**: Linking Spanish DNI numbers with university student records
- **Responsibilities**:
  - Maintain authoritative student enrollment records
  - Provide standardized API access to verified data
  - Execute real-time identity matching between PID and educational records
  - Ensure data integrity and audit compliance
  - Support continuous synchronization between legal and institutional identities

#### **🌐 EBSI Infrastructure Ecosystem**

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

#### **🆔 uSelf PID Issuer Agent**
- **Role**: Personal Identity Data validation service
- **Function**: Verify student's foundational identity credentials

### 3.3 Governance and Oversight Actors

#### **🏛️ Spanish Ministry of Universities and Research**
- **Role**: Root Trust Anchor (RootTAO)
- **Authority**: Issues EAA credentials authorising URV to issue Educational IDs
- **Scope**: National level governance and compliance

#### **🇪🇺 European Blockchain Services Infrastructure (EBSI)**
- **Role**: European-level trust infrastructure
- **Function**: Provide decentralised trust registry and schema validation
- **Governance**: Multi-national consortium ensuring European standards

### 3.4 Supporting Systems

#### **📱 Student GUI (Web Interface)**
- **Role**: User-facing interface for credential requests
- **Location**: `https://uself-verifier-gui.lspurv.urv.cat/`
- **Function**: Generate QR codes and facilitate user interactions

#### **🔗 Mobile Wallet (EUDI Wallet)**
- **Role**: Credential storage and presentation
- **Standards**: W3C Verifiable Credentials, OpenID4VP
- **Features**: Multi-format support, selective disclosure, cross-border compatibility

---

## 4. Technical Architecture Overview

### 4.1 System Architecture Diagram

```mermaid
graph TB
    subgraph "Student Domain"
        Student[👩‍🎓 Maria García]
        Mobile[📱 EUDI Wallet]
    end
    
    subgraph "University Infrastructure (lspurv.urv.cat)"
        GUI[🖥️ Student GUI]
        Agent[🔧 uSelf Issuer Agent]
        AuthSource[📊 Authentic Source<br/>**eIDAS 2.0 Official Role**]
        DB[🗄️ Student Registry DB]
        API[🔗 Standardized APIs<br/>**eIDAS 2.0 Compliant**]
    end
    
    subgraph "EBSI Infrastructure"
        DIDR[🆔 DID Registry]
        TRR[🛡️ Trust Registry] 
        SR[📋 Schema Registry]
        Proxy[🌐 EBSI Proxy]
        PIDAgent[🔐 PID Issuer Agent]
    end
    
    subgraph "Trust Governance"
        Ministry[🏛️ Spanish Ministry]
        EAA[📜 EAA Credentials<br/>**Authentic Source Authority**]
    end

    Student --> Mobile
    Mobile <--> GUI
    GUI <--> Agent
    Agent <--> API
    API <--> AuthSource
    AuthSource <--> DB
    
    Agent <--> DIDR
    Agent <--> TRR
    Agent <--> SR
    Agent <--> Proxy
    Proxy <--> PIDAgent
    
    Ministry --> EAA
    EAA --> TRR
    TRR --> Agent
    
    classDef eidas fill:#e1f5fe,stroke:#01579b,stroke-width:3px
    class AuthSource,API,EAA eidas
```

**Key Architectural Principle**: The university operates in **dual capacity** under eIDAS 2.0:
1. **As Authentic Source**: Authoritative holder of student data (Article 45b compliance)
2. **As Issuer**: Consumer of authentic source data via standardized APIs for credential creation

### 4.2 Trust Flow Architecture

The system implements a sophisticated **multi-layer trust model**:

1. **Foundational Layer**: Spanish national identity infrastructure provides PID
2. **Institutional Layer**: URV's authorisation via Spanish Ministry EAA credentials
3. **European Layer**: EBSI trust registries validate cross-border recognition
4. **Technical Layer**: Cryptographic proofs ensure credential integrity

### 4.3 Protocol Stack

- **Application Layer**: OpenID for Verifiable Credentials (OID4VCI)
- **Credential Layer**: W3C Verifiable Credentials Data Model
- **Trust Layer**: EBSI trust registries and EAA framework
- **Cryptographic Layer**: ES256 signatures, DID-based authentication
- **Transport Layer**: HTTPS with additional security headers

---

## 5. Detailed User Journey Flow

### 5.1 Phase 1: Journey Initiation (Steps 1-6)

#### **Step 1: The Request**
*Monday, 9:15 AM - Maria's dormitory*

Maria opens her web browser and navigates to the URV student portal. The interface is clean and multilingual, supporting both Catalan and Spanish as befitting the region's linguistic diversity.

**Technical Action**: 
```http
GET https://student-web/issue
```

**Behind the Scenes**: The student GUI system initialises, checking server status and preparing the credential issuance infrastructure.

#### **Step 2: Credential Offer Generation**
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

#### **Step 3: QR Code Magic**
*The bridge between digital and physical*

The Student GUI receives the credential offer and transforms it into a QR code—a visual bridge between the web interface and Maria's mobile wallet.

**Technical Implementation**:
```bash
openid-credential-offer://?credential_offer_uri=https://issuer.eu/issuer/offers/719307744250317677
```

The QR code contains not the full credential offer (which would be too large) but a secure URI pointing to the offer details. This follows EBSI recommendations for optimal user experience.

#### **Step 4: Mobile Engagement**
*Maria scans the QR code*

Maria holds up her EUDI Wallet and scans the QR code. The wallet's sophisticated parsing engine recognises the OpenID credential offer format and prepares for the issuance flow.

**User Experience**: The wallet displays a clear, user-friendly interface:
- "Universitat Rovira i Virgili wants to issue your Educational ID"
- "This credential will allow you to access university services and participate in European student mobility"
- "Tap to continue"

#### **Step 5: Protocol Handshake Initiation**
*Behind the scenes coordination*

The mobile wallet processes the QR code and initiates the OpenID4VCI flow, establishing a secure communication channel with the university's systems.

**Technical Flow**:
```http
HTTP 302 Redirect to Authorization Endpoint
```

#### **Step 6: Authorization Request**
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

### 5.2 Phase 2: Foundational Identity Verification - The Mandatory PID Process (Steps 7-22)

**Critical Process Note**: This phase represents the **absolute prerequisite** for EducationalID issuance. Under eIDAS 2.0 regulations and DC4EU framework requirements, **no educational credential can be issued without verified foundational identity**. The PID verification process ensures that Maria's educational credentials are anchored to her legally verified national identity.

#### **Step 7: The Trust Challenge**
*Proving who you are at the foundational level*

The uSelf Issuer Agent responds with a **direct_post** challenge, requesting Maria to present her PID credential. This is not optional—it's a **mandatory step** that forms the foundation of all subsequent trust relationships.

**User Experience**: Maria's wallet displays:
- "⚠️ **Identity Verification Required**: To issue your Educational ID, the university must verify your foundational identity"
- "🆔 **Spanish PID Required**: Please present your Person Identification Data (PID) issued by Spanish authorities"
- "🔒 **Security Notice**: This verification is mandatory under eIDAS 2.0 regulations"
- "ℹ️ This information will be used only for identity verification purposes"

#### **Step 8: Consent and Privacy**
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

#### **Step 9-10: The Digital Handshake**
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

**Maria's PID Credential Structure** (eIDAS 2.0 Compliant - See [Appendix A.1](#a1-eidas-20-pid-schema)):

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

#### **Steps 11-21: The Foundational Trust Verification Symphony**
*EBSI infrastructure validates Maria's foundational identity*

What happens next is invisible to Maria but represents **the most critical trust verification process** in the entire digital credential ecosystem. The uSelf Issuer Agent orchestrates a **comprehensive verification of Maria's foundational identity** across multiple EBSI services:

**Step 11-12: PID DID Resolution**
```http
GET https://ebsi-did-registry/did/{maria-pid-issuer-did}
```
**Purpose**: Resolve the DID of the Spanish authority that issued Maria's PID to verify the cryptographic keys and ensure the PID credential is properly signed by legitimate national authorities.

**Step 13-14: National Authority Trust Registry Verification**
```http
GET https://ebsi-tr-registry/tr
```
**Purpose**: Check the EBSI Trust Registry to verify that the Spanish national identity authorities are officially authorised to issue Person Identification Data credentials under eIDAS 2.0.

**Step 15-16: PID Schema Validation**
```http
GET https://ebsi-schema-registry/schema
```
**Purpose**: Validate that Maria's PID credential conforms to the official European PID schema and data format requirements.

**Step 17-20: Comprehensive PID Verification**
```http
GET https://ebsi-proxy/verify
```
**Purpose**: The EBSI Proxy performs the **complete foundational identity verification**, including:
- ✅ **Cryptographic signature validation** of the PID credential
- ✅ **Revocation status checking** to ensure the PID hasn't been revoked
- ✅ **Trust chain verification** back to Spanish national authorities
- ✅ **eIDAS 2.0 compliance verification** for regulatory alignment
- ✅ **Temporal validity checking** to ensure the PID is currently valid

**Step 21-22: Foundational Identity Verification Success**
The comprehensive verification process completes successfully, **confirming Maria's foundational identity**, and the system issues an authorization code to proceed with Educational ID issuance.

**Verification Result**: The system now has **cryptographic proof** that:
- Maria is who she claims to be (verified by Spanish national authorities)
- Her identity credential is valid and not revoked
- The verification complies with all eIDAS 2.0 requirements
- She is legally authorised to receive educational credentials in Spain

### 5.3 Phase 3: Credential Issuance (Steps 23-33)

#### **Step 23-24: Access Token Exchange**
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

#### **Step 25-26: The Moment of Truth**
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

#### **Step 27-30: Authentic Source Data Retrieval via Standardized APIs**
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
   - **Enrollment Verification**: Current active enrollment status

**Database Query (Internal to Authentic Source)**:
```sql
SELECT s.studentId, s.enrollmentStatus, s.programme, s.level, 
       s.enrollmentDate, s.expectedGraduation, s.institution,
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

**Authentic Source Response** (via standardized API - See [Appendix B.1](#b1-authentic-source-api-response)):

The authentic source provides a comprehensive response that demonstrates successful **identity matching** between Maria's legal identity (PID) and her institutional identity (student record). This response includes both the verified correlation and the educational data needed for EducationalID issuance.

**Critical Identity Matching Results**:
- ✅ **DNI Match**: 12345678A found in student database
- ✅ **Name Match**: García, Maria confirmed in enrollment records  
- ✅ **Birth Date Match**: 2004-03-15 validated against university records
- ✅ **Enrollment Verified**: Active student status confirmed
- ✅ **Credential Authorization**: Student authorized for EducationalID issuance

**Architectural Innovation**: This design demonstrates how eIDAS 2.0 enables institutional **dual roles** while maintaining:
- **Trust boundaries**: Clear separation of functions even within the same organization
- **Identity correlation**: Robust matching between legal and institutional identity
- **Interoperability**: Standardized APIs that work across organizational boundaries
- **Compliance**: Full regulatory alignment with European digital identity frameworks

#### **Step 31: Credential Generation**
*The digital birth certificate*

The agent constructs Maria's Educational ID credential using the **eduGAIN/SCHAC-based schema** (See [Appendix A.2](#a2-educationalid-schema)) rather than ELM. This credential follows the specific EducationalID schema designed for non-foundational identity in educational contexts.

The generated EducationalID credential incorporates:
- **Verified Identity Data**: From the PID verification process
- **Educational Attributes**: Following eduGAIN/SCHAC standards
- **Institutional Affiliation**: URV-specific organizational data
- **Assurance Levels**: REFEDS framework compliance

**Key Schema Features** (detailed in [Appendix A.2](#a2-educationalid-schema)):
- **SCHAC Unique Codes**: For cross-institutional identity resolution
- **eduGAIN Attributes**: Standard educational federation attributes
- **REFEDS Assurance**: Identity assurance framework compliance
- **Multi-value Support**: Arrays for affiliations and assurance levels

#### **Step 32: Event Notification**
*System coordination*

The agent sends a `credential_issued` event to the Student GUI, enabling real-time updates to any connected systems and maintaining audit trails for compliance purposes.

#### **Step 33: Delivery to Maria**
*The moment of completion*

The Educational ID credential is delivered to Maria's EUDI Wallet. The wallet validates the credential signature, stores it securely, and notifies Maria of successful issuance.

**User Experience**: Maria sees a success notification:
- "Your Educational ID has been issued successfully!"
- "You can now access university services and participate in international programmes"
- "This credential is valid until June 30, 2027"

---

## 6. Trust Verification Mechanisms

### 6.1 Multi-Layer Trust Architecture with eIDAS 2.0 Compliance

The EducationalID issuance process implements sophisticated **multi-layer trust verification** with full eIDAS 2.0 regulatory alignment, **built upon mandatory foundational identity verification**:

#### **Layer 1: Foundational Identity (PID) - MANDATORY PREREQUISITE**
- **Role**: **Absolute prerequisite** for all educational credentials
- **Source**: Spanish national identity infrastructure
- **Verification**: eIDAS-compliant digital identity (mandatory)
- **Assurance Level**: High (Level of Assurance 3)
- **Cryptographic Standard**: ES256 signatures
- **Legal Basis**: eIDAS 2.0 Article 3 - foundational identity requirement
- **Process**: **Complete EBSI verification of PID before any educational credential issuance**

#### **Layer 2: Authentic Source Authority (eIDAS 2.0 Article 45b)**
- **Role**: URV as certified eIDAS 2.0 Authentic Source
- **Authority**: Spanish Ministry EAA credentials authorizing authentic source function
- **Data Integrity**: Authoritative student records with cryptographic proofs
- **API Standards**: eIDAS 2.0 compliant standardized access protocols
- **Dependency**: **Only operates after Layer 1 (PID) verification is complete**

#### **Layer 3: Institutional Issuance Authority (EAA)**
- **Source**: Spanish Ministry of Universities and Research
- **Mechanism**: Electronic Attestation of Attributes (EAA)
- **Scope**: Authorizes URV to issue Educational IDs based on authentic source data
- **Validation**: EBSI Trust Registry verification
- **Prerequisite**: **Requires verified foundational identity from Layer 1**

#### **Layer 4: European Recognition (EBSI)**
- **Framework**: European Blockchain Services Infrastructure
- **Function**: Cross-border trust propagation
- **Standards**: W3C Verifiable Credentials, eduGAIN/SCHAC
- **Governance**: Multi-national European cooperation
- **Foundation**: **Built upon verified PID from Layer 1**

#### **Layer 5: Technical Integrity**
- **Cryptography**: Multiple signature verification
- **Revocation**: Real-time status checking
- **Audit**: Comprehensive logging and traceability
- **Privacy**: Selective disclosure and data minimization
- **Anchor**: **All technical integrity traces back to verified PID**

### 6.2 Trust Chain Example with eIDAS 2.0 Roles

```
🇪🇺 European Union (eIDAS 2.0 Regulatory Framework)
  ↓
🇪🇸 Spanish Ministry of Universities (Root Trust Anchor)
  ↓ [Issues EAA - Authentic Source Authority]
🏛️ URV as Authentic Source (eIDAS 2.0 Article 45b Role)
  ↓ [Standardized API provides verified data]
🔧 URV as Issuer (EAA-Authorized Credential Issuer)
  ↓ [Issues Educational ID based on authentic source data]
👩‍🎓 Maria García (Credential Holder)
  ↓ [Presents Credential]
🏫 Any European University (Relying Party)
```

**Key Innovation**: The dual role architecture demonstrates how institutions can operate as both **Authentic Source** and **Issuer** under eIDAS 2.0 while maintaining clear functional separation and regulatory compliance.

### 6.3 Security Properties

- **Authenticity**: Cryptographically proven issuer identity
- **Integrity**: Tamper-evident credential structure  
- **Non-repudiation**: Immutable audit trail
- **Privacy**: Minimal data disclosure with consent
- **Availability**: Distributed verification infrastructure
- **Interoperability**: European standards compliance

---

## 7. Technical Message Details

### 7.1 Credential Offer Response (Complete)

The credential offer provides comprehensive metadata about the EducationalID credential, including display parameters and supported credential subject attributes (detailed structure in [Appendix B.2](#b2-credential-offer-response)).

**Key Features**:
- **Credential Type**: `VerifiableEducationalID` with `jwt_vc` format
- **Display Configuration**: URV branding and multilingual support
- **Attribute Mapping**: Complete eduGAIN/SCHAC attribute support
- **Cryptographic Binding**: ES256 algorithm with DID-based binding

### 7.2 Authorization Request (Complete)

The authorization request demonstrates sophisticated presentation definition validation ensuring only valid **eIDAS 2.0 compliant PID credentials** are accepted (complete technical details in [Appendix B.3](#b3-authorization-request)).

**Key Validation Requirements**:
- ✅ **Credential Type**: Must be `PersonIdentificationData` (eIDAS 2.0 PID)
- ✅ **Required Fields**: `family_name`, `given_name`, `birth_date`, `nationality`
- ✅ **Administrative Number**: `personal_administrative_number` for unique identification
- ✅ **Issuing Country**: Must be "ES" (Spain) for this university
- ✅ **Cryptographic Validation**: ES256 signature algorithm required

### 7.3 Final Credential Response

The final credential response delivers the completed EducationalID to Maria's EUDI Wallet in JWT format, cryptographically signed by URV's institutional key (complete response structure in [Appendix B.4](#b4-final-credential-response)).

**Response Components**:
- **JWT-encoded Credential**: Complete EducationalID in W3C VC format
- **Digital Signature**: ES256 signature by URV's DID key
- **EBSI Anchoring**: Schema and trust registry references
- **Expiration Management**: Validity period and renewal information

---

## 8. Implementation Insights

### 8.1 Schema Architecture: eIDAS 2.0 PID vs. eduGAIN EducationalID

**Critical Distinction**: The EducationalID journey demonstrates the **architectural separation** between different credential types in the DC4EU framework:

#### **Foundational Identity (PID) - eIDAS 2.0 Regulation Compliant**
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

#### **Non-Foundational Identity Credentials (EducationalID)**
- **Schema Base**: eduGAIN/SCHAC standards, not ELM
- **Purpose**: Institutional identity and affiliation
- **Standards**: REFEDS, eduGAIN, SCHAC
- **Focus**: "Who you are within an educational context"
- **Key Attributes**: 
  - Educational identity: `eduPersonPrincipalName`, `eduPersonScopedAffiliation`
  - Institutional affiliation: `schacPersonalUniqueCode`, `schacHomeOrganization`
  - Assurance: REFEDS Assurance Framework compliance

#### **Academic Achievement Credentials (ELM-Based)**
- **Schema Base**: European Learning Model (ELM) 3.2
- **Purpose**: Learning outcomes and qualifications
- **Standards**: ELM, EDCI, Europass
- **Focus**: "What you have learned and achieved"
- **Key Attributes**:
  - Learning achievements, qualifications
  - Assessment results, credit systems
  - Quality assurance information

### 8.2 eIDAS 2.0 PID Integration Benefits

The PID's use of **official eIDAS 2.0 standards** provides:

1. **Legal Certainty**: Direct compliance with EU Regulation 2024/2977
2. **Cross-Border Recognition**: Automatic recognition across all EU Member States
3. **High Assurance**: Highest level of identity verification available in EU
4. **Standardized Format**: Common structure across all European identity providers
5. **Privacy Protection**: Built-in selective disclosure capabilities
6. **Administrative Integration**: Direct link to national identity systems

### 8.3 Identity Verification Chain

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

### 8.4 Technical Innovation: Identity Matching Infrastructure

The DC4EU framework's **identity matching infrastructure** represents a critical innovation in European digital identity:

#### **Pre-Deployment Data Preparation**
Before any credential can be issued, institutions must establish:

1. **Comprehensive Data Stores**: Complete population of student databases with verified enrollment information
2. **Identity Correlation Systems**: Cross-reference tables linking national identity numbers (DNI) to institutional records
3. **Validation Algorithms**: Automated matching procedures for PID attributes against educational records
4. **Temporal Synchronization**: Systems to maintain up-to-date correlation between legal and institutional identity

#### **Identity Matching Process**
**The Critical Bridge**: Connecting **legal identity** (Spanish PID) with **institutional identity** (EducationalID)

**Three-Layer Validation**:
- **Primary Key Match**: DNI from PID directly correlates to student database primary key
- **Attribute Verification**: Name and birth date provide multi-factor identity confirmation
- **Enrollment Validation**: Current student status and credential issuance authorization

#### **Technical Architecture Benefits**
- **Separation of Concerns**: Legal identity management vs. institutional identity management
- **Real-time Correlation**: Instant matching between PID and educational records
- **Audit Compliance**: Complete traceability of identity matching decisions
- **Privacy Protection**: Minimum necessary data correlation with selective disclosure
- **Scalability**: Standardized patterns applicable across all European educational institutions

This infrastructure ensures that **every educational credential** is properly anchored to **verified legal identity** while maintaining the flexibility needed for diverse institutional requirements across Europe.

### 8.5 European Digital Sovereignty

This implementation represents **European digital sovereignty** in action:

- **European standards**: W3C VC, EBSI, eIDAS 2.0
- **European infrastructure**: EBSI trust registries and verification
- **European governance**: Member State cooperation and recognition
- **European values**: Privacy, security, and citizen control

---

## Appendix A: Schema Specifications

### A.1 eIDAS 2.0 PID Schema

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
                "enum": ["AF", "AX", "AL", "DZ", "AS", "AD", "AO", "AI", "AQ", "AG", "AR", "AM", "AW", "AU", "AT", "AZ", "BS", "BH", "BD", "BB", "BY", "BE", "BZ", "BJ", "BM", "BT", "BO", "BQ", "BA", "BW", "BV", "BR", "IO", "BN", "BG", "BF", "BI", "CV", "KH", "CM", "CA", "KY", "CF", "TD", "CL", "CN", "CX", "CC", "CO", "KM", "CD", "CG", "CK", "CR", "CI", "HR", "CU", "CW", "CY", "CZ", "DK", "DJ", "DM", "DO", "EC", "EG", "SV", "GQ", "ER", "EE", "SZ", "ET", "FK", "FO", "FJ", "FI", "FR", "GF", "PF", "TF", "GA", "GM", "GE", "DE", "GH", "GI", "GR", "GL", "GD", "GP", "GU", "GT", "GG", "GN", "GW", "GY", "HT", "HM", "VA", "HN", "HK", "HU", "IS", "IN", "ID", "IR", "IQ", "IE", "IM", "IL", "IT", "JM", "JP", "JE", "JO", "KZ", "KE", "KI", "KP", "KR", "KW", "KG", "LA", "LV", "LB", "LS", "LR", "LY", "LI", "LT", "LU", "MO", "MG", "MW", "MY", "MV", "ML", "MT", "MH", "MQ", "MR", "MU", "YT", "MX", "FM", "MD", "MC", "MN", "ME", "MS", "MA", "MZ", "MM", "NA", "NR", "NP", "NL", "NC", "NZ", "NI", "NE", "NG", "NU", "NF", "MK", "MP", "NO", "OM", "PK", "PW", "PS", "PA", "PG", "PY", "PE", "PH", "PN", "PL", "PT", "PR", "QA", "RE", "RO", "RU", "RW", "BL", "SH", "KN", "LC", "MF", "PM", "VC", "WS", "SM", "ST", "SA", "SN", "RS", "SC", "SL", "SG", "SX", "SK", "SI", "SB", "SO", "ZA", "GS", "SS", "ES", "LK", "SD", "SR", "SJ", "SE", "CH", "SY", "TW", "TJ", "TZ", "TH", "TL", "TG", "TK", "TO", "TT", "TN", "TR", "TM", "TC", "TV", "UG", "UA", "AE", "GB", "US", "UM", "UY", "UZ", "VU", "VE", "VN", "VG", "VI", "WF", "EH", "YE", "ZM", "ZW"]
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

### A.2 EducationalID Schema

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
              "description": "Specifies the home organization of the credential subject",
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
              "description": "Primary Affiliation within Home Organization",
              "type": "string"
            },
            "eduPersonAffiliation": {
              "description": "Affiliation within Home Organization. It can contain multiple values such as member, student, employee, faculty, staff, affiliate, alumni, etc.",
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "eduPersonScopedAffiliation": {
              "description": "The person's affiliations within Home Organization scoped with the Home Organization",
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

---

## Appendix B: Technical Reference Materials

### B.1 Authentic Source API Response

Complete API response from URV's authentic source service demonstrating successful **identity matching** between PID and educational records:

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
      "enrollmentStatus": "ACTIVE",
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
    "enrollmentDetails": {
      "institution": "Universitat Rovira i Virgili",
      "institutionCode": "ES-URV-25025",
      "enrollmentDate": "2023-09-15",
      "expectedGraduation": "2027-06-30",
      "credentialIssuanceAuthorized": true,
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

**Key Identity Matching Components**:

1. **Primary Key Correlation**: DNI from PID directly matches student database primary key
2. **Multi-Factor Validation**: Name and birth date provide additional identity confirmation  
3. **Confidence Scoring**: Mathematical confidence levels for each matching element
4. **Audit Trail**: Complete logging of identity matching process for compliance
5. **Institutional Identity Mapping**: Translation from legal identity to educational identity attributes


---


### B.2 Credential Offer Response

Complete OpenID4VCI credential offer with full metadata:

```json
{
  "credential_issuer": "https://issuer.eu/issuer",
  "credentials": [
    {
      "format": "jwt_vc",
      "types": [
        "VerifiableCredential",
        "VerifiableEducationalID"
      ],
      "credentialDefinition": {
        "type": [
          "VerifiableCredential",
          "VerifiableEducationalID"
        ]
      },
      "cryptographic_binding_methods_supported": [
        "did:ebsi"
      ],
      "credential_signing_alg_values_supported": [
        "ES256"
      ],
      "credential_display": {
        "name": "Educational ID",
        "description": "Official educational identity credential based on eduGAIN/SCHAC standards",
        "background_color": "#1f4788",
        "text_color": "#ffffff",
        "logo": {
          "url": "https://urv.cat/logo.png",
          "alt_text": "URV Logo"
        },
        "locale": "en-US"
      },
      "credential_subject": {
        "identifier": {
          "display": [{"name": "Principal Name", "locale": "en-US"}]
        },
        "schacPersonalUniqueCode": {
          "display": [{"name": "Personal Unique Code", "locale": "en-US"}]
        },
        "schacPersonalUniqueID": {
          "display": [{"name": "Personal Unique ID", "locale": "en-US"}]
        },
        "schacHomeOrganization": {
          "display": [{"name": "Home Organization", "locale": "en-US"}]
        },
        "familyName": {
          "display": [{"name": "Family Name", "locale": "en-US"}]
        },
        "firstName": {
          "display": [{"name": "First Name", "locale": "en-US"}]
        },
        "displayName": {
          "display": [{"name": "Display Name", "locale": "en-US"}]
        },
        "dateOfBirth": {
          "display": [{"name": "Date of Birth", "locale": "en-US"}]
        },
        "mail": {
          "display": [{"name": "Email", "locale": "en-US"}]
        },
        "eduPersonPrincipalName": {
          "display": [{"name": "Educational Principal Name", "locale": "en-US"}]
        },
        "eduPersonPrimaryAffiliation": {
          "display": [{"name": "Primary Affiliation", "locale": "en-US"}]
        },
        "eduPersonAffiliation": {
          "display": [{"name": "Affiliations", "locale": "en-US"}]
        },
        "eduPersonScopedAffiliation": {
          "display": [{"name": "Scoped Affiliations", "locale": "en-US"}]
        },
        "eduPersonAssurance": {
          "display": [{"name": "Assurance Levels", "locale": "en-US"}]
        }
      }
    }
  ],
  "grants": {
    "authorization_code": {
      "issuer_state": "eyJraWQiOiJkaWQ6ZWJzaTp6dFJvWXlKTmRHcjh0bU# EducationalID Issuance: Complete User Journey Narrative with Technical Implementation

      ```

**Document Version:** 1.0  
**Status:** Production Ready - Approved for v1.0  
**Authors:** Angel Palomares (angel.palomares@eviden.com)  
**Reviewers:** Lluis Ariño (lluisalfons.arino@urv.cat)  
**Implementation:** Pilot 2 - dPKI with EBSI Integration  
**Date:** June 2025  
**Project:** DC4EU - Digital Credentials for Europe

---

## Executive Summary

This document presents the complete narrative for EducationalID issuance within the DC4EU Pilot 2 framework, implementing a No Authorize OpenID VCI flow with **mandatory Verifiable Presentation of PID credentials**. The journey demonstrates the sophisticated orchestration between multiple actors, systems, and trust mechanisms that enable secure, interoperable educational credential issuance across European borders.

**Critical Prerequisite**: Before any EducationalID can be issued, the citizen's **Person Identification Data (PID)** must be verified through the eIDAS 2.0 framework. This foundational identity verification is the cornerstone upon which all educational credentials are built.

**Key Innovation**: This implementation showcases the world's first production-ready dPKI system for educational credentials, integrating EBSI trust registries with traditional educational infrastructure to create a seamless, trustworthy credential ecosystem built upon verified foundational identity.

**Bottom Line**: Maria García, a Spanish student, successfully obtains her EducationalID from Universitat Rovira i Virgili through a process that validates her foundational identity via Spanish PID, matches it with university records, and issues a cryptographically secure educational credential recognizable across all European universities.

---

## Quick Reference Guide

### Process Overview
1. **Prerequisites**: University data preparation and identity matching infrastructure
2. **PID Verification**: Mandatory foundational identity validation (Steps 1-22)
3. **Educational ID Issuance**: Institutional credential creation (Steps 23-33)
4. **Cross-Border Recognition**: European-wide validity and trust

### Key Actors
- **Student**: Maria García (credential holder)
- **University**: Universitat Rovira i Virgili (dual role: Authentic Source + Issuer)
- **Infrastructure**: EBSI trust registries and verification services
- **Governance**: Spanish Ministry (root trust anchor)

### Technical Standards
- **PID Schema**: eIDAS 2.0 Person Identification Data (EU Regulation 2024/2977)
- **EducationalID Schema**: eduGAIN/SCHAC standards for institutional identity
- **Protocols**: OpenID4VCI, W3C Verifiable Credentials, EBSI trust framework

---

## Table of Contents

1. [Infrastructure Prerequisites](#1-infrastructure-prerequisites)
2. [The Story: Maria's Educational Identity Journey](#2-the-story-marias-educational-identity-journey)
3. [Actor Ecosystem and Roles](#3-actor-ecosystem-and-roles)
4. [Technical Architecture Overview](#4-technical-architecture-overview)
5. [Detailed User Journey Flow](#5-detailed-user-journey-flow)
6. [Trust Verification Mechanisms](#6-trust-verification-mechanisms)
7. [Technical Message Details](#7-technical-message-details)
8. [Implementation Insights](#8-implementation-insights)
9. [**Appendix A: Schema Specifications**](#appendix-a-schema-specifications)
10. [**Appendix B: Technical Reference Materials**](#appendix-b-technical-reference-materials)

---

## 1. Infrastructure Prerequisites

### 1.1 Critical Foundation Requirements

**Before any EducationalID can be issued**, institutions must complete essential infrastructure preparation. This is not optional—it's a **mandatory prerequisite** for participation in the DC4EU framework.

### 1.2 Data Store Preparation for EAA Issuance

#### **Student Registry Population**
- **Complete enrollment database**: All active students with validated enrollment data
- **Historical records**: Previous academic years and graduation records
- **Programme metadata**: Detailed information about academic programmes and levels
- **Status management**: Real-time enrollment status tracking and updates

#### **Identity Correlation Infrastructure**
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
└── Estado: Activo → enrollment_status: ACTIVE
```

### 1.3 Identity Matching Mechanisms

#### **Multi-Layer Validation Process**
1. **Primary Key Correlation**: DNI from PID serves as primary matching key
2. **Attribute Verification**: Name and birth date provide additional confirmation
3. **Enrollment Validation**: Current student status and credential authorization
4. **Temporal Verification**: Enrollment dates and validity periods

#### **Real-Time Matching Infrastructure**
- **API-based correlation**: Standardized endpoints for identity resolution
- **Confidence scoring**: Mathematical confidence levels for matching accuracy
- **Exception handling**: Procedures for handling matching conflicts or failures
- **Performance optimization**: Sub-second response times for user experience

### 1.4 eIDAS 2.0 Compliance Infrastructure

#### **Authentic Source Certification**
- **Article 45b compliance**: Official certification as eIDAS 2.0 Authentic Source
- **Data quality assurance**: Verified accuracy and completeness of student records
- **API standardization**: eIDAS 2.0 compliant interfaces for data access
- **Security measures**: Encryption, access control, and audit capabilities

#### **Dual Role Architecture**
Universities must implement **clear separation** between:
- **Authentic Source function**: Authoritative data repository
- **Issuer function**: Credential creation and issuance
- **API gateway**: Standardized access layer between roles

---

## 2. The Story: Maria's Educational Identity Journey

### 2.1 Setting the Scene

**Meet Maria García**: A 20-year-old computer science student at Universitat Rovira i Virgili (URV) in Catalonia, Spain. Maria is about to begin her second year and needs to establish her digital educational identity to access university services, participate in international exchange programmes, and eventually apply for graduate studies across Europe.

It's Monday morning, September 2025. Maria sits in her dormitory room, smartphone in hand, ready to embark on a digital journey that will transform how she interacts with educational institutions across Europe. Little does she know that behind the simple act of "getting her student ID" lies a sophisticated dance of cryptographic protocols, trust verification systems, and international cooperation frameworks.

### 2.2 The Human Story

**The Challenge**: Maria needs more than just a physical student card. In the digital age of European education, she requires a **Verifiable Educational ID** that:
- Proves her authentic enrollment at URV
- Enables automatic recognition across EU universities
- Integrates with the EUDI Wallet ecosystem
- Supports future mobility and academic recognition

**The Solution**: Through the DC4EU framework, Maria will receive a cryptographically secure, EBSI-anchored Educational ID that serves as her digital passport to the European Education Area. **However, this credential can only be issued after her foundational identity has been verified through her Spanish Person Identification Data (PID)**—a mandatory prerequisite that ensures the highest levels of trust and security.

### 2.3 The Journey Begins

Maria opens her **EUDI Wallet** application, a sleek interface that hides the complexity of European digital identity infrastructure. She taps on "Add Educational Credential" and selects "Universitat Rovira i Virgili" from a list of participating institutions.

What happens next is a masterpiece of digital orchestration, involving multiple actors across different systems, countries, and trust domains.

---

## 3. Actor Ecosystem and Roles

### 3.1 Primary Actors

#### **🎓 Maria García (Natural Person/Student)**
- **Role**: Credential holder and primary user
- **Systems**: EUDI Wallet (Mobile Application)
- **Responsibilities**:
  - Initiate credential request
  - Provide consent for data sharing
  - Present PID for verification
  - Accept issued credential into wallet

#### **🏛️ Universitat Rovira i Virgili (Dual Role Institution)**
- **Primary Role**: Educational credential issuer
- **Secondary Role**: **eIDAS 2.0 Authentic Source** for student data
- **Systems**: 
  - Student Information System (Authentic Source function)
  - Credential Issuance Infrastructure (Issuer function)
- **Key Personnel**: Registrar Office, Academic Secretary
- **Critical Architecture Note**: URV operates in **dual capacity**:
  - **As Authentic Source**: Maintains authoritative student records under eIDAS 2.0 Article 45b
  - **As Issuer**: Consumes data from its own Authentic Source via standardized APIs
- **Responsibilities**:
  - Verify student enrollment and academic standing (Authentic Source role)
  - Issue cryptographically secure Educational IDs (Issuer role)
  - Maintain clear separation between data provision and credential issuance
  - Integrate with European trust frameworks

### 3.2 Technical Infrastructure Actors

#### **🔐 uSelf Issuer Agent (Credential Issuance Service)**
- **Role**: Technical orchestrator for credential issuance
- **Location**: University infrastructure (`lspurv.urv.cat`)
- **Responsibilities**:
  - Manage OpenID4VCI protocol flows
  - Coordinate with EBSI infrastructure
  - Handle cryptographic operations
  - Generate QR codes and credential offers

#### **📊 Authentic Source (Official eIDAS 2.0 Role)**
- **Role**: **Official eIDAS 2.0 Authentic Source** - Authoritative repository of verified student information
- **Played by**: Universitat Rovira i Virgili (in dual capacity)
- **System**: Standardized API-accessible student registry with encrypted records
- **eIDAS 2.0 Compliance**: Certified authentic source for educational data under Article 45b
- **Critical Prerequisites**:
  - **Data Store Preparation**: Pre-population of educational data repositories for potential EAA issuance
  - **Identity Matching Infrastructure**: Mechanisms to correlate legal identity (PID) with institutional identity (EducationalID)
  - **Cross-Reference Systems**: Linking Spanish DNI numbers with university student records
- **Responsibilities**:
  - Maintain authoritative student enrollment records
  - Provide standardized API access to verified data
  - Execute real-time identity matching between PID and educational records
  - Ensure data integrity and audit compliance
  - Support continuous synchronization between legal and institutional identities

#### **🌐 EBSI Infrastructure Ecosystem**

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

#### **🆔 uSelf PID Issuer Agent**
- **Role**: Personal Identity Data validation service
- **Function**: Verify student's foundational identity credentials

### 3.3 Governance and Oversight Actors

#### **🏛️ Spanish Ministry of Universities and Research**
- **Role**: Root Trust Anchor (RootTAO)
- **Authority**: Issues EAA credentials authorising URV to issue Educational IDs
- **Scope**: National level governance and compliance

#### **🇪🇺 European Blockchain Services Infrastructure (EBSI)**
- **Role**: European-level trust infrastructure
- **Function**: Provide decentralised trust registry and schema validation
- **Governance**: Multi-national consortium ensuring European standards

### 3.4 Supporting Systems

#### **📱 Student GUI (Web Interface)**
- **Role**: User-facing interface for credential requests
- **Location**: `https://uself-verifier-gui.lspurv.urv.cat/`
- **Function**: Generate QR codes and facilitate user interactions

#### **🔗 Mobile Wallet (EUDI Wallet)**
- **Role**: Credential storage and presentation
- **Standards**: W3C Verifiable Credentials, OpenID4VP
- **Features**: Multi-format support, selective disclosure, cross-border compatibility

---

## 4. Technical Architecture Overview

### 4.1 System Architecture Diagram

```mermaid
graph TB
    subgraph "Student Domain"
        Student[👩‍🎓 Maria García]
        Mobile[📱 EUDI Wallet]
    end
    
    subgraph "University Infrastructure (lspurv.urv.cat)"
        GUI[🖥️ Student GUI]
        Agent[🔧 uSelf Issuer Agent]
        AuthSource[📊 Authentic Source<br/>**eIDAS 2.0 Official Role**]
        DB[🗄️ Student Registry DB]
        API[🔗 Standardized APIs<br/>**eIDAS 2.0 Compliant**]
    end
    
    subgraph "EBSI Infrastructure"
        DIDR[🆔 DID Registry]
        TRR[🛡️ Trust Registry] 
        SR[📋 Schema Registry]
        Proxy[🌐 EBSI Proxy]
        PIDAgent[🔐 PID Issuer Agent]
    end
    
    subgraph "Trust Governance"
        Ministry[🏛️ Spanish Ministry]
        EAA[📜 EAA Credentials<br/>**Authentic Source Authority**]
    end

    Student --> Mobile
    Mobile <--> GUI
    GUI <--> Agent
    Agent <--> API
    API <--> AuthSource
    AuthSource <--> DB
    
    Agent <--> DIDR
    Agent <--> TRR
    Agent <--> SR
    Agent <--> Proxy
    Proxy <--> PIDAgent
    
    Ministry --> EAA
    EAA --> TRR
    TRR --> Agent
    
    classDef eidas fill:#e1f5fe,stroke:#01579b,stroke-width:3px
    class AuthSource,API,EAA eidas
```

**Key Architectural Principle**: The university operates in **dual capacity** under eIDAS 2.0:
1. **As Authentic Source**: Authoritative holder of student data (Article 45b compliance)
2. **As Issuer**: Consumer of authentic source data via standardized APIs for credential creation

### 4.2 Trust Flow Architecture

The system implements a sophisticated **multi-layer trust model**:

1. **Foundational Layer**: Spanish national identity infrastructure provides PID
2. **Institutional Layer**: URV's authorisation via Spanish Ministry EAA credentials
3. **European Layer**: EBSI trust registries validate cross-border recognition
4. **Technical Layer**: Cryptographic proofs ensure credential integrity

### 4.3 Protocol Stack

- **Application Layer**: OpenID for Verifiable Credentials (OID4VCI)
- **Credential Layer**: W3C Verifiable Credentials Data Model
- **Trust Layer**: EBSI trust registries and EAA framework
- **Cryptographic Layer**: ES256 signatures, DID-based authentication
- **Transport Layer**: HTTPS with additional security headers

---

## 5. Detailed User Journey Flow

### 5.1 Phase 1: Journey Initiation (Steps 1-6)

#### **Step 1: The Request**
*Monday, 9:15 AM - Maria's dormitory*

Maria opens her web browser and navigates to the URV student portal. The interface is clean and multilingual, supporting both Catalan and Spanish as befitting the region's linguistic diversity.

**Technical Action**: 
```http
GET https://student-web/issue
```

**Behind the Scenes**: The student GUI system initialises, checking server status and preparing the credential issuance infrastructure.

#### **Step 2: Credential Offer Generation**
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

#### **Step 3: QR Code Magic**
*The bridge between digital and physical*

The Student GUI receives the credential offer and transforms it into a QR code—a visual bridge between the web interface and Maria's mobile wallet.

**Technical Implementation**:
```bash
openid-credential-offer://?credential_offer_uri=https://issuer.eu/issuer/offers/719307744250317677
```

The QR code contains not the full credential offer (which would be too large) but a secure URI pointing to the offer details. This follows EBSI recommendations for optimal user experience.

#### **Step 4: Mobile Engagement**
*Maria scans the QR code*

Maria holds up her EUDI Wallet and scans the QR code. The wallet's sophisticated parsing engine recognises the OpenID credential offer format and prepares for the issuance flow.

**User Experience**: The wallet displays a clear, user-friendly interface:
- "Universitat Rovira i Virgili wants to issue your Educational ID"
- "This credential will allow you to access university services and participate in European student mobility"
- "Tap to continue"

#### **Step 5: Protocol Handshake Initiation**
*Behind the scenes coordination*

The mobile wallet processes the QR code and initiates the OpenID4VCI flow, establishing a secure communication channel with the university's systems.

**Technical Flow**:
```http
HTTP 302 Redirect to Authorization Endpoint
```

#### **Step 6: Authorization Request**
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

### 5.2 Phase 2: Foundational Identity Verification - The Mandatory PID Process (Steps 7-22)

**Critical Process Note**: This phase represents the **absolute prerequisite** for EducationalID issuance. Under eIDAS 2.0 regulations and DC4EU framework requirements, **no educational credential can be issued without verified foundational identity**. The PID verification process ensures that Maria's educational credentials are anchored to her legally verified national identity.

#### **Step 7: The Trust Challenge**
*Proving who you are at the foundational level*

The uSelf Issuer Agent responds with a **direct_post** challenge, requesting Maria to present her PID credential. This is not optional—it's a **mandatory step** that forms the foundation of all subsequent trust relationships.

**User Experience**: Maria's wallet displays:
- "⚠️ **Identity Verification Required**: To issue your Educational ID, the university must verify your foundational identity"
- "🆔 **Spanish PID Required**: Please present your Person Identification Data (PID) issued by Spanish authorities"
- "🔒 **Security Notice**: This verification is mandatory under eIDAS 2.0 regulations"
- "ℹ️ This information will be used only for identity verification purposes"

#### **Step 8: Consent and Privacy**
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

#### **Step 9-10: The Digital Handshake**
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

**Maria's PID Credential Structure** (eIDAS 2.0 Compliant - See [Appendix A.1](#a1-eidas-20-pid-schema)):

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

#### **Steps 11-21: The Foundational Trust Verification Symphony**
*EBSI infrastructure validates Maria's foundational identity*

What happens next is invisible to Maria but represents **the most critical trust verification process** in the entire digital credential ecosystem. The uSelf Issuer Agent orchestrates a **comprehensive verification of Maria's foundational identity** across multiple EBSI services:

**Step 11-12: PID DID Resolution**
```http
GET https://ebsi-did-registry/did/{maria-pid-issuer-did}
```
**Purpose**: Resolve the DID of the Spanish authority that issued Maria's PID to verify the cryptographic keys and ensure the PID credential is properly signed by legitimate national authorities.

**Step 13-14: National Authority Trust Registry Verification**
```http
GET https://ebsi-tr-registry/tr
```
**Purpose**: Check the EBSI Trust Registry to verify that the Spanish national identity authorities are officially authorised to issue Person Identification Data credentials under eIDAS 2.0.

**Step 15-16: PID Schema Validation**
```http
GET https://ebsi-schema-registry/schema
```
**Purpose**: Validate that Maria's PID credential conforms to the official European PID schema and data format requirements.

**Step 17-20: Comprehensive PID Verification**
```http
GET https://ebsi-proxy/verify
```
**Purpose**: The EBSI Proxy performs the **complete foundational identity verification**, including:
- ✅ **Cryptographic signature validation** of the PID credential
- ✅ **Revocation status checking** to ensure the PID hasn't been revoked
- ✅ **Trust chain verification** back to Spanish national authorities
- ✅ **eIDAS 2.0 compliance verification** for regulatory alignment
- ✅ **Temporal validity checking** to ensure the PID is currently valid

**Step 21-22: Foundational Identity Verification Success**
The comprehensive verification process completes successfully, **confirming Maria's foundational identity**, and the system issues an authorization code to proceed with Educational ID issuance.

**Verification Result**: The system now has **cryptographic proof** that:
- Maria is who she claims to be (verified by Spanish national authorities)
- Her identity credential is valid and not revoked
- The verification complies with all eIDAS 2.0 requirements
- She is legally authorised to receive educational credentials in Spain

### 5.3 Phase 3: Credential Issuance (Steps 23-33)

#### **Step 23-24: Access Token Exchange**
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

#### **Step 25-26: The Moment of Truth**
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

#### **Step 27-30: Authentic Source Data Retrieval via Standardized APIs**
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
   - **Enrollment Verification**: Current active enrollment status

**Database Query (Internal to Authentic Source)**:
```sql
SELECT s.studentId, s.enrollmentStatus, s.programme, s.level, 
       s.enrollmentDate, s.expectedGraduation, s.institution,
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

**Authentic Source Response** (via standardized API - See [Appendix B.1](#b1-authentic-source-api-response)):

The authentic source provides a comprehensive response that demonstrates successful **identity matching** between Maria's legal identity (PID) and her institutional identity (student record). This response includes both the verified correlation and the educational data needed for EducationalID issuance.

**Critical Identity Matching Results**:
- ✅ **DNI Match**: 12345678A found in student database
- ✅ **Name Match**: García, Maria confirmed in enrollment records  
- ✅ **Birth Date Match**: 2004-03-15 validated against university records
- ✅ **Enrollment Verified**: Active student status confirmed
- ✅ **Credential Authorization**: Student authorized for EducationalID issuance

**Architectural Innovation**: This design demonstrates how eIDAS 2.0 enables institutional **dual roles** while maintaining:
- **Trust boundaries**: Clear separation of functions even within the same organization
- **Identity correlation**: Robust matching between legal and institutional identity
- **Interoperability**: Standardized APIs that work across organizational boundaries
- **Compliance**: Full regulatory alignment with European digital identity frameworks

#### **Step 31: Credential Generation**
*The digital birth certificate*

The agent constructs Maria's Educational ID credential using the **eduGAIN/SCHAC-based schema** (See [Appendix A.2](#a2-educationalid-schema)) rather than ELM. This credential follows the specific EducationalID schema designed for non-foundational identity in educational contexts.

The generated EducationalID credential incorporates:
- **Verified Identity Data**: From the PID verification process
- **Educational Attributes**: Following eduGAIN/SCHAC standards
- **Institutional Affiliation**: URV-specific organizational data
- **Assurance Levels**: REFEDS framework compliance

**Key Schema Features** (detailed in [Appendix A.2](#a2-educationalid-schema)):
- **SCHAC Unique Codes**: For cross-institutional identity resolution
- **eduGAIN Attributes**: Standard educational federation attributes
- **REFEDS Assurance**: Identity assurance framework compliance
- **Multi-value Support**: Arrays for affiliations and assurance levels
  
#### **Step 32: Event Notification**
*System coordination*

The agent sends a `credential_issued` event to the Student GUI, enabling real-time updates to any connected systems and maintaining audit trails for compliance purposes.

#### **Step 33: Delivery to Maria**
*The moment of completion*

The Educational ID credential is delivered to Maria's EUDI Wallet. The wallet validates the credential signature, stores it securely, and notifies Maria of successful issuance.

**User Experience**: Maria sees a success notification:
- "Your Educational ID has been issued successfully!"
- "You can now access university services and participate in international programmes"
- "This credential is valid until June 30, 2027"

---

## 6. Trust Verification Mechanisms

### 6.1 Multi-Layer Trust Architecture with eIDAS 2.0 Compliance

The EducationalID issuance process implements sophisticated **multi-layer trust verification** with full eIDAS 2.0 regulatory alignment, **built upon mandatory foundational identity verification**:

#### **Layer 1: Foundational Identity (PID) - MANDATORY PREREQUISITE**
- **Role**: **Absolute prerequisite** for all educational credentials
- **Source**: Spanish national identity infrastructure
- **Verification**: eIDAS-compliant digital identity (mandatory)
- **Assurance Level**: High (Level of Assurance 3)
- **Cryptographic Standard**: ES256 signatures
- **Legal Basis**: eIDAS 2.0 Article 3 - foundational identity requirement
- **Process**: **Complete EBSI verification of PID before any educational credential issuance**

#### **Layer 2: Authentic Source Authority (eIDAS 2.0 Article 45b)**
- **Role**: URV as certified eIDAS 2.0 Authentic Source
- **Authority**: Spanish Ministry EAA credentials authorizing authentic source function
- **Data Integrity**: Authoritative student records with cryptographic proofs
- **API Standards**: eIDAS 2.0 compliant standardized access protocols
- **Dependency**: **Only operates after Layer 1 (PID) verification is complete**

#### **Layer 3: Institutional Issuance Authority (EAA)**
- **Source**: Spanish Ministry of Universities and Research
- **Mechanism**: Electronic Attestation of Attributes (EAA)
- **Scope**: Authorizes URV to issue Educational IDs based on authentic source data
- **Validation**: EBSI Trust Registry verification
- **Prerequisite**: **Requires verified foundational identity from Layer 1**

#### **Layer 4: European Recognition (EBSI)**
- **Framework**: European Blockchain Services Infrastructure
- **Function**: Cross-border trust propagation
- **Standards**: W3C Verifiable Credentials, eduGAIN/SCHAC
- **Governance**: Multi-national European cooperation
- **Foundation**: **Built upon verified PID from Layer 1**

#### **Layer 5: Technical Integrity**
- **Cryptography**: Multiple signature verification
- **Revocation**: Real-time status checking
- **Audit**: Comprehensive logging and traceability
- **Privacy**: Selective disclosure and data minimization
- **Anchor**: **All technical integrity traces back to verified PID**

### 6.2 Trust Chain Example with eIDAS 2.0 Roles

```
🇪🇺 European Union (eIDAS 2.0 Regulatory Framework)
  ↓
🇪🇸 Spanish Ministry of Universities (Root Trust Anchor)
  ↓ [Issues EAA - Authentic Source Authority]
🏛️ URV as Authentic Source (eIDAS 2.0 Article 45b Role)
  ↓ [Standardized API provides verified data]
🔧 URV as Issuer (EAA-Authorized Credential Issuer)
  ↓ [Issues Educational ID based on authentic source data]
👩‍🎓 Maria García (Credential Holder)
  ↓ [Presents Credential]
🏫 Any European University (Relying Party)
```

**Key Innovation**: The dual role architecture demonstrates how institutions can operate as both **Authentic Source** and **Issuer** under eIDAS 2.0 while maintaining clear functional separation and regulatory compliance.

### 6.3 Security Properties

- **Authenticity**: Cryptographically proven issuer identity
- **Integrity**: Tamper-evident credential structure  
- **Non-repudiation**: Immutable audit trail
- **Privacy**: Minimal data disclosure with consent
- **Availability**: Distributed verification infrastructure
- **Interoperability**: European standards compliance

---

## 7. Technical Message Details

### 7.1 Credential Offer Response (Complete)

The credential offer provides comprehensive metadata about the EducationalID credential, including display parameters and supported credential subject attributes (detailed structure in [Appendix B.2](#b2-credential-offer-response)).

**Key Features**:
- **Credential Type**: `VerifiableEducationalID` with `jwt_vc` format
- **Display Configuration**: URV branding and multilingual support
- **Attribute Mapping**: Complete eduGAIN/SCHAC attribute support
- **Cryptographic Binding**: ES256 algorithm with DID-based binding

### 7.2 Authorization Request (Complete)

The authorization request demonstrates sophisticated presentation definition validation ensuring only valid **eIDAS 2.0 compliant PID credentials** are accepted (complete technical details in [Appendix B.3](#b3-authorization-request)).

**Key Validation Requirements**:
- ✅ **Credential Type**: Must be `PersonIdentificationData` (eIDAS 2.0 PID)
- ✅ **Required Fields**: `family_name`, `given_name`, `birth_date`, `nationality`
- ✅ **Administrative Number**: `personal_administrative_number` for unique identification
- ✅ **Issuing Country**: Must be "ES" (Spain) for this university
- ✅ **Cryptographic Validation**: ES256 signature algorithm required

### 7.3 Final Credential Response

The final credential response delivers the completed EducationalID to Maria's EUDI Wallet in JWT format, cryptographically signed by URV's institutional key (complete response structure in [Appendix B.4](#b4-final-credential-response)).

**Response Components**:
- **JWT-encoded Credential**: Complete EducationalID in W3C VC format
- **Digital Signature**: ES256 signature by URV's DID key
- **EBSI Anchoring**: Schema and trust registry references
- **Expiration Management**: Validity period and renewal information

---

## 8. Implementation Insights

### 8.1 Schema Architecture: eIDAS 2.0 PID vs. eduGAIN EducationalID

**Critical Distinction**: The EducationalID journey demonstrates the **architectural separation** between different credential types in the DC4EU framework:

#### **Foundational Identity (PID) - eIDAS 2.0 Regulation Compliant**
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

#### **Non-Foundational Identity Credentials (EducationalID)**
- **Schema Base**: eduGAIN/SCHAC standards, not ELM
- **Purpose**: Institutional identity and affiliation
- **Standards**: REFEDS, eduGAIN, SCHAC
- **Focus**: "Who you are within an educational context"
- **Key Attributes**: 
  - Educational identity: `eduPersonPrincipalName`, `eduPersonScopedAffiliation`
  - Institutional affiliation: `schacPersonalUniqueCode`, `schacHomeOrganization`
  - Assurance: REFEDS Assurance Framework compliance

#### **Academic Achievement Credentials (ELM-Based)**
- **Schema Base**: European Learning Model (ELM) 3.2
- **Purpose**: Learning outcomes and qualifications
- **Standards**: ELM, EDCI, Europass
- **Focus**: "What you have learned and achieved"
- **Key Attributes**:
  - Learning achievements, qualifications
  - Assessment results, credit systems
  - Quality assurance information

### 8.2 eIDAS 2.0 PID Integration Benefits

The PID's use of **official eIDAS 2.0 standards** provides:

1. **Legal Certainty**: Direct compliance with EU Regulation 2024/2977
2. **Cross-Border Recognition**: Automatic recognition across all EU Member States
3. **High Assurance**: Highest level of identity verification available in EU
4. **Standardized Format**: Common structure across all European identity providers
5. **Privacy Protection**: Built-in selective disclosure capabilities
6. **Administrative Integration**: Direct link to national identity systems

### 8.3 Identity Verification Chain

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

### 8.4 Technical Innovation: Identity Matching Infrastructure

The DC4EU framework's **identity matching infrastructure** represents a critical innovation in European digital identity:

#### **Pre-Deployment Data Preparation**
Before any credential can be issued, institutions must establish:

1. **Comprehensive Data Stores**: Complete population of student databases with verified enrollment information
2. **Identity Correlation Systems**: Cross-reference tables linking national identity numbers (DNI) to institutional records
3. **Validation Algorithms**: Automated matching procedures for PID attributes against educational records
4. **Temporal Synchronization**: Systems to maintain up-to-date correlation between legal and institutional identity

#### **Identity Matching Process**
**The Critical Bridge**: Connecting **legal identity** (Spanish PID) with **institutional identity** (EducationalID)

**Three-Layer Validation**:
- **Primary Key Match**: DNI from PID directly correlates to student database primary key
- **Attribute Verification**: Name and birth date provide multi-factor identity confirmation
- **Enrollment Validation**: Current student status and credential issuance authorization

#### **Technical Architecture Benefits**
- **Separation of Concerns**: Legal identity management vs. institutional identity management
- **Real-time Correlation**: Instant matching between PID and educational records
- **Audit Compliance**: Complete traceability of identity matching decisions
- **Privacy Protection**: Minimum necessary data correlation with selective disclosure
- **Scalability**: Standardized patterns applicable across all European educational institutions

This infrastructure ensures that **every educational credential** is properly anchored to **verified legal identity** while maintaining the flexibility needed for diverse institutional requirements across Europe.

### 8.5 European Digital Sovereignty

This implementation represents **European digital sovereignty** in action:

- **European standards**: W3C VC, EBSI, eIDAS 2.0
- **European infrastructure**: EBSI trust registries and verification
- **European governance**: Member State cooperation and recognition
- **European values**: Privacy, security, and citizen control

---

## Appendix A: Schema Specifications

### A.1 eIDAS 2.0 PID Schema

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
                "enum": ["AF", "AX", "AL", "DZ", "AS", "AD", "AO", "AI", "AQ", "AG", "AR", "AM", "AW", "AU", "AT", "AZ", "BS", "BH", "BD", "BB", "BY", "BE", "BZ", "BJ", "BM", "BT", "BO", "BQ", "BA", "BW", "BV", "BR", "IO", "BN", "BG", "BF", "BI", "CV", "KH", "CM", "CA", "KY", "CF", "TD", "CL", "CN", "CX", "CC", "CO", "KM", "CD", "CG", "CK", "CR", "CI", "HR", "CU", "CW", "CY", "CZ", "DK", "DJ", "DM", "DO", "EC", "EG", "SV", "GQ", "ER", "EE", "SZ", "ET", "FK", "FO", "FJ", "FI", "FR", "GF", "PF", "TF", "GA", "GM", "GE", "DE", "GH", "GI", "GR", "GL", "GD", "GP", "GU", "GT", "GG", "GN", "GW", "GY", "HT", "HM", "VA", "HN", "HK", "HU", "IS", "IN", "ID", "IR", "IQ", "IE", "IM", "IL", "IT", "JM", "JP", "JE", "JO", "KZ", "KE", "KI", "KP", "KR", "KW", "KG", "LA", "LV", "LB", "LS", "LR", "LY", "LI", "LT", "LU", "MO", "MG", "MW", "MY", "MV", "ML", "MT", "MH", "MQ", "MR", "MU", "YT", "MX", "FM", "MD", "MC", "MN", "ME", "MS", "MA", "MZ", "MM", "NA", "NR", "NP", "NL", "NC", "NZ", "NI", "NE", "NG", "NU", "NF", "MK", "MP", "NO", "OM", "PK", "PW", "PS", "PA", "PG", "PY", "PE", "PH", "PN", "PL", "PT", "PR", "QA", "RE", "RO", "RU", "RW", "BL", "SH", "KN", "LC", "MF", "PM", "VC", "WS", "SM", "ST", "SA", "SN", "RS", "SC", "SL", "SG", "SX", "SK", "SI", "SB", "SO", "ZA", "GS", "SS", "ES", "LK", "SD", "SR", "SJ", "SE", "CH", "SY", "TW", "TJ", "TZ", "TH", "TL", "TG", "TK", "TO", "TT", "TN", "TR", "TM", "TC", "TV", "UG", "UA", "AE", "GB", "US", "UM", "UY", "UZ", "VU", "VE", "VN", "VG", "VI", "WF", "EH", "YE", "ZM", "ZW"]
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

### A.2 EducationalID Schema

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
              "description": "Specifies the home organization of the credential subject",
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
              "description": "Primary Affiliation within Home Organization",
              "type": "string"
            },
            "eduPersonAffiliation": {
              "description": "Affiliation within Home Organization. It can contain multiple values such as member, student, employee, faculty, staff, affiliate, alumni, etc.",
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "eduPersonScopedAffiliation": {
              "description": "The person's affiliations within Home Organization scoped with the Home Organization",
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

---

## Appendix B: Technical Reference Materials

### B.1 Authentic Source API Response

Complete API response from URV's authentic source service demonstrating successful **identity matching** between PID and educational records:

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
      "enrollmentStatus": "ACTIVE",
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
    "enrollmentDetails": {
      "institution": "Universitat Rovira i Virgili",
      "institutionCode": "ES-URV-25025",
      "enrollmentDate": "2023-09-15",
      "expectedGraduation": "2027-06-30",
      "credentialIssuanceAuthorized": true,
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

**Key Identity Matching Components**:

1. **Primary Key Correlation**: DNI from PID directly matches student database primary key
2. **Multi-Factor Validation**: Name and birth date provide additional identity confirmation  
3. **Confidence Scoring**: Mathematical confidence levels for each matching element
4. **Audit Trail**: Complete logging of identity matching process for compliance
5. **Institutional Identity Mapping**: Translation from legal identity to educational identity attributes

### B.2 Credential Offer Response

In order to avoid overloading the result of the QR code, the standard defines an entry point based on the `credential_offer_uri` parameter:

```bash
openid-credential-offer://?credential_offer_uri=https://issuer.eu/issuer/offers/719307744250317677
```

The response to resolving the `credential_offer_uri` will vary depending on whether it is a No Authorise flow or a Pre-Authorise flow.

```json
{
   "credential_issuer":"https://issuer.eu/issuer",
   "credentials":[
      {
         "format":"jwt_vc",
         "types":[
            "VerifiableCredential",
            "CertificateProfessionalCompetence"
         ],
         "trust_framework":{
            "name":"uSelf Agent Issuer",
            "type":"CertificateProfessionalCompetence",
            "uri":"CertificateProfessionalCompetence testing"
         },
         "display":[
            {
               "name":"CertificateProfessionalCompetence",
               "description":"Schema defining a verifiable credential that validates whether a registered physician has an up to date certificate of professional competence"
            }
         ],
         "credentialSubject":{
            "id":{
               "display":[
                  {
                     "name":"id"
                  }
               ]
            },
            "personal_administrative_number":{
               "display":[
                  {
                     "name":"personal_administrative_number",
                     "description":"Nationally registered physician number"
                  }
               ]
            },
            "given_name":{
               "display":[
                  {
                     "name":"given_name",
                     "description":"Natural person name"
                  }
               ]
            },
            "family_name":{
               "display":[
                  {
                     "name":"family_name",
                     "description":"Natural person surname"
                  }
               ]
            },
            "is_entitled":{
               "value_type":"boolean",
               "display":[
                  {
                     "name":"is_entitled",
                     "description":"Indicates whether the physician is legally entitled to practice as a doctor."
                  }
               ]
            }
         }
      }
   ]
}
```

## B.3 Token Request

The wallet must obtain an access token to request the credential. In the No Authorise flow, this involves making a token request to the authorisation endpoint.

## B.4 Token Response

The authorisation server responds with an access token that will be used to request the credential:

```json
{
   "access_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6ImRpZDprZXk6ejJkbXpEODFjZ1B4OFZraTdKYnV1TW1GWXJXUGdZb3l0eWtVWjNleXFodDFqOUticzVpc0Uyc0pjWk1oaFpyOUN4UHVBOVBqNXFQNk5uU0pmTVhnS3RQZWdNRG53eXc2ODh3QjJCc1VmazNnSlJBMnFnUWNVRGttVE5wRHJYNjhwRFlzZE1hS3EzV29Tc1JqdGN3WXBzYVh1MkVFVVdFTkZEMTMxZVdYc0VDN3F0cGRrZyJ9...",
   "token_type":"Bearer",
   "expires_in":1741012594331,
   "c_nonce":"8450206689214712010",
   "c_nonce_expires_in":1741012594331
}
```

Key elements in the token response:
- **access_token**: The JWT token used to authenticate subsequent requests
- **token_type**: Indicates the token type (typically "Bearer")
- **expires_in**: Token validity period in seconds
- **c_nonce**: A nonce value used for proof of possession
- **c_nonce_expires_in**: Expiry time for the nonce value

## B.5 Credential Request

Once the access token has been obtained, the end user can request the verifiable credential:

```http
POST /credential
Content-Type: application/json
Authorization: Bearer eyJ0eXAi...

{
   "format":"jwt_vc",
   "types":[
      "VerifiableCredential",
      "CertificateProfessionalCompetence"
   ],
   "proof":{
      "proof_type":"jwt",
      "jwt":"eyJ0eXAiOiJvcGVuaWQ0dmNpLXByb29mK2p3dCIsImtpZCI6ImRpZDprZXk6ejJkbXpEODFjZ1B4OFZraTdKYnV1TW1GWXJXUGdZb3l0eWtVWjNleXFodDFqOUticzVpc0Uyc0pjWk1oaFpyOUN4UHVBOVBqNXFQNk5uU0pmTVhnS3RQZWdNRG53eXc2ODh3QjJCc1VmazNnSlJBMnFnUWNVRGttVE5wRHJYNjhwRFlzZE1hS3EzV29Tc1JqdGN3WXBzYVh1MkVFVVdFTkZEMTMxZVdYc0VDN3F0cGRrZyN6MmRtekQ4MWNnUHg4VmtpN0pidXVNbUZZcldQZ1lveXR5a1VaM2V5cWh0MWo5S2JzNWlzRTJzSmNaTWhoWnI5Q3hQdUE5UGo1cVA2Tm5TSmZNWGdLdFBlZ01Ebnd5dzY4OHdCMkJzVWZrM2dKUkEycWdRY1VEa21UTnBEclg2OHBEWXNkTWFLcTNXb1NzUmp0Y3dZcHNhWHUyRUVVV0VORkQxMzFlV1hzRUM3cXRwZGtnIiwiYWxnIjoiRVMyNTYifQ.eyJpYXQiOjE3NDEwMTE5OTQuMDY3LCJpc3MiOiJkaWQ6a2V5OnoyZG16RDgxY2dQeDhWa2k3SmJ1dU1tRllyV1BnWW95dHlrVVozZXlxaHQxajlLYnM1aXNFMnNKY1pNaGhacjlDeFB1QTlQajVxUDZOblNKZk1YZ0t0UGVnTURud3l3Njg4d0IyQnNVZmszZ0pSQTJxZ1FjVURrbVROcERyWDY4cERZc2RNYUtxM1dvU3NSanRjd1lwc2FYdTJFRVVXRU5GRDEzMWVXWHNFQzdxdHBka2ciLCJhdWQiOiJodHRwczovL3RhZHBvbGUtaW50ZXJuYWwtbWFtbWFsLm5ncm9rLWZyZWUuYXBwL2lzc3VlciIsImV4cCI6MTc0MTAxMjI5NCwibm9uY2UiOiI4NDUwMjA2Njg5MjE0NzEyMDEwIn0.SBGk5rshNgCMO49dNiSAxkMO-LVbP2aUWADFxclTzz8uDNvZAkqGAvKqFJGCyUvzA5u_pSZYnY6nODi6atOC6g"
   }
}
```

The credential request includes:
- **format**: The credential format (jwt_vc for JWT-based Verifiable Credentials)
- **types**: Array of credential types being requested
- **proof**: Proof of possession containing:
  - **proof_type**: Type of proof (typically "jwt")
  - **jwt**: A signed JWT proving the wallet controls the key material

## B.6 Credential Response

Finally, the issuer responds with the requested verifiable credential. The credential is typically returned in JWT format and contains the claims about the credential subject as specified in the credential offer.

The credential response completes the issuance flow, providing the wallet with a signed verifiable credential that can be stored and later presented to verifiers as proof of the attested claims.

## Summary

This document outlines the credential issuance process following the OpenID4VCI (OpenID for Verifiable Credential Issuance) protocol. The process consists of:

1. **Credential Offer**: The issuer provides a credential offer via a URI
2. **Token Exchange**: The wallet obtains an access token for authentication
3. **Credential Request**: Using the access token, the wallet requests the credential with proof of possession
4. **Credential Response**: The issuer returns the signed verifiable credential

This flow ensures secure issuance of verifiable credentials whilst maintaining privacy and preventing replay attacks through the use of nonces and proof of possession mechanisms.