# 06 — Lifecycle, trust framework and privacy

## 6.1 The complete lifecycle of a learning credential

An educational credential is not a static artefact. From its issuance to its expiry (or revocation), it traverses states that must be representable and verifiable in a standardised manner:

| State | Meaning | W3C-VCDM mechanism |
|---|---|---|
| **Issued** | The credential has been signed and published. | JAdES-B-B enveloping proof (JOSE) or Data Integrity embedded proof (`ecdsa-rdfc-2019`). |
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

## 6.4 Signature mechanisms: JAdES-B-B and Data Integrity

W3C-VCDM supports two families of credential proof mechanisms, both operative within the EUDIW profile:

### 6.4.1 JAdES-B-B (enveloping JOSE proof) — operative today

**JAdES** (JSON Advanced Electronic Signatures, ETSI TS 119 182-1) is the European standard for advanced and qualified electronic signatures over JSON content. For W3C-VC EAAs with JOSE enveloping proofs:

- **Clause 7.6.4.2 of ETSI TS 119 472-1 V1.1.1** prescribes JAdES-B-B when Flattened JSON Serialisation is used.
- For **QEAAs**, the additional requirements of clause 5.6.2 (qualified seal requirements) apply under requirement `QEAA-7.6.4.4-01`.
- JAdES-B-B is accepted by all EU Member State governments, compliant with eIDAS 2.0, and verifiable with standard European trust service tools.
- **SD-JWT EAAs** with Flattened JSON Serialisation also use JAdES-B-B; with Compact Serialisation the structure is a JAdES-B-B Compact Serialisation followed by SD-JWT disclosures.

JAdES-B-B is the **primary operative signature mechanism** for W3C-VC qualified EAAs in the current regulatory cycle.

### 6.4.2 Data Integrity embedded proofs — operative today

**Data Integrity** proofs (`ecdsa-rdfc-2019`, as specified in W3C Recommendation of 15 May 2025) are embedded within the JSON-LD credential as a `proof` property. They:

- Are verified without proprietary APIs, realising **digital sovereignty by design**.
- Enable offline verification (no server round-trip required).
- Are compatible with the `ldp_vc` / `ldp_vp` presentation format identifiers defined in OpenID4VP.

Requirement `EAA-7.6.5-W3C-01` (proposed) prescribes `ecdsa-rdfc-2019` as the minimum admissible embedded cryptosuite.

### 6.4.3 BBS+ (`bbs-2023`) and the pathway to cryptographic unlinkability

The **W3C Candidate Recommendation Data Integrity BBS Cryptosuites v1.0** (3 April 2025) formalises `bbs-2023` as a Data Integrity cryptosuite over BLS12-381. Its characteristic property is **cryptographic unlinkability** between presentations: two presentations of the same credential to two different verifiers produce probabilistically uncorrelatable proofs — even under verifier collusion.

This property is the technical mechanism for realising **Article 3(10) of Regulation 2024/2982**, which requires unlinkability for PID at LoA High.

**Current regulatory status**: BLS12-381 is not currently listed among the agreed curves in the ENISA Agreed Cryptographic Mechanisms (v2.0, April 2025), and `bbs-2023` is not yet incorporated into ETSI TS 119 312. ETSI TS 119 312 is under active revision, and the inclusion of privacy-preserving cryptographic mechanisms — including pairing-based schemes — is within its declared scope. The pathway for `bbs-2023` adoption in the EUDIW perimeter is:

1. Incorporation of `bbs-2023` / BLS12-381 into ETSI TS 119 312.
2. Update of ETSI TS 119 472-1 to reference the incorporated cryptosuite.
3. Commission adaptation of ENISA Agreed Cryptographic Mechanisms to include the scheme.

Until that incorporation, `ecdsa-rdfc-2019` (Data Integrity) and JAdES-B-B (enveloping JOSE) are the operative proof mechanisms. Implementations wishing to offer forward-compatible unlinkability may implement `bbs-2023` in addition, and the proposed EUDIW profile (`EAA-7.6.5-W3C-01`) specifies that `bbs-2023` shall be added to the admitted cryptosuites upon its ETSI TS 119 312 incorporation.

For selective disclosure without full unlinkability, SD-JWT-based disclosure (salted-hash) is available using the same JSON payload, as the two serialisations are structurally compatible. Zero-knowledge proof mechanisms compatible with the SD-JWT VC signature scheme — such as those under development in the Longfellow-ZK initiative — may also be referenced once stabilised, as they are architecturally compatible with JSON-based credentials.

## 6.5 Selective disclosure

Selective presentation is the mechanism by which the person reveals to the verifier only the attributes strictly necessary for the specific purpose (GDPR minimisation principle).

Within the W3C-VCDM profile, two selective-disclosure mechanisms are operative:

- **SD-based selective disclosure (salted-hash)**: fields are disclosed by revealing the corresponding salts; the rest remain protected. Compatible with JAdES-B-B and JOSE enveloping proofs. The verifier receives a presentation containing only the requested attributes, under a signature that was produced by the issuer.
- **BBS+ derived proofs** (`bbs-2023`): once incorporated into ETSI TS 119 312, provides cryptographic unlinkability in addition to selective disclosure. The wallet generates a derived proof per presentation; no two derivations are correlatable. This is the mechanism that natively satisfies Article 3(10) of CIR 2024/2982.

