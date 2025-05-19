# EUVETMC Signed Credential Example (JAdES D-Zero Profile)

This example transforms the unsigned EUVETMC into a JWS Compact Serialisation using the JAdES D-Zero signature profile. The credential is signed with the VET provider’s ECDSA P-256 key (placeholder key: `{"kty":"EC","x":"9f00-IlhEFVmlpCU8u51i4ZqCAY1bMHUu5OEbXOrOz8","y":"84Mp_hrdzqRDD3a8DNYPONWJYPND1H6WkN-NmnrRbD8","crv":"P-256","d":"Cb-7omOc3t9dSK6qx6ss6QenLS2EIB-wG7tfZJW_Tbw"}`).

- Uses JAdES D-Zero profile, with header specifying `typ: jades-d-z`, `cty: vc+ld+json`, and `sigPl` with the provider’s address.
- Payload is the minified unsigned credential, including all mandatory Annex I elements.
- Signature placeholder is used, to be replaced by an ECDSA signature.
- Verification involves decoding JWS, validating header/payload, and checking signature via EBSI.

## JWS Structure:

### Protected Header:
```json
{
  "alg": "ES256",
  "typ": "jades-d-z",
  "cty": "vc+ld+json",
  "kid": "did:ebsi:vetCroatia123#keys-1",
  "crit": ["sigT", "sigPl"],
  "sigT": "2025-05-04T10:00:00Z",
  "sigPl": {
    "addressCountry": "HR",
    "addressLocality": "Zagreb",
    "postalCode": "10000",
    "streetAddress": "Savska cesta 41"
  }
}
```

### Base64URL:
eyJhbGciOiJFUzI1NiIsInR5cCI6ImphZGVzLWQteiIsImN0eSI6InZjK2xkK2pzb24iLCJraWQiOiJkaWQ6ZWJzaTp2ZXRDcm9hdGlhMTIzI2tleXMtMSIsImNyaXQiOlsic2lnVCIsInNpZ1BsIl0sInNpZ1QiOiIyMDI1LTA1LTA0VDEwOjAwOjAwWiIsInNpZ1BsIjp7ImFkZHJlc3NDb3VudHJ5IjoiSFIiLCJhZGRyZXNzTG9jYWxpdHkiOiJaYWdyZWIiLCJwb3N0YWxDb2RlIjoiMTAwMDAiLCJzdHJlZXRBZGRyZXNzIjoiU2F2c2thIGNlc3RhIDQxIn19

