# universidade do porto (uporto) – pilot – student onboarding and diploma issuance

## scenario description

uporto pilots wallet‑based student onboarding for 25 first‑time students and subsequent diploma issuance. flows comply with **eidas2**, **arf**, **portuguese decree‑law 12/2025** and connect to **sgd/oots** data pull.

## key steps per user journey

### 1. student enrolment

* pick 25 incoming students.
* provide eudi wallets, pid retrieval via cartão de cidadão mobile.
* students execute onboarding process; issuer issues educationalid.

### 2. diploma issuance

* after scenario evaluation, registry exports diploma; issuer signs and delivers eaa.

### 3. verification

* employer verifies via public portal.

## scenario details

| element                                  | description                                                                |
| ---------------------------------------- | -------------------------------------------------------------------------- |
| **scenario name**                        | wallet onboarding and diploma                                              |
| **piloting agent**                       | universidade do porto                                                      |
| **end users identification**             | 25 students                                                                |
| **selection criteria**                   | new entrants 2025/26                                                       |
| **eaas involved**                        | pid, educationalid, diploma                                                |
| **institutional systems involved**       | sigarra, issuer, verifier                                                  |
| **technical components**                 | issuer `https://issuer.up.pt/v1`                                           |
| **governance setup**                     | did ebsi; qseal gns                                                        |
| **feedback & monitoring mechanism**      | survey                                                                     |
| **regulatory context**                   | gdpr, eidas2, dl 12/2025                                                   |
| **risk management considerations**       | onboarding failure                                                         |
| **credential lifecycle management**      | revocation on dropout                                                      |
| **infrastructure readiness**             | kubernetes                                                                 |
| **onboarding and training plan**         | orientation session                                                        |
| **progress tracking and reporting plan** | fortnightly updates                                                        |
| **issue escalation procedure**           | [suporte@up.pt](mailto:suporte@up.pt)                                      |
| **success metrics and kpis**             | below                                                                      |
| **spoc contact and validation status**   | sofia santos, [s.santos@up.pt](mailto:s.santos@up.pt); review 22 july 2025 |

### success metrics and kpis

| kpi                | formula                   | source | tool    | frequency | target |
| ------------------ | ------------------------- | ------ | ------- | --------- | ------ |
| onboarding success | completed ÷ invited × 100 | issuer | grafana | weekly    | ≥92 %  |
