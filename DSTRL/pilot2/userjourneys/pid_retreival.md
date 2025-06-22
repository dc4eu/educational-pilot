# PID Issuance: European Digital Identity Foundation User Journey

## Executive Summary

This document presents the comprehensive narrative for Person Identification Data (PID) issuance within the DC4EU framework, implementing a Pre-Authorised OpenID4VCI flow with **mandatory Member State identity verification**. The journey demonstrates critical foundational identity establishment that enables all subsequent digital credential issuance across European institutions whilst maintaining Member State sovereignty over identity management.

**Critical Context**: PID issuance remains **exclusively within Member State competence** under eIDAS 2.0 framework. However, Work Package 4 has established an agreement to enable **PID datastore provisioning facility as an authentic source** when the related Member State Authority is temporarily unable to provide PIDs directly, ensuring EUDIW operational continuity for Large Scale Pilots.

**Key Innovation**: This implementation showcases the foundational layer of Europe's digital identity ecosystem, establishing verified legal identity that serves as the cornerstone for all subsequent educational, professional, and civic digital credentials across European borders.

**Bottom Line**: María García, a Spanish citizen, successfully obtains her foundational PID credential through the Spanish national identity infrastructure, creating the verified digital identity foundation that will enable her to participate in European educational mobility and access digital services across all Member States.

---

## Document Metadata

- **Version**: 1.0
- **Date**: June 2025
- **Status**: Final
- **Language**: English (UK)
- **Framework**: DC4EU Large Scale Pilots
- **Compliance**: eIDAS 2.0, Member State Identity Regulations
- **Technical Specification**: Based on dc4eu-001-issue-pid-2.md
- **Scope**: Out of scope for Large Scale Pilots (Member State competence)

---

## Table of Contents

