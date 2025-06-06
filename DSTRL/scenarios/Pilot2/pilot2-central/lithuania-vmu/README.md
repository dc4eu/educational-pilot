# vytautas magnus university (vmu) – pilot – first‑time onboarding and diploma issuance

## scenario description

vytautas magnus university pilots wallet‑based onboarding of 25 students and subsequent diploma issuance, compliant with **eidas2**, the **arf**, and lithuanian **law 30/2024 on digital identity**. pid retrieval uses the national e‑identity gateway `eid-gateway.lt`.

## key steps per user journey

### 1. student enrolment

* select 25 new students joining in academic year 2025‑26.

  * **selection criteria:** lithuanian personal id, english ≥b1.
* provide litwallet and activation code.
* verify identity and retrieve pid via `eid-gateway.lt`.
* students receive **educationalid** confirming enrolment.

### 2. diploma issuance

* after completion the lsp registry exports diploma data.
* issuer signs and stores diploma eaas in wallets.

### 3. generic eaa verification

* employer uses verifier portal; portal validates the credential.

## scenario details

| element                                  | description                                                                                                                        |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| **scenario name**                        | onboarding and diploma issuance                                                                                                    |
| **piloting agent**                       | vytautas magnus university                                                                                                         |
| **end users identification**             | 25 students, 2 registrar staff, 1 it engineer                                                                                      |
| **selection criteria**                   | new entrants 2025‑26, lithuanian id                                                                                                |
| **eaas involved**                        | pid, educationalid, diploma                                                                                                        |
| **institutional systems involved**       | lsp registry, idp, issuer, verifier                                                                                                |
| **technical components**                 | issuer api `https://issuer.vmu.lt/v1`, verifier api `https://verify.vmu.lt/v1`, pid gateway `https://eid-gateway.lt/v2`, litwallet |
| **governance setup**                     | did registered in ebsi; qseal in regolith trust list                                                                               |
| **feedback & monitoring mechanism**      | moodle questionnaire; grafana                                                                                                      |
| **regulatory context**                   | gdpr, eidas2, arf, lt law 30/2024                                                                                                  |
| **risk management considerations**       | pid retrieval failure (low/high)                                                                                                   |
| **credential lifecycle management**      | revocation on dropout, renewal on updated data                                                                                     |
| **infrastructure readiness**             | openstack cluster, interfaces lt‑lt and en‑gb                                                                                      |
| **onboarding and training plan**         | orientation session                                                                                                                |
| **progress tracking and reporting plan** | fortnightly reports to dg‑eac                                                                                                      |
| **issue escalation procedure**           | helpdesk `it@vmu.lt`                                                                                                               |
| **success metrics and kpis**             | see table below                                                                                                                    |
| **spoc contact and validation status**   | lina kazlauskienė, [l.kazlauskiene@vmu.lt](mailto:l.kazlauskiene@vmu.lt); review 30 july 2025                                      |

### success metrics and kpis

| kpi                      | formula                     | source   | tool    | frequency | target |
| ------------------------ | --------------------------- | -------- | ------- | --------- | ------ |
| onboarding success       | completed ÷ invited × 100   | issuer   | grafana | weekly    | ≥92 %  |
| diploma issuance success | issued ÷ eligible × 100     | issuer   | grafana | weekly    | ≥98 %  |
| verification success     | successful ÷ attempts × 100 | verifier | grafana | weekly    | ≥98 %  |
| satisfaction             | avg survey score (1‑5)      | survey   | grafana | monthly   | ≥4.0   |
