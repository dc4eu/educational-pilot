# 00 — Executive summary

## Central thesis

The **W3C Verifiable Credentials Data Model (W3C-VCDM)**, in its versions 1.1 (the mandate currently in force under the first batch of Implementing Acts of eIDAS 2.0) and 2.0 (W3C Recommendation of 15 May 2025, forward-looking optional profile), is the appropriate technical foundation for credentialing of **education understood as lifelong learning** within the European Digital Identity Wallet (EUDIW). The format natively provides — and has demonstrated in production — the set of capabilities that lifelong learning needs: machine-to-machine semantic interoperability, dual structural + semantic validation, lifecycle with native suspension and revocation, cryptographic unlinkability for LoA High, digital sovereignty by design, native integration with the European semantic assets (ELM, ELI, EQF, ESCO, ISCED-F), and compatibility with the global educational credentialing ecosystems (Open Badges 3.0, CTDL, LER).

## The argument in ten lines

1. **Lifelong learning** requires that a qualification issued in one Member State be automatically interpretable in another, without human mediation or bilateral mappings.
2. W3C-VCDM provides that semantic interoperability through **JSON-LD** and `@context`, binding the credential to the authoritative European vocabularies.
3. The dual **JSON Schema + SHACL** architecture over the RDF graph, formalised in the requirements `EAA-7.2.1.3-W3C-01..04` of the EUDIW profile, enables executable structural + semantic validation.
4. The W3C **Bitstring Status List v1.0** Recommendation natively supports `statusPurpose: "revocation"` and `statusPurpose: "suspension"`, covering Article 24 and Section 9 of Regulation 2024/1183.
5. The **`bbs-2023`** cryptosuite over BLS12-381 provides native cryptographic unlinkability, required by Article 3(10) of Regulation 2024/2982 at LoA High assurance level.
6. Embedded **Data Integrity** proofs (`ecdsa-rdfc-2019`, `bbs-2023`) are verified without proprietary APIs, realising the principle of **digital sovereignty by design** invoked by European Parliament resolution P10_TA(2026)0022.
7. **DC4EU** validated W3C-VCDM in 36 institutions from 16 Member States (89 % of the European population), with 2,790 real credentials issued and 18 credential types published as the **Sectoral EAA Catalogue**.
8. The **European Learning Model v3.2** and the **EDC** profile are already registered in the **EBSI Trusted Schemas Registry v3** with an operational dual JSON Schema + SHACL architecture.
9. Globally, **80 % of the 267 decentralised-identity projects** analysed by the Web of Trust Map 2025 use W3C Verifiable Credentials, with more than 50 national programmes being deployed.
10. The regulatory path to complete operational treatment of W3C-VC in the EUDIW is **technically ready and regulatorily proposed**: eight symmetrical adaptations to those already applied to the other two formats, condensed into a regulatory proposal for CIR 2024/2977 (new Section 4.3 of Annex I) and CIR 2024/2979 (adaptation points 9–16 of Annex V).

## Ten requirements of lifelong learning

1. Native semantic expressiveness over authoritative European vocabularies.
2. Cross-border interoperability without intermediaries or bilateral mappings.
3. Verifiable issuer identity and assurance (including `eidasLegalIdentifier`).
4. Complete lifecycle with suspension + revocation.
5. Structural privacy (no "phone home", unlinkability, selective disclosure).
6. Integrated quality assurance with European educational quality frameworks.
7. Portability across formats, wallets and implementations.
8. Integration with OpenID4VCI / OpenID4VP protocols within the regulated HAIP.
9. Coverage of formal education, VET, secondary education, professional qualifications, CPD and informal learning.
10. Consistent verification with simultaneous support for VCDM 1.1 and VCDM 2.0 profiles during the transition.

The ten requirements are developed in [02 — Requirements of lifelong learning](./02-lifelong-learning-requirements.md) and their coverage by W3C-VCDM is detailed in [03 — Benefits of W3C-VCDM](./03-w3c-vcdm-benefits.md).

## Why now

- The **first batch of Implementing Acts** of Regulation 2024/1183 (CIR 2024/2977, CIR 2024/2979, CIR 2024/2982) is in force. W3C-VCDM 1.1 is the technical mandate for the syntactic layer.
- The **W3C VCDM 2.0 Recommendation** was published on 15 May 2025 together with the full package of complementary Recommendations (VC-JOSE-COSE, VC-Data-Integrity, Bitstring Status List, ECDSA Cryptosuites) and the BBS Cryptosuites Candidate Recommendation (3 April 2025).
- **ETSI TS 119 472-1 V1.1.1** (December 2025) contains clause 7 with the W3C-VC technical profile, already referenced by the Implementing Acts.
- The public consultation **Ref. Ares(2026)1286304** (5 February to early March 2026) gathered 43 contributions with broad convergence on the need to complete the W3C-VC profile in the EUDIW.
- The European ecosystem has invested **more than €80 million** of public funds in more than 200 organisations from more than 20 countries in solutions built on W3C-VCDM.

## Procedural recommendation

Maintain the reference to ETSI TS 119 472-1 without fixing a specific version and issue a **standardisation request to ETSI ESI** under Regulation (EU) No 1025/2012 to develop a **European High Assurance Interoperability Profile** that covers the three formats referenced in the EUDIW symmetrically. This approach — convergent across the 43 contributions to the public consultation — turns a round of regulatory clarifications into a **single European decision**, rather than 27 divergent national resolutions.

See [10 — Roadmap and recommendations](./10-roadmap.md) for concrete steps.

## Empirical evidence in summary

| Metric | Value |
|---|---|
| European public investment in W3C-VCDM | > €80M (ALASTRIA) |
| European projects on W3C-VCDM | DC4EU, ISBE, EBSI-VECTOR, Safe Island, PH4H, Sybol, TRACE4EU, Catena-X, Gaia-X |
| DC4EU — educational institutions | 36 in 16 Member States |
| DC4EU — population coverage | 89 % of the EU population |
| DC4EU — real credentials issued | 2,790 |
| DC4EU — credential types published | 18 (14 educational/professional + 4 QA) |
| DC4EU — funding | €19M Digital Europe Programme |
| CRUE Spanish Universities | 77 universities, 1.3M+ students |
| Global decentralised-identity projects on VC | 80 % of 267 (Web of Trust Map 2025) |
| National programmes on VC worldwide | > 50 (Bhutan, Singapore, Canada, USA, Australia, UAE, etc.) |

## Suggested next steps for the Commission

1. **Adopt** the new Section 4.3 of Annex I of CIR 2024/2977 with the encoding of the PID in JSON-LD W3C-VC (Table 9 with 27 attributes).
2. **Adopt** the adaptation points (9)–(16) of Annex V of CIR 2024/2979 with the rules for W3C-VC (normative references, dual schema, revocation, data structures, HAIP and OID4VCI).
3. **Issue** the standardisation request to ETSI ESI for the European High Assurance Interoperability Profile.
4. **Verify** that ETSI TS 119 472-3 covers the full OID4VCI flow for W3C-VC; if not, complete the coverage before the next amendment cycle.
5. **Recognise** explicitly the VCDM 1.1 (current) and VCDM 2.0 (forward-looking) profiles during the transition period.

---

**Key links**:

- [Context and foundations](./01-context-and-foundations.md)
- [Complete EUDI Wallet profile for W3C-VC](./08-eudiw-profile.md)
- [Roadmap and recommendations](./10-roadmap.md)
- [Annex B — Sources](./annexes/B-sources.md)
