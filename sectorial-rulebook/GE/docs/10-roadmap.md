# 10 — Roadmap and recommendations

## 10.1 Guiding principle

The roadmap is articulated on the principle of **regulatory symmetry between the three formats** referenced in the EUDIW: mdoc, SD-JWT VC and W3C-VC. The objective is not to rearrange the existing regulatory architecture, but to complete it with what the ecosystem already has operational and what public consultation Ref. Ares(2026)1286304 has evidenced as a consensual need.

The tone of the recommendations is **positive and constructive**: each proposal describes what is added and how it is added without touching the already functional elements of the other formats.

## 10.2 Time horizon

| Horizon | Period | Content |
|---|---|---|
| **Short term** | 2026 | Adoption of the proposed normative artefacts (Section 4.3 Annex I CIR 2024/2977, points (9)–(16) Annex V CIR 2024/2979). Issuance of the standardisation request to ETSI ESI, including ETSI TS 119 312 revision scope. |
| **Medium term** | 2026–2027 | Publication of the European HAIP by ETSI ESI. Revision of ETSI TS 119 312 to incorporate privacy-preserving cryptographic mechanisms (BLS12-381/`bbs-2023`). Consolidation of the Sectoral EAA Catalogue as post-DC4EU infrastructure. |
| **Long term** | 2027+ | Regulatory activation of `bbs-2023` unlinkability upon ETSI TS 119 312 incorporation. Sectoral extension to health, mobility, finance, defence. Integration with global ecosystems (Open Badges 3.0, CTDL, LER). |

## 10.3 Recommendations to the European Commission

### 10.3.1 Completing regulatory symmetry

- **Adopt** the new Section 4.3 of Annex I of CIR 2024/2977, with Table 9 of the 27 PID attributes in JSON-LD W3C-VC, prescribing **JAdES-B-B** (ETSI TS 119 182-1) as the enveloping signature for QEAAs and `ecdsa-rdfc-2019` for embedded Data Integrity proofs, as a symmetrical complement to Sections 4.1 (mdoc) and 4.2 (SD-JWT VC).
- **Adopt** adaptation points (9)–(16) of Annex V of CIR 2024/2979 with the operational rules for W3C-VC (normative references, dual schema, revocation, data structures, HAIP, OID4VCI, OID4VP, cryptography).
- **Recognise** explicitly **VCDM 2.0** as the forward-looking target. VCDM 1.1 credentials remain valid during the transition period; the transition is technically straightforward via the `@context` mechanism and does not require parallel issuance infrastructure.

### 10.3.2 Standardisation request to ETSI ESI

- **Issue** a standardisation request to **ETSI TC ESI** under Regulation (EU) No 1025/2012 for the development of a **European High Assurance Interoperability Profile (EU HAIP)**. The profile:
  - Covers symmetrically the three credential formats.
  - Integrates VCDM 2.0, mdoc and SD-JWT VC in a common conformance matrix.
  - Is versionable without modification of the Implementing Acts.
  - Is coordinated with the OpenID Foundation for the treatment of OID4VCI and OID4VP.
  - **Includes in its scope** the revision of ETSI TS 119 312 to incorporate privacy-preserving cryptographic mechanisms, specifically BLS12-381-based schemes (`bbs-2023`), providing the regulatory pathway for the cryptographic unlinkability obligation of Article 3(10) of CIR 2024/2982.

### 10.3.3 Verification of protocol coverage

- **Verify** that the next revision of **ETSI TS 119 472-3** covers the full OID4VCI flow for W3C-VC; otherwise, include this coverage in the standardisation request.

### 10.3.4 ENISA cryptographic mechanisms

- **Request** ENISA to include BLS12-381 and BBS-family schemes in a forthcoming update of the Agreed Cryptographic Mechanisms list, coordinated with the ETSI TS 119 312 revision, to resolve the current situation where Article 3(10) of CIR 2024/2982 creates a legal obligation for unlinkability without an agreed cryptographic mechanism to implement it.

### 10.3.5 Multilateral coherence with international initiatives

- **Maintain coherence** with international initiatives on educational credentials (Open Badges 3.0, CTDL, LER, Groningen Declaration Network) through active participation in the corresponding forums and updated bilateral mappings.

## 10.4 Recommendations to Member States

### 10.4.1 Recognition of the dual profile

- **Recognise** the dual validation architecture (JSON Schema + SHACL) as a normal mechanism of conformance for educational EAAs issued by national bodies.
- **Facilitate** the registration of educational issuers (universities, VET centres, employers with CPD programmes) in the **EBSI Trusted Issuers Registry**.
- **Accredit** the national educational quality agencies in the **Trusted Accreditation Organisations Registry**.

### 10.4.2 Alignment with national qualifications frameworks

- **Publish** the correspondence between the national qualifications framework and the EQF through resolvable IRIs in the `http://data.europa.eu/snb/eqf/` namespace, as ELM requires.
- **Maintain** the national Trusted Lists with active educational Qualified Trust Service Providers, integrated into the European LOTL.

### 10.4.3 Investment in the ecosystem

- **Give continuity** to the investments initiated in the LSPs (DC4EU, TRACE4EU, EBSI-VECTOR) through successor consortia that maintain the Sectoral EAA Catalogue, the SHACL shapes and the operational registries.

## 10.5 Recommendations to educational issuers

### 10.5.1 Progressive adoption

- **Integrate** the W3C-VCDM into existing issuance systems (SISs, VET registries, continuing-training platforms) following the proposed EUDIW profile. New deployments should target **VCDM 2.0** directly.
- **Adopt** the dual architecture (JSON Schema + SHACL) from the outset.
- **Issue** with **JAdES-B-B** qualified seals for QEAAs, using the existing QSealC infrastructure.
- **Register** the institutional DID in the EBSI TIR and link it to the `eidasLegalIdentifier`.

