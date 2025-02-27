# Educational Pilot

## 1 About

This repository is created for describing the details associated to Educational Credentials and Professional Qualifications Pilot.
It covers the high level technical architecture, lists the main components from core technical infrastructure with pointers to their descriptions, describes through RFCs the basic operations (workflows) implemented by the system as well as the specific use cases approved for the pilot. Details about EBSI Wallet Compliance tests are provided as well as Deployment instructions and license related to this documentation.

## 2 Architecture

The following diagrams show a high level detail of the different core technical infrastructure components to be deployed within the Educational Credentials and Professional Qualifications Pilot (dPKI profile).

![image](docs/images/Architecture.png)

### 2.1 Components description

- Keycloak: tbd
- Status Web GUI: tbd
- PID Generator GUI: tbd
- Student Web GUI: tbd
- Issuer Agent: tbd
- Authentic Source: tbd
- Izertis Holder Wallet (mobile app): tbd
- EUDI Wallet (mobile app): tbd

## 3 Basic Building blocks

The basic operations implemented by the system are gathered in a RFCs format. The following section is devoted for describing them.

### 3.1.1 Approved RFCs

These are the approved RFCs identified. 

| **RFC #** | **RFC Title**                                                                                                |
| --------- | ------------------------------------------------------------------------------------------------------------ |
| RFC-001   | [Issue Verifiable Credentials Workflow - v1.0](docs/rfc001-issue-verifiable-credential.md)                   |
| RFC-002   | [Present Verifiable Credentials Workflow - v1.0](docs/rfc002-present-verifiable-credential.md)               |

#### 3.1.2 Candidate RFCs (Work in progress)

Following are the candidates' RFCs taken up. Note that the title, etc, may change.

| **RFC #** | **RFC Title**                                                                               |
| --------- | ------------------------------------------------------------------------------------------- |
| RFC-003   | [To be defined](docs/rfc003-to-be-defined.md) |


## 4 Use Cases by project

For each of the different projects where uSelf has been applied, some specific use cases have been identified. This section is devoted for providing a view of those specific uses cases by project.

### 4.1 DC4EU

#### 4.1.1 Approved Use Cases

These are the approved use cases identified in DC4EU for applying in the Educational Pilot

| **Use Case #** | **Use Case Title**                                                                                           |
| -------------- | ------------------------------------------------------------------------------------------------------------ |
| DC4EU-001      | [Issue EducationalId using a PID for authentication - v1.0](docs/dc4eu/dc4eu-001-issue-eudcationalId.md)     |
| DC4EU-002      | [Issue a Diploma using a EducationalId for authentication - v1.0](docs/dc4eu/dc4eu-002-issue-diploma.md)        |
| DC4EU-003      | [Verify EducationalId for authentication - v1.0](docs/dc4eu/dc4eu-003-verify-diploma.md)                  |

#### 4.1.2 Candidate Use Cases (Work in progress)

Following are the candidates'Use cases taken up. Note that the title, etc, may change.

| **Use Case #** | **Use Case Title**                                                                                           |
| -------------- | ------------------------------------------------------------------------------------------------------------ |
| DC4EU-004      | [Issue a PID - v1.0](docs/dc4eu/dc4eu-004-issue-pid.md)                                                      |





## uSelf Compliance Test

Ledger uSelf is compliant with EBSI wallet compliance tests in order to assure the interoperability with other issuer, verifier and wallet solutions.
(Add mention to Izertis wallet)
### EUDI Wallet Compliance Test
(This section needs to defined)
### EBSI Compliance Test

| Tool |Version | Holder | Issuer | Verifier | Trust Model |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------                   | :----: | :----: | :------:|:------: |
| uself-agent            | v0.0.3 |   ✅   |   ✅    |  ✅     |  ✅     |
(To be added Izertis Wallet EBSI compliance)

### 5 Deployment
(TBD)

## Notice

The content in this repository is copyrighted by ATOS Spain S.A. (hereinafter referred to as ATOS or EVIDEN) unless otherwise specified. The information in this repository can only be used by the beneficiaries of the EU funded DC4EU Project and only for the purposes of the integration activities of this project, and that any other use is forbidden unless accepted in writing by ATOS. For more information please refer to the
license below.

## License
Copyright Notice Copyright © 2025 ATOS Spain S.A. (hereinafter referred to as "Atos" or "EVIDEN"). All rights reserved. Unauthorized use of this content, beyond the permissions specified in this license, without the prior written consent of Atos/EVIDEN is strictly prohibited. Authorized Use This content is authorized to the beneficiaries of the DC4EU project (European Commission’s Grant Agreement 101102611) solely for integration activities. Any other use, including reproduction, modification, distribution, or sharing with third parties, is forbidden without prior written authorization from Atos/EVIDEN. Confidentiality The content in this repository is marked as CONFIDENTIAL and is intended exclusively for internal use by DC4EU project partners. Disclosure or use of this content outside of the project requires explicit written consent from Atos/EVIDEN. Duration of Access Access to this repository is granted for the duration of the DC4EU Project. Upon the project’s conclusion, access will be terminated unless otherwise agreed upon in writing. Additionally, all Confidential Information that has been stored by the beneficiaries must be erased or destroyed.
