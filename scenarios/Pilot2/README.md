# Characterising the Decentralised PKI (dPKI) Scenario Using EBSI under eIDAS2

The decentralised **Public Key Infrastructure (dPKI)** model based on **EBSI** represents a significant evolution in the European digital identity framework. It complements the classical PKI trust model by enabling **self-sovereign identity (SSI)**, anchored on **W3C Verifiable Credentials (VC)** and **decentralised identifiers (DIDs)**. In the context of **eIDAS2**, this model enables dynamic trust relationships between credential issuers, EUDI Wallet holders, and relying parties, without a centralised certificate hierarchy.

This dPKI model does not replace the classical PKI; instead, it **complements it** by introducing **role-based authorisation capabilities** through **Electronic Attestations of Attributes (EAAs)** in the form of **W3C Verifiable Credentials**. This enables the deployment of **governance models already established in education and professional qualifications**, such as:
- Ministries accrediting universities or issuing mandates
- Agencies designating authorised issuing organisations
- Intermediaries operating on behalf of competent authorities

Through the use of DIDs and registry-linked metadata, it becomes possible to model and enforce **delegated authorisations**, with full traceability and legal accountability, across Member States.

## 1. Trust Anchoring via Decentralised Identifiers (DIDs)

### a. Legal Entities Registering DIDs
- Entities (e.g. universities, ministries, accreditation agencies) create DIDs via the **EBSI DID Registry**, under the **did:ebsi** method
- These DIDs represent the issuer's public key and service endpoints
- Identity proofs and authorisations are linked via **Verifiable Presentations (VPs)**

### b. Trust Anchoring Through TAOs and Registries
- The issuer's DID must be linked to:
  - A **Trusted Authorisation Organisation (TAO)**
  - A **Trusted Scheme Registry (TSR)** defining the legal framework
  - An **Issuer Registry (TIR)** and **Trusted Authorisation Registry (TAOR)**
- Trust is anchored through inclusion in these EBSI-managed or Member State-notified registries

## 2. Roles and Their dPKI Requirements

### a. Issuers
- Must register their DID in the **TIR** and define their **authorisation metadata** in the TAOR
- Credentials must reference:
  - **Credential type** (e.g. EQF degree, ESC, PID)
  - **Scheme ID** and **issuer authorisation**
- Examples:
  - A university issuing a diploma under the Higher Education Scheme
  - A chamber issuing a professional licence

### b. Relying Parties
- Must resolve the issuer's DID and verify:
  - The credential's signature
  - The scheme and role authorisation
  - The issuer's presence in the TIR/TAOR
- Can use decentralised trust verification libraries

### c. Relying Party Intermediaries
- May act on behalf of several verifiers (e.g. ENIC/NARIC platforms)
- Use their own DID and are referenced in TAOR with specific authorisation
- May present **delegated trust chains** (e.g. Ministry - Agency - Intermediary)

### d. EUDI Wallet
- Held by the **data subject (natural person)**
- Verifies issuer DIDs, credential integrity, and the validity of the trust chain
- Enables **selective disclosure** and **pairwise DID generation** for privacy-preserving interactions

## 3. Revocation and Status Checking in dPKI

### a. StatusList2021 Mechanism
- Issuers maintain a **StatusList2021** for revocation and suspension
- The status URL is referenced in the Verifiable Credential metadata

### b. Privacy-preserving Checks
- The EUDI Wallet requests revocation status through a **disintermediation proxy**, preserving holder anonymity
- No call from the verifier to the issuer is needed during presentation

## 4. Trust Registries and Notification Mechanisms

### a. EBSI Registries
- TIR (Trusted Issuer Registry)
- TSR (Trusted Scheme Registry)
- TAOR (Trusted Authorised Organisations Registry)
- TRPR (Trusted Relying Party Registry)
- **TASR (Trusted Authentic Source Registry)**
  - Enables Member States to register and publish **recognised authentic sources**
  - Allows third parties to verify the official status of an authentic source
  - Links authentic source entities with corresponding schemes and accreditation chains

### b. Member State Notifications
- Member States may notify trusted issuers, relying parties, and intermediaries
- Notifications are **digitally signed** and referenced in EBSI or Commission systems

## 5. Advantages of dPKI in Education and Professional Qualifications

- **Role-based trust**: The wallet validates not just the issuer identity, but their right to issue that credential
- **Delegation support**: Ministries can authorise institutions and sub-entities
- **Privacy-preserving**: No certificate chain is transmitted; verification is decentralised
- **Cross-border by design**: Trust is based on metadata and registry entries, not on shared CA hierarchies
- **Complementary to classical PKI**: Supports scenarios where dynamic authorisation, decentralised identifiers, and verifiable delegation are required

## 6. Characterisation of dPKI Usage in DC4EU' Pilot 2

In the context of **Pilot 2** of the DC4EU project, the decentralised PKI model will be tested across all participating domains:

### a. DID Registration and Credential Issuance
- Each issuer creates a DID under did:ebsi
- Credentials are issued as W3C VCs with EBSI-compatible metadata

### b. Registry-based Trust Establishment
- Issuer and role information is published in the TAOR, TIR, and TSR
- Authorisation to issue is validated by the verifier in real-time

### c. Wallet Interoperability and Trust Resolution
- Wallets verify DIDs and credential metadata without needing QTSP-issued certificates
- Relying parties validate the credential based on trust registries

### d. Revocation and Status Monitoring
- StatusList2021 used by all issuers
- Wallets and Relying parties query status via a privacy-preserving proxy

This model enables a fully **decentralised, role-aware, and privacy-respecting trust architecture**, aligned with eIDAS2 and supporting scalable cross-border recognition of educational and professional credentials
