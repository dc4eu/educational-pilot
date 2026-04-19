# 03 — Benefits of W3C-VCDM

This chapter documents how W3C-VCDM satisfies each of the ten requirements identified in [02 — Requirements of lifelong learning](./02-lifelong-learning-requirements.md). Each benefit is presented in affirmative terms, as a native capability of the format, with references to the corresponding W3C Recommendation and to the validated empirical evidence.

## B1 — Semantic expressiveness over authoritative European vocabularies

### How W3C-VCDM covers it

W3C-VCDM serialises the credential as **JSON-LD 1.1**, which means that every JSON property resolves, through the `@context`, to an **IRI in a controlled vocabulary**. The credential is interpreted simultaneously as a JSON tree (for classical processing) and as an **RDF graph** (for semantic reasoning).

This directly enables:

- Resolution of `elm:eidasLegalIdentifier`, `elm:EQFLevel`, `elm:educationSubject`, `elm:provenBy`, `elm:awardedBy`, `elm:hasClaim`, `elm:specifiedBy`, `elm:creditPoint`, `elm:framework`, etc. to IRIs of the ELM v3.2 vocabulary maintained by the Publications Office of the EU.
- Direct reference to controlled vocabularies:
  - `http://data.europa.eu/snb/eqf/` for EQF levels 1–8.
  - `http://data.europa.eu/snb/isced-f/` for ISCED-F fields of knowledge.
  - `http://data.europa.eu/esco/` for ESCO competences.
  - `http://publications.europa.eu/resource/authority/country/` for country codes.
- Use of `skos:notation` and `rdf:type` to mark authoritative values versus human labels.

### Conceptual example

```json
{
  "@context": [
    "https://www.w3.org/ns/credentials/v2",
    "http://data.europa.eu/snb/model/context/edc-ap"
  ],
  "type": [
    "VerifiableCredential",
    "EuropeanDigitalCredential",
    "EuropeanHigherEducationMicrocredential"
  ],
  "credentialSubject": {
    "type": "Person",
    "elm:hasClaim": {
      "type": "LearningAchievement",
      "elm:specifiedBy": {
        "elm:EQFLevel": {
          "id": "http://data.europa.eu/snb/eqf/7",
          "skos:notation": "7"
        },
        "elm:educationSubject": {
          "id": "http://data.europa.eu/snb/isced-f/0613"
        }
      }
    }
  }
}
```

By resolving `elm:EQFLevel` to its IRI, the verifier can determine with certainty that the credential corresponds to level 7 of the European Qualifications Framework, regardless of the text language, the issuing Member State and the verifying software.

### Empirical evidence

- DC4EU Sectoral EAA Catalogue with 18 credential types, all serialised in JSON-LD over ELM v3.2.
- Profile-specific SHACL shapes (HE microcredential, VET microcredential, diploma, secondary certificate) registered in EBSI TSR v3.

## B2 — Cross-border interoperability without intermediaries or bilateral mappings

### How W3C-VCDM covers it

The `@context` mechanism provides the verifier, in a deterministic and executable manner, with all the information required to interpret the credential: which rulebook applies, which version of the vocabulary is active, how to map each property to its reference definition. An **architect** qualification issued in Madrid and a **Berufsqualifikation** issued in Berlin, both with the same `@context` to the ESCO vocabulary and the same reference to Directive 2005/36/EC, are interpreted as referring to the **same regulated profession** without the need for a bilateral mapping.

As Alex Grech formulates it in his contribution to the Ares(2026)1286304 consultation: `@context` is the standardised, deterministic and executable method that connects the syntax of the credential with its shared semantics. Removing it would sever the link between the credential and its meaning.

### Processing model

1. The verifier receives a W3C-VC credential.
2. It resolves the `@context` array (local, cached, or from an authoritative server).
3. It applies JSON-LD 1.1 to build the RDF graph.
4. It evaluates the SHACL shapes referenced in `credentialSchema[]` against the graph.
5. It obtains a deterministic semantic validation result.

This processing is **identical** regardless of the verifier's jurisdiction, the credential's language and the verifying software vendor.

### Empirical evidence

- DC4EU validated interoperability in 36 institutions from 16 Member States, including scenarios of cross-border recognition of academic and professional credentials.

## B3 — Verifiable issuer identity and assurance

### How W3C-VCDM covers it

