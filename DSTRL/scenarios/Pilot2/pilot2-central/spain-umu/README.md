# universidad de murcia (umu) – pilot – wallet login to virtual campus

## scenario description

umu enables 20 undergraduate students to access its virtual campus using eaas from eudi wallet. the pilot adheres to **eidas2**, **arf** and **european education area** digital targets.

## key steps per user journey

### 1. onboarding

* pick 20 students.
* issue wallets, retrieve pid, educationalid.

### 2. virtual campus access

* moodle plugin requests educationalid; wallet returns proof; plugin validates.

## scenario details

| element                                  | description                                                             |
| ---------------------------------------- | ----------------------------------------------------------------------- |
| **scenario name**                        | wallet login to campus                                                  |
| **piloting agent**                       | universidad de murcia                                                   |
| **end users identification**             | 20 students                                                             |
| **selection criteria**                   | first year                                                              |
| **eaas involved**                        | pid, educationalid                                                      |
| **institutional systems involved**       | moodle, issuer, verifier                                                |
| **technical components**                 | plugin, issuer `https://issuer.umu.es/v1`                               |
| **governance setup**                     | did ebsi                                                                |
| **feedback & monitoring mechanism**      | moodle survey                                                           |
| **regulatory context**                   | gdpr, eidas2                                                            |
| **risk management considerations**       | login failure                                                           |
| **credential lifecycle management**      | n/a                                                                     |
| **infrastructure readiness**             | on‑prem cluster                                                         |
| **onboarding and training plan**         | pdf guide                                                               |
| **progress tracking and reporting plan** | weekly stats                                                            |
| **issue escalation procedure**           | [support@umu.es](mailto:support@umu.es)                                 |
| **success metrics and kpis**             | below                                                                   |
| **spoc contact and validation status**   | ana pérez, [a.perez@umu.es](mailto:a.perez@umu.es); review 18 july 2025 |

### success metrics and kpis

| kpi                  | formula                  | source | tool    | frequency | target |
| -------------------- | ------------------------ | ------ | ------- | --------- | ------ |
| wallet login success | success ÷ attempts × 100 | logs   | grafana | weekly    | ≥97 %  |
