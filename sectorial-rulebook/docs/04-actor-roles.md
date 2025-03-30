# Actor Roles

The EAA-based authorisation model involves a range of actors who issue, verify, consume, and manage credentials and their associated trust frameworks. This section defines their roles within the DC4EU governance structure.

---

## Natural Person

An individual who is the subject of a credential — e.g. a learner, teacher, or professional.

In the EUDI framework, a natural person is typically:
- The **holder of a credential**
- The **controller of a European Digital Identity Wallet (EUDI Wallet)**

---

## Legal Person

An organisation (e.g. a university, public authority, or professional body) involved in the issuance, verification, or governance of credentials.

Legal entities are usually:
- **Issuers**
- **Verifiers**
- **Accrediting authorities**

---

## Root Trusted Accreditation Organisation (RootTAO)

A top-level authority that is inherently trusted to grant initial authorisations. Typically:
- A **Ministry** or public authority
- A **European body** (e.g. GEANT, ENQA, EQAR)

RootTAOs issue EAAs to designate **Trusted Accreditation Organisations (TAOs)**.

---

## Trusted Accreditation Organisation (TAO)

An entity that receives an authorisation from a RootTAO and is permitted to issue authorisations to other entities, such as credential issuers.

Examples:
- A national quality assurance agency
- A National Research and Education Network (NREN)
- A professional chamber or licensing board

---

## Credential Issuer

An institution (e.g. university, training provider, professional body) that:
- Is authorised via an EAA
- Issues verifiable credentials (e.g. diplomas, licences, IDs)

Credential Issuers must:
- Hold a valid EAA issued by a TAO
- Be discoverable in trust registries
- Sign credentials with verifiable proofs

---

## Verifier

Any relying party (e.g. employer, university, regulator) that:
- Consumes credentials from learners
- Checks the **validity of the credential** and the **authorisation of the issuer**

Verifiers typically:
- Use trusted lists or registries
- Validate cryptographic proofs and authorisation chains
- Operate under data minimisation and legal compliance

---

## EUDI Wallet Holder

A natural person who:
- Controls their credentials in an **EUDI-compliant Wallet**
- Shares credentials selectively with verifiers
- Receives updates and revocations

The Wallet may enforce:
- Selective disclosure
- Consent management
- Trust registry lookup

---

## Supporting Infrastructure Actors

Other actors critical to the ecosystem include:

- **Trust Service Providers (TSPs)**: Entities providing digital signatures and identity certificates  
- **Registry Operators**: Manage TAO lists, Schema Registries, Revocation Lists  
- **Policy Authorities**: Define national or sector-specific governance frameworks

---

By clearly defining these roles, the authorisation model ensures traceability, responsibility, and compliance across all levels of the credential lifecycle.
