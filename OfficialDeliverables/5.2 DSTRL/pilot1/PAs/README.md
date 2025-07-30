# DC4EU Pilot1 Scenarios

## Executive Summary

The five DC4EU Pilot1 scenarios demonstrate two distinct approaches to implementing classical PKI-based digital credential systems across Nordic, Dutch, and Finnish educational institutions. Whilst all scenarios achieved their core objective of credential issuance, they reveal significant implementation diversity and highlight limitations in the classical PKI trust model for cross-border verification capabilities.

## Pilot1 Piloting Agent Scenarios

This analysis covers the following five Pilot1 scenarios from educational institutions across Europe:

- **[Finnish National Agency for Education (OPH)](dc_4_eu_pilot_1_oph_scenario.md)** - PID and Educational Credential Issuance and Verification (Finnish National Solution - Classical PKI)
- **[Amsterdam University of Applied Sciences (AUAS)](dc_4_eu_pilot_1_auas_scenario.md)** - Educational Credential Issuance and Verification with SUNET/SURF SaaS (Classical PKI)
- **[Danmarks Tekniske Universitet (DTU)](dc_4_eu_pilot_1_dtu_scenario.md)** - Educational Credential Issuance and Verification with SUNET/SURF SaaS (Classical PKI)
- **[Ladok Consortium (Sweden)](dc_4_eu_pilot_1_ladok_scenario.md)** - Educational Credential Issuance and Verification with SUNET/SURF SaaS (Classical PKI)
- **[Sikt - Norwegian Agency for Shared Services in Education and Research](dc_4_eu_pilot_1_sikt_scenario.md)** - Educational Credential Issuance and Verification with SUNET/SURF SaaS (Classical PKI)

## Comparative Analysis

### Technical Implementation Consistency

The five scenarios demonstrate two distinct implementation approaches within the Classical PKI framework:

#### SUNET/SURF SaaS Solution (4 institutions)
Four scenarios employed standardised technical configurations through the SUNET/SURF platform:
- **Pilot option**: Classical PKI with SD-JWT credentials
- **SaaS environment**: SUNET/SURF test environment
- **Wallet**: wwWallet
- **Common issuer public key**: `MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEi3v64MrIKoS9Aofws9Dg3Vd7Ej9ZMBUYJ8DuHxb2mNDiRbrmJ6KqdIsrXWRfzguJUceYWZuo8Fx6RVP+E7Muvg==`
- **Participating institutions**: AUAS (Netherlands), DTU (Denmark), Ladok (Sweden), Sikt (Norway)

#### Finnish National Solution (1 institution)
The OPH scenario implemented a distinctive national approach:
- **Pilot option**: Classical PKI with SD-JWT credentials
- **National infrastructure**: Finnish DVV (Digital and Population Data Services Agency) issuance service
- **Wallet**: Finnish EUDI Wallet Demo (Android)
- **Issuer platform**: DVV Issuance Service with national sealing certificates
- **Authentic source integration**: Direct connection to KOSKI (vocational/secondary education) and VIRTA (higher education) registries
- **National authentication**: Suomi.fi e-Identification integration
- **Unique characteristics**: Manual certificate sealing, consent-based data retrieval with 24-hour expiration, comprehensive PID integration

This implementation diversity demonstrates the flexibility of the Classical PKI approach whilst highlighting different governance and infrastructure models within the European educational credential ecosystem.

### Credential Volumes and User Engagement

| Institution | Infrastructure | Users Onboarded | Credentials Issued | Verification Scope |
|-------------|----------------|------------------|-------------------|-------------------|
| **OPH (Finland)** | Finnish DVV National | 22 | 22 educational credentials + PIDs | 10 verified (DVV + DC4EU verifiers) |
| **AUAS (Netherlands)** | SUNET/SURF SaaS | 53 | 224 | 114 Integrity checks only |
| **DTU (Denmark)** | SUNET/SURF SaaS | 25 | 50 | Integrity checks only |
| **Ladok (Sweden)** | SUNET/SURF SaaS | 50 | 125 | 125 Integrity checks only |
| **Sikt (Norway)** | SUNET/SURF SaaS | 25 | 50 | Integrity checks only |

**Key distinctions:**
- **OPH**: Only institution with full PID integration and cross-verifier testing
- **OPH**: Direct authentic source integration (national education registries)
- **OPH**: National-scale infrastructure readiness demonstration
- **Others**: Standardised SaaS approach with shared technical infrastructure

**Total Impact**: 178 users, 571 credentials issued, demonstrating significant pilot scale.

## Implementation Model Analysis

### Finnish National Model (OPH)

The OPH scenario represents a **sovereign national implementation** with the following characteristics:

#### Technical Infrastructure
- **Issuer**: Digital and Population Data Services Agency (DVV) using national sealing certificates
- **Authentic sources**: Direct integration with KOSKI (secondary/vocational) and VIRTA (higher education) national registries
- **Governance**: Centralised national model with consent-based data transfer
- **Legal framework**: Act on National Registers of Education Records (884/2017) and Act on Information Management in Public Administration (906/2019)

