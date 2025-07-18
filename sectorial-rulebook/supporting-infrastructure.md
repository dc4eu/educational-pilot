# Supporting Infrastructure

## Overview

The credential ecosystem in European education faces a fundamental challenge: how to maintain trust, security, and interoperability across diverse national systems whilst enabling the digital transformation that modern learners and employers demand. This supporting infrastructure addresses this challenge by creating a robust foundation that enables all credential system components to function effectively through a hybrid trust model that combines traditional PKI with decentralised PKI (dPKI) and verifiable data registers.

Unlike traditional approaches that rely solely on centralised trust authorities, this infrastructure recognises that educational credentials operate in a complex ecosystem where multiple forms of trust coexist. A university degree must be trusted by employers in different countries, professional qualifications need recognition across borders, and micro-credentials require validation in contexts far removed from their original issuance. The infrastructure therefore provides multiple pathways for establishing and verifying trust, ensuring that credentials remain valuable and verifiable regardless of technological evolution or institutional changes.

## Key Requirements

The infrastructure must meet stringent requirements that reflect the unique challenges of European educational systems. These requirements emerge from the reality that education operates across multiple jurisdictions, involves diverse stakeholders with varying technical capabilities, and handles sensitive personal data requiring the highest levels of privacy protection.

### Multi-domain and Sector Support

Educational credentials span an extraordinarily diverse landscape, from traditional university degrees to professional micro-credentials, from vocational certifications to continuing education achievements. This diversity creates a challenge: how can a single infrastructure support such varied credential types whilst maintaining consistent trust and verification standards?

The infrastructure addresses this through flexible architectures that accommodate different credential formats, validation requirements, and governance models. A professional engineering certification requires different validation mechanisms than a university transcript, yet both must be equally trustworthy and verifiable. By supporting multiple domains and sectors, the infrastructure ensures that no educational achievement is left behind in the digital transformation.

- Works across educational domains
- Supports varied credential types
- Accommodates different institutional needs
- Enables cross-sector recognition

### Distributed Architecture

The centralised approach to credential verification creates vulnerable single points of failure that can compromise entire educational systems. When a central authority experiences technical difficulties or security breaches, the consequences ripple across all connected institutions. This risk is particularly acute in education, where credentials may need verification decades after issuance.

A distributed architecture fundamentally changes this dynamic by spreading trust and responsibility across multiple nodes and authorities. This approach reflects the federated nature of European education, where trust emerges from networks of recognised institutions rather than single authoritative bodies. The result is a more resilient system that continues operating even when individual components face challenges.

- Avoids centralised points of failure
- Distributes trust and responsibility
- Supports system resilience
- Maintains institutional autonomy

### Pan-European Coverage

The European education landscape is characterised by rich diversity in languages, systems, and traditions, yet the European Education Area vision requires seamless recognition and mobility. This creates a tension between respecting national sovereignty in education and enabling cross-border recognition and mobility.

The infrastructure resolves this tension by providing consistent technical standards whilst accommodating diverse national approaches to credential governance. A degree from a Spanish university must be as technically verifiable in Estonia as it is in Spain, yet the infrastructure must respect the different regulatory and quality assurance frameworks that give those credentials their educational value.

- Functions across all member states
- Supports cross-border operations
- Enables European-wide recognition
- Maintains consistency across regions

### Privacy-enhanced Verification

Traditional credential verification often requires sharing more personal information than necessary for the specific verification context. When a graduate applies for a job requiring a degree, why should the employer need to see detailed grades or personal information unrelated to the qualification level? This over-disclosure creates privacy risks and reduces individual control over personal data.

Privacy-enhanced verification transforms this dynamic by enabling selective disclosure, where individuals can prove they possess specific qualifications without revealing unnecessary details. This approach aligns with GDPR principles whilst providing the verification confidence that relying parties require. The infrastructure thus enables a more respectful relationship between credential holders and those who need to verify credentials.

- Protects user privacy during verification
- Prevents unnecessary tracking
- Implements data minimisation
- Supports selective disclosure

### Data Protection Compliance

