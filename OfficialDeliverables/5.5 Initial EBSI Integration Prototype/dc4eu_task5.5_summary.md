# EUDI Wallet EBSI Integration

## Overview

Task 5.5 of Work Package 5 (Education and Professional Qualifications) within the DC4EU large-scale pilot developed the necessary enhancements to enable the European Commission's EUDI Wallet Reference Implementation to support EBSI-compliant Verifiable Credentials (VCs). This work addressed the objective of implementing a complete end-to-end flow for issuing, holding, and verifying EBSI-trusted credentials using real DIDs onboarded into the EBSI Pilot Registry.

## Technical architecture

The implementation extends all three EUDI Wallet Reference Implementation components whilst maintaining compatibility with their original architecture and data exchange formats:

### Core components enhanced

- **EUDI Issuer** - Extended to delegate VC issuance to the EBSI-Agent and wrap the resulting token in the standard transport structure used by the RI Wallet
- **EUDI Android Wallet** - Enhanced with EBSI-aware credential verification support by parsing received credentials, conditionally invoking the EBSI-Agent, and enriching internal structures with verified metadata
- **EUDI Verifier Backend** - Extended to extract EBSI credentials from submitted payloads and invoke the EBSI-Agent for final trust validation after all local checks pass
- **EUDI Verifier Frontend** - Modified to align with the enhanced Verifier backend functionality

### EBSI-specific components

- **EBSI-Agent Service** - A standalone Node.js microservice exposing the EBSI Hub Libraries over a RESTful interface, handling DID creation/resolution, VC/VP issuance, and verification in a technology-agnostic way
- **Document Manager Extension** - Enhanced the RI Wallet's document lifecycle library with support for recognizing and processing EBSI credentials, including token extraction and data enrichment workflows
- **Wallet Core Extension** - Introduced coroutine-based support for remote credential verification, ensuring that asynchronous EBSI verification can be integrated with existing synchronous workflows

## Implementation approach

Due to language and tooling mismatches between the existing EUDI Wallet components and EBSI requirements, the EBSI functionality is encapsulated in a dedicated microservice architecture. This approach ensures:

- Seamless integration without disrupting existing EUDI Wallet functionality
- Technology-agnostic access to EBSI Hub Libraries
- Conditional EBSI logic that can be enabled or disabled as needed
- Compatibility with the original RI architecture and data exchange formats

## Supported operations

The enhanced implementation supports:

- **DID Management** - Creation and resolution of EBSI DIDs
- **Credential Issuance** - VC issuance using EBSI-compliant processes
- **Credential Verification** - VP verification with EBSI trust validation
- **Wallet Integration** - Seamless credential storage and presentation within the EUDI Wallet ecosystem

## Further information

For comprehensive technical documentation, component repositories, implementation guidance, and access to all enhanced components, please refer to the complete project documentation at:

**[EUDI-EBSI Educational Pilot](https://github.com/dc4eu/eudi-ebsi-educational-pilot)**

This repository serves as the central entry point for accessing all seven component repositories, technical specifications, and deployment instructions for the EBSI-enhanced EUDI Wallet implementation.