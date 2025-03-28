# eIDAS Scenarios in the European Digital Ecosystem

## Overview

The European Digital Ecosystem under the amended eIDAS Regulation (EU) 2024/1183 introduces a new trust framework for electronic attestation of attributes (EAAs), establishing four distinct scenarios based on the type of entity issuing the attestations. These scenarios reflect the regulatory and technical approaches to trust service provision, while integrating European Blockchain Services Infrastructure (EBSI) to enhance the reliability, automation, and transparency of the trust model.

The integration of EBSI with classical PKI (Public Key Infrastructure) models creates a hybrid trust framework that addresses limitations in traditional approaches while providing enhanced security, privacy, and cross-border interoperability for educational and professional qualifications.

## Scenario 1: EAAs issued within closed systems

This scenario describes electronic attestations of attributes (EAAs) issued in a closed system, meaning the issuers operate under contractual or administrative law frameworks, outside the European Digital Identity Wallet (EUDIW) trust model.

### Key characteristics

- **Trust model**: Classical PKI (Public Key Infrastructure), as the issuers operate independently of EUDIW.
- **Legal scope**: These EAAs do not need to comply with eIDAS regulatory obligations but may still benefit from the non-discrimination principle (Article 45b(1)), ensuring their legal admissibility in proceedings.
- **Limitations**: Closed systems lack interoperability and do not provide cross-border recognition under eIDAS.
- **Role of EBSI**: In this scenario, EBSI's added value is limited as there is no formal link to the broader EU ecosystem.

### Educational applications

In the educational context, this scenario might apply to internal university systems or proprietary corporate training platforms that issue credentials only within their closed ecosystem. These credentials lack portability and cross-border recognition but may still serve specific institutional purposes.

## Scenario 2: EAAs issued by non-qualified trust service providers (TSPs)

This scenario focuses on EAAs issued by entities that are not qualified under eIDAS but still operate as trust service providers (TSPs). These issuers can register as Wallet Relying Parties in the EUDIW ecosystem and issue attestations under an unregulated but recognised trust model.

### Trust Model Combination: Overcoming classical PKI limitations with EBSI

#### Classical PKI limitations

- No predefined supervision or validation process for TSPs.
- No automatic mechanism for verifying the authenticity or trustworthiness of the issuer.
- Relying parties cannot distinguish between issuers that are official sources and those that are simply marketing existing data.
- Lack of cross-border legal recognition unless governed by contract or specific regulations (e.g., Professional Qualifications Directive).

#### EBSI's added value

- Enables decentralised identity verification via DID methods to prove issuer authenticity.
- Improves trust automation by allowing relying parties to check on-chain credentials issued by trusted sources.
- Introduces Verifiable Credentials (VCs) and Zero-Knowledge Proofs (ZKPs) to improve privacy and selective disclosure.
- Provides a decentralised registry of TSPs, ensuring that issuers are discoverable, transparent, and accountable.

### Educational applications

This scenario is particularly relevant for:
- Private educational institutions issuing non-regulated certifications
- Professional development providers offering industry-recognised credentials
- MOOC platforms and online learning providers
- Educational technology companies offering skill assessments
- Non-governmental organisations providing learning opportunities

By implementing EBSI in this scenario, these organisations can enhance the credibility and verifiability of their credentials without needing to achieve qualified status under eIDAS.

## Scenario 3: EAAs issued by public sector bodies responsible for an authentic source (Pub_EAAs)

In this scenario, public sector bodies or their authorised entities issue electronic attestations of attributes that must meet strict trust and security requirements equivalent to qualified trust services.

### Key characteristics

- **Trust model**: Follows a regulated and structured PKI model, where issuers must comply with EUDIW protocols (ISO/IEC 18013-5, W3C VC Data Model).
- **Legal scope**: Pub_EAAs have the same legal effect as their paper-based equivalents and benefit from cross-border recognition (Article 45b(3)).
- **Role of EBSI**: Enhances automated trust processing through on-chain verification and cross-border attestation discovery, reinforcing authentic source verification.

