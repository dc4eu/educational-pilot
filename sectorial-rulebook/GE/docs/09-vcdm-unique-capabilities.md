# 09 — Unique capabilities of VCDM for lifelong learning

## 9.1 Purpose of the chapter

This chapter gathers the subset of **capabilities that W3C-VCDM natively and documentedly realises** and that are operational requirements of lifelong learning. Each capability is presented in affirmative terms: what it contributes, how it demonstrates it, what operational evidence exists. Cross-references with the other chapters make it possible to see how each capability fits into the global architecture.

The chapter closes the argumentative part of the document and prepares the [roadmap](./10-roadmap.md).

## 9.2 Capability U1 — Native semantics with European controlled vocabularies

**What it contributes**: the ability to express, within the credential and without out-of-band metadata, the standardised meaning of each attribute through resolvable IRIs pointing to authoritative vocabularies (EQF, ESCO, ISCED-F, NACE, ELI, national frameworks).

**How it demonstrates it**: the JSON-LD 1.1 serialisation with `@context` and the resulting RDF graph contain triples that bind the declared values to the European schemas. A reasoner, a SHACL engine or a simple HTTP dereferencer can resolve the IRIs and confirm the semantics.

**Operational evidence**: ELM v3.2 is in production with a public `@context` maintained by DG EMPL. The EQF, ISCED-F and ESCO concepts are navigable from the EU Publications Office.

**References**: [05 — European Learning Model](./05-european-learning-model.md), [Annex B — Sources](./annexes/B-sources.md).

## 9.3 Capability U2 — Dual syntactic and semantic validation

**What it contributes**: the independent and complementary execution of JSON Schema (structural) and SHACL (semantic) over the same artefact, without the need for transformation or external registers.

**How it demonstrates it**: the `credentialSchema` field admits both validators (`FullJsonSchemaValidator2021` and `ShaclValidator2017`) in the same credential. Open tools (AJV, pySHACL, Jena) execute the pipeline without proprietary APIs.

**Operational evidence**: the EBSI TSR v3 profile already integrates registered JSON Schemas; the complementary SHACL shapes are published in the sectoral consortia (DC4EU, ELM operated by DG EMPL).

**References**: [04 — Dual validation architecture](./04-dual-validation-architecture.md).

## 9.4 Capability U3 — Lifecycle with native suspension and revocation

**What it contributes**: the two `statusPurpose`s (`"revocation"` and `"suspension"`) natively declared as part of the W3C Bitstring Status List v1.0 Recommendation, without proprietary extensions.

**How it demonstrates it**: the `credentialStatus` declaration can simultaneously list two `BitstringStatusListEntry` entries with the two purposes, each pointing to an independent list signed by the issuer.

**Operational evidence**: the specification has been a W3C Recommendation since 15 May 2025; open implementations are available in JavaScript, Python and Rust.

**References**: [06 — Lifecycle and trust](./06-lifecycle-and-trust.md), §6.2.

## 9.5 Capability U4 — Absence of "phone home" effect

**What it contributes**: the verifier downloads an aggregated list that covers many credentials; the issuer observes list downloads, not targeted queries on individual credentials. The person leaves no trace at the issuer when presenting a credential.

**How it demonstrates it**: the `BitstringStatusList` architecture aggregates by construction: a list of one million bits identifies one million credentials, but the download is indistinguishable between queries.

**Operational evidence**: documented in the W3C Recommendation; adopted by all reference implementations (Digital Bazaar, MATTR, Procivis, Sphereon, Walt.id, Izertis).

**References**: [06 — Lifecycle and trust](./06-lifecycle-and-trust.md), §6.3.

## 9.6 Capability U5 — Native cryptographic unlinkability with BBS+

**What it contributes**: two presentations of the same credential to two different verifiers are **cryptographically uncorrelatable**: not even with collusion between verifiers can the traces of one and the same person be reconstructed.

**How it demonstrates it**: the `bbs-2023` cryptosuite (BLS12-381) generates probabilistic derivations in each presentation, over a standard W3C Data Integrity scheme.

**Operational evidence**: the specification has been a W3C Candidate Recommendation since 3 April 2025; Rust and JavaScript implementations are already available. Article 3(10) of Regulation 2024/2982 requires unlinkability for LoA High in PID; W3C-VCDM with `bbs-2023` satisfies this requirement with a single native cryptosuite.

**References**: [03 — Benefits of W3C-VCDM](./03-w3c-vcdm-benefits.md), [06 — Lifecycle and trust](./06-lifecycle-and-trust.md), §6.4.

## 9.7 Capability U6 — Extensible trust model (eIDAS PKI ↔ EBSI dPKI)