W3C-VCDM 2.0 combines legal identification (X.509v3 / `eidasLegalIdentifier`) with decentralised identification (DID `did:ebsi:...` / `did:web:...`) in a hybrid PKI–dPKI model:

- The SHACL shape `he-micro:IssuerShape` requires the presence of exactly one `elm:eidasLegalIdentifier` with its `skos:notation` (legal identifier) and its `dc:spatial` as an IRI of the Publications Office country vocabulary.
- The issuer may sign with enveloping proofs (JOSE/COSE with X.509 certificate chain `x5c`) or with embedded proofs (Data Integrity with DID controller).
- The DC4EU profile validates the use of **jAdES D-Zero** (ETSI TS 119 182-1) for institutional signatures, integration with **QSealC** for qualified electronic seals, **QWAC** for qualified web-authentication certificates, and **QTS** for qualified time-stamps.
- The accreditation chain (QA agency → institution → sectoral issuer) is articulated via separate credentials (Accreditation Credentials) chained to sectoral Trust Anchors.

### Empirical evidence

- DC4EU demonstrated the complete cryptographic profile with jAdES D-Zero + QSealC + QTS + ES256/EdDSA/BBS.
- The DC4EU Sectoral Rulebook documents the issuer on-boarding processes and the verification of the accreditation chain.

## B4 — Lifecycle with native suspension and revocation

### How W3C-VCDM covers it

The W3C **Bitstring Status List v1.0** Recommendation (15 May 2025) defines `statusPurpose` with permissible values `"revocation"` and `"suspension"`. The proposed EUDIW profile formalises the following:

- **EAA-7.2.11-W3C-02**: W3C-VC QEAA and PuB-EAA must support at least one `credentialStatus` entry with `statusPurpose: "revocation"` **and** at least one with `statusPurpose: "suspension"`.
- **EAA-7.2.11-W3C-03**: `BitstringStatusListEntry` is the recommended mechanism, since it natively supports both purposes.

The Bitstring Status List status credential is itself a W3C-VC JSON-LD signed in accordance with the applicable requirements of ETSI EN 319 411-1 and resolvable by any conformant European validation service. This creates a coherent recursive system in which the status has the same semantics, cryptography and privacy principles as the credential to which it refers.

### Example

```json
"credentialStatus": [
  {
    "type": "BitstringStatusListEntry",
    "statusPurpose": "revocation",
    "statusListIndex": "83271",
    "statusListCredential": "https://status.agency.example/bitstrings/revocation/2026-04"
  },
  {
    "type": "BitstringStatusListEntry",
    "statusPurpose": "suspension",
    "statusListIndex": "12045",
    "statusListCredential": "https://status.agency.example/bitstrings/suspension/2026-04"
  }
]
```

### Regulatory coverage

- **Article 24 Regulation 2024/1183** (permanent revocation): covered by `statusPurpose: "revocation"`.
- **Section 9 Regulation 2024/1183** (temporary suspension): covered by `statusPurpose: "suspension"`.

## B5 — Structural privacy

### How W3C-VCDM covers it

W3C-VCDM supports multiple privacy mechanisms that are simultaneously operable:

- **Selective disclosure**:
  - **SD-JWT profile**: enveloping proofs with selective disclosure of attributes.
  - **BBS+ `bbs-2023`**: embedded proofs with selective disclosure and native unlinkability.
- **Cryptographic unlinkability**:
  - The `bbs-2023` cryptosuite over the **BLS12-381** curve generates a mathematically distinct proof in each presentation, making it impossible to correlate two verifications of the same credential.
  - ETSI TR 119 476-1 v1.3.1 §7.7.2 identifies BBS as the technically credible path to comply with Article 3(10) of CIR 2024/2982.
- **No phone home**:
  - `BitstringStatusListEntry` publishes status lists in an immutable and cacheable format; the verifier never calls the issuer during verification.
  - **EBSI proxies** provide decentralised infrastructure for resolving TrustRegistries without revealing the verifier's identity to the issuer.
- **Zero-knowledge readiness**:
  - BBS+ enables predicate proofs ("EQF ≥ 6") without revealing the exact value.
  - The architecture admits the future incorporation of more advanced ZKP schemes as they mature.
