# DC4EU Task T5.5: EBSI Profile Integration in the EUDI Wallet Reference Implementation

## Overview

Within the large-scale pilot Digital Credentials for Europe (DC4EU), Work Package 5 (WP5) focuses on education and professional qualifications. Task T5.5 represents a critical technical milestone aimed at integrating experimental support for the European Blockchain Services Infrastructure (EBSI) into the Reference Implementation (RI) of the European Digital Identity (EUDI) Wallet.

## Task Objectives

The primary objective of Task T5.5 was to adapt and extend the existing EUDI Wallet Reference Implementation codebase to support credential workflows over the EBSI Trust Registry. This comprehensive integration effort encompassed all three principal actors in the credential ecosystem:

- **Issuer**: Enhanced to issue credentials that are both semantically and structurally valid within the EBSI context
- **Holder (Wallet)**: Enabled to request, receive, organise, and securely present EBSI-compliant credentials
- **Verifier**: Equipped to consume verifiable presentations and apply relevant EBSI trust framework policies for validation

The task focused on implementing EBSI-compliant mechanisms to enhance interoperability, security, and verifiability of credentials whilst adhering to W3C Verifiable Credentials and Decentralised Identifiers standards, alongside EBSI-specific requirements such as DID methods, credential schemas, trust registries, and revocation mechanisms.

## Implementation Challenges and Architectural Adaptation

The original architectural plan envisioned full native integration of EBSI capabilities directly within each RI component. However, the implementation team encountered several significant technical limitations:

- **SDK maturity issues**: The Walt.id Android SDK proved difficult to integrate due to inadequate documentation and compatibility problems
- **Cross-language compatibility constraints**: EBSI Hub Libraries (TypeScript/Node.js) couldn't be directly integrated into Python (Issuer) or Kotlin (Wallet/Verifier) environments
- **Component extensibility limitations**: RI components lacked sufficient plugin interfaces for external credential lifecycle logic

## Realised Solution

In response to these challenges, a more pragmatic, microservice-based architecture was adopted:

### EBSI-Agent Microservice
A dedicated Node.js service was developed to bridge the gap between RI components and EBSI Hub Libraries. This stateless service:
- Encapsulates all EBSI-specific logic (DID resolution, credential issuance, verification)
- Exposes functionality via REST APIs
- Maintains full EBSI compliance whilst enabling cross-language compatibility

### Component Integration Approach
- **RI Issuer**: Extended to delegate EBSI credential construction and signing to the EBSI-Agent whilst maintaining CBOR wrapping for RI Wallet compatibility
- **RI Wallet**: Functions as a secure transport mechanism, storing and presenting credentials without active EBSI validation
- **RI Verifier**: Enhanced to extract EBSI credentials from CBOR payloads and delegate final verification to the EBSI-Agent

## Technical Implementation

The prototype demonstrates a fully operational end-to-end credential flow using:

- **Real EBSI infrastructure**: DIDs onboarded to the EBSI Pilot Registry
- **Standards compliance**: Full adherence to W3C VC/DID standards and EBSI specifications  
- **Production-ready security**: Utilisation of registered Trusted Issuer status and cryptographic integrity
- **Interoperable architecture**: Modular design enabling future enhancements and broader trust framework integration

### Key Technical Components
1. **EBSI-Agent Service**: REST API wrapper for EBSI Hub Libraries
2. **Enhanced RI Issuer**: Python Flask application with EBSI delegation capabilities
3. **Modified RI Wallet**: Kotlin Android application with EBSI credential support
4. **Extended RI Verifier**: Backend with EBSI verification integration

## Results and Significance

The implementation successfully delivers:

- A functional prototype meeting core Task T5.5 objectives
- Full end-to-end EBSI-compliant credential workflows
- Demonstration of real-world DID usage with EBSI Pilot Registry
- A foundation for future deeper wallet integration and broader interoperability

Whilst the solution required architectural compromises from the original vision, it provides a pragmatic pathway toward EBSI-EUDI convergence and serves as a valuable reference for future specification development.

## Future Work

The prototype establishes groundwork for several advancement directions:
- Deeper native EBSI integration within RI components
- Broader interoperability testing across heterogeneous wallet implementations  
- Alignment with evolving EUDI Wallet specifications including multi-credential storage and selective disclosure
- Automation of DID onboarding and policy-driven credential governance

---

**For comprehensive technical details, implementation instructions, and complete architectural specifications, please refer to the official deliverable:** [DC4EU D5.6 Feedback and Refinement Report - Task T5.5 EBSI Profile Integration](DC4EU_DRAFT_D5.6%20Feedback%20and%20Refinement%20Report%20-%20v0.5.docx)