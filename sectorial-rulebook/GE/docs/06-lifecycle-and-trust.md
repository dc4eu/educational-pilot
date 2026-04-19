# 06 — Lifecycle, trust framework and privacy

## 6.1 The complete lifecycle of a learning credential

An educational credential is not a static artefact. From its issuance to its expiry (or revocation), it traverses states that must be representable and verifiable in a standardised manner:

| State | Meaning | W3C-VCDM mechanism |
|---|---|---|
| **Issued** | The credential has been signed and published. | Cryptographic proof (Data Integrity or JOSE/COSE) in the credential. |
| **Active** | The credential is presentable and verifiable by third parties. | Absence of an entry in `BitstringStatusList` with `statusPurpose: "revocation"`. |
| **Suspended** | The credential has been temporarily suspended (investigation, complaint, doubt about the achievement). | Active bit in `BitstringStatusList` with `statusPurpose: "suspension"`. |
| **Restored** | The credential becomes valid again after a suspension. | Deactivated bit in `BitstringStatusList` with `statusPurpose: "suspension"`. |
| **Revoked** | The credential has been invalidated definitively. | Active bit in `BitstringStatusList` with `statusPurpose: "revocation"`. |
| **Expired** | The credential has passed its `validUntil`. | `validUntil` field in the credential. |
| **Renewed** | A new credential replaces the previous one. | Issuance of a new credential; revocation of the former. |

The **suspended** and **revoked** states are **regulatory requirements** in the EUDIW, established by Article 24 and Section 9 of Regulation 2024/1183. Both are natively supported by W3C-VCDM without proprietary extensions.

## 6.2 BitstringStatusList as a native mechanism

The **W3C Recommendation Bitstring Status List v1.0** (15 May 2025) formalises a mechanism of status lists over compressed bitstrings. A `BitstringStatusListEntry` entry in the credential references a position within a list signed by the issuer; the verifier downloads the list, checks the bit at the indicated position and derives the status.

### 6.2.1 Joint declaration of revocation and suspension

A single credential can simultaneously declare entries for revocation and suspension, referencing independent lists:

```json
"credentialStatus": [
  {
    "id": "https://status.example.eu/pilot/bsl-revocation-2026#12345",
    "type": "BitstringStatusListEntry",
    "statusPurpose": "revocation",
    "statusListIndex": "12345",
    "statusListCredential": "https://status.example.eu/pilot/bsl-revocation-2026"
  },
  {
    "id": "https://status.example.eu/pilot/bsl-suspension-2026#12345",
    "type": "BitstringStatusListEntry",
    "statusPurpose": "suspension",
    "statusListIndex": "12345",
    "statusListCredential": "https://status.example.eu/pilot/bsl-suspension-2026"
  }
]
```

A conformant verifier shall consult **both** lists and derive the aggregate status: valid ↔ no bit active; suspended ↔ bit active in suspension list; revoked ↔ bit active in revocation list.

### 6.2.2 Advantages of the mechanism

- **Efficiency**: a list of one million credentials occupies less than 16 KiB after GZIP compression. The download is one-off and cacheable.
- **Privacy**: the verifier downloads the complete list and does not query a specific endpoint for the credential. The issuer **cannot observe** when or how a credential is verified (anti-"phone home" principle).
- **Portability**: the list is itself a Verifiable Credential signed by the issuer, which can be published on EBSI, on an IPFS/URL classic, or on any accessible register.
- **Multiple purposes**: the standard admits additional `statusPurpose` values (`message`, `error`, etc.) for future signalling without modifying the format.

## 6.3 Absence of the "phone home" effect

The educational ecosystem is especially sensitive to the principle that **the issuer shall not observe** where, when or to whom the person presents their credential. A university should not know that a former student has presented their microcredential to a specific employer on the day before an interview. This is a key property of digital dignity and of GDPR compliance on minimisation and purpose limitation.

W3C-VCDM, combined with `BitstringStatusList`, guarantees this property:

- The list is downloaded once by the verifier and is cached.
- The issuer observes downloads of the complete list, never targeted queries for a credential.
- The architecture is **aggregated by construction**: one thousand verifications of one thousand distinct credentials result in a single list download.

