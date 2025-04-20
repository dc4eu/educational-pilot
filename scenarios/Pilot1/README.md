# Characterising the Classical PKI Scenario under eIDAS2

The classical **Public Key Infrastructure (PKI)** model underpins the trust framework of the European digital identity ecosystem. It is based on well-established cryptographic principles and a network of **trusted certification authorities**. In the context of **eIDAS2**, the model has been extended to accommodate new roles such as **EUDI Wallet holders**, **credential issuers**, **relying parties**, and **intermediaries**.

## 1. Certification Root Structures

### a. Trust Service Providers (TSPs) as Root Certification Authorities

Each Member State designates **qualified trust service providers (QTSPs)**, which issue:
- Qualified certificates for electronic seals (legal entities such as universities or ministries)
- Qualified certificates for website authentication
- Qualified certificates for electronic signatures (natural persons, including legal representatives)

These QTSPs operate under supervision and are listed in the **EU Trusted List Browser**, maintained by the **European Commission**.

### b. Two main PKI roots coexist
- **Issuers’ root CAs**: These anchor the identity of entities that issue **verifiable credentials** or **electronic attestations of attributes (EAAs)**. Examples: universities, ministries, accreditation agencies.
- **Relying parties’ root CAs**: These identify entities that **consume credentials** (e.g., employers, public authorities, recognition platforms), or act as **intermediaries** (e.g., gateways, digital campus services).

## 2. Roles and Their PKI Requirements

### a. Issuers
- Identified via a **qualified electronic seal certificate**
- Must appear in **national trusted lists** and possibly in **Commission-managed lists of credential types and issuer schemes**
- Their qualified certificate is used to prove origin and integrity of the credential
- Examples:
  - Ministry of Education issuing EQF credentials
  - University issuing EducationalID or MyAcademicID

### b. Relying Parties
- Identified via a **qualified certificate for website authentication** or **electronic seal**
- When requesting credentials from the EUDI Wallet, they must present:
  - Their identity
  - An attribute certificate authorising them to request specific data (e.g., PID, EAA)

### c. Relying Party Intermediaries
- Act on behalf of one or more relying parties (e.g., National Recognition Gateways, Erasmus platforms)
- Must be **formally recognised** by a Member State
- Present both a **qualified certificate** and an **electronic attribute certificate** indicating their intermediary role
- May be recorded in **Member State notifications** published by the Commission

### d. EUDI Wallet
- Held by the **natural person** (data subject / holder)
- Verifies the **authenticity and authorisation** of the **credential issuer** and the **relying party or intermediary**
- Interacts only with endpoints (issuers/verifiers) holding **valid, trusted qualified certificates**

## 3. Revocation and Status Checking Mechanisms

In the classical PKI model, certificate validity is guaranteed through **revocation infrastructure**:

### a. Certificate Revocation Lists (CRLs)
- Published by each certification authority
- Regularly updated and signed
- Must be checked by verifiers and wallet agents

### b. Online Certificate Status Protocol (OCSP)
- Real-time status verification of certificates
- Hosted by the QTSP or national trust infrastructure
- Used during wallet-verifier or wallet-issuer interactions

## 4. Notifications and Lists Supporting Trust

### a. National Trusted Lists (NTLs)
- Each Member State maintains a list of supervised trust service providers
- Published in a standardised format and aggregated at EU level

### b. EU Trusted List Browser
- Managed by the European Commission
- Aggregates all NTLs and exposes machine-readable trust services metadata
- Used by EUDI Wallet agents to build the trust chain

### c. Lists of Lists and Authorised Roles
- The Commission may maintain:
  - Lists of **approved credential schemes** (e.g., EQF, PID, ESC, ProfessionalID)
  - Lists of **authorised issuers** for specific credentials
  - Notifications of **relying party intermediaries** per Member State
- These are referenced in **Commission Implementing Acts** and necessary for **EUDI Wallet interoperability**

## 5. Limitations of the Classical PKI in Education Context (Summary)

- **No role-based authorisation**: A valid certificate does not prove the right to issue a specific credential
- **Static governance**: Cannot represent delegated authorisations (e.g., Ministry → University → Department)
- **Inflexibility in cross-border verification**: Verification requires agreement on a trusted set of CAs and mapping to roles

## 6. Characterisation of Classical PKI Usage in DC4EU – Pilot 1

In the context of **Pilot 1** of the DC4EU project, which focuses on implementing the **classical PKI trust model**, participating entities will operate using **qualified trust services**, following eIDAS2 and ARF specifications.

Each entity (issuer, verifier, intermediary) will be provided with:

### a. Qualified Certificates for Electronic Seals or Authentication
- Issued by a supervised QTSP in the respective Member State
- Used to sign verifiable credentials or authenticate endpoints

### b. Trusted Notification or Registration
- Each participating entity will be listed either:
  - In a **national trusted list**, or
  - In a **Member State notification** submitted to the European Commission

### c. (Optional) Attribute Certificates
- For relying parties and intermediaries, attribute certificates may be attached to confirm:
  - Their role (e.g. verifier, gateway, accreditation platform)
  - Their authorisation to request EAAs or PID from EUDI Wallet holders

### d. Wallet Interoperability Layer
- Entities will connect through EUDI Wallet APIs, and:
  - Validate certificates of issuers or verifiers
  - Use CRLs or OCSP for revocation checking
  - Present their own certificate chain to the holder’s wallet for trust verification

### e. Revocation and Status Monitoring
- All certificates used must support:
  - **OCSP endpoints** for real-time status checking
  - **CRLs** published by the QTSPs

This configuration ensures that **Pilot 1 entities** operate in a fully compliant and verifiable trust environment, even before dPKI is activated. It will also support progressive alignment with the decentralised trust model in Pilot 2.
