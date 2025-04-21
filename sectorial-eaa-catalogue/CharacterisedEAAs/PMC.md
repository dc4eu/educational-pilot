# DC4EU EAA Characterisations (EBSI Verifier Trust Model Aligned)

_Last updated: 2025-04-21_

# EAA Characterisation Proposals

## Professional Medical Certification (`PMC`)

```json
{
  "eaa_id": "PMC",
  "title": "Professional Medical Certification",
  "description": "Credential representing professional medical certification issued by an authorised institution under a recognised qualification framework.",
  "credential_type": "VerifiableAttestation",
  "data_model": {
    "standard": "W3C Verifiable Credentials",
    "profile": "DC4EU-Education",
    "schema_uri": "https://tsr.dc4eu.eu/schemas/pmc.jsonld"
  },
  "sectoral_scope": "ProfessionalQualifications",
  "issuable_by": {
    "authorised_roles": [
      "ProfessionalBody",
      "RegulatedAuthority"
    ],
    "taor_required": true,
    "tir_entry": "did:ebsi:issuer-pmc"
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
    "machine_readable": "https://tsr.dc4eu.eu/policies/pmc-disclosure.json"
  },
  "terms_of_reference_uri": "https://tsr.dc4eu.eu/tor/pmc.json",
  "revocation_support": {
    "method": "StatusList2021",
    "status_endpoint": "https://status.dc4eu.eu/status/pmc",
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

## Certificate Professional Competence (`CPC`)

```json
{
  "eaa_id": "CPC",
  "title": "Certificate Professional Competence",
  "description": "Credential representing certificate professional competence issued by an authorised institution under a recognised qualification framework.",
  "credential_type": "VerifiableAttestation",
  "data_model": {
    "standard": "W3C Verifiable Credentials",
    "profile": "DC4EU-Education",
    "schema_uri": "https://tsr.dc4eu.eu/schemas/cpc.jsonld"
  },
  "sectoral_scope": "ProfessionalQualifications",
  "issuable_by": {
    "authorised_roles": [
      "ProfessionalBody",
      "RegulatedAuthority"
    ],
    "taor_required": true,
    "tir_entry": "did:ebsi:issuer-cpc"
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
    "machine_readable": "https://tsr.dc4eu.eu/policies/cpc-disclosure.json"
  },
  "terms_of_reference_uri": "https://tsr.dc4eu.eu/tor/cpc.json",
  "revocation_support": {
    "method": "StatusList2021",
    "status_endpoint": "https://status.dc4eu.eu/status/cpc",
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

## Certificate of Professional Suitability Schema (`CPS`)

```json
{
  "eaa_id": "CPS",
  "title": "Certificate of Professional Suitability Schema",
  "description": "Credential representing certificate of professional suitability schema issued by an authorised institution under a recognised qualification framework.",
  "credential_type": "VerifiableAttestation",
  "data_model": {
    "standard": "W3C Verifiable Credentials",
    "profile": "DC4EU-Education",
    "schema_uri": "https://tsr.dc4eu.eu/schemas/cps.jsonld"
  },
  "sectoral_scope": "ProfessionalQualifications",
  "issuable_by": {
    "authorised_roles": [
      "ProfessionalBody",
      "RegulatedAuthority"
    ],
    "taor_required": true,
    "tir_entry": "did:ebsi:issuer-cps"
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
    "machine_readable": "https://tsr.dc4eu.eu/policies/cps-disclosure.json"
  },
  "terms_of_reference_uri": "https://tsr.dc4eu.eu/tor/cps.json",
  "revocation_support": {
    "method": "StatusList2021",
    "status_endpoint": "https://status.dc4eu.eu/status/cps",
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


# Non-Foundational Identity EAA Characterisations

## EducationalID (`EducationalID`)

```json
{
  "eaa_id": "EducationalID",
  "title": "EducationalID",
  "description": "Identity credential that identifies a natural person in the context of educational activities or affiliation, as issued by an authorised organisation.",
  "credential_type": "VerifiableAttestation",
  "data_model": {
    "standard": "W3C Verifiable Credentials",
    "profile": "DC4EU-Identity",
    "schema_uri": "https://tsr.dc4eu.eu/schemas/educationalid.jsonld"
  },
  "sectoral_scope": "FormalEducation",
  "issuable_by": {
    "authorised_roles": [
      "HigherEducationInstitution",
      "UniversityAlliance"
    ],
    "taor_required": true,
    "tir_entry": "did:ebsi:issuer-educationalid"
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
    "machine_readable": "https://tsr.dc4eu.eu/policies/educationalid-disclosure.json"
  },
  "terms_of_reference_uri": "https://tsr.dc4eu.eu/tor/educationalid.json",
  "revocation_support": {
    "method": "StatusList2021",
    "status_endpoint": "https://status.dc4eu.eu/status/educationalid",
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

## AllianceID (`AllianceID`)

```json
{
  "eaa_id": "AllianceID",
  "title": "AllianceID",
  "description": "Identity credential that identifies a natural person in the context of alliance activities or affiliation, as issued by an authorised organisation.",
  "credential_type": "VerifiableAttestation",
  "data_model": {
    "standard": "W3C Verifiable Credentials",
    "profile": "DC4EU-Identity",
    "schema_uri": "https://tsr.dc4eu.eu/schemas/allianceid.jsonld"
  },
  "sectoral_scope": "FormalEducation",
  "issuable_by": {
    "authorised_roles": [
      "HigherEducationInstitution",
      "UniversityAlliance"
    ],
    "taor_required": true,
    "tir_entry": "did:ebsi:issuer-allianceid"
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
    "machine_readable": "https://tsr.dc4eu.eu/policies/allianceid-disclosure.json"
  },
  "terms_of_reference_uri": "https://tsr.dc4eu.eu/tor/allianceid.json",
  "revocation_support": {
    "method": "StatusList2021",
    "status_endpoint": "https://status.dc4eu.eu/status/allianceid",
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

## MyAcademicID (`MyAcademicID`)

```json
{
  "eaa_id": "MyAcademicID",
  "title": "MyAcademicID",
  "description": "Identity credential that identifies a natural person in the context of myacademic activities or affiliation, as issued by an authorised organisation.",
  "credential_type": "VerifiableAttestation",
  "data_model": {
    "standard": "W3C Verifiable Credentials",
    "profile": "DC4EU-Identity",
    "schema_uri": "https://tsr.dc4eu.eu/schemas/myacademicid.jsonld"
  },
  "sectoral_scope": "FormalEducation",
  "issuable_by": {
    "authorised_roles": [
      "HigherEducationInstitution",
      "UniversityAlliance"
    ],
    "taor_required": true,
    "tir_entry": "did:ebsi:issuer-myacademicid"
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
    "machine_readable": "https://tsr.dc4eu.eu/policies/myacademicid-disclosure.json"
  },
  "terms_of_reference_uri": "https://tsr.dc4eu.eu/tor/myacademicid.json",
  "revocation_support": {
    "method": "StatusList2021",
    "status_endpoint": "https://status.dc4eu.eu/status/myacademicid",
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

## DoctorID (`DoctorID`)

```json
{
  "eaa_id": "DoctorID",
  "title": "DoctorID",
  "description": "Identity credential that identifies a natural person in the context of doctor activities or affiliation, as issued by an authorised organisation.",
  "credential_type": "VerifiableAttestation",
  "data_model": {
    "standard": "W3C Verifiable Credentials",
    "profile": "DC4EU-Identity",
    "schema_uri": "https://tsr.dc4eu.eu/schemas/doctorid.jsonld"
  },
  "sectoral_scope": "ProfessionalQualifications",
  "issuable_by": {
    "authorised_roles": [
      "ProfessionalBody",
      "RegulatedAuthority"
    ],
    "taor_required": true,
    "tir_entry": "did:ebsi:issuer-doctorid"
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
    "machine_readable": "https://tsr.dc4eu.eu/policies/doctorid-disclosure.json"
  },
  "terms_of_reference_uri": "https://tsr.dc4eu.eu/tor/doctorid.json",
  "revocation_support": {
    "method": "StatusList2021",
    "status_endpoint": "https://status.dc4eu.eu/status/doctorid",
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

## EngineerID (`EngineerID`)

```json
{
  "eaa_id": "EngineerID",
  "title": "EngineerID",
  "description": "Identity credential that identifies a natural person in the context of engineer activities or affiliation, as issued by an authorised organisation.",
  "credential_type": "VerifiableAttestation",
  "data_model": {
    "standard": "W3C Verifiable Credentials",
    "profile": "DC4EU-Identity",
    "schema_uri": "https://tsr.dc4eu.eu/schemas/engineerid.jsonld"
  },
  "sectoral_scope": "ProfessionalQualifications",
  "issuable_by": {
    "authorised_roles": [
      "ProfessionalBody",
      "RegulatedAuthority"
    ],
    "taor_required": true,
    "tir_entry": "did:ebsi:issuer-engineerid"
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
    "machine_readable": "https://tsr.dc4eu.eu/policies/engineerid-disclosure.json"
  },
  "terms_of_reference_uri": "https://tsr.dc4eu.eu/tor/engineerid.json",
  "revocation_support": {
    "method": "StatusList2021",
    "status_endpoint": "https://status.dc4eu.eu/status/engineerid",
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


# Foundational Identity EAA Characterisation

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

