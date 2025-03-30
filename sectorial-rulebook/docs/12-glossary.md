# Glossary

This glossary defines the key terms used throughout the DC4EU Sectoral Rulebook for Education and Professional Qualifications.

---

## Natural Person
An individual acting as a credential holder. In the EUDI context, they control a wallet and present verifiable credentials.

## Legal Person
An organisation with legal personality (e.g. university, ministry, company) that can act as an issuer, verifier, or authority.

## Electronic Attestation of Attributes (EAA)
A verifiable credential asserting the rights or qualifications of an entity, issued under the eIDAS 2.0 framework. It certifies authorisation (e.g. to issue diplomas).

## Root Trusted Accreditation Organisation (RootTAO)
A top-level authority inherently trusted to begin the trust chain. Typically a ministry or an EU-level public body.

## Trusted Accreditation Organisation (TAO)
An entity authorised by a RootTAO to issue EAAs to credential issuers. Examples include national QA agencies, NRENs, or professional chambers.

## Credential Issuer
A university, training provider, or professional body authorised (via EAA) to issue verifiable credentials to learners or professionals.

## Verifiable Credential (VC)
A tamper-evident digital statement issued by a trusted entity and cryptographically verifiable by any third party. EAAs are a specific type of VC.

## Verifier
An organisation (e.g. employer, university) that checks the authenticity and authorisation status of a credential and its issuer.

## EUDI Wallet
The European Digital Identity Wallet used by natural persons to store and present verifiable credentials in compliance with eIDAS 2.0.

## Qualified EAA (QEAA)
An EAA issued by a Qualified Trust Service Provider (QTSP), offering the highest legal assurance under eIDAS.

## PubEAA
An EAA registered in a trusted list or registry, making it discoverable and verifiable automatically.

## Sectoral EAA Catalogue
A structured reference of EAAs, their semantic definitions, and expected usage across sectors. Defines standard credential types.

## European Qualifications Framework (EQF)
A common EU framework for comparing qualifications and levels of learning across Member States.

## European Education Area (EEA)
A strategic initiative aiming to ensure automatic recognition of learning outcomes and mobility across Europe.

## European Learning Model (ELM)
A standardised data model used to describe and structure learning achievements and credentials in a machine-readable way.

## 🎓 EDC – European Digital Credentials

A standard digital credential format developed by the European Commission to support the issuance and recognition of learning achievements and qualifications.

- Based on the **European Learning Model (ELM)**
- Uses **W3C Verifiable Credentials** and **JSON-LD**
- Typically issued by **educational institutions** and recognised **across Europe**
- Integrated with **Europass**, **X-Road**, **EMREX**, and increasingly aligned with **EUDI Wallet** standards

EDCs can represent:
- Degrees, diplomas, and certificates
- Learning outcomes and qualifications
- Accreditation or validation statements

In DC4EU, EDCs are used as the payload format for learner credentials, while EAAs provide the authorisation framework for their issuers.

## Trust List
An official registry of trusted issuers or authorisation providers (e.g. RootTAOs, QTSPs, TAOs).

## Registry
A database (centralised or decentralised) used to publish metadata about issuers, authorisations, credential schemas, or status.

## Revocation Registry
A technical service that allows verifiers to check if a credential or EAA has been revoked or is no longer valid.

## Point-in-Time Validation
The ability to verify that an EAA or credential was valid at a specific historical moment — essential for long-term trust.

## eIDAS 2.0
The revised EU regulation (2024/1183) governing digital identity, trust services, and the European Digital Identity Wallet (EUDIW).
