# Trust Lists and Registries

Trust registries are essential components of the DC4EU trust framework. They allow verifiers and wallets to discover, validate, and trace the authority of credential issuers and their authorisation chains.

This section describes the core registries and how they are used in EAA-based verification.

---

## 1. TAO Registry

The **Trusted Accreditation Organisation (TAO) Registry** is a machine-readable list of entities authorised to issue Electronic Attestations of Attributes (EAAs).

### Contents:
- Entity ID (e.g. DID, LEI, NIF)  
- Legal name  
- Jurisdiction  
- Type of authority (RootTAO or TAO)  
- Valid EAAs issued or held  
- Metadata for verification

### Usage:
- Verifiers and wallets resolve issuers’ authority chains  
- Wallets display trust information to end users  
- Enables interoperability between countries and sectors

---

## 2. Trusted Schema Registry (TSR)

The TSR stores schemas and semantic definitions for all EAAs and credentials used in DC4EU.

### Contents:
- Credential types (e.g. EQFlevelX, HigherEducationInstitution)  
- Data model schemas (JSON-LD)  
- Context files (e.g. `@context`)  
- Alignment to ELM and EQF

### Usage:
- Verifiers parse credential structures  
- Wallets render data consistently  
- Developers validate conformance

---

## 3. Trusted Status Registry (TSRI)

The TSRI tracks the **status and validity** of EAAs (and optionally credentials) across their lifecycle.

### Contents:
- Status entries (active, revoked, suspended)  
- Revocation reasons  
- Timestamps  
- Links to affected EAAs

### Usage:
- Revocation checks during verification  
- Historical (point-in-time) validation  
- Traceability and transparency for compliance

---

## Discovery and Resolution

Wallets, verifiers, and EUDI infrastructure use these registries to:

- Resolve issuer identities and authorisations  
- Determine trust anchors for EAAs  
- Validate schema conformance and issuance rules  
- Apply policy rules based on jurisdiction and credential type

---

## Integration Models

Registries can be:
- Hosted centrally (e.g. by ministries, EU agencies)  
- Federated or decentralised (e.g. via EBSI, DID-based resolvers)  
- Accessed via APIs or embedded in Wallet Trust Modules

All registry entries are:
- Signed for integrity  
- Timestamped for auditing  
- Discoverable via open standards (e.g. DID resolution, HTTP endpoints)

---

## Trust Anchor Listing

In the case of QEAA and PubEAA models, RootTAOs and QTSPs may also appear in:

- **Union Trusted Lists (UTLs)** under eIDAS  
- **National Trust Lists** (NTLs)  
- **EBSI Governance Ledgers**

These listings ensure that trust discovery and validation are robust, interoperable, and auditable.
