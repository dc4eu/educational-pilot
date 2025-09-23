# Sectorial EAA Catalogue for Education and Professional Qualifications

## Overview

This Sectorial Electronic Attestation of Attributes (EAA) Rulebook contains all data models and schemas agreed at the sectorial level for Education and Professional Qualifications. It provides the technical specifications that implement the principles outlined in the [Sectorial Rulebook](../sectorial-rulebook/).

## EAA catalogue governance
For the definition of the EAA catalogue, it is essential to identify, for each entry in the catalogue, the party responsible for its creation and evolution - that is, the 'Attribute schema provider'.
The common thread throughout the entire EAA catalogue is the utilisation of the European Learning Model (ELM v3.2) as a shared ontology.
Given the absence of a central authority in education, yet recognising the necessity to establish this sectoral role, we might consider making an assignment based on competencies, bearing in mind that **DG-EAC** is responsible for Primary, Secondary and Tertiary education, whilst **DG-EMPL** oversees Adult education and TVET. OF course, Member States, as key satkeholders and comptencies' owners, should also be members of such governance.

## EAAs are not the original Diplomas

EAA is defined as an attestation in electronic form that allows attributes to be authenticated.

It is important to explain and clarify that there is a distinction between the Diploma itself and an EAA of the diploma (for example, in Spain this is legally required to be issued on A3 paper with specific weight and security measures, or, using digital means, the Diploma is stored, curated and preserved in a database record). 
The EAA does not replace the former, but holds equivalent legal value.

## European Learning Model (ELM)

ELM allows educational institutions, employers, learners, and credential-verifying bodies to communicate clearly and effectively about learning achievements and credentials.

Key benefits include:
- Interoperability across different European systems.
- Easier recognition of qualifications.
- Clear communication about learning outcomes and achievements.
- Standardised descriptions for educational credentials.

For further information on ELM, access [European Learning Model information](./elm/elm.md)

## European Digital Credentials for Learning (EDC)

European Digital Credentials for Learning (EDC) are verifiable digital representations of learning achievements, issued by educational institutions to document qualifications such as diplomas, training certificates, and micro-credentials. They are signed with an electronic seal from a trusted institution, ensuring authenticity and security. EDCs can be issued in all EU and Europass languages, facilitating cross-border recognition of qualifications. ​

Key benefits include:

- Enhanced security and authenticity: EDCs are electronically sealed, making them tamper-evident and legally equivalent to paper-based credentials. ​
- Efficient sharing and storage: Learners can store their EDCs securely in their Europass wallet (the "My Library" repository) and share them easily with employers or educational institutions. ​
- Standardized format: EDCs provide a consistent structure for describing learning achievements, promoting interoperability across different European systems. ​
- Support for various learning contexts: They can document formal education, non-formal learning, online courses, and volunteering experiences, among others. ​

