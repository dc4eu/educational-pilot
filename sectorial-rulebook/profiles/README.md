# DC4EU Technical Profiles Comparison Matrix: Pilot1 vs Pilot2

## Executive Summary

This matrix provides a comprehensive comparison of the technical aspects between Pilot1 (Classical PKI with SD-JWT) and Pilot2 (Hybrid PKI with W3C VC) within the DC4EU project framework for education and professional qualifications.

---

## **1. TRUST MODEL ARCHITECTURE**

| **Aspect** | **Pilot1 (Classical PKI)** | **Pilot2 (Hybrid PKI)** |
|:-----------|:---------------------------|:------------------------|
| **Core Trust Model** | Classical PKI exclusively | Combined Classical PKI + Decentralised PKI (dPKI) |
| **Trust Anchors** | Certificate Authorities (CAs) | CAs + EBSI (European Blockchain Services Infrastructure) |
| **Trust Validation** | Hierarchical certificate chains | Dual-layer: X.509 certificates + EBSI trust registries |
| **Trust Registries** | Traditional CA-based trusted lists | EBSI Trust Registry + Schema Registry + DID Registry |
| **Authority Model** | Certificate Authority hierarchy | Trust Authority Organisations (TAOs) + CA hierarchy |
| **Decentralisation Level** | Centralised | Hybrid centralised-decentralised |

---

## **2. CREDENTIAL FORMAT & STRUCTURE**

| **Aspect** | **Pilot1 (Classical PKI)** | **Pilot2 (Hybrid PKI)** |
|:-----------|:---------------------------|:------------------------|
| **Credential Format** | SD-JWT (Selective Disclosure JWT) - **DRAFT STANDARD** | W3C Verifiable Credentials (VC) - **ESTABLISHED STANDARD** |
| **Data Model** | SD-JWT-VC - **PENDING STANDARDISATION** | W3C-VCDM 1.1 & W3C-VCDM 2.0 - **6+ YEARS PROVEN** |
| **Schema Standard** | JSON Schema with SD-JWT extensions - **EVOLVING** | W3C VC Data Model + European Learning Model (ELM) - **MATURE** |
| **Selective Disclosure** | Built-in with SD-JWT hashing - **DRAFT SPECIFICATION** | Supported through W3C VC features - **TESTED IMPLEMENTATIONS** |
| **Credential Structure** | JWT with `_sd` arrays for privacy - **EXPERIMENTAL** | JSON-LD with cryptographic proofs - **PRODUCTION-READY** |
| **Privacy Mechanism** | Hash-based selective disclosure - **UNPROVEN AT SCALE** | Multiple methods (BBS+, zero-knowledge proofs) - **BATTLE-TESTED** |

---

## **3. CRYPTOGRAPHIC SPECIFICATIONS**

