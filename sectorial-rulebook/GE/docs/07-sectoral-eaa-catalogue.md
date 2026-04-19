# 07 — Sectoral EAA catalogue

## 7.1 Purpose of the catalogue

The **Sectoral EAA Catalogue** is the set of educational and professional credential profiles that the **DC4EU** consortium published and validated operationally as a sectoral extension of the EUDIW profile for education, vocational training and continuing learning. Its function is threefold:

1. **Enumerate** the types of lifelong-learning credentials that practice identifies as essential.
2. **Define** for each type the dual schema (JSON Schema + SHACL shape) that realises the dual architecture of chapter 04.
3. **Demonstrate** that the W3C-VCDM profile covers the full spectrum of needs without fractures of interoperability.

The catalogue is published in the **EBSI Trusted Schemas Registry v3** and in the DC4EU project repositories, with stable versions and change traceability.

## 7.2 General structure

Each entry in the catalogue contains:

- **Code**: short identifier (for example, `EUHEMC`).
- **Full name**: English denomination registered as `type` in the credential.
- **Scope**: formal educational, VET, professional, quality assurance.
- **JSON Schema**: schema identifier in EBSI TSR v3.
- **SHACL shape**: reference to the authoritative semantic profile.
- **Validated examples**: real credentials issued in the DC4EU framework, accessible as an implementation reference.

## 7.3 The 18 types of the DC4EU catalogue

The catalogue covers **18 credential types**, grouped into two large blocks: education and profession (14), quality assurance (4).

### 7.3.1 Education and profession (14)

| Code | Name | Scope |
|---|---|---|
| `EUHEMC` | European Higher Education Microcredential | Higher education, microcredential |
| `EUVETMC` | European VET Microcredential | Vocational training, microcredential |
| `EUHEPOE` | European Higher Education Proof of Enrolment | Higher education, enrolment |
| `EUHED` | European Higher Education Diploma | Higher education, diploma |
| `EUHEDS` | European Higher Education Diploma Supplement | Higher education, supplement |
| `EUHETOR` | European Higher Education Transcript of Records | Higher education, academic transcript |
| `EUUSC` | European University Student Card | Higher education, student credential |
| `EUUSTOR` | European University Short-Term Organised Response | Higher education, short-duration certificate |
| `CPS` | Certificate of Professional Skills | Professional, skills |
| `AMT` | Attestation of Mandatory Training | Professional, mandatory training |
| `CPD` | Continuing Professional Development | Professional, continuing training |
| `PTC` | Professional Training Certificate | Professional, training certificate |
| `EUPPC` | European Professional Practice Certificate | Professional, practice |
| `EUSCC` | European Secondary Completion Certificate | Secondary education, completion |

### 7.3.2 Quality assurance (4)

| Code | Name | Scope |
|---|---|---|
| `EUEQA` | European Education Quality Accreditation | Institutional QA |
| `EUPQA` | European Programme Quality Accreditation | Programme QA |
| `EUAQA` | European Assessor Quality Accreditation | Assessor QA |
| `EUQAA` | European Quality Assurance Authorisation | QA, agency authorisation |

## 7.4 Coverage of the lifelong-learning spectrum

The catalogue is significant for **what it covers** and **how it covers it**:

- **What**: each type covers a modality identified in the 2022 Council Recommendation on microcredentials and in the European Qualifications Framework. The combination covers formal education (primary/secondary/higher), vocational training, professional qualifications, continuing training, short-format credentials, academic transcripts, enrolments and diplomas.
- **How**: all types share the same **underlying technical model**: VCDM (1.1 or 2.0) with ELM v3.2 `@context`, dual credentialSchema, BitstringStatusList and Data Integrity. The difference between types is exclusively **semantic**: ELM subclass, applicable vocabularies, specific SHACL rules.

This technical uniformity is what enables a single wallet, a single verifier and a single issuer to handle the 18 types with the same infrastructure. The marginal cost of adding a new type to a deployed system is negligible.

## 7.5 Operational validation