Educational credentials contain some of the most sensitive personal data individuals possess, including not just academic achievements but often financial information, health accommodations, and detailed performance records. The regulatory landscape around this data is complex and evolving, with GDPR setting high standards for protection whilst educational institutions need practical ways to manage credentials effectively.

The infrastructure provides built-in compliance mechanisms that make data protection a natural part of credential management rather than an additional burden. By implementing privacy by design principles, the infrastructure ensures that compliance becomes an enabling feature rather than a limiting constraint.

- Aligns with GDPR requirements
- Implements privacy by design
- Supports data subject rights
- Enables appropriate governance

### Security Audit Mechanisms

Trust in educational credentials ultimately depends on the ability to verify that the underlying systems operate correctly and securely. However, traditional credential systems often operate as "black boxes" where external parties cannot independently verify system integrity or security measures. This opacity creates vulnerability to both technical failures and deliberate manipulation.

Comprehensive audit mechanisms provide transparency into system operations whilst maintaining security. These mechanisms enable stakeholders to verify that credentials are issued, stored, and verified according to stated policies and security standards. The result is a more trustworthy system where confidence emerges from verifiable evidence rather than blind trust.

- Provides transparency on system operation
- Enables security verification
- Supports compliance checking
- Maintains system integrity

### Verification Record Keeping

Educational credentials often require verification many years after initial issuance, sometimes decades later when individuals change careers or pursue further education. Traditional paper-based systems handle this through physical document preservation, but digital systems require more sophisticated approaches to long-term verification capability.

The infrastructure addresses this challenge through comprehensive record-keeping that maintains verification capability over extended periods whilst protecting privacy and supporting system evolution. These records enable dispute resolution, support compliance audits, and provide evidence for system improvements.

- Maintains appropriate audit trails
- Supports future verification needs
- Enables dispute resolution
- Provides operational evidence

### Service Discovery Tools

The distributed nature of the credential ecosystem creates a new challenge: how do wallets, verifiers, and other system components locate the services they need? Unlike centralised systems where service locations are predetermined, distributed systems require dynamic discovery mechanisms that adapt to changing network topologies and service availability.

Service discovery tools solve this challenge by providing reliable mechanisms for locating verification services, issuer information, and wallet-service connections. These tools enable the ecosystem to function as a coherent whole whilst maintaining the flexibility and resilience that distribution provides.

- Helps locate verification services
- Supports issuer discovery
- Enables wallet-service connections
- Facilitates ecosystem navigation

### Cross-country Legal Entity Recognition

Educational institutions derive their authority to issue credentials from national legal frameworks that vary significantly across Europe. A university chartered in France operates under different legal provisions than one established in Poland, yet both must be recognisable and trustworthy to verifiers across Europe.

The infrastructure provides technical mechanisms for representing and verifying legal entity status across borders, enabling consistent trust assessment regardless of jurisdictional differences. This capability is essential for supporting student mobility and ensuring that credentials retain their value when individuals move between countries.

- Supports recognition of institutions across borders
- Enables trust in foreign entities
- Maintains consistent verification
- Supports institutional mobility

## Trust Infrastructure Models

The evolution of digital trust has created multiple viable approaches to credential verification, each with distinct advantages and appropriate use cases. Rather than mandating a single approach, the infrastructure supports multiple trust models that can coexist and complement each other. This flexibility reflects the reality that educational institutions operate in diverse contexts with varying technical capabilities, regulatory requirements, and stakeholder expectations.

### Classical PKI Infrastructure

Public Key Infrastructure has provided the backbone for digital trust for decades, offering mature, well-understood security models that have proven their reliability in high-stakes environments. In educational contexts, classical PKI provides the regulatory compliance and institutional familiarity that many organisations require whilst offering predictable performance characteristics that system administrators can plan around.

The classical PKI approach leverages established hierarchical trust relationships that mirror traditional institutional structures in education. National authorities establish root trust, educational institutions receive certificates that prove their authority, and credentials can be verified through established certificate chains. This model provides the legal certainty and technical predictability that many educational institutions require.

