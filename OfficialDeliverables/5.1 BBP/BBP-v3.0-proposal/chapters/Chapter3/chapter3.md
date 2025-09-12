## <a id="_Toc182376668"></a><a id="_Toc184710015"></a>Chapter 3: Current challenges and needs in educational and professional credential management

The management of educational credentials in Europe is at a critical juncture, facing a myriad of challenges stemming from the diverse and decentralised nature of the continent's education systems\. This chapter examines the current state of credential management, identifying key challenges and needs within the European educational ecosystem\.

The trust framework's solution to these challenges is detailed in Section 4\.1, with technical specifications provided in Section 7\.2\.

### <a id="_Toc182376669"></a><a id="_Toc184710016"></a>3\.1 Credential issuance and verification

#### 3\.1\.1 Diversity in credential formats

Educational institutions across Europe issue credentials in a wide range of formats, from traditional paper\-based documents to advanced digital certificates\. This diversity reflects deep\-rooted institutional practices and national regulations\.

Paper\-based credentials remain common in many European countries, often incorporating security features such as watermarks or holograms\. However, these present challenges in terms of verification, especially across borders, and are vulnerable to loss or damage\.

Digital credentials are gaining traction, with formats ranging from simple PDF documents to more sophisticated verifiable credentials\-based certificates\. Some institutions issue hybrid credentials, providing both paper and digital versions\. The adoption of digital credentials varies significantly between countries and institutions\.

This diversity in credential formats creates challenges for employers and educational institutions attempting to verify qualifications from different countries\. Each format may require different verification methods, leading to inefficiencies and potential security risks\.

#### 3\.1\.2 Verification processes

The verification of educational credentials remains a complex and often manual process in many parts of Europe\. Methods used for verification vary widely, reflecting the diverse credential formats and institutional practices\.

Many institutions still rely on direct communication with the issuing body for verification\. This method, while potentially thorough, is time\-consuming and resource\-intensive\. It can lead to significant delays in processes such as university admissions or job applications, particularly when credentials need to be verified across borders\.

Some countries have implemented digital verification platforms at a national level\. For example, the Netherlands has developed a system called DUO, which allows for the digital verification of Dutch educational credentials\. While such systems can streamline the verification process within a country, they often lack interoperability with systems from other countries, limiting their usefulness in a pan\-European context\.

There's a need for a trust infrastructure must provide:

- Distributed verification capabilities
- Redundant record keeping
- Independent verification pathways
- Protection against single points of failure

Such infrastructure is a potential solution for credential verification, offering the potential for near\-instantaneous verification and could significantly reduce the administrative burden of credential checking\.

The lack of a standardised, digitalised cross\-border verification system creates inefficiencies and potential security risks\. It also poses barriers to student mobility and professional recognition across Europe, as the time and effort required to verify credentials can discourage institutions and employers from considering applicants with qualifications from unfamiliar systems\.

#### 3\.1\.3 Building on Bologna Process achievements

The current digital credential challenges mirror those addressed by the Bologna Process for degree structures and quality assurance\. The Bologna Process demonstrated that:

- Common standards can coexist with national autonomy
- Voluntary frameworks can achieve widespread adoption
- Practical tools \(like ECTS\) can solve complex cross\-border challenges
- Quality assurance can be standardized while respecting institutional diversity

These lessons inform our approach to digital credential standardization\. Just as ECTS created a common "currency" for academic credit, digital credentials need standardized formats and trust frameworks that work across borders while respecting institutional and national requirements\.

### <a id="_Toc182376670"></a><a id="_Toc184710017"></a>3\.2 Recognition of qualifications

#### 3\.2\.1 Academic recognition

The recognition of academic qualifications for further study presents several challenges, largely stemming from the autonomy granted to educational institutions in many European countries\.

