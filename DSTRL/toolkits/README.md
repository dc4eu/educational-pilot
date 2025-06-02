# DC4EU Pilot Architecture Overview

The **DC4EU** project defines two distinct pilot tracks based on the **trust model** and the **verifiable credential format** adopted. Each pilot explores different technical and governance configurations aligned with European interoperability principles and the evolving digital identity ecosystem.

## Pilot 1 – Classical PKI with SD-JWT

**Pilot 1** relies on a trust model based exclusively on **Classical PKI** (Public Key Infrastructure). In this configuration:

- Credentials are issued and verified through hierarchical trust chains using established Certificate Authorities.
- The **credential format** follows the **SD-JWT** (Selective Disclosure JSON Web Token) specification.
- This approach is compatible with existing digital infrastructures and emphasises short-term interoperability.

[Access to Pilot1 technincal documentation](./Pilot1/)

## Pilot 2 – Combined PKI & Decentralised PKI with W3C VC

**Pilot 2** implements a **combined trust model**, where both **Classical PKI** and **Decentralised PKI** mechanisms coexist.

- Decentralised trust is supported via **trusted ledgers**, in particular the **European Blockchain Services Infrastructure (EBSI)**.
- Credentials are issued using the **W3C Verifiable Credentials (VC)** standard.
- This model supports long-term interoperability, alignment with the **eIDAS 2.0 Regulation**, and integration with the **EUDI Wallet** ecosystem.

[Access to Pilot2 technincal documentation](./Pilot2/README.md)

## Summary

| Pilot    | Trust Model                          | Credential Format      | Data Model Format| Infrastructure Reference          |
|----------|--------------------------------------|------------------------|------------------|-----------------------------------|
| Pilot1  | Classical PKI                        | SD-JWT                 | SD-JWT-VC        | Traditional CA-based trust chains, eIDAS 2.0, ARF |
| Pilot2  | Decentralised PKI + Classical PKI   | W3C Verifiable Credentials | W3C-VCDM 1.1 & W3C-VCDM 2.0 | Traditional CA-based trust chains, EBSI-ledger, eIDAS 2.0, ARF        |
| Pilot3  | The pilot agents who chose to pilot both options (Pilot 1 and Pilot 2)        |

Each pilot supports specific use cases and technological pathways that will inform future large-scale adoption across Member States in the fields of education and professional qualifications.

