# budapest university of technology and economics (bme) – pilot – dual-channel educational credentials

## scenario description

this scenario shows how budapest university of technology and economics issues and verifies educational electronic attestations of attributes (eaas) using both ebsi decentralised public key infrastructure and hungarian national trust lists. the flow observes **eidas2 article 6a**, the **eu digital identity architecture and reference framework (arf)** and interfaces with the **single digital gateway once‑only technical system (oots)**. the work forms part of dc4eu and mirrors erasmus+ digital credential activity.

## key steps per user journey

### 1. onboarding in education

* recruit 25 recent bsc graduates from bme.

  * **selection criteria:** 180 ects completed, diploma conferred after 1 february 2025, hungarian and english competence ≥b2, inclusive of accessibility needs.
* nominate three registry officers as verifiers and one integration engineer.
* ship each student an izertis eudi wallet with activation token and brief them in a 30‑minute session on wallet use, privacy and pid.
* verify identity on campus, then issue credentials for pid retrieval.
* guide students through pid retrieval and wallet activation.
* students submit an **educationalid request**. issuer checks pid and confirms enrolment, then issues educationalid to the wallet.

### 2. educational achievement issuance

* registry queries the neptun student system for each graduate’s completed modules and thesis.
* students select achievements through the wallet interface.
* issuer api signs and pushes the achievement eaas to wallets.

### 3. generic eaa verification

* any third party can verify eaas via the public verifier portal.
* the portal checks cryptographic integrity, issuer anchoring in ebsi and the hungarian trust list, and education sector governance.
* on success it returns a json‑ld payload and a pdf proof.

## scenario details

| element                                  | description                                                                                                                             |
| ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| **scenario name**                        | digital credentials for graduate verification                                                                                           |
| **piloting agent**                       | budapest university of technology and economics                                                                                         |
| **end users identification**             | 25 graduates, 3 registry verifiers, 1 it engineer                                                                                       |
| **selection criteria**                   | diploma holder, ≥180 ects, english ≥b2, includes accessibility cases                                                                    |
| **eaas involved**                        | pid, educationalid, bachelor degree achievement                                                                                         |
| **institutional systems involved**       | neptun student registry, bme idp, credential issuer microservice, verification portal                                                   |
| **technical components**                 | issuer api `https://issuer.bme.hu/v1`, verifier api `https://verify.bme.hu/v1`, pid gateway `https://pid.gov.hu/v2`, izertis wallet sdk |
| **governance setup**                     | dids registered in ebsi; qualified certificates listed in nkhi trust list; change board minutes kept in confluence                      |
| **feedback & monitoring mechanism**      | wallet survey after each issuance; grafana dashboards; weekly scrum review                                                              |
| **regulatory context**                   | gdpr art 32, eidas2 art 6a, arf v1.3 wallets section, national decree 451/2016 on electronic documents                                  |
| **risk management considerations**       | identity mismatch (medium/medium) mitigated by supervised pid retrieval; wallet loss (low/high) mitigated by seed backup advice         |
| **credential lifecycle management**      | suspension by student via wallet or by registrar on revocation list; renewal upon new studies; revocation on disciplinary ruling        |
| **infrastructure readiness**             | kubernetes cluster on campus, hardware hsm, interfaces hu‑hu and en‑gb                                                                  |
| **onboarding and training plan**         | wallet quick‑start pdf, video demo, sandbox portal for staff                                                                            |
| **progress tracking and reporting plan** | loki logs, weekly email to dg‑eac observers                                                                                             |
| **issue escalation procedure**           | it helpdesk `servicedesk@bme.hu` tier 1, escalated to digital credentials lead gábor kovács within 4 h, atos product owner after 24 h   |
| **success metrics and kpis**             | see table below                                                                                                                         |
| **spoc contact and validation status**   | gábor kovács, digital credentials lead, [g.kovacs@bme.hu](mailto:g.kovacs@bme.hu); compliance review 20 june 2025                       |

### success metrics and kpis

| kpi                           | formula                                                  | data source    | tool    | frequency | target |
| ----------------------------- | -------------------------------------------------------- | -------------- | ------- | --------- | ------ |
| wallet activation rate        | wallets activated ÷ wallets issued × 100                 | issuer logs    | grafana | weekly    | ≥95 %  |
| issuance success rate         | eaas issued ÷ eaas requested × 100                       | issuer metrics | grafana | weekly    | ≥97 %  |
| verification success rate     | successful verifications ÷ verifications attempted × 100 | verifier logs  | grafana | weekly    | ≥98 %  |
| user satisfaction             | average survey score (1‑5)                               | survey tool    | grafana | monthly   | ≥4.0   |
| mean incident resolution time | avg hours from ticket open to close                      | helpdesk       | grafana | monthly   | ≤24 h  |