**What it contributes**: smooth coexistence between the hierarchical eIDAS-PKI trust (QTS, LOTL) and the decentralised EBSI trust (TIR, TAOR, TSR). An issuer can be identified simultaneously by an `eidasLegalIdentifier` (PKI) and a DID (dPKI), and its accreditations are themselves verifiable credentials.

**How it demonstrates it**: the EUDIW profile for W3C-VC includes `eidasLegalIdentifier` as a canonical field in the `issuer`, and admits DID resolution against the EBSI TIR.

**Operational evidence**: operated by DC4EU in 16 Member States and 36 accredited institutions.

**References**: [06 — Lifecycle and trust](./06-lifecycle-and-trust.md), §6.5–§6.6.

## 9.8 Capability U7 — Multilingual traceability

**What it contributes**: ELM credentials are issued once and rendered in any of the 24 official EU languages thanks to the multilingual values of the controlled vocabularies and the localised labels of ELM.

**How it demonstrates it**: each concept IRI (`eqf:7`, `isced-f:0619`, ESCO occupations) has `rdfs:label` in the 24 languages. The wallet or verifier renderer selects the interface language.

**Operational evidence**: the Europass Dataspace has operated this over ELM for years; the pattern extends trivially to any EAA over W3C-VCDM.

**References**: [05 — European Learning Model](./05-european-learning-model.md), §5.8.

## 9.9 Capability U8 — Integration with global ecosystems

**What it contributes**: native semantic compatibility with **Open Badges 3.0** (1EdTech), mappability with **CTDL** (Credential Engine) and **LER**. A European EAA is interpreted in global contexts without reissuance.

**How it demonstrates it**: Open Badges 3.0 is built on VCDM. The ELM ↔ CTDL mapping is documented by 1EdTech and Credential Engine.

**Operational evidence**: **80 % of the 267 decentralised-identity projects** analysed by the Web of Trust Map 2025 use W3C-VC; more than 50 national programmes worldwide adopt it (Bhutan, Singapore, Canada, USA, Australia, United Arab Emirates, among others).

**References**: [05 — European Learning Model](./05-european-learning-model.md), §5.9; [01 — Context](./01-context-and-foundations.md).

## 9.10 Capability U9 — Digital sovereignty by design

**What it contributes**: all technical specifications are **W3C Recommendations**, ETSI standards or open IETF/OpenID specifications. No piece requires a proprietary licence or a private API. The Commission, the Member States and the European ecosystem can implement without external dependencies.

**How it demonstrates it**: the key components (VCDM, VC-JOSE-COSE, VC-Data-Integrity, BitstringStatusList, BBS Cryptosuites, ECDSA Cryptosuites, ELM, JSON Schema, SHACL) are open and W3C/ETSI/W3C-CG/IETF reference standards.

**Operational evidence**: the principle is the one invoked by the European Parliament resolution **P10_TA(2026)0022**, which demands that European critical infrastructure rest on open standards and auditable components.

**References**: [01 — Context and foundations](./01-context-and-foundations.md), §1.7; [Annex B — Sources](./annexes/B-sources.md).

## 9.11 Capability U10 — Uniform recursion of the model

**What it contributes**: an **accreditation** is a verifiable credential; a **status list** is a verifiable credential; a **presentation** is a verifiable credential (Verifiable Presentation). The same technical model, the same lifecycle and the same trust mechanisms apply at all levels.

**How it demonstrates it**: ELM classes admit `Accreditation` as a first-class credential; `BitstringStatusList` is typed as a `VerifiableCredential`; presentations are standard VCDM envelopes.

**Operational evidence**: the DC4EU trust framework operates over this recursion in the 16 Member States of the pilot.

**References**: [06 — Lifecycle and trust](./06-lifecycle-and-trust.md), §6.7.

## 9.12 Capability U11 — Interoperability between wallet implementations

**What it contributes**: the W3C-VC profile issued by one implementer is received, stored and presented by any other conformant wallet, without modifications.

**How it demonstrates it**: the VCDM + ELM + OID4VCI/VP + HAIP combination contains no implementation ambiguities; the canonical fields are identical.

**Operational evidence**: validation in DC4EU with four independent implementations (Identify, UAegean, Netcompany, Cappatrust) exchanging the 2,790 real credentials of the pilot.

**References**: [06 — Lifecycle and trust](./06-lifecycle-and-trust.md), §6.9.

## 9.13 Capability U12 — Dual-profile detection VCDM 1.1 / VCDM 2.0

**What it contributes**: one and the same wallet or verifier can detect and process credentials issued under VCDM 1.1 (the mandate in force by the first batch of Implementing Acts) and VCDM 2.0 (forward-looking Recommendation) without ambiguity, by inspecting the primary `@context`.

**How it demonstrates it**: `"https://www.w3.org/2018/credentials/v1"` ↔ VCDM 1.1; `"https://www.w3.org/ns/credentials/v2"` ↔ VCDM 2.0. The two processing paths are isomorphic except for optional fields added in 2.0.

