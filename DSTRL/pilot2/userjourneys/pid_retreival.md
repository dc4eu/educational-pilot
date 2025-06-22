# PID Issuance: European Digital Identity Foundation User Journey

## Executive Summary

This document presents the comprehensive narrative for Person Identification Data (PID) issuance within the DC4EU framework, implementing a Pre-Authorised OpenID4VCI flow with **mandatory Member State identity verification**. The journey demonstrates critical foundational identity establishment that enables all subsequent digital credential issuance across European institutions whilst maintaining Member State sovereignty over identity management.

**Critical Context**: PID issuance remains **exclusively within Member State competence** under eIDAS 2.0 framework. However, Work Package 4 has established an agreement to enable **PID datastore provisioning facility as an authentic source** when the related Member State Authority is temporarily unable to provide PIDs directly, ensuring EUDIW operational continuity for Large Scale Pilots.

**Key Innovation**: This implementation showcases the foundational layer of Europe's digital identity ecosystem, establishing verified legal identity that serves as the cornerstone for all subsequent educational, professional, and civic digital credentials across European borders.

**Bottom Line**: Maria García, a Spanish citizen, successfully obtains her foundational PID credential through the Spanish national identity infrastructure, creating the verified digital identity foundation that will enable her to participate in European educational mobility and access digital services across all Member States.

---

## Table of Contents

