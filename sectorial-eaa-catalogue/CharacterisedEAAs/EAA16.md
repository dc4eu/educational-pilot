# DC4EU EAA Characterisations (EBSI Verifier Trust Model Aligned)

_Last updated: 2025-04-21_

# EAA Characterisation Proposals

## ProfessionalID (`ProfessionalID`)

```json
{
  "eaa_id": "ProfessionalID",
  "title": "ProfessionalID",
  "description": "Identity credential that identifies a natural person in the context of professional activities or affiliation, as issued by an authorised organisation.",
  "credential_type": "VerifiableAttestation",
  "data_model": {
    "standard": "W3C Verifiable Credentials",
    "profile": "DC4EU-Identity",
    "schema_uri": "https://tsr.dc4eu.eu/schemas/professionalid.jsonld"
  },
  "sectoral_scope": "ProfessionalQualifications",
  "issuable_by": {
    "authorised_roles": [
      "ProfessionalBody",
      "RegulatedAuthority"
    ],
    "taor_required": true,
    "tir_entry": "did:ebsi:issuer-professionalid"
  },
  "usable_by": {
  "verifier_authorisation_required": true,
  "input_descriptor_type": "TO_BE_DEFINED",  // replace with actual EAA type
  "trust_framework": "eIDAS",
  "limit_root_tao": ["did:ebsi:example-root-tao"],
    "authorised_roles": [
      "RecognitionAuthority",
      "VerifierWithEduRole",
      "VerifierWithProfRole"
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
    "machine_readable": "https://tsr.dc4eu.eu/policies/professionalid-disclosure.json"
  },
  "terms_of_reference_uri": "https://tsr.dc4eu.eu/tor/professionalid.json",
  "revocation_support": {
    "method": "StatusList2021",
    "status_endpoint": "https://status.dc4eu.eu/status/professionalid",
    "supports_suspension": true
  },
  "binding_requirements": {
    "proof_of_possession": true,
    "cryptographic_binding_to_holder": true
  },
  "expiry": {
    "type": "dynamic",
    "validity": "linked to affiliation or membership period"
  },
  "version": "1.0"
}
```