**Trust Hierarchy**:
- National Certificate Authorities (CAs)
- Educational PKI hierarchies
- Institutional certificate chains
- Cross-border trust lists

**Key Components**:
- Certificate Authority (CA) trust stores
- Certificate Revocation Lists (CRLs)
- Online Certificate Status Protocol (OCSP) services
- Certificate validation services
- Cross-certification mechanisms

**Characteristics**:
- Established regulatory compliance
- Mature tooling and infrastructure
- Predictable verification times (~200ms)
- Well-understood security models

### Decentralised PKI with Verifiable Data Registers

The limitations of hierarchical trust models have become increasingly apparent as educational credentials diversify and cross-border mobility increases. Decentralised PKI addresses these limitations by distributing trust across multiple authorities and enabling more granular governance models that better reflect the complex relationships in modern education.

Built on the European Blockchain Services Infrastructure (EBSI), this approach enables educational institutions to demonstrate specific authorisations rather than just general authority. For example, an institution can prove it is authorised to issue EQF Level 7 credentials or provide MyAcademicID services, creating more precise and meaningful trust relationships. This granular approach reduces verification complexity whilst providing stronger assurance about specific institutional capabilities.

**Trust Components**:
- EBSI Trust Registry
- Trusted Issuer Registry
- Trusted Schema Registry
- Accreditation Registry
- Revocation Registry

**Key Features**:
- Decentralised identifier (DID) resolution
- Verifiable credential schemas
- Distributed trust anchors
- Granular authorisation verification
- Self-sovereign identity support

**Characteristics**:
- Enhanced privacy through selective disclosure
- Granular governance capabilities
- Reduced verification times (~150ms)
- Regulatory alignment with eIDAS 2.0

### Hybrid Trust Model

The hybrid approach recognises that the transition from traditional to decentralised trust models is not instantaneous and that different stakeholders may require different forms of trust assurance. Rather than forcing a choice between classical PKI and dPKI, the hybrid model combines both approaches to provide enhanced trust assurance and improved interoperability.

This model is particularly valuable in educational contexts where institutions may have significant investments in PKI infrastructure whilst needing to support modern credential standards and cross-border recognition. The hybrid approach enables progressive modernisation whilst maintaining existing trust relationships and regulatory compliance.

**Architecture**:
- Dual trust path validation
- X.509-DID binding mechanisms
- Fallback capabilities
- Cross-validation protocols

**Trust Enhancement**:
- Both PKI and dPKI paths must validate successfully
- Certificate-DID binding verification
- Enhanced interoperability with legacy systems
- Resilient operation during infrastructure unavailability

**Performance Considerations**:
- Increased verification time (~407ms total)
- Additional network requests required
- Enhanced trust assurance through dual validation
- Improved system resilience

## Implementation Considerations

Successful implementation of supporting infrastructure requires careful consideration of institutional contexts, technical capabilities, and long-term strategic objectives. The choice between trust models is not merely technical but reflects broader organisational decisions about risk tolerance, interoperability requirements, and resource allocation.

### Trust Model Selection

The decision of which trust model to implement should align with institutional capabilities and strategic objectives rather than following technology trends. Each model offers distinct advantages that may be more or less relevant depending on specific circumstances and requirements.

**Pure dPKI - Recommended When**:

Digital-native organisations with flexible technical architectures may find pure dPKI offers the best balance of performance, simplicity, and future-proofing. This approach is particularly suitable for institutions that can rely on EBSI infrastructure availability and prefer simplified maintenance requirements. The performance advantages (~150ms verification time) make this approach attractive for high-volume verification scenarios.

- Digital-native organisation with no legacy PKI infrastructure
- Performance is critical (≈150ms verification time)
- Simplified maintenance is preferred
- EBSI infrastructure is highly reliable in deployment context

**Hybrid Model - Recommended When**:

Institutions with existing PKI investments or complex interoperability requirements may find the hybrid model provides the best path forward. This approach is particularly valuable where enhanced trust assurance justifies the additional complexity and where fallback capabilities are important for operational reliability. The hybrid model enables progressive modernisation whilst maintaining existing trust relationships.