1. [Quick Reference Guide](#1-quick-reference-guide)
2. [Governance and Competence Framework](#2-governance-and-competence-framework)
3. [Infrastructure Prerequisites](#3-infrastructure-prerequisites)
4. [The Story: Maria's Digital Identity Foundation](#4-the-story-marias-digital-identity-foundation)
5. [Actor Ecosystem and Roles](#5-actor-ecosystem-and-roles)
6. [Technical Architecture Overview](#6-technical-architecture-overview)
7. [Detailed User Journey Flow](#7-detailed-user-journey-flow)
8. [Work Package 4 Provisional Solutions](#8-work-package-4-provisional-solutions)
9. [Technical Message Details](#9-technical-message-details)
10. [Implementation Insights](#10-implementation-insights)
11. [Appendices](#11-appendices)

---

## 1. Quick Reference Guide

### 1.1 Process Overview

1. **Citizen Authentication**: National identity verification through Member State systems
2. **Legal Identity Validation**: Official document verification and biometric confirmation
3. **PID Credential Issuance**: Cryptographically signed foundational identity credential
4. **European Interoperability**: EBSI trust registry integration for cross-border recognition
5. **Fallback Provisioning**: Work Package 4 datastore facility when Member State systems unavailable

### 1.2 Key Actors

- **Citizen**: Maria García (Spanish national, credential holder)
- **Member State Authority**: Spanish Ministry of Interior (primary issuer)
- **National Identity Provider**: Cl@ve authentication system
- **WP4 Datastore Facility**: Provisional authentic source (when MS unavailable)
- **EBSI Trust Registry**: European-wide validation infrastructure

### 1.3 Regulatory Framework

- **Primary Competence**: Member State authority under eIDAS 2.0
- **European Standards**: Interoperability through EBSI trust framework
- **Data Protection**: GDPR compliance with national data sovereignty
- **Cross-Border Recognition**: Mutual recognition across all EU Member States

### 1.4 Critical Success Factors

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

---

## 4. The Story: Maria's Digital Identity Foundation

### 4.1 Setting the Scene

**Location**: Tarragona, Spain  
**Date**: Monday, 3rd June 2025, 10:30 AM  
**Context**: Maria García, 21, needs to establish her foundational digital identity to participate in European educational mobility programmes

Maria sits in her university dormitory, knowing that before she can access any European digital services or apply for study abroad programmes, she needs her foundational digital identity credential—her PID. This isn't just another university credential; it's the legal foundation that proves who she is according to Spanish law and enables her participation in the broader European digital ecosystem.

### 4.2 The Digital Identity Imperative

**Why PIDs Matter**: In the emerging European digital economy, PID credentials serve as the foundational layer for all other digital interactions. Without a verified PID, Maria cannot:
- Apply for educational credentials from any European university
- Access cross-border professional qualification recognition
- Participate in European student mobility programmes
- Use European digital public services whilst travelling

**The Legal Framework**: Her PID will be issued directly by Spanish authorities, ensuring it carries the full legal weight of Spanish sovereignty whilst being recognised across all EU Member States through the EBSI trust framework.

---

## 5. Actor Ecosystem and Roles

### 5.1 Primary Actors

#### Maria García (Citizen/Holder)
- **Role**: Spanish citizen requesting foundational digital identity
- **Responsibilities**: Provide authentic identity documentation, complete verification procedures
- **Technical Requirements**: EUDI Wallet app, valid Spanish identity documentation
- **Legal Status**: Spanish national with full civil rights

#### Spanish Ministry of Interior (Issuing Authority)
- **Role**: Authoritative PID issuer for Spanish citizens
- **Responsibilities**: Identity verification, legal validation, secure credential issuance
- **Technical Capabilities**: National PKI, citizen databases, cryptographic infrastructure
- **Legal Authority**: Exclusive competence under Spanish law and eIDAS 2.0

#### Cl@ve Authentication System (Identity Provider)
- **Role**: National citizen authentication platform
- **Responsibilities**: Secure citizen login, multi-factor authentication, session management
- **Technical Integration**: DNI card readers, biometric systems, SMS verification
- **Security Level**: eIDAS High assurance level authentication

### 5.2 Supporting Infrastructure

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

### 6.1 National Identity Layer

**Spain's Digital Identity Infrastructure**:
- **Citizen Authentication**: Cl@ve system with DNI integration
- **Document Verification**: Real-time validation against civil registries
- **Biometric Confirmation**: Fingerprint matching with national databases
- **Legal Validation**: Cross-reference with population and immigration records

### 6.2 Credential Issuance Layer

**Technical Components**:
- **Identity Proofing Service**: High-assurance citizen verification
- **Credential Generation Service**: W3C VC compliant PID creation
- **Digital Signature Service**: Spanish national PKI signing infrastructure
- **Distribution Service**: Secure delivery to citizen's EUDI Wallet

### 6.3 European Interoperability Layer

**EBSI Integration**:
- **Trust Anchor Registration**: Spanish Ministry registered as authoritative issuer
- **Schema Harmonisation**: Standard PID data model across Member States
- **Cross-Border Validation**: Real-time verification of Spanish PIDs in other MS
- **Revocation Management**: Coordinated credential lifecycle management

### 6.4 Protocol Stack

- **Application Layer**: OpenID4VCI with eIDAS 2.0 extensions
- **Credential Layer**: W3C Verifiable Credentials with PID schema
- **Trust Layer**: EBSI trust registries and Member State PKI
- **Cryptographic Layer**: ES256 signatures with national key management
- **Transport Layer**: HTTPS with additional security headers and endpoint protection

---

## 7. Detailed User Journey Flow

### 7.1 Phase 1: Citizen Initiation (Steps 1-5)

#### Step 1: Digital Identity Request
*Monday, 10:30 AM - Maria's dormitory*

Maria opens her EUDI Wallet application and selects "Obtain Digital Identity Documents". The interface clearly explains that she's about to request her foundational PID credential from Spanish authorities.

**Technical Action**: 
```http
GET https://wallet.eu/identity/request-pid
```

**Behind the Scenes**: The wallet prepares for Spain-specific PID issuance, configuring the interface for Spanish regulatory requirements and authentication methods.

#### Step 2: Member State Selection and Routing
*System identifies citizen nationality*

The EUDI Wallet automatically detects Maria's Spanish nationality from her device configuration and routes her request to the Spanish national identity infrastructure.

**Technical Exchange**:
```http
GET https://spain.gov.es/identity/pid-issuance/initiate
```

**Regulatory Compliance**: The system ensures that only Spanish authorities will handle her foundational identity verification, maintaining national sovereignty.

#### Step 3: National Authentication Initiation
*Cl@ve system engagement*

Maria is redirected to the official Cl@ve authentication portal, Spain's national citizen authentication system, which will verify her identity to the highest assurance level.

**Technical Implementation**:
```http
REDIRECT https://clave.gob.es/authenticate?return_uri=https://wallet.eu/callback&citizen_id=12345678A
```

**User Experience**: Maria sees the familiar Spanish government interface with options for:
- DNI card authentication
- Mobile phone verification
- Biometric authentication

#### Step 4: Multi-Factor Authentication
*High-assurance identity verification*

Maria chooses DNI card authentication, inserting her Spanish national identity card into her laptop's card reader and entering her PIN.

**Technical Process**:
```bash
# DNI card verification
dni_verify --card-present --pin-verification --biometric-match
```

**Security Level**: This achieves eIDAS High level of assurance, meeting the strict requirements for foundational identity credentials.

#### Step 5: Biometric Confirmation
*Final identity proofing*

The system prompts Maria to provide a live facial photograph, which is matched against the biometric data stored on her DNI card and in national databases.

**Verification Process**:
- **Liveness detection**: Ensures the photograph is taken in real-time
- **Facial recognition**: Matches against DNI card photograph
- **Database cross-reference**: Confirms identity with civil registry records

### 7.2 Phase 2: Legal Identity Validation (Steps 6-12)

#### Step 6: Civil Registry Verification
*Behind the scenes legal validation*

The Spanish Ministry of Interior's systems automatically verify Maria's legal status by cross-referencing multiple official databases.

**Technical Queries**:
```sql
-- Population registry check
SELECT * FROM population_registry WHERE dni = '12345678A';

-- Civil status verification  
SELECT * FROM civil_status WHERE citizen_id = '12345678A';

-- Immigration status (for naturalised citizens)
SELECT * FROM immigration_records WHERE dni = '12345678A';
```

**Validation Results**: Confirms Maria's Spanish nationality, civil status, and legal residence.

#### Step 7: Document Authenticity Verification
*Anti-fraud measures*

The system validates the authenticity of Maria's DNI card by checking its cryptographic signatures and comparing security features against known valid patterns.

**Security Checks**:
- **Card authenticity**: Cryptographic signature validation
- **Chip integrity**: Secure element data verification
- **Physical security**: Comparison with known counterfeit patterns
- **Issuing authority**: Confirmation of legitimate card issuance

#### Step 8: Historical Identity Validation
*Comprehensive background verification*

The system reviews Maria's identity history to ensure consistency and detect any irregularities or previous identity changes.

**Historical Analysis**:
- **Previous addresses**: Residential history validation
- **Name changes**: Legal name modification records
- **Document history**: Previous DNI issuances and renewals
- **Cross-border activity**: Entry/exit records for validation

#### Step 9: Risk Assessment and Fraud Detection
*Advanced security screening*

Automated systems perform sophisticated risk analysis to detect potential identity fraud or credential abuse.

**Risk Factors Evaluated**:
- **Behaviour patterns**: Unusual authentication attempts
- **Device analysis**: Device fingerprinting and location verification
- **Network analysis**: VPN detection and IP reputation
- **Temporal analysis**: Request timing and frequency patterns

### 7.3 Phase 3: PID Credential Generation (Steps 13-18)

#### Step 10: Legal Authority Confirmation
*Final authorisation checkpoint*

The Spanish Ministry of Interior's authorised officer (automated system with human oversight) makes the final decision to issue the PID credential.

**Authorisation Process**:
```json
{
  "citizen_id": "12345678A",
  "verification_status": "PASSED",
  "assurance_level": "HIGH",
  "issuing_authority": "ES_MINISTRY_INTERIOR",
  "legal_basis": "eIDAS_2.0_Article_7",
  "authorisation_timestamp": "2025-06-03T10:45:23Z"
}
```

#### Step 11: PID Schema Population
*Credential data preparation*

The system prepares Maria's PID credential according to the standardised European schema whilst maintaining Spanish national specificities.

**PID Data Structure**:
```json
{
  "credentialSubject": {
    "id": "did:key:z2dmzD81cgPx8Vki7JbuuMmFYrWPgYoytyKUZ3eyqht1j9Kbh4",
    "type": ["Person", "EUIDASpanishCitizen"],
    "identifier": "ES-DNI-12345678A",
    "given_name": "María",
    "family_name": "García López",
    "birth_date": "2004-03-15",
    "birth_place": "Tarragona, España",
    "nationality": "ES",
    "gender": "F",
    "current_address": {
      "street_address": "Carrer de la Unió, 23",
      "locality": "Tarragona",
      "postal_code": "43001",
      "country": "ES"
    },
    "issuing_authority": "Ministerio del Interior - España",
    "document_number": "12345678A",
    "issuance_date": "2025-06-03",
    "expiry_date": "2035-06-03"
  }
}
```

#### Step 12: Cryptographic Signing
*Spanish national PKI signature*

The PID credential is digitally signed using Spain's national PKI infrastructure, ensuring its legal validity and tamper-evident properties.

**Signing Process**:
```bash
# Generate credential signature using Spanish national CA
sign_credential --issuer="Spain_Ministry_Interior" --key="national_pid_signing_key" --algorithm="ES256"
```

**Trust Chain**: The signature creates a verifiable trust chain from Maria's credential back to the Spanish state's root certificate authority.

### 7.4 Phase 4: European Integration and Delivery (Steps 19-22)

#### Step 13: EBSI Trust Registry Registration
*European interoperability establishment*

The newly issued PID is registered with the EBSI trust registry, enabling its recognition across all EU Member States.

**EBSI Integration**:
```http
POST https://ebsi.eu/trust-registry/credentials
{
  "issuer": "did:ebsi:spain-ministry-interior",
  "credential_type": "PID",
  "member_state": "ES",
  "schema_id": "https://ebsi.eu/schemas/pid/v1.0",
  "trust_anchor": "ES_ROOT_CA"
}
```

#### Step 14: Cross-Border Validation Setup
*Multi-Member State recognition*

The credential is configured for recognition by other Member States' verification systems, enabling Maria to use her Spanish PID across Europe.

**Validation Configuration**:
- **Schema mapping**: Alignment with other MS PID formats
- **Trust path establishment**: Clear verification pathway for foreign verifiers
- **Attribute translation**: Language and format conversion capabilities
- **Legal equivalency**: Mapping to other national identity frameworks

#### Step 15: Secure Delivery to EUDI Wallet
*Final credential transmission*

The completed PID credential is securely transmitted to Maria's EUDI Wallet through encrypted channels.

**Delivery Protocol**:
```http
POST https://wallet.eu/credentials/receive
Authorization: Bearer <citizen_access_token>
Content-Type: application/json

{
  "credential": "<JWT_ENCODED_PID_CREDENTIAL>",
  "issuer_metadata": "<SPANISH_MINISTRY_METADATA>",
  "trust_chain": "<EBSI_VALIDATION_PATH>"
}
```

#### Step 16: Wallet Integration and Storage
*Local credential management*

Maria's EUDI Wallet receives the PID, validates its authenticity, and securely stores it for future use.

**Wallet Processing**:
- **Signature verification**: Confirms Spanish Ministry authenticity
- **EBSI validation**: Checks European trust registry status
- **Local storage**: Encrypted storage in secure element
- **Backup preparation**: Secure cloud backup with user consent

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

**Modified User Journey**: When Maria attempts to obtain her PID and Spanish systems are unavailable:

1. **Automatic Detection**: Wallet detects Spanish system unavailability
2. **Facility Routing**: Request routed to WP4 datastore facility
3. **Spanish Authority Validation**: Facility contacts available Spanish authentication services
4. **Provisional Issuance**: Credential issued under Spanish authority but via facility infrastructure
5. **Enhanced Validation**: Additional verification steps to ensure legitimacy
6. **Temporary Marking**: Credential clearly marked as provisionally issued
7. **Spanish Confirmation**: Full validation occurs when Spanish systems resume

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

### 9.1 Initiate PID Request

**Request Initiation**:
```http
GET https://spain.gov.es/identity/pid-issuance/initiate
User-Agent: EUDI-Wallet/2.1.0
Accept: application/json
X-Citizen-Nationality: ES
X-Request-Type: initial_pid_issuance
```

**Response**:
```json
{
  "authentication_endpoint": "https://clave.gob.es/authenticate",
  "required_documents": ["DNI", "biometric_verification"],
  "assurance_level": "HIGH",
  "estimated_duration": "15-20 minutes",
  "legal_notice": "This PID will be issued under Spanish national authority",
  "session_id": "es_pid_20250603_104530_001"
}
```

### 9.2 Cl@ve Authentication

**Authentication Request**:
```http
POST https://clave.gob.es/authenticate
Content-Type: application/x-www-form-urlencoded

citizen_id=12345678A&
authentication_method=dni_card&
return_uri=https://spain.gov.es/pid-callback&
assurance_level=HIGH&
session_id=es_pid_20250603_104530_001
```

**Authentication Response**:
```json
{
  "authentication_status": "SUCCESS",
  "citizen_verified": true,
  "assurance_level": "HIGH",
  "verification_methods": ["dni_card", "biometric_match"],
  "citizen_attributes": {
    "dni": "12345678A",
    "verified_identity": true,
    "biometric_match": true,
    "card_authenticity": "VALID"
  },
  "auth_token": "eyJhbGciOiJFUzI1NiIs...",
  "expires_in": 1800
}
```

### 9.3 PID Credential Generation

**Credential Generation Request**:
```http
POST https://spain.gov.es/identity/generate-pid
Authorization: Bearer eyJhbGciOiJFUzI1NiIs...
Content-Type: application/json

{
  "citizen_id": "12345678A",
  "verification_status": "COMPLETE",
  "assurance_level": "HIGH",
  "requested_format": "w3c_verifiable_credential",
  "wallet_did": "did:key:z2dmzD81cgPx8Vki7JbuuMmFYrWPgYoytyKUZ3eyqht1j9Kbh4"
}
```

**PID Credential Response**:
```json
{
  "credential": "eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImRpZDplYnNpOnNwYWluLW1pbmlzdHJ5LWludGVyaW9yI2tleXMtMSJ9.eyJpc3MiOiJkaWQ6ZWJzaTpzcGFpbi1taW5pc3RyeS1pbnRlcmlvciIsInN1YiI6ImRpZDprZXk6ejJkbXpEODFjZ1B4OFZraTdKYnV1TW1GWXJXUGdZb3l0eWtVWjNleXFodDFqOUtiaD...",
  "credential_type": "PID",
  "issuer": "Spanish Ministry of Interior",
  "issuance_date": "2025-06-03T10:45:23Z",
  "expiry_date": "2035-06-03T10:45:23Z",
  "trust_chain": ["ES_ROOT_CA", "ES_MINISTRY_INTERIOR", "PID_ISSUING_KEY"],
  "ebsi_registration": "https://ebsi.eu/trust-registry/credentials/es_pid_20250603_001"
}
```

### 9.4 EBSI Trust Registry Integration

**Trust Registry Registration**:
```http
POST https://ebsi.eu/trust-registry/register-credential
Authorization: Bearer <ministry_api_token>
Content-Type: application/json

{
  "issuer_did": "did:ebsi:spain-ministry-interior",
  "credential_id": "es_pid_20250603_001",
  "credential_type": "PID",
  "member_state": "ES",
  "schema_compliance": "ebsi_pid_v1.0",
  "trust_anchor": "ES_ROOT_CA",
  "cross_border_recognition": true
}
```

---

## 10. Implementation Insights

### 10.1 Member State Integration Challenges

#### Technical Harmonisation

**National System Variations**: Each Member State operates unique identity infrastructure:
- **Authentication Methods**: DNI cards (Spain), eID cards (Belgium), BankID (Sweden)
- **Data Schemas**: Different national identity attribute sets
- **Security Levels**: Varying assurance level implementations
- **Legal Requirements**: National privacy and data protection variations

**Standardisation Approach**:
```json
{
  "harmonisation_strategy": {
    "common_schema": "EBSI PID standard with national extensions",
    "authentication_mapping": "National methods to eIDAS assurance levels",
    "data_minimisation": "Core attributes + optional national specifics",
    "legal_compliance": "GDPR + national identity legislation"
  }
}
```

#### Legal and Regulatory Coordination

**Sovereignty Protection**: Ensuring Member State authority is preserved:
- **National Oversight**: Member State approval for all PID issuance
- **Legal Responsibility**: Clear accountability for credential validity
- **Audit Rights**: Member State access to all citizen PID records
- **Revocation Authority**: Exclusive Member State control over credential lifecycle

### 10.2 Work Package 4 Facility Implementation

#### Technical Architecture Considerations

**High Availability Design**:
```bash
# WP4 Facility Components
Load_Balancer: Multi-region distribution
Auth_Proxy: Redundant connections to Member State systems  
Verification_Engine: Enhanced KYC with multiple validation sources
Credential_Store: Encrypted temporary storage for provisional PIDs
Audit_System: Real-time transaction logging and Member State reporting
Monitoring: 24/7 operational oversight with automated alerts
```

**Security Enhancements for Provisional Issuance**:
- **Multi-Factor Verification**: Additional validation steps beyond normal requirements
- **Enhanced Audit Trail**: Complete transaction recording for Member State review
- **Time-Limited Validity**: Provisional credentials expire if not validated
- **Clear Status Marking**: Obvious indication of provisional vs. standard issuance

#### Operational Protocols

**Activation Decision Matrix**:
```json
{
  "activation_criteria": {
    "technical_failure": "Member State systems unavailable > 2 hours",
    "pilot_criticality": "Large Scale Pilot operations at risk",
    "citizen_impact": "Significant citizen service disruption",
    "member_state_approval": "Explicit MS authorisation required",
    "monitoring_requirement": "Continuous oversight mandatory"
  }
}
```

### 10.3 European Interoperability Excellence

#### Cross-Border Recognition Mechanisms

**Trust Path Establishment**:
- **EBSI Integration**: All Member State PIDs registered in European trust registry
- **Mutual Recognition**: Automatic acceptance of foreign PIDs by national verifiers
- **Schema Translation**: Real-time conversion between national PID formats
- **Legal Equivalency**: Harmonised legal status across Member State boundaries

**Verification Workflow for Foreign PIDs**:
```bash
# French verifier checking Spanish PID
1. Extract_Issuer_DID: "did:ebsi:spain-ministry-interior"
2. Query_EBSI: Verify Spanish Ministry trust status
3. Validate_Signature: Check cryptographic authenticity
4. Schema_Translation: Convert Spanish attributes to French equivalents
5. Legal_Recognition: Apply French legal recognition rules
6. Verification_Result: Accept/Reject with audit trail
```

---

## 11. Appendices

### 11.1 Appendix A: eIDAS 2.0 PID Schema

```json
{
  "@context": [
    "https://www.w3.org/2018/credentials/v1",
    "https://ebsi.eu/schemas/pid/v1.0"
  ],
  "type": ["VerifiableCredential", "PersonIdentificationData"],
  "issuer": {
    "id": "did:ebsi:spain-ministry-interior",
    "name": "Ministerio del Interior - España",
    "type": "MemberStateAuthority"
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
      "issuing_authority": "Ministerio del Interior - España"
    }
  },
  "evidence": [
    {
      "type": "DocumentVerification",
      "verifier": "did:ebsi:spain-ministry-interior",
      "evidenceDocument": "Spanish National Identity Card",
      "subjectPresence": "Physical",
      "documentPresence": "Physical"
    }
  ],
  "credentialStatus": {
    "id": "https://spain.gov.es/credentials/status/12345678A",
    "type": "StatusList2021Entry"
  }
}
```

### 11.2 Appendix B: Work Package 4 Delegation Agreement Template

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
</DelegationAgreement>
```

### 11.3 Appendix C: Cross-Border Verification Workflow

```mermaid
sequenceDiagram
    participant French_Verifier as French University
    participant EBSI_Registry as EBSI Trust Registry  
    participant Spanish_PID as Spanish PID Credential
    participant Verification_Service as EU Verification Service
    
    Note over French_Verifier,Verification_Service: Cross-Border PID Verification
    
    French_Verifier->>Spanish_PID: Present credential for verification
    activate Spanish_PID
    
    Spanish_PID->>EBSI_Registry: Extract issuer DID: did:ebsi:spain-ministry-interior
    activate EBSI_Registry
    
    EBSI_Registry->>EBSI_Registry: Verify Spanish Ministry trust status
    EBSI_Registry->>French_Verifier: Trust status: VERIFIED
    deactivate EBSI_Registry
    
    French_Verifier->>Verification_Service: Validate cryptographic signature
    activate Verification_Service
    
    Verification_Service->>Verification_Service: Check signature against Spanish public key
    Verification_Service->>French_Verifier: Signature status: VALID
    deactivate Verification_Service
    
    French_Verifier->>French_Verifier: Apply French legal recognition rules
    French_Verifier->>French_Verifier: Schema translation: Spanish -> French format
    
    Note over French_Verifier: Verification Result: ACCEPTED
    
    deactivate Spanish_PID
```

### 11.4 Appendix D: Emergency Activation Procedures

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

### 11.5 Appendix E: Data Protection and Privacy Framework

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

### 11.6 Appendix F: Quality Assurance and Testing Framework

#### Comprehensive Testing Strategy

**Identity Verification Testing**:
```bash
# Test scenarios for PID issuance
test_scenarios:
  - valid_citizen_standard_flow
  - invalid_document_rejection
  - biometric_mismatch_handling
  - expired_document_detection
  - duplicate_request_prevention
  - cross_border_verification
  - emergency_facility_activation
  - provisional_credential_upgrade
  - system_failure_recovery
  - audit_trail_integrity
```

**Performance and Scalability Requirements**:
- **Response Time**: Maximum 5 seconds for identity verification
- **Throughput**: Support 10,000 concurrent PID issuance requests
- **Availability**: 99.9% uptime with graceful degradation
- **Recovery Time**: Maximum 1 hour for system restoration

**Security Testing Protocol**:
- **Penetration Testing**: Quarterly security assessments
- **Vulnerability Scanning**: Continuous automated security monitoring
- **Cryptographic Validation**: Regular key rotation and algorithm verification
- **Social Engineering Protection**: Phishing and fraud resistance testing

---

## Conclusion

This comprehensive user journey document establishes the foundational framework for Person Identification Data (PID) issuance within the DC4EU ecosystem whilst maintaining absolute respect for Member State competence and sovereignty. The implementation demonstrates how European digital identity interoperability can be achieved without compromising national authority over foundational identity credentials.

**Key Success Factors**:
- **Member State Sovereignty**: Exclusive national authority over PID issuance preserved
- **European Interoperability**: Seamless cross-border recognition through EBSI trust framework
- **Operational Continuity**: Work Package 4 provisional facility ensures Large Scale Pilot viability
- **Legal Compliance**: Full adherence to eIDAS 2.0 and national identity legislation
- **Technical Excellence**: Robust, secure, and scalable implementation supporting European digital transformation

**Future Evolution**: As Member State digital identity infrastructure matures and eIDAS 2.0 implementation progresses, this framework will adapt to support enhanced capabilities whilst maintaining the core principles of national sovereignty and European interoperability that underpin the European Digital Identity ecosystem.

The successful implementation of this PID issuance framework creates the essential foundation upon which all subsequent educational, professional, and civic digital credentials can be built, enabling European citizens to participate fully in the digital single market whilst maintaining their fundamental rights to privacy, data protection, and national identity.