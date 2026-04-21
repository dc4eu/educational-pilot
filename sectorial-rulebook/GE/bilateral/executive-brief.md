# Executive brief — Symmetrical treatment of W3C-VC in the EUDI Wallet profile

## Joint ES–DE position for the next cycle of Implementing Acts of Regulation (EU) 2024/1183

---

### 1. Context

The first batch of eIDAS 2.0 Implementing Acts (CIR 2024/2977, 2024/2979, 2024/2982) treats the three credential formats referenced by Regulation 2024/1183 — **mdoc**, **SD-JWT VC**, **W3C-VC** — with asymmetric operational depth. The Annexes articulate the operational treatment of mdoc (Section 4.1 Annex I, points (1)–(4) Annex V) and SD-JWT VC (Section 4.2 Annex I, points (5)–(8) Annex V); W3C-VC is referenced as an admissible format, with ETSI TS 119 472-1 V1.1.1 clause 7 as the technical anchor — which already prescribes **JAdES-B-B** as the operative enveloping signature (clause 7.6.4.2) — **but the operational pieces for the Annexes are pending completion**.

The public consultation **Ref. Ares(2026)1286304** (43 contributions, closed early March 2026) evidenced broad convergence on the need to close this gap, and on the procedural path (standardisation request to ETSI ESI) to close it coherently at European level.

### 2. The ask

Complete the regulatory symmetry by **addition, not substitution**. Add to the Annexes the operational pieces that W3C-VC has ready in the ecosystem, leaving the existing treatment of mdoc and SD-JWT VC intact. No format is displaced; no deployment is broken; no Member State is asked to redeploy.

### 3. Five decisive arguments

**JAdES-B-B: the operative European signature, accepted by all governments.** ETSI TS 119 472-1 V1.1.1 clause 7.6.4.2 already prescribes **JAdES-B-B** (ETSI TS 119 182-1) as the signature for W3C-VC QEAAs with JOSE enveloping proofs. JAdES is the European standard for advanced electronic signatures on JSON content, accepted under eIDAS 2.0 by all EU Member State governments, and directly referenced in CIR 2024/2979 Annex IV. The regulatory machinery for W3C-VC qualified signatures is already in place; what is missing is its expression in the operational pieces of the Implementing Acts Annexes.

**Pathway to cryptographic unlinkability (Article 3(10) CIR 2024/2982).** Article 3(10) creates a legal obligation for unlinkability at LoA High for which no format currently listed in Annex XIV provides a compliance path. The `bbs-2023` cryptosuite (W3C Candidate Recommendation, 3 April 2025) over BLS12-381 is the identified technical mechanism to satisfy this requirement — it realises mathematical unlinkability from a single base signature. Its adoption in the EUDIW perimeter follows the incorporation of BLS12-381-based schemes into ETSI TS 119 312, which is under active revision. The Commission standardisation request to ETSI ESI should include this revision in its scope. Until that incorporation, selective disclosure is available via SD-JWT salted-hash on the same JSON payload.

**Native European semantics at scale.** JSON-LD 1.1 with `@context` binds each attribute to resolvable IRIs of authoritative European vocabularies (EQF, ESCO, ISCED-F, NACE, ELI). SHACL shapes, published alongside the schema, execute semantic validation with standard open tools (pySHACL, Jena SHACL, TopBraid). For 24 official languages × 27 Member States × hundreds of credential types × thousands of issuers, this is the only architecture that scales without divergent national interpretations.

**Infrastructure and investment already in place.** ELM v3.2 and EDC v1.9 (DG EMPL, Europass), EBSI Trusted Schemas Registry v3, the DC4EU Sectoral EAA Catalogue (18 credential types), and four interoperable wallets independently validated (Identify/Izertis, UAegean, Netcompany, Cappatrust) are in production. Aggregate European public investment on W3C-VCDM exceeds **€80M** (ALASTRIA + DC4EU + other LSPs). Global wallet support is documented at **https://canivc.com** (50+ implementations).

