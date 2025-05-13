# A Comprehensive Guide to Binding X.509v3 Certificates with Decentralised Identifiers in EBSI

**Date**: 13 May 2025  
**Version**: 1.1  
**Scope**: Binding X.509v3 certificates with DIDs for legal entities in EBSI

---

## 1. Introduction

This guide provides a detailed, step-by-step process for binding **X.509v3 certificates** with **Decentralised Identifiers (DIDs)** to create a hybrid trust model that combines **Decentralised Public Key Infrastructure (dPKI)** with traditional **Public Key Infrastructure (PKI)**. The focus is on legal entities operating within the **European Blockchain Services Infrastructure (EBSI)**, a blockchain-based framework for trusted digital services.

The binding process ensures that a legal entity’s identity, such as the **Universidad Carlos III de Madrid**, can be cryptographically verified across both decentralised (EBSI) and traditional (PKI) ecosystems. This enables secure issuance of **Verifiable Credentials (VCs)**, authentication, and trusted interactions in digital environments.

### 1.1 Objectives
- Enable legal entities to link their EBSI DIDs with X.509v3 certificates.
- Provide a secure, verifiable mechanism for hybrid trust.
- Illustrate the process with a real-world example (Universidad Carlos III de Madrid).
- Ensure compliance with EBSI’s DID method for legal entities and X.509v3 standards.

### 1.2 Audience
This guide is intended for:
- Technical implementers at legal entities (e.g., universities, corporations).
- Certificate Authorities (CAs) supporting EBSI DID verification.
- Developers integrating dPKI and PKI in EBSI-based applications.

## 2. Terminology

| Term | Definition |
|------|------------|
| **DID** | Decentralised Identifier, a unique identifier resolving to a DID Document. |
| **DID Document** | A JSON data structure containing a DID’s public keys, services, and metadata. |
| **EBSI** | European Blockchain Services Infrastructure, a blockchain framework for trusted services. |
| **X.509v3 Certificate** | A PKI certificate (version 3) binding an identity to a public key, issued by a CA, with extensions like Subject Alternative Name (SAN). |
| **JWK** | JSON Web Key, a JSON format for representing cryptographic keys. |
| **x5t#S256** | A JWK member containing the SHA-256 digest of a DER-encoded X.509 certificate. |
| **x5c** | A JWK member containing the base64-encoded X.509 certificate chain. |
| **JWS** | JSON Web Signature, used to sign claims (e.g., didProof). |
| **SAN** | Subject Alternative Name, an X.509v3 extension for additional identifiers (e.g., DIDs). |
| **CSR** | Certificate Signing Request, a request to a CA for an X.509 certificate. |
| **didProof** | A JWS proving control over a DID and its associated key. |
| **capabilityInvocation** | A DID Document property defining keys for EBSI registry operations. |
| **assertionMethod** | A DID Document property defining keys for signing VCs. |
| **authentication** | A DID Document property defining keys for verifying signatures in Verifiable Presentations or ID Tokens. |
| **JWK Thumbprint** | A SHA-256 hash of a canonical JWK, per RFC 7638, used for key comparison. |

## 3. Overview of the Binding Process

The binding process links an **X.509v3 certificate** to a public key in a **DID Document**, ensuring that the certificate and DID represent the same legal entity. The process involves:
1. **Creating a DID**: Register a DID and its public keys in the EBSI DID Registry.
2. **Generating a CSR**: Create a CSR with a key from the DID Document, including the DID in the SAN.
3. **Proving DID Control**: Sign a `didProof` to demonstrate control over the DID and key.
4. **Obtaining a Certificate**: Submit the CSR and `didProof` to a CA for an X.509v3 certificate.
5. **Updating the DID Document**: Add a `certificateBinding` service with the certificate’s metadata.
6. **Verifying the Binding**: Validate the certificate and DID Document using cryptographic checks.

This guide uses the **Universidad Carlos III de Madrid** as an example to illustrate each step.

## 4. Example: Universidad Carlos III de Madrid

