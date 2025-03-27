# Europass Digital Credentials (EDC) compliant with W3C Verifiable Credentials Data Model v1.1

## Introduction

The Europass Digital Credentials (EDC) framework leverages the W3C Verifiable Credentials Data Model (VCDM) version 1.1, ensuring interoperability, authenticity, and trustworthiness of digital educational credentials across Europe.

This document provides an overview of how the EDC instantiates and aligns with the VCDM v1.1, including illustrative JSON code examples updated to reflect compliance with the European Blockchain Services Infrastructure (EBSI) standards.

Europass Digital Credentials aligned with the W3C VCDM v1.1 and EBSI standards ensure credentials are secure, interoperable, and trusted across Europe. Institutions adopting EDC enhance credential issuance and verification, promoting mobility and transparency in European education and employment landscapes.

## Compliance with eIDAS Implementing Acts

To comply with the first batch of eIDAS implementing acts regarding supported data models for Verifiable Credentials, EDC credentials must be converted to W3C-VCDM v1.1. This conversion is guided by the European Blockchain Services Infrastructure (EBSI) initiative, with contributions from DG-EMPL, and provides a benchmark for interoperability across the EU.

## What is the W3C Verifiable Credentials Data Model v1.1?

The W3C Verifiable Credentials Data Model (VCDM) v1.1 is an internationally recognized standard defining digital credentials' structure, issuance, presentation, and verification securely, tamper-evidently, and privacy-preservingly.

Key aspects include:

- **Issuer**: Entity asserting claims about a subject.
- **Holder**: Individual or entity possessing the credential.
- **Verifier**: Entity validating credential authenticity and integrity.
- **Claims**: Assertions made about the credential subject.

## Europass Digital Credentials as W3C-VCDM Compliant Credentials

Europass Digital Credentials instantiate the W3C VCDM v1.1 by defining standardized JSON schemas, ensuring credentials are structured and machine-readable.

### Key Features

- **JSON Schema-based**: Credentials follow precise JSON schema definitions, ensuring interoperability.
- **Semantic Interoperability**: Common vocabularies ensure consistent interpretation.
- **Decentralisation**: Independent verification without centralised infrastructure.
- **Security and Privacy**: Cryptographic signatures and privacy-preserving techniques.

## Structure of Europass Digital Credentials (Aligned with EBSI standards)

### Context (`@context`)
```json
"@context": [
  "https://www.w3.org/2018/credentials/v1",
  "https://essif.europa.eu/schemas/vc-context/v1"
]
```

### Identifier (`id`)
```json
"id": "urn:uuid:123e4567-e89b-12d3-a456-426614174000"
```

### Type (`type`)
```json
"type": ["VerifiableCredential", "VerifiableAttestation", "EuropassCredential"]
```

### Issuer (`issuer`)
```json
"issuer": {
  "id": "did:ebsi:00001234abcd5678efgh9012",
  "name": "Example University"
}
```

### Issuance Date (`issuanceDate`)
```json
"issuanceDate": "2023-01-01T00:00:00Z"
```

### Credential Subject (`credentialSubject`)
```json
"credentialSubject": {
  "id": "did:ebsi:0987abcd6543efgh",
  "givenName": "Jane",
  "familyName": "Doe",
  "qualification": {
    "title": "Bachelor of Science",
    "field": "Computer Science"
  }
}
```

### Credential Schema (`credentialSchema`)
```json
"credentialSchema": {
  "id": "https://schema.ebsi.eu/education/diploma-v1",
  "type": "JsonSchemaValidator2018"
}
```

### Proof (`proof`)
```json
"proof": {
  "type": "Ed25519Signature2018",
  "created": "2023-01-01T00:00:00Z",
  "proofPurpose": "assertionMethod",
  "verificationMethod": "did:ebsi:00001234abcd5678efgh9012#keys-1",
  "jws": "eyJhbGciOiJFZERTQSJ9..signature"
}
```

## JSON Schemas and Repositories

The JSON schemas for EDC credentials compliant with VCDM v1.1 and aligned with EBSI standards are publicly accessible:

- [EBSI JSON Schemas for EDC](https://code.europa.eu/ebsi/json-schema/-/tree/main/schemas/vcdm1.1/europass/edc)

These schemas ensure credentials issued under Europass are:

- Technically interoperable
- Semantically accurate
- Cryptographically secure

## Benefits of Compliance

Compliance with W3C-VCDM v1.1 provides:

- **Trustworthiness**: Independent verification.
- **Portability**: Easy cross-border credential sharing.
- **Long-term Validity**: Adherence to international standards.
- **Privacy-by-design**: Supports selective disclosure, giving users control over their data.


