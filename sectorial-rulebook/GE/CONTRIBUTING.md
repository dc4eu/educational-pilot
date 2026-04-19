# Contribution guide

Thank you for your interest in reviewing and contributing to this documentation on W3C-VCDM for lifelong learning within the EUDI Wallet framework.

## Editorial principles

### Affirmative tone

The documentation articulates the benefits of W3C-VCDM as **requirements that lifelong learning needs to satisfy**, not as arguments against other formats. Contributions must respect this principle:

- Express the capabilities of W3C-VCDM in affirmative terms (what it contributes, what it enables, what it satisfies).
- Acknowledge the regulatory context of the EUDIW: three credential formats are formally referenced, and this document advocates for symmetrical regulatory treatment among all of them.
- Avoid disparaging comparisons, negative characterisations or adversarial language towards other technical formats.
- Document empirical, regulatory and technical evidence objectively.

### Technical and regulatory accuracy

- Always reference W3C Recommendations, ETSI specifications, CIRs and EU Regulations with a complete identifier and date.
- Examples in JSON-LD, SHACL (Turtle) and JSON Schema must be validatable by standard tools.
- Proposed regulatory requirements must include the identifier (for example `EAA-7.2.1.3-W3C-02`) and a reference to the applicable article of the Regulation or ETSI clause.

### Language

The main body is in **English (UK)**. The following are accepted:

- Contributions in UK English directly on the existing files.
- Translation proposals to other official EU languages via a pull request that creates a per-language sub-directory (`./es/`, `./de/`, `./fr/`, etc.) without modifying the body in English.

## How to review

1. **Coherence review**: detect contradictions between chapters, broken cross-references, incorrect numbering.
2. **Source review**: verify that every empirical statement is supported by a citable source in [`annexes/B-sources.md`](./docs/annexes/B-sources.md).
3. **Technical review**: validate that JSON-LD and SHACL snippets are well-formed, that references to controlled vocabularies (EQF, ESCO, ISCED-F) use correct IRIs, and that SHACL shapes are executable.
4. **Tone review**: ensure that the affirmative editorial principle is respected throughout.

## How to propose changes

### Issues

For each finding in the review, open an issue in the repository with:

- **Title**: summary of the finding.
- **Affected file(s)**: relative path from the root.
- **Type**: `typo`, `factual`, `normative`, `structural`, `tone`, `sources`, `translation`.
- **Description**: explanation of the problem and suggested correction.

### Pull requests

Modifications are proposed via pull request against the `main` branch:

- One PR per coherent topic (do not group heterogeneous changes).
- Clear description of the changes and their justification.
- Reference to the corresponding issue where applicable.

### New-content proposals

To add content (new chapter, new section, new annex), first open a discussion issue to reach consensus on placement and scope before opening the pull request.

## Profile of third-party reviewers

This document is intended for review by:

- Members of the **W3C Verifiable Credentials Working Group** and affiliated communities.
- Members of **ETSI TC ESI**, especially participants in ETSI TS 119 472-1.
- Members of the **OpenID Foundation** and the **Digital Credentials Consortium**.
- **DG CONNECT** of the European Commission, units responsible for eIDAS 2.0.
- Consortia of **DC4EU**, **TRACE4EU**, **EBSI VECTOR**, **Catena-X**, **Gaia-X** and other projects funded by the **Digital Europe Programme**.
- National standardisation bodies and educational quality-assurance agencies (**ENQA**, **EQAR**, member agencies).
- University associations (**EUNIS**, **CRUE**, **EUA**) and global educational networks (**Groningen Declaration Network**, **1EdTech**, **Credential Engine**).

## Code of conduct

Contributors are expected to behave in a professional, respectful and constructive manner. Technical discussions are welcome; personal attacks, offensive language and adversarial characterisations towards persons or organisations are not.

## Contact

For general queries or matters not resolved through issues or pull requests, contact the principal author through the channels indicated in the repository profile.
