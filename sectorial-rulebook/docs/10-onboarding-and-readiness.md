# Onboarding and Readiness

This section outlines the technical, legal, and governance prerequisites for entities seeking to participate in the DC4EU ecosystem as RootTAOs, TAOs, or Credential Issuers.

The onboarding process ensures that only authorised, discoverable, and trustworthy entities issue or delegate Electronic Attestations of Attributes (EAAs).

---

## Who Can Onboard?

Entities wishing to act as:

- **Root Trusted Accreditation Organisations (RootTAOs)**  
  Must be recognised ministries or EU-level authorities with legal authority.

- **Trusted Accreditation Organisations (TAOs)**  
  Must be legally authorised by RootTAOs and capable of issuing EAAs to credential issuers.

- **Credential Issuers**  
  Must hold valid authorisations and meet minimum digital infrastructure criteria.

---

## Legal Requirements

Each onboarding entity must:

- Be formally recognised in national or EU law  
- Have a mandate or legal basis to issue, accredit, or regulate credentials  
- Accept DC4EU governance terms and trust model rules  
- Provide evidence supporting their status (e.g. legislation, government registry entry)

---

## Technical Requirements

To issue or receive EAAs, entities must:

- Operate a **Verifiable Credential issuance system**  
- Support **W3C VC** format and JSON-LD serialization  
- Implement **digital signature mechanisms** (advanced or qualified)  
- Integrate with at least one trust model:
  - X.509 PKI (classical)
  - Decentralised PKI (e.g. DIDs, EBSI)  
- Provide public endpoints (or registry entries) for verification metadata

---

## Metadata for Discovery

Entities must provide machine-readable metadata for inclusion in:

- **TAO Registry** (entity roles and delegations)  
- **Trusted Schema Registry (TSR)** (credential types they issue)  
- **Trusted Status Registry (TSRI)** (revocation and validity data)

Metadata typically includes:
- Entity ID (e.g. LEI, NIF, ORG DID)  
- Legal name  
- Jurisdiction  
- Authorisation types held  
- Trust model details (e.g. DID Document or certificate chain)

---

## Verification Environment

Entities must support:
- Testing and staging environments  
- Credential previews  
- Response to automated verification requests

These environments help Wallet Providers and Verifiers test compatibility and trust chain validation before going live.

---

## Minimum Readiness Checklist

| Requirement                             | Applies to     |
|----------------------------------------|----------------|
| Legal authority to act                 | RootTAO, TAO   |
| Verifiable Credential support          | TAO, Issuer    |
| Signature capabilities (A/QSeal)       | All            |
| Trust model metadata                   | All            |
| Registry integration                   | RootTAO, TAO   |
| Staging/test environment available     | Issuer         |

---

## Onboarding Documentation

Entities must complete:
- A self-declaration or registration form  
- Legal basis mapping (to national/EU law)  
- Metadata JSON package for registry ingestion

These materials are reviewed by the governance bodies of DC4EU or competent Member State authorities.
