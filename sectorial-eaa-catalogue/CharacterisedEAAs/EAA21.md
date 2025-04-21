# DC4EU EAA Characterisations (EBSI Verifier Trust Model Aligned)

_Last updated: 2025-04-21_

# EAA Characterisation Proposals

## Person Identifier (PID)

```json
{
  "eaa_id": "PID",
  "title": "Person Identifier (PID)",
  "description": "Foundational identity credential representing a unique, legal, and verifiable identifier for natural persons across Member States, aligned with eIDAS 2.0 and ARF.",
  "credential_type": "QEAA",
  "data_model": {
    "standard": "W3C Verifiable Credentials",
    "profile": "DC4EU-FoundationalID",
    "schema_uri": "https://tsr.dc4eu.eu/schemas/pid.jsonld"
  },
  "sectoral_scope": "CrossSectoral",
  "issuable_by": {
    "authorised_roles": [
      "PIDAccreditedAuthority"
    ],
    "taor_required": true,
    "tir_entry": "did:ebsi:issuer-pid"
  },
  "usable_by": {
  "verifier_authorisation_required": true,
  "input_descriptor_type": "TO_BE_DEFINED",  // replace with actual EAA type
  "trust_framework": "eIDAS",
  "limit_root_tao": ["did:ebsi:example-root-tao"],
    "authorised_roles": [
      "VerifierWithPIDLicence",
      "WalletHolder"
    ],
    "entitlement_check": "required"
  },
  "requires_pid": false,
  "disclosure_policy": {
  "restricted_access": true,
  "verifier_role_check": true,
  "confidentiality_level": "confidential",
  "presentation_policy_uri": "https://tsr.dc4eu.eu/policies/TO_BE_DEFINED-presentation-policy.json",
    "restricted_access": true,
    "verifier_role_check": true,
    "machine_readable": "https://tsr.dc4eu.eu/policies/pid-disclosure.json"
  },
  "terms_of_reference_uri": "https://tsr.dc4eu.eu/tor/pid.json",
  "revocation_support": {
    "method": "StatusList2021",
    "status_endpoint": "https://status.dc4eu.eu/status/pid",
    "supports_suspension": true
  },
  "binding_requirements": {
    "proof_of_possession": true,
    "cryptographic_binding_to_holder": true
  },
  "expiry": {
    "type": "dynamic",
    "validity": "linked to national or EU legal framework"
  },
  "version": "1.0"
}
```

