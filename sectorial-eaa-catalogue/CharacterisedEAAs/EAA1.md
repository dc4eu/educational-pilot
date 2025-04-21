# DC4EU EAA Characterisations (EBSI Verifier Trust Model Aligned)

_Last updated: 2025-04-21_

# EAA Characterisation Proposals

# Additional EAA Characterisation Proposals (Non-Foundational Identity)

## Enrolment Status (`EAA1`)

```json
{
  "eaa_id": "EAA1",
  "title": "Enrolment Status",
  "description": "Attestation that confirms the current enrolment status of a learner in a formal education programme.",
  "credential_type": "VerifiableAttestation",
  "data_model": {
    "standard": "W3C Verifiable Credentials",
    "profile": "DC4EU-Education",
    "schema_uri": "https://tsr.dc4eu.eu/schemas/enrolment-status-v1.jsonld"
  },
  "sectoral_scope": "FormalEducation",
  "issuable_by": {
    "authorised_roles": [
      "HigherEducationInstitution",
      "VocationalEducationInstitution"
    ],
    "taor_required": true,
    "tir_entry": "did:ebsi:issuer-edu"
  },
  "usable_by": {
  "verifier_authorisation_required": true,
  "input_descriptor_type": "TO_BE_DEFINED",  // replace with actual EAA type
  "trust_framework": "eIDAS",
  "limit_root_tao": ["did:ebsi:example-root-tao"],
    "authorised_roles": [
      "StudentUnion",
      "PublicTransportService",
      "VerifierWithEduRole"
    ],
    "entitlement_check": "optional"
  },
  "requires_pid": true,
  "disclosure_policy": {
  "restricted_access": true,
  "verifier_role_check": true,
  "confidentiality_level": "confidential",
  "presentation_policy_uri": "https://tsr.dc4eu.eu/policies/TO_BE_DEFINED-presentation-policy.json",
    "restricted_access": true,
    "verifier_role_check": true,
    "machine_readable": "https://tsr.dc4eu.eu/policies/enrolment-disclosure.json"
  },
  "terms_of_reference_uri": "https://tsr.dc4eu.eu/tor/enrolment.json",
  "revocation_support": {
    "method": "StatusList2021",
    "status_endpoint": "https://status.dc4eu.eu/status/enrolment",
    "supports_suspension": true
  },
  "binding_requirements": {
    "proof_of_possession": true,
    "cryptographic_binding_to_holder": true
  },
  "expiry": {
    "type": "dynamic",
    "validity": "linked to academic year"
  },
  "version": "1.0"
}
```