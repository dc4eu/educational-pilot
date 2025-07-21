# DSTRL Procedures Directory

**Digital Student Records and Transcript Ledger - Operational Procedures and Legal Framework**

This directory contains the comprehensive procedural framework and legal guidance documentation for implementing the Digital Student Records and Transcript Ledger (DSTRL) within the European digital credentials ecosystem. It serves as the authoritative reference for organisations seeking to understand, implement, and operate within the DC4EU (Digital Credentials for Europe) legal and operational framework.

## Overview

The DSTRL Procedures directory provides detailed guidance on the legal, technical, and operational requirements for establishing and maintaining digital credential services across European educational institutions and professional bodies. This documentation addresses the complex regulatory environment established by eIDAS 2.0 and provides practical implementation pathways for different organisational contexts.

The procedures framework centres on a **legal entity-centric approach**, where educational institutions, professional bodies, public authorities, and technology providers assume clearly defined roles within a formalised trust network governed by European and national regulations.

## Directory Structure and Navigation

### Main Framework Documents

#### [`entities-main-framework.md`](./entities-main-framework.md)
**Purpose:** Comprehensive overview of the DC4EU legal entity ecosystem framework  
**Key Content:**
- Executive summary and navigation guide for the entire framework
- Quick reference matrix of entity roles and eligibility
- Implementation pathway recommendations (Classical PKI vs dPKI/EBSI)
- Trust network overview and relationship mapping
- Getting started checklists for new and existing organisations

#### Legal Entity Framework (`/entities/`)
A comprehensive sub-directory containing five core documents that define the operational framework for different types of legal entities within the DC4EU ecosystem:

**[`compliance.md`](./entities/compliance.md)**
- **Purpose:** Systematic regulatory adherence framework
- **Focus:** Entity-specific compliance requirements and monitoring procedures
- **Key Sections:**
  - Compliance requirements by entity type (QEAA Providers, Public Bodies, Relying Parties)
  - Continuous monitoring frameworks and tracking tools
  - Multi-level governance structure (European, National, Institutional)
  - Progressive enforcement approach and remediation procedures
  - Compliance checklists and dashboard templates

**[`implementation.md`](./entities/implementation.md)**
- **Purpose:** Practical step-by-step implementation guidance
- **Focus:** Technical integration processes and operational procedures
- **Key Sections:**
  - Classical PKI infrastructure implementation (X.509v3 certificates)
  - Decentralised PKI/EBSI integration (DIDs and blockchain)
  - Quality assurance and testing frameworks
  - Pilot implementation procedures and scaling strategies
  - Support resources and maintenance requirements

**[`relationships.md`](./entities/relationships.md)**
- **Purpose:** Inter-organisational trust network mapping
- **Focus:** Authority hierarchies and operational dependencies
- **Key Sections:**
  - Authority relationship matrices (European, National, Institutional levels)
  - Trust chain structures and cross-border mechanisms
  - Operational relationship patterns and lifecycle management
  - Quality assurance metrics and issue resolution procedures

## Key Concepts and Principles

### Legal Entity Ecosystem Approach
The DSTRL procedures framework operates on fundamental principles that distinguish it from individual-focused identity systems:

**Institutional Identity First**
- Educational institutions, professional bodies, and public authorities assume defined ecosystem roles
- Organisational capabilities determine the scope of ecosystem participation
- Institutional accountability maintains trust and reliability across the network

**Formalised Trust Relationships**
- Trust relationships established through formal accreditation and certification processes
- Authority chains define supervision and oversight responsibilities
- Operational agreements enable day-to-day ecosystem functions

**Regulatory Compliance Integration**
- Structured onboarding and monitoring frameworks maintain regulatory compliance
- Legal obligations clearly defined for each organisational role
- Enforcement mechanisms ensure accountability and standards maintenance

### Entity Roles and Responsibilities

The framework defines six primary organisational roles within the European digital credentials ecosystem:

#### **Authentic Sources (AS)**
- Maintain authoritative records (student data, professional licences, qualifications)
- Typically universities, professional bodies, and government agencies
- Provide verified data feeds to credential issuers

#### **Qualified EAA Providers (QEAA)**
- Offer highest level of assurance for digital credential issuance
- Must hold Qualified Trust Service Provider (QTSP) status
- Subject to stringent regulatory oversight and compliance requirements

#### **Public Body EAA Providers (Pub-EAA)**
- Public sector entities designated to provide digital credential services
- Equivalent security requirements to QTSPs but under public mandate
- Government universities, professional licensing bodies, public certification authorities