This property partially realises **Requirement R5** (structural privacy) of chapter 02.

## 6.4 Selective disclosure and unlinkability

Selective presentation is the mechanism by which the person reveals to the verifier only the attributes strictly necessary for the specific purpose (GDPR minimisation principle).

W3C-VCDM supports two families of selective-disclosure mechanisms with distinct properties:

### 6.4.1 SD-based selective disclosure (salted-hash)

Mechanisms such as SD-JWT (and its JOSE/COSE counterpart) allow fields to be revealed by de-salting their hashes. The person presents the salts corresponding to the attributes to be revealed; the rest remain protected.

**Property**: the verifier receives a document signed by the issuer with only the requested attributes.

### 6.4.2 BBS+ signatures (`bbs-2023`) and cryptographic unlinkability

The **W3C Candidate Recommendation Data Integrity BBS Cryptosuites v1.0** (3 April 2025) formalises `bbs-2023` as a Data Integrity cryptosuite over BLS12-381. The characteristic property is **unlinkability** between presentations: the person can present the same credential to two different verifiers, generating cryptographically **uncorrelatable** proofs.

Operational consequence: even if two verifiers collaborate and compare the identifiers received, **they cannot determine** whether the two presentations correspond to the same person or to different persons.

This property realises **Article 3(10) of Regulation 2024/2982**, which requires unlinkability for PID with LoA High. W3C-VCDM is the only format referenced in the EUDIW that has a **native Data Integrity cryptosuite with unlinkability**, documented as a W3C Candidate Recommendation.

## 6.5 Hybrid PKI-dPKI trust framework

The EUDIW trust framework combines two architectures:

### 6.5.1 Classical eIDAS PKI (hierarchical)

The chain of qualified certificates (QTS, QSealC, QWAC) rests on the **EU Trusted List (LOTL)** published by the Commission and maintained by the Member States. Each Member State publishes its national Trusted List (clause 3.1 of Implementing Regulation (EU) 2015/1505) with the authorised Qualified Trust Service Providers.

### 6.5.2 Decentralised infrastructure (EBSI)

The **European Blockchain Services Infrastructure (EBSI)** operates as a complementary decentralised register:

- **Trusted Issuers Registry (TIR)**: register of issuers with their DIDs and accreditations.
- **Trusted Accreditation Organisations Registry (TAOR)**: register of the authorities that accredit issuers.
- **Trusted Schemas Registry (TSR) v3**: register of authoritative schemas (JSON Schemas and SHACL shapes).
- **Verifiable Revocation Registry**: registers of status lists.

### 6.5.3 Convergence for the educational domain

For educational EAAs, the operational convergence between both architectures is as follows:

- The issuer (university, VET centre, employer) is registered in the **Trusted Issuers Registry** with its DID.
- The DID resolves to a DID document that includes verifiable public keys and references to valid accreditations.
- Accreditations are themselves Verifiable Credentials signed by quality agencies (members of **ENQA / EQAR** or equivalents) registered in the **TAOR**.
- Schemas (JSON + SHACL) are registered in the **TSR v3** with immutable identifiers.
- Status lists are published as Verifiable Credentials signed by the issuer.

The result is a **verifiable end-to-end trust chain**: any verifier can, with only the credential received and access to the EBSI registers and to the European LOTL, establish technical, semantic, accreditation and status validity without mediation by the issuer.

## 6.6 Issuer identity and `eidasLegalIdentifier`

Article 3(6) and Annex V of Regulation 2024/1183 establish that a qualified EAA must be traceable to a **real legal person identified under eIDAS**. W3C-VCDM supports this requirement through the `eidasLegalIdentifier` field in the `issuer`:

```json
"issuer": {
  "id": "did:ebsi:zDnaeUC5QAe9gpMJhbU1J4s7A",
  "type": "Organisation",
  "legalName": "Universitat Rovira i Virgili",
  "eidasLegalIdentifier": "urn:eidas:legalPersonIdentifier:ES:Q9350003A",
  "registeredIn": {
    "id": "http://data.europa.eu/eli/jurisdiction/ESP",
    "type": "Jurisdiction"
  }
}
```

