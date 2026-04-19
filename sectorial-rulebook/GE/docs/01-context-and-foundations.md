# 01 — Context and foundations

## 1.1 Lifelong learning as a reference framework

Education, understood in its contemporary European sense, is not a state achieved at a particular moment but a **lifelong continuum**: early-years education, primary and secondary education, vocational education and training, higher education, microcredentials, continuing professional development (CPD), non-formal and informal learning, regulated professional licensing, recognition of work experience and cross-border mobility. This continuum is what the Council Recommendation of 22 May 2018 on key competences for lifelong learning, Directives 2005/36/EC and 2013/55/EU on recognition of professional qualifications, the Council Recommendation of 16 June 2022 on microcredentials and the European Education Area 2025 objectives define as lifelong learning.

Digital credentialing of this continuum requires a single technical and semantic language capable of:

- Expressing the nature of each credential (diploma, certificate, microcredential, professional licence, evidence of experience, quality accreditation).
- Binding each credential to the European qualifications frameworks (EQF, ECTS, ECVET, ISCED-F, ESCO) through authoritative references.
- Enabling automated cross-border recognition among educational institutions, employers, regulatory authorities and citizens.
- Guaranteeing the holder's privacy and autonomy over what, when and to whom each piece of information is disclosed.
- Managing the full lifecycle (issuance, update, suspension, revocation) while respecting heterogeneous national regulatory frameworks.

## 1.2 European regulatory framework

### 1.2.1 Regulation (EU) 2024/1183 (eIDAS 2.0)

Regulation (EU) 2024/1183 of the European Parliament and of the Council, of 11 April 2024, amending Regulation (EU) No 910/2014 as regards establishing the European Digital Identity Framework, formally introduces into the Union acquis:

- The **European Digital Identity Wallet (EUDIW)** as a mandatory instrument to be issued by each Member State.
- **Electronic Attestations of Attributes (EAA)** in their QEAA (qualified) and PuB-EAA (issued by public-sector bodies) variants.
- Specific provisions on **suspension** and **revocation** of (Q)EAA (Article 24 and Section 9), required for regulated professions and credentials with a non-permanent lifecycle.
- **Article 5a(16)(b)** on unlinkability between relying parties, developed by Article 3(10) of CIR 2024/2982.
- Articles **45k and 45l** on qualified electronic-ledger services, applicable to the auditable evidence of trust actions in the credential lifecycle.

### 1.2.2 First batch of Implementing Acts

The first batch of Commission Implementing Regulations (CIR) developing Regulation 2024/1183 comprises:

- **CIR (EU) 2024/2977**, Annex I — technical specifications for the encoding of the PID. Sections 4.1 and 4.2 cover encoding in **ISO/IEC mdoc** (CBOR/COSE) and in **SD-JWT VC** (JOSE). Section 4.3, currently absent, is proposed in this document to cover the encoding in **JSON-LD W3C-VC** (Table 9 with 27 attributes).
- **CIR (EU) 2024/2979**, Annex V — adaptations to ETSI TS 119 472-1 V1.1.1. The existing adaptation points (1) to (8) cover mdoc and SD-JWT VC. Points (9) to (16) are proposed to complete the treatment of W3C-VC.
- **CIR (EU) 2024/2982**, Annex XIV — presentation protocols (HAIP). It includes the format identifiers `dc+sd-jwt`, `mso_mdoc`, `jwt_vc_json` and `vp+jwt`, with the proposed addition of `ldp_vc` and `ldp_vp` for embedded Data Integrity proofs.

### 1.2.3 ETSI TS 119 472-1 V1.1.1

ETSI TS 119 472-1 V1.1.1 (2025-12) — "Electronic Attestation of Attributes (EAA) profiles" — defines technical profiles for the three credential formats recognised in the EUDIW framework:

- Clause 5 — ISO/IEC mdoc profile.
- Clause 6 — SD-JWT VC profile.
- **Clause 7 — W3C-VC JSON-LD profile** (complete technical content: credential types, `credentialSchema` with `JsonSchemaCredential`, `CddlSchemaCredential` and `ShaclSchemaCredential`, revocation via BitstringStatusListEntry/TokenStatusList/CRL/OCSP, enveloping JOSE/COSE proofs and embedded Data Integrity proofs).

