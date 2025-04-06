{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://schema.ebsi.eu/education/certificate-of-participation-v1",
  "title": "Certificate of Participation Verifiable Attestation",
  "type": "object",
  "required": [
    "@context",
    "id",
    "type",
    "issuer",
    "issuanceDate",
    "credentialSubject",
    "credentialSchema"
  ],
  "properties": {
    "@context": {
      "type": "array",
      "items": [
        {"const": "https://www.w3.org/2018/credentials/v1"},
        {"const": "https://essif.europa.eu/schemas/vc-context/v1"}
      ]
    },
    "id": {"type": "string", "format": "uri"},
    "type": {
      "type": "array",
      "items": [
        {"const": "VerifiableCredential"},
        {"const": "VerifiableAttestation"},
        {"const": "CertificateOfParticipation"}
      ]
    },
    "issuer": {
      "type": "object",
      "required": ["id", "name", "homepage"],
      "properties": {
        "id": {"type": "string", "format": "uri"},
        "name": {"type": "string"},
        "homepage": {"type": "string", "format": "uri"}
      }
    },
    "issuanceDate": {"type": "string", "format": "date-time"},
    "credentialSubject": {
      "type": "object",
      "required": [
        "id", "givenName", "familyName", "fullName", "dateOfBirth",
        "nationalID", "citizenshipCountry", "hasClaim"
      ],
      "properties": {
        "id": {"type": "string", "format": "uri"},
        "givenName": {"type": "object"},
        "familyName": {"type": "object"},
        "fullName": {"type": "object"},
        "dateOfBirth": {"type": "string", "format": "date-time"},
        "nationalID": {
          "type": "object",
          "required": ["notation", "country"],
          "properties": {
            "notation": {"type": "string"},
            "country": {"type": "string"}
          }
        },
        "citizenshipCountry": {
          "type": "array",
          "items": {
            "type": "object",
            "required": ["id", "prefLabel", "notation"],
            "properties": {
              "id": {"type": "string", "format": "uri"},
              "prefLabel": {"type": "object"},
              "notation": {"type": "string"}
            }
          }
        },
        "hasClaim": {
          "type": "array",
          "items": {
            "type": "object",
            "required": ["id", "type", "awardedBy"],
            "properties": {
              "id": {"type": "string", "format": "uri"},
              "type": {"type": "string"},
              "awardedBy": {
                "type": "object",
                "required": ["awardingBody"],
                "properties": {
                  "awardingBody": {
                    "type": "array",
                    "items": {
                      "type": "object",
                      "required": ["legalName", "location"],
                      "properties": {
                        "legalName": {"type": "object"},
                        "location": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "required": ["address"],
                            "properties": {
                              "address": {
                                "type": "array",
                                "items": {
                                  "type": "object",
                                  "required": ["countryCode"],
                                  "properties": {
                                    "countryCode": {
                                      "type": "object",
                                      "required": ["id", "prefLabel", "notation"],
                                      "properties": {
                                        "id": {"type": "string", "format": "uri"},
                                        "prefLabel": {"type": "object"},
                                        "notation": {"type": "string"}
                                      }
                                    }
                                  }
                                }
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    },
    "credentialSchema": {
      "type": "object",
      "required": ["id", "type"],
      "properties": {
        "id": {"type": "string", "format": "uri"},
        "type": {"const": "JsonSchemaValidator2018"}
      }
    }
  }
}