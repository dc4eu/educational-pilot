# EAA Types and Scenarios

This section explains the different types of Electronic Attestations of Attributes (EAAs) and the trust scenarios under which they can be issued and verified. These are classified based on compliance with the amended eIDAS 2.0 Regulation and the capabilities of the European Digital Identity Wallet (EUDIW).

---

## Types of EAAs

The DC4EU model defines three main types of EAAs:

### 1. EAA (Standard Electronic Attestation of Attributes)

- Issued by a trusted entity using either:
  - Classical PKI (e.g. X.509-based certificates)
  - Decentralised PKI (dPKI, e.g. EBSI)
  - Or both combined (hybrid model) — as in DC4EU Education and Professional Qualifications
- Digitally signed with an advanced electronic seal or certificate
- Discoverable via metadata or direct presentation
- Verifiable through EUDI Wallets
- Legal assurance depends on the issuer’s governance and recognition

✅ *EUDI Wallet Compatible*

---

### 2. PubEAA (Public EAA)

- An EAA issued by a **Public Sector Body** that:
  - Is in charge of an **Authentic Source**, or
  - Is formally mandated to act on behalf of one
- May or may not be issued by a Qualified Trust Service Provider (QTSP)
- Registered in a **Trusted List or Registry** for automatic discovery
- Enables legal and semantic recognition of attributes, especially in the public domain

Typical examples:
- Ministries issuing accreditation EAAs
- National QA agencies acting under public authority

✅ *EUDI Wallet Compatible and discoverable*

---

### 3. QEAA (Qualified EAA)

- Issued by a **Qualified Trust Service Provider (QTSP)** under eIDAS 2.0
- Offers the highest level of legal and technical assurance
- Mandated for specific regulated or high-assurance scenarios
- Registered in the **Union Trusted List (UTL)**

Typical examples:
- Ministries or QTSPs issuing licences or professional mandates with legal effect

✅ *EUDI Wallet Compatible and fully enforceable*

---

## Scenario Classifications

Each trust scenario aligns with the above EAA types:

### 🔹 Scenario 1: EAA (Non-Qualified EAA)

- Issued using classical PKI, dPKI, or hybrid trust models
- Not issued by a QTSP
- Fully compatible with EUDI Wallet
- Trust and legal effect based on issuer’s authorisation and registries

Example: A university issuing EQF-level EAAs using dPKI + X.509 hybrid model

✅ *EUDI Wallet Compatible*

---

### 🔹 Scenario 2: PubEAA (Registered Public EAA)

- Issuer is a public body acting as or on behalf of an authentic source
- Registered in a trusted list or registry (e.g. TAO Registry)
- Discoverable by verifiers and wallets
- Enhanced trust and semantic interoperability

Example: A QA agency issuing programme-level accreditation

✅ *EUDI Wallet Compatible and discoverable*

---

### Scenario 3: QEAA (Qualified EAA)

- Issued by a QTSP under eIDAS 2.0
- Highest legal and cryptographic assurance
- Registered in the Union Trusted List (UTL)
- May be required for sensitive credentials (e.g. professional licences)

Example: Ministry of Health issuing QEAA for medical licensure

✅ *EUDI Wallet Compatible and legally enforceable*

---

## Scenario Comparison Table

| Scenario        | Trust Level   | Registry Required     | EUDIW Compatible | Legal Assurance          |
|----------------|---------------|------------------------|------------------|--------------------------|
| Scenario 1      | Medium        | Optional               | ✅ Yes           | Based on issuer governance |
| Scenario 2      | High          | Required (Pub. List)   | ✅ Yes           | Strong (Authentic Source)  |
| Scenario 3      | Very High     | Mandatory (UTL)        | ✅ Yes           | Qualified (eIDAS)          |

---

## Technical Discovery & Resolution

Wallets and verifiers use metadata, DID Documents, and trusted registries to resolve:

- Credential types and schemas
- Authorisation chains and trust anchors
- Validity, expiry, and revocation
- Jurisdictional context and regulatory constraints

This ensures that EAAs can be verified programmatically — even across borders and over time.
