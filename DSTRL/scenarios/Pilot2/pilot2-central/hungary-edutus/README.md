# edutus university – pilot – micro‑credential issuance post‑graduation

## scenario description

edutus university demonstrates issuance and verification of post‑graduate micro‑credential eaas to recent alumni through ebsi decentralised pki and the hungarian national trust list. flows comply with **eidas2 art 6a**, follow **arf 1.3**, and connect to the **sgd once‑only technical system** for trusted data pull.

## key steps per user journey

### 1. onboarding in education

* target 10 alumni (bachelor or master) who graduated in 2024.

  * **selection criteria:** degree conferred at edutus, gpa ≥3.5, english ≥b1.
* assign two study‐administration officers as verifiers and one it liaison.
* distribute izertis eudi wallets and onboarding codes.
* verify identity and trigger pid retrieval.
* alumni request **educationalid**; issuer validates pid and issues attribute.

### 2. micro‑credential issuance

* alumni complete a five‑hour online training on sustainable design.
* lms exports completion data; issuer signs and delivers a micro‑credential eaa.

### 3. generic eaa verification

* third‑party verifier portal validates credential integrity, ebsi anchoring and trust‑list status.

## scenario details

| element                                  | description                                                                                                               |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| **scenario name**                        | micro‑credential for alumni                                                                                               |
| **piloting agent**                       | edutus university                                                                                                         |
| **end users identification**             | 10 alumni, 2 verifiers, 1 it liaison                                                                                      |
| **selection criteria**                   | 2024 graduates, gpa ≥3.5, english ≥b1                                                                                     |
| **eaas involved**                        | pid, educationalid, micro‑credential completion                                                                           |
| **institutional systems involved**       | lms moodle, alumni registry, issuer microservice, verifier portal                                                         |
| **technical components**                 | issuer api `https://issuer.edutus.hu/v1`, verifier api `https://verify.edutus.hu/v1`, pid gateway `https://pid.gov.hu/v2` |
| **governance setup**                     | did anchored in ebsi; qseal listed in nkhi trust list                                                                     |
| **feedback & monitoring mechanism**      | in‑wallet feedback form; grafana dashboard                                                                                |
| **regulatory context**                   | gdpr, eidas2 art 6a, arf wallets chapter                                                                                  |
| **risk management considerations**       | alumni not reachable (low/medium) mitigated by email reminders                                                            |
| **credential lifecycle management**      | renewal if course updated; revocation on academic misconduct                                                              |
| **infrastructure readiness**             | docker swarm on campus; interfaces hu‑hu and en‑gb                                                                        |
| **onboarding and training plan**         | wallet quick‑start guide; webinar                                                                                         |
| **progress tracking and reporting plan** | weekly metrics to dg‑eac observers                                                                                        |
| **issue escalation procedure**           | helpdesk `support@edutus.hu`, escalated to credentials lead anna nagy                                                     |
| **success metrics and kpis**             | see table below                                                                                                           |
| **spoc contact and validation status**   | anna nagy, credentials lead, [a.nagy@edutus.hu](mailto:a.nagy@edutus.hu); review 22 june 2025                             |

### success metrics and kpis

| kpi                            | formula                                   | data source    | tool    | frequency | target |
| ------------------------------ | ----------------------------------------- | -------------- | ------- | --------- | ------ |
| wallet activation rate         | wallets activated ÷ wallets issued × 100  | issuer logs    | grafana | weekly    | ≥90 %  |
| micro‑credential issuance rate | eaas issued ÷ participants × 100          | issuer metrics | grafana | weekly    | ≥95 %  |
| verification success rate      | successful verifications ÷ attempts × 100 | verifier logs  | grafana | weekly    | ≥98 %  |
| satisfaction                   | avg survey score (1‑5)                    | survey         | grafana | monthly   | ≥4.2   |
| incident resolution time       | avg hours                                 | helpdesk       | grafana | monthly   | ≤24 h  |
