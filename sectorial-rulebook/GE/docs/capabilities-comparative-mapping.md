# Comparative capability mapping — technical working notes

> **Internal working note.** This document is not part of the numbered series 00–10 nor of annexes A–C. It is not referenced from the index nor from the repository's navigation. Its function is to serve as technical support for bilateral conversations — in particular, the negotiation of joint positions for the revision of the Implementing Acts of Regulation (EU) 2024/1183. The tone differs deliberately from the rest of the repository: here we analyse, for each unique capability of W3C-VCDM identified in chapter 09, the foreseeable objection from the SD-JWT VC perspective, the honest technical reading of that objection, and the appropriate reply.
>
> The final table orders the 15 capabilities by **argument strength** to facilitate conversational prioritisation: which points deserve insistence, which are honest ties, and which it is better to concede rather than to defend.

## 0. Principles of use

Three principles guide the use of this material:

**Technical honesty.** The interlocutors on the other side of the table (in particular the German SPRIND / BMDS teams) have comparable technical depth. Weak, exaggerated or inaccurate arguments will be detected in seconds and will erode the credibility of the rest. When a capability is a real operational tie, this document recognises it explicitly.

**Selective asymmetry.** Not all 15 capabilities are decisive. Approximately six constitute strong differentiators of VCDM for lifelong learning; another six are moderate or contextual advantages; three are technical ties. The negotiation should concentrate on the six strong differentiators and avoid dispersing into the ties.

**Requirements-first framing.** The most powerful technical reply does not consist of defending VCDM as a format, but of deriving the requirements from the educational use cases and observing which format covers them natively and which requires extensions, out-of-band metadata or bilateral agreements. The format is a consequence, not a premise.

## 1. U1 — Native semantics with European controlled vocabularies

**Capability.** JSON-LD 1.1 with `@context` that links each attribute to resolvable IRIs of authoritative vocabularies (EQF, ESCO, ISCED-F, NACE, ELI, national frameworks). The derivable RDF graph allows any consumer to confirm the semantics without out-of-band metadata.

**Foreseeable objection.** "SD-JWT VC can include typed claims with URI values pointing to EQF codes. The practical effect is equivalent."

**Technical analysis.** It is not equivalent. In SD-JWT VC the semantic link is *conventional*: the profile document describes that the `qualification_level` claim should contain an EQF URI, but the verifier has no canonical way of checking at verification time that the URI effectively belongs to the authoritative scheme, nor of deriving the RDF triples that would enable automated reasoning. In VCDM with `@context`, the expansion to RDF is deterministic and verifiable by any standard JSON-LD engine; SHACL operates on the resulting graph. The difference is not theoretical: in a credential with 30 attributes referenced to six vocabularies, the cost of implementing semantic validation by convention in SD-JWT VC grows linearly with each credential type, whereas in VCDM it is zero marginal cost.

**Suggested reply.** "It is not a question of whether a URI can be in a claim. It is a question of whether the verifier can check, without external documentation and without logic specific to each type, that the value belongs to the authoritative vocabulary. JSON-LD makes that link declarative and executable; the alternatives leave it as a convention implemented ad hoc by each consumer. At the scale of 27 Member States × 24 languages × hundreds of credential types, the difference is operational, not theoretical."

**Strength.** High. Structural differentiator.

## 2. U2 — Dual validation JSON Schema + SHACL

**Capability.** Complementary execution of syntactic validation (JSON Schema) and semantic validation (SHACL over RDF) on the same credential, with open standard tools.

**Foreseeable objection.** "SD-JWT VC supports JSON Schema for structure. Semantic validation can be implemented in the application layer of the verifier."

**Technical analysis.** Moving semantic validation to the application layer means that each verifier implements its own business rules. In a multi-issuer, multi-type, multi-sectoral ecosystem, this produces 27 divergent interpretations of the same credential. SHACL resolves this with an artefact published together with the schema, executable by any conformant engine (pySHACL, Jena SHACL, TopBraid, shacl-js). Coherent ECTS ↔ EQF rules, validity of ISCED-F codes, accreditation of the issuer, can be expressed once and executed everywhere.

The fine point: SD-JWT VC can, in theory, be accompanied by JSON Schema extended with custom semantics (for example, via OpenAPI-style `x-` extensions). But that is no longer a standard: it is a local dialect. SHACL is a W3C Recommendation since July 2017, operated in production by EBSI TSR v3.

