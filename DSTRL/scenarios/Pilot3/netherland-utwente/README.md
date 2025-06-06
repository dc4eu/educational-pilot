# university of twente (utwente) – pilot – diploma issuance and wallet authentication

## scenario description

university of twente tests wallet‑based diploma issuance and verification together with wallet authentication for a campus application. the pilot observes **eidas2**, the **arf**, and interfaces with the dutch once‑only infrastructure under the **single digital gateway**.

## key steps per user journey

### 1. onboarding

* recruit 25 participants (students or employees).

  * **selection criteria:** active university account, digid, english ≥b2.
* distribute eudi wallets and activation codes.
* verify identity with digid and retrieve pid.
* participants request **educationalid** credential.

### 2. diploma issuance

* the osiris registry exports diploma data.
* participant selects diploma in wallet; issuer signs and delivers diploma eaa.

### 3. application access with wallet authentication

* campus portal sends didcomm request.
* participant presents educationalid; portal validates and grants access.

### 4. generic eaa verification

* third‑party verifier portal validates the diploma.

## scenario details

| element                                  | description                                                                                                                                     |
| ---------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| **scenario name**                        | diploma issuance and wallet authentication                                                                                                      |
| **piloting agent**                       | university of twente                                                                                                                            |
| **end users identification**             | 25 participants, 3 registry officers, 2 it engineers                                                                                            |
| **selection criteria**                   | active utwente id, digid, english ≥b2                                                                                                           |
| **eaas involved**                        | pid, educationalid, diploma                                                                                                                     |
| **institutional systems involved**       | osiris, keycloak idp, issuer, verifier, campus portal                                                                                           |
| **technical components**                 | issuer api `https://issuer.utwente.nl/v1`, verifier api `https://verify.utwente.nl/v1`, pid gateway `https://digid.nl/pid/v2`, dutch wallet sdk |
| **governance setup**                     | did anchored in ebsi; qseal in logius trust list                                                                                                |
| **feedback & monitoring mechanism**      | limesurvey after each flow; grafana dashboards                                                                                                  |
| **regulatory context**                   | gdpr, eidas2, arf, dutch higher education act                                                                                                   |
| **risk management considerations**       | digid outage (low/medium), credential mismatch (medium/medium)                                                                                  |
| **credential lifecycle management**      | revocation on error, renewal on updates                                                                                                         |
| **infrastructure readiness**             | openshift cluster, interfaces nl‑nl and en‑gb                                                                                                   |
| **onboarding and training plan**         | online tutorial                                                                                                                                 |
| **progress tracking and reporting plan** | weekly sync with ministry of education                                                                                                          |
| **issue escalation procedure**           | servicedesk `ict@utwente.nl`, escalate to credentials lead tom jansen                                                                           |
| **success metrics and kpis**             | see table below                                                                                                                                 |
| **spoc contact and validation status**   | tom jansen, [t.jansen@utwente.nl](mailto:t.jansen@utwente.nl); review 28 july 2025                                                              |

### success metrics and kpis

| kpi                       | formula                             | source      | tool    | frequency | target |
| ------------------------- | ----------------------------------- | ----------- | ------- | --------- | ------ |
| wallet activation         | activated ÷ issued × 100            | issuer      | grafana | weekly    | ≥95 %  |
| diploma issuance          | issued ÷ requested × 100            | issuer      | grafana | weekly    | ≥97 %  |
| vc authentication success | successful vc auth ÷ attempts × 100 | portal logs | grafana | daily     | ≥98 %  |
| verification success      | successful ÷ attempts × 100         | verifier    | grafana | weekly    | ≥98 %  |
| incident resolution time  | avg hours                           | helpdesk    | grafana | monthly   | ≤24 h  |