Institutional autonomy in recognition practices leads to inconsistencies in how qualifications are valued and recognised\. An academic qualification that is readily accepted for further study in one institution may be viewed differently by another, even within the same country\. This variability can create uncertainty for students and potentially lead to unfair outcomes\.

The methods used for evaluating and recognising prior qualifications vary widely\. Some institutions conduct case\-by\-case manual evaluations, which can be thorough but time\-consuming and potentially subjective\. Others use more standardised procedures based on systems like the European Credit Transfer and Accumulation System \(ECTS\)\. While ECTS has helped to standardise credit recognition within the European Higher Education Area, its application is not uniform across all institutions and programmes\.

The lack of automation in recognition processes is a significant issue\. Few institutions reported automated recognition processes, with most relying on human evaluation\. This reliance on manual processes can lead to delays and inconsistencies, particularly when dealing with a high volume of applications or unfamiliar qualifications\.

#### 3\.2\.2 Professional recognition

The recognition of professional qualifications faces its own set of challenges, often more complex due to the regulatory nature of many professions\.

Each EU member state has its own regulations for professional recognition, particularly for regulated professions\. This regulatory complexity can make it difficult for professionals to have their qualifications recognised when moving between countries, even within the EU\.

The responsibility for recognition is often distributed among numerous authorities based on professional fields\. For example, medical qualifications might be recognised by a health authority or by the national body representing the corresponding professional corporations, while engineering qualifications fall under a different body\. This fragmentation can make the recognition process confusing and time\-consuming for applicants, who may need to navigate multiple systems and requirements\.

While some countries have implemented digital services for professional recognition applications, many processes remain paper\-based and time\-consuming\. The European Professional Card, an electronic procedure for recognising professional qualifications between EU countries, is a step towards digitalisation but is currently limited to a few professions\.

These challenges significantly hinder professional mobility within Europe\. Professionals may face lengthy and complex processes to have their qualifications recognised in different countries, potentially discouraging them from seeking opportunities abroad or leading to underemployment when they do move\.

The operational model addresses these challenges through mechanisms detailed in Section 4\.2, with practical examples demonstrated in Section 6\.3\.1\.

### <a id="_Toc182376671"></a><a id="_Toc184710018"></a>3\.3 Data management and interoperability

#### 3\.3\.1 Data models and standards

The lack of widely adopted standards for data models in the education sector is a significant barrier to interoperability\. Our research found that only 18% of surveyed countries reported aligning their educational data models with international standards like ELMO \- ELMO is a data format for the exchange of \(education\) result information\. ELMO is an implementation of the European \(CEN\) standards ELM\-AI \(European Learner Mobility – Achievement Information, EN 15981\) and MLO \(Metadata for Learning Objects, EN 15982\)\.

The adoption of common data models varies across education levels\. Higher education tends to have higher adoption rates \(59% of surveyed countries\), likely due to initiatives like the Bologna Process which have encouraged standardisation in this sector\. However, adoption rates are lower for other levels of education, creating challenges for lifelong learning recognition\.

This lack of standardisation hampers data interoperability and complicates the process of comparing and recognising qualifications across borders\. When educational data is stored and structured differently in various systems, it becomes difficult to create automated processes for qualification recognition or to provide comprehensive views of an individual's educational achievements\.

#### 3\.3\.2 Data sharing and privacy

While all surveyed countries adhere to the General Data Protection Regulation \(GDPR\), the implementation of education or professional\-specific data protection measures varies\. This variability can create uncertainty about what data can be shared and how, potentially hindering efforts to create comprehensive systems for credential recognition\.

There are limited mechanisms for secure, efficient cross\-border exchange of educational data\. While initiatives like EMREX aim to facilitate such exchange in higher education, their adoption is not universal\. The lack of established channels for data exchange can lead to reliance on less secure methods or create barriers to recognition processes\.

Balancing data sharing for recognition purposes with stringent privacy requirements presents an ongoing challenge\. Educational institutions and regulatory bodies must navigate the need to verify and recognise qualifications while respecting individuals' rights to data privacy and control over their personal information\.

