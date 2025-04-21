# DC4EU EAA Characterisations (EBSI Verifier Trust Model Aligned)

_Last updated: 2025-04-21_

# EAA Characterisation Proposals

## Higher education diploma Supplement (`HEDS`)

```json
{
  "eaa_id": "HEDS",
  "title": "Higher education diploma Supplement",
  "description": "Credential representing higher education diploma supplement issued by an authorised institution under a recognised qualification framework.",
  "credential_type": "VerifiableAttestation",
  "data_model": {
    "standard": "W3C Verifiable Credentials",
    "profile": "DC4EU-Education",
    "schema_uri": "https://tsr.dc4eu.eu/schemas/heds.jsonld"
  },
  "sectoral_scope": "FormalEducation",
  "issuable_by": {
    "authorised_roles": [
      "HigherEducationInstitution",
      "VocationalEducationInstitution"
    ],
    "taor_required": true,
    "tir_entry": "did:ebsi:issuer-heds"
  },
  "usable_by": {
  "verifier_authorisation_required": true,
  "input_descriptor_type": "TO_BE_DEFINED",  // replace with actual EAA type
  "trust_framework": "eIDAS",
  "limit_root_tao": ["did:ebsi:example-root-tao"],
    "authorised_roles": [
      "RecognitionAuthority",
      "PublicEmploymentService",
      "VerifierWithEduRole"
    ],
    "entitlement_check": "required"
  },
  "requires_pid": true,
  "disclosure_policy": {
  "restricted_access": true,
  "verifier_role_check": true,
  "confidentiality_level": "confidential",
  "presentation_policy_uri": "https://tsr.dc4eu.eu/policies/TO_BE_DEFINED-presentation-policy.json",
    "restricted_access": true,
    "verifier_role_check": true,
    "machine_readable": "https://tsr.dc4eu.eu/policies/heds-disclosure.json"
  },
  "terms_of_reference_uri": "https://tsr.dc4eu.eu/tor/heds.json",
  "revocation_support": {
    "method": "StatusList2021",
    "status_endpoint": "https://status.dc4eu.eu/status/heds",
    "supports_suspension": false
  },
  "binding_requirements": {
    "proof_of_possession": true,
    "cryptographic_binding_to_holder": true
  },
  "expiry": {
    "type": "static",
    "valid_until": "2040-12-31"
  },
  "version": "1.0"
}
```