#### Unique Capabilities
- **PID integration**: Full Personal Identification Data issuance and verification
- **Cross-verifier compatibility**: Successfully tested with both DVV national verifier and DC4EU verifier
- **Authentic source connectivity**: Real-time access to comprehensive national educational databases
- **Production readiness**: Demonstrated scalable national infrastructure

#### Implementation Challenges
- **Manual certificate sealing**: No automated PKI integration
- **Interoperability gaps**: Attribute naming mismatches with DC4EU standards (e.g., "givenName.und" vs "givenName")
- **Limited revocation**: No credential revocation or suspension capabilities implemented

### SUNET/SURF SaaS Model

The four-institution consortium demonstrates **federated SaaS implementation**:

#### Standardisation Benefits
- **Uniform technical stack**: Identical configurations across Nordic and Dutch institutions
- **Simplified deployment**: Centralised SaaS environment reduces institutional technical requirements
- **Cross-border consistency**: Shared issuer public key enables simplified trust relationships

#### Scalability Limitations
- **RP certificate absence**: Universal limitation preventing full cross-border verification
- **Limited authentic source integration**: Test environments without production data connectivity
- **Verification constraints**: Restricted to integrity checks rather than full trust chain validation

### Comparative Analysis

| Aspect | Finnish National (OPH) | SUNET/SURF Consortium |
|--------|------------------------|----------------------|
| **Infrastructure ownership** | National sovereign | Shared federated |
| **Authentic source integration** | Production-ready | Test environment |
| **PID capabilities** | Full integration | Not implemented |
| **Cross-verifier testing** | Successful | Limited to integrity |
| **Scalability model** | National deployment | Multi-institutional SaaS |
| **Governance complexity** | National legislation | Consortium agreements |

## Critical Technical Limitations

### Universal Verification Constraints

The most significant finding across all scenarios is the **absence of Relying Party (RP) certificates**, which prevented full cross-border verification testing.

### Implementation-Specific Limitations

#### Finnish National Model (OPH)
- **Standards alignment**: Credential structure differences requiring manual adjustments for DC4EU compatibility
- **Selective disclosure granularity**: Challenges with individual attribute selection in interconnected educational credentials
- **Certificate lifecycle**: Manual sealing process limiting automated trust chain validation
- **Revocation infrastructure**: Absence of credential revocation or suspension capabilities

#### SUNET/SURF Consortium Model
- **Relying Party infrastructure**: Universal absence of RP certificates preventing full verification testing
- **Authentic source connectivity**: Limited to test data without production registry integration
- **Trust chain validation**: Incomplete PKI infrastructure limiting cross-border verification scope
- **DNS resolution coordination**: Technical coordination challenges affecting SaaS instance accessibility

## Key Learnings and Implications

### Technical Feasibility

1. **Classical PKI Scalability**: Both models demonstrate technical feasibility at institutional and national scales
2. **Hybrid Trust Models**: The limitations revealed suggest need for complementary dPKI approaches (as noted in Pilot2)
3. **Standardised Schemas**: Critical need for harmonised credential schemas and attribute naming conventions
4. **Verification Infrastructure**: Enhanced cross-border verification capabilities beyond integrity checks

### Scaling Pathway

1. **Expand Verifier Network**: Integration with more diverse verification endpoints
2. **Production Readiness**: Transition from test environments to production-grade infrastructure
3. **Multi-Pilot Integration**: Coordination between Pilot1 and Pilot2 approaches for comprehensive trust framework

## Conclusions

The DC4EU Pilot1 scenarios reveal **two viable but distinct approaches** to classical PKI-based credential implementation within European higher education.

### Finnish National Model Success
The OPH implementation demonstrates that **sovereign national infrastructure** can successfully deliver production-ready digital credential services. Key achievements include:
- Full PID integration with educational credentials
- Real authentic source connectivity to national education registries
- Cross-verifier interoperability (with technical adjustments)
- Scalable national deployment model

### SUNET/SURF Consortium Coordination
The four-institution consortium proves that **federated SaaS approaches** can achieve technical standardisation across borders. Notable outcomes include:
- Uniform technical implementation across Nordic and Dutch institutions
- Simplified institutional deployment requirements
- Shared infrastructure reducing individual technical complexity

### Universal Technical Constraints
Both implementation models encountered **classical PKI limitations**:
- Absence of comprehensive Relying Party certificate infrastructure
- Limited cross-border trust chain validation capabilities
- Standards alignment challenges between national and European frameworks

### Strategic Implications
These findings suggest that **hybrid approaches** combining national sovereignty with European interoperability standards offer the most promising pathway for production deployment. The diversity of successful implementation models validates the flexibility required for pan-European digital credential adoption whilst highlighting critical standardisation requirements.

### Recommendations for Production Scaling
1. **Harmonise standards**: Align national credential schemas with European DC4EU frameworks
2. **Develop RP infrastructure**: Implement comprehensive Relying Party certificate provisioning
3. **Enable hybrid governance**: Support both national sovereign and federated consortium models
4. **Enhance interoperability**: Standardise attribute naming and selective disclosure mechanisms

---

*Analysis conducted on 30 July 2025 based on submitted DTSRL scenarios from participating Pilot1 institutions.*