- **Embedded Disclosure Policies**:
  - The DC4EU sectoral profile includes disclosure policies bound to the verifier's authorisations, allowing the issuer to define which combinations of attributes are appropriate for each category of relying party.

### Empirical evidence

- DC4EU validated in production StatusList2021 (direct predecessor of Bitstring Status List), EBSI proxies, BBS signatures (within the sectoral cryptographic profile), and Embedded Disclosure Policies.

## B6 — Integrated quality assurance

### How W3C-VCDM covers it

The DC4EU sectoral catalogue defines four types of Accreditation Credentials in W3C-VCDM:

- **Institutional Accreditation**: accredits that an institution is recognised to issue credentials in a domain.
- **Programme Accreditation**: accredits that a specific educational programme meets quality standards.
- **QA Agency Credential**: accredits that a quality-assurance agency is recognised by ENQA/EQAR.
- **EQAR Registration Credential**: accredits the status of an agency in the European Quality Assurance Register.

Educational credentials (EUHED, EUHEMC, EUVETMC, etc.) include verifiable references to the corresponding Accreditation Credentials via ELM properties (`elm:accreditedBy`, `elm:hasAccreditation`). From an educational credential, the verifier can resolve the entire chain up to the EQAR register without semantic rupture.

### Coverage of European frameworks

- **ESG 2015** (European Standards and Guidelines): ELM properties capture the quality standards.
- **EQAR Register**: specific credential linked to the public register.
- **Recommendation on microcredentials (2022)**: the 10 mandatory elements of a European microcredential materialise as structured properties of EUHEMC/EUVETMC.

## B7 — Portability across formats, wallets and implementations

### How W3C-VCDM covers it

The key property is **verification without proprietary APIs**:

- Embedded **Data Integrity** proofs (`ecdsa-rdfc-2019`, `bbs-2023`) are verified with standard cryptography libraries, without depending on APIs mediated by the operating system.
- Enveloping **JOSE/COSE** proofs are verified with any conformant JOSE/COSE implementation.
- Offline verification is supported (every artefact — credential, schema, SHACL shape, status credential — can be cached and resolved locally from EBSI TSR).
- Compatibility with Open Badges 3.0, CTDL and LER allows the European portfolio to be partially recognisable in complementary global ecosystems.

### Empirical evidence

- DC4EU demonstrated interoperability among **four distinct wallets**: EUDI Wallet Reference Implementation, DC4EU Identity Wallet, ValidateID and Walt.ID Web Wallet.
- 80 % of 267 global decentralised-identity projects analysed by the Web of Trust Map 2025 use W3C-VC.

## B8 — Integration with OpenID4VCI / OpenID4VP protocols

### How W3C-VCDM covers it

The proposed EUDIW profile for W3C-VC covers all four quadrants (issuance × presentation, enveloping × embedded):

| | Issuance (OID4VCI) | Presentation (OID4VP / HAIP) |
|---|---|---|
| **Enveloping (JOSE/COSE)** | `jwt_vc_json-ld` | `jwt_vc_json`, `vp+jwt` |
| **Embedded (Data Integrity)** | `ldp_vc` | `ldp_vc`, `ldp_vp` |

**HAIP-W3C-ENV-01**: the `credential_definition` parameter includes the `@context` array and the `type` array in accordance with the new Section 4.3 of Annex I.

**HAIP-W3C-EMB-01/02/03/04**: the identifiers `ldp_vc` and `ldp_vp` are added to Annex XIV with admissible cryptosuites (`DataIntegrityProof` with `ecdsa-rdfc-2019` as a minimum, `bbs-2023` once incorporated into ETSI TS 119 312).

**OID4VCI-W3C-01/02/03/04/05**: Credential Issuer metadata with `format`, `@context`, `type`, `cryptographic_binding_methods_supported`, `proof_types_supported`; `eudi_wallet_info` object and `key_attestation` of Annex III unchanged.

### Empirical evidence

- The identifier `jwt_vc_json-ld` is already in production in the EBSI OID4VCI implementation, validated in 80 organisations from 23 Member States during DC4EU.
- The EUDI Wallet Reference Implementation was extended by GRNet within DC4EU WP5 to support the W3C-VC profile with full OID4VCI/OID4VP flows.

## B9 — Coverage of all modalities of learning

### How W3C-VCDM covers it

The **Sectoral EAA Catalogue** built by DC4EU over W3C-VCDM covers the following modalities:

