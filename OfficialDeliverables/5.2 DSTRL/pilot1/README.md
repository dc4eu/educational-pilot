# DSTRL Pilot1 - Classical PKI with SD-JWT

**Deployment and Testing Scenarios Results Library - Classical PKI Implementation**

Welcome to Pilot1 of the DC4EU Deployment and Testing Scenarios Results Library (DSTRL) project. This pilot demonstrates the implementation of digital educational credentials using traditional Public Key Infrastructure (PKI) with Selective Disclosure JSON Web Tokens (SD-JWT) for credential format.

## Overview

Pilot1 demonstrates two distinct approaches to digital credential implementation using Classical PKI infrastructure with Selective Disclosure JSON Web Tokens (SD-JWT). Through five institutional scenarios, this pilot reveals both **SaaS consortium models** (SUNET/SURF SaaS) and **sovereign national implementations** (Finnish DVV), providing educational institutions with multiple pathways to digital credentials whilst highlighting different governance and infrastructure strategies within European digital identity frameworks.

## Implementation Models Demonstrated

Pilot1 encompasses two distinctive implementation approaches within the Classical PKI framework:

### SUNET/SURF SaaS Model
**Participating institutions**: AUAS (Netherlands), DTU (Denmark), Ladok (Sweden), Sikt (Norway)
- **Infrastructure model**: Shared SaaS platform
- **Governance approach**: Multi-institutional consortium agreements  
- **Technical standardisation**: Uniform configurations across Nordic and Dutch institutions
- **Deployment complexity**: Simplified institutional requirements through centralised services

### Finnish National Sovereign Model  
**Participating institution**: OPH (Finnish National Agency for Education)
- **Infrastructure model**: National DVV (Digital and Population Data Services Agency) 
- **Governance approach**: National legislation-based (Acts 884/2017 and 906/2019)
- **Technical capabilities**: Full PID integration with direct authentic source connectivity
- **Deployment complexity**: Comprehensive national-scale infrastructure

Both models successfully demonstrate Classical PKI viability whilst revealing different strategic approaches to European digital credential adoption.

## Current Implementation Status

For comprehensive implementation progress across both the SUNET/SURF consortium and Finnish national model, including  certificate deployment status, and cross-border verification capabilities, please refer to the [**DC4EU Piloting Status Tracker**](../procedures/piloting/piloting-status-tracker.md).

**Key Implementation Insights**:
- **178 users onboarded** across both implementation models
- **571 credentials issued** demonstrating significant pilot scale
- **Two viable governance approaches** validated within Classical PKI framework
- **Cross-verifier compatibility** achieved (with technical adjustments required)

## Technical Architecture

### Core Components and Flow

#### Credential Issuance Journey
1. **User Authentication**: PKI certificate-based identity verification
2. **Authorisation Check**: Institutional database query for credential eligibility
3. **Data Retrieval**: Authentic source integration for credential attributes
4. **Credential Generation**: SD-JWT format credential creation
5. **Wallet Delivery**: Secure transfer to wwWallet application
6. **Storage Confirmation**: Verification of successful credential storage

### Credential Verification Journey
1. **Presentation Request**: Verifier initiates credential request
2. **Selective Disclosure**: User selects information to share
3. **Credential Presentation**: SD-JWT credential transmitted
4. **Signature Verification**: PKI-based authenticity validation
5. **Trust Chain Validation**: Certificate authority verification
6. **Decision Response**: Accept/reject determination

## Strengths and Capabilities

### Established Infrastructure Leverage
- **Familiar Technology**: Builds on well-understood PKI principles
- **Existing Investments**: Utilises current certificate infrastructure
- **Proven Security**: Time-tested cryptographic mechanisms
- **Regulatory Compliance**: Alignment with eIDAS 1.0 frameworks

### Model-Specific Capabilities

#### SaaS Consortium Strengths (SUNET/SURF)
- **Rapid deployment**: Simplified institutional onboarding through shared infrastructure
- **Technical consistency**: Standardised configurations across multiple countries
- **Resource efficiency**: Reduced individual institutional technical requirements
- **Cross-border coordination**: Demonstrated Nordic-Dutch collaboration model

#### National Sovereign Strengths (Finnish DVV)
- **Production readiness**: Full integration with national education registries (KOSKI, VIRTA)
- **Comprehensive coverage**: PID integration alongside educational credentials
- **Authentic source connectivity**: Real-time access to official educational databases
- **National compliance**: Full alignment with Finnish legal frameworks