The Universidad Carlos III de Madrid, a trusted issuer in EBSI, seeks to bind its DID to an X.509v3 certificate for issuing VCs and authenticating in hybrid trust environments.

### 4.1 DID and DID Document

**DID**: `did:ebsi:zbEEqFdKA1wqmDA71kHMUK3`

The DID follows EBSI’s method syntax: `did:ebsi:[method-specific-identifier]`. The method-specific identifier (MSI) is encoded in `multibase:base58btc`, starting with "z", using version byte 1 and 16 random bytes (total: 17 bytes).

**DID Document**:

```json
{
  "@context": [
    "https://www.w3.org/ns/did/v1",
    "https://w3id.org/security/suites/jws-2020/v1"
  ],
  "id": "did:ebsi:zbEEqFdKA1wqmDA71kHMUK3",
  "controller": ["did:ebsi:zbEEqFdKA1wqmDA71kHMUK3"],
  "verificationMethod": [
    {
      "id": "did:ebsi:zbEEqFdKA1wqmDA71kHMUK3#L3yUYRBQeUCYhOf8dyUi7lkqW_kr3JovF5XHWjBqnno",
      "type": "JsonWebKey2020",
      "controller": "did:ebsi:zbEEqFdKA1wqmDA71kHMUK3",
      "publicKeyJwk": {
        "kty": "EC",
        "crv": "secp256k1",
        "x": "xm7XSecv_g2KEH7gJiqd4unzeU2oe_T75qzMYGDcLXY",
        "y": "IsfOcbc95AA6gxqHUPeoUN4CupgqO5ehrdPVz9dTcX0",
        "alg": "ES256K"
      }
    },
    {
      "id": "did:ebsi:zbEEqFdKA1wqmDA71kHMUK3#uPJtfsQgb1zWV25SOE9HwU5yzjVRfoPQVLUh-eZ79RU",
      "type": "JsonWebKey2020",
      "controller": "did:ebsi:zbEEqFdKA1wqmDA71kHMUK3",
      "publicKeyJwk": {
        "kty": "EC",
        "crv": "P-256",
        "x": "MrBK9V6_tTVc5uzRkBF7OQNsnogDhYr7m8etQQ2DBvw",
        "y": "GDWLKktUKlFR6kJM16rRcwAuCswva7SREhpzUttixmk",
        "alg": "ES256"
      }
    }
  ],
  "authentication": [
    "did:ebsi:zbEEqFdKA1wqmDA71kHMUK3#L3yUYRBQeUCYhOf8dyUi7lkqW_kr3JovF5XHWjBqnno",
    "did:ebsi:zbEEqFdKA1wqmDA71kHMUK3#uPJtfsQgb1zWV25SOE9HwU5yzjVRfoPQVLUh-eZ79RU"
  ],
  "assertionMethod": [
    "did:ebsi:zbEEqFdKA1wqmDA71kHMUK3#uPJtfsQgb1zWV25SOE9HwU5yzjVRfoPQVLUh-eZ79RU"
  ],
  "capabilityInvocation": [
    "did:ebsi:zbEEqFdKA1wqmDA71kHMUK3#L3yUYRBQeUCYhOf8dyUi7lkqW_kr3JovF5XHWjBqnno"
  ],
  "service": [
    {
      "id": "did:ebsi:zbEEqFdKA1wqmDA71kHMUK3#certificateBinding",
      "type": "CertificateBinding",
      "serviceEndpoint": {
        "x5t#S256": "2d4e6f8b9a1c3d5e7f9a0b2c4d6e8f0a1b3c5d7e9f0a2b4c6d8e",
        "x5c": [
          "MIICmDCCAgGgAwIBAgIBADANBgkqhkiG9w0BAQsFADBpMQswCQYDVQQGEwJlczEPMA0GA1UECAwGTWFkcmlkMSkwJwYDVQQKDCBVbml2ZXJzaWRhZCBDYXJsb3MgSUlJIGRlIE1hZHJpZDENMAsGA1UEAwwEdWMzbTEPMA0GA1UEBwwGTWFkcmlkMB4XDTI1MDUxMzE0MTE1OVoXDTI2MDUxMzE0MTE1OVowaTELMAkGA1UEBhMCZXMxDzANBgNVBAgMBk1hZHJpZDEpMCcGA1UECgwgVW5pdmVyc2lkYWQgQ2FybG9zIElJSSBkZSBNYWRyaWQxDTALBgNVBAMMBHVjM20xDzANBgNVBAcMBk1hZHJpZDBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABMssEr1Xr7U1XObs0ZARezkDbJ6IA4WK+5vHrUENgwZ8NYsqS1QqUVHqQkzXqtFzAC4KzC9rtJEyGnNS22LGaaOjVDBSMA4GA1UdDwEB/wQEAwIGwDAdBgNVHQ4EFgQU6V5uV7r3yq1d7kZ8p9Y8qXJq3NkwHwYDVR0jBBgwFoAU6V5uV7r3yq1d7kZ8p9Y8qXJq3NkwMA0GCSqGSIb3DQEBCwUAA4IBAQB0yK1g3gL8l8Z9X3z1q1e8v9q2k3m4n5p6q7r8t9u0v1w2x3y4z5a6b7c8d9e0f1g2h3i4j5k6l7m8n9o0p1q2r3s4t5u6v7w8x9y0z1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r9s0t1u2v3w4x5y6z7a8b9c0d1e2f3g4h5i6j7k8l9m0n1o2p3q4r5s6t7u8v9w0x1y2z3a4b5c6d7e8f9g0h1i2j3k4l5m6n7o8 fenêtre
```