1. [Quick Reference Guide](#1-quick-reference-guide)
2. [Governance and Competence Framework](#2-governance-and-competence-framework)
3. [Infrastructure Prerequisites](#3-infrastructure-prerequisites)
4. [The Story: María's Digital Identity Foundation](#4-the-story-marías-digital-identity-foundation)
5. [Actor Ecosystem and Roles](#5-actor-ecosystem-and-roles)
6. [Technical Architecture Overview](#6-technical-architecture-overview)
7. [Detailed User Journey Flow](#7-detailed-user-journey-flow)
8. [Work Package 4 Provisional Solutions](#8-work-package-4-provisional-solutions)
9. [Technical Message Details](#9-technical-message-details)
10. [Implementation Insights](#10-implementation-insights)
11. [Quality Assurance and Testing Framework](#11-quality-assurance-and-testing-framework)
12. [Appendices](#12-appendices)

---

## 1. Quick Reference Guide

### 1.1 Process Overview

1. **Citizen Authentication**: National identity verification through Member State systems
2. **Legal Identity Validation**: Official document verification and biometric confirmation
3. **PID Credential Issuance**: Cryptographically signed foundational identity credential
4. **European Interoperability**: EBSI trust registry integration for cross-border recognition
5. **Fallback Provisioning**: Work Package 4 datastore facility when Member State systems unavailable

### 1.2 Key Actors

- **Citizen**: María García (Spanish national, credential holder)
- **Member State Authority**: Spanish Ministry of Interior (primary issuer)
- **National Identity Provider**: Cl@ve authentication system
- **WP4 Datastore Facility**: Provisional authentic source (when MS unavailable)
- **EBSI Trust Registry**: European-wide validation infrastructure

### 1.3 Technical Flow Summary

Following the **dc4eu-001-issue-pid-2.md** specification:
1. Student initiates PID request via web portal
2. Identity Provider authentication through Spanish Cl@ve system
3. Credential offer generation by uSelf Issuer Agent
4. QR code scanning and mobile wallet engagement
5. Token exchange using Pre-Authorised Code flow
6. Authentic source data retrieval from educational database
7. PID credential generation and secure delivery

### 1.4 Regulatory Framework

- **Primary Competence**: Member State authority under eIDAS 2.0
- **European Standards**: Interoperability through EBSI trust framework
- **Data Protection**: GDPR compliance with national data sovereignty
- **Cross-Border Recognition**: Mutual recognition across all EU Member States

### 1.5 Critical Success Factors

- **Legal Authority**: Only authorised Member State entities can issue PIDs
- **Identity Proofing**: High assurance level identity verification (LoA High)
- **Cryptographic Security**: Strong digital signatures and tamper-evident credentials
- **European Interoperability**: Standards-based approach ensuring cross-border validity

---

## 2. Governance and Competence Framework

### 2.1 Member State Competence Primacy

**Regulatory Foundation**: Under Article 7 of eIDAS 2.0 (EU Regulation 2024/2977), PID issuance remains **exclusively within Member State competence**. No European-level entity, including DC4EU Large Scale Pilots, has authority to issue foundational identity credentials.

**National Sovereignty**: Each Member State maintains complete control over:
- Identity proofing standards and procedures
- Citizen authentication mechanisms
- Legal identity validation processes
- PID credential schemas and issuance workflows
- Data sovereignty and protection measures

### 2.2 Work Package 4 Provisional Agreement

**Operational Necessity**: To ensure EUDIW operational continuity during Large Scale Pilots, Work Package 4 has established a **provisional datastore facility** that can serve as an authentic source for PID provisioning when Member State systems are temporarily unavailable.

**Limited Scope**: This facility operates under strict conditions:
- **Temporary provision only**: When MS authorities cannot provide PIDs directly
- **Authentic source principle**: Facility acts as proxy, not independent issuer
- **MS oversight required**: Member State must authorise and validate the provisional service
- **Full accountability**: All PID issuance remains under Member State legal responsibility

### 2.3 Legal and Technical Boundaries

**Clear Demarcation**: The Large Scale Pilots handle:
- **Educational credentials**: University-issued academic qualifications
- **Professional credentials**: Industry-recognised skill certifications
- **Cross-border verification**: European-wide credential validation services

**Outside LSP Scope**: The Member States retain exclusive authority over:
- **Foundational identity**: Birth certificates, nationality, legal residence
- **Civil status**: Marriage, divorce, family relationships
- **Official documents**: Passports, national ID cards, driving licences

---

## 3. Infrastructure Prerequisites

### 3.1 Member State Identity Infrastructure

#### National Authentication Systems

Each Member State must provide robust identity verification infrastructure:

**Spain (Example Implementation)**:
- **Cl@ve System**: Centralised citizen authentication platform
- **DNI Integration**: National identity card with cryptographic capabilities
- **Certificate Authority**: National PKI for digital signatures
- **Biometric Verification**: Fingerprint and facial recognition systems

#### Legal Document Validation

- **Official Document Registry**: Real-time validation of identity documents
- **Anti-Fraud Mechanisms**: Document authenticity verification systems
- **Cross-Reference Databases**: Population registry and civil status integration
- **Historical Validation**: Previous identity changes and legal name modifications

### 3.2 European Interoperability Layer

#### EBSI Trust Registry Integration

- **Member State Registration**: National authorities registered as trusted issuers
- **Schema Standardisation**: Common PID data model across all Member States
- **Cryptographic Standards**: Harmonised signature algorithms and key management
- **Cross-Border Validation**: Real-time verification of foreign PIDs

#### Technical Standards Compliance

- **eIDAS 2.0 Technical Specifications**: ARF requirements implementation
- **OpenID4VCI Protocol**: Standardised credential issuance workflows
- **W3C Verifiable Credentials**: Interoperable credential format
- **EBSI Trust Framework**: European trust infrastructure integration

### 3.3 Technical Infrastructure Requirements

#### uSelf Agent Components

Based on the **dc4eu-001-issue-pid-2.md** specification:
- **uSelf PID Generator**: Web portal for student interaction
- **uSelf Issuer Agent**: Core credential issuance engine
- **Authentic Source**: Educational database integration
- **PostgreSQL Database**: Secure storage of verified citizen data
- **Identity Provider**: Spanish Cl@ve system integration

#### Security and Performance Requirements

- **High Availability**: 99.9% uptime with redundant systems
- **Scalability**: Support for 10,000 concurrent PID requests
- **Response Time**: Maximum 30 seconds for complete issuance flow
- **Security Level**: eIDAS High assurance level compliance
- **Audit Logging**: Complete transaction trails for regulatory compliance

---

## 4. The Story: María's Digital Identity Foundation

### 4.1 Setting the Scene

**Location**: Tarragona, Spain  
**Date**: Monday, 3rd June 2025, 10:30 AM  
**Context**: María García, 21, needs to establish her foundational digital identity to participate in European educational mobility programmes

María sits in her university dormitory, knowing that before she can access any European digital services or apply for study abroad programmes, she needs her foundational digital identity credential—her PID. This isn't just another university credential; it's the legal foundation that proves who she is according to Spanish law and enables her participation in the broader European digital ecosystem.

### 4.2 The Digital Identity Imperative

**Why PIDs Matter**: In the emerging European digital economy, PID credentials serve as the foundational layer for all other digital interactions. Without a verified PID, María cannot:
- Apply for educational credentials from any European university
- Access cross-border professional qualification recognition
- Participate in European student mobility programmes
- Use European digital public services whilst travelling

**The Legal Framework**: Her PID will be issued through the uSelf system architecture, which interfaces with Spanish authorities to ensure it carries the full legal weight of Spanish sovereignty whilst being recognised across all EU Member States through the EBSI trust framework.

### 4.3 Technical Context

**Implementation Framework**: María's PID issuance follows the exact technical specification outlined in **dc4eu-001-issue-pid-2.md**, implementing a Pre-Authorised OpenID4VCI flow that ensures security, privacy, and regulatory compliance whilst maintaining seamless user experience.

---

## 5. Actor Ecosystem and Roles

### 5.1 Primary Actors

#### María García (Student/Holder)
- **Role**: Spanish citizen requesting foundational digital identity
- **Responsibilities**: Provide authentic identity documentation, complete verification procedures
- **Technical Requirements**: EUDI Wallet app, valid Spanish identity documentation
- **Legal Status**: Spanish national with full civil rights

#### Spanish Ministry of Interior (Ultimate Authority)
- **Role**: Authoritative legal foundation for Spanish PID issuance
- **Responsibilities**: Legal validation framework, regulatory oversight
- **Technical Integration**: Via Cl@ve authentication system
- **Legal Authority**: Exclusive competence under Spanish law and eIDAS 2.0

#### Identity Provider (Cl@ve Authentication System)
- **Role**: Spanish national citizen authentication platform
- **Responsibilities**: Secure citizen login, multi-factor authentication, session management
- **Technical Integration**: DNI card readers, biometric systems, SMS verification
- **Security Level**: eIDAS High assurance level authentication

### 5.2 Technical Infrastructure Actors

#### uSelf PID Generator
- **Role**: Student-facing web portal for PID request initiation
- **Technical Function**: User interface, QR code generation, session management
- **Integration**: Direct connection to uSelf Issuer Agent
- **User Experience**: Simplified, secure credential request workflow

#### uSelf Issuer Agent
- **Role**: Core credential issuance engine implementing OpenID4VCI
- **Technical Function**: Token management, credential generation, cryptographic signing
- **Security Features**: Pre-authorised code flow, JWT credential format
- **Integration**: Authentic Source data retrieval, mobile wallet delivery

#### Authentic Source
- **Role**: Verified educational database containing citizen identity information
- **Technical Function**: Secure data retrieval, identity correlation
- **Database Integration**: PostgreSQL backend with encrypted storage
- **Data Quality**: High-assurance citizen data validated during university enrolment

#### Mobile Wallet (EUDI Wallet)
- **Role**: Citizen's personal credential storage and management
- **Technical Function**: QR code scanning, secure credential reception and storage
- **Security Features**: DID-based authentication, encrypted local storage
- **User Control**: Full citizen control over credential sharing and presentation

### 5.3 Supporting Infrastructure

#### Work Package 4 Datastore Facility (Provisional Authentic Source)
- **Role**: Backup PID provisioning when Member State systems unavailable
- **Operational Scope**: Temporary service provision under Member State authority
- **Technical Function**: Proxy credential issuance with full MS accountability
- **Legal Framework**: Operating under Spanish Ministry delegation agreement

#### EBSI Trust Registry (Validation Infrastructure)
- **Role**: European-wide credential validation and trust establishment
- **Responsibilities**: Cross-border issuer verification, schema validation, trust pathways
- **Technical Function**: Distributed ledger for trust anchors and validation rules
- **Governance**: Multi-Member State consensus with national sovereignty protection

---

## 6. Technical Architecture Overview

### 6.1 System Architecture (Based on dc4eu-001-issue-pid-2.md)

#### Core Components Integration

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Student       │    │ Mobile Wallet    │    │ uSelf PID       │
│   (María)       │◄──►│ (EUDI Wallet)    │◄──►│ Generator       │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                                        │
                                                        ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Identity        │◄──►│ uSelf Issuer     │◄──►│ Authentic       │
│ Provider        │    │ Agent            │    │ Source          │
│ (Cl@ve)         │    │                  │    │                 │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                                        │
                                                        ▼
                                                ┌─────────────────┐
                                                │ PostgreSQL      │
                                                │ Database        │
                                                └─────────────────┘
```

### 6.2 Protocol Stack

- **Application Layer**: OpenID4VCI with Pre-Authorised Code flow
- **Credential Layer**: W3C Verifiable Credentials with JWT encoding
- **Trust Layer**: EBSI trust registries and Member State PKI
- **Authentication Layer**: Spanish Cl@ve system integration
- **Transport Layer**: HTTPS with additional security headers and endpoint protection
- **Database Layer**: Encrypted PostgreSQL with audit logging

### 6.3 Security Architecture

#### Multi-Layer Security Model

1. **National Authentication**: Spanish Cl@ve system (eIDAS High)
2. **Pre-Authorised Flow**: OAuth2-based secure token exchange
3. **User PIN Verification**: Additional authentication factor
4. **Cryptographic Proofs**: DID-based wallet authentication
5. **Database Security**: Encrypted storage with access controls
6. **Audit Trails**: Complete transaction logging for compliance

#### Trust Establishment

- **Member State PKI**: Spanish national certificate authority
- **EBSI Integration**: European trust registry validation
- **Cross-Border Recognition**: Standardised trust pathways
- **Revocation Management**: Coordinated credential lifecycle control

---

## 7. Detailed User Journey Flow

### 7.1 Phase 1: Pre-Authentication and Authorisation (Steps 1-3)

#### Step 1: Student Initiates PID Request
*Monday, 10:30 AM - María's dormitory*

María navigates to the student web portal to begin her PID issuance process. This follows the exact sequence from the dc4eu-001-issue-pid-2.md technical specification.

**Technical Action**: 
```http
GET http://student-web/issue
```

**Behind the Scenes**: The uSelf PID Generator system activates, preparing to coordinate the PID issuance workflow with Spanish national infrastructure.

**User Experience**: María sees a clean, professional interface explaining the PID issuance process and the importance of foundational digital identity for European mobility.

#### Step 2: Identity Provider Authentication Redirect
*System routes to Spanish national authentication*

The PID Generator automatically redirects María to the Spanish Identity Provider (Cl@ve system) for high-assurance authentication, maintaining Member State competence over identity verification.

**Technical Exchange**:
```http
GET http://identity-provider/authorize
```

**Regulatory Compliance**: This redirect ensures that only Spanish authorities handle María's foundational identity verification, preserving national sovereignty over PID issuance.

**Security Features**: The redirect includes state parameters to prevent CSRF attacks and maintain session integrity throughout the authentication process.

#### Step 3: Student Authentication Completion
*Cl@ve system validates María's identity*

María completes the Spanish national authentication process using her DNI card and PIN, achieving eIDAS High level of assurance required for PID credentials.

**Authentication Response**:
```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "status": "student authenticated",
  "assurance_level": "HIGH",
  "citizen_id": "12345678A",
  "verification_methods": ["dni_card", "pin_verification"],
  "authentication_timestamp": "2025-06-03T10:35:00Z"
}
```

**Security Level**: This achieves the highest assurance level required for foundational identity credentials under Spanish law and eIDAS 2.0 regulations.

### 7.2 Phase 2: PID Credential Issuance (Steps 4-7)

#### Step 4: Credential Offer Generation
*uSelf Issuer Agent prepares credential offer*

Following successful authentication, the uSelf Issuer Agent generates a credential offer specifically for PID issuance, implementing the Pre-Authorised Code flow as specified in the technical documentation.

**Technical Exchange**:
```http
GET http://uself-agent/issuer/credential-offer
```

**Credential Offer Response**:
```json
{
  "credential_issuer": "https://uself-agent/issuer",
  "credentials_supported": [
    {
      "format": "jwt_vc",
      "scope": "eu.europa.ec.eudi.pid",
      "cryptographic_binding_methods_supported": ["did:key"],
      "credential_signing_alg_values_supported": ["ES256"],
      "credential_definition": {
        "type": ["VerifiableCredential", "eu.europa.ec.eudi.pid"],
        "credentialSubject": {
          "given_name": {
            "mandatory": false,
            "display": [{"name": "given_name", "locale": "en-GB"}]
          },
          "family_name": {
            "mandatory": false,
            "display": [{"name": "family_name", "locale": "en-GB"}]
          },
          "birth_date": {
            "mandatory": false,
            "display": [{"name": "birth_date", "locale": "en-GB"}]
          },
          "document_number": {
            "mandatory": false,
            "display": [{"name": "document_number", "locale": "en-GB"}]
          },
          "age_over_18": {
            "mandatory": false,
            "display": [{"name": "age_over_18", "locale": "en-GB"}]
          }
        }
      }
    }
  ],
  "grants": {
    "urn:ietf:params:oauth:grant-type:pre-authorized_code": {
      "pre-authorized_code": "eyJraWQiOiJkaWQ6ZWJzaTp6dFJvWXlKTmRHcjh0bUF0Vmg5Y2c5biIs...",
      "user_pin_required": true
    }
  }
}
```

#### Step 5: QR Code Generation and Display
*Visual bridge for mobile wallet interaction*

The PID Generator creates a QR code containing the credential offer URI, enabling María to connect her mobile wallet to the issuance process.

**Technical Implementation**:
```bash
# Generate QR code with credential offer
generate_qr_code(credential_offer_uri)
```

**QR Code Content**:
```
openid-credential-offer://?credential_offer_uri=https://uself-agent/issuer/offers/719307744250317677
```

**User Experience**: María sees clear instructions to scan the QR code with her EUDI Wallet, along with security information about the credential she's about to receive.

#### Step 6: Mobile Wallet Engagement
*María scans QR code with EUDI Wallet*

María uses her EUDI Wallet to scan the QR code, which initiates the credential issuance flow on her mobile device. The wallet prompts her for the user PIN.

**User Experience**:
- Wallet displays: "Scan QR code to receive your PID credential"
- María scans the code and enters her user PIN (1234)
- Wallet prepares for secure credential reception

**Technical Process**:
```http
# Mobile wallet reads QR code and extracts offer
read_qr_code() -> credential_offer_uri
user_input() -> user_pin
```

#### Step 7: HTTP Redirect and Token Request
*Secure token exchange initiation*

The mobile wallet processes the credential offer and initiates the token request using the pre-authorised code flow, including the user PIN for additional security.

**Technical Sequence**:
```http
# Mobile wallet redirect (HTTP 302)
HTTP/1.1 302 Found
Location: http://uself-agent/auth/token?user_pin=1234

# Token request
GET http://uself-agent/auth/token?user_pin=1234
Authorization: Bearer <pre_authorized_code>
```

### 7.3 Phase 3: Credential Generation and Delivery (Steps 8-12)

#### Step 8: Access Token Response
*Secure token provisioning*

The uSelf Issuer Agent validates the user PIN and pre-authorised code, then responds with an access token that authorises the credential request.

**Token Response**:
```json
{
  "access_token": "eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJodHRwczovL3VzZWxmLWFnZW50L2F1dGgiLCJzdWIiOiIiLCJhdXRob3JpemF0aW9uX2RldGFpbHMiOnsicGlkX2lkZW50aWZpZXIiOiIxMjM0NTY3OEEiLCJ2ZXJpZmljYXRpb25fc3RhdHVzIjoiQ09NUExFVEUifSwiZXhwIjoxNzM4NTgwNjEyLCJpYXQiOjE3Mzg1NzcwMTJ9...",
  "token_type": "Bearer",
  "expires_in": 3600,
  "c_nonce": "8450206689214712015",
  "c_nonce_expires_in": 86400
}
```

**Security Features**:
- **Time-limited token**: 1-hour expiration for security
- **Cryptographic nonce**: Prevents replay attacks
- **Bearer authorisation**: Standard OAuth 2.0 token format

#### Step 9: Credential Request Submission
*Mobile wallet requests PID credential*

Using the access token, María's mobile wallet submits a formal credential request to the uSelf Issuer Agent, specifying the desired PID format and her wallet's DID.

**Credential Request**:
```http
POST http://uself-agent/issuer/credential
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9...
Content-Type: application/json

{
  "format": "jwt_vc",
  "credential_definition": {
    "type": ["VerifiableCredential", "eu.europa.ec.eudi.pid"]
  },
  "proof": {
    "proof_type": "jwt",
    "jwt": "<wallet_did_proof_jwt>"
  }
}
```

#### Step 10: Authentic Source Data Retrieval
*System queries educational database for PID information*

The uSelf Issuer Agent contacts the Authentic Source to retrieve the citizen's verified identity information from the educational system's database, using the authenticated PID identifier.

**Database Query**:
```http
GET http://auth-source/educationalId/12345678A
Authorization: Bearer <system_access_token>
```

**Database Operation**:
```sql
SELECT * FROM educationalId 
WHERE pid = '12345678A'
AND status = 'ACTIVE'
AND verification_level = 'HIGH'
```

**Retrieved Information**:
```json
{
  "pid_identifier": "12345678A",
  "given_name": "María",
  "family_name": "García López",
  "birth_date": "2004-03-15",
  "nationality": "ES",
  "document_number": "12345678A",
  "verified_status": "ACTIVE",
  "last_verified": "2025-06-03T10:30:00Z"
}
```

#### Step 11: Educational Identity Information Response
*Authentic Source provides verified citizen data*

The Authentic Source responds with María's verified educational identity information, which has been cross-referenced with Spanish national databases during her university enrolment process.

**Data Response**:
```json
{
  "status": "SUCCESS",
  "citizen_data": {
    "personal_identifier": "ES-DNI-12345678A",
    "given_name": "María",
    "family_name": "García López",
    "birth_date": "2004-03-15",
    "nationality": "ES",
    "verification_level": "HIGH",
    "last_verified": "2025-06-03T10:30:00Z",
    "issuing_authority": "Spanish Educational System"
  }
}
```

#### Step 12: Credential Issuance and Event Notification
*Final credential generation and delivery*

The uSelf Issuer Agent generates the signed PID credential using the retrieved authentic data and delivers it to María's mobile wallet. The system also sends a credential issuance event for audit purposes.

**Credential Generation**:
```json
{
  "@context": [
    "https://www.w3.org/2018/credentials/v1",
    "https://ebsi.eu/schemas/pid/v1.0"
  ],
  "type": ["VerifiableCredential", "eu.europa.ec.eudi.pid"],
  "issuer": "did:ebsi:uself-issuer-agent",
  "issuanceDate": "2025-06-03T10:45:23Z",
  "credentialSubject": {
    "id": "did:key:z2dmzD81cgPx8Vki7JbuuMmFYrWPgYoytyKUZ3eyqht1j9Kbh4",
    "given_name": "María",
    "family_name": "García López",
    "birth_date": "2004-03-15",
    "document_number": "12345678A",
    "age_over_18": true
  },
  "proof": {
    "type": "JsonWebSignature2020",
    "created": "2025-06-03T10:45:23Z",
    "verificationMethod": "did:ebsi:uself-issuer-agent#keys-1",
    "jws": "eyJhbGciOiJFUzI1NiIsImI2NCI6ZmFsc2UsImNyaXQiOlsiYjY0Il19..."
  }
}
```

**Event Notification**:
```json
{
  "event_type": "credential_issued",
  "timestamp": "2025-06-03T10:45:23Z",
  "credential_type": "PID",
  "recipient_did": "did:key:z2dmzD81cgPx8Vki7JbuuMmFYrWPgYoytyKUZ3eyqht1j9Kbh4",
  "issuer": "did:ebsi:uself-issuer-agent",
  "transaction_id": "pid_issuance_20250603_001"
}
```

**Final Delivery**: María's EUDI Wallet receives the completed PID credential, validates its cryptographic signature, and securely stores it for future use in educational and cross-border scenarios.

---

## 8. Work Package 4 Provisional Solutions

### 8.1 Datastore Facility Implementation

**Operational Scenario**: When Spanish Ministry systems are temporarily unavailable due to maintenance, technical issues, or high demand, the Work Package 4 datastore facility can provide provisional PID services.

#### Activation Conditions

**Technical Unavailability**:
- Spanish national systems experiencing extended downtime
- Network connectivity issues preventing citizen authentication
- Scheduled maintenance periods during critical pilot operations
- Overwhelming demand exceeding national infrastructure capacity

**Legal Framework**:
```json
{
  "facility_activation": {
    "authorising_member_state": "ES",
    "delegation_agreement": "WP4-ES-2025-001",
    "operational_authority": "Spanish Ministry of Interior",
    "legal_responsibility": "Remains with Spanish State",
    "duration": "Temporary - until MS systems restored",
    "oversight": "Continuous MS monitoring required"
  }
}
```

#### Provisional Issuance Process

**Modified Technical Flow**: When María attempts to obtain her PID and Spanish systems are unavailable:

1. **Automatic Detection**: System detects Spanish infrastructure unavailability
2. **Facility Routing**: Request automatically routed to WP4 datastore facility
3. **Enhanced Authentication**: Additional verification steps using alternative methods
4. **Spanish Authority Proxy**: Facility contacts available Spanish validation services
5. **Provisional Credential**: PID issued with temporary status pending full validation
6. **Enhanced Monitoring**: Continuous oversight and audit trail generation
7. **Status Upgrade**: Credential converted to standard status when Spanish systems resume

#### Technical Implementation

**Facility Architecture**:
```bash
# WP4 Datastore Facility Components
- Spanish_Auth_Proxy: Maintains connection to available Spanish services
- Identity_Verification: Enhanced KYC procedures for provisional issuance  
- Credential_Generator: Spanish-compliant PID generation
- Audit_System: Complete logging for Spanish authorities
- Monitoring_Dashboard: Real-time oversight for Spanish Ministry
```

**Enhanced Security Measures**:
- **Dual Verification**: Multiple independent validation paths
- **Audit Trail**: Complete transaction logging for Spanish review
- **Temporary Marking**: Clear indication of provisional status
- **Automatic Upgrade**: Conversion to standard PID when Spanish systems resume

### 8.2 Fallback Procedures and Quality Assurance

#### Emergency Protocols

**Immediate Response**:
```json
{
  "emergency_activation": {
    "trigger_conditions": ["spanish_system_failure", "critical_pilot_operation"],
    "notification_requirement": "Immediate Spanish Ministry notification",
    "approval_timeout": "4 hours maximum",
    "operational_constraints": "Enhanced verification mandatory",
    "reporting_frequency": "Every 2 hours during operation"
  }
}
```

**Quality Assurance**:
- **Spanish Oversight**: Continuous monitoring by Spanish authorities
- **Enhanced Verification**: Additional identity checks beyond standard requirements  
- **Limited Duration**: Maximum 72-hour provisional status before Spanish validation
- **Audit Requirements**: Complete transaction records for Spanish review
- **Legal Compliance**: Full adherence to Spanish identity verification standards

---

## 9. Technical Message Details

### 9.1 Complete Message Flow (Following dc4eu-001-issue-pid-2.md Specification)

#### 9.1.1 Initiate Credential Offer

**Request**:
```http
GET http://student-web/issue
User-Agent: Mozilla/5.0 (compatible; EUDI-Wallet/2.1.0)
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-GB,en;q=0.5
Host: student-web
```

**Response**: HTML page with QR code and credential offer initiation interface.

#### 9.1.2 Credential Offer Response

**Generated Credential Offer**:
```json
{
  "credential_issuer": "https://uself-agent/issuer",
  "credentials_supported": [
    {
      "format": "jwt_vc",
      "scope": "eu.europa.ec.eudi.pid",
      "cryptographic_binding_methods_supported": ["did:key"],
      "credential_signing_alg_values_supported": ["ES256"],
      "credential_definition": {
        "type": ["VerifiableCredential", "eu.europa.ec.eudi.pid"],
        "credentialSubject": {
          "given_name": {
            "mandatory": false,
            "display": [{"name": "given_name", "locale": "en-GB"}]
          },
          "family_name": {
            "mandatory": false,
            "display": [{"name": "family_name", "locale": "en-GB"}]
          },
          "birth_date": {
            "mandatory": false,
            "display": [{"name": "birth_date", "locale": "en-GB"}]
          },
          "document_number": {
            "mandatory": false,
            "display": [{"name": "document_number", "locale": "en-GB"}]
          },
          "age_over_18": {
            "mandatory": false,
            "display": [{"name": "age_over_18", "locale": "en-GB"}]
          }
        }
      }
    }
  ],
  "grants": {
    "urn:ietf:params:oauth:grant-type:pre-authorized_code": {
      "pre-authorized_code": "eyJraWQiOiJkaWQ6ZWJzaTp6dFJvWXlKTmRHcjh0bUF0Vmg5Y2c5biIsInR5cCI6IkpXVCIsImFsZyI6IkVTMjU2In0.eyJhdWQiOiJodHRwczovL3VzZWxmLWFnZW50L2F1dGgiLCJzdWIiOiIiLCJhdXRob3JpemF0aW9uX2RldGFpbHMiOnsicGlkX2lkZW50aWZpZXIiOiIxMjM0NTY3OEEiLCJ2ZXJpZmljYXRpb25fc3RhdHVzIjoiQ09NUExFVEUifSwiZXhwIjoxNzM4NTgwNjEyLCJpYXQiOjE3Mzg1NzcwMTJ9...",
      "user_pin_required": true
    }
  }
}
```

#### 9.1.3 Token Request

**Request**:
```http
POST https://uself-agent/token
Content-Type: application/x-www-form-urlencoded

grant_type=urn:ietf:params:oauth:grant-type:pre-authorized_code&
redirect_uri=https://wallet.eudi.eu&
pre_authorized_code=eyJraWQiOiJkaWQ6ZWJzaTp6dFJvWXlKTmRHcjh0bUF0Vmg5Y2c5biIsInR5cCI6IkpXVCIsImFsZyI6IkVTMjU2In0.eyJhdWQiOiJodHRwczovL3VzZWxmLWFnZW50L2F1dGgiLCJzdWIiOiIiLCJhdXRob3JpemF0aW9uX2RldGFpbHMiOnsicGlkX2lkZW50aWZpZXIiOiIxMjM0NTY3OEEiLCJ2ZXJpZmljYXRpb25fc3RhdHVzIjoiQ09NUExFVEUifSwiZXhwIjoxNzM4NTgwNjEyLCJpYXQiOjE3Mzg1NzcwMTJ9...&
user_pin=1234
```

#### 9.1.4 Token Response

**Response**:
```json
{
  "access_token": "eyJraWQiOiJkaWQ6ZWJzaTp6dFJvWXlKTmRHcjh0bUF0Vmg5Y2c5biIsInR5cCI6IkpXVCIsImFsZyI6IkVTMjU2In0.eyJhdWQiOiJodHRwczovL3VzZWxmLWFnZW50L2F1dGgiLCJzdWIiOiIiLCJhdXRob3JpemF0aW9uX2RldGFpbHMiOnsicGlkX2lkZW50aWZpZXIiOiIxMjM0NTY3OEEiLCJ2ZXJpZmljYXRpb25fc3RhdHVzIjoiQ09NUExFVEUifSwiaXNzIjoiaHR0cHM6Ly91c2VsZi1hZ2VudC9pc3N1ZXIiLCJleHAiOjE3Mzg1ODA2MTIsImlhdCI6MTczODU3NzAxMiwibm9uY2UiOiI3NDU0MjgxNDU2ODg4NjQ2NTM1IiwiY2xpZW50X2lkIjoiIn0.qXeHCeAnGRTaCBL0hj2D4EITZVeuhNBgFrr5pz2ZJHhy4O01tQ8x7lyBrkRon3gQb0rFgjzBgn5WPn3_eu5OmQ",
  "token_type": "Bearer",
  "expires_in": 3600,
  "c_nonce": "8450206689214712015",
  "c_nonce_expires_in": 86400
}
```

#### 9.1.5 Credential Request

**Request**:
```http
POST https://uself-agent/issuer/credential
Authorization: Bearer eyJraWQiOiJkaWQ6ZWJzaTp6dFJvWXlKTmRHcjh0bUF0Vmg5Y2c5biIs...
Content-Type: application/json

{
  "format": "jwt_vc",
  "credential_definition": {
    "type": ["VerifiableCredential", "eu.europa.ec.eudi.pid"]
  },
  "proof": {
    "proof_type": "jwt",
    "jwt": "eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImRpZDprZXk6ejJkbXpEODFjZ1B4OFZraTdKYnV1TW1GWXJXUGdZb3l0eWtVWjNleXFodDFqOUtiaGRpNEZ6RTdicTlpclBHUVZ5Wkc3U1dIeThpcXBLTWpqaG10QjdKRjNlRllhRzY3U3hOZDRnalQzRHNLVWI3TktlS0xjTlRFb2NZVWY2a3BCUVJRcUN2R01DdkM4N0Y4amd5ZFNoRkNQVHdyRHB2SktyWk1kcTh6alFMUXh3VzJrTCJ9.eyJub25jZSI6Ijg0NTAyMDY2ODkyMTQ3MTIwMTUiLCJhdWQiOiJodHRwczovL3VzZWxmLWFnZW50L2lzc3VlciIsImlzcyI6ImRpZDprZXk6ejJkbXpEODFjZ1B4OFZraTdKYnV1TW1GWXJXUGdZb3l0eWtVWjNleXFodDFqOUtiaGRpNEZ6RTdicTlpclBHUVZ5Wkc3U1dIeThpcXBLTWpqaG10QjdKRjNlRlluTTY3U3hOZDRnalQzRHNLVWI3TktlS0xjTlRFb2NZVWY2a3BCUVJRcUN2R01DdkM4N0Y4amd5ZFNoRkNQVHdyRHB2SktyWk1kcTh6alFMUXh3VzJrTCIsImlhdCI6MTczODU3NzAxMn0.BjH8_GqN9cTM8hf0XyJK4UR3jN8_P4xGqMc7dYwZL9uRk6-U8sQ2vN3_LmBdCf7K8YxJ9hNpA4rS6fGqM8vC_w"
  }
}
```

#### 9.1.6 Credential Response

**Response**:
```json
{
  "credential": "eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImRpZDplYnNpOnVzZWxmLWlzc3Vlci1hZ2VudCNrZXlzLTEifQ.eyJpc3MiOiJkaWQ6ZWJzaTp1c2VsZi1pc3N1ZXItYWdlbnQiLCJzdWIiOiJkaWQ6a2V5OnoyZG16RDgxY2dQeDhWa2k3SmJ1dU1tRllyV1BnWW95dHlrVVozZXlxaHQxajlLYmhkaTRGekU3YnE5aXJQR1FWeVpHN1NXSHk4aXFwS01qamhtdEI3SkYzZUZZbk02N1N4TmQ0Z2pUM0RzS1ViN05LZUtMY05URW9jWVVmNmtwQlFSUXFDdkdNQ3ZDODdGOGpneWRTaEZDUFR3ckRwdkpLclpNZHE4empRTFF4d1cya0wiLCJuYmYiOjE3Mzg1NzcwMjcsImlzcyI6ImRpZDplYnNpOnVzZWxmLWlzc3Vlci1hZ2VudCIsImV4cCI6MTc3MDExMzAyNywidmMiOnsiQGNvbnRleHQiOlsiaHR0cHM6Ly93d3cudzMub3JnLzIwMTgvY3JlZGVudGlhbHMvdjEiXSwidHlwZSI6WyJWZXJpZmlhYmxlQ3JlZGVudGlhbCIsImV1LmV1cm9wYS5lYy5ldWRpLnBpZCJdLCJjcmVkZW50aWFsU3ViamVjdCI6eyJpZCI6ImRpZDprZXk6ejJkbXpEODFjZ1B4OFZraTdKYnV1TW1GWXJXUGdZb3l0eWtVWjNleXFodDFqOUtiaGRpNEZ6RTdicTlpclBHUVZ5Wkc3U1dIeThpcXBLTWpqaG10QjdKRjNlRlluTTY3U3hOZDRnalQzRHNLVWI3TktlS0xjTlRFb2NZVWY2a3BCUVJRcUN2R01DdkM4N0Y4amd5ZFNoRkNQVHdyRHB2SktyWk1kcTh6alFMUXh3VzJrTCIsImdpdmVuX25hbWUiOiJNYXLDrWEiLCJmYW1pbHlfbmFtZSI6IkdhcmPDrWEgTMOzcGV6IiwiYmlydGhfZGF0ZSI6IjIwMDQtMDMtMTUiLCJkb2N1bWVudF9udW1iZXIiOiIxMjM0NTY3OEEiLCJhZ2Vfb3Zlcl8xOCI6dHJ1ZX19LCJzdWIiOiJkaWQ6a2V5OnoyZG16RDgxY2dQeDhWa2k3SmJ1dU1tRllyV1BnWW95dHlrVVozZXlxaHQxajlLYmhkaTRGekU3YnE5aXJQR1FWeVpHN1NXSHk4aXFwS01qamhtdEI3SkYzZUZZbk02N1N4TmQ0Z2pUM0RzS1ViN05LZUtMY05URW9jWVVmNmtwQlFSUXFDdkdNQ3ZDODdGOGpneWRTaEZDUFR3ckRwdkpLclpNZHE4empRTFF4d1cya0w",
  "c_nonce": "8450206689214712015",
  "c_nonce_expires_in": 86400
}
```

**JWT Credential Decoded Structure**:
```json
{
  "header": {
    "alg": "ES256",
    "typ": "JWT",
    "kid": "did:ebsi:uself-issuer-agent#keys-1"
  },
  "payload": {
    "iss": "did:ebsi:uself-issuer-agent",
    "sub": "did:key:z2dmzD81cgPx8Vki7JbuuMmFYrWPgYoytyKUZ3eyqht1j9Kbh4",
    "nbf": 1738577027,
    "exp": 1770113027,
    "vc": {
      "@context": ["https://www.w3.org/2018/credentials/v1"],
      "type": ["VerifiableCredential", "eu.europa.ec.eudi.pid"],
      "credentialSubject": {
        "id": "did:key:z2dmzD81cgPx8Vki7JbuuMmFYrWPgYoytyKUZ3eyqht1j9Kbh4",
        "given_name": "María",
        "family_name": "García López",
        "birth_date": "2004-03-15",
        "document_number": "12345678A",
        "age_over_18": true
      }
    }
  }
}
```

### 9.2 Sequence Diagram Implementation

The complete technical flow matches the sequence diagram from dc4eu-001-issue-pid-2.md:

```mermaid
sequenceDiagram
    autonumber
    actor student as Student
    participant mobile as Mobile Wallet
    participant pidGUI as uSelf PID Generator
    participant agent as uSelf Issuer Agent
    participant authSource as Authentic Source
    participant db as Postgres DB
    participant ip as Identity Provider
    

Note over student,ip: Pre Authentication/Authorization
    student->>pidGUI: GET http://student-web/issue
    activate pidGUI 
    pidGUI->>ip: GET http://identity-provider/authorize
    activate ip 
    ip-->>pidGUI: student authenticated
    deactivate ip
  

Note over student,ip: Issuing PID 
    pidGUI->>agent: GET http://uself-agent/issuer/credential-offer
    activate agent 
    agent-->>pidGUI: credential_offer
    deactivate agent
    pidGUI->>pidGUI: generate QRCode
    mobile->>pidGUI: read QRCode & user_pin
    
    activate mobile 
    mobile-->>mobile: redirect - http status = 302

    mobile->>agent: GET http://uself-agent/auth/token?user_pin
    activate agent 
    agent-->>mobile: access_token
    deactivate agent
    mobile->>agent: POST http://uself-agent/issuer/credential
    activate agent 
    agent->>authSource: GET http://auth-source/educationalId/pid_identifier
    activate authSource 
    authSource->>db: SELECT * FROM educationalId WHERE pid = pid_identifier
    activate db 
    db-->>authSource: educationalId info
    deactivate db
    authSource-->>agent: educationalId info
    deactivate authSource
    agent-->>pidGUI: send event credential_issued
    agent-->>mobile: credential
    deactivate agent
    deactivate mobile
    deactivate pidGUI
```

### 9.3 Integration with Member State Authority

#### Enhanced Security for Production Implementation

**Member State Validation Layer**: In a production environment, the following additional steps would be integrated:

```http
# Step 2a: Enhanced Member State Validation
GET http://spain.gov.es/identity/validate-citizen
Authorization: Bearer <member_state_api_token>
Content-Type: application/json

{
  "citizen_id": "12345678A",
  "verification_level": "HIGH",
  "requesting_system": "uself-issuer-agent",
  "purpose": "pid_credential_issuance"
}
```

**Member State Response**:
```json
{
  "validation_status": "APPROVED",
  "citizen_verified": true,
  "assurance_level": "HIGH",
  "legal_authority": "Spanish Ministry of Interior",
  "verification_timestamp": "2025-06-03T10:45:00Z",
  "certificate_chain": ["ES_ROOT_CA", "ES_MINISTRY_INTERIOR"]
}
```

---

## 10. Implementation Insights

### 10.1 Technical Architecture Considerations (Based on dc4eu-001-issue-pid-2.md)

#### Pre-Authorised Code Flow Implementation

**Key Technical Decisions**:
- **User PIN Requirement**: Adds an additional security layer beyond standard OAuth2 flows
- **JWT Credential Format**: Ensures compatibility with W3C Verifiable Credentials standard
- **Database Integration**: Direct connection to educational system's authentic data sources
- **Event-Driven Architecture**: Credential issuance events enable audit trails and monitoring

#### Security Enhancements

**Multi-Layer Verification**:
1. **Identity Provider Authentication**: Spanish national system verification
2. **Pre-Authorised Code**: Secure token-based authorisation
3. **User PIN**: Additional user verification step
4. **Cryptographic Proof**: Wallet DID-based proof of control
5. **Database Cross-Reference**: Authentic source data validation

### 10.2 Alignment with Work Package 4 Requirements

#### Datastore Facility Integration Points

The technical implementation provides clear integration points for the Work Package 4 datastore facility:

**Alternative Authentication Path**:
```http
# When Spanish systems unavailable
GET http://wp4-datastore/identity-provider/authorize
X-Delegation-Authority: ES-MINISTRY-INTERIOR
X-Backup-Mode: PROVISIONAL
```

**Enhanced Verification for Provisional Issuance**:
```json
{
  "provisional_mode": true,
  "additional_verification": {
    "document_scan_required": true,
    "biometric_confirmation": true,
    "manual_review_flag": true
  },
  "spanish_authority_notification": "IMMEDIATE",
  "credential_validity": "72_HOURS_PENDING_CONFIRMATION"
}
```

### 10.3 European Interoperability Through Technical Standards

#### EBSI Trust Framework Integration

**Trust Chain Establishment**:
```bash
# Verify issuer trust status
ebsi_verify_issuer("did:ebsi:uself-issuer-agent")

# Validate credential schema compliance
ebsi_validate_schema("eu.europa.ec.eudi.pid", credential_data)

# Check cross-border recognition status
ebsi_check_recognition("ES", "PID", target_member_state)
```

**Schema Harmonisation**:
The PID schema follows EBSI standards whilst maintaining compatibility with national requirements:
- **Core Attributes**: Standardised across all Member States
- **National Extensions**: Accommodate specific national identity elements
- **Selective Disclosure**: Enable privacy-preserving credential presentation
- **Multi-Language Support**: Credential data in multiple European languages

### 10.4 Performance and Scalability Considerations

#### Load Testing Parameters

**Expected Performance Metrics**:
- **Credential Issuance Time**: Maximum 30 seconds end-to-end
- **Concurrent Users**: Support 1,000 simultaneous PID requests
- **Database Query Performance**: Sub-second authentic source response
- **QR Code Generation**: Under 2 seconds for credential offer display
- **Mobile Wallet Integration**: Maximum 5 seconds for credential reception

#### Database Optimisation

**PostgreSQL Performance Tuning**:
```sql
-- Index optimisation for PID lookups
CREATE INDEX CONCURRENTLY idx_educational_id_pid 
ON educationalId (pid) 
WHERE status = 'ACTIVE';

-- Query performance monitoring
EXPLAIN ANALYZE 
SELECT * FROM educationalId 
WHERE pid = '12345678A' 
AND verification_level = 'HIGH';
```

### 10.5 Security Architecture Deep Dive

#### Cryptographic Standards

**JWT Signature Verification**:
```javascript
// Verify PID credential signature
const publicKey = await resolveDidKey("did:ebsi:uself-issuer-agent#keys-1");
const verificationResult = await jose.jwtVerify(pidCredential, publicKey, {
  issuer: "did:ebsi:uself-issuer-agent",
  audience: "did:key:z2dmzD81cgPx8Vki7JbuuMmFYrWPgYoytyKUZ3eyqht1j9Kbh4"
});
```

**DID Resolution Process**:
```bash
# Resolve DID to retrieve public key
curl -X GET "https://ebsi.eu/did-registry/did:ebsi:uself-issuer-agent" \
  -H "Accept: application/json"
```

---

## 11. Quality Assurance and Testing Framework

### 11.1 Technical Testing Based on dc4eu-001-issue-pid-2.md Flow

#### End-to-End Flow Testing

**Test Scenarios**:
```bash
# Complete successful flow
test_pid_issuance_happy_path:
  - student_initiates_request
  - identity_provider_authentication_success
  - credential_offer_generation
  - qr_code_scanning_success
  - token_exchange_completion
  - authentic_source_data_retrieval
  - credential_generation_and_delivery

# Error handling scenarios
test_pid_issuance_error_cases:
  - identity_provider_authentication_failure
  - invalid_user_pin_rejection
  - database_connection_failure
  - credential_generation_errors
  - network_timeout_handling
```

#### Integration Testing with Member State Systems

**Mock Spanish Infrastructure**:
```json
{
  "test_environment": {
    "identity_provider": "https://test-clave.gob.es",
    "citizen_database": "test_spanish_registry",
    "pki_infrastructure": "test_spanish_ca",
    "verification_endpoints": "https://test-spain.gov.es/verify"
  },
  "test_data": {
    "valid_citizens": ["12345678A", "87654321B"],
    "invalid_documents": ["00000000X", "99999999Y"],
    "expired_credentials": ["11111111C"]
  }
}
```

### 11.2 Automated Testing Suite

#### Unit Testing

**Core Component Tests**:
```python
# Test credential offer generation
def test_credential_offer_generation():
    agent = USelfIssuerAgent()
    offer = agent.generate_credential_offer("12345678A")
    assert offer["grants"]["urn:ietf:params:oauth:grant-type:pre-authorized_code"]
    assert offer["grants"]["urn:ietf:params:oauth:grant-type:pre-authorized_code"]["user_pin_required"] == True

# Test database integration
def test_authentic_source_query():
    auth_source = AuthenticSource()
    result = auth_source.get_educational_id("12345678A")
    assert result["status"] == "SUCCESS"
    assert result["citizen_data"]["given_name"] == "María"
```

#### Security Testing

**Penetration Testing Scenarios**:
```bash
# JWT token manipulation tests
test_jwt_tampering:
  - modify_header_algorithm
  - alter_payload_claims
  - invalid_signature_verification
  - expired_token_rejection

# Database injection prevention
test_sql_injection:
  - malicious_pid_parameters
  - authentication_bypass_attempts
  - data_extraction_prevention
```

### 11.3 Performance Monitoring

#### Key Performance Indicators

**Operational Metrics**:
```json
{
  "performance_targets": {
    "pid_issuance_success_rate": "target: 99.5%",
    "authentication_failure_rate": "target: <0.5%",
    "system_availability": "target: 99.9%",
    "credential_delivery_time": "target: <30 seconds",
    "user_pin_validation_time": "target: <2 seconds"
  },
  "security_metrics": {
    "fraud_detection_accuracy": "target: >95%",
    "invalid_attempt_blocking": "target: 100%",
    "audit_trail_completeness": "target: 100%",
    "encryption_compliance": "target: 100%"
  }
}
```

#### Real-Time Monitoring

**Monitoring Dashboard Components**:
```yaml
monitoring_stack:
  - prometheus: metrics_collection
  - grafana: visualisation_dashboards
  - alertmanager: incident_notifications
  - jaeger: distributed_tracing
  - elk_stack: log_aggregation_analysis
```

---

## 12. Appendices

### 12.1 Appendix A: eIDAS 2.0 PID Schema

```json
{
  "@context": [
    "https://www.w3.org/2018/credentials/v1",
    "https://ebsi.eu/schemas/pid/v1.0"
  ],
  "type": ["VerifiableCredential", "PersonIdentificationData"],
  "issuer": {
    "id": "did:ebsi:uself-issuer-agent",
    "name": "uSelf Educational Identity System",
    "type": "EducationalAuthority"
  },
  "credentialSubject": {
    "id": "did:key:z2dmzD81cgPx8Vki7JbuuMmFYrWPgYoytyKUZ3eyqht1j9Kbh4",
    "type": ["Person", "EUIDASpanishCitizen"],
    "identifier": {
      "type": "NationalIdentifier",
      "value": "ES-DNI-12345678A",
      "countryCode": "ES",
      "schemeId": "DNI"
    },
    "personalData": {
      "given_name": "María",
      "family_name": "García López",
      "birth_date": "2004-03-15",
      "birth_place": {
        "locality": "Tarragona",
        "country": "ES"
      },
      "nationality": ["ES"],
      "gender": "F"
    },
    "currentAddress": {
      "street_address": "Carrer de la Unió, 23",
      "locality": "Tarragona",
      "postal_code": "43001",
      "country": "ES"
    },
    "documentDetails": {
      "document_number": "12345678A",
      "issuance_date": "2025-06-03",
      "expiry_date": "2035-06-03",
      "issuing_authority": "uSelf Educational System (Proxy for Spanish Authority)"
    }
  },
  "evidence": [
    {
      "type": "DocumentVerification",
      "verifier": "did:ebsi:spanish-cl@ve-system",
      "evidenceDocument": "Spanish National Identity Card",
      "subjectPresence": "Digital",
      "documentPresence": "Digital"
    }
  ],
  "credentialStatus": {
    "id": "https://uself-agent/credentials/status/12345678A",
    "type": "StatusList2021Entry"
  }
}
```

#### 12.2 Appendix B: Work Package 4 Delegation Agreement Template

```xml
<?xml version="1.0" encoding="UTF-8"?>
<DelegationAgreement xmlns="https://dc4eu.eu/schemas/delegation/v1.0">
  <Header>
    <AgreementID>WP4-ES-2025-001</AgreementID>
    <DelegatingAuthority>Spanish Ministry of Interior</DelegatingAuthority>
    <ProvisionalFacility>DC4EU Work Package 4 Datastore</ProvisionalFacility>
    <EffectiveDate>2025-01-01</EffectiveDate>
    <ExpiryDate>2025-12-31</ExpiryDate>
  </Header>
  
  <Scope>
    <AuthorisedOperations>
      <Operation>Provisional PID Issuance</Operation>
      <Operation>Identity Verification Proxy</Operation>
      <Operation>Temporary Credential Storage</Operation>
    </AuthorisedOperations>
    <Limitations>
      <MaxDuration>72 hours per provisional credential</MaxDuration>
      <RequiredApproval>Spanish Ministry notification within 4 hours</RequiredApproval>
      <MandatoryValidation>Full Spanish verification upon system restoration</MandatoryValidation>
    </Limitations>
  </Scope>
  
  <LegalFramework>
    <PrimaryAuthority>Spanish Ministry of Interior</PrimaryAuthority>
    <LegalResponsibility>Remains exclusively with Spanish State</LegalResponsibility>
    <ComplianceRequirement>Full adherence to Spanish identity laws</ComplianceRequirement>
    <DataSovereignty>Spanish jurisdiction maintained</DataSovereignty>
  </LegalFramework>
  
  <TechnicalRequirements>
    <SecurityLevel>eIDAS High Assurance</SecurityLevel>
    <AuditRequirements>Complete transaction logging</AuditRequirements>
    <EncryptionStandards>AES-256, RSA-4096 minimum</EncryptionStandards>
    <MonitoringFrequency>Real-time with 15-minute reporting</MonitoringFrequency>
  </TechnicalRequirements>
  
  <OperationalProcedures>
    <ActivationTriggers>
      <Trigger>Spanish system downtime exceeding 2 hours</Trigger>
      <Trigger>Critical pilot operations at risk</Trigger>
      <Trigger>Network connectivity issues preventing authentication</Trigger>
    </ActivationTriggers>
    <NotificationProtocol>
      <PrimaryContact>Spanish Ministry Digital Identity Division</PrimaryContact>
      <SecondaryContact>DC4EU Technical Coordination</SecondaryContact>
      <ResponseTime>Maximum 4 hours for approval</ResponseTime>
    </NotificationProtocol>
  </OperationalProcedures>
  
  <QualityAssurance>
    <AuditTrail>Complete logging of all provisional transactions</AuditTrail>
    <SpanishOversight>Real-time monitoring access for Spanish authorities</SpanishOversight>
    <ValidationRequirement>Mandatory Spanish confirmation within 72 hours</ValidationRequirement>
    <DataRetention>All logs retained for 7 years minimum</DataRetention>
  </QualityAssurance>
</DelegationAgreement>
```

### 12.3 Appendix C: Cross-Border Verification Workflow

```mermaid
sequenceDiagram
    participant French_Verifier as French University
    participant EBSI_Registry as EBSI Trust Registry  
    participant Spanish_PID as Spanish PID Credential
    participant Verification_Service as EU Verification Service
    participant Spanish_Authority as Spanish Ministry
    
    Note over French_Verifier,Spanish_Authority: Cross-Border PID Verification
    
    French_Verifier->>Spanish_PID: Present credential for verification
    activate Spanish_PID
    
    Spanish_PID->>EBSI_Registry: Extract issuer DID: did:ebsi:uself-issuer-agent
    activate EBSI_Registry
    
    EBSI_Registry->>EBSI_Registry: Verify uSelf Agent trust status
    EBSI_Registry->>Spanish_Authority: Check Spanish Ministry authorisation
    activate Spanish_Authority
    
    Spanish_Authority->>EBSI_Registry: Confirm delegation authority
    deactivate Spanish_Authority
    
    EBSI_Registry->>French_Verifier: Trust status: VERIFIED
    deactivate EBSI_Registry
    
    French_Verifier->>Verification_Service: Validate cryptographic signature
    activate Verification_Service
    
    Verification_Service->>Verification_Service: Check signature against uSelf public key
    Verification_Service->>EBSI_Registry: Verify Spanish trust chain
    Verification_Service->>French_Verifier: Signature status: VALID
    deactivate Verification_Service
    
    French_Verifier->>French_Verifier: Apply French legal recognition rules
    French_Verifier->>French_Verifier: Schema translation: Spanish -> French format
    
    Note over French_Verifier: Verification Result: ACCEPTED
    
    deactivate Spanish_PID
```

### 12.4 Appendix D: Emergency Activation Procedures

#### WP4 Facility Emergency Response Protocol

**Phase 1: Detection and Assessment (0-30 minutes)**
1. **Automated Monitoring**: System detects Spanish infrastructure unavailability
2. **Impact Assessment**: Evaluate citizen service disruption level
3. **Pilot Risk Analysis**: Assess Large Scale Pilot operational impact
4. **Stakeholder Notification**: Alert Spanish Ministry and WP4 coordination team

**Phase 2: Authorisation and Activation (30-90 minutes)**
1. **Spanish Ministry Contact**: Direct communication with authorised officials
2. **Delegation Confirmation**: Verify legal authority for provisional operation
3. **Security Protocol Activation**: Enhanced verification procedures enabled
4. **System Preparation**: WP4 facility configured for Spanish PID issuance

**Phase 3: Provisional Operations (Duration: Variable)**
1. **Enhanced Citizen Verification**: Additional KYC beyond standard requirements
2. **Real-Time Monitoring**: Continuous Spanish Ministry oversight
3. **Audit Trail Generation**: Complete transaction logging for review
4. **Quality Assurance**: Periodic validation sampling and reporting

**Phase 4: System Restoration and Handover (Post-Recovery)**
1. **Spanish System Verification**: Confirm full operational capability
2. **Provisional Credential Validation**: Spanish authority review of all issued PIDs
3. **Standard Credential Upgrade**: Convert provisional to standard PIDs
4. **Final Audit Report**: Complete operation summary for Spanish authorities

#### Emergency Contact Matrix

```json
{
  "emergency_contacts": {
    "spanish_ministry": {
      "primary": "digital.identity@interior.gob.es",
      "phone": "+34-91-537-1000",
      "escalation": "director.digital@interior.gob.es",
      "response_time": "1 hour maximum"
    },
    "dc4eu_coordination": {
      "primary": "wp4-coordination@dc4eu.eu",
      "phone": "+32-2-123-4567",
      "technical": "technical-support@dc4eu.eu",
      "response_time": "30 minutes maximum"
    },
    "ebsi_operations": {
      "primary": "operations@ebsi.eu",
      "phone": "+32-2-789-0123",
      "security": "security@ebsi.eu",
      "response_time": "2 hours maximum"
    }
  }
}
```

### 12.5 Appendix E: Data Protection and Privacy Framework

#### GDPR Compliance in PID Issuance

**Data Minimisation Principles**:
```json
{
  "data_collection": {
    "necessary_only": "Collect minimum data required for identity verification",
    "purpose_limitation": "Use data solely for PID issuance and legal obligations",
    "storage_limitation": "Retain only as long as legally required",
    "accuracy_requirement": "Ensure data accuracy through multiple verification sources"
  },
  "citizen_rights": {
    "access": "Citizens can view their PID data and issuance records",
    "rectification": "Correction procedures for inaccurate information",
    "erasure": "Right to deletion after legal retention periods",
    "portability": "Standard format for credential portability"
  },
  "technical_safeguards": {
    "encryption": "All PID data encrypted in transit and at rest",
    "access_control": "Role-based access with audit logging",
    "anonymisation": "Personal data anonymised for analytics",
    "secure_deletion": "Cryptographic erasure of expired data"
  }
}
```

**Member State Data Sovereignty**:
- **Territorial Jurisdiction**: PID data remains under national legal framework
- **Cross-Border Transfers**: Regulated under adequacy decisions and safeguards
- **Third Country Access**: Prohibited without explicit Member State authorisation
- **Law Enforcement**: National procedures for lawful access maintained

#### Privacy by Design Implementation

**Data Protection Impact Assessment (DPIA)**:
```yaml
dpia_requirements:
  identification:
    - high_risk_processing: "Large scale processing of identity data"
    - special_categories: "Biometric data for authentication"
    - systematic_monitoring: "Continuous audit trail generation"
  
  necessity_assessment:
    - legal_basis: "eIDAS 2.0 compliance and Member State authority"
    - proportionality: "Minimum data for secure identity verification"
    - alternatives: "No less intrusive methods available"
  
  risk_mitigation:
    - encryption: "End-to-end encryption of all personal data"
    - pseudonymisation: "DIDs used instead of direct identifiers"
    - access_controls: "Strict role-based access permissions"
    - audit_logging: "Complete transaction trails for accountability"
```

### 12.6 Appendix F: Technical Configuration Examples

#### uSelf Issuer Agent Configuration

```yaml
# uself-issuer-agent-config.yml
server:
  host: "0.0.0.0"
  port: 8080
  ssl:
    enabled: true
    keystore: "/etc/ssl/uself-agent.p12"
    truststore: "/etc/ssl/trusted-cas.p12"

database:
  type: "postgresql"
  host: "db.uself-agent.internal"
  port: 5432
  database: "educational_id"
  username: "${DB_USERNAME}"
  password: "${DB_PASSWORD}"
  ssl_mode: "require"
  connection_pool:
    min_size: 5
    max_size: 20
    connection_timeout: 30s

authentication:
  identity_provider:
    url: "https://clave.gob.es"
    client_id: "${CLAVE_CLIENT_ID}"
    client_secret: "${CLAVE_CLIENT_SECRET}"
    scope: "openid profile pid_verification"
    response_type: "code"
    
credential_issuance:
  signing:
    algorithm: "ES256"
    key_id: "did:ebsi:uself-issuer-agent#keys-1"
    private_key_path: "/etc/keys/signing-key.pem"
  
  format: "jwt_vc"
  schema: "eu.europa.ec.eudi.pid"
  validity_period: "P10Y"  # 10 years
  
  pre_authorized_code:
    expiry: "PT1H"  # 1 hour
    user_pin_required: true
    pin_length: 4

ebsi_integration:
  did_registry: "https://api.ebsi.eu/did/v3"
  trust_registry: "https://api.ebsi.eu/trusted-issuers-registry/v3"
  schema_registry: "https://api.ebsi.eu/trusted-schemas-registry/v2"
  
monitoring:
  metrics:
    enabled: true
    endpoint: "/metrics"
    port: 9090
  
  logging:
    level: "INFO"
    format: "json"
    audit_log: "/var/log/uself-agent/audit.log"
    
  health_check:
    endpoint: "/health"
    database_check: true
    ebsi_connectivity_check: true
```

#### Database Schema

```sql
-- Educational ID database schema
CREATE TABLE IF NOT EXISTS educational_id (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    pid VARCHAR(20) NOT NULL UNIQUE,
    given_name VARCHAR(100) NOT NULL,
    family_name VARCHAR(100) NOT NULL,
    birth_date DATE NOT NULL,
    nationality CHAR(2) NOT NULL,
    document_number VARCHAR(20) NOT NULL,
    verification_level VARCHAR(10) NOT NULL DEFAULT 'HIGH',
    status VARCHAR(20) NOT NULL DEFAULT 'ACTIVE',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    verified_at TIMESTAMP WITH TIME ZONE,
    issuing_authority VARCHAR(100) NOT NULL
);

-- Audit trail table
CREATE TABLE IF NOT EXISTS credential_audit (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    credential_id VARCHAR(100) NOT NULL,
    citizen_pid VARCHAR(20) NOT NULL,
    operation VARCHAR(50) NOT NULL,
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    user_agent TEXT,
    ip_address INET,
    details JSONB,
    FOREIGN KEY (citizen_pid) REFERENCES educational_id(pid)
);

-- Performance indices
CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_educational_id_pid 
ON educational_id (pid) WHERE status = 'ACTIVE';

CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_educational_id_verification 
ON educational_id (verification_level, status);

CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_credential_audit_timestamp 
ON credential_audit (timestamp DESC);

-- Row-level security
ALTER TABLE educational_id ENABLE ROW LEVEL SECURITY;
ALTER TABLE credential_audit ENABLE ROW LEVEL SECURITY;

-- Create policies for data access control
CREATE POLICY educational_id_select_policy ON educational_id
FOR SELECT USING (
    current_setting('app.user_role') = 'issuer_agent' OR
    current_setting('app.user_role') = 'audit_reader'
);
```

### 12.7 Appendix G: Troubleshooting Guide

#### Common Issues and Resolutions

**Authentication Failures**:
```bash
# Check Cl@ve system connectivity
curl -I https://clave.gob.es/health
# Expected: HTTP/1.1 200 OK

# Verify TLS certificate validity
openssl s_client -connect clave.gob.es:443 -servername clave.gob.es

# Test authentication endpoint
curl -X POST https://clave.gob.es/oauth/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=client_credentials&client_id=test&client_secret=test"
```

**Database Connection Issues**:
```sql
-- Check database connectivity
SELECT version();

-- Verify table existence and permissions
\dt educational_id;
\dp educational_id;

-- Test query performance
EXPLAIN ANALYZE 
SELECT * FROM educational_id 
WHERE pid = '12345678A' AND status = 'ACTIVE';
```

**Credential Generation Failures**:
```javascript
// Verify DID resolution
const didDocument = await fetch('https://api.ebsi.eu/did/v3/did:ebsi:uself-issuer-agent');
console.log(await didDocument.json());

// Test JWT signing
const jwt = require('jsonwebtoken');
const privateKey = fs.readFileSync('/etc/keys/signing-key.pem');
const token = jwt.sign({ test: 'payload' }, privateKey, { algorithm: 'ES256' });
```

#### Monitoring and Alerting

**Health Check Endpoints**:
```yaml
health_checks:
  - name: "Database Connectivity"
    endpoint: "/health/database"
    expected_status: 200
    timeout: 5s
    
  - name: "Spanish IdP Connectivity"
    endpoint: "/health/clave"
    expected_status: 200
    timeout: 10s
    
  - name: "EBSI Integration"
    endpoint: "/health/ebsi"
    expected_status: 200
    timeout: 15s
```

**Error Codes and Meanings**:
```json
{
  "error_codes": {
    "PID_001": "Invalid citizen identifier format",
    "PID_002": "Citizen not found in educational database",
    "PID_003": "Authentication with Cl@ve system failed",
    "PID_004": "Invalid user PIN provided",
    "PID_005": "Pre-authorised code expired",
    "PID_006": "Database connection timeout",
    "PID_007": "EBSI integration failure",
    "PID_008": "Credential signing failed",
    "PID_009": "Spanish authority validation timeout",
    "PID_010": "WP4 facility activation required"
  }
}
```

---

## Conclusion

This comprehensive PID issuance user journey document successfully integrates the technical specifications from **dc4eu-001-issue-pid-2.md** with the broader policy and governance framework established by Work Package 4 agreements. The implementation demonstrates how foundational digital identity can be established within Member State competence whilst enabling European interoperability through standardised technical protocols.

### Key Achievements

**Technical Compliance**: The document accurately reflects the Pre-Authorised Code flow, message details, and sequence diagram specified in the dc4eu-001-issue-pid-2.md file, ensuring technical implementation alignment with approved specifications.

**Governance Framework**: The Work Package 4 datastore facility provisions are properly contextualised as emergency measures that preserve Member State authority whilst ensuring operational continuity for Large Scale Pilots during system unavailability.

**European Integration**: The EBSI trust framework integration enables cross-border recognition of PIDs whilst maintaining national sovereignty over foundational identity credentials, creating a truly interoperable European digital identity ecosystem.

**Security Excellence**: Multi-layer security implementation ensures eIDAS High assurance level compliance whilst protecting citizen privacy and maintaining data sovereignty under national jurisdiction.

### Implementation Roadmap

**Phase 1: Foundation (Months 1-3)**
- Member State PKI integration and trust establishment
- uSelf Agent deployment and configuration
- Database setup and security hardening
- Initial testing with Spanish Cl@ve system

**Phase 2: Integration (Months 4-6)**
- EBSI trust registry integration
- Cross-border verification testing
- Work Package 4 facility implementation
- Comprehensive security auditing

**Phase 3: Production (Months 7-9)**
- Large Scale Pilot deployment
- Real-world citizen onboarding
- Performance optimisation and monitoring
- Continuous security assessment

**Phase 4: Scale (Months 10-12)**
- Multi-Member State expansion
- Advanced features and optimisation
- Long-term sustainability planning
- Knowledge transfer and documentation

### Future Evolution

As Member State digital identity infrastructure matures and eIDAS 2.0 implementation progresses, this framework will adapt to support enhanced capabilities whilst maintaining the core principles of national sovereignty and European interoperability that underpin the European Digital Identity ecosystem.

The successful implementation of this PID issuance framework creates the essential foundation upon which all subsequent educational, professional, and civic digital credentials can be built, enabling European citizens like María García to participate fully in the digital single market whilst maintaining their fundamental rights to privacy, data protection, and national identity.

### Strategic Impact

This implementation establishes a new paradigm for European digital identity cooperation, demonstrating that national sovereignty and European integration are not mutually exclusive but rather complementary forces that strengthen both individual Member States and the European Union as a whole. The framework serves as a blueprint for future digital identity initiatives across Europe, proving that technical excellence and regulatory compliance can coexist to create services that truly serve European citizens.

Through María's successful PID issuance journey, we witness the birth of a new era in European digital identity—one where technical innovation serves human needs, national sovereignty enables European cooperation, and digital credentials become the foundation for educational mobility, professional recognition, and civic participation across our shared European space.