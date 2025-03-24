# Definition of Scenario

In the context of **DC4EU**, a **scenario** refers to the complete and structured definition provided by a **piloting agent** to characterise and execute one or more **user journeys**. It encompasses the set of technical, organisational, and governance elements required to ensure that the digital credential workflows are functional, compliant, and aligned with the project's architecture.

Each scenario must define:

- The final **user journeys** to be implemented, including target user groups (students, professionals, administrative staff)  
- The specific **Electronic Attestations of Attributes (EAAs)** to be issued and/or verified  
- The institutional systems or databases connected to the **issuance** and **verification** processes  
- The toolkits and technical components used (e.g. **issuer**, **verifier**, **wallet**, **PID retrieval** services)  
- The governance configuration: **identifiers**, **authorisations**, and **trust model registration**  
- The monitoring and reporting structure, including **feedback channels** and **KPIs**

Scenarios serve as the **operational unit** for execution, onboarding, monitoring, and reporting. They provide the **Single Point of Contact (SPOC)** with a clear framework to assess readiness and track the progress of piloting agents throughout the **five implementation phases** defined in the DC4EU methodology.

While the methodology defines common building blocks, each scenario will reflect the **local specificities** of the piloting agent, including language, legal context, and user typologies.

> **Note:** Each piloting agent may define one or multiple scenarios, depending on the diversity of credentials, use cases, or user groups involved.



# Scenarios list

This section outlines the common and pilot-specific artefacts that support scenario implementation across Pilots 1 and 2. These include toolkits, templates, and technical components used by piloting agents, SPOCs, and end users.


## Common elements for all Pilots

| Item              | Type            | Purpose                                               | Used by                     | Provided by         |
|-------------------|------------------|--------------------------------------------------------|------------------------------|----------------------|
| Governance template | Template        | Register credential type, issuer authority, DID, X509v3 | Piloting agents              | GovPart & SGAD       |
| Feedback form      | Template        | Capture end-user satisfaction and issues               | Piloting agents / end users | Neumann              |
| KPI dashboard      | Reporting tool  | Track operational indicators                           | SPOC / Piloting agents       | GRNet                |



## Pilot 1

### Centrally provided by DC4EU

| Item                      | Type    | Purpose                                                                          | Used by        | Provided by |
|---------------------------|---------|----------------------------------------------------------------------------------|----------------|-------------|
| Issuer interface          | Toolkit | Enable issuance of verifiable credentials                                       | Piloting agents| SUNET       |
| Verifier interface        | Toolkit | Enable verification of credentials including governance                         | Piloting agents| SUNET       |
| Natural person wallet     | Toolkit | Enable end-user to request/share credentials and perform user journeys          | Piloting agents| GUNet       |
| Basic user journey provisioner | Toolkit | Provide basic user journeys as building blocks that can be easily used or extended | Piloting agents| SUNET       |

### Centrally provided as national solution – Finland

| Item                      | Type    | Purpose                                                                          | Used by        | Provided by |
|---------------------------|---------|----------------------------------------------------------------------------------|----------------|-------------|
| Issuer interface          | Toolkit | Enable issuance of verifiable credentials                                       | Piloting agents| OPH         |
| Verifier interface        | Toolkit | Enable verification of credentials including governance                         | Piloting agents| OPH         |
| Natural person wallet     | Toolkit | Enable end-user to request/share credentials and perform user journeys          | Piloting agents| OPH         |
| Basic user journey provisioner | Toolkit | Provide basic user journeys as building blocks that can be easily used or extended | Piloting agents| OPH         |



## Pilot 2

### Centrally provided by DC4EU

| Item                      | Type    | Purpose                                                                          | Used by        | Provided by |
|---------------------------|---------|----------------------------------------------------------------------------------|----------------|-------------|
| Issuer interface          | Toolkit | Enable issuance of verifiable credentials                                       | Piloting agents| ATOS        |
| Verifier interface        | Toolkit | Enable verification of credentials including governance                         | Piloting agents| ATOS        |
| Natural person wallet     | Toolkit | Enable end-user to request/share credentials and perform user journeys          | Piloting agents| IZERTIS     |
| Basic user journey provisioner | Toolkit | Provide basic user journeys as building blocks that can be easily used or extended | Piloting agents| ATOS        |

### Centrally provided as national solution – Poland

| Item                      | Type    | Purpose                                                                          | Used by        | Provided by |
|---------------------------|---------|----------------------------------------------------------------------------------|----------------|-------------|
| Issuer interface          | Toolkit | Enable issuance of verifiable credentials                                       | Piloting agents| NASK        |
| Verifier interface        | Toolkit | Enable verification of credentials including governance                         | Piloting agents| NASK        |
| Natural person wallet     | Toolkit | Enable end-user to request/share credentials and perform user journeys          | Piloting agents| NASK        |
| Basic user journey provisioner | Toolkit | Provide basic user journeys as building blocks that can be easily used or extended | Piloting agents| NASK        |

### Institutionally provided as a piloting agent – Howest University

| Item                      | Type    | Purpose                                                                          | Used by        | Provided by |
|---------------------------|---------|----------------------------------------------------------------------------------|----------------|-------------|
| Issuer interface          | Toolkit | Enable issuance of verifiable credentials                                       | Piloting agents| Walt.ID     |
| Verifier interface        | Toolkit | Enable verification of credentials including governance                         | Piloting agents| Walt.ID     |
| Natural person wallet     | Toolkit | Enable end-user to request/share credentials and perform user journeys          | Piloting agents| Walt.ID     |
| Basic user journey provisioner | Toolkit | Provide basic user journeys as building blocks that can be easily used or extended | Piloting agents| Walt.ID     |




## Scenario checklist template (optional structure)

To support documentation and review of each scenario, piloting agents are encouraged to complete a structured overview using the template below:

| Element                                 | Description                                                                 |
|-----------------------------------------|-----------------------------------------------------------------------------|
| Scenario name                           | Unique name to identify the scenario                                        |
| Piloting agent                          | Institution responsible                                                     |
| User journey(s) covered                 | Description and link to user journey definitions                           |
| User types                              | Students / professionals / administrative staff                            |
| EAAs involved                           | Type(s) of credential(s) to be issued and/or verified                      |
| Governance setup                        | DID(s), authorisation templates, trust registration                        |
| Technical components                    | Issuer / verifier / wallet / PID services / integration endpoints          |
| Institutional systems involved          | Local databases or information systems connected                           |
| Feedback & monitoring mechanism         | Feedback collection tools and KPI reporting plan                           |
| SPOC contact and review status          | Assigned SPOC and current status of validation                             |

---

## Related documents and references

- [DC4EU Methodology - WP5 Task 2.8 (v0.2)](link-to-document)
- [User journey definitions and technical guides](link-to-guides)
- [EAAs catalogue – Task 2.5](link-to-eaa-catalogue)
- [Governance template and trust framework registration guide](link-to-governance-template)