- **Higher education**: EUHED, EUHEDS, EUHETOR, EUHEPOE, EUHEMC.
- **Vocational education and training (VET)**: EUVETD, EUVETC, EUVETMC.
- **Upper secondary education**: EUUSC, EUUSTOR.
- **Professional qualifications**: CPS, AMT, CPD, PTC.
- **Quality assurance**: Institutional Accreditation, Programme Accreditation, QA Agency Credential, EQAR Registration Credential.
- **Identity**: PID (EUDI), EducationalID (student/staff), AllianceID (university alliance), European Student Card, MyAcademicID, ProfessionalID, DoctorID, EngineerID.

The three proven deployment models — **institutional self-hosting**, **managed service (GovPart)**, **national coordination (OPI/NASK Poland)** — allow each institution to choose a path commensurate with its technical capacity, without sacrificing interoperability.

See [07 — Sectoral EAA catalogue](./07-sectoral-eaa-catalogue.md) for the complete detail.

## B10 — Consistent verification with VCDM 1.1 and VCDM 2.0 profiles

### How W3C-VCDM covers it

The verification flow proposed in the DC4EU Sectoral Rulebook distinguishes the two profiles by inspecting the `credentialSchema[]` array:

- **VCDM 1.1 profile**: `credentialSchema` with one entry of `type: JsonSchema`. The verifier runs syntactic validation against the referenced JSON Schema.
- **VCDM 2.0 profile**: `credentialSchema` with two entries, one of `type: JsonSchema` and another of `type: ShaclValidator2017` (or `ShaclSchemaCredential`). The verifier runs:
  1. Syntactic validation (JSON Schema), and
  2. Materialisation of the RDF graph from JSON-LD with the ELM v3.2 `@context` and semantic validation against the referenced SHACL shape.

Both schemas (JSON Schema and SHACL shape) must resolve to entries in the **EBSI Trusted Schemas Registry v3**. The verifier SHOULD accept both profiles during the transition period and both are expected to continue being accepted when future updates to the Implementing Acts also recognise VCDM 2.0.

### Non-modification principle

The JSON Schema already registered in EBSI TSR (identifier `0x05332a9dc53a4a26a15711262904f2a1dd081cf3da735350f42dac20426530a4` for the HE microcredential profile) is neither modified nor revoked. The SHACL shape is registered as a new independent schema. Credentials issued from the time of availability declare both. This **preserves backward compatibility** with all issuers and verifiers already operating over JSON Schema.

See [04 — Dual validation architecture](./04-dual-validation-architecture.md) for the technical detail.

## Summary table

| Requirement | Native W3C-VCDM capability | Regulatory reference |
|---|---|---|
| R1 | JSON-LD + `@context` over European vocabularies | JSON-LD 1.1; ELM v3.2 |
| R2 | Deterministic interpretation via `@context` | W3C-VCDM 2.0; JSON-LD 1.1 |
| R3 | `eidasLegalIdentifier` + hybrid PKI–dPKI model | ETSI EN 319 411-1; CIR 2024/2979 |
| R4 | `BitstringStatusListEntry` with suspension + revocation | W3C Bitstring Status List v1.0 |
| R5 | `bbs-2023` + StatusList + EBSI proxies + EDP | W3C BBS Cryptosuites v1.0; ETSI TR 119 476-1 |
| R6 | Chained Accreditation Credentials | ESG 2015; EQAR Register |
| R7 | Data Integrity without proprietary APIs; multi-wallet | P10_TA(2026)0022; DC4EU |
| R8 | `jwt_vc_json-ld`, `ldp_vc`, `ldp_vp` in HAIP | CIR 2024/2982 Annex XIV (proposal) |
| R9 | 18 credential types + 3 deployment models | DC4EU Sectoral EAA Catalogue |
| R10 | Dual-profile detection via `credentialSchema[]` | ETSI TS 119 472-1 V1.1.1 cl. 7.2.1.3 |

---

**Next links**:

- [04 — Dual validation architecture](./04-dual-validation-architecture.md)
- [05 — European Learning Model (ELM v3.2)](./05-european-learning-model.md)
- [06 — Lifecycle and trust](./06-lifecycle-and-trust.md)
- [09 — Unique capabilities of W3C-VCDM](./09-vcdm-unique-capabilities.md)
