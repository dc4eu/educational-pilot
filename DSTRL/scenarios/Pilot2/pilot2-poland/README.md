# polish universities consortium – pilot – multi‑institution degree verification

## scenario description

a consortium of three polish universities (uniwersytet warszawski, politechnika wrocławska, agh kraków) collaborates to pilot cross‑institution degree issuance and verification using ebsi pki and the national trust list managed by nccert. the pilot references **eidas2**, the **arf**, and links to the **sgd/oots** gateway under ministerial project govtech 2030.

## key steps per user journey

### 1. onboarding

* select 30 master graduates (10 per university).
* criteria: degree conferred after 1 march 2025, polish language competence, no outstanding fees.
* universities issue wallets (öwallet fork) and assist in pid retrieval through m‑ob citizen id.

### 2. degree issuance

* university registries export diploma metadata; issuer signs and issues degree eaas.

### 3. cross‑institution verification

* employer verifies degree presented from wallet; verifier checks issuer anchoring and returns proof.

## scenario details

| element                                  | description                                                                                          |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| **scenario name**                        | polish joint degree verification                                                                     |
| **piloting agent**                       | uw, pw, agh consortium                                                                               |
| **end users identification**             | 30 graduates, 6 registry officers, 3 it engineers                                                    |
| **selection criteria**                   | 2025 master graduates, polish id                                                                     |
| **eaas involved**                        | pid, educationalid, master degree                                                                    |
| **institutional systems involved**       | usos, jsos, agh‑srs, issuer, verifier                                                                |
| **technical components**                 | issuer `https://issuer.edu.pl/v1`, verifier `https://verify.edu.pl/v1`, pid `https://m‑ob.gov.pl/v2` |
| **governance setup**                     | dids registered in ebsi; qseal in nccert trust list                                                  |
| **feedback & monitoring mechanism**      | jira service management feedback                                                                     |
| **regulatory context**                   | gdpr, eidas2, polish act on higher education art 343                                                 |
| **risk management considerations**       | credential mismatch between systems (medium/medium)                                                  |
| **credential lifecycle management**      | revocation via national diploma registry                                                             |
| **infrastructure readiness**             | university dc docker clusters; interfaces pl‑pl and en‑gb                                            |
| **onboarding and training plan**         | webinar + pdf guide                                                                                  |
| **progress tracking and reporting plan** | fortnightly meetings with ministry                                                                   |
| **issue escalation procedure**           | central helpdesk `support@edu.pl`                                                                    |
| **success metrics and kpis**             | below                                                                                                |
| **spoc contact and validation status**   | piotr nowak, [p.nowak@uw.edu.pl](mailto:p.nowak@uw.edu.pl); review 5 july 2025                       |

### success metrics and kpis

| kpi                            | formula                     | source   | tool    | frequency | target |
| ------------------------------ | --------------------------- | -------- | ------- | --------- | ------ |
| wallet activation              | activated ÷ issued × 100    | issuer   | grafana | weekly    | ≥90 %  |
| cross‑uni verification success | successful ÷ attempts × 100 | verifier | grafana | weekly    | ≥96 %  |
