# Trust models accpeted for education and professional qualifications - Understanding the Classical PKI model and its extension using EBSI under eIDAS2

## Table of contents
- [Trust models accpeted for education and professional qualifications - Understanding the Classical PKI model and its extension using EBSI under eIDAS2](#trust-models-accpeted-for-education-and-professional-qualifications---understanding-the-classical-pki-model-and-its-extension-using-ebsi-under-eidas2)
  - [Table of contents](#table-of-contents)
  - [1. Classical PKI Trust Model: Purpose and Structure](#1-classical-pki-trust-model-purpose-and-structure)
    - [a. Identifying Issuers](#a-identifying-issuers)
    - [b. Identifying Relying Parties and Intermediaries](#b-identifying-relying-parties-and-intermediaries)
    - [c. Authorised Requests to EUDI Wallets](#c-authorised-requests-to-eudi-wallets)
  - [2. Limitations of the Classical PKI Model in Education and Qualifications Governance](#2-limitations-of-the-classical-pki-model-in-education-and-qualifications-governance)
    - [a. It proves who an entity is, not what it is allowed to do](#a-it-proves-who-an-entity-is-not-what-it-is-allowed-to-do)
    - [b. No dynamic governance layer](#b-no-dynamic-governance-layer)
  - [3. A Complementary Trust Model: dPKI and Verifiable Authorisations under EBSI and eIDAS2](#3-a-complementary-trust-model-dpki-and-verifiable-authorisations-under-ebsi-and-eidas2)
    - [a. What is dPKI?](#a-what-is-dpki)
    - [b. How it works](#b-how-it-works)
    - [c. What this enables](#c-what-this-enables)
    - [d. Concrete example](#d-concrete-example)
  - [4. Conclusion](#4-conclusion)

## 1. Classical PKI Trust Model: Purpose and Structure

The **Public Key Infrastructure (PKI)** trust model is the cornerstone of secure digital identity in Europe and globally. It enables **authentication**, **confidentiality**, and **integrity** through digital certificates issued by **trusted Certification Authorities (CAs)**. These certificates bind a public key to the identity of a natural or legal person.

Under the **eIDAS** framework (and further reinforced in **eIDAS2**), this trust model plays a central role in:

### a. Identifying Issuers
Issuers of verifiable credentials (universities, ministries, public authorities, professional bodies, etc.) use **qualified certificates for electronic seals or website authentication**. These certificates ensure that the entity behind a DID or endpoint is **legally recognised and authentic**.

### b. Identifying Relying Parties and Intermediaries
Relying parties—those who **receive and verify** verifiable credentials—must also be clearly identified. In many contexts (e.g., professional qualification recognition, cross-border mobility portals), this identification is **mandated**.

To fulfil this, eIDAS2 introduces **electronic attribute certificates**—standardised mechanisms that bind **specific roles or rights** to the identity of the relying party or their **intermediaries** (e.g. gateways, digital campus platforms, national nodes).

### c. Authorised Requests to EUDI Wallets
These relying parties or their intermediaries may also need to **initiate interactions** with EUDI Wallet holders, such as requesting presentation of the **PID (Person Identification Data)** or specific **Electronic Attestations of Attributes (EAAs)**. To do so, they must prove:
- Their **identity** (via qualified certificate)
- Their **entitlement** to request a given credential (via electronic attribute certificate)

This mechanism ensures security, transparency, and legal certainty throughout the interaction chain.

## 2. Limitations of the Classical PKI Model in Education and Qualifications Governance

While robust and mature, the classical PKI trust model presents several **limitations when applied to the granular governance needs** of education and professional qualifications:

### a. It proves who an entity is, not what it is allowed to do
PKI enables the verification of an issuer’s legal identity but **does not communicate the authorisation** of that issuer to issue a certain **type of educational or professional credential**.

**Examples**:
- A digital certificate may confirm that a university exists, but not whether it is authorised to issue an **EQF level 7 diploma**.
- A professional association may be legally identified, but the PKI does not state whether it can issue a **ProfessionalID** or conduct **continuing medical education (CME)** quality assurance.

### b. No dynamic governance layer
Classical PKI lacks the ability to represent and manage the **hierarchical and federated authorisation structures** required in education:
- Ministries authorising universities
- National QA agencies accrediting regional bodies
- NRENs acting as intermediaries for federated identities (MyAcademicID)

These **multi-tiered relationships** are critical in Europe’s diverse and decentralised education landscape.

## 3. A Complementary Trust Model: dPKI and Verifiable Authorisations under EBSI and eIDAS2

To address these gaps, the DC4EU initiative—aligned with **EBSI**, the **European Learning Model**, and **eIDAS2**—proposes a **decentralised PKI model (dPKI)** based on **verifiable credentials and electronic attestations of attributes (EAAs)**.

### a. What is dPKI?
Decentralised PKI leverages **W3C Verifiable Credentials** and **DIDs (Decentralised Identifiers)**. It does not replace classical PKI but **extends it** with a layer of **governed, verifiable authorisations**.

### b. How it works
In this model:
- Root TAOs (e.g. Ministries, EQAR, GEANT) issue **EAA-based verifiable credentials** to authorised entities (e.g. universities, professional bodies, QA agencies)
- These credentials include statements such as:
  - `"LicenceToActAtNationalLevel"`
  - `"EQFlevel8Issuer"`
  - `"MyAcademicIDIssuer"`
  - `"QualityAssuranceAtProgrammeLevel"`
- These authorisations are **signed, timestamped and traceable**, and can be verified by any relying party in real time.

### c. What this enables
- **Granular, role-based trust**: Not only who the issuer is, but what they are allowed to issue, and by whom they were authorised
- **Federated governance**: Alignment with how education and qualifications are governed in the EU
- **Cross-border interoperability**: Supports the goals of the **European Education Area**, **EQF implementation**, and **automatic recognition** of learning outcomes

### d. Concrete example
A university in Spain (e.g. URV) presents a verifiable credential proving it is authorised by the Ministry of Science to issue:
- Degrees at EQF level 7
- EducationalID
- AllianceID credentials

This can be validated in real time by a verifier in another Member State, using standard EBSI trust registries and linked data proofs.

## 4. Conclusion

The **classical PKI trust model remains essential** for securing identity and ensuring compliance with legal frameworks. However, to **fully enable trusted governance of education and qualifications**, it must be **complemented** by a **dPKI model** based on **EAAs** and **verifiable authorisations**.

This layered model provides:
- Legal identity (PKI)
- Role-based authorisation (dPKI)
- Seamless verification across Member States
- Trustable, automated, and governed interaction with the EUDI Wallet

Such a combination is not only desirable—it is indispensable for implementing the principles of **eIDAS2**, the **Single Digital Gateway Regulation**, and the **European Education Area**.

