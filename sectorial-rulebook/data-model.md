# Data Model

## Overview

The credential data model follows W3C Verifiable Credential standards, structuring educational data in a consistent format. This standardised approach enables interoperability whilst supporting the specific needs of educational credentials.

## Compliance with 1st Batch of eIDAS Implementing Acts

In alignment with the **first batch of eIDAS implementing acts**, specifically the implementing regulation **"laying down rules for the application of Regulation (EU) No 910/2014 of the European Parliament and of the Council as regards person identification data and electronic attestations of attributes issued to European Digital Identity"**, the European framework mandates that **data shall be issued in two formats**:

### Mandated Data Formats

1. **ISO/IEC 18013-5:2021 [ISO18013-5] format** where person identification data attributes must be encoded in **CBOR**
2. **W3C Verifiable Credentials Data Model 1.1** where person identification data attributes must be encoded in **JSON**

> **Regulatory status — VCDM 1.1 vs VCDM 2.0.** The 1st batch of eIDAS 2.0 Implementing Acts **currently mandates W3C‑VCDM 1.1** for electronic attestations of attributes encoded in JSON. **W3C‑VCDM 2.0** (W3C Recommendation, May 2025) is offered in this rulebook as an **additional, optional forward‑looking profile** — it does **not** replace VCDM 1.1. Future updates to the Implementing Acts are expected to recognise **both** versions; issuers and verifiers SHOULD be prepared to support both to preserve backward compatibility. See the [Dual Validation Architecture (SHACL + EBSI)](../sectorial-eaa-catalogue/edc-vcdm2.0/dual-validation-architecture.md) note for the details of the VCDM 2.0 profile.

### Strategic Choice: W3C-VCDM for Education and Professional Qualifications

For the **education and professional qualifications sector**, where **semantic richness, ontological alignment, and cross-border interoperability** are paramount, the chosen data model in full alignment with eIDAS and the 1st batch of implementing acts is **W3C Verifiable Credentials Data Model (W3C-VCDM)**.

This strategic choice is driven by several critical requirements:

**Semantic Richness Requirements**:
- Educational credentials require complex semantic relationships between learning outcomes, competencies, assessments, and achievements
- Professional qualifications demand precise representation of skills, competencies, and regulatory compliance
- The **European Learning Model (ELM)** ontology requires sophisticated data structures that W3C-VCDM can accommodate through JSON-LD

**Cross-Border European Alignment**:
- **European Education Area** initiatives require harmonised credential representation
- **Bologna Process** implementations benefit from semantic interoperability
- **European Qualifications Framework (EQF)** alignment necessitates structured ontological mapping
- **Europass Digital Credentials Infrastructure** integration requires W3C-VCDM compatibility

**Global Mobility Considerations**:
- **Beyond-Europe mobility** requires internationally recognised standards
- **W3C-VCDM** provides global interoperability for European credentials
- **JSON-based encoding** ensures universal accessibility and processing
- **International academic recognition** benefits from globally adopted standards

**Technical and Regulatory Advantages**:
- **JSON encoding** provides human-readable and machine-processable format
- **Linked Data capabilities** through JSON-LD enable rich semantic expression
- **Extensibility** supports evolving educational and professional requirements
- **Privacy-preserving features** align with GDPR and eIDAS privacy principles

## Implementation: EDC-W3C-VCDM

The practical implementation is achieved through **European Digital Credentials compliant with W3C-VCDM (EDC-W3C-VCDM)**, which represents:

- **ELM ontology serialisation** in W3C-VCDM format
- **Full compliance** with the 1st batch of implementing acts
- **Semantic interoperability** across European educational systems
- **Global recognition** through internationally adopted standards

This approach ensures that educational and professional credentials issued in Europe are:
- **Legally compliant** with eIDAS implementing acts
- **Semantically rich** to represent complex educational achievements
- **Globally interoperable** for international mobility
- **Privacy-preserving** through advanced W3C-VCDM features

### Optional Forward‑Looking Profile: EDC‑W3C‑VCDM 2.0 (Dual Validation)

In addition to the mandatory EDC‑W3C‑VCDM 1.1 profile described above, this rulebook offers an **optional EDC‑W3C‑VCDM 2.0 profile** that issuers MAY adopt when they are ready. This profile does **not** replace VCDM 1.1 — both coexist — and it introduces a **dual validation architecture** in the credential's `credentialSchema[]` array:

- **`JsonSchema`** enforces the syntactic constraints over the JSON tree (the layer already used in VCDM 1.1).
- **`ShaclValidator2017`** enforces the semantic/ontological constraints on the RDF graph that emerges from interpreting the JSON‑LD through its **ELM v3.2** context. This is what the VCDM 1.1 profile cannot express natively.

Both schemas are registered in the EBSI Trusted Schemas Registry v3, making them verifiable, immutable and discoverable. Issuers following this profile SHOULD continue to issue the equivalent VCDM 1.1 credential whenever their relying parties require it, until the Implementing Acts formally recognise VCDM 2.0.

