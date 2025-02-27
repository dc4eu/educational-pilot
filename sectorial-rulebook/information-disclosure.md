# Information Disclosure

## Embeded Disclosure
## Selective Disclosure



# Selective Disclosure

## Overview

The system enables users to share only necessary credential data, meeting privacy requirements through advanced cryptographic techniques and carefully designed disclosure policies. This capability gives individuals control over their personal information while still enabling credential verification.

## Key Components

### Technical Implementations
- **SD-JWS** (Selective Disclosure for JSON Web Signatures)
- **SD-JWT** (Selective Disclosure for JSON Web Tokens)
- **BBS+** cryptography for zero-knowledge proofs
- Other privacy-preserving credential formats

### Issuer-Defined Disclosure Policies
- Guidelines for appropriate data sharing
- Minimum disclosure requirements
- Context-specific disclosure rules
- Privacy-protecting default settings

### Privacy-Preserving Verification Methods
- Zero-knowledge proof verification
- Minimal data disclosure protocols
- Unlinkable presentation techniques
- User-controlled attribute sharing

## Implementation Considerations

When implementing selective disclosure:
- Cryptographic implementations must follow current best practices
- User interfaces should make disclosure choices clear
- Default settings should minimise data sharing
- Technical performance should support efficient verification
- Fallback mechanisms should be available when needed

## Benefits

Selective disclosure provides:
- Enhanced privacy protection for credential holders
- Compliance with data minimisation principles
- Context-appropriate information sharing
- Prevention of unnecessary data collection
- User control over personal information

## Cross-Border Scenarios

For cross-border educational mobility, selective disclosure enables:
- Sharing only necessary qualification information
- Protection of sensitive personal data across jurisdictions
- Compliance with varied privacy requirements
- User control when interacting with foreign institutions

## Practical Applications

Selective disclosure supports scenarios such as:
- Proving degree attainment without revealing grades
- Confirming age requirements without revealing birth date
- Demonstrating institutional affiliation without full enrolment details
- Verifying specific skills without sharing entire educational history
- Proving professional qualifications without unnecessary personal data