For further information on EDC, access [European Digital Credentials for Learning]( https://europass.europa.eu/en/europass-digital-tools/european-digital-credentials-learning)

## EDC and ELM, closely realted but not the same

ELM (European Learning Model) is an ontology or conceptual data model describing learning achievements, qualifications, and educational credentials, covering formal, non-formal, and informal education. It is a general framework describing educational data clearly and consistently.
EDC (European Digital Credential) is an application profile that specifically implements the European Learning Model (ELM) to create digital credentials. EDC uses the concepts and structure defined by ELM, adding technical standards and constraints (e.g., SHACL constraints) to ensure data quality, authenticity, and validity specifically for digital credentialing purposes.
In other words:

- ELM provides the underlying conceptual model.
- EDC applies this model specifically to digital credentials, including concrete implementations, validations, and practical usage aligned closely —but not entirely— with W3C Verifiable Credentials.

## EDC and W3C-VC, inspired by but not equal to

European Digital Credentials (EDC) issued using Online Credential Builder (OCB) provided by DG-EMPL, it's a ELM serialisation inspired by W3C-VC but not fully compliant.

- Top-level structure: EDC credentials, as produced by OCB, uses "credential" instead of putting W3C fields directly at the root.
- Missed issuanceDate / expirationDate
- Missed revocation/suspension (not supported)
- deliveryDetails are linked to especific delivery mechanism used by OBC, it won't be required 


EDC JSON structure (view 1)


```mermaid
graph TD
  Root["Root (Object)"]
  credential["credential (Object)"]
  deliveryDetails["deliveryDetails (Object)"]

  Root --> credential
  Root --> deliveryDetails
```

EDC JSON structure (view 2)


```mermaid
graph TD
  Root["Root (Object)"]
  credential["credential (Object)"]
  id["id (String)"]
  type["type (Array)"]
  credentialSchema["credentialSchema (Array)"]
  evidence["evidence (Array)"]
  credentialSubject["credentialSubject (Object)"]
  issuanceDate["issuanceDate (String)"]
  issued["issued (String)"]
  validFrom["validFrom (String)"]
  credentialProfiles["credentialProfiles (Array)"]
  displayParameter["displayParameter (Object)"]
  identifier["identifier (Array)"]
  deliveryDetails["deliveryDetails (Object)"]
  deliveryAddress["deliveryAddress (Array)"]
  displayDetails["displayDetails (Object)"]

  Root --> credential
  credential --> id
  credential --> type
  credential --> credentialSchema
  credential --> evidence
  credential --> credentialSubject
  credential --> issuanceDate
  credential --> issued
  credential --> validFrom
  credential --> credentialProfiles
  credential --> displayParameter
  credential --> identifier
  credential --> deliveryDetails
  deliveryDetails --> deliveryAddress
  deliveryDetails --> displayDetails
```

## European Digital Credentials – W3C Compliant (EDC-W3C)

EDC-W3C represents the European Digital Credentials for Learning (EDC) fully aligned with the W3C Verifiable Credentials Data Model (VCDM), as adopted in the first batch of the Implementing Acts under the European Digital Identity framework.

This enhanced version of EDC ensures full compliance with globally recognised standards for digital credentials, promoting interoperability beyond Europe and supporting secure, verifiable, and privacy-preserving learning achievements.

EDC-W3C is a W3C-VCDM serialisation of the European Learning Model (ELM) provided by DG EMPL (Directorate-General for Employment, Social Affairs and Inclusion).

Key benefits include:
- Global interoperability: Based on W3C-VCDM, EDC-W3C enables seamless cross-border and cross-sector recognition of credentials.
- Full alignment with EU and international digital identity standards: Supporting the vision of the European Digital Identity Wallet.
- Data integrity and privacy: Ensures secure, verifiable credentials while respecting the privacy of credential holders.
- Consistency with the European Learning Model: Structured data remains anchored in ELM while adopting the W3C format.

```mermaid
graph TD
  Root["Root (Object)"]
  credential["credential (Object)"]
  id["id (String)"]
  type["type (Array)"]
  credentialSchema["credentialSchema (Array)"]
  evidence["evidence (Array)"]
  credentialSubject["credentialSubject (Object)"]
  issuanceDate["issuanceDate (String)"]
  issued["issued (String)"]
  validFrom["validFrom (String)"]
  credentialProfiles["credentialProfiles (Array)"]
  displayParameter["displayParameter (Object)"]
  identifier["identifier (Array)"]
  deliveryDetails["deliveryDetails (Object) - optional"]
  deliveryAddress["deliveryAddress (Array)"]
  displayDetails["displayDetails (Object)"]

  Root --> credential
  Root --> id
  Root --> type
  Root --> credentialSchema
  Root --> evidence
  Root --> credentialSubject
  Root --> issuanceDate
  Root --> issued
  Root --> validFrom
  Root --> credentialProfiles
  Root --> displayParameter
  Root --> identifier
  Root --> deliveryDetails
  deliveryDetails --> deliveryAddress
  deliveryDetails --> displayDetails
  ```

For further information on EDC-W3C, access:
- [EDC-W3C compliant with W3C-VCDM 1.0](https://code.europa.eu/ebsi/json-schema/-/tree/main/schemas/vcdm1.1/europass/edc) 
- [EDC-W3C compliant with W3C-VCDM 2.0](https://code.europa.eu/ebsi/json-schema/-/tree/main/schemas/vcdm2.0/edc)

## PID Scheme (outside the scope of LSPs, but required for the wallet to become operational + onboarding of students/professionals in educational/professional qualification domains). Must be compliant with 1st batch of implementing acts.

| Scope        | Data model name    | Brief explanation |Status/Detailed explanation |Schema URL     | Registry URL |
|-----------------------------|--------------------------|--------|------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| Foundational identity       | PID (Natural Person)     | Person Identification Data (PID) for foundational credentials compliant with eIDAS 2.0 and ARF |Available| [Schema](https://code.europa.eu/ebsi/json-schema/-/tree/main/schemas/vcdm1.1/vid/natural-person)                 | [Registry](https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/z2bTCgjmBDY5kwNWGL3hfSQUZP6d8AZUnLFXe8coTa3zK) |

## Table with available schemes for non-foundational IDs
| Scope        | Data model name    | Brief explanation |Status/Detailed explanation |Schema URL     | Registry URL |
|-----------------------------|--------------------------|--------|------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| Non-foundational identity   | EducationalID           | Identifies the natural person in the context of an educational organisation, including national extensions |Available| [Schema](https://code.europa.eu/ebsi/json-schema/-/tree/main/schemas/vcdm1.1/education/verifiable-education-id) | [Registry](https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/zEmFZquJtANNz7XNE46thRi1E2cAfpQiXVLSBdDgLyfGP) |
| Non-foundational identity   | AllianceID               | Identifies a student or staff member as affiliated with a European university alliance |Available| [Schema](https://code.europa.eu/ebsi/json-schema/-/tree/main/schemas/vcdm1.1/alliance-id)                       | [Registry](https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/zCHc3ZfYg2871W2WftjLu4QNMQrDzG57oG5pvGoyHcagB) |
| Non-foundational identity   | EuropeanStudentCard | European Student Card for student mobility, based on DG-EAC's service |Available| [Schema](https://code.europa.eu/ebsi/json-schema/-/blob/main/schemas/vcdm1.1/dc4eu/european-student-card/schema.json) | [Registry](https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/0x0e46f9509c52e649d8b461216b66836bd8398b8779469a571404264ea02c3bd9) |
| Non-foundational identity   | MyAcademicID             | Identity credential for student mobility, based on MyAcademicID and eduGAIN infrastructure |Available| [Schema](https://code.europa.eu/ebsi/json-schema/-/tree/main/schemas/vcdm1.1/multi-uni-pilot/my-academic-id)     | [Registry](https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/z3XDm4kDtztE8DzLsVdhfshYvx2upnfLmqHtyVjkaXM1g) |
| Non-foundational identity   | ProfessionalID             | Identity credential for , based on  |Available| [Schema](https://code.europa.eu/ebsi/json-schema/-/tree/main/schemas/vcdm1.1/dc4eu/professional-id)     | [Registry](https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/z2CHBovrL2TptHFFtszG5Jn8LZU1SxLfMY6Vg93ctKEAw) |
| Non-foundational identity   | DoctorID             | Identity credential for , based on  |Available| [Schema](https://code.europa.eu/ebsi/json-schema/-/tree/main/schemas/vcdm1.1/dc4eu/doctor-id)     | [Registry](https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/zDD8wM8F6UsfrdACeph41EFmgEUUsDnC6SVqY4QFh8MFZ) |
| Non-foundational identity   | EngineerID             | Identity credential for , based on  |Available| [Schema](https://code.europa.eu/ebsi/json-schema/-/tree/main/schemas/vcdm1.1/dc4eu/engineer-id)     | [ Registry](https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/ziwaS92VRyKojd3Xmk9wgvBo5XYwqG8EYENK9zFQNJWG) |

## Table with available datamodels based on EDC-W3C (W3C-VCDM 1.1 aligned to 1st batch of implementing acts)

| Scope | Data model name | Stablished Acronim (type) | Brief explanation | Status/Detailed explanation | Schema URL | Registry URL | Unsigned credential | Signed Credential | Authentic Source Content |
|-------|----------------|----------------|-------------------|----------------------|------------|--------------|------------|------------|------------|
|Education and Professional qualifications| EDC-W3C| Generic academic and professional achievements | European Digital Credential compliant with W3C-VCDM v1.1 credential format based on ELM v3.2 in alignment to 1st batch of implementing acts, supports any type of educational and professional qualifications | Generic EDC-W3C | [Schema](https://code.europa.eu/ebsi/json-schema/-/tree/main/schemas/vcdm1.1/europass/edc) | [Registry](https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/0xe9d256a96313a24d5884d56f0835047febc0ebf46fbdd20c906f49057a1e0f02)  | N/A | N/A| N/A|
| Education | Higher Education European Micro Credentials | EUHEMC | Educational achievement microcredential for | [Higher Education Micro Credential](./formal-education/business/EUHEMC-highereducation-microcredential_business.md) | [LocalSchema](./formal-education/schemes/EUHEMC-EuropeanHigherEducationMicrocredential.json) | [EBSIRegistry](https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/0x05332a9dc53a4a26a15711262904f2a1dd081cf3da735350f42dac20426530a4) | [HEEUMC unsigned](./formal-education/examples/EUHEMC/euhe-microcredential-example-john-doe.md) | [HEEUMC signed](./formal-education/examples/EUHEMC/euhe-microcredential-signed-john-doe.md) | [HEEUMC Authetic Source Content](./formal-education/examples/EUHEMC/euhe-microcredential-examples-authentic_source.md)|
| Education | Vocational Educational Training European Micro Credentials | EUVETMC | Educational achievement microcredential for | [Vocational Educational Training Micro Credential](./formal-education/business/EUVETMC-vet-microcredential_business.md) | [LocalSchema](./formal-education/schemes/EUVETMC-EuropeanVocationalEducationTrainingMicrocredential.json) | [EBSIRegistry](https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/0x690878adbdbc2c6b2865829003a1e34800df5d173d302ff11958836f8f977a26) | [VETEUMC unsigned](./formal-education/examples/EUVETMC/euvet-microcredential-example-john-doe.md) | [VETEUMC signed](./formal-education/examples/EUVETMC/euvet-microcredential-signed-john-doe.md) |  [HEEUMC Authetic Source Content](./formal-education/examples/EUHEMC/euhe-microcredential-examples-authentic_source.md)|
| Education | Higher education proof of enrolment | EUHEPOE| EHigher education proof of enrolment| [Higher Education Proof of Enrolment](./formal-education/business/EUHEPOE-highereducation-proofofenrolment_business.md) | [Local Schema](./formal-education/schemes/EUHEPOE-EuropeanHigherEducationProofOfEnrolment.json) | [Registry](https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/0x9e7bdbe465fbca504ec04df331c47ef6d88eb258312d3471277e84dabda4a92e) | [EUHEPOE Unsigned](./formal-education/examples/EUHEPOE/euhepoe-highereducation-proofofenrollment-john-doe.md) | [EUHEPOE Signed](./formal-education/examples/EUHEPOE/euhepoe-highereducation-proofofenrollment-signed-john-doe.md)| [HEEUMC Authetic Source Content](./formal-education/examples/EUHEMC/euhe-microcredential-examples-authentic_source.md)|
| Education | Higher education diploma | EUHED| Higher education diploma | [Higher education diploma](./formal-education/business/EUHED-highereducation-diploma_business.md) | [Local Schema](./formal-education/schemes/EUHED-EuropeanHigherEducationDiploma.json) | [Registry](https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/0x7663df08b9a50f226e185efb7ec08f3d69f4a95e653ebffd3137b3eb6923dda8) | [EUHED Unsigned](./formal-education/examples/EUHED/euhed-highereducation-diploma-john-doe.md) | [EUHED Signed](./formal-education/examples/EUHED/euhed-highereducation-diploma-signed-john-doe.md)| [HEEUMC Authetic Source Content](./formal-education/examples/EUHEMC/euhe-microcredential-examples-authentic_source.md)|
| Education | Higher education diploma Supplement| EUHEDS| Higher education diploma Supplement | [Higher education diploma Supplement](./formal-education/highereducation-microcredential.md) | [Local Schema](./formal-education/schemes/EUHEDS-EuropeanHigherEducationDiplomaSupplement.json) | [Registry](https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/0x597214a686156123e6603272b72638a615d83037d306b16170ff838168dfaf13) | [EUHEDS Unsigned](./formal-education/examples/EUHEDS/euheds-highereducation-diplomasupplement-john-doe.md) | [EUHEDS Signed](./formal-education/examples/EUHEDS/euheds-highereducation-diplomasupplement-signed-john-doe.md)| [HEEUMC Authetic Source Content](./formal-education/examples/EUHEMC/euhe-microcredential-examples-authentic_source.md)|
| Education | Higher education transcript of records | EUHETOR| Higher education transcript of records| [Higher education transcript of records](./formal-education/schemes/EUHETOR-highereducation-transcriptofrecords.schema.json) | [Local Schema](./formal-education/schemes/EUHETOR-EuropeanHigherEducationTranscriptOfRecords.json) | [Registry](https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/0x1e4611b4d031fbd282e6cfc241623d3b25f322ed87aee7670f7c1a20a63c14f3) | [EUHETOR Unsigned](./formal-education/examples/EUHETOR/euhetor-highereducation-transcriptofrecords-john-doe.md) | [EUHETOR Signed](./formal-education/examples/EUHETOR/euhetor-highereducation-transcriptofrecordst-signed-john-doe.md)| [HEEUMC Authetic Source Content](./formal-education/examples/EUHEMC/euhe-microcredential-examples-authentic_source.md)|
| Education | Upper secondary education certificate | EUUSC | Upper secondary education certificate | [Upper secondary education certificates](./formal-education/business/EUUSC-uppersecondary-certificate.md) | [Local Schema](./formal-education/schemes/EUUSC-EuropeanUpperSecondaryEducationCertificate.json) | [Registry](https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/0x901e24612f601d3f6932b3d20ba50615cfd6d64ce4e8c263312b5c3c3b2f9623) | [EUUSC Unsigned](./formal-education/examples/UpperSecindaryCertificate/euusc-uppersecondary-certificate-john-doe.json) | [EUUSC Signed](./formal-education/examples/UpperSecindaryCertificate/euusc-uppersecondary-certificate-signed-john-doe.json)| [HEEUMC Authetic Source Content](./formal-education/examples/EUHEMC/euhe-microcredential-examples-authentic_source.md)|
| Education | Upper secondary education transcript of records | EUUSTOR | Upper secondary education transcript of records | [Upper secondary education transcript of records](./formal-education/business/EUUSTOR-uppersecondaryeducation-transcriptofrecords_business.md) | [Local Schema](./formal-education/schemes/EUUSTOR-EuropeanUpperSecondaryEducationTranscriptOfRecords.json) | [Registry](https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/0xaf79750aade036da40ba02a0b85f671d7232a1ad13df91b72df2ba0891f91aba) | [EUUSTOR Unsigned](./formal-education/examples/UpperSecondaryTranscriptOfRecords/euustor-uppersecondaryeducation-transcriptofrecords-john-doe.json) | [EUUSTOR Signed](./formal-education/examples/UpperSecondaryTranscriptOfRecords/euustorr-uppersecondarieducation-transcriptofrecordst-signed-john-doe.json)| [HEEUMC Authetic Source Content](./formal-education/examples/EUHEMC/euhe-microcredential-examples-authentic_source.md)|
| Professional qualifications | Certificate of Professional Suitability | CPS | Professional achievement credential for| Certificate of Professional Suitability | [LocalSchema](./formal-education/schemes/ProfessionalSuitabilityCredential.json) | [Registry](https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/0x2d5971743a402de5ba00aad9697200153cbac29ccb5b1852e704cd541213f994) | Unsigned | Signed| [HEEUMC Authetic Source Content](./formal-education/examples/EUHEMC/euhe-microcredential-examples-authentic_source.md)|
| Professional qualifications | Accreditatio Medical Training | AMT | Professional achievement credential for| Accreditation Medical Training| [LocalSchema](./formal-education/schemes/ProfessionalTrainingCredential.json) | [Registry](https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/0xa92c40f0684db3bbcf2bb2600579dfaf7785a421515394c79eb9de41debf17a7) | Unsigned | Signed| [HEEUMC Authetic Source Content](./formal-education/examples/EUHEMC/euhe-microcredential-examples-authentic_source.md)|
| Professional qualifications | Continous Professional Development | CPD | Professional achievement credential for| Continous Professional Development| [Schema](https://code.europa.eu/ebsi/json-schema/-/tree/main/schemas/vcdm1.1/dc4eu/continuous-professional-development) | [Registry](https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/z3RwKaN1kZciYkRpkqjwTW6whKV4WefiYx6wviWR7gzow) | Unsigned | Signed| [HEEUMC Authetic Source Content](./formal-education/examples/EUHEMC/euhe-microcredential-examples-authentic_source.md)|
| Professional qualifications | Professional Training Certificate | PTC | Professional achievement credential for| Professional Training Certificate| [Schema](https://code.europa.eu/ebsi/json-schema/-/tree/main/schemas/vcdm1.1/dc4eu/professional-training) | [Registry](https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/zCPP3GVyk2bK65E81K8BC6T2gdNYQNEeKgm9wEYuSgHTU) | Unsigned | Signed| [HEEUMC Authetic Source Content](./formal-education/examples/EUHEMC/euhe-microcredential-examples-authentic_source.md)|




## Detailed information per category or type

The EAA Rulebook is organised into the following categories:

### [Foundational Identity](./foundational-identity/)

### [Formal Education](./formal-education/)

### [Quality Assurance Regimes](./quality-assurance/)

### [Non-foundational ID](./non-foundational-id/)

## [Schemes for Data Models](./schemes-data-models/)

## Implementation

These data models and schemas are designed to be implemented through the technical components described in the [Toolkits](../toolkits/) section. They support the workflows and use cases outlined there while ensuring compliance with the principles established in the [Sectorial Rulebook](../sectorial-rulebook/).

## Version Control

All data models and schemas in this rulebook are versioned to allow for backward compatibility as the framework evolves. Implementers should always check for the latest versions while maintaining support for existing credentials.
