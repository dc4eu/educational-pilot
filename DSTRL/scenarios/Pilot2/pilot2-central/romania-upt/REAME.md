# politehnica university of timisoara (upt) – pilot – graduate diploma issuance and verification

## scenario description

this scenario shows how politehnica university of timisoara issues and verifies graduate diploma electronic attestations of attributes (eaas) through both ebsi decentralised pki and the romanian national trust list managed by the ministry of research, innovation and digitalisation. the process follows **eidas2 article 6a**, the **eu digital identity architecture and reference framework (arf)** and connects to the **single digital gateway once‑only technical system (oots)** for pid retrieval.

## key steps per user journey

### 1. onboarding in education

* select 10 bsc graduates from upt.

  * **selection criteria:** diploma awarded after 1 february 2025, romanian and english at b2, inclusive accessibility.
* deliver izertis eudi wallets and onboarding tokens.
* verify each graduate’s identity and issue credentials for pid retrieval.
* guide graduates through pid retrieval and wallet activation.
* graduates request an **educationalid**; issuer validates pid and issues attribute.

### 2. diploma issuance

* student registry exports diploma metadata from the universitario system.
* graduates review data in the wallet.
* issuer api signs and stores diploma eaas in wallets.

### 3. generic eaa verification

* public verifier portal validates the diploma using ebsi anchoring and national trust list status.
* verifier returns machine‑readable result and a pdf receipt.

## scenario details

| element                                  | description                                                                                                                             |
| ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| **scenario name**                        | graduate diploma issuance and verification                                                                                              |
| **piloting agent**                       | politehnica university of timisoara                                                                                                     |
| **end users identification**             | 10 graduates, 2 registry officers, 1 it engineer                                                                                        |
| **selection criteria**                   | bsc diploma 2025, romanian id, english ≥b2                                                                                              |
| **eaas involved**                        | pid, educationalid, bachelor diploma                                                                                                    |
| **institutional systems involved**       | universitario registry, upt idp, issuer microservice, verifier portal                                                                   |
| **technical components**                 | issuer api `https://issuer.upt.ro/v1`, verifier api `https://verify.upt.ro/v1`, pid gateway `https://pid.gov.ro/v2`, izertis wallet sdk |
| **governance setup**                     | did registered in ebsi; qseal listed in onrc trust list                                                                                 |
| **feedback & monitoring mechanism**      | in‑wallet survey, grafana dashboard                                                                                                     |
| **regulatory context**                   | gdpr, eidas2 art 6a, arf, romanian law 455/2001 on electronic signature                                                                 |
| **risk management considerations**       | identity mismatch (medium/medium), wallet loss (low/high)                                                                               |
| **credential lifecycle management**      | suspension by student or registry, renewal on corrected data, revocation on academic misconduct                                         |
| **infrastructure readiness**             | kubernetes cluster on campus, hsm for key custody, interfaces ro‑ro and en‑gb                                                           |
| **onboarding and training plan**         | wallet quick‑start pdf, short webinar                                                                                                   |
| **progress tracking and reporting plan** | weekly metrics emailed to dg‑eac observers                                                                                              |
| **issue escalation procedure**           | it service desk `helpdesk@upt.ro`, escalated to credentials lead andra popescu within 4 hours                                           |
| **success metrics and kpis**             | see table below                                                                                                                         |
| **spoc contact and validation status**   | andra popescu, credentials lead, [a.popescu@upt.ro](mailto:a.popescu@upt.ro); compliance review 25 july 2025                            |

### success metrics and kpis

| kpi                           | formula                                   | data source    | tool    | frequency | target |
| ----------------------------- | ----------------------------------------- | -------------- | ------- | --------- | ------ |
| wallet activation rate        | wallets activated ÷ wallets issued × 100  | issuer logs    | grafana | weekly    | ≥95 %  |
| diploma issuance success      | diplomas issued ÷ requests × 100          | issuer metrics | grafana | weekly    | ≥97 %  |
| verification success          | successful verifications ÷ attempts × 100 | verifier logs  | grafana | weekly    | ≥98 %  |
| user satisfaction             | average survey score (1‑5)                | survey tool    | grafana | monthly   | ≥4.0   |
| mean incident resolution time | avg hours ticket open to close            | helpdesk       | grafana | monthly   | ≤24 h  |
