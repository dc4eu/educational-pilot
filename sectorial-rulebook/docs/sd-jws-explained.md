# Selective Disclosure with SD-JWT

## Introduction
Selective Disclosure JSON Web Tokens (**SD-JWT**) enable users to share only necessary data from a Verifiable Credential (VC), ensuring **privacy, data minimization, and compliance with GDPR and eIDAS 2.0**. This approach is essential in **education, professional qualifications, and digital identity verification**.

SD-JWT provides **secure, privacy-preserving verifiable credentials**, making it a critical component for **EUDI Wallets, education, and professional identity verification**. By implementing SD-JWT, organizations can enhance **trust, security, and interoperability** in digital identity ecosystems.

## Business Perspective
### Why SD-JWT Matters
- **Privacy-first**: Users share only required attributes.
- **GDPR & eIDAS Compliance**: Supports data minimization and consent-based disclosures.
- **Security**: Cryptographically verifiable credentials reduce fraud.
- **Interoperability**: Aligns with the European Digital Identity (**EUDI Wallet**) and Verifiable Credentials (**W3C-VC**).

### Use Cases
- **Higher Education**: Universities issue digital diplomas with selective disclosure.
- **Employment Verification**: Job applicants share only their degree, omitting birthdate.
- **Healthcare & Financial Services**: Users prove eligibility without revealing full personal details.

## Technical Perspective
### How SD-JWT Works
SD-JWT extends standard JWT by **hashing attributes** before disclosure.

1. **Issuer creates a Verifiable Credential (VC)**
2. **Hashes the claims** and stores them as `_sd` fields.
3. **Issues and signs the SD-JWT** using ES256 or EdDSA.
4. **Holder selectively discloses claims** to a verifier.
5. **Verifier validates the JWT** and checks disclosed values.

### SD-JWT Structure
```json
{
  "@context": ["https://www.w3.org/ns/credentials/v2"],
  "id": "9bcc9aaa-3bdc-4414-9450-739c295c752c",
  "type": ["VerifiableCredential", "StudentID"],
  "issuer": "did:ebsi:zvHWX359A3CvfJnCYaAiAde",
  "validFrom": "2023-01-01T00:00:00Z",
  "credentialSubject": {
    "id": "did:key:z2dmz...",
    "_sd": [
      "zSmImWHPJzQ7Rx8ZG0IYhUF1Ozj8f17wDKJGhxUkrdU",
      "T4RnDm1clVLCav2Mrsel6sNMz8pqGCeMrrp__YrV_-w"
    ],
    "student": true
  },
  "_sd_alg": "sha-256"
}
```

## Issuance & Presentation Lifecycle
### Issuance Flow
1. **Issuer creates Verifiable Credential (VC)** in JSON-LD.
2. **Hashes sensitive claims** and stores them in `_sd`.
3. **Signs SD-JWT** using DID-based signature.

### Presentation Flow
1. **Holder selects claims to disclose**.
2. **Constructs SD-JWT + Disclosures**.
3. **Verifier checks hash integrity** and validates the JWT signature.

### Example SD-JWT Format
```plaintext
<SD-JWT>~<Disclosure 1>~<Disclosure 2>~...~<Disclosure N>
```

## Code Example: Verifying an SD-JWT
```python
import hashlib
import base64

def verify_disclosure(disclosure, digest):
    computed_digest = hashlib.sha256(disclosure.encode()).digest()
    return base64.urlsafe_b64encode(computed_digest).decode('utf-8').rstrip('=') == digest
```

## Deployment on GitHub Pages
1. **Create a GitHub repository** named `sd-jwt-guide`.
2. **Enable GitHub Pages** via repository settings.
3. **Commit this `index.md` file** to the `main` branch.
4. **GitHub will generate a webpage** at `https://yourusername.github.io/sd-jwt-guide/`.