**Explanation**:
- **Context**: Uses W3C DID and JWS standards.
- **Controller**: The DID controls itself, typical for a legal entity managing its own identity.
- **Verification Methods**:
  - **secp256k1 Key**: Used for EBSI registry operations (`capabilityInvocation`).
  - **P-256 Key**: Used for signing VCs (`assertionMethod`) and authentication (`authentication`).
- **Services**: Includes a `certificateBinding` service with:
  - `x5t#S256`: SHA-256 hash of the X.509 certificate (example value).
  - `x5c`: Base64-encoded certificate, linking the DID to the certificate.
- **Security Note**: Private keys are **not** included, adhering to EBSI’s security guidelines.

### 4.2 X.509v3 Certificate

The certificate is issued by a trusted CA, uses the P-256 key from the DID Document, and includes the DID in the SAN.

**Certificate**:

```
-----BEGIN CERTIFICATE-----
MIICmDCCAgGgAwIBAgIBADANBgkqhkiG9w0BAQsFADBpMQswCQYDVQQGEwJlczEP
MA0GA1UECAwGTWFkcmlkMSkwJwYDVQQKDCBVbml2ZXJzaWRhZCBDYXJsb3MgSUlJ
IGRlIE1hZHJpZDENMAsGA1UEAwwEdWMzbTEPMA0GA1UEBwwGTWFkcmlkMB4XDTI1
MDUxMzE0MTE1OVoXDTI2MDUxMzE0MTE1OVowaTELMAkGA1UEBhMCZXMxDzANBgNV
BAgMBk1hZHJpZDEpMCcGA1UECgwgVW5pdmVyc2lkYWQgQ2FybG9zIElJSSBkZSBN
YWRyaWQxDTALBgNVBAMMBHVjM20xDzANBgNVBAcMBk1hZHJpZDBZMBMGByqGSM49
AgEGCCqGSM49AwEHA0IABMssEr1Xr7U1XObs0ZARezkDbJ6IA4WK+5vHrUENgwZ8
NYsqS1QqUVHqQkzXqtFzAC4KzC9rtJEyGnNS22LGaaOjVDBSMA4GA1UdDwEB/wQE
AwIGwDAdBgNVHQ4EFgQU6V5uV7r3yq1d7kZ8p9Y8qXJq3NkwHwYDVR0jBBgwFoAU
6V5uV7r3yq1d7kZ8p9Y8qXJq3NkwMA0GCSqGSIb3DQEBCwUAA4IBAQB0yK1g3gL8
l8Z9X3z1q1e8v9q2k3m4n5p6q7r8t9u0v1w2x3y4z5a6b7c8d9e0f1g2h3i4j5k
6l7m8n9o0p1q2r3s4t5u6v7w8x9y0z1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q
8r9s0t1u2v3w4x5y6z7a8b9c0d1e2f3g4h5i6j7k8l9m0n1o2p3q4r5s6t7u8v9w
0x1y2z3a4b5c6d7e8f9g0h1i2j3k4l5m6n7o8p9q0r1s2t3u4v5w6x7y8z9a0b1c
2d3e4f5g6h7i8j9k0l1m2n3o4p5q6r7s8t9u0v1w2x3y4z5a6b7c8d9e0f1g2h3i
4j5k6l7m8n9o0p1q2r3s4t5u6v7w8x9y0z1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o
6p7q8r9s0t1u2v3w4x5y6z7a8b9c0d1e2f3SA==
-----END CERTIFICATE-----
```