The concrete datamodels, JSON Schemas, SHACL shapes and signed/unsigned examples available today for this profile are listed in the [VCDM 2.0 table of the Sectorial EAA Catalogue](../sectorial-eaa-catalogue/README.md#table-with-available-datamodels-based-on-edc-w3c-w3c-vcdm-20-dual-json-schema--shacl-validation).

## Key Components

Each credential includes:

### Context Definitions
- Provides semantic definitions for credential interpretation using **JSON-LD contexts**
- Enables consistent understanding across systems through **European Learning Model** vocabulary
- Links to standardised vocabularies including **EQF, ESCO, and educational taxonomies**
- Supports semantic interoperability through **W3C-VCDM context mechanisms**

### Unique Identifier
- Creates a distinct reference for each credential following **W3C-VCDM identifier requirements**
- Supports verification and tracking through **cryptographically verifiable identifiers**
- Enables reference across systems using **DIDs or HTTP URIs**
- Maintains credential distinctiveness through **globally unique identifiers**

### Credential Type
- Indicates the nature of the educational achievement using **W3C-VCDM type system**
- Supports appropriate handling by different systems through **semantic typing**
- Enables filtering and categorisation using **educational credential taxonomies**
- Aligns with educational taxonomies through **ELM-based type definitions**

### Issuing Authority Identifier
- Links the credential to its authoritative source using **verifiable issuer identifiers**
- Supports trust verification through **institutional DIDs or certificates**
- Enables institutional recognition through **trusted issuer registries**
- Connects to trusted issuer registries via **EBSI trust infrastructure**

### Issue Date and Validity
- Records when the credential was officially granted using **ISO 8601 date formats**
- Supports timelines of achievement through **temporal validity indicators**
- Enables chronological organisation of **educational progression**
- Facilitates validity checking through **machine-readable date constraints**

### Credential Subject Information
- Identifies the person to whom the credential belongs using **privacy-preserving identifiers**
- Links achievements to individual educational journeys through **verifiable subject identification**
- Supports privacy-protecting identification via **selective disclosure mechanisms**
- Enables appropriate credential attribution through **cryptographic binding**

### Educational Achievement Data
- Represents learning outcomes using **European Learning Model structures**
- Documents competencies and skills through **ESCO-aligned taxonomies**
- Records assessment results using **EQF-compliant level indicators**
- Supports quality assurance information through **accreditation references**

### Cryptographic Proof of Authenticity
- Ensures the credential hasn't been tampered with using **W3C-VCDM proof mechanisms**
- Supports verification of issuer authority through **digital signatures**
- Enables trust establishment via **cryptographic verification protocols**
- Protects credential integrity through **tamper-evident proofs**

### Multi-language Support
- Enables credential interpretation across languages using **JSON-LD language tags**
- Supports mobility across language regions through **multilingual field encoding**
- Facilitates cross-border understanding via **European language support**
- Respects linguistic diversity through **native language preservation**

## Implementation Considerations

When implementing the W3C-VCDM data model for educational credentials:
- **JSON-LD contexts** should reference European Learning Model vocabularies
- **Cryptographic suites** should follow current W3C-VCDM best practices and eIDAS requirements
- **Schema validation** should implement both W3C-VCDM and ELM compliance checking. Under the mandatory VCDM 1.1 profile, this is done via a single `JsonSchema` entry in `credentialSchema`. Under the optional VCDM 2.0 profile, this is done via the **dual validation architecture**: `JsonSchema` (syntactic) **plus** `ShaclValidator2017` (semantic, ELM v3.2). Both profiles MUST be accepted by verifiers during the transition period.
- **Extensibility** should be supported for future educational requirements whilst maintaining compatibility
- **Backwards compatibility** should be maintained with existing European credential systems, in particular: verifiers SHOULD accept both VCDM 1.1 and VCDM 2.0 credentials throughout the transition period defined by the evolution of the eIDAS Implementing Acts
- **Privacy features** should leverage W3C-VCDM selective disclosure capabilities
- **Status management** should implement privacy-preserving revocation mechanisms

## Cross-Border Scenarios

For cross-border educational mobility and professional recognition, the W3C-VCDM data model provides:
- **Consistent interpretation** of credentials across all member states through semantic interoperability
- **Multilingual credential representation** using JSON-LD language support
- **Standardised formats** for qualification recognition through W3C global standards
- **Interoperability** between different national systems via shared data model
- **Semantic alignment** with European educational frameworks through ELM integration
- **Global recognition** potential through internationally adopted W3C standards

## Alignment with Standards and Frameworks

The W3C-VCDM implementation aligns with:
- **W3C Verifiable Credentials Data Model 1.1** as **currently mandated** by the 1st batch of eIDAS Implementing Acts
- **W3C Verifiable Credentials Data Model 2.0** (W3C Recommendation, May 2025) as **optional forward‑looking profile**, expected to be recognised alongside 1.1 in future Implementing Act updates
- **SHACL (Shapes Constraint Language)** for semantic/ontological validation of the ELM graph under the VCDM 2.0 profile
- **European Learning Model (ELM) v3.2** for educational semantic representation
- **Europass Digital Credentials Infrastructure** for European credential interoperability
- **European Qualifications Framework (EQF)** for qualification level representation
- **ESCO taxonomy** for skills and competency classification
- **Schema.org educational vocabulary** for global semantic interoperability
- **eIDAS 2.0 requirements** for European digital identity compliance
- **GDPR principles** for privacy-preserving credential management

## Technical Standards Integration

The implementation ensures compliance with:
- **ISO/IEC 18013-5:2021** compatibility for hybrid scenarios where CBOR encoding is required
- **W3C-VCDM 1.1 specification** for core credential structure and verification (currently mandatory)
- **W3C-VCDM 2.0 specification** for the optional dual‑validation profile (currently optional; accepted alongside 1.1 and expected to become formally recognised)
- **SHACL (Shapes Constraint Language, W3C Recommendation)** for semantic validation in the VCDM 2.0 profile
- **JSON-LD 1.1** for semantic linking and context management
- **RFC 7519 (JWT)** for compact credential serialisation when required
- **StatusList2021** for privacy-preserving credential status management
- **European Blockchain Services Infrastructure (EBSI)** standards for trust anchoring (Trusted Schemas Registry v3 hosts both the JsonSchema and the ShaclValidator2017 shapes)

This comprehensive approach ensures that educational and professional credentials are not only compliant with current European regulations but also positioned for future evolution and global interoperability whilst maintaining the highest standards of privacy protection and semantic richness.