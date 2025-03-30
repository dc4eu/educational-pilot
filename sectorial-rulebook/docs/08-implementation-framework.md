# Implementation Framework

This section outlines the technical, cryptographic, and trust infrastructure used to implement the EAA-based authorisation model within the European Digital Identity (EUDI) ecosystem.

The framework supports issuance, verification, lifecycle management, and integration with national and European-level trust services.

---

## Cryptographic Foundations

EAAs are implemented as **Verifiable Credentials (VCs)** following the **W3C VC Data Model**. They are:

- Digitally signed using advanced or qualified electronic seals  
- Serialized in JSON-LD for semantic interoperability  
- Anchored to either X.509 PKI or Decentralised Identifiers (DIDs)  

Wallets and verifiers use **cryptographic proofs** to ensure:
- Data integrity  
- Origin authentication  
- Non-repudiation  

---

## Trust Models Supported

The model accommodates both classical and decentralised trust infrastructures:

| Trust Model             | Description                                     |
|--------------------------|-------------------------------------------------|
| **Classical PKI**       | X.509 certificates, national trust lists, QTSPs |
| **Decentralised PKI**   | DIDs, DID Documents, EBSI                       |
| **Hybrid**              | Combinations (e.g. DIDs + QSeal from QTSP)     |

---

## Data and Schema Registries

Registries provide machine-readable metadata about:
- Authorised entities (TAO Registry)  
- Credential structures (Trusted Schema Registry - TSR)  
- Status/revocation (Trusted Status Registry - TSRI)  

Used for:
- Trust discovery  
- Credential resolution  
- Real-time validation  

---

## Identity Matching

To resolve identities across jurisdictions:
- Wallets support structured attributes  
- Matching policies follow MS-specific rules  
- Unique IDs (e.g. LEI, NIF) ensure institutional consistency  

---

## Wallet Enforcement Policies

EUDI Wallets enforce:
- **Selective Disclosure**  
- **Consent management**  
- **Trust resolution** via registry queries  
- **Credential expiration and revocation**

Wallets may include a **Policy Agent** to enforce eIDAS and GDPR compliance.

---

## Lifecycle Management

Credential lifecycle is supported via:
- Validity periods  
- Revocation endpoints or registries  
- Temporal verification (e.g. point-in-time trust checks)

---

## Interoperability

EAAs and credentials are:
- **Mapped to the European Learning Model (ELM)**  
- **Compatible with Europass, EMREX, MyAcademicID**  
- **Compliant with eIDAS 2.0** and ETSI/EN standards  
- **Resolvable through DID and HTTP endpoints**  

This ensures they can be trusted across borders, ecosystems, and future use cases.