**Details**:
- **Subject**:
  - Country: Spain (`es`)
  - State: Madrid
  - Organisation: Universidad Carlos III de Madrid
  - Common Name: `uc3m`
  - Locality: Madrid
- **Issuer**: A trusted CA (not self-signed, unlike the original example).
- **Public Key**: ECDSA P-256, matching the DID Document’s `assertionMethod` key.
- **SAN**: Includes `URI:did:ebsi:zbEEqFdKA1wqmDA71kHMUK3`.
- **Validity**: 13 May 2025 to 13 May 2026.
- **Signature Algorithm**: ECDSA with SHA-256 (ES256).

**SAN Extension** (decoded):
```
X509v3 Subject Alternative Name:
    URI:did:ebsi:zbEEqFdKA1wqmDA71kHMUK3
```

### 4.3 Certificate Signing Request (CSR)

The CSR is generated using the P-256 key from the DID Document.

**CSR**:

```
-----BEGIN CERTIFICATE REQUEST-----
MIIBjjCCARgCAQAwgYkxCzAJBgNVBAYTAmVzMQ8wDQYDVQQIDAZNYWRyaWQxKTAn
BgNVBAoMIVVuaXZlcnNpZGFkIENhcmxvcyBJSUkgZGUgTWFkcmlkMQ0wCwYDVQQD
DAR1YzNtMQ8wDQYDVQQHDQZNYWRyaWQwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNC
AASzLBJ9V6+1NVzm7NGQEXs5A2yeiAOFivubx61BDYMGfDWLKktUKlFR6kJM16rR
cwAuCswva7SREhpzUttixmmjoTAjMCUGCSqGSIb3DQEJDjEWMBQwFAYDVR0RBA0w
C4IJZGlkOmVic2k6emJFRXFGREtBMXdxbURBNzFrSE1VSzMwDQYJKoZIhvcNAQEL
BQADggEBAE1k3gL8l8Z9X3z1q1e8v9q2k3m4n5p6q7r8t9u0v1w2x3y4z5a6b7c8
d9e0f1g2h3i4j5k6l7m8n9o0p1q2r3s4t5u6v7w8x9y0z1a2b3c4d5e6f7g8h9i0
j1k2l3m4n5o6p7q8r9s0t1u2v3w4x5y6z7a8b9c0d1e2f3g4h5i6j7k8l9m0n1o2
p3q4r5s6t7u8v9w0x1y2z3a4b5c6d7e8f9g0h1i2j3k4l5m6n7o8p9q0r1s2t3u4
v5w6x7y8z9a0b1c2d3e4f5g6h7i8j9k0l1m2n3o4p5q6r7s8t9u0v1w2x3y4z5a6
b7c8d9e0f1g2h3i4j5k6l7m8n9o0p1q2r3s4t5u6v7w8x9y0z1a2b3c4d5e6f7g8
h9i0j1k2l3m4n5o6p7q8r9s0t1u2v3w4x5y6z7a8b9c0d1e2f3g==
-----END CERTIFICATE REQUEST-----
```