### <a id="_Toc182376672"></a><a id="_Toc184710019"></a>3\.4 Technological infrastructure

The development of technological infrastructure to support digital credential management varies significantly across Europe, creating disparities in the ability to issue, manage, and verify digital credentials\.

Some countries have implemented national platforms for issuing and verifying digital credentials\. For example, Estonia's e\-government infrastructure includes provisions for digital educational certificates\. However, these advanced systems are not universally adopted across Europe\.

Trusted ledger initiatives for credential management are being explored by some institutions, offering potential for secure, decentralised credential verification\. However, widespread adoption remains limited, often confined to pilot projects or specific institutions\.

Many institutions still rely on legacy systems that are not easily integrated with newer digital solutions\. This reliance on older technology can create barriers to adopting more advanced credential management systems and can hinder interoperability efforts\.

The disparity in technological readiness across European educational institutions poses challenges for implementing unified digital credential solutions\. Institutions with more advanced systems may be reluctant to adopt new standards that require significant changes, while those with less developed infrastructure may struggle to implement more advanced solutions\.

### <a id="_Toc182376673"></a><a id="_Toc184710020"></a>3\.5 Legal and regulatory framework

The legal and regulatory landscape for educational credentials in Europe is complex and varied, reflecting the diversity of national education systems and the evolving nature of digital credentials\.

Many countries have specific legislation governing the issuance and recognition of educational credentials\. These laws may not always align with digital transformation goals, potentially creating legal barriers to the adoption of digital credentials or new verification methods\.

EU\-level initiatives like the European Qualifications Framework aim to improve the comparability of qualifications across countries\. However, implementation and recognition at the national level remain inconsistent, highlighting the challenges of creating truly pan\-European solutions in education\.

The evolving landscape of digital identity regulations, including the amended eIDAS Regulation framework, presents both opportunities and challenges for digital credential management\. While these regulations aim to create a common framework for electronic identification across Europe, their application to educational and professional credentials is still developing\.

According to Recital \(55\) of the eIDAS 2 Regulation, “an electronic attestation of attributes should not be denied legal effect on the grounds that it is in an electronic form or that it does not meet the requirements of the qualified electronic attestation of attributes”, a principle that ensures the validity of any electronic attestation of attributes, especially when a sector\-specific EU or national legislation already allows issuing documents to specific bodies\. One relevant example for the educational and professional domain is the Professional Qualifications Directive, where the issuers of the credentials would be the competent authority, typically an authentic source of the information contained within\.

Thus, Article 1\(c\) of the amended eIDAS Regulation “establishes a legal framework for”, among others, “electronic attestation of attributes”, which is defined by Article 3\(44\) as “an attestation in electronic form that allows attributes to be authenticated”\. The amended eIDAS Regulation considers two specific subtypes of electronic attestations of attributes \(named as “qualified electronic attestation of attributes” and “electronic attestation of attributes issued by or on behalf of a public sector body responsible for an authentic source”\), which receive direct legal recognition, but enshrining the validity and judicial admissibility of all electronic attestations of attributes\. According to Article 45b\(1\) of the amended eIDAS Regulation, “an electronic attestation of attributes shall not be denied legal effect or admissibility as evidence in legal proceedings on the sole ground that it is in electronic form or that it does not meet the requirements for qualified electronic attestations of attributes”\.

This legal approach, which is common to the different legal evidentiary institutions enabled by trust services, ensures that innovative approaches can be used in real world use cases requiring legal validity\. 

Navigating this complex regulatory environment while pushing for innovation in credential management requires careful consideration, to be explored during the Large\-Scale Pilots\. Depending of the results, it may necessitate legislative updates at both national and EU levels \(especially to the eIDAS Implementing Acts\) to fully enable the potential of digital credentials while ensuring appropriate safeguards and recognition\. This is potentially one of the most relevant contributions to the evolution of the eIDAS ecosystem, where some gaps have already been identified\.

