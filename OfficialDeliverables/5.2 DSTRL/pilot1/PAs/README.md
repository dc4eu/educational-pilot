# Analysis of DC4EU Pilot1 Scenarios

## Executive Summary

The five DC4EU Pilot1 scenarios demonstrate a coordinated approach to implementing classical PKI-based digital credential systems across Nordic and Dutch educational institutions. Whilst all scenarios achieved their core objective of credential issuance, they reveal significant limitations in the classical PKI trust model for cross-border verification capabilities.

## Pilot1 Piloting Agent Scenarios

This analysis covers the following five Pilot1 scenarios from educational institutions across Europe:

- **[Finnish National Agency for Education (OPH)](dc_4_eu_pilot_1_oph_scenario.md)** - PID and Educational Credential Issuance and Verification (Finnish National Solution)
- **[Amsterdam University of Applied Sciences (AUAS)](dc_4_eu_pilot_1_auas_scenario.md)** - Educational Credential Issuance and Verification with SUNET/SURF SaaS (Classical PKI)
- **[Danmarks Tekniske Universitet (DTU)](dc_4_eu_pilot_1_dtu_scenario.md)** - Educational Credential Issuance and Verification with SUNET/SURF SaaS (Classical PKI)
- **[Ladok Consortium (Sweden)](dc_4_eu_pilot_1_ladok_scenario.md)** - Educational Credential Issuance and Verification with SUNET/SURF SaaS (Classical PKI)
- **[Sikt - Norwegian Agency for Shared Services in Education and Research](dc_4_eu_pilot_1_sikt_scenario.md)** - Educational Credential Issuance and Verification with SUNET/SURF SaaS (Classical PKI)

## Comparative Analysis

### Technical Implementation Consistency

All five scenarios employed identical technical configurations:
- **Pilot option**: Classical PKI with SD-JWT credentials
- **SaaS environment**: SUNET/SURF test environment (except OPH using Finnish DVV)
- **Wallet**: wwWallet (AUAS, DTU, Ladok, Sikt) or Finnish EUDI Wallet Demo (OPH)
- **Common issuer public key**: `MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEi3v64MrIKoS9Aofws9Dg3Vd7Ej9ZMBUYJ8DuHxb2mNDiRbrmJ6KqdIsrXWRfzguJUceYWZuo8Fx6RVP+E7Muvg==`

This standardisation demonstrates effective coordination by SURF/SUNET but also highlights the limited diversity in technical approaches tested.

### Credential Volumes and User Engagement

| Institution | Users Onboarded | Credentials Issued | Verification Scope |
|-------------|------------------|-------------------|-------------------|
| OPH (Finland) | 22 | 22 educational credentials | 10 successfully verified |
| AUAS (Netherlands) | 53 | 224 | 114 Integrity checks only |
| DTU (Denmark) | 25 | 50 | Integrity checks only |
| Ladok (Sweden) | 50 | 125 | 125 Integrity checks only |
| Sikt (Norway) | 25 | 50 | Integrity checks only |

**Total Impact**: 125 users, 371 credentials issued, demonstrating significant pilot scale.

## Critical Technical Limitations

### Universal Verification Constraints

The most significant finding across all scenarios is the **absence of Relying Party (RP) certificates**, which prevented full cross-border verification testing. This limitation manifested differently:

- **OPH**: Achieved partial verification (10 credentials) but noted "attribute-level interoperability gaps with DC4EU verifier"
- **SUNET/SURF scenarios**: Limited to "integrity checks only" rather than full trust chain validation

### Trust Infrastructure Gaps

The classical PKI model revealed fundamental limitations:
- **No dynamic governance layer**: PKI certificates confirm institutional identity but not authorisation to issue specific credential types
- **Absence of revocation mechanisms**: None of the scenarios implemented credential lifecycle management
- **Manual sealing processes**: OPH noted reliance on manually created certificates without integration to national trust lists

## Regulatory and Operational Findings

### GDPR Compliance Success

All scenarios successfully demonstrated GDPR-compliant consent-based data transfers, indicating robust privacy frameworks.

### Infrastructure Readiness Variations

- **Finland (OPH)**: Most advanced with national DVV infrastructure and integration with KOSKI/VIRTA databases
- **Other scenarios**: Relied on remote SaaS without institutional system integration

## User Experience Assessment

### Positive Reception

All scenarios reported positive user feedback regarding:
- Wallet installation simplicity
- Credential reception processes
- Overall user experience

### Common Challenges

Users consistently reported confusion around:
- Multiple consent steps (particularly noted by OPH)
- Understanding data visibility and credential verification processes

## Strategic Recommendations

### Immediate Actions Required

1. **RP Certificate Provisioning**: Priority implementation of Relying Party certificates for cross-border verification testing
2. **Trust List Integration**: Development of automated trust list validation mechanisms
3. **Credential Lifecycle Implementation**: Addition of revocation and suspension capabilities

### Architectural Considerations

1. **Hybrid Trust Models**: The limitations revealed suggest need for complementary dPKI approaches (as noted in Pilot2)
2. **Standardised Schemas**: Critical need for harmonised credential schemas and attribute naming conventions
3. **Verification Infrastructure**: Enhanced cross-border verification capabilities beyond integrity checks

### Scaling Pathway

1. **Expand Verifier Network**: Integration with more diverse verification endpoints
2. **Production Readiness**: Transition from test environments to production-grade infrastructure
3. **Multi-Pilot Integration**: Coordination between Pilot1 and Pilot2 approaches for comprehensive trust framework

## Conclusions

The DC4EU Pilot1 scenarios successfully demonstrate the feasibility of classical PKI-based credential issuance at scale across multiple European educational institutions. However, they clearly illustrate the inherent limitations of classical PKI for the granular governance requirements of educational credential ecosystems.

The consistent technical implementation across scenarios provides valuable baseline data, whilst the universal verification limitations underscore the necessity for enhanced trust infrastructure development. The positive user reception validates the user experience design, but the technical constraints confirm the need for hybrid trust models combining classical and decentralised PKI approaches.

These findings provide essential evidence for the evolution towards more sophisticated trust frameworks capable of supporting the full European Digital Education Area vision.

---

*Analysis conducted on 1 July 2025 based on submitted DTSRL scenarios from participating Pilot1 institutions.*