### 10.5.2 Capacity building

- **Train** IT teams and the academic units responsible for credential management in the principles of VCDM 2.0, ELM, JAdES-B-B, SHACL and the OID4VCI/VP protocols.
- **Participate** in sectoral working groups (EUNIS, CRUE, DC4EU consortia and successors) to consolidate good practice.

### 10.5.3 Coherence with the quality assurance policy

- **Articulate** the issuance of EAAs with internal quality assurance processes and with the accrediting agencies (ENQA, EQAR, member national agencies) through verifiable `Accreditation` credentials.

## 10.6 Recommendations to the technical community

### 10.6.1 W3C Verifiable Credentials Working Group

- **Give continuity** to the development of the VCDM with attention to the needs of the European educational sector.
- **Finalise** the transition of the Candidate Recommendation of BBS Cryptosuites v1.0 to Recommendation, with European implementers as early adopters.
- **Coordinate** with ETSI ESI and the OpenID Foundation for cross-cutting coherence.

### 10.6.2 ETSI TC ESI

- **Operationalise** rapidly the standardisation request once issued.
- **Advance** the revision of ETSI TS 119 312 to include privacy-preserving cryptographic mechanisms (BLS12-381/BBS family), resolving the gap between the Article 3(10) legal obligation and the available agreed mechanisms.
- **Maintain** ETSI TS 119 472-1 updated with the most recent W3C Recommendations without introducing divergent proprietary requirements.
- **Publish** clear and verifiable conformance criteria for each of the three formats of the profile.

### 10.6.3 OpenID Foundation

- **Maintain** OpenID4VCI and OpenID4VP with first-class support for the W3C-VC formats, including `ldp_vc` and `jwt_vc_json-ld`.
- **Collaborate** with ETSI and W3C in the definition of the European HAIP.

### 10.6.4 1EdTech, Credential Engine, Groningen Declaration Network

- **Maintain** convergence with the European VCDM ecosystem through documented mappings and format-conversion tools.

## 10.7 Recommendations to DC4EU and successors

- **Transfer** the Sectoral EAA Catalogue to a post-pilot governance structure (permanent consortium or DG EMPL unit) that guarantees its maintenance.
- **Publish** the credentials issued in the pilot as public reference material (subject to the consent of the persons involved and with personal data protected).
- **Document** the lessons learned from the deployment in 16 Member States so that they serve new entrants.

## 10.8 Success indicators

| Indicator | Target 2026 | Target 2030 |
|---|---|---|
| Member States with registered issuers | 20 | 27 |
| Universities issuing EAA over W3C-VCDM | 200 | 1,000 |
| VET centres issuing | 100 | 500 |
| Enterprises issuing CPD | 50 | 500 |
| EAAs issued annually | 100,000 | 10,000,000 |
| Wallets with certified W3C-VC support | 6 | 20 |
| Operational verifiers | 100 | 5,000 |
| Types in the Sectoral EAA Catalogue | 18 | 40 |
| ETSI TS 119 312 revision incorporating BLS12-381 | — | Completed by 2027 |

## 10.9 Risks and mitigations

1. **National fragmentation**: the risk that each Member State adopts divergent interpretations of the profile. Mitigation: the standardisation request to ETSI ESI concentrates a single European decision.
2. **Misalignment with global ecosystems**: the risk that the European profile moves away from Open Badges 3.0, CTDL or LER. Mitigation: active participation in the corresponding forums and maintenance of documented mappings.
3. **Loss of post-pilot continuity**: the risk that the Sectoral EAA Catalogue loses traction when DC4EU ends. Mitigation: transfer to a permanent governance structure and successor funding under the Digital Europe Programme.
4. **Delayed ETSI TS 119 312 revision**: the risk that the unlinkability gap persists if the ETSI revision is slow. Mitigation: explicit inclusion in the standardisation request scope; ENISA cryptographic mechanisms update as a parallel track; optional forward-compatible implementation of `bbs-2023` by early adopters.

## 10.10 Executive summary of the roadmap

1. The **complete technical profile** for W3C-VC is ready, with JAdES-B-B as the operative qualified signature and a clear pathway for `bbs-2023` unlinkability.
2. The **symmetrical regulatory proposal** (Section 4.3 Annex I CIR 2024/2977, points (9)–(16) Annex V CIR 2024/2979) is non-invasive and feasible in the next amendment cycle.
3. The **standardisation request to ETSI ESI** — including ETSI TS 119 312 revision scope — is the procedural mechanism that converts the regulatory decision into a single European operation.
4. The **Member States** already have the elements at their disposal (Trusted Lists, national qualifications frameworks, QSealC infrastructure, accreditable issuers).
5. The **educational issuers** already have the artefacts (JSON Schemas, SHACL shapes, ELM profiles, JAdES-B-B implementations) and the reference implementations.
6. The **international technical community** (W3C, ETSI, OpenID, 1EdTech, Credential Engine, DC4EU) is available to coordinate.
7. The **public consultation Ref. Ares(2026)1286304** has evidenced convergence on the need and on the proposed approach.

The moment is propitious: all the ingredients are in place. What remains is the formal decision of the Commission to activate the regulatory symmetry.

---

**Start of the annexes**: [Annex A — Glossary](./annexes/A-glossary.md) · [Annex B — Sources](./annexes/B-sources.md) · [Annex C — Stakeholders and evidence](./annexes/C-stakeholders-evidence.md)
