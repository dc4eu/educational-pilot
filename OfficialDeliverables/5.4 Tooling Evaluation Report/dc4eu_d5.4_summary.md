# DC4EU D5.4: Tooling Evaluation Report

## Overview

Within the Digital Credentials for Europe (DC4EU) large-scale pilot, Deliverable D5.4 represents a critical preparatory assessment conducted under Work Package 5 (WP5) - Education and Professional Qualifications. This deliverable provides a comprehensive evaluation of available tools and libraries required to integrate European Blockchain Services Infrastructure (EBSI) capabilities into the EUDI Wallet Reference Implementation (RI).

## Objective and Scope

The primary objective of D5.4 was to conduct a systematic analysis of tooling solutions capable of enabling EBSI-compliant credential workflows within the existing EUDI Wallet ecosystem. The evaluation focused on identifying libraries and frameworks that could support three core functionalities:

- **Requesting EBSI-compliant verifiable credentials** from issuers with onboarded DIDs
- **Organising acquired credentials** into verifiable presentations
- **Enabling secure sharing and verification** of credentials using EBSI-compliant processes

The report serves as the technical foundation for the subsequent development of the "Experimental EBSI Integration Prototype" (D5.5), establishing the architectural approach and tooling selection for implementing end-to-end issuance and verification workflows in compliance with EBSI standards.

## Technical Context and Requirements

The evaluation addressed specific architectural constraints imposed by the existing RI components:

### RI Wallet (Android/Kotlin)
- Required native Android plugin capabilities to preserve secure access to user private keys
- Needed integration with Android Keystore system for cryptographic operations
- Demanded EBSI-compliant DID resolution and verifiable presentation creation

### RI Issuer (Python/Flask)  
- Required external service integration due to absence of mature EBSI SDKs in Python
- Needed secure access to issuer PKI for credential signing operations
- Required REST API or RPC communication mechanisms for EBSI functionality

### RI Verifier (TypeScript/JavaScript)
- Positioned for direct integration with EBSI libraries due to language compatibility
- Required VP verification capabilities and DID resolution functionality
- Needed compliance with EBSI trust framework policies

## Evaluated Solutions

The report conducted comprehensive assessment of two primary tooling candidates:

### EBSI Hub Libraries

**Core Capabilities:**
- Comprehensive TypeScript-based suite specifically designed for EBSI ecosystem
- Full support for Decentralised Identifiers (DIDs) using `did:ebsi` and `did:key` methods
- W3C-compliant Verifiable Credentials support in both JSON-LD and JWT formats
- Advanced privacy features including selective disclosure and zero-knowledge proofs
- Robust cryptographic tools supporting Ed25519 and secp256k1 algorithms

**Evaluation Assessment:**
- **Strengths**: Purpose-built for EBSI, excellent standards compliance, comprehensive documentation
- **Integration**: Straightforward implementation within JavaScript/TypeScript environments
- **Interoperability**: Full compliance with W3C DID and VC standards ensuring cross-platform compatibility

### Walt.id Android SDK

**Core Capabilities:**
- Kotlin-native toolkit optimised for Android development environments  
- Multi-method DID support including `did:key`, `did:web`, and `did:ebsi`
- Built-in wallet functionality leveraging Android Keystore for secure storage
- Verifiable credential creation, signing, and verification capabilities
- Self-sovereign identity wallet features with user-centric control

**Evaluation Assessment:**
- **Strengths**: Native Android integration, hardware-backed security, modular design
- **Challenges**: Documentation gaps, particularly for EBSI pilot network configuration
- **Compatibility Issues**: Minor incompatibilities with EBSI verification services (e.g., missing required JWT fields)

## Key Findings and Recommendations

The evaluation revealed that both solutions offered viable pathways to EBSI compliance, albeit with distinct integration approaches:

### EBSI Hub Libraries
- **Recommended for**: RI Issuer and RI Verifier integration
- **Rationale**: Native JavaScript/TypeScript compatibility, comprehensive EBSI-specific functionality
- **Implementation approach**: Direct integration for verifier, microservice wrapper for issuer

### Walt.id Android SDK  
- **Recommended for**: RI Wallet integration with caveats
- **Challenges identified**: Documentation limitations, configuration complexity for EBSI pilot network
- **Mitigation strategy**: Direct engagement with Walt.id developers or fallback to EBSI Hub Libraries via Android-compatible wrapper

## Proposed Architecture

The report outlined a hybrid integration approach addressing the technical constraints of each RI component:

- **RI Issuer**: EBSI-Agent microservice (Node.js) exposing EBSI Hub Libraries via REST API
- **RI Wallet**: Native Kotlin plugin with preference for Walt.id SDK, fallback to EBSI Hub Libraries integration
- **RI Verifier**: Direct integration of EBSI Hub Libraries as JavaScript module

This architecture preserved component autonomy whilst enabling full EBSI compliance across the credential lifecycle.

## Significance and Impact

D5.4 established the technical foundation for EBSI integration within the EUDI Wallet ecosystem by:

- **Providing evidence-based tooling selection** through systematic evaluation
- **Identifying implementation pathways** that respect existing architectural constraints  
- **Establishing risk mitigation strategies** for identified integration challenges
- **Enabling informed decision-making** for the subsequent prototype development phase

## Future Work

The deliverable concluded with a pragmatic implementation plan for Task T5.5:

1. **Primary approach**: Exhaust possibilities of Walt.id SDK integration through direct developer engagement
2. **Fallback strategy**: Implement Android solution using EBSI Hub Libraries if primary approach proves unfeasible
3. **Timeline consideration**: Ensure sufficient flexibility to accommodate both approaches within project constraints

---

**For detailed technical specifications, comprehensive evaluation criteria, and complete architectural recommendations, please refer to the official deliverable:** [DC4EU D5.4 Tooling Evaluation Report](https://dm158x9fyyzgp.cloudfront.net/wp-content/uploads/2025/07/DC4EU_D5.4_Tooling_Evaluation_Report.pdf)