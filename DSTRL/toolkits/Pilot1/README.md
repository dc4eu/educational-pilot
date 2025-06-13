# DC4EU Pilot 1 – User Journeys under Classical PKI using SD-JWT-VC

This document provides a narrative description of the user journeys defined in DC4EU **Pilot 1**, based on the **Classical PKI trust model** and using the **SD-JWT-VC** credential format.

---

## Context Overview

### Trust Model: Classical PKI

Pilot 1 relies on a **hierarchical trust infrastructure** using:

* X.509 certificates
* eIDAS Trusted Lists
* CRL/OCSP for revocation

### Credential Format: SD-JWT-VC

A non-W3C credential type focusing on:

* Selective Disclosure
* Simple JSON claims
* JWT-like digital signatures

> **Be aware:** Unlike W3C Verifiable Credentials (VCDM), SD-JWT-VC does not support:
>
> * Linked data / semantic web compatibility
> * Ontologies (e.g. ELM, EQF, ESCO)
> * JSON-LD or RDF structures

This makes Pilot 1 ideal for **short-term adoption** and **basic cross-border workflows**, but less suited for long-term semantic interoperability.

---

## User Journey Narratives

### 1. Install Wallet

* User downloads and installs a wallet compatible with SD-JWT-VC.
* Wallet supports QR code scanning, passkey creation, and credential storage.
* Privacy-preserving: No server-side storage; user controls disclosure.

> Wallet parses flat JSON-based credentials, no need for JSON-LD context resolution.

---

### 2. Issue PID (Personal Identification Data)

* Trusted authority (e.g. national eID provider) issues PID in SD-JWT-VC format.
* Attributes include: name, birthdate, nationality, identifier.
* Credential is signed with X.509v3 certificate.
* Integrity and authenticity verified via Trusted List.

> PID acts as the foundational identifier within the pilot, compliant with eIDAS.

---

### 3. Issue Diploma

* University issues a diploma credential to the user.
* Credential includes degree title, awarding body, completion date.
* Signed using university's qualified certificate.
* Issuer's trust anchor must be published in national Trusted List.

<!--  > No support for EQF level, ECTS metadata, or semantic descriptors. -->

---

### 4. Issue Micro-credential

* User completes a short course; institution issues a Micro-credential.
* Credential includes: course name, date, provider.
* Issued and signed as SD-JWT-VC.

<!--  > Not linked to ELM or formal curriculum ontologies. Usable for human recognition. -->

---

### 5. Verify PID and Diploma

* Relying party requests to verify user's PID and diploma.
* User discloses selected attributes.
* Verifier uses issuer's certificate chain to validate signatures.
* Trust verified via eIDAS Trusted List.

<!--  > Selective disclosure ensures privacy; but verification logic lacks semantic processing. -->

---

### 6. Verify PID and Micro-credential

* Similar to previous flow.
* Relying party validates issuer and claims.
* Useful for admission, recognition, or upskilling scenarios.

> Semantic interpretation (e.g. ECTS recognition) must be handled manually.

---

## Format Comparison Table

| Feature                        | SD-JWT-VC (Pilot 1)  | W3C-VC (Pilot 2)           |
| ------------------------------ | -------------------- | -------------------------- |
| Trust Model                    | Classical PKI        | dPKI + Classical PKI       |
| Credential Format              | SD-JWT-VC            | W3C VCDM 1.1 / 2.0         |
| Selective Disclosure           | ✔                    | ✔                          |
| JSON-LD / Linked Data          | ❌                    | ✔                          |
| Ontology Support (ELM, EQF)    | ❌                    | ✔                          |
| Signature Model                | JWT-based            | BBS+, LD-Proof, etc.       |
| Semantics & Schema Referencing | Limited (none)       | Rich semantic capabilities |
| Use Case Fit                   | Fast onboarding, MVP | Long-term ecosystem fit    |

---

## Additional Resources

* [DC4EU GitHub Documentation](https://github.com/dc4eu)
* [SD-JWT-VC Specification (draft)](https://datatracker.ietf.org/doc/draft-ietf-oauth-selective-disclosure-jwt/)
* [Trusted List Browser](https://webgate.ec.europa.eu/tl-browser/#/)

---

## Summary

Pilot 1 enables a practical, lightweight implementation of user journeys with verifiable credentials under a Classical PKI infrastructure. It offers:

* **Legal assurance and privacy** via eIDAS-compliant trust chains.
* **Rapid onboarding** for educational and identity scenarios.

However, it is not suited for:

* **Complex data modelling** (e.g., curriculum alignment).
* **Interoperability with EBSI, Europass, or Linked Data frameworks.**

For such cases, transition to **W3C-VC-based Pilot 2** is recommended.