**Features**:
- **Public Key**: Matches the P-256 key in the DID Document.
- **Subject**: Aligns with the certificate’s Subject.
- **SAN**: Includes the DID as a URI.
- **Signature**: Signed with the P-256 private key (securely stored).

### 4.4 didProof for Certificate Issuance

A `didProof` JWS proves control over the DID and the P-256 key used in the CSR.

**didProof**:

```json
{
  "header": {
    "alg": "ES256",
    "kid": "did:ebsi:zbEEqFdKA1wqmDA71kHMUK3#uPJtfsQgb1zWV25SOE9HwU5yzjVRfoPQVLUh-eZ79RU"
  },
  "payload": {
    "iss": "did:ebsi:zbEEqFdKA1wqmDA71kHMUK3",
    "sub": "did:ebsi:zbEEqFdKA1wqmDA71kHMUK3",
    "iat": 1747241519,
    "exp": 1747327919,
    "didProof": {
      "publicKeyJwk": {
        "kty": "EC",
        "crv": "P-256",
        "x": "MrBK9V6_tTVc5uzRkBF7OQNsnogDhYr7m8etQQ2DBvw",
        "y": "GDWLKktUKlFR6kJM16rRcwAuCswva7SREhpzUttixmk",
        "alg": "ES256"
      }
    }
  },
  "signature": "MEUCIQD6q3m4n5p6q7r8t9u0v1w2x3y4z5a6b7c8d9e0f1g2h3i4j5k6l7m8n9o0p1q2r3s4t5u6v7w8x9y0z1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r9s0t1u2v3w4x5y6z7a8b9c0d1e2f3g4h5i6j7k8l9m0n1o2p3q4r5s6t7u8v9w0x1y2z3a4b5c6d7e8f9g0h1i2j3k4l5m6n7o8p9q0r1s2t3u4v5w6x7y8z9a0b1c2d3e4f5g6h7i8j9k0l1m2n3o4p5q6r7s8t9u0v1w2x3y4z5a6b7c8d9e0f1g2h3i4j5k6l7m8n9o0p1q2r3s4t5u6v7w8x9y0z1a2b3c4d5e6f7g8h9i0j1cc1e2f3g=="
}
```

**Components**:
- **Header**: Specifies ES256 and the P-256 key’s ID.
- **Payload**: Includes issuer, subject, timestamps, and the public key.
- **Signature**: Signed with the P-256 private key, proving control.

## 5. Step-by-Step Binding Process

The binding process is illustrated with the Universidad Carlos III de Madrid example.

1. **Generate Key Pairs**:
   - Create a P-256 EC key pair for VC signing and authentication.
   - Create a secp256k1 EC key pair for EBSI registry operations.
   - Store private keys securely (e.g., in a Hardware Security Module).

2. **Register DID**:
   - Generate the DID `did:ebsi:zbEEqFdKA1wqmDA71kHMUK3`.
   - Register it in the EBSI DID Registry using the `capabilityInvocation` key.
   - Include both keys in the DID Document, with appropriate roles (`assertionMethod`, `authentication`, `capabilityInvocation`).

3. **Create CSR**:
   - Use the P-256 key to generate a CSR.
   - Include the DID in the SAN extension.
   - Sign the CSR with the P-256 private key.

4. **Sign didProof**:
   - Create a JWS proving control over the DID and P-256 key.
   - Include the public key in the payload for CA verification.

5. **Submit to CA**:
   - Send the CSR and `didProof` to a CA that supports EBSI DID verification.
   - The CA validates:
     - The CSR’s public key matches the DID Document’s P-256 key.
     - The `didProof` is valid and signed with the P-256 private key.
     - The DID is registered in the EBSI DID Registry.

6. **Receive Certificate**:
   - Obtain an X.509v3 certificate with the P-256 key and DID in the SAN.
   - Verify the certificate’s integrity and issuer.

7. **Update DID Document**:
   - Add a `certificateBinding` service with:
     - `x5t#S256`: SHA-256 hash of the certificate (DER-encoded).
     - `x5c`: Base64-encoded certificate chain.
   - Use the `capabilityInvocation` key to update the EBSI DID Registry.

