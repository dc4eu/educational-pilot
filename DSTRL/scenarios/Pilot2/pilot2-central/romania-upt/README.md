# Politehnica University of Timisoara (UPT) – pilot – issuance and verification of Micro-credentials for the E³UDRES² – Ent-r-e-novators Summer School

## scenario description

his scenario shows how Politehnica University of Timisoara issues and verifies micro-credentials for the E³UDRES² – Ent-r-e-novators PhD Summer School, part of teh E³UDRES² European Universities Alliance, of attributes (eaas) through both EBSI decentralised PKI and the Romanian national trust list managed by the Ministry of Research, Innovation and Digitalisation. the process follows **eIDAS2 article 6a**, the **eu digital identity architecture and reference framework (arf)** and connects to the **single digital gateway once‑only technical system (oots)** for PID retrieval.

## key steps per user journey

### 1. onboarding in education

* select 25 participants from UPT and European Universities Alliance in the PhD Summer School.
  * **selection criteria:** the participants completed all the activities in the program and agreed to the GDPR and the EBSI information and done the minimum training
* deliver Izertis EUDI wallets and onboarding tokens.
* verify each participant’s identity and issue credentials for PID retrieval.
* guide graduates through PID retrieval and wallet activation.
* graduates request an **EducationalId**; issuer validates PID and issues attribute.

### 2. micro-credential issuance

* student registry exports microicredential metadata from the UPT University system.
* participants review data in the wallet.
* issuer API signs and stores MC eaas in wallets.

### 3. generic eaa verification

* public verifier portal validates the micro-credential using EBSI anchoring and national trust list status.
* verifier returns machine‑readable result and a pdf receipt.

## scenario details

| element                                  | description                                                                        |
| ---------------------------------------- | ---------------------------------------------------------------------------------- |
| **scenario name**                        | micro-credential issuance and verification |
| **piloting agent**                       | Politehnica University of Timisoara |
| **end users identification**             | 10 students |
| **selection criteria**                   | E³UDRES² – Ent-r-e-novators PhD Summer School Completion |
| **eaas involved**                        | PID, EducationalID, Micro-credential |
| **institutional systems involved**       | university registry, issuer microservice, verifier portal |
| **technical components**                 | Issuer API `https://uself-issuer-gui.lspupt.upt.ro`, Verifier API `https://uself-verifier-gui.lspupt.upt.ro`, PID gateway `https://uself-pid-generator.lspupt.upt.ro`, Izertis EUDI Wallet |
| **governance setup**                     | DID registered in EBSI; qseal listed in onrc trust list |
| **feedback & monitoring mechanism**      | Survey |
| **regulatory context**                   | GDPR, eIDAS2 art 6a, arf, romanian law 455/2001 on electronic signature |
| **risk management considerations**       | identity mismatch (medium/medium), wallet loss (low/high) |
| **credential lifecycle management**      | suspension by student or registry, renewal on corrected data, revocation on data error |
| **infrastructure readiness**             | Dockerized services available in the UPT Cloud |
| **onboarding and training plan**         | wallet quick‑start PDF, short webinar |
| **progress tracking and reporting plan** | weekly dg‑eac report |
| **issue escalation procedure**           | IT service desk `helpdesk@upt.ro`, escalated to credentials lead Andra Popescu within 4 hours |
| **success metrics and kpis**             | See table below |
| **spoc contact and validation status**   | Andra Popescu, credentials lead, [a.popescu@upt.ro](mailto:a.popescu@upt.ro); compliance review 25 july 2025 |

### success metrics and kpis

| kpi                           | formula                                   | data source    | tool    | frequency | target |
| ----------------------------- | ----------------------------------------- | -------------- | ------- | --------- | ------ |
| wallet activation rate        | wallets activated ÷ wallets issued × 100  | issuer logs    | grafana | weekly    | ≥95 %  |
| micro-credentials issuance success      | mc issued ÷ requests × 100          | issuer metrics | grafana | weekly    | ≥97 %  |
| verification success          | successful verifications ÷ attempts × 100 | verifier logs  | grafana | weekly    | ≥98 %  |
| user satisfaction             | average survey score (1‑5)                | survey tool    | grafana | monthly   | ≥4.0   |