**Operational evidence**: the proposed EUDIW profile explicitly declares simultaneous support; the DC4EU pilot wallets already realise it.

**References**: [01 — Context and foundations](./01-context-and-foundations.md), §1.5; [02 — Requirements R10](./02-lifelong-learning-requirements.md).

## 9.14 Capability U13 — Sectoral extensibility without fracturing the core

**What it contributes**: specialised sectors (health, mobility, finance, defence, education) define their own profiles on the same VCDM core, and conformant wallets handle them without updates.

**How it demonstrates it**: the projects funded by DEP demonstrate this extensibility: **DC4EU** (education), **PH4H** (health), **TRACE4EU / EBSI-VECTOR** (mobility), **Catena-X / Gaia-X** (industrial mobility), **Safe Island** (social). They all share the technical core.

**Operational evidence**: the **combined portfolio of European public funds exceeds 80 million euros** in more than 200 organisations from more than 20 countries.

**References**: [07 — Sectoral EAA catalogue](./07-sectoral-eaa-catalogue.md); [01 — Context and foundations](./01-context-and-foundations.md), §1.6.

## 9.15 Capability U14 — Compatibility with the HAIP architecture and OpenID4VC*

**What it contributes**: the W3C-VC formats (`jwt_vc_json-ld`, `ldp_vc`) are first-class citizens in the OpenID4VCI and OpenID4VP metadata. The presentation via HAIP is defined symmetrically to the other formats.

**How it demonstrates it**: the OpenID4VCI and OpenID4VP specifications admit `credential_configurations_supported` and `presentation_definition` lists with the W3C-VC formats.

**Operational evidence**: implemented by the DC4EU, TRACE4EU and EBSI-VECTOR pilots with cross-verification.

**References**: [03 — Benefits of W3C-VCDM](./03-w3c-vcdm-benefits.md), [08 — Complete profile](./08-eudiw-profile.md), §8.3.3.

## 9.16 Capability U15 — Sustainable evolution of the model

**What it contributes**: the W3C-VCDM model evolves by **versioned Recommendations**, with W3C publications following the mature process of the organisation (Working Drafts → Candidate Recommendations → Recommendations). Backward compatibility is preserved with the `@context` mechanism.

**How it demonstrates it**: the very history VCDM 1.0 → 1.1 → 2.0 is evidence of the process; each version extends capabilities without invalidating the previous one.

**Operational evidence**: wallets with VCDM 1.1 support receive VCDM 2.0 credentials and automatically distinguish the additional capabilities.

**References**: [01 — Context and foundations](./01-context-and-foundations.md), §1.4–§1.5.

## 9.17 Aggregate summary

The table below consolidates the 15 unique capabilities and their operational realisation:

| # | Capability | Operational realisation |
|---|---|---|
| U1 | Native semantics | ELM v3.2 + EQF/ESCO/ISCED-F |
| U2 | Dual validation | JSON Schema + SHACL in `credentialSchema` |
| U3 | Suspension and revocation | `BitstringStatusList` (W3C Rec 2025-05-15) |
| U4 | No "phone home" | Aggregated status lists |
| U5 | Cryptographic unlinkability | `bbs-2023` over BLS12-381 |
| U6 | Hybrid PKI ↔ dPKI | `eidasLegalIdentifier` + DID + EBSI TIR |
| U7 | Multilingual traceability | EU multilingual controlled vocabularies |
| U8 | Global compatibility | Open Badges 3.0 + CTDL + LER |
| U9 | Sovereignty by design | Open W3C + ETSI Recommendations |
| U10 | Uniform recursion | Accreditations, lists, presentations over VCDM |
| U11 | Wallet interoperability | 4 validated implementations DC4EU |
| U12 | VCDM 1.1/2.0 dual profile | Detection via `@context` |
| U13 | Sectoral extensibility | DC4EU + PH4H + TRACE4EU + Catena-X + Safe Island |
| U14 | HAIP + OID4VC* | `ldp_vc`, `jwt_vc_json-ld` formats in metadata |
| U15 | Sustainable evolution | Mature W3C process with backward compatibility |

## 9.18 Conclusion of the chapter

The 15 capabilities are the **affirmative condensation** of the lifelong-learning requirements identified in [02](./02-lifelong-learning-requirements.md), operationalised by the architectures documented in [04](./04-dual-validation-architecture.md), [05](./05-european-learning-model.md), [06](./06-lifecycle-and-trust.md) and [07](./07-sectoral-eaa-catalogue.md), and formalised by the regulatory profile proposed in [08](./08-eudiw-profile.md).

The whole constitutes a mature, verifiable and operational technical basis ready to be referenced in full by the next regulatory cycle of the EUDIW.

---

**Next**: [10 — Roadmap and recommendations](./10-roadmap.md)