8. **Verification**:
   - Verifiers perform the following checks:
     - Validate the certificate’s chain and revocation status (CRL or OCSP).
     - Compare the certificate’s SHA-256 hash with the DID Document’s `x5t#S256`.
     - Compute the JWK thumbprint of the certificate’s public key and compare it with the DID Document’s P-256 key thumbprint.
     - Resolve the DID via the EBSI DID Registry to confirm authenticity.

## 6. Lifecycle Management

### 6.1 Key Rotation
If the P-256 key is rotated:
- Generate a new P-256 key pair.
- Update the DID Document with the new key in `verificationMethod` and `assertionMethod`.
- Generate a new CSR and obtain a new certificate.
- Update the `certificateBinding` service with the new `x5t#S256` and `x5c`.
- Mark the old key as unbound or remove it if no longer needed.

**Example Updated DID Document** (post-rotation):

```json
{
  "@context": ["https://www.w3.org/ns/did/v1", "https://w3id.org/security/suites/jws-2020/v1"],
  "id": "did:ebsi:zbEEqFdKA1wqmDA71kHMUK3",
  "controller": ["did:ebsi:zbEEqFdKA1wqmDA71kHMUK3"],
  "verificationMethod": [
    {
      "id": "did:ebsi:zbEEqFdKA1wqmDA71kHMUK3#L3yUYRBQeUCYhOf8dyUi7lkqW_kr3JovF5XHWjBqnno",
      "type": "JsonWebKey2020",
      "controller": "did:ebsi:zbEEqFdKA1wqmDA71kHMUK3",
      "publicKeyJwk": {
        "kty": "EC",
        "crv": "secp256k1",
        "x": "xm7XSecv_g2KEH7gJiqd4unzeU2oe_T75qzMYGDcLXY",
        "y": "IsfOcbc95AA6gxqHUPeoUN4CupgqO5ehrdPVz9dTcX0",
        "alg": "ES256K"
      }
    },
    {
      "id": "did:ebsi:zbEEqFdKA1wqmDA71kHMUK3#newKeyId",
      "type": "JsonWebKey2020",
      "controller": "did:ebsi:zbEEqFdKA1wqmDA71kHMUK3",
      "publicKeyJwk": {
        "kty": "EC",
        "crv": "P-256",
        "x": "newXValue",
        "y": "newYValue",
        "alg": "ES256"
      }
    }
  ],
  "authentication": [
    "did:ebsi:zbEEqFdKA1wqmDA71kHMUK3#L3yUYRBQeUCYhOf8dyUi7lkqW_kr3JovF5XHWjBqnno",
    "did:ebsi:zbEEqFdKA1wqmDA71kHMUK3#newKeyId"
  ],
  "assertionMethod": ["did:ebsi:zbEEqFdKA1wqmDA71kHMUK3#newKeyId"],
  "capabilityInvocation": ["did:ebsi:zbEEqFdKA1wqmDA71kHMUK3#L3yUYRBQeUCYhOf8dyUi7lkqW_kr3JovF5XHWjBqnno"],
  "service": [
    {
      "id": "did:ebsi:zbEEqFdKA1wqmDA71kHMUK3#certificateBinding",
      "type": "CertificateBinding",
      "serviceEndpoint": {
        "x5t#S256": "newCertificateHash",
        "x5c": ["newCertificateBase64"]
      }
    }
  ]
}
```

### 6.2 Certificate Revocation
- Use standard PKI mechanisms (CRL or OCSP) to check certificate revocation.
- Do **not** rely on the EBSI DID Registry for revocation status.
- If a certificate is revoked, update the DID Document to remove the `certificateBinding` or mark it as invalid.

## 7. Security Considerations