**Suggested reply.** "Semantic validation exists in both ecosystems. The difference is where it lives: in a standard artefact published together with the schema (SHACL) or in the verifier's code. The first option produces an interoperable ecosystem; the second produces 27 national variants. For educational credentials that cross borders, the difference is the cost of adoption for the verifiers."

**Strength.** High. Structural differentiator.

## 3. U3 — Lifecycle with native suspension and revocation

**Capability.** `BitstringStatusList` as a W3C Recommendation with the two `statusPurpose`s (`"revocation"` and `"suspension"`) treated natively.

**Foreseeable objection.** "IETF Token Status List (draft-ietf-oauth-status-list) covers the same pattern for SD-JWT VC, including suspension."

**Technical analysis.** A valid objection. Token Status List offers equivalent functionality in terms of mechanism. The real differences are three: (a) BitstringStatusList is a W3C Recommendation published on 15 May 2025, already operated in DC4EU and EBSI in production; Token Status List is in IETF draft with fewer documented educational deployments. (b) The status list in the VCDM world is itself a Verifiable Credential signed, which produces homogeneity of envelope and of verification; in SD-JWT VC the list has a JWT envelope different from that of the credential. (c) Production history: BitstringStatusList has three years of accumulated operational deployment in EBSI + DC4EU + ISBE.

**Suggested reply.** "Both ecosystems cover suspension and revocation. What varies is deployment maturity. BitstringStatusList is in production in DC4EU with 2,790 operational credentials; Token Status List is documented and has implementations, but the body of educational deployment is smaller. If the joint position wants to avoid operational risk in 2026, the mature path for the educational sector is the existing one."

**Strength.** Medium. Differentiator by maturity, not by capability.

## 4. U4 — Absence of "phone home" effect

**Capability.** Aggregated status lists downloadable once and cacheable; the issuer does not observe individual presentations.

**Foreseeable objection.** "Token Status List offers exactly the same pattern. The property is format-agnostic."

**Technical analysis.** Correct. The architectural pattern can be realised in both formats. There is no differentiator.

**Suggested reply.** Do not insist on this point as a format differentiator. If it comes up, recognise that both formats support the pattern and move the conversation to the next point. It can be mentioned as a desirable property of the educational ecosystem in general, but not as a pro-VCDM argument.

**Strength.** Tie. Do not defend.

## 5. U5 — Native cryptographic unlinkability with BBS+

**Capability.** Cryptosuite `bbs-2023` (W3C Candidate Recommendation, 3 April 2025) over BLS12-381 that produces derivations of the same credential that are cryptographically uncorrelatable with each other. Natively satisfies Article 3(10) of Regulation 2024/2982 for LoA High.

**Foreseeable objection.** "SD-JWT VC can achieve pseudo-unlinkability through batch issuance: the issuer issues N copies of a single-use credential, the wallet presents them sequentially."

**Technical analysis.** These are two technically distinct properties.

Batch issuance provides *limited statistical unlinkability*: if N copies are presented, the verifiers cannot correlate presentations 1 and 2, but they do know that the holder received N copies. It scales with N. If N runs out, re-issuance is needed. If N is small, the unlinkability is weak. The operational cost grows: each educational credential potentially presentable hundreds of times throughout a professional career requires the issuer to pre-issue hundreds of copies, and for the wallet to manage them.

BBS+ with `bbs-2023` provides *mathematical cryptographic unlinkability*: from a single base signature, the holder generates infinite uncorrelatable presentations. The operational cost is: one issuance, infinite presentations, zero pre-computation on the part of the issuer.

For educational credentials (diplomas, microcredentials, professional certificates) that are presented over decades before heterogeneous verifiers, the operational difference is significant.

A secondary objection exists: "BBS+ is in Candidate Recommendation, not final Recommendation". True; but the specification is technically stable (the CR was published in April 2025 after broad consensus), there are implementations in Rust and JavaScript, and the expected status of Recommendation will be reached during 2026. For the IA cycle we are discussing, the maturity is sufficient.

**Suggested reply.** "Batch issuance covers an operational approximation to unlinkability, but does not realise the cryptographic property in the sense of Article 3(10). For educational credentials that are presented hundreds of times over a professional life, pre-issuing hundreds of copies per person per credential type multiplies the issuer's operational obligations without closing the door to correlation. BBS+ realises unlinkability from a single base signature, and the standard is in Candidate Recommendation with mature implementations. This is a concrete differentiator of the VCDM ecosystem that is not accidental, but the result of years of specific cryptographic work."