| **Aspect** | **Pilot1 (Classical PKI)** | **Pilot2 (Hybrid PKI)** |
|:-----------|:---------------------------|:------------------------|
| **Signature Algorithms** | ES256, ES384, ES512, RS256, RS384, RS512 | ES256, ES384, ES512, EdDSA, BBS+ |
| **Key Types** | EC (P-256, P-384, P-521), RSA (min 2048-bit) | EC (P-256, P-384, P-521), Ed25519, RSA |
| **Hash Functions** | SHA-256 or stronger | SHA-256, SHA-384, SHA-512 |
| **Signature Format** | JWS (JSON Web Signature) | JWS, JAdES, Linked Data Signatures |
| **Key Management** | X.509 certificate-based | X.509 + DID-based key management |
| **Cryptographic Binding** | Certificate chain validation | Certificate + DID binding (x5t#S256) |

---

## **4. IDENTITY & AUTHENTICATION**

| **Aspect** | **Pilot1 (Classical PKI)** | **Pilot2 (Hybrid PKI)** |
|:-----------|:---------------------------|:------------------------|
| **Identity Model** | X.509 certificates only | X.509 certificates + Decentralised Identifiers (DIDs) |
| **Issuer Identity** | Distinguished Name (DN) in certificates | DN + DID (did:ebsi:) |
| **Authentication Method** | Certificate-based authentication | Dual: Certificate + DID-based authentication |
| **Identity Resolution** | CA directory services | DID resolution + CA services |
| **Global Uniqueness** | Certificate serial numbers | DID + certificate binding |
| **Self-Sovereign Identity** | Not supported | Supported through DID infrastructure |

---

## **5. INFRASTRUCTURE REQUIREMENTS**

| **Aspect** | **Pilot1 (Classical PKI)** | **Pilot2 (Hybrid PKI)** |
|:-----------|:---------------------------|:------------------------|
| **Core Infrastructure** | Traditional CA infrastructure | CA infrastructure + EBSI blockchain |
| **Registry Services** | Certificate revocation lists (CRLs), OCSP | CRL/OCSP + EBSI registries (DID, Trust, Schema) |
| **Blockchain Integration** | Not required | EBSI blockchain integration required |
| **Distributed Ledger** | Not applicable | EBSI-based distributed ledger |
| **Node Requirements** | CA connectivity | CA connectivity + EBSI node access |
| **Scalability Model** | Traditional PKI scalability | Hybrid scalability (PKI + blockchain) |

---

## **6. REGULATORY COMPLIANCE**

| **Aspect** | **Pilot1 (Classical PKI)** | **Pilot2 (Hybrid PKI)** |
|:-----------|:---------------------------|:------------------------|
| **eIDAS Compliance** | eIDAS 1.0 & 2.0 compliant | eIDAS 2.0 compliant with enhanced features |
| **GDPR Compliance** | Data minimisation through SD-JWT | Enhanced privacy through W3C VC + zero-knowledge |
| **European Standards** | ETSI standards compliance | ETSI + W3C standards compliance |
| **Cross-border Recognition** | Through traditional mutual recognition | Enhanced through EBSI trust registries |
| **Regulatory Framework** | Classical digital signature regulations | Extended digital identity regulations |
| **Legal Effect** | Non-discrimination principle (Article 45b) | Non-discrimination + enhanced trust (EBSI) |

---

## **7. ONBOARDING PROCESSES**

| **Aspect** | **Pilot1 (Classical PKI)** | **Pilot2 (Hybrid PKI)** |
|:-----------|:---------------------------|:------------------------|
| **Issuer Onboarding** | CA registration + certificate issuance | CA registration + DID creation + EBSI registration |
| **Verifier Onboarding** | Relying party certificates | WRPAC + DID registration + EBSI authorisation |
| **Registration Authority** | Certificate Authorities | CAs + EBSI Trust Registry |
| **Capability Declaration** | Certificate extensions | DID Document + EBSI Trust Registry entries |
| **Authorisation Model** | Certificate-based authorisation | Verifiable credentials for authorisation |
| **Governance Integration** | National educational databases | National databases + EBSI trust registries |

---

## **8. VERIFICATION MECHANISMS**

| **Aspect** | **Pilot1 (Classical PKI)** | **Pilot2 (Hybrid PKI)** |
|:-----------|:---------------------------|:------------------------|
| **Verification Process** | Certificate chain validation + SD-JWT integrity | Certificate validation + DID resolution + EBSI trust check |
| **Trust Validation** | CA trust chain | Multi-layer: CA chain + EBSI trust registry |
| **Revocation Checking** | CRL/OCSP | CRL/OCSP + EBSI status registry |
| **Real-time Validation** | OCSP | OCSP + EBSI real-time queries |
| **Cross-border Verification** | Mutual recognition agreements | EBSI-facilitated automatic recognition |
| **Verification Complexity** | Moderate (single trust path) | Higher (dual trust path validation) |

---

## **9. CREDENTIAL LIFECYCLE**

| **Aspect** | **Pilot1 (Classical PKI)** | **Pilot2 (Hybrid PKI)** |
|:-----------|:---------------------------|:------------------------|
| **Issuance** | SD-JWT creation + signature | W3C VC creation + cryptographic proof |
| **Storage** | EUDIW with SD-JWT format | EUDIW with W3C VC format |
| **Presentation** | Selective disclosure of SD-JWT claims | W3C VC presentation with selective disclosure |
| **Revocation** | Certificate revocation lists | CRL + EBSI status registry |
| **Suspension** | Not directly supported | Supported through EBSI registry |
| **Renewal** | Certificate renewal process | Certificate + DID key rotation |
| **Lifecycle Management** | Traditional PKI lifecycle | Enhanced with blockchain immutability |

---

## **10. INTEROPERABILITY**

| **Aspect** | **Pilot1 (Classical PKI)** | **Pilot2 (Hybrid PKI)** |
|:-----------|:---------------------------|:------------------------|
| **Standards Compliance** | SD-JWT specification - **DRAFT/EXPERIMENTAL** | W3C VC + DID specifications - **W3C RECOMMENDATIONS** |
| **Wallet Compatibility** | EUDIW with SD-JWT support - **EARLY ADOPTION** | EUDIW with W3C VC support - **MATURE ECOSYSTEM** |
| **Cross-pilot Compatibility** | Limited (format differences) - **INTEROP CHALLENGES** | Enhanced (W3C VC standard) - **PROVEN INTEROPERABILITY** |
| **International Standards** | JWT-based standards - **EMERGING** | W3C global standards - **WIDELY ADOPTED** |
| **Legacy System Integration** | Easier (JWT familiarity) - **THEORETICAL** | More complex (new W3C standards) - **PROVEN PATTERNS** |
| **Future-proofing** | Medium (JWT evolution) - **UNCERTAIN EVOLUTION** | High (W3C standardisation) - **STABLE EVOLUTION PATH** |

---

## **11. IMPLEMENTATION COMPLEXITY**

| **Aspect** | **Pilot1 (Classical PKI)** | **Pilot2 (Hybrid PKI)** |
|:-----------|:---------------------------|:------------------------|
| **Technical Complexity** | Low to Medium - **BUT BLEEDING-EDGE STANDARDS** | High - **BUT MATURE TECHNOLOGY STACK** |
| **Implementation Time** | Shorter (familiar PKI) - **OFFSET BY SPEC UNCERTAINTY** | Longer (new technologies) - **PREDICTABLE WITH PROVEN TOOLS** |
| **Developer Learning Curve** | Moderate - **PLUS EXPERIMENTAL SPEC LEARNING** | Steep - **BUT COMPREHENSIVE DOCUMENTATION** |
| **Infrastructure Investment** | Lower - **PLUS RISK OF REWORK** | Higher - **BUT STABLE INVESTMENT** |
| **Operational Complexity** | Familiar PKI operations - **PLUS DRAFT SPEC HANDLING** | New DID + blockchain operations - **WELL-DOCUMENTED PATTERNS** |
| **Maintenance Overhead** | Standard PKI maintenance - **PLUS SPEC EVOLUTION TRACKING** | PKI + blockchain maintenance - **ESTABLISHED BEST PRACTICES** |

---

## **12. PERFORMANCE CHARACTERISTICS**

| **Aspect** | **Pilot1 (Classical PKI)** | **Pilot2 (Hybrid PKI)** |
|:-----------|:---------------------------|:------------------------|
| **Verification Speed** | Fast (traditional PKI) | Moderate (multiple registry queries) |
| **Scalability** | High (proven PKI scalability) | Medium (blockchain limitations) |
| **Network Dependency** | Moderate (CRL/OCSP) | High (EBSI connectivity required) |
| **Offline Capabilities** | Limited | Enhanced (DID caching) |
| **Resource Requirements** | Low to Medium | Medium to High |
| **Throughput** | High | Medium |

---

## **13. SECURITY CONSIDERATIONS**

| **Aspect** | **Pilot1 (Classical PKI)** | **Pilot2 (Hybrid PKI)** |
|:-----------|:---------------------------|:------------------------|
| **Attack Vectors** | Traditional PKI attacks | PKI + blockchain attacks |
| **Single Point of Failure** | CA compromise | Distributed (reduced risk) |
| **Quantum Resistance** | Depends on algorithms | Enhanced (crypto-agility) |
| **Privacy Protection** | SD-JWT selective disclosure | Enhanced W3C VC privacy |
| **Audit Trail** | Certificate logs | Certificate logs + blockchain |
| **Compromise Recovery** | Certificate revocation | Certificate + DID key rotation |

---

## **14. USE CASE ALIGNMENT**

| **Aspect** | **Pilot1 (Classical PKI)** | **Pilot2 (Hybrid PKI)** |
|:-----------|:---------------------------|:------------------------|
| **Educational Credentials** | Optimised for traditional diplomas | Enhanced for comprehensive qualifications |
| **Professional Qualifications** | Standard certification support | Advanced competency mapping |
| **Micro-credentials** | Basic support | Enhanced granular credentials |
| **Cross-border Mobility** | Limited automatic recognition | Enhanced EBSI-facilitated recognition |
| **Industry Integration** | Traditional sector alignment | Innovation-focused sectors |
| **Government Services** | Standard public sector | Enhanced public sector innovation |

---

## **15. EAA SCENARIO ALIGNMENT**

| **Aspect** | **Pilot1 (Classical PKI)** | **Pilot2 (Hybrid PKI)** |
|:-----------|:---------------------------|:------------------------|
| **Optimal EAA Scenarios** | **PubEAA + QEAA** (Scenarios 3 & 4) | **Non-qualified EAA** (Scenario 2) |
| **PubEAA Suitability** | **HIGH** - Classical PKI aligns with public sector authentic source requirements | **MEDIUM** - Can complement but not primary focus |
| **QEAA Suitability** | **HIGH** - Natural fit for qualified trust service provider infrastructure | **MEDIUM** - Can complement but adds complexity |
| **Non-qualified EAA Suitability** | **LOW** - Limited trust mechanisms for non-qualified scenarios | **HIGH** - EBSI provides crucial trust enhancement |
| **Regulatory Alignment** | **Strong** for qualified/public scenarios with established trust chains | **Strong** for non-qualified scenarios requiring enhanced trust |
| **Trust Model Fit** | **Perfect** for scenarios with formal regulatory oversight | **Perfect** for scenarios needing automated trust processing |

---

## **16. SCENARIO-SPECIFIC TECHNICAL REQUIREMENTS**

| **Aspect** | **Pilot1 (Classical PKI)** | **Pilot2 (Hybrid PKI)** |
|:-----------|:---------------------------|:------------------------|
| **PubEAA Requirements** | ✅ Qualified electronic signature/seal support | ✅ Qualified signature + DID binding |
| **QEAA Requirements** | ✅ QTSP infrastructure alignment | ✅ QTSP + EBSI registration |
| **Non-qualified EAA Gap** | ❌ **Limited automated trust processing** | ✅ **EBSI-enhanced trust mechanisms** |
| **Authentic Source Integration** | ✅ Natural fit with public sector PKI | ✅ Enhanced with verifiable accreditation |
| **Cross-border Recognition** | ✅ Established mutual recognition (PubEAA/QEAA) | ✅ EBSI-facilitated recognition (all scenarios) |
| **Automated Trust Processing** | ❌ **"Trust model falls short"** for non-qualified | ✅ **"EBSI provides major business value"** |

---

## **16. COST IMPLICATIONS**

| **Aspect** | **Pilot1 (Classical PKI)** | **Pilot2 (Hybrid PKI)** |
|:-----------|:---------------------------|:------------------------|
| **Initial Investment** | Lower **for PubEAA/QEAA scenarios** | Higher **but optimal for non-qualified EAA** |
| **Operational Costs** | Standard PKI costs **for regulated scenarios** | PKI + blockchain costs **with enhanced trust value** |
| **Training Costs** | Moderate **for familiar PKI** | High **but mature W3C standards** |
| **Maintenance Costs** | Standard **for traditional trust chains** | Enhanced **with automated trust processing** |
| **Scaling Costs** | Linear **for regulated scenarios** | Non-linear **but addresses trust gaps** |
| **ROI Timeline** | Shorter **for PubEAA/QEAA** | Longer **but essential for non-qualified scenarios** |

---

## **17. STRATEGIC CONSIDERATIONS**

| **Aspect** | **Pilot1 (Classical PKI)** | **Pilot2 (Hybrid PKI)** |
|:-----------|:---------------------------|:------------------------|
| **Market Readiness** | High **for public sector/qualified** - **LOW for non-qualified** (draft standards) | Medium **for all scenarios** - **HIGH for non-qualified** (6+ years W3C VC) |
| **Innovation Potential** | Limited **- HIGH SPEC RISK** | High **- PROVEN INNOVATION for non-qualified trust** |
| **Competitive Advantage** | Strong **for PubEAA/QEAA** - **UNDERMINED BY SPEC UNCERTAINTY** | Innovation **- BACKED BY MATURE STANDARDS** |
| **Risk Profile** | Low **for regulated scenarios** - **INCREASED BY DRAFT STANDARDS** | Medium **- MITIGATED BY PROVEN TECHNOLOGY** |
| **Strategic Alignment** | Conservative **for traditional sectors** - **ACTUALLY EXPERIMENTAL** | Innovation **for emerging non-qualified scenarios** - **BASED ON PROVEN FOUNDATIONS** |
| **Future Evolution** | Proven **for qualified scenarios** - **UNCERTAIN PATH for non-qualified** | Transformative **- CLEAR ROADMAP for all scenarios** |

---

## **RECOMMENDATIONS**

### **Choose Pilot1 (Classical PKI) when:**
- **PubEAA or QEAA scenarios** are your primary focus
- **Public sector authentic source** or **qualified trust service provider** context
- **Regulated educational credentials** with established legal frameworks
- **Traditional institutional hierarchy** and formal oversight structures
- **Mature PKI infrastructure** already in place
- **Cross-border recognition** through established mutual recognition agreements

### **Choose Pilot2 (Hybrid PKI) when:**
- **Non-qualified EAA scenarios** are your primary focus
- **Enhanced automated trust processing** is essential
- **Innovation in credential verification** without full regulatory oversight
- **EBSI-enhanced trust mechanisms** are needed to fill trust gaps
- **Diverse issuer ecosystem** including non-traditional credential providers
- **Future-proofing** with mature W3C standards (6+ years proven)

### **Key Scenario Alignment:**
- **Pilot1**: Optimised for **PubEAA (Scenario 3)** and **QEAA (Scenario 4)**
- **Pilot2**: Essential for **Non-qualified EAA (Scenario 2)** where "EBSI provides major business value"

---

## **CRITICAL REALIZATION**

**The scenario-based analysis reveals the true strategic positioning:**

### **Pilot1 (Classical PKI)**:
- **STRONG** for traditional regulated scenarios (PubEAA/QEAA)
- **WEAK** for non-qualified scenarios where "trust model falls short"
- **RISK** from draft SD-JWT specifications in all scenarios

### **Pilot2 (Hybrid PKI)**:
- **ESSENTIAL** for non-qualified scenarios requiring automated trust processing
- **COMPLEMENTARY** for PubEAA/QEAA scenarios with enhanced capabilities
- **STABLE** foundation with mature W3C standards across all scenarios

### **Strategic Insight:**
The choice is not just about technical architecture but about **regulatory scenario alignment**. Pilot1 serves the traditional qualified/public sector well but struggles with emerging non-qualified scenarios. Pilot2 addresses the full spectrum of EAA scenarios with mature standards, making it the more comprehensive solution despite higher complexity.

---

## **CONCLUSION**

The matrix reveals a fundamental insight: **the choice between Pilot1 and Pilot2 is primarily driven by EAA scenario requirements rather than just technical preferences**.

### **The Scenario-Driven Reality:**

**Pilot1 (Classical PKI)**: 
- **Perfectly aligned** for PubEAA and QEAA scenarios (Scenarios 3 & 4)
- **Optimal** for public sector authentic sources and qualified trust service providers
- **Challenged** by non-qualified EAA scenarios where "trust model falls short"
- **Risk factor**: Draft SD-JWT specifications create uncertainty across all scenarios

**Pilot2 (Hybrid PKI)**:
- **Essential** for non-qualified EAA scenarios where "EBSI provides major business value"
- **Complementary** for PubEAA/QEAA scenarios with enhanced capabilities
- **Comprehensive** coverage of all EAA scenarios with mature W3C standards
- **Stable foundation**: 6+ years of proven W3C VC technology

### **Strategic Recommendation:**

Organizations should select their pilot based on **primary EAA scenario requirements**:

- **Traditional regulated institutions** (ministries, QTSPs, established universities) → **Pilot1** for PubEAA/QEAA
- **Emerging credential ecosystem** (non-qualified providers, innovative institutions) → **Pilot2** for comprehensive scenario coverage
- **Comprehensive digital identity strategy** → **Pilot2** for future-proof foundation with mature standards

The critical insight is that Pilot2's apparent complexity is offset by its mature standards foundation and comprehensive scenario coverage, making it the more strategic choice for organizations planning long-term digital credential ecosystems.