Both mechanisms are JSON-based and structurally compatible; the issuer signature scheme determines which selective-disclosure path is available at presentation time.

## 6.6 Hybrid PKI-dPKI trust framework

The EUDIW trust framework combines two architectures:

### 6.6.1 Classical eIDAS PKI (hierarchical)

The chain of qualified certificates (QTS, QSealC, QWAC) rests on the **EU Trusted List (LOTL)** published by the Commission and maintained by the Member States. Each Member State publishes its national Trusted List (clause 3.1 of Implementing Regulation (EU) 2015/1505) with the authorised Qualified Trust Service Providers.

JAdES-B-B proofs on W3C-VC credentials are anchored to this PKI chain: the issuer's QSealC appears in the national Trusted List, and the verifier confirms it via the EU LOTL under CIR 2015/1505.

### 6.6.2 Decentralised infrastructure (EBSI)

The **European Blockchain Services Infrastructure (EBSI)** operates as a complementary decentralised register:

- **Trusted Issuers Registry (TIR)**: register of issuers with their DIDs and accreditations.
- **Trusted Accreditation Organisations Registry (TAOR)**: register of the authorities that accredit issuers.
- **Trusted Schemas Registry (TSR) v3**: register of authoritative schemas (JSON Schemas and SHACL shapes).
- **Verifiable Revocation Registry**: registers of status lists.

### 6.6.3 Convergence for the educational domain

For educational EAAs, the operational convergence between both architectures is as follows:

- The issuer (university, VET centre, employer) is registered in the **Trusted Issuers Registry** with its DID.
- The DID resolves to a DID document that includes verifiable public keys and references to valid accreditations.
- Accreditations are themselves Verifiable Credentials signed by quality agencies (members of **ENQA / EQAR** or equivalents) registered in the **TAOR**.
- Schemas (JSON + SHACL) are registered in the **TSR v3** with immutable identifiers.
- Status lists are published as Verifiable Credentials signed by the issuer.
- JAdES-B-B signatures on QEAAs are anchored through the issuer's QSealC in the national Trusted List.

The result is a **verifiable end-to-end trust chain**: any verifier can, with only the credential received and access to the EBSI registers and to the European LOTL, establish technical, semantic, accreditation and status validity without mediation by the issuer.

## 6.7 Issuer identity and `eidasLegalIdentifier`

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

The identifier is constructed with the scheme defined in the Annex of Implementing Regulation (EU) 2015/1501. The JAdES-B-B enveloping proof anchors the issuer's legal identity to the QSealC in the national Trusted List, establishing the PKI ↔ dPKI bridge for qualified credentials.

## 6.8 Mapping of quality accreditations (ENQA/EQAR)

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

## 6.9 Protection of personal data and GDPR

The architecture satisfies the applicable GDPR principles:

- **Lawfulness and transparency**: the legal basis is established by eIDAS 2.0 and by the sectoral educational rules.
- **Minimisation**: selective disclosure limits the data revealed to the specific purpose.
- **Purpose limitation**: the verifier can only process the attributes revealed.
- **Integrity and confidentiality**: JAdES-B-B and Data Integrity proofs guarantee integrity; the presentation channel (OID4VP) guarantees confidentiality.
- **Right to erasure**: although an issued credential cannot be "erased" retrospectively, revocation definitively invalidates its use. Expired credentials may be purged from the wallet's store if the person so decides.
- **Portability**: the VCDM format is open; the person can export their credentials to any conformant wallet.

## 6.10 Interoperability between wallets

Within the DC4EU framework, the interoperability of the EUDIW W3C-VC profile was validated between **four independent wallet implementations**:

- **Identify wallet** (Izertis, Spain).
- **UAegean wallet** (University of the Aegean, Greece).
- **Netcompany wallet** (Netcompany-Intrasoft, Luxembourg/Denmark).
- **Cappatrust wallet** (Cappatrust, Belgium).

Credentials issued by one implementer were received, stored and presented by the other three without modifications. Broader global wallet support for W3C-VCDM is documented at **https://canivc.com**, which tracks conformance across more than 50 implementations worldwide.

## 6.11 Outcome

The lifecycle and trust framework for an educational EAA over W3C-VCDM covers all identified regulatory and operational requirements:

1. Full lifecycle with native suspension and revocation (Article 24, Section 9 of Regulation 2024/1183).
2. Absence of "phone home" effect via `BitstringStatusList`.
3. Selective disclosure (salted-hash, SD-JWT) operative today; cryptographic unlinkability (BBS+) on the ETSI TS 119 312 incorporation pathway.
4. JAdES-B-B enveloping signatures for qualified EAAs, accepted by all EU governments.
5. Issuer identity with `eidasLegalIdentifier` and verifiable accreditation chain.
6. Hybrid PKI eIDAS ↔ dPKI EBSI trust framework.
7. Structural GDPR compliance.
8. Interoperable portability between wallet implementations.

---

**Next**: [07 — Sectoral EAA catalogue](./07-sectoral-eaa-catalogue.md)
