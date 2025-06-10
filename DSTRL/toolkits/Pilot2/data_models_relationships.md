# Relationship Model Between Entities in the DC4EU Ecosystem

## Introduction

The DC4EU (Digital Credentials for Europe) project within the eIDAS Large Scale Pilot programme establishes a hierarchical model of digital credentials that enables secure and interoperable verification of identity and academic achievements. This model is based on three main types of credentials that form a chain of trust.

## System Architecture

### 1. PID (Person Identification Data) - The Foundation Credential

The **PID** constitutes the foundation of the entire digital credentials ecosystem. It is the highest trust-level credential that establishes the legal identity of a natural person.

**Key characteristics:**
- Contains fundamental personal data such as given name, family name, date of birth, nationality, and address
- Includes a unique `document_number` that serves as the primary key
- Issued by governmental authorities with high security standards
- Has a clearly defined expiry date and issuing authority
- Complies with ISO standards for country codes (ISO 3166-1)

**Key fields for linkage:**
- `document_number`: Primary unique identifier
- `personal_administrative_number`: Unique personal administrative number
- Biometric and contact data for additional verification

### 2. EducationalID - The Bridging Credential (same applies to MyAcademicIDIssuer, MyAllianceID,ProfessionalIdCredential,DoctorIdCredential,EngineerIdCredential,EuropeanStudentCard)

The **EducationalID** acts as a bridge between legal identity (PID) and specific academic credentials.

**Linkage function:**
- **Connection to PID**: The `id` field of the EducationalID links to the `document_number` of the PID
- **Connection to academic credentials**: The `identifier` field (eduPersonPrincipalName) serves as the key to link with other credentials

**Educational context-specific characteristics:**
- Contains information specific to the educational context (affiliations, home organisation)
- Includes unique identifiers such as `schacPersonalUniqueCode` and `eduPersonPrincipalName`
- Defines the identity assurance level through `eduPersonAssurance`
- Allows for multiple simultaneous educational affiliations

### 3. Specific Academic Credentials - Verifiable Achievements

Credentials such as **Certificate of Enrolment** and other academic achievements are linked to the ecosystem through the EducationalID.

**Linkage mechanism:**
- The `id` field of the credential subject corresponds to the `identifier` of the EducationalID
- This enables tracing the achievement back to the original verified identity

## Verification Flow

### Issuance and Verification Process

1. **Base Identity Verification**
   - The citizen presents their PID issued by governmental authorities
   - The authenticity and validity of the document is verified

2. **EducationalID Issuance**
   - The educational institution verifies identity using the PID
   - The linkage is established: `EducationalID.id ↔ PID.document_number`
   - Unique educational identifiers are assigned

3. **Academic Credential Issuance**
   - Specific credentials are linked to the EducationalID
   - The relationship is established: `Credential.credentialSubject.id ↔ EducationalID.identifier`
   - Traceability to the original PID is maintained

### Chain of Trust

```
PID (Government) → EducationalID (Institution) → Academic Credentials (Institutions)
     ↓                    ↓                            ↓
Legal Identity    Educational Identity         Specific Achievements
```

## Benefits of the Model

### Security and Privacy
- **Context separation**: Governmental data is not directly exposed in academic credentials
- **Graduated verification**: Only necessary information can be verified according to context
- **Granular revocation**: Each level can be revoked independently

### Interoperability
- **Common standards**: Use of standardised JSON schemas and ISO codes
- **International compatibility**: Mutual recognition between European countries
- **Flexibility**: Allows for different types of academic credentials

### Operational Efficiency
- **Reusability**: The EducationalID can be used for multiple credentials
- **Automation**: Automatic verification of the chain of trust
- **Fraud reduction**: Cryptographic linking between levels

## Technical Considerations

### Identifier Management
- Identifiers must be unique and persistent over time
- Coordination between different systems and jurisdictions is required
- Migration from legacy systems must preserve existing linkages

### Privacy Aspects
- Implementation of selective disclosure techniques
- Data minimisation according to the principle of proportionality
- Compliance with GDPR and data protection regulations

## Conclusion

The relationship model between PID, EducationalID, and specific academic credentials in DC4EU represents a sophisticated approach to digital identity management in the educational domain. This hierarchical architecture ensures both the security and flexibility necessary for an interoperable and trustworthy European digital credentials ecosystem.