#### **EAA Providers (Non-Qualified)**
- Commercial and institutional providers offering digital credential services
- Lower regulatory burden but must meet security and interoperability standards
- Private universities, training providers, certification bodies

#### **Relying Parties (RP)**
- Organisations that verify and rely upon digital credentials
- Educational institutions, employers, professional bodies, government services
- Must implement proper verification procedures and data protection measures

#### **Supervisory Bodies**
- National authorities responsible for oversight and regulation
- Monitor compliance, maintain registries, enforce standards
- Coordinate with European-level frameworks and cross-border operations

## Implementation Pathways

### Classical PKI Pathway
**Recommended for:** Organisations with existing PKI infrastructure
- Traditional X.509v3 certificate-based trust model
- Integration with EU Trusted Lists
- Established QTSP relationships
- Proven security and compliance frameworks

### Decentralised PKI (dPKI) Pathway  
**Recommended for:** Forward-looking organisations preparing for eIDAS 2.0
- Decentralised Identifiers (DIDs) and W3C Verifiable Credentials
- European Blockchain Services Infrastructure (EBSI) integration
- Enhanced interoperability and verifiability
- Preparation for evolving European standards

### Hybrid Approach
**Recommended for:** Organisations seeking comprehensive coverage
- Combination of traditional certificates and EBSI DIDs
- Dual trust model implementation
- Enhanced flexibility and future-readiness
- Comprehensive user journey support

## Regulatory Context

This procedural framework operates within the evolving European regulatory landscape, including:

- **eIDAS 2.0 Regulation:** European framework for electronic identification and trust services
- **General Data Protection Regulation (GDPR):** Data protection and privacy requirements
- **European Qualifications Framework (EQF):** Academic credential recognition standards
- **Architecture and Reference Framework (ARF):** Technical interoperability specifications

## Getting Started

### For New Organisations
1. **Review Entity Roles:** Determine appropriate ecosystem role(s) using the main framework document
2. **Assess Compliance Requirements:** Use entity-specific compliance documentation
3. **Plan Implementation:** Select implementation pathway based on technical capabilities
4. **Establish Relationships:** Identify necessary trust relationships and partnerships
5. **Begin Pilot Implementation:** Follow structured testing and deployment procedures

### For Existing Participants
1. **Review Current Compliance Status:** Utilise compliance tracking tools and dashboards
2. **Optimise Trust Relationships:** Assess current network position and identify improvements
3. **Enhance Governance:** Implement advanced monitoring and performance management
4. **Consider Role Expansion:** Evaluate opportunities for additional ecosystem roles

## Quality Assurance and Governance

The procedures framework includes comprehensive quality assurance mechanisms:

- **Multi-level governance structure** spanning European, national, and institutional levels
- **Continuous monitoring frameworks** with automated compliance dashboards
- **Progressive enforcement approach** with remediation support
- **Performance metrics and KPIs** for system-wide effectiveness measurement
- **Issue escalation procedures** with clear resolution pathways

## Support and Resources

### Documentation Suite Navigation
- **Main Framework:** [`entities-main-framework.md`](./entities-main-framework.md) - Comprehensive overview and quick reference
- **Compliance Framework:** [`entities/compliance.md`](./entities/compliance.md) - Regulatory adherence procedures
- **Implementation Guide:** [`entities/implementation.md`](./entities/implementation.md) - Technical integration procedures  
- **Relationship Management:** [`entities/relationships.md`](./entities/relationships.md) - Trust network mapping

### Additional Support
- **Technical Assistance:** Contact your national supervisory body for implementation support
- **Training Resources:** Access DC4EU training programmes and certification materials
- **Community Forums:** Participate in practitioner networks and knowledge-sharing platforms
- **Professional Services:** Engage with certified implementation partners for deployment assistance

## Framework Evolution

This procedural framework is designed to evolve with the European digital identity landscape through:

- **European Commission policy development** and regulation updates
- **Standards bodies technical specification evolution**
- **Practitioner feedback** from ecosystem participants  
- **Research findings** from academic and industry collaborations

Regular updates ensure the framework remains current with regulatory changes, technological developments, and operational experience from deployment across European institutions.

---

**Last Updated:** July 2025  
**Version:** 2.1  
**Next Review:** December 2025

*This procedural framework supports the creation of a unified European digital credential ecosystem whilst respecting institutional autonomy and national sovereignty in educational and professional qualification systems. By focusing on legal entities and their formalised relationships, it provides the foundation for trusted, interoperable, and legally compliant digital credential management across the European Union.*