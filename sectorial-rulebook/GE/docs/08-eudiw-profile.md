# 08 — Complete EUDI Wallet profile for W3C-VC

## 8.1 Purpose of the chapter

This chapter synthesises the **complete technical profile of the W3C Verifiable Credentials Data Model** for its operational treatment within the EUDI Wallet, articulated as a **regulatory proposal symmetrical** to the already complete references for the other two formats of the ecosystem (mdoc and SD-JWT VC).

The tone is deliberately **constructive**: it is not formulated against any technical option; it proposes to complete a piece of the European regulatory jigsaw that the ecosystem has ready and that the Ares(2026)1286304 public consultation called for with broad convergence.

## 8.2 Current regulatory context

The **first batch of Implementing Acts** of Regulation (EU) 2024/1183 references the three credential formats:

- **mdoc** (ISO/IEC 18013-5, CBOR): with complete operational treatment in Annexes I and V of CIR 2024/2977 and CIR 2024/2979.
- **SD-JWT VC** (IETF OAuth WG): with complete operational treatment in the same Annexes.
- **W3C VCDM 1.1** (JSON-LD): referenced as an admissible format, with ETSI TS 119 472-1 V1.1.1 clause 7 as technical reference, but with **operational treatment pending completion** in the Annexes.

The proposal of this chapter is what balances regulatory symmetry, adding for W3C-VC the same operational pieces that the other two formats already have.

## 8.3 Architecture of the proposed profile

The profile is articulated in three layers:

### 8.3.1 Data layer

- Canonical **JSON-LD 1.1** serialisation with authoritative `@context`.
- Use of **ELM v3.2** as the reference semantic model for educational EAAs.
- **Dual validation architecture** (JSON Schema + SHACL) with both entries declared in `credentialSchema`.
- Mandatory fields according to VCDM: `@context`, `id`, `type`, `issuer`, `validFrom` (VCDM 2.0) / `issuanceDate` (VCDM 1.1), `credentialSubject`, `credentialStatus`, `credentialSchema`, cryptographic proof.
- Issuer identification with `eidasLegalIdentifier`.

### 8.3.2 Status layer

- **BitstringStatusListEntry** with `statusPurpose: "revocation"` mandatory for qualified EAAs.
- **BitstringStatusListEntry** with `statusPurpose: "suspension"` optional and recommended for educational credentials with a prolonged lifecycle.
- Status lists published as Verifiable Credentials signed by the issuer.

### 8.3.3 Protocol layer

- **OpenID4VCI** for issuing credentials to the wallet.
- **OpenID4VP** for presentation to the verifier.
- **HAIP** (High Assurance Interoperability Profile) as the security profile.
- Declaration in `openid4vci_metadata` of the applicable format (`jwt_vc_json-ld`, `ldp_vc` or equivalents).

## 8.4 The eight elements of profile completeness

The regulatory-parity analysis identifies **eight elements** (four for data/status, four for protocol) that define the complete profile:

### 8.4.1 Data and status elements (1–4)

1. **Normative references to VCDM 1.1 and 2.0**: explicit inclusion of the W3C Recommendations in the normative references of the Annexes.
2. **Dual validation architecture**: mandatory declaration of the JSON Schema + SHACL pair in `credentialSchema`.
3. **BitstringStatusList with revocation and suspension**: simultaneous support for both `statusPurpose`s.
4. **Educational data structures**: referencing of ELM v3.2 and the Sectoral EAA Catalogue as admitted extensions.

### 8.4.2 Protocol elements (5–8)

5. **HAIP for W3C-VC**: formalisation of the HAIP profile applicable to W3C-VC, with the same security requirements as the other two formats.
6. **OpenID4VCI for W3C-VC**: admitted formats (`jwt_vc_json-ld`, `ldp_vc`) and issuer metadata (`credential_issuer_metadata`) for W3C-VC.
7. **OpenID4VP for W3C-VC**: presentation formats (`ldp_vp`, `jwt_vp_json-ld`) and applicable `presentation_definition`.
8. **Cryptography and proofs**: Data Integrity cryptosuites (`ecdsa-rdfc-2019`, `eddsa-rdfc-2022`, `bbs-2023`) and equivalent admitted JOSE.

## 8.5 Proposal for symmetrical regulatory adaptation

The proposal materialises in two concrete artefacts:

### 8.5.1 New Section 4.3 of Annex I of CIR 2024/2977

A new Section 4.3 (symmetrical to Sections 4.1 mdoc and 4.2 SD-JWT VC) with the encoding of the **PID in JSON-LD W3C-VC**. The section includes:

- List of PID attributes in JSON-LD: Table 9 with **27 attributes** corresponding to the minimum fields of Regulation 2024/1183.
- Canonical encodings and JSON-LD types for each attribute.
- Admitted selective-disclosure mechanisms (BBS+ and salted-hash).
- Cryptographic-proof requirements.
- Status (BitstringStatusListEntry) and trust framework (EBSI TIR / TAOR).

### 8.5.2 Adaptation points (9)–(16) of Annex V of CIR 2024/2979

Eight adaptation points (symmetrical to (1)–(8) for the other formats) with the rules for W3C-VC:

| Adaptation | Object |
|---|---|
| (9) | Normative references to W3C VCDM 1.1 and 2.0. |
| (10) | Dual validation architecture (JSON Schema + SHACL). |
| (11) | Credential status: BitstringStatusList with revocation and suspension. |
| (12) | Data structure: ELM v3.2, Sectoral EAA Catalogue, extension mechanisms. |
| (13) | HAIP applicable to W3C-VC. |
| (14) | OpenID4VCI: formats, issuer metadata, `credential_configurations_supported`. |
| (15) | OpenID4VP: presentation formats, `presentation_definition`, selective disclosure. |
| (16) | Cryptography: admissible Data Integrity and JOSE/COSE cryptosuites. |

