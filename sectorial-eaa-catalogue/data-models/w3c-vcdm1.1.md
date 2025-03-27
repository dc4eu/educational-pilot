# W3C Verifiable Credentials Data Model (VCDM) v1.1 Overview

The **Verifiable Credentials Data Model (VCDM) v1.1** is a standard developed by the World Wide Web Consortium (W3C) designed for creating, exchanging, and verifying digital credentials securely, privately, and interoperably.

1st batch of eIDAS ammedment implementing acts recognised, together with mDL/CBOR, W3C-VCDM1.1 as supported dta models.



## What are Verifiable Credentials?

Verifiable Credentials (VCs) are tamper-evident digital credentials cryptographically signed by an issuer. They enable holders to securely and privately present trusted information to verifiers.



## Key Roles

- **Issuer:** Issues the credential to the holder (e.g., a university issuing digital diplomas).
- **Holder:** Controls the credential, typically a person or organisation that owns or manages the credentials.
- **Verifier:** Verifies the credential's authenticity and validity.



## Core Elements of VCDM

### 1. Credential
A set of claims made by an issuer. Example fields include:
- `@context`: Links to schema definitions (often JSON-LD).
- `id`: A unique identifier for the credential.
- `type`: Type of credential (e.g., "UniversityDegreeCredential").
- `issuer`: Identifies who issued the credential.
- `issuanceDate`: When the credential was issued.
- `credentialSubject`: Contains claims about the holder (e.g., name, degree awarded).

### 2. Presentation
How credentials are packaged and shared with verifiers.
- May contain multiple credentials.
- Includes proofs (cryptographic evidence).

### 3. Proof
Cryptographic evidence used to verify credentials.
- Typically digital signatures or zero-knowledge proofs.
- Ensures credential integrity and authenticity.



## Credential Formats

- **JSON-LD:** Recommended format, supports semantic interoperability.
- **JWT (JSON Web Token):** Compact format suitable for certain applications.



## Advantages

- **Interoperability:** Designed to work across different systems and platforms.
- **Privacy:** Holders control the sharing of their information.
- **Decentralisation:** Does not rely on centralised authorities.
- **Security:** Credentials are cryptographically protected against forgery or tampering.



## Use Cases

- Digital identity and personal documentation.
- Educational certificates and professional qualifications.
- Supply chain traceability and authenticity certificates.



## Example

```json
{
  "@context": [
    "https://www.w3.org/2018/credentials/v1",
    "https://www.w3.org/2018/credentials/examples/v1"
  ],
  "id": "http://example.edu/credentials/3732",
  "type": ["VerifiableCredential", "UniversityDegreeCredential"],
  "issuer": "https://example.edu/issuers/14",
  "issuanceDate": "2025-01-01T19:23:24Z",
  "credentialSubject": {
    "id": "did:example:123456789",
    "degree": {
      "type": "BachelorDegree",
      "name": "Bachelor of Science and Arts"
    }
  },
  "proof": {
    "type": "Ed25519Signature2018",
    "created": "2025-01-01T19:23:24Z",
    "proofPurpose": "assertionMethod",
    "verificationMethod": "https://example.edu/issuers/keys/1",
    "jws": "..."
  }
}
```



## Resources

- [Official W3C Specification](https://www.w3.org/TR/vc-data-model/)
- [GitHub Repository for Further Implementation Examples](https://github.com/w3c/vc-data-model)
