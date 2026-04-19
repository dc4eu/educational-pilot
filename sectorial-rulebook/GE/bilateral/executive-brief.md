# Executive brief — Symmetrical treatment of W3C-VC in the EUDI Wallet profile

## Joint ES–DE position for the next cycle of Implementing Acts of Regulation (EU) 2024/1183

---

### 1. Context

The first batch of eIDAS 2.0 Implementing Acts (CIR 2024/2977, 2024/2979, 2024/2982) treats the three credential formats referenced by Regulation 2024/1183 — **mdoc**, **SD-JWT VC**, **W3C-VC** — with asymmetric operational depth. The Annexes articulate the operational treatment of mdoc (Section 4.1 Annex I, points (1)–(4) Annex V) and SD-JWT VC (Section 4.2 Annex I, points (5)–(8) Annex V); W3C-VC is referenced as an admissible format, with ETSI TS 119 472-1 V1.1.1 clause 7 as the technical anchor, **but the operational pieces are pending completion**.

The public consultation **Ref. Ares(2026)1286304** (43 contributions, closed early March 2026) evidenced broad convergence on the need to close this gap, and on the procedural path (standardisation request to ETSI ESI) to close it coherently at European level.

### 2. The ask

Complete the regulatory symmetry by **addition, not substitution**. Add to the Annexes the operational pieces that W3C-VC has ready in the ecosystem, leaving the existing treatment of mdoc and SD-JWT VC intact. No format is displaced; no deployment is broken; no Member State is asked to redeploy.

### 3. Five decisive arguments

**Cryptographic unlinkability (Article 3(10) CIR 2024/2982).** W3C BBS Cryptosuites v1.0 (Candidate Recommendation, 3 April 2025) realises mathematical unlinkability from a single base signature over BLS12-381. Batch issuance, the approximation available in SD-JWT VC, scales linearly with the expected number of presentations — for educational credentials presented over decades before heterogeneous verifiers, this is a significant operational and privacy cost. BBS+ is the only native Data Integrity cryptosuite in the EUDIW-referenced formats that realises the property cryptographically.

**Native European semantics at scale.** JSON-LD 1.1 with `@context` binds each attribute to resolvable IRIs of authoritative European vocabularies (EQF, ESCO, ISCED-F, NACE, ELI). SHACL shapes, published alongside the schema, execute semantic validation with standard open tools (pySHACL, Jena SHACL, TopBraid). For 24 official languages × 27 Member States × hundreds of credential types × thousands of issuers, this is the only architecture that scales without divergent national interpretations.

**Infrastructure and investment already in place.** ELM v3.2 and EDC v1.9 (DG EMPL, Europass), EBSI Trusted Schemas Registry v3, the DC4EU Sectoral EAA Catalogue (18 credential types), and four interoperable wallets independently validated (ISRAEL/Izertis, UAegean, Netcompany, Cappatrust) are in production. Aggregate European public investment on W3C-VCDM exceeds **€80M** (ALASTRIA + DC4EU + other LSPs).

**Empirical validation.** The DC4EU Large Scale Pilot covered **36 educational institutions in 16 Member States (89 % of the EU population)**, issued **2,790 real credentials** across the 18 catalogue types, and validated four wallet implementations exchanging those credentials. The European educational architecture is already operational on VCDM + ELM; there is nothing to invent.

**Global strategic positioning.** 80 % of the 267 global decentralised-identity projects tracked in the Web of Trust Map 2025 are built on W3C-VC. Open Badges 3.0 (1EdTech Consortium) is built on VCDM. The European educational sector trains citizens who work globally; format symmetry with the world's convergent ecosystem is a competitiveness decision, not a technicality.

### 4. The proposal — two concrete normative artefacts

**New Section 4.3 of Annex I of CIR 2024/2977**, symmetrical to Sections 4.1 (mdoc) and 4.2 (SD-JWT VC), with the encoding of the **27 PID attributes** in JSON-LD W3C-VC, admitted selective-disclosure mechanisms (BBS+ and salted-hash), status treatment (BitstringStatusList with revocation and suspension), and trust-framework references (EBSI TIR/TAOR).

**Adaptation points (9)–(16) of Annex V of CIR 2024/2979**, symmetrical to the eight adaptations already in place for the other formats: (9) normative references to W3C VCDM 1.1 and 2.0; (10) dual validation architecture JSON Schema + SHACL; (11) BitstringStatusList with revocation and suspension; (12) data structures (ELM v3.2, Sectoral EAA Catalogue, extension mechanisms); (13) HAIP applicable to W3C-VC; (14) OpenID4VCI formats and metadata; (15) OpenID4VP formats and `presentation_definition`; (16) admitted Data Integrity and JOSE/COSE cryptosuites.

### 5. Procedural path

**Standardisation request to ETSI TC ESI** under Regulation (EU) No 1025/2012, for a European High Assurance Interoperability Profile (EU HAIP) covering the three formats symmetrically. Advantages: (a) concentrates what would otherwise be 27 national clarifications into a single coherent European decision; (b) is versionable without amending the Implementing Acts (the Acts reference ETSI TS 119 472-1 without fixing a version); (c) is coordinated with W3C, IETF and OpenID Foundation through existing ETSI liaisons.

### 6. Political line

The proposal is **non-invasive**. Symmetry is obtained by addition. The existing operational treatment of mdoc and SD-JWT VC is preserved unchanged. What changes is that W3C-VC deployments — including the 36 DC4EU institutions, the national investments aggregated over the last four years, and the Europass/ELM backbone operated by DG EMPL — receive the same operational recognition that mdoc and SD-JWT VC deployments already have.

### 7. Single message if the conversation runs short

> "What is on the table is not choosing a format. It is deciding whether the EUDIW offers symmetrical treatment to the three formats that the Regulation itself references. The technical symmetry already exists; what is lacking is regulatory symmetry. Germany and Spain proposing that symmetry jointly is the move that turns 27 divergent national decisions into a coherent European decision."

### 8. Suggested joint actions

1. **Joint ES–DE statement** at the next Expert Group on the European Digital Identity, supporting the symmetrical completion of Annexes I and V.
2. **Co-sponsored letter** to DG CONNECT supporting the issuance of the ETSI ESI standardisation request under Regulation (EU) No 1025/2012.
3. **Alignment with DG EMPL** on the continuity of the Sectoral EAA Catalogue as post-DC4EU European infrastructure, as part of the Europass Dataspace.
4. **Bilateral technical workshop** (ES–DE) to converge on the operational pieces for Section 4.3 Annex I / points (9)–(16) Annex V before the next Expert Group meeting.

---

*Brief prepared as bilateral support material. Aligned with the public consultation Ref. Ares(2026)1286304 and with the technical documentation published in the Torsten_EN repository (chapters 00–10 + annexes A–C). Update if the bilateral reveals new regulatory inflections.*
