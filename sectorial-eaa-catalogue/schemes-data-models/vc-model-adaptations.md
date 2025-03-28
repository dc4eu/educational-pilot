# Conversion Guideline: EDC to EBSI-Compliant Verifiable Credentials

## Introduction

The **European Digital Credential (EDC)** builder facilitates issuing digital credentials such as diplomas or certificates. To integrate these into the **European Blockchain Services Infrastructure (EBSI)**, additional adjustments are required. This ensures compatibility, enhances trust, and guarantees compliance with global **W3C Verifiable Credential standards**.

Converting EDC-generated credentials to EBSI-compliant Verifiable Credentials enhances trust, interoperability, and ensures future-readiness, aligning your institution or organisation with Europe's digital credentialing vision.

### Business Benefits
- **Interoperability:** Credentials validated across multiple European platforms.
- **Security and Trust:** Secure blockchain-based credential verification.
- **Standard Compliance:** Fully aligns with global W3C standards.

---

## Conversion Steps with Technical Examples

### Step 1: Remove top-level "credential" wrapper

| EDC-compliant                           | EBSI-compliant                |
| --------------------------------------- | ----------------------------- |
| `{ "credential": { ...data... }}`        | `{ ...data... }`              |

---

### Step 2: Add `@context` Element

| EDC-compliant                           | EBSI-compliant                                              |
| --------------------------------------- | ----------------------------------------------------------- |
| *(Not included)*                        | `"@context": ["https://www.w3.org/2018/credentials/v1", "https://example.ebsi.eu/credentials/v1"]` |

---

### Step 3: Add explicit Issuer Information (DID format)

| EDC-compliant                                | EBSI-compliant                                    |
| -------------------------------------------- | ------------------------------------------------- |
| `"issuer": {"id": "https://uni.edu"}`       | `"issuer": {"id": "did:ebsi:00001234abcd5678efgh9012"}` |

---

### Step 4: Insert EBSI Schema Entry

| EDC-compliant                   | EBSI-compliant                                                 |
| ------------------------------- | -------------------------------------------------------------- |
| *(No schema reference)*         | `"credentialSchema": {"id": "https://schema.ebsi.eu/education/diploma-v1", "type": "JsonSchemaValidator2018"}` |

---

### Step 5: Remove `deliveryDetails`

| EDC-compliant                                        | EBSI-compliant     |
| ---------------------------------------------------- | ------------------ |
| `"deliveryDetails": {"email": "user@example.com"}` | *(Removed)*        |

---

### Step 6: Modify `credentialSubject` ID to DID

| EDC-compliant                                        | EBSI-compliant                                          |
| ---------------------------------------------------- | ------------------------------------------------------- |
| `"credentialSubject": {"id": "student-id-1234"}`    | `"credentialSubject": {"id": "did:ebsi:0987abcd6543efgh"}` |

---

### Step 7: Confirm Issuer ID in DID format

| EDC-compliant                              | EBSI-compliant                                      |
| ------------------------------------------ | --------------------------------------------------- |
| `"issuer": {"id": "uni-5678"}`          | `"issuer": {"id": "did:ebsi:0000abcd1111efgh"}`   |

---

### Step 8: Add "VerifiableAttestation" Type

| EDC-compliant                           | EBSI-compliant                                        |
| --------------------------------------- | ----------------------------------------------------- |
| `"type": ["DiplomaCredential"]`        | `"type": ["VerifiableAttestation", "DiplomaCredential"]` |

---

## Technical Summary Table

| Element                    | Action   | EDC Example                                 | EBSI Example                                       |
| -------------------------- | -------- | ------------------------------------------- | -------------------------------------------------- |
| Top-level Wrapper          | Remove   | `{ "credential": { … }}`                    | `{ … }`                                            |
| `@context`                 | Add      | *(Not included)*                            | `"@context": ["https://www.w3.org/2018/credentials/v1", "https://example.ebsi.eu/credentials/v1"]` |
| Issuer ID                  | Modify   | `"issuer": {"id":"https://uni.edu"}`        | `"issuer": {"id":"did:ebsi:issuerdidexample"}` |
| Schema Reference           | Add      | *(Not included)*                            | `"credentialSchema": {"id":"https://schema.ebsi.eu/...","type":"JsonSchemaValidator2018"}` |
| `deliveryDetails`          | Remove   | `"deliveryDetails": {"email":"user@example.com"}` | *(Removed)*                                        |
| Subject ID                 | Modify   | `"credentialSubject":{"id":"student-id-1234"}` | `"credentialSubject":{"id":"did:ebsi:subjectdidexample"}` |
| `VerifiableAttestation`    | Add      | `"type":["DiplomaCredential"]`               | `"type":["VerifiableAttestation","DiplomaCredential"]` |