- Legacy PKI integration is required
- Maximum interoperability with existing systems is needed
- Enhanced trust assurance through dual validation is valued
- Regulatory compliance requires traditional PKI elements
- Fallback capability during EBSI unavailability is important

**Classical PKI - Recommended When**:

Mature institutions with established PKI infrastructure and conservative risk profiles may find classical PKI continues to meet their needs effectively. This approach is particularly suitable where regulatory requirements mandate traditional PKI approaches and where technical teams have deep expertise in PKI management. The predictable performance characteristics make this approach suitable for well-understood verification scenarios.

- Existing PKI infrastructure is mature and well-established
- Regulatory requirements mandate traditional PKI approaches
- Decentralised infrastructure is not yet available
- Conservative trust model is preferred

### Technical Implementation

The technical implementation of supporting infrastructure must balance multiple competing requirements including scalability, security, performance, and interoperability. These requirements often create tensions that require careful architectural decisions and ongoing monitoring to ensure optimal system performance.

**Infrastructure Requirements**:

Scalability planning must account for the long-term growth of the credential ecosystem, recognising that educational credentials may experience significant volume increases as digital adoption accelerates. Security maintenance requires ongoing attention to emerging threats and regular updates to cryptographic standards. Performance optimisation must consider the diverse technical capabilities of ecosystem participants, from well-resourced universities to smaller training providers.

- Scalability to accommodate growing ecosystem needs
- Security maintained through regular updates
- Performance optimised for efficient operations
- Interoperability enabling system connections
- Governance frameworks clearly defined

**Hybrid Model Dependencies**:

The hybrid model introduces additional complexity that requires careful dependency management and operational monitoring. The integration of classical PKI and dPKI components creates new failure modes that must be anticipated and managed through appropriate monitoring and alerting systems.

```
Classical PKI Components:
- Certificate Authority trust stores
- OCSP responder services
- CRL distribution points
- Certificate validation libraries

dPKI Components:
- EBSI registry access
- DID resolution services
- Verifiable credential validators
- Trust registry interfaces

Hybrid-Specific Components:
- X.509-DID binding validators
- Dual-path verification engines
- Fallback orchestration services
- Cross-validation protocols
```

### Security Considerations

The security implications of different trust models extend beyond technical implementation to encompass operational procedures, incident response, and long-term risk management. Each model creates different security profiles that require tailored approaches to monitoring, maintenance, and risk mitigation.

**Enhanced Security Benefits**:

The hybrid model provides security advantages through defence in depth, requiring adversaries to compromise multiple independent systems to successfully attack credential verification. This approach provides comprehensive audit trails that enhance forensic capabilities whilst enabling resilient operation during partial infrastructure failures.

- Dual trust anchors requiring compromise of both PKI and dPKI
- Binding integrity preventing certificate/DID substitution attacks
- Comprehensive audit trails across both trust models
- Resilient operation during partial infrastructure failures

**Risk Management**:

The complexity of hybrid systems introduces new risks that require careful management and monitoring. Binding verification failures can invalidate entire credentials, creating operational risks that must be managed through appropriate testing and monitoring procedures. The coordination required between PKI and dPKI lifecycle management creates additional operational complexity that must be planned and managed.

- Binding verification failures invalidate entire credential
- Coordination required between PKI and dPKI lifecycle management
- Increased complexity in error handling and monitoring
- Performance impact requiring careful system design

## Cross-Border Scenarios

The European education landscape requires credential systems that operate seamlessly across national boundaries whilst respecting the sovereignty and diversity of national educational systems. This creates unique challenges that require sophisticated technical solutions and careful attention to legal and regulatory differences.

For cross-border educational mobility, supporting infrastructure must bridge diverse national approaches to credential governance whilst maintaining consistent technical standards. A Croatian student studying in Ireland must be able to present credentials that are technically verifiable and educationally meaningful to Irish institutions, whilst those same credentials must remain valid when the student returns to Croatia or seeks employment in Germany.

**Trust Interoperability**:

The infrastructure addresses cross-border challenges through consistent technical standards that accommodate diverse national trust models. This approach enables recognition of national PKI infrastructures whilst providing EBSI-mediated trust for dPKI credentials. The hybrid validation capabilities support both trust models, ensuring that credentials remain verifiable regardless of the trust infrastructure available in different countries.

- Consistent operation across member states
- Recognition of diverse national PKI infrastructures
- EBSI-mediated trust for dPKI credentials
- Hybrid validation supporting both trust models

**Service Integration**:

Cross-border service integration requires sophisticated coordination between national systems whilst maintaining the efficiency and reliability that users expect. The infrastructure provides technical support for credential recognition through reliable verification services that operate across borders and integrate with diverse educational systems.

- Technical support for credential recognition
- Reliable verification services across borders
- Integration with diverse educational systems
- Harmonised privacy and disclosure policies

## Technical Components

The supporting infrastructure comprises multiple interconnected components that work together to provide comprehensive credential ecosystem support. These components must operate reliably both independently and in coordination with each other, creating a resilient system that continues functioning even when individual components experience difficulties.

**Trust Infrastructure**:

The trust infrastructure provides the foundation for all credential verification activities, encompassing both traditional and decentralised trust models. This infrastructure includes national and EBSI-based trust registries, comprehensive verification services, and the binding validation services that enable hybrid trust models to function effectively.

- Trust registries (EBSI and national)
- Verification services (PKI and dPKI)
- Certificate authorities and trust anchors
- Binding validation services

**Service Discovery**:

The distributed nature of the credential ecosystem requires sophisticated service discovery mechanisms that enable ecosystem participants to locate the services they need whilst maintaining security and privacy. These mechanisms must adapt to changing network topologies and service availability whilst providing reliable connections between wallets, verifiers, and service providers.

- Service directories
- Issuer discovery mechanisms
- Wallet-service connection protocols
- Cross-border service location

**Governance Framework**:

The governance framework provides the policy and procedural foundation that enables technical trust mechanisms to operate effectively. This framework includes authorisation verification systems that validate institutional authorities, compliance monitoring tools that ensure ongoing adherence to standards, and dispute resolution processes that handle conflicts and exceptions.

- Authorisation verification systems
- Compliance monitoring tools
- Audit trail mechanisms
- Dispute resolution processes

**Integration Interfaces**:

The transition to modern credential systems requires careful attention to integration with existing systems and processes. These interfaces provide the technical bridges that enable legacy systems to participate in the modern credential ecosystem whilst supporting progressive enhancement capabilities that enable gradual modernisation.

- Legacy system bridges
- API gateways
- Protocol translation services
- Progressive enhancement capabilities

**Supporting Documentation**:

Comprehensive documentation ensures that ecosystem participants can effectively implement and maintain their components whilst achieving interoperability with other ecosystem participants. This documentation encompasses technical specifications, integration guides, compliance frameworks, and operational procedures that enable effective ecosystem participation.

- Technical specifications
- Integration guides
- Compliance frameworks
- Operational procedures

## Conclusion

The supporting infrastructure represents a fundamental evolution in how educational credentials are managed, verified, and trusted across European education systems. By providing flexible trust models that accommodate diverse institutional needs, regulatory requirements, and technical capabilities, the infrastructure enables a more inclusive and resilient credential ecosystem.

The hybrid approach offers particular value by enabling institutions to leverage existing investments whilst adopting modern credential standards and cross-border recognition capabilities. This approach recognises that the transition to modern credential systems is not instantaneous and that different stakeholders may require different forms of trust assurance.

The infrastructure's emphasis on privacy-enhanced verification and selective disclosure aligns with European values around data protection whilst providing the verification confidence that employers, institutions, and other relying parties require. Through comprehensive audit mechanisms and transparent operations, the infrastructure builds trust through verifiable evidence rather than blind faith.

As European education continues to evolve towards greater mobility, flexibility, and digital integration, the supporting infrastructure provides the technical foundation that enables these aspirations to become reality whilst maintaining the security, privacy, and trust standards that European citizens expect and deserve.