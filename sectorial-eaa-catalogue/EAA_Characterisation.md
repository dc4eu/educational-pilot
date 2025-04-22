
# EAA Characterisation

## Characterisation of an Electronic Attestation of Attributes (EAA)

To build a coherent and conformance-ready **sectoral EAA catalogue**, each EAA must be described in a way that supports:

- Policy enforcement via decentralised authorisation
- Interoperability and discoverability through the Once-Only Technical System (OOTS)
- Wallet-side enforcement of disclosure constraints
- Runtime status checking (revocation and suspension)
- Compatibility with conformity assessments and trust registry validation

The following metadata fields must be included:

| Field                    | Purpose                                                                                         | Reference/Source              |
|--------------------------|-------------------------------------------------------------------------------------------------|--------------------------------|
| `eaa_id`                 | Unique identifier of the EAA (e.g. `EUHED`, `USC`, `EducationalID`)                                        | Sectoral catalogue            |
| `title`                  | Human-readable name of the EAA                                                                   | Sectoral definition           |
| `description`            | Semantic meaning and domain of application                                                       | National or EU-level authority|
| `data_model`             | Reference to JSON-LD schema or ELM-based structure                                          | ELM, W3C VCDM           |
| `credential_type`        | One of `VerifiableCredential`, `VerifiableAttestation`, or `QEAA`                                | eIDAS2 IA – Annex V           |
| `sectoral_scope`         | Domain of use (e.g. `FormalEducation`, `ProfessionalQualifications`)                            | Sectoral governance           |
| `issuable_by`            | Roles authorised to issue, mapped to TAOR and TIR                                                | TAOR, TSR, TIR                |
| `usable_by`              | Roles authorised to request, via VerifierAuthorisation VCs                                       | TSR, EBSI VC Framework        |
| `requires_pid`           | Whether the EAA is only valid when associated with a PID or QEAA                                 | DC4EU, Annex V                |
| `disclosure_policy`      | Embedded policy restricting which verifier roles may access this EAA                             | Embedded in TSR, wallet logic |
| `terms_of_reference_uri` | Link to JSON ToR stored in TSR specifying usage, presentation rules, and constraints             | TSR                           |
| `revocation_support`     | Method used to check revocation and suspension status                                            | StatusList2021, ARF v1.8.0    |
| `binding_requirements`   | Whether the credential must be cryptographically bound to the wallet holder                      | Annex VII – Security          |
| `expiry`                 | Static or dynamic expiry value                                                                   | Wallet-side enforcement       |
| `version`                | Version of the EAA characterisation entry                                                        | Sectoral catalogue            |

**Note:** `revocation_support` must include both revocation and suspension support where required.

``` mermaid
graph TD
  EAA["Electronic Attestation of Attributes (EAA)"]

  EAA --> ID["eaa_id"]
  EAA --> TITLE["title"]
  EAA --> DESC["description"]
  EAA --> CTYPE["credential_type"]
  EAA --> DMODEL["data_model\n(schema_uri, standard, profile)"]
  EAA --> SECTOR["sectoral_scope"]
  EAA --> ISSUEBY["issuable_by\n(authorised_roles, taor_required, tir_entry)"]
  EAA --> USEBY["usable_by\n(authorised_roles, entitlement_check)"]
  EAA --> REQPID["requires_pid"]
  EAA --> DPOL["disclosure_policy\n(machine_readable, verifier_role_check)"]
  EAA --> TOR["terms_of_reference_uri"]

  EAA --> REVOKE["revocation_support"]
  REVOKE --> R_METHOD["method"]
  REVOKE --> R_ENDPOINT["status_endpoint"]
  REVOKE --> R_SUSPEND["supports_suspension"]

  EAA --> BIND["binding_requirements\n(proof_of_possession, cryptographic_binding_to_holder)"]
  EAA --> EXP["expiry\n(type, valid_until)"]
  EAA --> VER["version"]
```
---

## Identity trust (via classical PKI)

eIDAS2 mandates the use of classical PKI mechanisms to validate the **legal identity** of both issuers and verifiers:

- **QWACs** for secure communication
- **QSealCs** for credential signing
- **EU Trusted Lists (LOTL)** for trust service discovery
- **CRLs and OCSP** for revocation checking

These mechanisms validate *who* an entity is, but **not whether it is authorised** to issue or request a specific EAA.

---

## Functional role trust (via dPKI and registries)

Authorisation is managed using decentralised trust registries:

| Registry | Purpose                                                                                              |
|----------|------------------------------------------------------------------------------------------------------|
| TIR      | Registers legal entities authorised to issue EAAs (linked to DID and QSealC)                         |
| TAOR     | Lists entities permitted to accredit others in a regulated domain                                    |
| TSR      | Maps each EAA to issuer/verifier roles, hosts Terms of Reference, and presentation policies          |

Issuers and verifiers must be explicitly registered and authorised in these registries.

---

## Relying party authorisation

Verifiers (relying parties) must:

1. Prove legal identity using a QWAC, QSealC or equivalent
2. Present a **VerifierAuthorisation VC** that includes:
   - `type`: `VerifierAuthorisation`
   - `permissions.type`: `RequestPolicy`
   - `input_descriptors` referencing the requested EAA type (e.g. `StudentID`)
   - Optional `limitRootTao` to constrain authority scope

This credential must be:
- Issued by an accredited TAO or delegated body
- Checked by the EUDI Wallet before any EAA disclosure

---

## Disclosure control

Each EAA defines both a **disclosure policy** (catalogue-level) and a **presentation policy** (runtime logic).

Presentation policies:
- Define the confidentiality level (`public`, `restricted`, `confidential`)
- Specify the required VCs a verifier must present
- Link verifier rights to EAA type access via `input_descriptors`
- Optionally restrict access to verifiers under a specific `limitRootTao`

These policies are enforced **exclusively by the wallet** during VP generation.

---

## Terms of Reference (ToR) enforcement

ToRs describe the semantic and operational usage of each EAA, including:

- Disclosure restrictions
- Required verifier credentials
- Permitted presentation contexts
- Binding and integrity constraints
- Links to a `presentation_policy_uri` for runtime enforcement

---

## Comparative enforcement table

| Trust Layer                 | Classical PKI                            | Decentralised PKI (dPKI)                           | EUDI Wallet Enforcement                                               |
|----------------------------|------------------------------------------|----------------------------------------------------|------------------------------------------------------------------------|
| Legal identity verification | Yes (via QWAC/QSealC + EU Trusted List) | Yes (via DID + TIR entry)                          | Must verify both PKI and dPKI where applicable                         |
| Functional role authorisation | No                                   | Yes (via TAOR/TSR + VerifierAuthorisation VC)      | Must validate VC and match EAA type via input_descriptors              |
| Credential issuance control | Partial (via QSealC)                    | Yes (TSR + ToR role validation)                    | Must ensure issuer is linked in TSR and ToR is enforced                |
| Selective disclosure        | No                                      | Yes (via disclosure and presentation policies)     | Mandatory: requires runtime policy enforcement and verifier proof      |
| Terms of reference (ToR)    | Not supported                           | Anchored and versioned in TSR                     | Must enforce ToR + referenced presentation policy                      |
| Revocation/suspension       | CRL, OCSP                               | StatusList2021 + on-chain event                   | Wallet checks real-time status including suspension                    |

---

## Three implementation guidelines

### 1. Governance of trusted issuance
- Only TAOR-accredited entities listed in the TIR may issue EAAs.
- Issuers must be linked to EAAs in the TSR and declare Terms of Reference and disclosure logic.

### 2. Sectoral disclosure control
- Each EAA must declare verifier role restrictions in a machine-readable policy.
- EUDI Wallets must validate both the verifier identity and their VerifierAuthorisation VC before VP generation.

### 3. Role-based access enforcement
- Relying parties must present a `VerifierAuthorisation` VC matching the `input_descriptor` of the requested EAA.
- Wallets must reject any presentation request lacking such a credential or when the verifier does not meet `limitRootTao`.

