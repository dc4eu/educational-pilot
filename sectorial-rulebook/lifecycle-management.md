# Lifecycle Management

## Overview

The credential lifecycle system supports educational mobility while protecting credential integrity. This balance enables institutions to manage qualifications independently while ensuring European-wide recognition. The system incorporates privacy-by-design principles, letting institutions update credential status without tracking usage patterns.

## Breaking the Delegated Authentication Model: eIDAS 2.0 and EUDIW Privacy Revolution

### The Traditional "Phone Home" Problem

Traditional PKI-based verification systems relied on **delegated authentication models** where verification activities required direct communication between verifiers and credential issuers or their infrastructure:

- **Certificate Revocation Lists (CRLs)**: Verifiers download complete revocation lists from issuing Certificate Authorities
- **Online Certificate Status Protocol (OCSP)**: Real-time queries to issuer-controlled OCSP responders
- **Direct issuer contact**: Verification processes that reveal to issuers when and where their credentials are being used

This model created significant **privacy and surveillance concerns**:
- **Tracking capability**: Issuers could monitor when, where, and by whom their credentials were being verified
- **Central surveillance points**: Single points where verification activities could be monitored
- **Privacy violation**: Credential usage patterns could be tracked and profiled
- **Cross-border surveillance**: Foreign credential usage could be monitored by issuing states

### The eIDAS 2.0 and EUDIW Paradigm Shift

The **European Digital Identity Wallet (EUDIW)** framework under **eIDAS 2.0** fundamentally transforms this model by implementing **user-controlled, privacy-preserving verification**:

**Core Principle**: **Verification must avoid "phone home" calls** that could compromise credential holder privacy or enable tracking of credential usage.

### Privacy-Preserving Status Verification

The new model implements several mechanisms to eliminate privacy-invasive verification:

**Decentralised StatusLists (StatusList2021)**:
- Status information is published in **privacy-preserving formats** that don't require direct issuer contact
- **Batch processing** of status information prevents individual credential tracking
- **Unlinkable queries** ensure verification activities cannot be correlated to specific users
- **Distributed caching** eliminates single points of surveillance

**EBSI Proxy Services**:
- **Decentralised proxy infrastructure** shields verification activities from issuer monitoring
- **Aggregated status checking** prevents individual credential usage tracking
- **Privacy-preserving trust resolution** without revealing verification patterns
- **Multi-jurisdictional distribution** prevents single-state surveillance

**Wallet-Mediated Verification**:
- **User-controlled disclosure** where credential holders determine what information to share
- **Local verification capabilities** where possible, eliminating external communication
- **Privacy-preserving presentation protocols** that minimise data exposure
- **Selective disclosure** ensuring only necessary information is revealed

### Technical Implementation Requirements

To comply with eIDAS 2.0 privacy principles, verification systems must:

**Eliminate Direct Issuer Contact**:
- Status verification **must not** involve direct communication with credential issuers
- Revocation and suspension checking **must use** privacy-preserving methods
- Trust chain validation **must avoid** revealing verification activities to issuers

**Implement Privacy-Preserving Protocols**:
- Use **StatusList2021** or equivalent privacy-preserving status mechanisms
- Employ **unlinkable status queries** that prevent correlation attacks
- Implement **distributed verification infrastructure** to prevent central monitoring
- Support **offline verification** where cryptographically possible

**Protect Verification Metadata**:
- Verification timestamps **must not** be shared with issuers
- Verifier identity **must not** be revealed to issuers during status checking
- Geographic location of verification **must not** be exposed through verification protocols
- Frequency of verification **must not** be trackable by issuers

### Member State Implementation Considerations

Different member states must adapt their verification infrastructure to support privacy-preserving models:

**National Status Infrastructure**:
- Transition from **centralised OCSP responders** to **decentralised StatusLists**
- Implement **privacy-preserving aggregation** of credential status information
- Support **distributed caching** of status information without tracking
- Ensure **cross-border privacy protection** in verification protocols

**Regulatory Compliance**:
- Verification systems must comply with **GDPR data minimisation** principles
- Status checking must implement **purpose limitation** and avoid excessive data collection
- **Data protection by design** must be embedded in all verification protocols
- **User consent mechanisms** must govern verification activities where required

## Electronic Attestations of Attributes (EAAs) Lifecycle Requirements

In the education and professional qualifications domain, issuers of Electronic Attestations of Attributes (EAAs) must maintain comprehensive lifecycle management capabilities to ensure credential integrity and regulatory compliance across the European Union, whilst adhering to the new privacy-preserving verification paradigm.

### Mandatory Revocation Capabilities

**All EAA issuers** in the education and professional qualifications sector are required to implement revocation capabilities:

- **Educational institutions** issuing academic credentials must be able to revoke EAAs in cases such as:
  - Discovery of academic misconduct or fraud
  - Withdrawal of institutional accreditation
  - Correction of erroneous credential information
  - Violation of academic integrity policies

- **Professional qualifications bodies** must revoke EAAs when:
  - Professional misconduct is established
  - Licensing requirements are no longer met
  - Continuing professional development obligations are not fulfilled
  - Professional registration is terminated

### Member State-Specific Suspension Requirements

Some member states require **suspension capabilities** in addition to revocation, allowing for temporary invalidation of EAAs:

- **Temporary suspension** may be required during:
  - Ongoing investigations into academic or professional misconduct
  - Pending resolution of licensing disputes
  - Administrative reviews of credential validity
  - Appeals processes against professional sanctions

- **Automatic suspension** may occur when:
  - Professional licenses require renewal but are temporarily expired
  - Continuing education requirements are temporarily unmet
  - Institutional accreditation is under review

### Impact on Verification Processes