ETSI TS 119 472-3 adds details for OID4VCI issuance and OID4VP verification, and ETSI TR 119 476-1 v1.3.1 documents the unlinkability analysis with explicit conclusions on the BBS cryptosuites.

### 1.2.4 Applicable W3C Recommendations

On 15 May 2025 the W3C published the full package of Recommendations that formalise the data model and the assurance mechanisms of the Verifiable Credentials ecosystem:

- **Verifiable Credentials Data Model v2.0** — canonical data model.
- **Securing Verifiable Credentials using JOSE and COSE** — enveloping proofs.
- **Verifiable Credential Data Integrity v1.0** — embedded proofs.
- **Bitstring Status List v1.0** — status mechanism with `statusPurpose: revocation | suspension`.
- **Data Integrity ECDSA Cryptosuites v1.0** — `ecdsa-rdfc-2019` cryptosuite.

On 3 April 2025 the **Candidate Recommendation** of **Data Integrity BBS Cryptosuites v1.0** was published, with the `bbs-2023` cryptosuite and the proof-derivation mechanism for unlinkable selective disclosure.

The **JSON-LD 1.1** Recommendation (2020) provides the canonical serialisation of the data model; the **SHACL** Recommendation (20 July 2017) provides the declarative shapes language for semantic validation over the RDF graph.

### 1.2.5 Other relevant regulatory sources

- **Directive 2005/36/EC** and **Directive 2013/55/EU** on recognition of professional qualifications.
- **Council Recommendation of 16 June 2022** on a European approach to microcredentials.
- **Regulation (EU) No 1025/2012** on European standardisation (legal basis for standardisation requests to ETSI ESI).
- **General Data Protection Regulation (EU) 2016/679 (GDPR)** — minimisation and purpose-limitation principles.
- **European Parliament Resolution of 22 January 2026** on European technological sovereignty (P10_TA(2026)0022).

## 1.3 European trust infrastructure

### 1.3.1 EBSI

The **European Blockchain Services Infrastructure (EBSI)**, a joint initiative of the European Commission and the European Blockchain Partnership, provides:

- **EBSI Trusted Schemas Registry (TSR) v3** — immutable register of schemas (JSON Schema, SHACL shapes, CDDL) identified by cryptographic hash and resolvable offline.
- **EBSI Trusted Issuers Registry (TIR)** — register of accredited issuers with their DIDs and X.509v3 certificates.
- **EBSI Trust Chains (Trusted Accreditation Organisations, TAO)** — accreditation chain for regulated domains (QA agency → educational institution → sectoral issuer).
- **EBSI Proxies** — privacy-preserving verification infrastructure that eliminates "phone home" calls to the issuer.

### 1.3.2 DC4EU programme

The **Digital Credentials for Europe (DC4EU)** project — a consortium of 23 Member States, 80 organisations, €19M from the Digital Europe Programme (2023–2025) — has developed and validated in production:

- The sectoral cryptographic profile for education and professional qualifications (JAdES D-Zero, QSealC, QWAC, QTS, ES256/EdDSA/BBS).
- The **Sectoral EAA Catalogue** with 14 educational and professional credential types + 4 quality-assurance types.
- The **Sectoral Rulebook** covering the processes of issuance, verification, lifecycle management, information disclosure and identity management.
- The extension of the Commission's **EUDI Wallet Reference Implementation** to support the W3C-VC profile with complete OID4VCI/OID4VP flows.
- 2,790 real credentials issued in 36 institutions from 16 Member States (89 % of the EU population).
- 19 public deliverables available at `https://www.dc4eu.eu/reports/`.

### 1.3.3 European Learning Model (ELM v3.2)

The **European Learning Model (ELM)** in version 3.2 is the official European ontology for the representation of achievements, learning outcomes, competences, skills, assessments, activities, awarding processes, entitlements and qualifications, maintained by the Publications Office of the EU. It provides:

- Controlled vocabularies (EQF, ESCO, ISCED-F, NUTS, country vocabulary).
- RDF classes for each educational entity (`elm:LearningAchievement`, `elm:LearningActivity`, `elm:Assessment`, `elm:AwardingProcess`, etc.).
- Properties with rich semantics (`elm:hasClaim`, `elm:provenBy`, `elm:awardedBy`, `elm:specifiedBy`, `elm:eidasLegalIdentifier`, `elm:EQFLevel`, `elm:creditPoint`, `elm:educationSubject`).
- Official JSON-LD context for direct use in W3C-VCDM credentials.

The EU's **European Digital Credential (EDC)** profile derives from ELM v3.2 and is already registered in EBSI TSR v3 with a dual JSON Schema + SHACL architecture, under the generic `edc_generic_shacl` shape from which the shapes specific to each credential type are derived.

## 1.4 The three formats in the EUDIW framework

The EUDIW framework formally recognises three credential formats, each with its natural domain of application and its own technical profile. The regulatory treatment of the three formats should be symmetrical in order to guarantee technical pluralism and the sovereignty of choice on the part of issuers and Member States:

| Format | Encoding | Natural use case | Technical profile | Operational status |
|---|---|---|---|---|
| ISO/IEC mdoc | CBOR/COSE | Proximity offline presentation, identity documents such as driving licences | ETSI TS 119 472-1 cl. 5 + ISO/IEC 18013-5/7 + CTAP | Complete in CIRs |
| SD-JWT VC | JOSE (compact JSON) | Simple cases, integration with the classical OAuth/OIDC ecosystem | ETSI TS 119 472-1 cl. 6 + draft-ietf-oauth-sd-jwt-vc-13 | Complete in CIRs |
| W3C-VC JSON-LD | JSON-LD over an RDF graph | Credentials with rich semantics (education, health, B2B, supply chain, regulated professions) | ETSI TS 119 472-1 cl. 7 + W3C Recommendations of 15 May 2025 | Normative reference; regulatory adaptations proposed in this document |

This document focuses on articulating why W3C-VCDM is the appropriate option for lifelong learning, while respecting the coexistence of the three formats in the EUDIW framework.

## 1.5 W3C VCDM 2.0 Recommendation — coexistence with VCDM 1.1

The first batch of Implementing Acts takes W3C-VCDM 1.1 as its reference, consolidated as a W3C Recommendation since 2022 and with six years of production deployment globally. The **W3C-VCDM 2.0** Recommendation published on 15 May 2025 retains data-model backward compatibility and contributes:

- `validFrom` / `validUntil` instead of `issuanceDate` / `expirationDate`.
- Structured support for `credentialStatus[]` as an array (compatible with native dual `BitstringStatusListEntry`).
- Alignment with `credentialSchema[]` as an array with two entries (`JsonSchemaCredential` + `ShaclSchemaCredential`).
- Canonical integration with the Data Integrity and JOSE/COSE packages.

The architecture of the proposed EUDIW profile enables **simultaneous coexistence** of both profiles during the transition: verifiers accept `credentialSchema` with a single entry (VCDM 1.1 profile, current mandate) and `credentialSchema` with two entries (VCDM 2.0 profile, forward-looking). See [06 — Lifecycle and trust](./06-lifecycle-and-trust.md) for the dual-verification flow.

## 1.6 Principle of integration, not invention

As documented in the post "W3C Verifiable Credentials in Europe: From Theory to Large-Scale Validation" (February 2026): the European Commission has already developed the PID in W3C-VCDM format through the EUROPEUM/EBSI infrastructure, DC4EU has validated the approach at scale in 36 institutions from 16 Member States, and the Commission's own EUDI Wallet Reference Implementation has been successfully extended within DC4EU to support the W3C-VC profile with full OID4VCI/OID4VP flows. **What remains is regulatory integration, not technical invention**.

---

**Next links**:

- [02 — Requirements of lifelong learning](./02-lifelong-learning-requirements.md)
- [03 — Benefits of W3C-VCDM](./03-w3c-vcdm-benefits.md)
- [08 — Complete EUDI Wallet profile for W3C-VC](./08-eudiw-profile.md)
