# skaitos kompiuterių servisas (sks) – pilot – professional qualification verification

## scenario description

sks, a lithuanian it service company, pilots verification of professional qualification electronic attestations of attributes (eaas) issued by vocational bodies. the flow showcases third‑party verification only (no issuance) using an arf‑compliant wallet and a verifier portal. compliance follows **eidas2**, **arf**, and lithuanian law 30/2024 on digital identity services.

## key steps per user journey

### 1. professional qualification eaa verification

* employee presents professional qualification eaa from wallet.
* verifier portal validates integrity, issuer did anchoring, trust list status and authorisation.
* portal returns validity response and human‑readable pdf.

## scenario details

| element                                  | description                                                                                |
| ---------------------------------------- | ------------------------------------------------------------------------------------------ |
| **scenario name**                        | professional qualification verification                                                    |
| **piloting agent**                       | skaitos kompiuterių servisas (sks)                                                         |
| **end users identification**             | up to 50 employees                                                                         |
| **selection criteria**                   | employment at sks, lithuanian pid                                                          |
| **eaas involved**                        | professional qualification eaa                                                             |
| **institutional systems involved**       | verifier portal, hr system                                                                 |
| **technical components**                 | verifier api `https://verify.sks.lt/v1`, wallet `litwallet`                                |
| **governance setup**                     | verifier did registered in ebsi; qseal in regolith trust list                              |
| **feedback & monitoring mechanism**      | hr survey; kibana dashboards                                                               |
| **regulatory context**                   | gdpr, eidas2, lt law 30/2024                                                               |
| **risk management considerations**       | forged credential (low/high)                                                               |
| **credential lifecycle management**      | not applicable (verification only)                                                         |
| **infrastructure readiness**             | aws‑lt region; interfaces lt‑lt and en‑gb                                                  |
| **onboarding and training plan**         | slack tutorial                                                                             |
| **progress tracking and reporting plan** | monthly hr report                                                                          |
| **issue escalation procedure**           | it desk `help@sks.lt`                                                                      |
| **success metrics and kpis**             | see below                                                                                  |
| **spoc contact and validation status**   | ruta žukauskaitė, [r.zukauskaite@sks.lt](mailto:r.zukauskaite@sks.lt); review 10 july 2025 |

### success metrics and kpis

| kpi                   | formula                     | source   | tool   | frequency | target |
| --------------------- | --------------------------- | -------- | ------ | --------- | ------ |
| verification success  | successful ÷ attempts × 100 | verifier | kibana | weekly    | ≥98 %  |
| employee satisfaction | avg score (1‑5)             | survey   | kibana | monthly   | ≥4.0   |