The catalogue was validated operationally in the **DC4EU** pilot with the following metrics:

| Metric | Value |
|---|---|
| Issuing institutions | 36 |
| Participating Member States | 16 |
| EU population coverage | 89 % |
| Real credentials issued | 2,790 |
| Types effectively deployed | 18 |
| Interoperable wallets validated | 4 (ISRAEL, UAegean, Netcompany, Cappatrust) |
| Pilot funding | €19M (Digital Europe Programme) |

The credentials issued covered real cases: cross-border university admission, recognition of VET microcredentials between Member States, certification of continuing training of regulated professionals, portable academic transcripts.

## 7.6 Non-invention principle

One editorial principle of the catalogue — aligned with the general principle of this document — is **non-invention**. The catalogue **does not create**:

- New vocabularies: it reuses EQF, ESCO, ISCED-F, NACE, ELI, national frameworks.
- Proprietary technical schemas: it uses JSON Schema Draft 2020-12 and SHACL 1.0.
- Ontologies parallel to ELM: it uses ELM v3.2 exclusively.
- Proprietary registers: it uses EBSI TSR v3.
- Formats outside VCDM: all types are W3C Verifiable Credentials.

The added value of the catalogue is the **consolidated combination**, the **sectoral profiling** and the **operational validation**: it turns a set of open specifications into a sectoral profile that is usable end-to-end.

## 7.7 Mapping with CCIs and cross-references

Each type of the catalogue is associated with a **CCI (Credential Type Code Identifier)** in the controlled vocabulary published by ELM v3.2, and admits cross-references with:

- **ISCED-F** for the field of study.
- **EQF** for the level.
- **ESCO** for the referenced skills and occupations.
- **Open Badges 3.0** for international equivalence.
- **CTDL** (Credential Engine) via bilateral mapping.

This cross-reference layer is what makes a European credential interpretable in non-European contexts (North American LER, Asian university systems adhering to the Groningen Declaration Network) without reissuance.

## 7.8 Extensibility

The catalogue is **open to extension**:

- New sectoral types can be incorporated by defining the corresponding ELM subclass, JSON Schema and SHACL shape, and registering them in EBSI TSR v3.
- Member States can define derived national profiles as specialisations of the base types, with SHACL shapes that add specific constraints of the national framework.
- Specialised sectors (health, defence, finance) can define their own profiles following the same architecture, as sister projects already do (**PH4H** in health, **EBSI-VECTOR** in mobility, **Catena-X** in industrial mobility).

All extended profiles remain technically compatible with the W3C-VCDM core. A wallet conformant with the EUDIW profile can handle them without updates.

## 7.9 Public availability

The 18 types of the catalogue are published with:

- JSON Schemas accessible in **EBSI TSR v3** with content identifiers (SHA-256).
- SHACL shapes accessible as signed Turtle files, with resolvable URIs.
- Examples of real credentials documented in the **DC4EU repository** and the **Europass Dataspace**.
- Implementation guides in the DC4EU project publications (D5.1.1, D5.1.2 and complementary deliverables).

The transfer of the catalogue to a post-pilot framework (successors to DC4EU, permanent consortia of the EUDIW ecosystem) is planned in the roadmap of chapter 10.

## 7.10 Outcome

The Sectoral EAA Catalogue contributes to the EUDIW profile for W3C-VC:

1. Empirical demonstration of complete sectoral coverage of lifelong learning.
2. 18 operational profiles in production, with real credentials issued.
3. Technical uniformity with purely semantic differences between types.
4. Validation in 16 Member States and 36 institutions, covering 89 % of the EU population.
5. Interoperability between 4 validated wallet implementations.
6. Open architecture for sectoral extension without modification of the W3C-VCDM core.

The catalogue jointly realises **Requirements R1–R10** of chapter 02 at operational scale, and constitutes the empirical basis on which the [complete EUDIW profile for W3C-VC](./08-eudiw-profile.md) of the next chapter rests.

---

**Next**: [08 — Complete EUDIW profile for W3C-VC](./08-eudiw-profile.md)
