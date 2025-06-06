# universidad carlos iii de madrid (uc3m) – pilot – vc authentication in virtual campus

## scenario description

uc3m integrates verifiable credential authentication into its virtual campus (lms) to let 20 students log in using eaas from their eudi wallets. flow meets **eidas2**, **arf**, and supports **sgd/oots** interoperability.

## key steps per user journey

### 1. onboarding

* integrate vc auth plugin into lms.
* recruit 20 students enrolled in ‘data science’ course.
* students receive wallets, retrieve pid, request educationalid.

### 2. accessing virtual campus

* lms presents didcomm request; student signs and returns educationalid.
* lms checks verifier service and grants session.

## scenario details

| element                                  | description                                                                              |
| ---------------------------------------- | ---------------------------------------------------------------------------------------- |
| **scenario name**                        | vc auth for lms                                                                          |
| **piloting agent**                       | universidad carlos iii de madrid                                                         |
| **end users identification**             | 20 students, 2 admins                                                                    |
| **selection criteria**                   | enrolled in data science course                                                          |
| **eaas involved**                        | pid, educationalid                                                                       |
| **institutional systems involved**       | blackboard lms, issuer, verifier                                                         |
| **technical components**                 | vc auth plugin, issuer `https://issuer.uc3m.es/v1`, verifier `https://verify.uc3m.es/v1` |
| **governance setup**                     | did registered in ebsi                                                                   |
| **feedback & monitoring mechanism**      | in‑lms questionnaire                                                                     |
| **regulatory context**                   | gdpr, eidas2                                                                             |
| **risk management considerations**       | login failure (medium/low)                                                               |
| **credential lifecycle management**      | logout revokes session token                                                             |
| **infrastructure readiness**             | lms cloud cluster                                                                        |
| **onboarding and training plan**         | video tutorial                                                                           |
| **progress tracking and reporting plan** | daily auth stats                                                                         |
| **issue escalation procedure**           | it desk                                                                                  |
| **success metrics and kpis**             | below                                                                                    |
| **spoc contact and validation status**   | javier garcía, [j.garcia@uc3m.es](mailto:j.garcia@uc3m.es); review 15 july 2025          |

### success metrics and kpis

| kpi                | formula                                   | source   | tool   | frequency | target |
| ------------------ | ----------------------------------------- | -------- | ------ | --------- | ------ |
| successful vc auth | successful vc auth ÷ total attempts × 100 | lms logs | kibana | daily     | ≥98 %  |
