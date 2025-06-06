# universidad de alcalá (uah) – pilot – digital student id and achievement issuance

## scenario description

uah demonstrates issuance and verification of electronic attestations of attributes (eaas) for student status and academic achievement using ebsi pki and spanish trust lists. the flow follows **eidas2 art 6a**, **arf 1.3**, and integrates with the **once‑only technical system (oots)** under the **single digital gateway** regulation.

## key steps per user journey

### 1. onboarding in education

* select 25 final‑year students.

  * **selection criteria:** ≥180 ects, spanish dni, languages es‑es or en‑gb, inclusive.
* deliver izertis eudi wallet and onboarding token.
* verify identity and assist pid retrieval via `micarte.gob.es`.
* students request **educationalid** and receive attribute after enrolment confirmation.

### 2. educational achievement issuance

* lms exports thesis grade and honours list; issuer signs and stores achievement eaas.

### 3. generic eaa verification

* employer or university verifies eaas via public portal.

## scenario details

| element                                  | description                                                                                         |
| ---------------------------------------- | --------------------------------------------------------------------------------------------------- |
| **scenario name**                        | digital student id and achievements                                                                 |
| **piloting agent**                       | universidad de alcalá                                                                               |
| **end users identification**             | 25 students, 3 registry verifiers, 1 it engineer                                                    |
| **selection criteria**                   | final year, dni, language es/en                                                                     |
| **eaas involved**                        | pid, educationalid, degree achievement                                                              |
| **institutional systems involved**       | sigm@, idp, issuer, verifier                                                                        |
| **technical components**                 | issuer `https://issuer.uah.es/v1`, verifier `https://verify.uah.es/v1`, pid `https://pid.gob.es/v2` |
| **governance setup**                     | dids registered in ebsi; qseal in boe trust list                                                    |
| **feedback & monitoring mechanism**      | wallet survey; grafana                                                                              |
| **regulatory context**                   | gdpr, eidas2, arf, loo 3/2018                                                                       |
| **risk management considerations**       | identity theft (low/high)                                                                           |
| **credential lifecycle management**      | revocation on withdrawal                                                                            |
| **infrastructure readiness**             | kubernetes; interfaces es‑es/en‑gb                                                                  |
| **onboarding and training plan**         | webinar                                                                                             |
| **progress tracking and reporting plan** | weekly dg‑eac report                                                                                |
| **issue escalation procedure**           | ict desk `soporte@uah.es`                                                                           |
| **success metrics and kpis**             | below                                                                                               |
| **spoc contact and validation status**   | maría lópez, [m.lopez@uah.es](mailto:m.lopez@uah.es); review 12 july 2025                           |

### success metrics and kpis

| kpi               | formula                 | source | tool    | frequency | target |
| ----------------- | ----------------------- | ------ | ------- | --------- | ------ |
| wallet activation | activated ÷ issued ×100 | issuer | grafana | weekly    | ≥95 %  |
| issuance success  | issued ÷ requested ×100 | issuer | grafana | weekly    | ≥97 %  |