### Educational applications

This scenario applies to:
- Public universities and educational institutions
- National education ministries
- Public accreditation bodies
- Governmental qualification authorities
- Public research institutions

These entities can issue credentials that hold the same legal weight as their traditional paper equivalents while gaining the advantages of digital verification and automated trust processing through EBSI integration.

## Scenario 4: EAAs issued by qualified trust service providers (QEAAs)

This scenario involves qualified trust service providers (QTSPs) that meet the highest level of trust under eIDAS. These entities issue qualified EAAs (QEAAs), ensuring full compliance with EUDIW protocols, interoperability, and legal recognition across EU Member States.

### Key characteristics

- **Trust model**: Classical strict PKI model, relying on qualified electronic signatures/seals and trusted lists maintained by national supervisory bodies.
- **Legal scope**: QEAAs benefit from legal equivalence and automatic cross-border recognition (Article 24a(9)).
- **Role of EBSI**: Enhances automation and verifiability by:
  - Recording qualified issuers in an immutable, decentralised ledger.
  - Providing immediate discoverability for verifiers and relying parties.
  - Supporting smart contracts for automated validation of EAAs.

### Educational applications

This scenario represents the highest level of trust for educational credentials and applies to:
- National qualification authorities requiring legal certainty
- Regulated professional qualifications with legal effects
- Professional licensing bodies with statutory authority
- Cross-border educational credentials requiring automatic recognition
- Credentials with significant legal or professional consequences

QEAAs in the educational context benefit from the combined strength of qualified trust services and EBSI's enhanced automation and verification capabilities.

## Integration with Sectorial EAA Catalogue

The EBSI scenarios provide the trust framework within which the Sectorial EAA Catalogue for Education and Professional Qualifications operates. Each credential type defined in the catalogue can be implemented within the appropriate EBSI scenario based on:

1. The legal status of the issuing institution
2. The regulatory requirements for the credential
3. The cross-border recognition needs
4. The privacy and selective disclosure requirements

For example:
- Formal degree credentials from public universities might be implemented as Pub_EAAs (Scenario 3)
- Professional certifications from industry bodies might be implemented as TSP EAAs with EBSI enhancements (Scenario 2)
- Regulated professional qualifications might be implemented as QEAAs (Scenario 4)
- Internal university micro-credentials might initially be implemented within closed systems (Scenario 1)

## Conclusion: The power of combining trust models

By integrating EBSI's decentralised PKI (dPKI) model with traditional classical PKI, the European digital ecosystem overcomes key limitations of classical PKI, including:

1. **Enhanced issuer trustworthiness**: EBSI enables DID-based identity verification to ensure that TSPs are authentic and accountable.
2. **Improved automation and discoverability**: The decentralised ledger provides on-chain evidence for EAAs, allowing automated processing and validation.
3. **Cross-border interoperability**: By linking decentralised identity with eIDAS-recognised trust services, EBSI ensures mutual recognition of EAAs beyond national frameworks.
4. **Privacy and security advancements**: With Verifiable Credentials (VCs) and Zero-Knowledge Proofs (ZKPs), EBSI provides selective disclosure, ensuring compliance with GDPR and eIDAS 2.0 privacy requirements.

The combination of classical PKI and decentralised PKI (dPKI) through EBSI creates a trust model that is robust, scalable, and fit for the evolving European Digital Identity framework, ensuring security, interoperability, and trust in electronic transactions across the EU.

## Implementation guidance

When implementing educational credentials within the Sectorial EAA Catalogue, organisations should:

1. **Identify the appropriate scenario** based on their legal status and the regulatory requirements for their credentials
2. **Implement the relevant trust model** (classical PKI, dPKI, or combined)
3. **Ensure compliance with the technical specifications** for their scenario
4. **Leverage EBSI capabilities** to enhance trust, automation, and cross-border recognition
5. **Align credential data models** with the Sectorial EAA Catalogue specifications

This approach ensures that educational credentials benefit from the appropriate level of trust, legal recognition, and technical interoperability across the European Digital Ecosystem.
