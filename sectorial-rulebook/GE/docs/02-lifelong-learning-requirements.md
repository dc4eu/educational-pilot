# 02 — Requirements of lifelong learning

This chapter enumerates the ten substantive requirements that digital credentialing of lifelong learning must satisfy within the EUDI Wallet framework. Each requirement is presented with its functional rationale, its regulatory basis and the concrete criteria that the technical solution must meet. The coverage of each requirement by W3C-VCDM is developed in [03 — Benefits of W3C-VCDM](./03-w3c-vcdm-benefits.md).

## R1 — Semantic expressiveness over authoritative European vocabularies

**Rationale.** An academic or professional qualification is not a string of text: it is a concept bound to European frameworks (EQF, ESCO, ISCED-F), to ontological classes (ELM `LearningAchievement`, `Assessment`, `AwardingProcess`), to relationships (achievement → learning outcome → competence → skill) and to controlled vocabularies (country, jurisdiction, field of knowledge). Without this semantic layer, automated cross-border interpretation is impossible.

**Criteria of the technical solution.**

- The credential must allow each property to resolve to an authoritative IRI in a European controlled vocabulary.
- The credential structure must express relationships between entities (an achievement is `specifiedBy` a specification, `provenBy` one or more assessments, `awardedBy` an awarding process).
- The format must allow vocabularies to be managed, versioned and resolved without depending on proprietary servers.
- Semantic validation must be executable by machines, not merely documented in prose.

**Regulatory basis.** Directives 2005/36/EC and 2013/55/EU on recognition of qualifications; Council Recommendation of 22 May 2018 on key competences; ELM v3.2; ESCO (Regulation (EU) No 661/2014); EQF (Recommendation of 22 May 2017).

## R2 — Cross-border interoperability without intermediaries or bilateral mappings

**Rationale.** Lifelong learning includes academic mobility (Erasmus+), professional mobility (recognition of regulated qualifications), recognition of prior learning (RPL, validation of non-formal learning) and participation in cross-border public procurement. In all these scenarios the credential must be interpretable automatically by the receiving system without the need for bilateral mappings between Member States, without human mediation and without case-by-case negotiation.

**Criteria of the technical solution.**

- The interpretation of the credential must be deterministic: the verifier arrives at the same semantic result regardless of its jurisdiction.
- The credential must self-describe the applicable rulebook, the active vocabulary and the rules for claim mapping.
- Interoperability must not depend on bilateral agreements between issuers and verifiers.
- The format must enable "diversity of implementations, unity of standard": diversity of wallets and implementations, unity of the semantic standard.

**Regulatory basis.** Article 26 TFEU (internal market); Directives on recognition of qualifications; Council Recommendation on microcredentials (2022); Digital Single Market Act.

## R3 — Verifiable issuer identity and assurance

**Rationale.** A credential is worth what its issuer is worth. The verifier must be able to establish with certainty: (a) who signs the credential, (b) that the issuer is legally authorised to issue this specific type of credential, (c) that the institutional accreditation chain (QA agency → institution → programme → credential) is traceable and verifiable, and (d) that the issuer's identity model complies with the eIDAS 2.0 framework.

**Criteria of the technical solution.**

- The issuer must have a verifiable `eidasLegalIdentifier` with explicit jurisdiction.
- Issuer authentication must combine **classical PKI (X.509v3)** with **decentralised PKI (DIDs)** according to the use case.
- Institutional accreditation must be verifiable as a separate credential (Accreditation Credential) chained to the sectoral Trust Anchor.
- The issuance infrastructure must support qualified electronic seals (QSealC) and qualified time-stamps (QTS) where the nature of the credential requires it.

**Regulatory basis.** Articles 1 to 6 of Regulation 2024/1183; ETSI EN 319 411-1; ETSI EN 319 412-1 V1.4.4; CIR 2024/2979 Annexes I–III.

## R4 — Complete lifecycle with suspension and revocation

**Rationale.** Educational and professional credentials are not permanent. Revocation may be necessary due to academic fraud, withdrawal of accreditation or correction of errors. Suspension is required by several Member States during ongoing investigations, appeals, pending renewals or precautionary measures. The lifecycle must support both states as semantically distinct.

