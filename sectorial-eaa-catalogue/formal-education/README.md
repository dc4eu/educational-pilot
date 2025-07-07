# Formal Education

## Overview

This section contains data models and schemas for representing formal educational qualifications within the European Educational and Professional Qualifications framework. These models provide standardised formats for credentials issued by recognised educational institutions, enabling interoperability and recognition across the European education area.

Data models and schemas for representing formal educational qualifications:

- Diploma credentials
- Degree certificates
- Microcredentials for HE & VET
- Transcripts of records
- Course certificates
- Learning agreements

## Credential Types

### Diploma Credentials

Diploma credentials represent the formal completion of an educational programme at a specific level. Our schemas support:

- Bachelor's degrees
- Master's degrees
- Doctoral degrees
- Professional diplomas
- Vocational qualifications

EAA's defined
- [Higher Education Diploma](./business/EUHED-highereducation-diploma_business.md)
- [Higher Education Diploma Supplement](./business/EUHEDS-highereducation-diplomasupplement_business.md) 
- [Higher Edcuation Master Degree](./business/EUHED-highereducation-diploma_business.md)
- [Higher Edcuation Transcript of Records](./business/EUHETOR-highereducation-transcriptofrecords_business.md)

For detailed schema information, see [Diploma Schema](./schemes/EUHED-EuropeanHigherEducationDiploma.json) covering Bachelor, Master.

### Degree Certificates

Degree certificates provide formal recognition of educational achievements. Our schemas support:

- Academic degrees
- Professional certifications
- Programme completion certificates
- Institutional certificates

EAA's defined
- [Higher Education Proof of Enrolment](./business/EUHEPOE-highereducation-proofofenrolment_business.md)

For detailed schema information, see [Degree Certificate Schema](./schemes/EUHEPOE-EuropeanHigherEducationProofOfEnrolment.json).

### Transcripts of Records

Transcripts document the courses taken and results achieved during an educational programme. Our schemas support:

- Course listings
- Grade records
- Credit achievements
- Learning outcome attainment
- Programme progression

EAA's defined
- [Higher Education Transcript of Records](./business/EUHETOR-highereducation-transcriptofrecords_business.md)
  
For detailed schema information, see [Transcript Schema](./schemes/EUHETOR-EuropeanHigherEducationTranscriptOfRecords.json).

### Microcredentials in Higher Education

Microcredentials attest to the achievement of specific learning outcomes following a short learning experience. Our schemas support:

- University microcredentials
- Short learning programmes with ECTS credits
- EQF-aligned certifications
- Learning outcomes with ESCO skills alignment
- Quality-assured short credentials

EAA's defined
- [Higher Education Microcredential ](./business/EUHEMC-highereducation-microcredential_business.md)

For detailed schema information, see [Microcredential HE Schema](./schemes/EUHEMC-EuropeanHigherEducationMicrocredential.json).

### Educational Identifiers

Educational identifiers provide verifiable proof of student status. Our schemas support:

- Student identification
- Institutional affiliation
- Programme enrolment
- Academic status
- Access rights

EAA's defined
For detailed schema information, see [Educational ID Schema](../non-foundational-id/educational-id-schema.md).

### Course Certificates

Course certificates document completion of specific educational components. Our schemas support:

- Individual course completion
- Module achievements
- Short programme completion
- Professional development courses
- Specialised training

EAA's defined
- [Upper Secondary Education Transcript of Records](./business/EUUSTOR-uppersecondaryeducation-transcriptofrecords_business.md)

For detailed schema information, see [Course Certificate Schema](./schemes/EUUSTOR-EuropeanUpperSecondaryEducationTranscriptOfRecords.json).


## Implementation and Integration

These schemas are designed to:

- Align with the European Learning Model (ELM)
- Support W3C Verifiable Credentials standards
- Enable multi-language credential representation
- Facilitate qualification recognition across borders
- Integrate with national qualification frameworks
- Support European Qualification Framework (EQF) levels

## Usage in User Journeys

These formal education schemas support key user journeys including:

- University application with verified prior qualifications
- Student mobility between European institutions
- Employment verification of educational achievements
- Professional licensing based on formal qualifications
- Continued education and lifelong learning pathways
- Microcredential stacking into larger qualifications

## Examples

- [Certificate of participation](../formal-education/examples/certificate-of-participation.md)
- [Transcript of records](../formal-education/examples/transcript-of-records.md)
- [Joint degree](../formal-education/examples/joint-degree.md)
- [Master degree](../formal-education/examples/master-degree.md)

## Versioning

All schemas follow a consistent versioning pattern:
- Major versions for breaking changes
- Minor versions for feature additions
- Patch versions for corrections

Current version: 1.0.0