### Selective Disclosure Benefits
- **Privacy Protection**: Minimal data sharing capabilities
- **GDPR Compliance**: Data minimisation and consent mechanisms
- **Flexible Presentation**: Context-appropriate information sharing
- **User Control**: Individual control over personal data disclosure

## Current Limitations and Considerations

### Universal Classical PKI Constraints

Both implementation models encountered shared limitations inherent to Classical PKI approaches:

**Relying Party Infrastructure Gaps**
- **RP certificate absence**: Universal limitation preventing full cross-border verification testing
- **Trust chain validation**: Incomplete PKI infrastructure limiting verification scope to integrity checks
- **Cross-border interoperability**: Requires bilateral trust agreements and enhanced infrastructure

### Model-Specific Limitations

#### SUNET/SURF SaaS Model
- **Test environment constraints**: Limited authentic source integration in pilot environments
- **Scalability dependencies**: Reliant on consortium coordination for infrastructure scaling
- **Limited lifecycle management**: No credential revocation or suspension capabilities implemented

#### Finnish National Model (DVV)
- **Standards alignment**: Credential structure differences requiring manual adjustments for DC4EU compatibility
- **Manual processes**: Certificate sealing requires manual intervention limiting automation
- **Interoperability gaps**: Attribute naming mismatches with European standards (e.g., "givenName.und" vs "givenName")
- **Limited lifecycle management**: No credential revocation or suspension capabilities implemented

### Strategic Implications

These findings suggest that **hybrid approaches** combining national sovereignty with European interoperability standards offer the most promising pathway for production deployment.

### Lifecycle Management
**Limited Credential Lifecycle Features**
- Revocation mechanisms not fully implemented in pilot
- Suspension capabilities require additional PKI infrastructure
- Real-time status checking depends on CRL/OCSP availability

## Directory Structure

### Infrastructure Documentation (`/infrastructure`)
- PKI implementation guidelines and requirements
- Certificate management procedures and best practices
- Integration specifications for institutional systems
- Security configuration and operational guidance

### Piloting Agent Scenarios (`/PAs`)
- **Comprehensive implementation analysis** comparing federated consortium (SUNET/SURF) and national sovereign (Finnish DVV) approaches
- **Detailed scenario documentation** from five institutions across Nordic, Dutch, and Finnish educational systems  
- **Comparative technical insights** highlighting infrastructure diversity within Classical PKI framework
- **User journey outcomes** and verification testing results across both implementation models
- **Strategic recommendations** for European digital credential adoption pathways

### User Journey Documentation (`/userjourneys`)
- Step-by-step credential issuance processes
- Verification workflow specifications
- User experience guidance and recommendations
- Error handling and troubleshooting procedures

## Getting Started with Pilot1

### For Educational Institutions

#### Assessment and Planning
1. **Infrastructure Assessment**: Evaluate existing PKI capabilities and institutional requirements
2. **Governance Model Selection**: Determine alignment with consortium or national approaches
3. **Implementation model selection**: Choose between federated consortium approach (SUNET/SURF model) or national sovereign implementation (Finnish DVV model) based on:
   - **Institutional requirements**: Technical capacity and resource availability
   - **Governance preferences**: Consortium agreements vs national legislation compliance
   - **Integration complexity**: SaaS simplicity vs comprehensive authentic source connectivity
   - **Strategic objectives**: Rapid deployment vs production-ready national infrastructure

## Strategic Insights and Recommendations

### Validated Implementation Pathways

Pilot1 demonstrates that **Classical PKI remains viable** for European digital credential deployment through two distinct but equally valid approaches:

**SaaS Model**: Enables rapid, coordinated deployment across multiple institutions and countries through shared infrastructure, suitable for institutions seeking simplified technical requirements and proven cross-border collaboration.

**National Sovereign Model**: Provides comprehensive, production-ready infrastructure with full authentic source integration, suitable for national agencies requiring complete control and regulatory compliance.

### Critical Success Factors

1. **Standards harmonisation**: Essential for European interoperability regardless of implementation model
2. **RP infrastructure development**: Universal requirement for enhanced cross-border verification capabilities  
3. **Governance flexibility**: Supporting both consortium and national approaches accommodates diverse institutional needs
4. **Hybrid strategy readiness**: Classical PKI provides foundation for eventual integration with decentralised approaches (Pilot2)

### Production Deployment Considerations

The diversity of successful implementation models within Pilot1 validates the **flexibility required for pan-European adoption** whilst highlighting **standardisation needs** for seamless interoperability across different governance and infrastructure approaches.

---

*For detailed scenario analysis and comparative technical insights, refer to [Pilot1 Participating Agent Scenarios](./PAs/README.md).*