**Strength.** Maximum. This is the most solid technical differentiator of VCDM for LoA High in education.

## 6. U6 — Hybrid trust model PKI eIDAS ↔ dPKI EBSI

**Capability.** Coexistence of the qualified PKI chain (QTS, LOTL) with the decentralised EBSI registers (TIR, TAOR, TSR, revocation).

**Foreseeable objection.** "SD-JWT VC works cleanly with classical eIDAS PKI. The EBSI dPKI adds operational complexity."

**Technical analysis.** The objection has some truth: there is nothing in SD-JWT VC that prevents it from integrating with EBSI, and there is nothing in VCDM that obliges the use of EBSI. The choice of trust model is orthogonal to the format. The value of EBSI resides in the European public investment made (Commission + Member States) and in the existence of the operational registers (TIR, TAOR with quality agencies, TSR v3 with the schemas of the sectoral catalogue).

What VCDM contributes distinctively is the *recursive credential model*: an `Accreditation` is a Verifiable Credential; a status list is a Verifiable Credential; a presentation is a Verifiable Presentation — all with the same envelope. This simplifies reasoning about the trust graph.

**Suggested reply.** Do not present this as a format differentiator. Present it as *optimal integration with the European investment already made*. The question is: given that EBSI exists and is operational, which format integrates with least friction? The answer is VCDM due to the recursive model. But the objection "we could use SD-JWT VC over EBSI" is not technically false.

**Strength.** Medium. Argument of integration, not of intrinsic capability.

## 7. U7 — Multilingual traceability

**Capability.** The labels of the controlled vocabularies (EQF, ESCO, ISCED-F) are published in the 24 official languages of the EU with canonical IRIs. An ELM credential renders in any language without reissuance nor modification of the payload.

**Foreseeable objection.** "SD-JWT VC can include multilingual strings as claim values. Germany already does so in some implementations."

**Technical analysis.** Multilingual strings can be embedded in SD-JWT VC, true. But the architecture is different:

- In VCDM + ELM, the credential references a canonical IRI (`eqf:7`); the wallet or the verifier resolves the IRI and obtains the localised label in any language, through the vocabulary published by the EU. The credential is small and stable.
- In SD-JWT VC with multilingual embedding, the issuer must include the 24 translations in each credential, or agree with the verifier that localisations will be downloaded out of band. The payload grows; the responsibility for translation falls on the issuer for each credential type.

For a single issuer with a single credential type, the difference is minor. For the aggregate ecosystem (thousands of issuers, tens of types, 24 languages), the difference is significant. Also for the size of the credential and its transmission in mobile contexts with limited bandwidth.

**Suggested reply.** "Both approaches work. The difference is where the localisation burden resides. VCDM+ELM delegates it to the vocabularies published by the EU, already multilingual by definition. Any other path obliges the educational issuer — a university, a VET centre — to maintain translations of their own credential, or the verifiers to implement proprietary localisation resolution. The cost multiplies by issuer and by type."

**Strength.** High. Structural differentiator with clear operational impact.

## 8. U8 — Compatibility with global ecosystems (Open Badges 3.0, CTDL, LER)

**Capability.** Open Badges 3.0 built on VCDM; documented mappings with CTDL (Credential Engine) and LER; 80 % of 267 global decentralised-identity projects over W3C-VC.

**Foreseeable objection.** "The EUDIW is a European ecosystem. Compatibility with Open Badges 3.0 / CTDL / LER is desirable but not a requirement."

**Technical analysis.** The objection has weight from the perspective of a regulator who defines strictly the EUDIW perimeter. But the EUDIW users — in particular students, professionals, persons in continuing training — do not live within the perimeter. An engineer trained in Munich works in Singapore; a doctor trained in Barcelona publishes in Boston; a VET technician trained in Lyon works in Toronto. If the European credential is illegible in the rest of the world without reissuance, the cost is borne by these users and, with them, by the European labour market.

The strategic question for the bilateral: do we want an EUDIW that *is* a de facto global standard for education, or an EUDIW that *requires bridges* with the rest of the world? The answer has consequences for the competitiveness of the European educational system.

**Suggested reply.** "The format decision has a strategic component beyond the technical perimeter. The European educational sector competes in a global market; its graduates work globally; its researchers publish globally. 80 % of the global ecosystem of digital credentials converges on VCDM. Choosing a different format for the European educational core creates friction at every border. It is not an argument of format capability, but of positioning of the EUDIW in the world ecosystem."

