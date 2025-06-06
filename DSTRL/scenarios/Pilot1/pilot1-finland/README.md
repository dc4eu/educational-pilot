# finnish national agency for education (oph) – pilot – pid driven degree issuance

## scenario description

the finnish national agency for education pilots pid retrieval and degree issuance via the national issuance service and an arf‑compliant eudi wallet built by the digital and population data services agency (dvv). credentials are verified through the dvv national simulator. the scenario aligns with **eidas2 art 6a**, the **sig‑standardisation act 619/2024** and integrates with the national suomi.fi identification service as a practical instance of **sgd/oots**.

## key steps per user journey

### 1. onboarding in wallet and pid

* recruit 25 professionals from oph and a partnering higher education institution.
* distribute dvv eudi wallets and guide users through pid retrieval using suomi.fi e‑identification (face recognition + mobile id).

### 2. degree issuance

* users request degree data via wallet -> my studyinfo.
* my studyinfo extracts data from the virkailija opintopolku registry.
* user confirms selected achievements; issuer signs and stores eaas in the wallet.

### 3. using pid information

* user accesses the higher education application portal.
* portal extracts pid from wallet presentation, stores it, and pre‑fills personal details.

## scenario details

| element                                  | description                                                                                                                             |
| ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| **scenario name**                        | pid backed degree issuance                                                                                                              |
| **piloting agent**                       | finnish national agency for education (oph) with dvv                                                                                    |
| **end users identification**             | 25 professionals                                                                                                                        |
| **selection criteria**                   | oph staff or he professionals, finnish personal id, Finnish/Swedish language                                                            |
| **eaas involved**                        | pid, degree eaa                                                                                                                         |
| **institutional systems involved**       | studyinfo registry, dvv pid gateway, suomi.fi idp, issuer and verifier services                                                         |
| **technical components**                 | issuer api `https://issuer.dvv.fi/v1`, verifier api `https://verify.dvv.fi/v1`, pid retrieval `https://pid.suomi.fi/v2`, dvv wallet sdk |
| **governance setup**                     | did anchored in ebsi; qseal in valtuudet trust list                                                                                     |
| **feedback & monitoring mechanism**      | national feedback service; grafana dashboards                                                                                           |
| **regulatory context**                   | gdpr, eidas2 art 6a, act 619/2024, arf                                                                                                  |
| **risk management considerations**       | pid retrieval failure (low/high) mitigated by helpdesk fallback                                                                         |
| **credential lifecycle management**      | revocation on user request; renewal on degree correction                                                                                |
| **infrastructure readiness**             | kubernetes in dvv data centre, siaf certified                                                                                           |
| **onboarding and training plan**         | wallet how‑to videos; faq portal                                                                                                        |
| **progress tracking and reporting plan** | monthly report to dg‑empl                                                                                                               |
| **issue escalation procedure**           | dvv service desk 24/7, escalation to project lead juha laakso                                                                           |
| **success metrics and kpis**             | see below                                                                                                                               |
| **spoc contact and validation status**   | juha laakso, [juha.laakso@oph.fi](mailto:juha.laakso@oph.fi); review 30 june 2025                                                       |

### success metrics and kpis

| kpi                       | formula                                  | data source | tool    | frequency | target |
| ------------------------- | ---------------------------------------- | ----------- | ------- | --------- | ------ |
| pid retrieval success     | successful pid ÷ attempts × 100          | idp logs    | grafana | weekly    | ≥95 %  |
| degree issuance rate      | degrees issued ÷ requests × 100          | issuer      | grafana | weekly    | ≥97 %  |
| pid reuse in applications | applications with pid ÷ total apps × 100 | studyinfo   | grafana | monthly   | ≥85 %  |