The identifier is constructed with the scheme defined in the Annex of Implementing Regulation (EU) 2015/1501 (unique legal-person identifier in the country–type–national-identifier format). The correspondence between the DID `did:web` (or `did:ebsi`) and the `eidasLegalIdentifier` is declared by the issuer and attested by the accreditation agency, closing the PKI ↔ dPKI bridge for legal identity.

## 6.7 Mapping of quality accreditations (ENQA/EQAR)

Quality accreditations are represented as independent credentials, typed as `Accreditation` in ELM:

```json
{
  "@context": [
    "https://www.w3.org/ns/credentials/v2",
    "http://data.europa.eu/snb/model/context/edc-ap.jsonld"
  ],
  "type": ["VerifiableCredential", "Accreditation"],
  "issuer": "did:ebsi:zAccredAgent-ANECA",
  "credentialSubject": {
    "id": "did:ebsi:zDnaeUC5QAe9gpMJhbU1J4s7A",
    "type": "Organisation",
    "accreditationFor": "http://data.europa.eu/snb/qualification-type/he-programme",
    "decisionDate": "2024-06-15",
    "validFrom": "2024-09-01",
    "validUntil": "2030-08-31",
    "accreditingAgent": {
      "id": "urn:agent:EQAR:ANECA",
      "legalName": "Agencia Nacional de Evaluación de la Calidad y Acreditación"
    },
    "registeredIn": "https://www.eqar.eu/register/..."
  }
}
```

The `Accreditation` is itself an EAA, following the same dual JSON Schema + SHACL profile. It can be suspended or revoked via `BitstringStatusList`, and its issuer (the quality agency) is in turn registered in the TAOR.

This **uniform recursion** (credentials over credentials, with the same lifecycle) is a property of W3C-VCDM that drastically simplifies the architecture of the educational trust framework.

## 6.8 Protection of personal data and GDPR

The architecture satisfies the applicable GDPR principles:

- **Lawfulness and transparency**: the legal basis is established by eIDAS 2.0 and by the sectoral educational rules.
- **Minimisation**: selective disclosure limits the data revealed to the specific purpose.
- **Purpose limitation**: the verifier can only process the attributes revealed.
- **Integrity and confidentiality**: cryptographic proofs guarantee integrity; the presentation channel (OID4VP) guarantees confidentiality.
- **Right to erasure**: although an issued credential cannot be "erased" retrospectively, revocation definitively invalidates its use. Expired credentials may be purged from the wallet's store if the person so decides.
- **Portability**: the VCDM format is open; the person can export their credentials to any conformant wallet.

## 6.9 Interoperability between wallets

Within the DC4EU framework, the interoperability of the EUDIW W3C-VC profile was validated between **four independent wallet implementations**:

- **ISRAEL wallet** (Izertis, Spain).
- **UAegean wallet** (University of the Aegean, Greece).
- **Netcompany wallet** (Netcompany-Intrasoft, Luxembourg/Denmark).
- **Cappatrust wallet** (Cappatrust, Belgium).

Credentials issued by one implementer were received, stored and presented by the other three without modifications. This outcome demonstrates that the W3C-VC profile is **effectively portable** and satisfies **Requirement R7** of chapter 02.

## 6.10 Outcome

The lifecycle and trust framework for an educational EAA over W3C-VCDM covers all identified regulatory and operational requirements:

1. Full lifecycle with native suspension and revocation (Article 24, Section 9 of Regulation 2024/1183).
2. Absence of "phone home" effect via `BitstringStatusList`.
3. Selective disclosure and cryptographic unlinkability (BBS+).
4. Issuer identity with `eidasLegalIdentifier` and verifiable accreditation chain.
5. Hybrid PKI eIDAS ↔ dPKI EBSI trust framework.
6. Structural GDPR compliance.
7. Interoperable portability between wallet implementations.

These properties are complemented by the semantics provided by the [European Learning Model](./05-european-learning-model.md), the [dual validation architecture](./04-dual-validation-architecture.md) and the [Sectoral EAA catalogue](./07-sectoral-eaa-catalogue.md).

---

**Next**: [07 — Sectoral EAA catalogue](./07-sectoral-eaa-catalogue.md)