**Strength.** High. Strategic-political argument, not strictly technical.

## 9. U9 — Digital sovereignty by design

**Capability.** All specifications (VCDM, VC-Data-Integrity, VC-JOSE-COSE, BitstringStatusList, BBS, ECDSA, JSON-LD, SHACL) are W3C Recommendations or open ETSI standards.

**Foreseeable objection.** "SD-JWT VC is also an open standard (IETF OAuth WG). Digital sovereignty is symmetrical."

**Technical analysis.** Correct. Both ecosystems are open. Resolution P10_TA(2026)0022 applies to both.

**Suggested reply.** Recognise symmetry. Avoid insisting on this point as a differentiator. If it comes up, reformulate as "both are acceptable from the digital sovereignty perspective — the question is which best covers the functional requirements of lifelong learning".

**Strength.** Tie. Do not defend.

## 10. U10 — Uniform recursion of the model

**Capability.** Accreditations, status lists and presentations are all Verifiable Credentials with the same envelope. An ENQA Accreditation over a university is the same structure as a microcredential issued by that university.

**Foreseeable objection.** "SD-JWT VC allows nesting and cross-references between tokens. The practical effect is equivalent."

**Technical analysis.** Not false, but the uniformity is different. In VCDM, a verifier that processes a credential also processes the issuer's accreditation with the same library, the same cryptographic-proof pipeline, the same dual validation. In SD-JWT VC, the credential uses a JWT envelope, the status list uses a different envelope (Token Status List), the accreditation might use another profile. The verifier's code manages more cases.

For an operational verification system at university scale (thousands of verifications daily, credentials issued by hundreds of institutions in tens of countries), uniformity reduces the verifier's maintenance cost. It is not a capital difference, but it is real.

**Suggested reply.** "Uniform recursion is not a first-order differentiator, but it simplifies the construction and maintenance of verification systems in the educational ecosystem. Accreditation, credential, status list and presentation share a single envelope with a single validation logic. In small ecosystems the difference is marginal; in ecosystems at the scale of 27 Member States with thousands of issuers and millions of credentials, it accumulates."

**Strength.** Medium. Real operational advantage, not decisive.

## 11. U11 — Interoperability between wallet implementations

**Capability.** Four independent wallets validated operationally in DC4EU (Identify/Izertis, UAegean, Netcompany, Cappatrust) exchanging the 2,790 real credentials of the pilot.

**Foreseeable objection.** "Equivalent interoperability demonstrations exist in SD-JWT VC, especially in the pilots led by Germany."

**Technical analysis.** Correct on the formal plane. What DC4EU contributes is the *specific validation for education* with 18 types of the Sectoral EAA Catalogue, in 16 Member States, with the participation of national accreditation agencies. It is not a format demonstration in vacuum; it is a demonstration of the complete issuer–wallet–verifier flow for real educational scenarios. That is the specific value.

**Suggested reply.** "It is not a question of whether wallet interoperability exists in both ecosystems — it does. It is a question of which stack is validated specifically for the educational sector with the European accreditation ecosystem. DC4EU offers 36 institutions, 16 Member States, 18 credential types, 2,790 real credentials. If the joint position wants to rest on operational evidence from the educational sector, that is the available base."

**Strength.** High as specific empirical evidence, tie as formal property of the format.

## 12. U12 — Dual-profile detection VCDM 1.1 / VCDM 2.0

**Capability.** Automatic detection by `@context` between versions 1.1 and 2.0 of VCDM, allowing coexistence during the transition period.

**Foreseeable objection.** "This is an internal matter of the VCDM ecosystem. It does not apply to the comparative discussion."

**Technical analysis.** The objection is correct. This point does not contribute a differentiator against SD-JWT VC — it contributes internal robustness to VCDM itself. It is relevant to assure the Commission and the Member States that referencing the two profiles simultaneously is technically clean, but it is not an argument against another format.

**Suggested reply.** Do not use as a comparative argument. Use, if appropriate, as an argument for the Recital: "the Commission can reference VCDM 1.1 and VCDM 2.0 simultaneously without ambiguity of interpretation, thanks to the native `@context` detection mechanism". Useful in the regulatory recital, neutral in the bilateral with Torsten.

**Strength.** Irrelevant in the bilateral. Useful in another forum.

## 13. U13 — Sectoral extensibility without core fracture

