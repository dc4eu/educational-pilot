# università di bologna (unibo) – pilot – bachelor diploma eaa

## scenario description

unibo issues bachelor diploma electronic attestations of attributes (eaas) to 25 final‑year students via ebsi pki and italian agid trust list. alignment with **eidas2 art 6a**, **arf** and the **italian digital administration code**.

## key steps per user journey

### 1. onboarding

* choose 25 students.
* wallet distribution, pid retrieval, educationalid issuance.

### 2. diploma issuance

* almaesami system exports degree; issuer signs and stores diploma eaa.

### 3. verification

* verifier portal checks credential integrity and issuer status.

## scenario details

| element                                  | description                                                                        |
| ---------------------------------------- | ---------------------------------------------------------------------------------- |
| **scenario name**                        | bachelor diploma eaa                                                               |
| **piloting agent**                       | università di bologna                                                              |
| **end users identification**             | 25 students                                                                        |
| **selection criteria**                   | graduation july 2025                                                               |
| **eaas involved**                        | pid, educationalid, diploma eaa                                                    |
| **institutional systems involved**       | almaesami, issuer, verifier                                                        |
| **technical components**                 | issuer `https://issuer.unibo.it/v1`                                                |
| **governance setup**                     | did ebsi; qseal agid                                                               |
| **feedback & monitoring mechanism**      | survey                                                                             |
| **regulatory context**                   | gdpr, eidas2, cad                                                                  |
| **risk management considerations**       | diploma data error                                                                 |
| **credential lifecycle management**      | revocation on correction                                                           |
| **infrastructure readiness**             | unibo cloud                                                                        |
| **onboarding and training plan**         | workshops                                                                          |
| **progress tracking and reporting plan** | monthly report                                                                     |
| **issue escalation procedure**           | [help@unibo.it](mailto:help@unibo.it)                                              |
| **success metrics and kpis**             | below                                                                              |
| **spoc contact and validation status**   | luca rinaldi, [l.rinaldi@unibo.it](mailto:l.rinaldi@unibo.it); review 20 july 2025 |

### success metrics and kpis

| kpi              | formula                 | source | tool    | frequency | target |
| ---------------- | ----------------------- | ------ | ------- | --------- | ------ |
| diploma issuance | issued ÷ students × 100 | issuer | grafana | weekly    | ≥98 %  |
 