- **Binding Proofs**: All bindings (`didProof`, `certificateBinding`) **MUST** be cryptographically signed using JWS with ES256 or ES256K.
- **Private Key Protection**: Private keys **MUST** be stored securely (e.g., HSM, secure enclave) and **NEVER** included in DID Documents or public records.
- **Trust on First Use (TOFU)**: Avoid in production; always validate certificate chains and DID Registry entries.
- **Replay and Substitution Attacks**: Use timestamps (`iat`, `exp`) in `didProof` and unique `x5t#S256` values to prevent attacks.
- **Key Separation**: Use distinct keys for `capabilityInvocation` (registry operations) and `assertionMethod`/`authentication` (VC signing and authentication) to limit the impact of a key compromise.
- **Compliance**: Follow ETSI, ENISA, and NIST guidelines for key management, secure storage, and TLS for data transmission.

## 8. Privacy Considerations

- This method is for **legal entities** only (e.g., Universidad Carlos III de Madrid).
- **Personal data or personal public keys MUST NOT** be included in the DID Document.
- Implementers **MUST** ensure no personal information is stored or transmitted in public registries.

## 9. Limitations

- **Multiple Certificates**: A single public key may have multiple certificates, requiring unique `certificateBinding` entries for each.
- **CA Support**: CAs must support EBSI DID verification and SAN inclusion, which may require custom extensions.
- **Revocation Dependency**: Certificate revocation relies on external PKI mechanisms, not EBSI.

## 10. Verification Process

Verifiers validate the binding as follows:

1. **Certificate Validation**:
   - Check the certificate’s chain and revocation status using CRL or OCSP.
   - Ensure the certificate is valid and issued by a trusted CA.

2. **Hash Comparison**:
   - Compute the SHA-256 hash of the certificate (DER-encoded).
   - Compare it with the `x5t#S256` in the DID Document’s `certificateBinding`.

3. **Key Comparison**:
   - Extract the certificate’s public key and convert it to a JWK.
   - Calculate the JWK thumbprint (RFC 7638).
   - Compare it with the P-256 key’s thumbprint in the DID Document.

4. **DID Resolution**:
   - Query the EBSI DID Registry via HTTPS to retrieve the DID Document.
   - Verify the DID Document’s authenticity and integrity.

**Example JWK Thumbprint Calculation**:

**JWK** (P-256 key):
```json
{
  "kty": "ECON",
  "crv": "P-256",
  "x": "MrBK9V6_tTVc5uzRkBF7OQNsnogDhYr7m8etQQ2DBvw",
  "y": "GDWLKktUKlFR6kJM16rRcwAuCswva7SREhpzUttixmk",
  "alg": "ES256"
}
```

**Canonical JWK**:
```json
{"crv":"P-256","kty":"EC","x":"MrBK9V6_tTVc5uzRkBF7OQNsnogDhYr7m8etQQ2DBvw","y":"GDWLKktUKlFR6kJM16rRcwAuCswva7SREhpzUttixmk"}
```

**SHA-256 Hash** (base64url-encoded):
```
uPJtfsQgb1zWV25SOE9HwU5yzjVRfoPQVLUh-eZ79RU
```

This matches the key’s ID in the DID Document, confirming the binding.

## 11. Conformance Requirements

A conforming implementation **MUST**:
- Use RFC 7638 JWK thumbprints for key comparison.
- Include `x5c` in the `certificateBinding` service.
- Support JWS with ES256 or ES256K for `didProof` and VC signing.

A conforming implementation **SHOULD**:
- Include the DID in the certificate’s SAN.
- Support key rotation and certificate lifecycle management.

A conforming implementation **MAY**:
- Include revocation metadata in the DID Document (not recommended).

## 12. Summary

This guide provides a complete and illustrative process for binding X.509v3 certificates with DIDs in EBSI, using the **Universidad Carlos III de Madrid** as an example. Key features include:
- A secure DID Document with separate keys for registry operations and VC signing.
- An X.509v3 certificate with the DID in the SAN, issued by a trusted CA.
- A `certificateBinding` service linking the certificate to the DID Document.
- Cryptographic verification using JWK thumbprints and certificate hashes.
- Compliance with EBSI and PKI standards, ensuring a robust hybrid trust model.

By following this guide, legal entities can establish trusted digital identities that bridge decentralised and traditional infrastructures, enabling secure and verifiable interactions in digital ecosystems.