### <a id="_Toc182376674"></a><a id="_Toc184710021"></a>3\.6 Stakeholder needs and concerns

Different stakeholders in the educational ecosystem have varying needs and concerns regarding credential management\. Understanding and addressing these diverse perspectives is crucial for developing effective solutions\.

Educational institutions seek ways to reduce the administrative burden associated with issuing and verifying credentials\. They also express concerns about balancing standardisation with institutional autonomy in credential issuance and recognition\. Many institutions face challenges in adapting to new technologies for credential management, including costs and training needs\.

Students and graduates demand easily portable and universally recognised credentials to support mobility for study and work\. They express concerns about data privacy and desire greater control over their educational records\. There's an increasing need for recognition of non\-traditional learning experiences and micro\-credentials, reflecting changing patterns of learning and career development\. Students are seeking more flexible ways to showcase their skills and knowledge, beyond traditional degree certificates\.

Employers and professional bodies seek quick and reliable methods to verify candidates' qualifications\. This need is particularly acute in sectors with high mobility or where specific qualifications are crucial for regulatory compliance\. There's a growing emphasis on recognising specific skills and competencies beyond formal qualifications, as employers look for more granular information about candidates' capabilities\. Multinational employers face challenges in comparing and recognising qualifications from different educational systems, which can complicate international recruitment processes\.

Regulatory bodies are tasked with ensuring the quality and integrity of educational and professional credentials while adapting to technological changes\. They must balance the need for innovation with maintaining rigorous standards\. There's an increasing need for cross\-border cooperation between national regulatory bodies to facilitate smoother recognition processes\. Developing robust systems to prevent credential fraud remains a key concern, particularly as digital credentials become more prevalent\.

### <a id="_Toc182376675"></a><a id="_Toc184710022"></a>3\.7 Opportunities for digital solutions

The trust framework offers five key opportunity areas for transforming credential management:

1\. Digital transformation

- Standardized digital credential formats across Europe
- Secure, verifiable digital documents replacing paper
- Integration with existing information systems
- Support for emerging credential types
- Digital workflow automation

2\. Cross\-border mobility

- Automated qualification recognition
- Standardized credential verification
- Multilingual credential support
- Simplified professional licensing
- Enhanced student mobility

3\. System efficiency

- Reduced manual verification needs
- Streamlined administrative processes
- Lower operational costs
- Faster credential processing
- Improved data accuracy

4\. Data protection and privacy

- Enhanced personal data control
- Secure credential storage
- Privacy\-preserving verification
- Compliance with GDPR
- Selective information sharing

5\. Innovation support

- New educational service models
- Enhanced labour market matching
- Support for lifelong learning
- Improved policy analytics
- Cross\-institutional collaboration

These opportunities are realised through:

- Operational processes detailed in Chapter 4
- Technical implementations specified in 8
- Practical use cases demonstrated in Chapter 7 Implementation guidance is provided in Chapter 8

The current state of educational credential management in Europe presents a complex landscape of challenges and opportunities\. Key issues include the diversity of issuance and verification practices, inconsistencies in recognition processes, limited data standardisation and interoperability, varied technological readiness, and a complex regulatory environment\.

Addressing these challenges requires a multifaceted approach that considers the needs of all stakeholders while leveraging technological innovations\. The development of solutions like the European Digital Identity Wallet and associated frameworks offers promising avenues for addressing many of these challenges\. By providing a standardised, secure platform for storing and sharing digital credentials, such systems could significantly improve the portability and recognition of qualifications across Europe\.

However, successful implementation will require careful consideration of the diverse national contexts, regulatory requirements, and stakeholder needs identified in this analysis\. It will also necessitate ongoing dialogue and cooperation between educational institutions, employers, regulatory bodies, and technology providers to ensure that solutions meet the needs of all parties and can be effectively integrated into existing systems\.