### Payload:
Minified unsigned credential.
```json
{"@context":["https://www.w3.org/2018/credentials/v1","https://w3id.org/edc/v1"],"id":"urn:uuid:9e7c4f8d-1b9a-4e1b-8f2a-7b9c0d5e6d3a","type":["VerifiableCredential","EuropeanDigitalCredential","EuropeanVETMicroCredentials"],"issuer":{"id":"did:ebsi:vetCroatia123"},"issuerCountry":{"id":"urn:concept:hr","type":"Concept","prefLabel":{"en":"Croatia"}},"issuanceDate":"2025-05-04T10:00:00Z","issued":"2025-05-04T10:00:00Z","validFrom":"2025-05-04T10:00:00Z","qualityAssurance":{"id":"urn:concept:eqavet","type":"Concept","prefLabel":{"en":"EQAVET-compliant"}},"credentialSubject":{"id":"did:ebsi:example:vetstudent456","type":"Person","fullName":{"en":"Ana Kovačić"},"givenName":{"en":"Ana"},"familyName":{"en":"Kovačić"},"nationalID":{"id":"urn:legal:hr:OIB:9876543210","type":"LegalIdentifier","notation":"9876543210","spatial":{"id":"urn:concept:hr","type":"Concept","prefLabel":{"en":"Croatia"}}},"hasClaim":[{"id":"urn:uuid:2b3c4d5e-6f7g-8h9i-0j1k-2l3m4n5o6p7q","type":"LearningAchievement","title":{"en":"Renewable Energy Installation"},"creditReceived":[{"id":"urn:uuid:3c4d5e6f-7g8h-9i0j-1k2l-3m4n5o6p7q8r","type":"CreditPoint","framework":{"id":"urn:concept:ECVET","type":"Concept","prefLabel":{"en":"ECVET"}},"point":"5"}],"level":{"id":"urn:concept:eqf4","type":"Concept","prefLabel":{"en":"EQF Level 4"}},"learningSetting":{"id":"urn:concept:work-based","type":"Concept","prefLabel":{"en":"Work-based"}},"stackability":{"id":"urn:concept:stackable","type":"Concept","prefLabel":{"en":"Stackable toward VET qualification"}},"learningOutcome":[{"id":"urn:uuid:4d5e6f7g-8h9i-0j1k-2l3m-4n5o6p7q8r9s","type":"LearningOutcome","title":{"en":"Ability to install solar panels"},"relatedCompetence":[{"id":"urn:concept:solar-installation","type":"Concept","prefLabel":{"en":"Solar Panel Installation"}}],"relatedESCOSkill":[{"id":"http://data.europa.eu/esco/skill/67890","type":"Concept","prefLabel":{"en":"Renewable Energy Systems"}}]}],"awardedBy":{"id":"urn:uuid:award-1","type":"AwardingProcess","awardingBody":{"id":"did:ebsi:vetCroatia123","type":"Organisation","legalName":{"en":"Agency for VET and Adult Education"}}}},{"id":"urn:uuid:5e6f7g8h-9i0j-1k2l-3m4n-5o6p7q8r9s0t","type":"LearningAssessment","title":{"en":"Solar Installation Practical Test"},"assessmentType":{"id":"urn:concept:practical","type":"Concept","prefLabel":{"en":"Practical Test"}},"grade":{"id":"urn:uuid:6f7g8h9i-0j1k-2l3m-4n5o-6p7q8r9s0t1u","type":"Note","noteLiteral":{"en":"90/100"}},"awardedBy":{"id":"urn:uuid:award-2","type":"AwardingProcess","awardingBody":{"id":"did:ebsi:vetCroatia123","type":"Organisation","legalName":{"en":"Agency for VET and Adult Education"}}}}]},"credentialSchema":{"id":"https://trusted-registries.ebsi.eu/schemas/euvetmc/1.0","type":"JsonSchema"},"displayParameter":{"id":"urn:uuid:7g8h9i0j-1k2l-3m4n-5o6p-7q8r9s0t1u2v","type":"DisplayParameter","title":{"en":"EUVETMC Display"},"language":[{"id":"urn:concept:en","type":"Concept","prefLabel":{"en":"English"}}],"primaryLanguage":{"id":"urn:concept:en","type":"Concept","prefLabel":{"en":"English"}},"individualDisplay":[{"id":"urn:uuid:8h9i0j1k-2l3m-4n5o-6p7q-8r9s0t1u2v3w","type":"IndividualDisplay","fieldPath":"credentialSubject.fullName","label":{"en":"Full Name"},"order":1},{"id":"urn:uuid:9i0j1k2l-3m4n-5o6p-7q8r-9s0t1u2v3w4x","type":"IndividualDisplay","fieldPath":"credentialSubject.hasClaim[0].title","label":{"en":"Achievement Title"},"order":2}]}}
```
### Signature:
Placeholder for ECDSA signature.

Example format: [signature-placeholder].