**Capability.** DC4EU, PH4H, TRACE4EU, EBSI-VECTOR, Catena-X, Gaia-X, Safe Island — all European LSPs build sectoral profiles on the same VCDM + ELM core without redesign.

**Foreseeable objection.** "Many of these LSPs are format-plural or are migrating to SD-JWT VC as the primary format to align with the EUDIW."

**Technical analysis.** The objection has some truth: recent European strategy favours SD-JWT VC in some LSPs as a format for PID and some attributes. But the specific *educational* scenarios are developed over VCDM + ELM. Migrating them to SD-JWT VC requires remodelling the semantic layer (ELM is natively RDF/JSON-LD; SD-JWT VC requires translation to a flat representation).

The argument is economic rather than technical: what is the cost of migrating what is already built on VCDM versus the marginal cost of supporting VCDM in wallets that already support SD-JWT VC? Migration cost: high (semantic redesign, re-validation, new investment). Marginal VCDM support cost: low (open libraries, incremental pipeline).

**Suggested reply.** "The sectoral LSPs are format-plural in some domains. But the specific educational architecture is built on VCDM + ELM for semantic reasons, not for format preference. Migrating that architecture to SD-JWT VC would imply redesigning the European semantic model of learning — significant investment with null benefit against the status quo. The rational path is to preserve what is built and to add VCDM support in German wallets, which is an incremental operation."

**Strength.** Medium–high. Concrete economic argument.

## 14. U14 — HAIP + OID4VC* compatibility

**Capability.** W3C-VC formats (`ldp_vc`, `jwt_vc_json-ld`) are first-class citizens in OpenID4VCI and OpenID4VP; the European HAIP would cover the three formats symmetrically.

**Foreseeable objection.** "The current HAIP focuses on mdoc + SD-JWT VC. Adding VCDM increases the scope of implementation in German wallets."

**Technical analysis.** The objection is honest. Adding VCDM to the German wallet has non-zero cost: libraries for JSON-LD, for Data Integrity (at least `ecdsa-rdfc-2019`), for SHACL if semantic validation is implemented in the wallet (although it is usual for validation to be done by the verifier). The marginal cost: a few well-maintained open-source dependencies (Digital Bazaar, MATTR, Animo, etc.), amortisable once. The accumulated cost *of not adding it*: impossibility to consume educational credentials issued by European institutions over VCDM, including the complete Sectoral EAA Catalogue. The asymmetry of costs favours adoption.

**Suggested reply.** "Let us recognise the marginal cost of adding VCDM support to an already-SD-JWT-VC wallet. It is real but bounded: OpenID4VCI and OpenID4VP already contemplate the formats; the libraries are open and mature. The alternative cost is losing access to the European educational ecosystem already built on VCDM, with the public investment of more than 80 million euros that this represents. The arithmetic favours incremental adoption."

**Strength.** Medium. Economic argument, not of capability.

## 15. U15 — Sustainable evolution of the model

**Capability.** Mature W3C process (Working Drafts → Candidate Recommendations → Recommendations) with backward compatibility preserved by `@context`.

**Foreseeable objection.** "IETF has equivalently mature processes."

**Technical analysis.** A correct objection. Both bodies are mature. There is no differentiator.

**Suggested reply.** Do not insist. Both processes are equally defensible. If it comes up, recognise symmetry and pass to the next point.

**Strength.** Tie. Do not defend.

## 16. Prioritised synthesis

The following table orders the 15 capabilities by argument strength in a bilateral conversation whose objective is to underpin the symmetrical inclusion of VCDM in the EUDIW profile. The "Type" column indicates whether the differentiator is structural (intrinsic technical property), operational (deployment cost/benefit), empirical (production evidence), strategic (positioning) or null (tie).

| Priority | Capability | Strength | Type |
|---|---|---|---|
| 1 | U5 — BBS+ cryptographic unlinkability | Maximum | Structural |
| 2 | U1 — Native semantics with EU vocabularies | High | Structural |
| 3 | U2 — Dual validation JSON Schema + SHACL | High | Structural |
| 4 | U7 — Native multilingual traceability | High | Operational |
| 5 | U8 — Compatibility with global ecosystems | High | Strategic |
| 6 | U11 — DC4EU wallet interoperability | High | Empirical |
| 7 | U13 — Sectoral extensibility | Medium–high | Economic |
| 8 | U14 — HAIP + OID4VC* (arithmetic of adoption) | Medium | Economic |
| 9 | U3 — Native lifecycle | Medium | Operational |
| 10 | U6 — Hybrid trust model | Medium | Integration |
| 11 | U10 — Uniform recursion | Medium | Operational |
| 12 | U4 — No "phone home" | Tie | Null |
| 13 | U9 — Digital sovereignty | Tie | Null |
| 14 | U15 — Sustainable evolution | Tie | Null |
| 15 | U12 — Dual profile VCDM 1.1 / 2.0 | Irrelevant | Internal |