This proposal is **non-invasive** for the formats already treated: it adds parallel sections and points without modifying the existing ones. Regulatory symmetry is obtained by **addition**, not by **substitution**.

## 8.6 Table of equivalences between the three formats

| Element of the profile | mdoc (ISO/IEC 18013-5) | SD-JWT VC (IETF OAuth) | W3C-VC (VCDM 1.1 / 2.0) |
|---|---|---|---|
| Serialisation | CBOR | JWT with `sd` claim | JSON-LD 1.1 |
| Data schema | CDDL | JSON Schema | JSON Schema + SHACL (dual) |
| Status | ISO + TR 17015 mechanisms | Reference list, Status list JWT | BitstringStatusList (W3C Rec) |
| Native suspension | — | — | `statusPurpose: "suspension"` |
| Native revocation | TR 17015 | Status list | `statusPurpose: "revocation"` |
| Selective disclosure | Native mdoc | `sd` claims | BBS+ (`bbs-2023`) + salted-hash |
| Cryptographic unlinkability | — | — | Native BBS+ (`bbs-2023`) |
| Semantic vocabularies | — (typed CDDL) | Typed JSON | RDF + ELM + EQF/ESCO/ISCED-F |
| Trust model | eIDAS PKI | eIDAS PKI + OpenID list | eIDAS PKI + EBSI dPKI |
| Issuance/presentation protocols | OID4VCI / OID4VP | OID4VCI / OID4VP | OID4VCI / OID4VP |
| Applicable HAIP | Yes | Yes | Proposed (Point 13) |
| Authoritative schema register | — | JSON Schema registries | EBSI TSR v3 |
| LSP pilot operational validation | ISO ecosystem | Multi-LSP | DC4EU (36 inst., 16 MS) |

The reading of the table is direct: the three formats functionally cover the EUDIW space with different emphases. W3C-VC natively contributes the semantic and unlinkability layers that are crucial for the educational EAAs of lifelong learning.

## 8.7 Procedural recommendation: ETSI ESI standardisation request

The Ares(2026)1286304 public consultation evidenced broad convergence on a concrete procedural approach:

- **Maintain** the reference to ETSI TS 119 472-1 without fixing a specific version in the Implementing Acts.
- **Issue** a standardisation request to **ETSI TC ESI** under Regulation (EU) No 1025/2012 to develop a **European High Assurance Interoperability Profile** covering the three referenced formats symmetrically.

The operational advantage is to turn a potentially fragmented round of national clarifications into a **single coherent European decision**, accountable and versionable without regulatory blockages.

## 8.8 Verifiable prior milestones

The proposed profile relies on already verifiable technical and regulatory milestones:

- **W3C VCDM 2.0 + complementary package** (VC-JOSE-COSE, VC-Data-Integrity, Bitstring Status List v1.0, ECDSA Cryptosuites v1.0): published on **15 May 2025**.
- **W3C BBS Cryptosuites v1.0**: Candidate Recommendation of **3 April 2025**.
- **ETSI TS 119 472-1 V1.1.1**: publication of **December 2025**, with clause 7 dedicated to W3C-VC.
- **ELM v3.2 + EDC v1.9**: published by DG EMPL with canonical `@context` and registration in EBSI TSR v3.
- **DC4EU Sectoral EAA Catalogue**: 18 operational types.
- **Public consultation Ref. Ares(2026)1286304**: 43 contributions, broad convergence.

## 8.9 Impact on implementers

The proposed profile does not introduce new requirements for implementers who are already following ecosystem good practice. Specifically:

- **Wallets** already conformant with the EUDIW profile (OID4VCI/VP support, HAIP) require adding support for `ldp_vc` / `jwt_vc_json-ld` formats with Data Integrity, and for `BitstringStatusList`. Both are incremental extensions, not redesigns.
- **Issuers** already issuing EDC over VCDM (universities, VET centres, companies with CPD) will satisfy the profile by applying the non-modification principle.
- **Verifiers** already consuming EDC add steps (3) and (4) of the pipeline of chapter 04 with standard open libraries.

The marginal cost of adoption is low thanks to the **continuity with the investments already made** by the ecosystem (€80M+ ALASTRIA, €19M DC4EU, CRUE 77 universities).

## 8.10 Outcome

The complete EUDIW profile for W3C-VC:

1. Is articulated in three layers (data, status, protocol) with eight elements symmetrical to the other formats.
2. Materialises in two concrete normative artefacts: Section 4.3 of Annex I CIR 2024/2977 and points (9)–(16) of Annex V CIR 2024/2979.
3. Reuses the operational artefacts of the ecosystem (ELM v3.2, EBSI TSR v3, DC4EU Sectoral Catalogue) without modification.
4. Completes the regulatory symmetry between the three formats admitted by eIDAS 2.0.
5. Relies on verifiable milestones published between April 2025 and December 2025, with empirical validation in 16 Member States.
6. Has a clear procedural path (standardisation request to ETSI ESI) agreed upon in the public consultation of early 2026.

The next chapter details the [unique capabilities that W3C-VCDM contributes to lifelong learning](./09-vcdm-unique-capabilities.md).

---

**Next**: [09 — Unique capabilities of VCDM for lifelong learning](./09-vcdm-unique-capabilities.md)