JWS Compact Serialisation:
eyJhbGciOiJFUzI1NiIsInR5cCI6ImphZGVzLWQteiIsImN0eSI6InZjK2xkK2pzb24iLCJraWQiOiJkaWQ6ZWJzaTp2ZXRDcm9hdGlhMTIzI2tleXMtMSIsImNyaXQiOlsic2lnVCIsInNpZ1BsIl0sInNpZ1QiOiIyMDI1LTA1LTA0VDEwOjAwOjAwWiIsInNpZ1BsIjp7ImFkZHJlc3NDb3VudHJ5IjoiSFIiLCJhZGRyZXNzTG9jYWxpdHkiOiJaYWdyZWIiLCJwb3N0YWxDb2RlIjoiMTAwMDAiLCJzdHJlZXRBZGRyZXNzIjoiU2F2c2thIGNlc3RhIDQxIn19.eyJAY29udGV4dCI6WyJodHRwczovL3d3dy53My5vcmcvMjAxOC9jcmVkZW50aWFscy92MSIsImh0dHBzOi8vdzNpZC5vcmcvZWRjL3YxIl0sImlkIjoidXJuOnV1aWQ6OWU3YzRmOGQtMWI5YS00ZTFiLThmMmEtN2I5YzBkNWU2ZDNhIiwidHlwZSI6WyJWZXJpZmlhYmxlQ3JlZGVudGlhbCIsIkV1cm9wZWFuRGlnaXRhbENyZWRlbnRpYWwiLCJFdXJvcGVhblZFVE1pY3JvQ3JlZGVudGlhbHMiXSwiaXNzdWVyIjp7ImlkIjoiZGlkOmVic2k6dmV0Q3JvYXRpYTEyMyJ9LCJpc3N1ZXJDb3VudHJ5Ijp7ImlkIjoidXJuOmNvbmNlcnQ6aHIiLCJ0eXBlIjoiQ29uY2VwdCIsInByZWZMYWJlbCI6eyJlbiI6IkNyb2F0aWEifX0sImlzc3VhbmNlRGF0ZSI6IjIwMjUtMDUtMDRUMTA6MDA6MDBaIiwiaXNzdWVkIjoiMjAyNS0wNS0wNFQxMDowMDowMFoiLCJ2YWxpZEZyb20iOiIyMDI1LTA1LTA0VDEwOjAwOjAwWiIsInF1YWxpdHlBc3N1cmFuY2UiOnsiaWQiOiJ1cm46Y29uY2VwdDplcWF2ZXQiLCJ0eXBlIjoiQ29uY2VwdCIsInByZWZMYWJlbCI6eyJlbiI6IkVRQVZFVC1jb21wbGlhbnQifX0sImNyZWRlbnRpYWxTdWJqZWN0Ijp7ImlkIjoiZGlkOmVic2k6ZXhhbXBsZTp2ZXRzdHVkZW50NDU2IiwidHlwZSI6IlBlcnNvbiIsImZ1bGxOYW1lIjp7ImVuIjoiQW5hIEtvdmHDpWnEhyJ9LCJnaXZlbk5hbWUiOnsiZW4iOiJBbmEifSwiZmFtaWx5TmFtZSI6eyJlbiI6IktvdmHDpWnEhyJ9LCJuYXRpb25hbElEIjp7ImlkIjoidXJuOmxlZ2FsOmhyOk9JQjo5ODc2NTQzMjEwIiwidHlwZSI6IkxlZ2FsSWRlbnRpZmllciIsIm5vdGF0aW9uIjoiOTg3NjU0MzIxMCIsInNwYXRpYWwiOnsiaWQiOiJ1cm46Y29uY2VwdDpociIsInR5cGUiOiJDb25jZXB0IiwicHJlZkxhYmVsIjp7ImVuIjoiQ3JvYXRpYSJ9fX0sImhhc0NsYWltIjpbeyJpZCI6InVybjp1dWlkOjJiM2M0ZDVlLTZmN2ctOGg5aS0wajFrLTJsM240bjVvNnA3cSIsInR5cGUiOiJMZWFybmluZ0FjaGlldmVtZW50IiwidGl0bGUiOnsiZW4iOiJSZW5ld2FibGUgRW5lcmd5IEluc3RhbGxhdGlvbiJ9LCJjcmVkaXRSZWNlaXZlZCI6W3siaWQiOiJ1cm46dXVpZDo0ZDVlNmY3Zy04aDlpLTBqMWstMmwzbS00bjVvNnA3cThyOXMiLCJ0eXBlIjoiQ3JlZGl0UG9pbnQiLCJmcmFtZXdvcmsiOnsiaWQiOiJ1cm46Y29uY2VwdDpFQ1ZFVCIsInR5cGUiOiJDb25jZXB0IiwicHJlZkxhYmVsIjp7ImVuIjoiRUNWRVQifX0sInBvaW50IjoiNSJ9XSwibGV2ZWwiOnsiaWQiOiJ1cm46Y29uY2VwdDplcWY0IiwidHlwZSI6IkNvbmNlcnQiLCJwcmVmTGFiZWwiOnsiZW4iOiJFUUYgTGV2ZWwgNCJ9fSwibGVhcm5pbmdTZXR0aW5nIjp7ImlkIjoidXJuOmNvbmNlcnQ6d29yay1iYXNlZCIsInR5cGUiOiJDb25jZXB0IiwicHJlZkxhYmVsIjp7ImVuIjoiV29yay1iYXNlZCJ9fSwic3RhY2thYmlsaXR5Ijp7ImlkIjoidXJuOmNvbmNlcrQ6c3RhY2thYmxlIiwidHlwZSI6IkNvbmNlcnQiLCJwcmVmTGFiZWwiOnsiZW4iOiJTdGFja2FibGUgdG93YXJkIFZFVCBxdWFsaWZpY2F0aW9uIn19LCJsZWFybmluZ091dGNvbWUiOlt7ImlkIjoidXJuOnV1aWQ6NGQ1ZTZmN2ctOGg5aS0wajFrLTJsM20tNG41bzZwN3E4cjlzIiwidHlwZSI6IkxlYXJuaW5nT3V0Y29tZSIsInRpdGxlIjp7ImVuIjoiQWJpbGl0eSB0byBpbnN0YWxsIHNvbGFyIHBhbmVscyJ9LCJyZWxhdGVkQ29tcGV0ZW5jZSI6W3siaWQiOiJ1cm46Y29uY2VwdDpzb2xhci1pbnN0YWxsYXRpb24iLCJ0eXBlIjoiQ29uY2VwdCIsInByZWZMYWJlbCI6eyJlbiI6IlNvbGFyIFBhbmVsIEluc3RhbGxhdGlvbiJ9fV0sInJlbGF0ZWRFU0NPU2tpbGwiOlt7ImlkIjoiaHR0cDovL2RhdGEuZXVyb3BhLmV1L2VzY28vc2tpbGwvNjc4OTAiLCJ0eXBlIjoiQ29uY2VwdCIsInByZWZMYWJlbCI6eyJlbiI6IlJlbmV3YWJsZSBFbmVyZ3kgU3lzdGVtcyJ9fV19XSwiYXdhcmRlZEJ5Ijp7ImlkIjoidXJuOnV1aWQ6YXdhcmQtMSIsInR5cGUiOiJBd2FyZGluZ1Byb2Nlc3MiLCJhd2FyZGluZ0JvZHkiOnsiaWQiOiJkaWQ6ZWJzaTp2ZXRDcm9hdGlhMTIzIiwidHlwZSI6Ik9yZ2FuaXNhdGlvbiIsImxlZ2FsTmFtZSI6eyJlbiI6IkFnZW5jeSBmb3IgVkVUIGFuZCBBZHVsdCBFZHVjYXRpb24ifX19XX0sImNyZWRlbnRpYWxTY2hlbWEiOnsiaWQiOiJodHRwczovL3RydXN0ZWQtcmVnaXN0cmllcy5lYnNpLmV1L3NjaGVtYXMvZXV2ZXRtYy8xLjAiLCJ0eXBlIjoiSnNvblNjaGVtYSJ9LCJkaXNwbGF5UGFyYW1ldGVyIjp7ImlkIjoidXJuOnV1aWQ6N2c4aDlpMGotMWsybC0zbTRuLTVvNnAtN3E4cjlzMHQxdTJ2IiwidHlwZSI6IkRpc3BsYXlQYXJhbWV0ZXIiLCJ0aXRsZSI6eyJlbiI6IkVVTkVUTUMgRGlzcGxheSJ9LCJsYW5ndWFnZSI6W3siaWQiOiJ1cm46Y29uY2VwdDplbiIsInR5cGUiOiJDb25jZXB0IiwicHJlZkxhYmVsIjp7ImVuIjoiRW5nbGlzaCJ9fV0sInByaW1hcnlMYW5ndWFnZSI6eyJpZCI6InVybjpjb25jZXB0OmVuIiwidHlwZSI6IkNvbmNlcnQiLCJwcmVmTGFiZWwiOnsiZW4iOiJFbmdsaXNoIn19LCJpbmRpdmlkdWFsRGlzcGxheSI6W3siaWQiOiJ1cm46dXVpZDo4aDlpMGoxay0ybDNtLTQuNXAtNnA3cS04cjlzMHQxdTJ2M3ciLCJ0eXBlIjoiSW5kaXZpZHVhbERpc3BsYXkiLCJmaWVsZFBhdGgiOiJjcmVkZW50aWFsU3ViamVjdC5mdWxsTmFtZSIsImxhYmVsIjp7ImVuIjoiRnVsbCBOYW1lIn0sIm9yZGVyIjoxfSx7ImlkIjoidXJuOnV1aWQ6OWkwajFrMmwtM200bi01bzZwLTdxOHItOXMwdDF1MnYzd3czeCIsInR5cGUiOiJJbmRpdmlkdWFsRGlzcGxheSIsImZpZWxkUGF0aCI6ImNyZWRlbnRpYWxTdWJqZWN0Lmhhc0NsYWltWzBdLnRpdGxlIiwibGFiZWwiOnsiZW4iOiJBY2hpZXZlbWVudCBUaXRsZSJ9LCJvcmRlciI6Mn1dfX19.[signature-placeholder]

### Signing Process
Prepare Header: Include alg, typ, cty, kid, crit, sigT, sigPl; encode as Base64URL.
Prepare Payload: Minify unsigned credential, ensuring all mandatory Annex I elements; encode as Base64URL.
Sign: Compute ECDSA signature over ASCII(BASE64URL(UTF8(Header)) || '.' || BASE64URL(Payload)) using private key.
Combine: Form JWS as <header>.<payload>.<signature>.

### Verification Process
Decode JWS: Split into header, payload, and signature.
Validate Header: Check alg (ES256), typ (jades-d-z), cty (vc+ld+json), kid, sigT, sigPl.
Validate Payload: Ensure valid JSON-LD Verifiable Credential per EUVETMC schema, with Annex I elements.
Verify Signature: Use issuer’s public key (from DID) to verify ECDSA signature.
Check Trust: Confirm issuer is in EBSI’s trusted registries and credential aligns with EQAVET standards.