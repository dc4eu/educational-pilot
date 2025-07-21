# Pilot3 User Journeys Documentation

## Overview

**Pilot3** user journeys combine both **Pilot1** and **Pilot2** user experiences, allowing users to interact with both classical PKI and decentralised PKI systems. Users can access credentials and services through either trust model, depending on their needs and preferences.

## Foundation and Basis

Pilot3 user journeys are built upon the combination of both pilot approaches:

```
Pilot3 User Journeys = Pilot1 User Journeys + Pilot2 User Journeys
```

This means users can:
- Access services using **either** classical PKI or decentralised PKI authentication
- Obtain credentials in **both** SD-JWT and W3C Verifiable Credentials formats
- Verify credentials through **both** trust models
- Choose the most appropriate system for their specific use case

## Relationship with Pilot1 and Pilot2

### Pilot1 User Journey Component
- **Authentication**: Classical PKI certificate-based authentication
- **Credential Format**: SD-JWT with selective disclosure
- **Verification**: Hierarchical PKI trust chain validation
- **User Experience**: Traditional certificate-based interactions

### Pilot2 User Journey Component
- **Authentication**: DID-based decentralised identity
- **Credential Format**: W3C Verifiable Credentials
- **Verification**: Decentralised trust via EBSI
- **User Experience**: Self-sovereign identity principles

## User Experience Options

Pilot3 users have multiple pathways through the system:

### Option 1: Classical PKI Path (Pilot1)
Users can follow traditional PKI-based user journeys for:
- Certificate-based authentication
- SD-JWT credential issuance and verification
- Hierarchical trust validation

### Option 2: Decentralised PKI Path (Pilot2)
Users can utilise decentralised identity features for:
- DID-based authentication
- W3C Verifiable Credentials issuance and verification
- Distributed trust validation

### Option 3: Hybrid Usage
Users may switch between or combine both approaches based on:
- Specific use case requirements
- Verifier system capabilities
- Personal preferences
- Technical constraints

## Core User Journey Flows

Pilot3 supports all user journey flows from both pilots:

### From Pilot1
- PKI-based user onboarding and authentication
- SD-JWT credential request and issuance
- Certificate-based credential verification
- Cross-border PKI credential recognition

### From Pilot2
- DID-based user onboarding and identity management
- W3C VC credential request and issuance
- Decentralised credential verification
- EBSI-based cross-border credential recognition

## Related User Journey Documentation

For detailed user journey specifications, please refer to the individual pilot documentation:

### Pilot1 User Journey References
- [Pilot1 User Onboarding Process](./pilot1/user-onboarding.md)
- [Pilot1 Credential Issuance Journey](./pilot1/credential-issuance.md)
- [Pilot1 Credential Verification Process](./pilot1/credential-verification.md)
- [Pilot1 Cross-Border Recognition](./pilot1/cross-border-verification.md)

### Pilot2 User Journey References
- [Pilot2 DID-Based User Onboarding](./pilot2/user-onboarding.md)
- [Pilot2 W3C VC Issuance Process](./pilot2/credential-issuance.md)
- [Pilot2 Decentralised Verification](./pilot2/credential-verification.md)
- [Pilot2 EBSI Cross-Border Recognition](./pilot2/cross-border-verification.md)

### Specific DC4EU Use Cases
- [PID Retrieval Process](./pilot2/userjourneys/pid_retrieval.md)
- [Educational ID Issuance](./pilot2/userjourneys/educational_id_issuance.md)
- [Academic Achievement Issuance](./pilot2/userjourneys/academic_achievement_issuance.md)
- [EAA Verification Process](./pilot2/userjourneys/eaa_verification.md)

## Implementation Considerations

### User Choice and Flexibility
- Users can select their preferred trust model for each interaction
- Institutions should provide clear guidance on when to use each system
- Fallback mechanisms should be available if one system is unavailable

### System Integration
- Both systems should be accessible through unified interfaces where possible
- User accounts and preferences should be consistent across both systems
- Credential wallets should support both SD-JWT and W3C VC formats

## Additional Resources

- [User Journey Comparison Guide](./user-journey-comparison.md)
- [Trust Model Selection Guidelines](./trust-model-selection.md)
- [Credential Format Guide](./credential-formats.md)
- [Troubleshooting and Support](./troubleshooting-guide.md)


**Note**: Pilot3 does not create new user journey types. It provides access to both Pilot1 and Pilot2 user journeys within the same institutional environment. For comprehensive user journey details, please consult the individual pilot documentation linked above.