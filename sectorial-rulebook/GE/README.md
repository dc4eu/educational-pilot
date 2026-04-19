# Why W3C-VCDM is necessary for education and lifelong learning

**Structured documentation on the W3C Verifiable Credentials Data Model (VCDM) 1.1 and 2.0 as the foundation of educational and professional credentialing in the EUDI Wallet framework (eIDAS 2.0).**

---

## Purpose of this repository

This repository consolidates the technical, regulatory and operational case for full adoption of the **W3C Verifiable Credentials Data Model (W3C-VCDM)** — in its versions 1.1 (the mandate currently in force under the first batch of Implementing Acts of eIDAS 2.0) and 2.0 (W3C Recommendation of 15 May 2025, forward-looking optional profile) — as a required format for credentialing of **education understood as lifelong learning** within the European Digital Identity Wallet (EUDIW) framework.

The document is written in affirmative terms. It articulates the capabilities of W3C-VCDM as requirements that lifelong learning needs to satisfy, and it documents how the standard satisfies them by design and how they have already been validated in production by European public investment.

## Structure of the documentation

The documentation is organised in eleven thematic chapters and three annexes, all in Markdown, intended for third-party review and for eventual publication in a public repository.

| # | Document | Content |
|---|---|---|
| 00 | [Executive summary](./docs/00-executive-summary.md) | Synthesis for public-policy decision-makers and members of standardisation bodies |
| 01 | [Context and foundations](./docs/01-context-and-foundations.md) | eIDAS 2.0 framework, CIRs 2024/2977, 2024/2979, 2024/2982, ETSI TS 119 472-1, W3C Recommendations of 15 May 2025 |
| 02 | [Requirements of lifelong learning](./docs/02-lifelong-learning-requirements.md) | The ten substantive requirements of lifelong learning for digital credentialing |
| 03 | [Benefits of W3C-VCDM](./docs/03-w3c-vcdm-benefits.md) | How W3C-VCDM satisfies each of the ten requirements |
| 04 | [Dual validation architecture](./docs/04-dual-validation-architecture.md) | JSON Schema + SHACL over the RDF graph, EBSI TSR v3 register, example Turtle shapes |
| 05 | [European Learning Model (ELM v3.2)](./docs/05-european-learning-model.md) | European ontological model of learning and its integration with W3C-VCDM |
| 06 | [Lifecycle and trust](./docs/06-lifecycle-and-trust.md) | BitstringStatusList, hybrid PKI–dPKI model, structural privacy (no "phone home") |
| 07 | [Sectoral EAA catalogue](./docs/07-sectoral-eaa-catalogue.md) | 14 educational and professional types + 4 quality-assurance types over W3C-VCDM |
| 08 | [Complete EUDI Wallet profile for W3C-VC](./docs/08-eudiw-profile.md) | Two-layer profile (ETSI TS 119 472-1 cl.7 + Commission regulatory adaptations), regulatory proposal for CIR 2024/2977 and CIR 2024/2979 |
| 09 | [Unique capabilities of W3C-VCDM](./docs/09-vcdm-unique-capabilities.md) | Educational requirements that W3C-VCDM uniquely satisfies |
| 10 | [Roadmap and recommendations](./docs/10-roadmap.md) | Procedural path, recommendations to the Commission, transition from VCDM 1.1 to VCDM 2.0 |
| A | [Glossary](./docs/annexes/A-glossary.md) | Technical terms and acronyms |
| B | [Sources](./docs/annexes/B-sources.md) | Regulatory, technical and empirical references |
| C | [Stakeholders and evidence](./docs/annexes/C-stakeholders-evidence.md) | European ecosystem, funded pilots, contributions to public consultations |

## How to read this repository

- **Policy-makers and members of the Council / European Parliament**: begin with the [Executive summary](./docs/00-executive-summary.md) and the [Roadmap](./docs/10-roadmap.md).
- **W3C, OpenID Foundation and ETSI ESI reviewers**: begin with the [Complete EUDI Wallet profile](./docs/08-eudiw-profile.md) and the [Dual validation architecture](./docs/04-dual-validation-architecture.md).
- **Educational community (universities, VET, QA agencies, professional bodies)**: begin with the [Requirements](./docs/02-lifelong-learning-requirements.md), the [Benefits](./docs/03-w3c-vcdm-benefits.md) and the [Sectoral catalogue](./docs/07-sectoral-eaa-catalogue.md).
- **Technical implementers**: begin with the [Dual validation architecture](./docs/04-dual-validation-architecture.md), the [Lifecycle and trust](./docs/06-lifecycle-and-trust.md) and the [Unique capabilities](./docs/09-vcdm-unique-capabilities.md).

## Guiding principle of the document

This document articulates the benefits of W3C-VCDM **in affirmative terms**, as native capabilities and requirements that the format satisfies by design. References to other formats appear exclusively in a neutral regulatory context (symmetrical treatment of the three formats formally referenced in the EUDIW framework), without negative qualifications or disparaging comparisons. The objective is to document what W3C-VCDM contributes to education and lifelong learning, not to detract value from other options.

## How to contribute

See [CONTRIBUTING.md](./CONTRIBUTING.md) for contribution, review and amendment-proposal guidelines.

## Licence

The content of this repository is published under a **Creative Commons Attribution 4.0 International (CC BY 4.0)** licence. See [LICENSE](./LICENSE) for the full text.

## Authorship and credits

- **Principal author**: Lluís Alfons Ariño Martín — Convenor, EU Digital Credentials (EBSI/EUDI Wallet); Executive Strategist: Digital Transformation, eGovernment & SSI Policy; EUNIS Board Member.
- **Empirical base**: DC4EU Large Scale Pilot (Digital Europe Programme, €19M, 36 institutions, 16 Member States, 2,790 real credentials issued, 18 credential types).
- **Regulatory base**: first batch of Implementing Acts of Regulation (EU) 2024/1183 (CIR 2024/2977, CIR 2024/2979, CIR 2024/2982), ETSI TS 119 472-1 V1.1.1, W3C Recommendations of 15 May 2025 and Candidate Recommendation of 3 April 2025.

## Document version

- **Version**: 1.0.0
- **Date**: April 2026
- **Status**: Draft for third-party review

---

*This repository complements the public consultation Ref. Ares(2026)1286304 and the 43 contributions received by the European Commission during the period February–March 2026.*
