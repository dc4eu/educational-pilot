# eIDAS Roles

## Introduction
The European Digital Identity Framework, established under **Regulation (EU) 2024/1183**, defines various roles related to electronic identification and trust services. These roles are essential for ensuring secure and reliable digital transactions across the European Union. This document provides an overview of key actors within the eIDAS framework, detailing their functions, the types of attestations they **issue** or **consume**, regulatory references, and the requirements to assume each role.

Relevant roles (issuance and verification perspective):
- Authentic Source
- Trust Service Provider
- Public Sector Body in Charge of an Authentic Source
- Qualified Trust Service Provider
- Relying Party
- Relying Party Intermediary

These roles form the backbone of the **European Digital Identity Framework**, ensuring that electronic identification and trust services remain **secure, interoperable, and legally recognised across the EU**. Each role carries specific responsibilities and compliance requirements, supporting the **digital transformation of public and private services**.


# eIDAS roles compliance matrix

This table summarises the compliance requirements for different roles under **Regulation (EU) 2024/1183** (eIDAS 2). Each "X" indicates that the role is required to meet the specified requirement.

| **Requirement** | **Authentic Source** | **Public Sector Body in Charge of an Authentic Source** | **Trust Service Provider (TSP)** | **Qualified Trust Service Provider (QTSP)** | **Relying Party** | **Relying Party Intermediary** |
|----------------|---------------------|---------------------------------------------------------|----------------------------------|---------------------------------------------|------------------|-----------------------------|
| Recognised under Union or national law | X | X |  |  |  |  |
| Ensures secure access and data integrity | X | X | X | X |  |  |
| Provides electronic attestations of attributes (EAA) | X | X | X | X |  |  |
| Compliance with Annex VII of Regulation (EU) 2024/1183 | X | X | X | X |  |  |
| Must allow verification by QTSPs | X | X |  |  |  |  |
| Must provide an interface for Digital Identity Wallets |  | X |  |  | X | X |
| Supervised by a national authority |  | X | X | X | X | X |
| Subject to regular security audits |  |  | X | X | X | X |
| Use of qualified electronic signatures or seals |  |  |  | X |  |  |
| Notifies authorities of security breaches within 24 hours |  |  |  | X |  |  |
| Must register and provide intended use cases |  |  |  |  | X | X |
| Must not request unauthorised data |  |  |  |  | X | X |
| Responsible for validating electronic attestations |  |  |  |  | X | X |
| Must respect pseudonyms when full identification is not required |  |  |  |  | X | X |
| Cannot store transaction content |  |  |  |  |  | X |
| Facilitates secure interactions between users and relying parties |  |  |  |  |  | X |


## Authentic Source

### Definition
An **Authentic Source** is a repository or system, maintained under the responsibility of a public sector body or a private entity, that contains and provides attributes about a natural or legal person or object. It is considered the **source of truth** for those attributes under Union or national law. It may be a primary or a secondary source, according to National law or administrative practice.

### Role
- Acts as a **trusted data source** for electronic attestations of attributes.
- Ensures the **accuracy, integrity, and legal validity** of the attributes it provides.
- Provides data that can be relied upon by **Trust Service Providers (TSPs)** for the issuance of qualified electronic attestations.

### Type of Attestation related to this role
- **Electronic attestation of attributes (EAA)**
- **Qualified electronic attestation of attributes (QEAA)** (if designated as such)

### Regulatory References
- **Regulation (EU) 2024/1183**, Article 3(47)
- **Annex VII** of Regulation (EU) 2024/1183

### Requirements
- Must be officially recognised as an authentic source under **Union or national law**.
- Must ensure **secure access mechanisms** to protect data integrity.
- Must allow designated entities (e.g., **Qualified Trust Service Providers**) to verify data electronically.

## Trust Service Provider (TSP)

### Definition
A **Trust Service Provider (TSP)** is an entity providing **electronic trust services**, such as issuing electronic certificates, electronic seals, timestamps, and electronic attestations of attributes.

### Role
- Provides **electronic trust services** that enhance security and trust in digital transactions.
- Ensures **compliance with eIDAS requirements** for electronic attestations and digital signatures.
- May offer **electronic identification services** based in qualified certificates for signatures or seals, complementing national identity schemes.

### Service Types
- **Electronic attestations of attributes (EAA)**
- **Certificates for electronic signatures and seals**
- **Electronic timestamps and electronic registered delivery services**
- **Electronic ledgers** 

