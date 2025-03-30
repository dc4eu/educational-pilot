# Authorisation Model

The authorisation model defines how entities are granted the right to issue verifiable credentials in a legally and technically trustworthy manner. It ensures that **credential issuers** can prove their authority through **Electronic Attestations of Attributes (EAAs)**, which are verifiable, traceable, and interoperable.

---

## Objective

To allow **verifiers** to confidently determine whether a given issuer is legitimately authorised to issue a specific type of credential — based on a digitally verifiable chain of trust.

---

## Authorisation Chain Structure

The model uses a multi-tiered delegation of trust:

1. **Root Trusted Accreditation Organisation (RootTAO)**  
   → issues EAA to  
2. **Trusted Accreditation Organisation (TAO)**  
   → issues EAA to  
3. **Credential Issuer**

Each EAA in the chain is verifiable and can be resolved back to a trusted anchor.

---

## Core Components

### 1. Entity Information

Defines attributes of participating entities.

| Attribute           | Description                                         |
|--------------------|-----------------------------------------------------|
| ID                 | Unique identifier (e.g. DID, Legal Entity ID)       |
| Name               | Full legal name                                     |
| Address            | Physical or registered location                     |
| Establishment Date | Official date of creation or registration           |
| Role               | RootTAO, TAO, Issuer, or Verifier                   |

---

### 2. Authorisation Information (EAA)

Each authorisation is an EAA issued as a verifiable credential.

| Attribute              | Description                                                          |
|------------------------|----------------------------------------------------------------------|
| Authorisation ID       | Globally unique identifier                                           |
| Granter ID             | ID of the entity issuing the authorisation                          |
| Grantee ID             | ID of the recipient entity                                           |
| Type of EAA            | Defines scope (e.g. HigherEducationInstitution, QA Agency, etc.)     |
| Jurisdictional Limits  | Geographic or legal scope                                            |
| Issuance Date          | When the authorisation begins                                        |
| Validity Date          | When the authorisation expires, if applicable                        |
| Evidence               | Legal or regulatory basis (e.g. national law, EU regulation)         |

---

## Authorisation Verification Logic

To validate an issuer’s authority, verifiers check:

1. Signature of the EAA  
2. Validity and status of the authorisation  
3. Grantee's identity  
4. Trust anchor resolution (via RootTAO)  
5. Jurisdiction and scope compliance  

---

## Trust Anchors and Resolution

EAAs are anchored to RootTAOs, which are published in:
- **Trusted Lists**
- **Trust Registries (e.g. TAO Registry on EBSI)**
- **Public Key Infrastructures (X.509 or DIDs)**

Wallets and verifiers use these registries to:
- Validate issuer chains
- Discover valid TAOs and Issuers
- Resolve schema types and semantic context

---

## Trust Models Supported

The model is agnostic to the type of trust infrastructure, supporting both:
- **Classical PKI** (e.g. national trust lists, X.509 certificates)
- **Decentralised PKI (dPKI)** (e.g. DIDs, EBSI-based registries)

This dual compatibility ensures flexibility for Member States and scalability across sectors.