**Criteria of the technical solution.**

- The status mechanism must differentiate `statusPurpose: "revocation"` (permanent) and `statusPurpose: "suspension"` (reversible).
- The mechanism must be privacy-preserving: no "phone home" calls to the issuer during verification.
- The mechanism must allow unlinkable queries that prevent correlation between verifications.
- Status credentials must themselves be digitally signed W3C-VC credentials, resolvable by any conformant European validation service.

**Regulatory basis.** Article 24 and Section 9 of Regulation 2024/1183; CIR 2024/2979 Annex V (adaptations 5 and 6 for SD-JWT VC, proposals 12 and 13 for W3C-VC).

## R5 — Structural privacy

**Rationale.** Lifelong learning generates a longitudinal portfolio of sensitive credentials that accompanies the citizen for decades. Privacy cannot be an optional policy: it must be built into the cryptographic architecture of the credential. The EUDIW enshrines this principle in Article 5a(16)(b) of Regulation 2024/1183 and in Article 3(10) of CIR 2024/2982.

**Criteria of the technical solution.**

- **Selective disclosure**: the holder reveals only the attributes necessary for each interaction.
- **Cryptographic unlinkability**: two verifications of the same credential to two different relying parties must not be mathematically correlatable.
- **No phone home**: verification does not reveal to the issuer when, where or to whom the credential is used.
- **Zero-knowledge readiness**: the architecture must admit evolution towards ZKP (proving "EQF ≥ 6" without revealing the exact level, "grade average ≥ X" without revealing individual grades).
- **Embedded Disclosure Policies**: the credential may include disclosure policies bound to the verifier's authorisations.

**Regulatory basis.** Article 5a(16)(b) Regulation 2024/1183; Article 3(10) CIR 2024/2982; GDPR (Arts. 5, 25); Charter of Fundamental Rights (Art. 8); ETSI TR 119 476-1 v1.3.1 §7.7.2.

## R6 — Integrated quality assurance

**Rationale.** European educational credentials operate within a quality-assurance ecosystem (ENQA, EQAR, national agencies) that confers recognised value on programmes and institutions. The digital credential must be able to transport or link the corresponding accreditation evidence, enabling the verifier to check automatically that the academic programme is accredited, that the institution is recognised and that the QA agency is a member of the EQAR register.

**Criteria of the technical solution.**

- Existence of an **Accreditation Credential** credential type (institutional, programme, QA agency, EQAR register).
- Chaining between the educational credential and the accreditation credential (verifiable without semantic rupture).
- Coverage of the European quality frameworks (ESG — European Standards and Guidelines, EQAR Register).
- Compatibility with periodic external-evaluation processes.

**Regulatory basis.** Council Recommendation of 24 September 1998 on cooperation in quality assurance; ESG 2015; statutes of ENQA and EQAR; Recommendation on microcredentials (2022).

## R7 — Portability across formats, wallets and implementations

**Rationale.** The European citizen will use their EUDI Wallet for decades, will change providers, will move their portfolio between devices, and will need their credentials to be verifiable before a myriad of verifiers with heterogeneous implementations. Portability cannot depend on proprietary APIs, closed platforms or monopolistic implementations.

**Criteria of the technical solution.**

- Verification must be possible by any software conformant with the specified cryptosuites, without APIs mediated by the operating system.
- The credential must be able to travel between wallets from different providers without loss of information or semantic fragmentation.
- Acceptable cryptosuites must be open, auditable and free from entry barriers due to royalties.
- Verification must operate offline when the situation requires it (classroom, campus, international events, areas with intermittent connectivity).
- The educational portfolio must be compatible with complementary global ecosystems (Open Badges 3.0, CTDL, LER) to facilitate extra-European mobility.

**Regulatory basis.** European Parliament Resolution P10_TA(2026)0022 on technological sovereignty; Regulation (EU) No 1025/2012 on standardisation; DSM interoperability principle.

## R8 — Integration with OpenID4VCI / OpenID4VP protocols