### Regulatory References
- **Amended Regulation (EU) 2014/910**, Article 3(16)
- **Amended Regulation (EU) 2014/910**, Articles 45-49

### Requirements
- Must comply with **eIDAS technical and legal requirements** for trust services.
- Must undergo **regular security audits and conformity assessments**.
- Must ensure **secure and verifiable issuance of electronic attestations**.

## Public Sector Body in Charge of an Authentic Source

### Definition
A **Public Sector Body in Charge of an Authentic Source** is a governmental entity responsible for maintaining and ensuring the authority and integrity of an authentic source, or for issuing electronic attestations of attributes on behalf of such a source.

### Role
- Ensures that the authentic source **operates in compliance with regulatory requirements**.
- May directly issue **electronic attestations of attributes (EAA)** on behalf of the authentic source.
- Facilitates secure data exchange mechanisms with **relying parties** and **qualified trust service providers**.

### Service Types
- **Public Sector Body Electronic attestation of attributes (PubEAA)**
- **Qualified electronic attestation of attributes (QEAA)** (if authorised)

### Regulatory References
- **Amended Regulation (EU) 2014/910**, Article 3(46)
- **Annex VII** of Amended Regulation (EU) 2014/910

### Requirements
- Must be designated by a **Member State** as responsible for an **authentic source**.
- Must ensure **secure storage and transfer** of identity-related data.
- Must comply with **eIDAS-equivalent security and interoperability standards**.

## Qualified Trust Service Provider (QTSP)

### Definition
A **Qualified Trust Service Provider (QTSP)** is a trust service provider that meets **specific security and compliance requirements** under eIDAS and has been granted a "qualified" status by a **national supervisory authority**.

### Role
- Issues **qualified trust services**, including **qualified electronic attestations of attributes (QEAA)**.
- Provides **qualified electronic signatures, seals, timestamps, and archiving services**.
- Ensures the **highest level of reliability and trustworthiness** in digital transactions.

### Service types
- **Qualified electronic attestation of attributes (QEAA)**
- **Qualified electronic signatures and seals**
- **Qualified electronic timestamps and registered delivery services**

### Regulatory References
- **Amended Regulation (EU) 2014/910**, Article 3(45)
- **Annex V** and **Annex VII** of Amended Regulation (EU) 2014/910
- **Amended Regulation (EU) 2014/910**, Articles 45-49

### Requirements
- Must undergo **audits by an accredited conformity assessment body**.
- Must be **supervised by a national authority** designated under eIDAS.
- Must provide **enhanced security and transparency** in trust service operations.

## Relying Party

### Definition
A Relying Party is a natural or legal person that depends on electronic identification means, electronic attestations of attributes, or trust services to authenticate users or verify digital transactions.

### Role
- **Consumes electronic identification means and trust services for authentication and verification.**
- **Benefits from compliance with eIDAS trust service requirements.**
- **Uses qualified electronic attestations of attributes for verifying identity or entitlements.**

### Type of Attestation USED
- **Electronic attestation of attributes (EAA)**
- **Qualified electronic attestation of attributes (QEAA)**
- **Qualified electronic signatures and seals**

### Regulatory References
- **Amended Regulation (EU) 2014/910, Article 3(6)**
- **Amended Regulation (EU) 2014/910, Articles 45-49**

### Requirements
- **Must ensure proper verification mechanisms for relying on trust services.**
- **Must comply with eIDAS security and interoperability requirements.**
- **Must establish secure authentication workflows when handling digital identity attributes.**

## Relying Party Intermediary

### Definition
A Relying Party Intermediary is an entity that facilitates the interaction between a Relying Party and other eIDAS trust services, enabling the verification and processing of electronic identification means and electronic attestations of attributes.

### Role
- **Acts as a bridge between relying parties and trust services.**
- **Ensures secure and standardised communication of electronic attestations.**
- **May provide validation services for digital signatures, seals, or attributes.**

### Type of Attestation USED
- **Electronic attestation of attributes (EAA)**
- **Qualified electronic attestation of attributes (QEAA)**
- **Qualified electronic signatures and seals**

### Regulatory References
- **Regulation (EU) 2024/1183, Article 3(7)**
- **Regulation (EU) 2024/1183, Articles 45-49**

### Requirements
- **Must ensure compliance with eIDAS security and interoperability standards.**
- **Must facilitate trustworthy interactions between relying parties and trust service providers.**
- **Must be capable of verifying electronic attestations of attributes and signatures.**