**Global strategic positioning.** 80 % of the 267 global decentralised-identity projects tracked in the Web of Trust Map 2025 are built on W3C-VC. Open Badges 3.0 (1EdTech Consortium) is built on VCDM. The European educational sector trains citizens who work globally; format symmetry with the world's convergent ecosystem is a competitiveness decision, not a technicality.

### 4. The proposal — two concrete normative artefacts

**New Section 4.3 of Annex I of CIR 2024/2977**, symmetrical to Sections 4.1 (mdoc) and 4.2 (SD-JWT VC), with the encoding of the **27 PID attributes** in JSON-LD W3C-VC. The section specifies: JAdES-B-B as the enveloping signature for QEAAs; `ecdsa-rdfc-2019` as the operative embedded-proof cryptosuite; selective-disclosure mechanisms (SD-JWT salted-hash today; `bbs-2023` upon ETSI TS 119 312 incorporation); status treatment (BitstringStatusList with revocation and suspension); and trust-framework references (EBSI TIR/TAOR).

**Adaptation points (9)–(16) of Annex V of CIR 2024/2979**, symmetrical to the eight adaptations already in place for the other formats: (9) normative references to W3C VCDM 2.0 and 1.1; (10) dual validation architecture JSON Schema + SHACL; (11) BitstringStatusList with revocation and suspension; (12) data structures (ELM v3.2, Sectoral EAA Catalogue, extension mechanisms); (13) HAIP applicable to W3C-VC; (14) OpenID4VCI formats and metadata; (15) OpenID4VP formats and `presentation_definition`; (16) cryptography — JAdES-B-B (enveloping), `ecdsa-rdfc-2019` (embedded Data Integrity), `bbs-2023` (upon ETSI TS 119 312 incorporation).

### 5. Procedural path

**Standardisation request to ETSI TC ESI** under Regulation (EU) No 1025/2012, for a European High Assurance Interoperability Profile (EU HAIP) covering the three formats symmetrically. The request should include in its scope the ongoing revision of ETSI TS 119 312 to incorporate privacy-preserving cryptographic mechanisms, providing the regulatory pathway for `bbs-2023`. Advantages: (a) concentrates what would otherwise be 27 national clarifications into a single coherent European decision; (b) is versionable without amending the Implementing Acts; (c) is coordinated with W3C, IETF and OpenID Foundation through existing ETSI liaisons.

### 6. Political line

The proposal is **non-invasive**. Symmetry is obtained by addition. The existing operational treatment of mdoc and SD-JWT VC is preserved unchanged. What changes is that W3C-VC deployments — including the 36 DC4EU institutions, the national investments aggregated over the last four years, and the Europass/ELM backbone operated by DG EMPL — receive the same operational recognition that mdoc and SD-JWT VC deployments already have.

### 7. Single message if the conversation runs short

> "What is on the table is not choosing a format. It is deciding whether the EUDIW offers symmetrical treatment to the three formats that the Regulation itself references. The technical symmetry already exists — including a government-accepted European signature standard (JAdES-B-B) and a clear pathway to unlinkability via ETSI TS 119 312; what is lacking is regulatory symmetry. Germany and Spain proposing that symmetry jointly is the move that turns 27 divergent national decisions into a coherent European decision."

### 8. Suggested joint actions

1. **Joint ES–DE statement** at the next Expert Group on the European Digital Identity, supporting the symmetrical completion of Annexes I and V.
2. **Co-sponsored letter** to DG CONNECT supporting the issuance of the ETSI ESI standardisation request under Regulation (EU) No 1025/2012, with explicit inclusion of ETSI TS 119 312 revision scope for privacy-preserving cryptography.
3. **Alignment with DG EMPL** on the continuity of the Sectoral EAA Catalogue as post-DC4EU European infrastructure, as part of the Europass Dataspace.
4. **Bilateral technical workshop** (ES–DE) to converge on the operational pieces for Section 4.3 Annex I / points (9)–(16) Annex V before the next Expert Group meeting.

---

*Brief prepared as bilateral support material. Aligned with the public consultation Ref. Ares(2026)1286304 and with the technical documentation published in the Torsten_EN repository (chapters 00–10 + annexes A–C). Update if the bilateral reveals new regulatory inflections.*