## 17. The five decisive arguments

If the time in the bilateral is shortened and the defence has to be concentrated on the minimum number of points with maximum impact, the five decisive arguments are:

**1. Cryptographic unlinkability for LoA High (U5).** Article 3(10) of Regulation 2024/2982. BBS+ realises the property cryptographically from a single base signature; batch issuance is an operational approximation with growing cost. Most solid differentiator of VCDM for the high-assurance profile.

**2. Native European semantics (U1) with executable dual validation (U2).** ELM v3.2 over JSON-LD with SHACL. Resolvable EQF/ESCO/ISCED-F vocabularies. Semantic rules executable by standard tools. For 24 languages × 27 Member States × hundreds of credential types × thousands of issuers, this is the only architecture that scales without 27 divergent interpretations.

**3. Native multilingual traceability (U7).** The European vocabularies publish the labels in the 24 languages; the credential references canonical IRIs; the wallet/verifier resolves localisation without burden for the issuer. Significant difference in accumulated operational cost.

**4. DC4EU empirical evidence (U11) + sectoral extensibility (U13).** 36 institutions, 16 Member States, 89 % of the EU population, 2,790 real credentials, 18 types of the Sectoral EAA Catalogue, 4 interoperable wallets. European educational architecture built on VCDM + ELM. Migrating has a high cost with no benefit; maintaining has a low marginal cost.

**5. Global strategic positioning (U8).** 80 % of the world ecosystem of decentralised identity on W3C-VC. Open Badges 3.0 built on VCDM. 50+ national programmes. An educational EUDIW single-format not aligned with this ecosystem creates friction at every border for every European student, researcher and professional in global markets.

## 18. Traps to avoid

**Do not argue about ties.** U4, U9, U15 are technically neutral between VCDM and SD-JWT VC. Insisting weakens the strong arguments by association.

**Do not exaggerate the maturity of BBS+.** Candidate Recommendation is the real status. Mentioning it pre-emptively disarms the objection about maturity. Recognise that final Recommendation is expected in 2026.

**Do not question the suitability of SD-JWT VC for PID or of mdoc for mDL.** They are good solutions for those domains. The argument is about the specific educational domain and lifelong learning.

**Do not frame the discussion as exclusive.** The EUDIW profile already references the three formats; the question is symmetrical operational treatment. Framing it as "VCDM instead of SD-JWT VC" is losing the conversation; framing it as "complete symmetrical treatment of the three referenced formats" is winning it.

**Do not present the repository document as an ultimatum.** It is technical support material. The political conclusions are built by the table, not by a PDF.

## 19. Single message if time runs out to one minute

> "What is on the table is not choosing a format. It is deciding whether the EUDIW offers symmetrical treatment to the three formats that the Regulation itself references, or whether it leaves one of them with an operational asymmetry that would affect the European educational sector along its whole chain — from the issuance of microcredentials to the cross-border recognition of professional qualifications. The technical symmetry already exists; what is lacking is regulatory symmetry. Germany and Spain proposing that symmetry jointly is the move that turns 27 divergent national decisions into a coherent European decision."

## 20. Suggested next steps

If the bilateral conversation progresses favourably, prepare:

- **Executive two-page brief** (separate, public document, with the compact regulatory argument).
- **End-to-end ES → DE walkthrough** (concrete case: URV student applies for a job at Siemens, complete issuance–wallet–presentation–verification flow with ELM + VCDM + OID4VP + BBS+).
- **Economic estimate** of the two alternative costs: (a) adding VCDM support to German wallets vs (b) migrating the European educational architecture from VCDM to SD-JWT VC.
- **Joint ES–DE declaration** for the next Expert Group meeting, in case of alignment.

This document is maintained as a technical working reference. Update if the conversation reveals new objections not anticipated.

---

*Last revision: April 2026. Internal working document. Do not circulate except to actors directly involved in the preparation of the ES–DE bilateral.*