**Rationale.** The EUDIW operates over **OpenID4VCI** for issuance and **OpenID4VP** for presentation, with a European profile **HAIP (High Assurance Interoperability Profile)** formalised in Annex XIV of CIR 2024/2982. The educational credential must be able to traverse these protocols with normalised format identifiers covering both enveloping proofs (JOSE/COSE) and embedded proofs (Data Integrity).

**Criteria of the technical solution.**

- Format identifiers recognised in HAIP for issuance and presentation: `jwt_vc_json`, `vp+jwt`, `ldp_vc`, `ldp_vp`, `jwt_vc_json-ld`.
- Credential Issuer metadata (OID4VCI) including `@context`, `type`, cryptographic binding methods and supported proof types.
- Compatibility with the `eudi_wallet_info` object and with the `key_attestation` element of Annex III of CIR 2024/2979.
- End-to-end coverage validated in a reference implementation.

**Regulatory basis.** CIR 2024/2982 Annexes XIII and XIV; ETSI TS 119 472-3; OpenID4VCI and OpenID4VP (OpenID Foundation).

## R9 — Coverage of all modalities of learning

**Rationale.** Lifelong learning spans formal education (from secondary school to doctorate), vocational education and training (initial and continuing VET), higher education (bachelor's, master's, doctorate, microcredentials), regulated professional qualifications (medicine, engineering, architecture, law, health professions), non-formal learning (courses, workshops, corporate programmes) and informal learning (work experience, volunteering, autodidactic learning recognised by RPL).

**Criteria of the technical solution.**

- Credential types for diplomas, diploma supplements, transcripts of records, enrolment certificates and microcredentials in higher education (EUHED, EUHEDS, EUHETOR, EUHEPOE, EUHEMC).
- Credential types for VET: diploma, certificate, microcredential (EUVETD, EUVETC, EUVETMC).
- Credential type for secondary: certificate and transcript (EUUSC, EUUSTOR).
- Credential types for professional qualifications: fitness-to-practise, medical training, CPD, professional training (CPS, AMT, CPD, PTC).
- Credential types for quality assurance: institutional, programme, QA agency, EQAR register accreditation.
- Three proven deployment models to accommodate institutional diversity (self-hosting, managed service, national coordination).

**Regulatory basis.** Recommendation on microcredentials (2022); ELM v3.2; ESG 2015; European Education Area strategy; sectoral catalogues validated in DC4EU.

## R10 — Consistent verification with VCDM 1.1 and VCDM 2.0 profiles

**Rationale.** The first batch of Implementing Acts takes W3C-VCDM 1.1 as its reference. The W3C VCDM 2.0 Recommendation (15 May 2025) is forward-looking. Lifelong learning demands that credentials issued today (1.1 profile) remain verifiable in the future, and that credentials issued tomorrow (2.0 profile) can coexist with current ones without breaking the trust of already deployed verifiers.

**Criteria of the technical solution.**

- The verifier detects the profile by inspecting the cardinality and types of the `credentialSchema[]` array:
  - One entry of type `JsonSchema` → VCDM 1.1 profile.
  - Two entries (`JsonSchema` + `ShaclValidator2017` / `ShaclSchemaCredential`) → VCDM 2.0 profile.
- The verifier applies syntactic validation (JSON Schema) to the 1.1 profile and syntactic + semantic validation (JSON Schema + SHACL) to the 2.0 profile.
- Both profiles are accepted during the transition period, and both are expected to continue being accepted when future updates to the Implementing Acts also recognise VCDM 2.0.
- Schemas and shapes are registered in EBSI TSR v3 as immutable resources.

**Regulatory basis.** ETSI TS 119 472-1 V1.1.1 clause 7.2.1.3; W3C Recommendations of 15 May 2025; EDC profile; EBSI TSR v3.

---

**Next links**:

- [03 — Benefits of W3C-VCDM](./03-w3c-vcdm-benefits.md)
- [04 — Dual validation architecture](./04-dual-validation-architecture.md)
- [06 — Lifecycle and trust](./06-lifecycle-and-trust.md)
