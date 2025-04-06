
# Joint Degree Credential – EBSI Compliant Example

This document presents a **Joint Degree** credential converted into a Verifiable Credential (VC) compliant with the **European Blockchain Services Infrastructure (EBSI)**. It includes:

- A compliant VC (unsigned)
- A signed version of the VC (simulated)
- A Mermaid class diagram with cardinality
- Download links for all artefacts

---

## 1. Converted Credential (Unsigned)

The following VC adheres to EBSI specifications and includes standard fields for a jointly awarded degree qualification.

**Download**: [VC Unsigned](./JointDegree-EBSI-VC-unsigned.json)

---

## 2. Signed Credential (Simulated)

Includes a simulated `proof` block using the `Ed25519Signature2018` type for illustrative purposes.

**Download**: [VC Signed](./JointDegree-EBSI-VC-signed.json)

---

## 3. Class Diagram (Mermaid with Cardinality)

This diagram models the structure of a joint degree credential and its key components.

**Download**: [Mermaid Diagram](./JointDegree-mermaid-diagram.md)


```mermaid
classDiagram
  class VerifiableCredential {
    +@context: list [1..*]
    +id: string [1]
    +type: list [1..*]
    +issuer: object [1]
    +issuanceDate: date [1]
    +issued: date [1]
    +validFrom: date [0..1]
    +validUntil: date [0..1]
    +expirationDate: date [0..1]
    +credentialSubject: CredentialSubject [1]
    +credentialSchema: CredentialSchema [1]
    +credentialStatus: object [0..1]
    +proof: object [0..1]
  }

  class CredentialSubject {
    +id: string [1]
    +type: string [1]
    +givenName: string [1]
    +familyName: string [1]
    +dateOfBirth: string [1]
    +hasCredential: JointDegreeCredential [1]
  }

  class JointDegreeCredential {
    +title: string [1]
    +description: string [0..1]
    +educationalLevel: string [1]
    +eqfLevel: string [0..1]
    +awardingOpportunity: object [0..1]
    +awardedBy: list [1..*]
    +learningAchievement: object [1]
  }

  class CredentialSchema {
    +id: string [1]
    +type: string [1]
  }

  VerifiableCredential --> CredentialSubject
  CredentialSubject --> JointDegreeCredential
  VerifiableCredential --> CredentialSchema
```


---

## 4. EBSI Compliance Overview

- The holder is identified by a DID (`did:key:...`)
- Context includes W3C, example VC and schema URI
- A revocation mechanism is declared using `credentialStatus`
- The awarding organisations are listed in `awardedBy`
- `proof` is illustrative and not cryptographically valid

---

## 5. References

- [EBSI Trusted Schema Registry](https://api-pilot.ebsi.eu/trusted-schemas-registry/)
- [W3C Verifiable Credentials Data Model](https://www.w3.org/TR/vc-data-model/)
- [DC4EU Blueprint Guide](https://www.dc4eu.eu/)
