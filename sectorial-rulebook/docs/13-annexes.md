# Annexes

This section provides supporting materials, mappings, and references to reinforce implementation of the EAA-based authorisation model for education and professional qualifications.

---

## A. EQF Level Mapping

The following EAAs represent authorisations to issue qualifications aligned with the European Qualifications Framework (EQF):

| EAA Value   | Description                         |
|-------------|-------------------------------------|
| EQFlevel1   | Basic knowledge (e.g. primary)      |
| EQFlevel2   | Lower secondary education           |
| EQFlevel3   | Upper secondary education           |
| EQFlevel4   | Advanced secondary / VET            |
| EQFlevel5   | Short-cycle tertiary / VET          |
| EQFlevel6   | Bachelor’s level qualifications     |
| EQFlevel7   | Master’s level qualifications       |
| EQFlevel8   | Doctoral level / advanced professions |

---

## B. Sample EAA Types by Domain

| Domain                  | Example EAAs                               |
|-------------------------|--------------------------------------------|
| Formal Education        | HigherEducationInstitution, EQFlevel6–8   |
| Quality Assurance       | QAHELicenseToActAtNationalLevel            |
| Professional Bodies     | ProfessionalBody, LicenceToAct             |
| CPD / Training          | AuthorityToDeliverAccreditedTraining       |
| Digital Identity        | MyAcademicIDIssuer, ProfessionalID         |

---

## C. Sample Credential Payload (EAA)

```json
{
  "@context": [
    "https://www.w3.org/2018/credentials/v1",
    "https://dc4eu.eu/credentials/contexts/eaa.jsonld"
  ],
  "id": "urn:uuid:1234-5678",
  "type": ["VerifiableCredential", "EAA"],
  "issuer": "did:ebsi:MINISTRY-001",
  "issuanceDate": "2025-01-01T00:00:00Z",
  "credentialSubject": {
    "id": "did:ebsi:UNIVERSITY-URV",
    "authorisation": {
      "type": "HigherEducationInstitution",
      "jurisdiction": "Spain",
      "validFrom": "2025-01-01",
      "validUntil": "2029-12-31"
    }
  },
  "proof": {
    "type": "Ed25519Signature2020",
    "created": "2025-01-01T00:00:00Z",
    "verificationMethod": "did:ebsi:MINISTRY-001#keys-1",
    "proofPurpose": "assertionMethod",
    "jws": "eyJhbGciOiJF..."
  }
}
```

---

## D. Semantic Alignment: ELM & Europass

EAAs and credentials may map to the **European Learning Model (ELM)** fields for maximum interoperability.

| EAA Field              | ELM Equivalent             |
|------------------------|----------------------------|
| Type of EAA            | `learningOpportunityType` or `awardingBodyRole` |
| EQF Level              | `learningLevel`            |
| Issuer Organisation ID | `awardingBody.identifier`  |
| Jurisdiction           | `location.country`         |

---

## E. Regulatory References

- **eIDAS Regulation (EU 910/2014)** and **amendment 2024/1183**  
- **Regulation (EC) No 765/2008** on accreditation and market surveillance  
- **General Data Protection Regulation (GDPR)** – Regulation (EU) 2016/679  
- **European Education Area (EEA)** strategic framework  
- **European Qualifications Framework (EQF)** recommendation (2017/C 189/03)  
- **W3C Verifiable Credentials Data Model**  
- **EBSI Governance Model & Technical Specifications**  
- **MyAcademicID and eduGAIN integration frameworks**  

---

This Annex can be extended with implementation-specific materials, screenshots, technical conformance tests, and national mappings as Member States onboard into the DC4EU ecosystem.