The verification process **must account for both revocation and suspension status** to properly validate EAA authenticity, whilst **strictly avoiding "phone home" calls** that could compromise privacy:

**For an EAA to be considered valid**, verifiers must confirm:
1. **Cryptographic integrity**: The EAA's digital signature is valid
2. **Issuer authorisation**: The issuing entity is authorised to issue the specific EAA type
3. **Current status**: The EAA has not been revoked or suspended (checked via privacy-preserving methods)
4. **Temporal validity**: The EAA is within its validity period
5. **Trust chain integrity**: All components of the trust chain remain valid

**Privacy-Preserving Verification Requirements**:
- Status checking **must use** privacy-preserving mechanisms like StatusList2021
- Verification **must not** reveal to issuers when, where, or by whom credentials are being verified
- **No direct communication** with issuer infrastructure during verification
- **Unlinkable status queries** to prevent tracking of verification activities

**Verification failures** occur when:
- The EAA status indicates "revoked" or "suspended" (determined through privacy-preserving means)
- The privacy-preserving status checking service is unavailable (depending on policy)
- The revocation or suspension information cannot be cryptographically verified without compromising privacy
- Verification would require "phone home" calls that violate privacy principles

## Key Components

### Credential Status Tracking
- Tracks credential status changes (active, suspended, revoked)
- Supports institutional control over credential validity
- Provides transparency about qualification status
- Maintains credential integrity through cryptographically signed status updates

### Privacy-Preserving Verification
- Maintains verification services that respect privacy
- Prevents tracking of credential usage through unlinkable status queries
- Protects student and professional privacy rights
- Implements data minimisation principles in status responses

### Institutional Management Tools
- Provides tools for educational institutions and professional bodies to manage their issued credentials
- Enables administrative processes for credential updates including suspension and revocation
- Supports institutional autonomy in credential lifecycle decisions
- Facilitates credential maintenance across the entire lifecycle

### Status Communication Mechanisms
- **StatusList2021**: Primary method for communicating revocation and suspension status in a privacy-preserving manner
- **Privacy-preserving real-time status checking**: For high-assurance verification scenarios without compromising privacy
- **Batch status updates**: For efficient processing of multiple credential status changes without individual tracking
- **Decentralised proxy protocols**: To protect credential holder privacy during verification and eliminate "phone home" scenarios

## Implementation Considerations

When implementing lifecycle management for EAAs under the new eIDAS 2.0 privacy paradigm:
- Status update mechanisms must be secure and authenticated using institutional digital certificates
- **Privacy protection must be built into all verification processes** to prevent tracking and eliminate "phone home" scenarios
- Status information should be available **without compromising privacy** through unlinkable queries and decentralised infrastructure
- Audit trails should document all status changes with tamper-evident logging **whilst protecting verification privacy**
- Revocation and suspension should be effective across the entire European ecosystem **through privacy-preserving mechanisms**
- Member state-specific requirements for suspension must be accommodated **within the privacy-preserving framework**
- Fallback mechanisms should handle status service unavailability **without reverting to privacy-invasive methods**
- Status checking must be integrated into all verification workflows **using only privacy-preserving protocols**
- **Traditional CRL/OCSP mechanisms must be replaced** with privacy-preserving alternatives like StatusList2021
- **Direct issuer contact during verification is prohibited** to maintain privacy and prevent tracking

## Cross-Border Scenarios

For cross-border educational mobility and professional recognition, lifecycle management provides:
- Consistent status verification across all member states
- Support for qualification recognition throughout the entire credential lifecycle
- Privacy protection for mobile students and professionals
- Maintenance of credential integrity across borders
- Harmonised revocation and suspension recognition
- Interoperability between different national status management systems

## Lifecycle Status Types

The system supports various status types required for educational and professional credentials:
- **Active**: The credential is valid and can be trusted for all purposes
- **Suspended**: The credential is temporarily invalidated (may be restored)
- **Revoked**: The credential has been permanently invalidated (cannot be restored)
- **Expired**: The credential is no longer valid due to time limitations
- **Updated**: The credential has been replaced by a newer version

### Status Transition Rules

**From Active to Suspended**:
- Requires authorised institutional decision
- Must include reason code and expected resolution timeframe
- Can be reversed to Active status

**From Active to Revoked**:
- Requires authorised institutional decision with permanent effect
- Must include reason code and effective date
- Cannot be reversed (new credential issuance required)

**From Suspended to Active**:
- Requires resolution of suspension cause
- Must include verification of compliance restoration

**From Suspended to Revoked**:
- May occur if suspension issues cannot be resolved
- Follows same requirements as direct revocation

## Privacy-by-Design Principles

The system implements privacy-by-design through:
- Privacy-preserving status checking using unlinkable queries
- Data minimisation in status responses (only essential information disclosed)
- Unlinkability of verification requests to prevent tracking
- User control over credential usage and status disclosure
- Transparency about status information whilst protecting privacy
- Zero-knowledge proofs for status verification where technically feasible

## Regulatory Compliance

The lifecycle management system ensures compliance with:
- **eIDAS 2.0 requirements** for electronic attestation lifecycle management
- **GDPR data protection principles** in status tracking and verification
- **Member state-specific requirements** for suspension and revocation procedures
- **Sectoral regulations** governing educational and professional credential management
- **European quality assurance frameworks** for education and professional qualifications

## Technical Implementation Standards

Status management implementations must support:
- **W3C Verifiable Credentials** status checking mechanisms
- **StatusList2021** for efficient status communication
- **Cryptographic integrity** of all status updates
- **Interoperable protocols** for cross-border status verification
- **Real-time and batch processing** capabilities
- **Audit logging** with tamper-evident records