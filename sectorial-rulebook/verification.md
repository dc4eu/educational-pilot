# Verification

## Overview

The verification process ensures credential validity while protecting privacy through a distributed system that avoids single points of failure. This approach balances security needs with privacy protection, preventing unnecessary monitoring of credential usage.

## Key Characteristics

### Distributed Verification
- Avoids single points of failure
- Distributes trust across the ecosystem
- Maintains system resilience
- Prevents centralised control

### Privacy Protection
- Shields from issuer monitoring
- Prevents tracking of credential usage
- Protects user privacy
- Implements data minimisation

### Time-based Validation
- Links validation to credential issuance
- Supports expiration mechanisms
- Enables time-bound credentials
- Maintains temporal relevance

## Verification Process

The verification process follows these steps:

1. **Secure Wallet Connection**
   - Establish secure channel with the wallet
   - Verify requester/issuer identity 
     - Use X.509v3 - clasical PKI - to verify if it is an issuer/RP/RPI authorised to interact with the EUDIW
     - Use DID - decentrilzed PKI - to verify educaitonal governance/entitlement
     - Use EAA catalogue to check embded disclosure entitlement - if applies
   - Verify proof of possession
   - Authenticate the verification request
   - Create encrypted communication

2. **Credential Request**
   - Request specific credentials
   - Specify required attributes
   - Indicate purpose of verification
   - Apply data minimisation

3. **Integrity Verification**
   - Check cryptographic signatures
   - Validate hash integrity
   - Verify digital proofs
   - Ensure credential hasn't been tampered with

4. **Metadata Checking**
   - Verify expiration dates
   - Check issuance dates
   - Validate credential type
   - Confirm appropriate usage context

5. **Issuer Verification**
   - Digital identifier validation
   - Educational accreditation checking
   - Accreditation issuer verification
   - Trust chain validation

6. **Identity Information Analysis**
   - Validate holder information
   - Check binding between credential and holder
   - Verify identity attributes when necessary
   - Apply appropriate identity assurance levels

7. **Schema Compliance Checking**
   - Verify credential structure
   - Validate against schema definitions
   - Check required fields
   - Ensure proper formatting

8. **EAA Catalogue Compliance Checking**
   - Verify ontology mandatory elements
   - Validate against sectorial catalogue definitions
   - Check required elements
   - Ensure proper formatting

9. **Quality Assurance Verification**
   - Issuer entitlement checking
   - Expiration verification
   - Status checking
   - Quality framework alignment

10. **Credential Status Verification**
   - Check for revocation and/or suspension
   - Verify revocation and/or suspension status
   - Validate current status
   - Confirm active status

11. **Record Keeping (evidences)**
    - Maintain audit records
    - Document verification results
    - Store minimal verification evidence
    - Support future audit needs

## Implementation Considerations

When implementing verification processes:
- Privacy protection should be built into all verification steps
- Verification should be efficient and responsive
- Error handling should be informative yet secure
- Technical performance should support large-scale verification
- Interoperability with different credential formats should be maintained

## Cross-Border Scenarios

For cross-border educational mobility, verification provides:
- Consistent validation across member states
- Recognition of credentials from different countries
- Support for qualification recognition
- Trust establishment across borders
