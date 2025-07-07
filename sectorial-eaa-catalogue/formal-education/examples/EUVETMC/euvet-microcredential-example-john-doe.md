# EUVETMC Unsigned Credential
The unsigned_credential field in the artifact contains the full JSON-LD representation of the European Vocational Education and Training Microcredential (EUVETMC) without a signature. This is the payload that would be signed using the JAdES D-Zero profile.
It excludes the proof property, as specified in issuance-detailed.md, because the JAdES D-Zero profile uses an external JWS for signing rather than embedding a proof object within the credential.

```json
{
  "@context": [
    "https://www.w3.org/2018/credentials/v1",
    "https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/contexts/european-digital-credential-v3.jsonld"
  ],
  "id": "urn:uuid:7b8c9d0e-f12a-43b5-9c7d-558766221111",
  "type": [
    "VerifiableCredential",
    "VerifiableAttestation",
    "EuropeanDigitalCredential",
    "EuropeanVocationalEducationTrainingMicrocredential"
  ],
  "identifier": [
    {
      "id": "urn:identifier:123457789-VETMC-2025",
      "type": "Identifier",
      "notation": "123457789-VETMC-2025",
      "schemeAgency": {
        "en": "Barcelona Vocational Training Institute"
      },
      "dateIssued": "2025-07-01T09:00:00Z"
    }
  ],
  "credentialProfiles": [
    {
      "id": "https://data.europa.eu/europass/credential-profiles/vet-microcredential-v1",
      "type": "Concept",
      "prefLabel": {
        "en": "Vocational Education and Training Microcredential Profile v1"
      }
    }
  ],
  "displayParameter": {
    "id": "urn:display:john-doe-vet-microcredential",
    "type": "DisplayParameter",
    "title": {
      "en": "Vocational Digital Skills Training Microcredential",
      "es": "Microcredencial de Formación en Competencias Digitales Vocacionales"
    },
    "language": [
      {
        "id": "https://id.eesc.europa.eu/languages/en",
        "type": "Concept",
        "prefLabel": {
          "en": "English"
        }
      }
    ],
    "primaryLanguage": {
      "id": "https://id.eesc.europa.eu/languages/en",
      "type": "Concept",
      "prefLabel": {
        "en": "English"
      }
    },
    "individualDisplay": [
      {
        "id": "urn:display:individual-1",
        "type": "IndividualDisplay",
        "language": {
          "id": "https://id.eesc.europa.eu/languages/en",
          "type": "Concept",
          "prefLabel": {
            "en": "English"
          }
        },
        "displayDetail": [
          {
            "id": "urn:display:detail-1",
            "type": "DisplayDetail",
            "image": {
              "id": "urn:media:certificate-image",
              "type": "MediaObject",
              "contentType": {
                "id": "https://www.iana.org/assignments/media-types/image/png",
                "type": "Concept",
                "prefLabel": {
                  "en": "image/png"
                }
              },
              "contentEncoding": {
                "id": "https://www.iana.org/assignments/character-sets/base64",
                "type": "Concept",
                "prefLabel": {
                  "en": "base64"
                }
              },
              "content": "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAACklEQVR4nGMAAQAABQABDQottAAAAABJRU5ErkJggg=="
            },
            "page": 1
          }
        ]
      }
    ]
  },
  "issuer": {
    "id": "did:ebsi:987654321",
    "type": "Organisation",
    "legalName": {
      "en": "Barcelona Vocational Training Institute"
    },
    "location": {
      "id": "urn:location:vet-institute-barcelona",
      "type": "Location",
      "address": [
        {
          "id": "urn:address:vet-institute-barcelona",
          "type": "Address",
          "countryCode": {
            "id": "https://id.eesc.europa.eu/countries/ES",
            "type": "Concept",
            "prefLabel": {
              "en": "Spain"
            }
          },
          "fullAddress": {
            "id": "urn:note:address",
            "type": "Note",
            "noteLiteral": {
              "en": "Gran Via de les Corts Catalanes, 585, 08007 Barcelona, Spain"
            }
          }
        }
      ]
    }
  },
  "credentialSubject": {
    "id": "did:ebsi:123456789",
    "type": "Person",
    "dateOfBirth": "1995-05-15T00:00:00Z",
    "familyName": {
      "en": "Doe"
    },
    "givenName": {
      "en": "John"
    },
    "hasClaim": [
      {
        "id": "urn:claim:vet-digital-skills",
        "type": "LearningAchievement",
        "title": {
          "en": "Vocational Digital Skills Training Microcredential",
          "es": "Microcredencial de Formación en Competencias Digitales Vocacionales"
        },
        "description": {
          "en": "Completion of a vocational training microcredential in digital skills, covering basic digital tools and applications."
        },
        "awardedBy": {
          "id": "urn:awarding:vet-institute-barcelona",
          "type": "AwardingProcess",
          "awardingBody": {
            "id": "did:ebsi:987654321",
            "type": "Organisation",
            "legalName": {
              "en": "Barcelona Vocational Training Institute"
            },
            "location": {
              "id": "urn:location:vet-institute-barcelona",
              "type": "Location",
              "address": [
                {
                  "id": "urn:address:vet-institute-barcelona",
                  "type": "Address",
                  "countryCode": {
                    "id": "https://id.eesc.europa.eu/countries/ES",
                    "type": "Concept",
                    "prefLabel": {
                      "en": "Spain"
                    }
                  },
                  "fullAddress": {
                    "id": "urn:note:address",
                    "type": "Note",
                    "noteLiteral": {
                      "en": "Gran Via de les Corts Catalanes, 585, 08007 Barcelona, Spain"
                    }
                  }
                }
              ]
            }
          },
          "awardingDate": "2025-07-01T09:00:00Z",
          "location": {
            "id": "urn:location:vet-institute-barcelona",
            "type": "Location",
            "address": [
              {
                "id": "urn:address:vet-institute-barcelona",
                "type": "Address",
                "countryCode": {
                  "id": "https://id.eesc.europa.eu/countries/ES",
                  "type": "Concept",
                  "prefLabel": {
                    "en": "Spain"
                  }
                },
                "fullAddress": {
                  "id": "urn:note:address",
                  "type": "Note",
                  "noteLiteral": {
                    "en": "Gran Via de les Corts Catalanes, 585, 08007 Barcelona, Spain"
                  }
                }
              }
            ]
          }
        },
        "specifiedBy": {
          "id": "urn:spec:vet-digital-skills",
          "type": "Qualification",
          "creditPoint": [
            {
              "id": "urn:credit:ecvet-3",
              "type": "CreditPoint",
              "framework": {
                "id": "urn:framework:ecvet",
                "type": "Concept",
                "notation": "ECVET"
              },
              "point": "3"
            }
          ],
          "educationSubject": [
            {
              "id": "https://digcomp.europa.eu/competence/1.1",
              "type": "Concept",
              "prefLabel": {
                "en": "Browsing, searching and filtering data, information and digital content"
              }
            }
          ],
          "mode": [
            {
              "id": "http://data.europa.eu/esco/concept/1234",
              "type": "Concept",
              "prefLabel": {
                "en": "Online"
              }
            }
          ],
          "eqfLevel": {
            "id": "urn:eqf:level-4",
            "type": "Concept",
            "notation": "4"
          }
        },
        "provenBy": [
          {
            "id": "urn:assessment:vet-digital-skills",
            "type": "LearningAssessment",
            "grade": {
              "id": "urn:grade:vet-digital-skills",
              "type": "Note",
              "noteLiteral": {
                "en": "Pass"
              }
            },
            "specifiedBy": {
              "id": "urn:spec:assessment-digital-skills",
              "type": "LearningAssessmentSpecification",
              "title": {
                "en": "Digital Skills Assessment"
              }
            },
            "awardedBy": {
              "id": "urn:awarding:assessment-vet-institute",
              "type": "AwardingProcess",
              "awardingBody": {
                "id": "did:ebsi:987654321",
                "type": "Organisation",
                "legalName": {
                  "en": "Barcelona Vocational Training Institute"
                },
                "location": {
                  "id": "urn:location:vet-institute-barcelona",
                  "type": "Location",
                  "address": [
                    {
                      "id": "urn:address:vet-institute-barcelona",
                      "type": "Address",
                      "countryCode": {
                        "id": "https://id.eesc.europa.eu/countries/ES",
                        "type": "Concept",
                        "prefLabel": {
                          "en": "Spain"
                        }
                      },
                      "fullAddress": {
                        "id": "urn:note:address",
                        "type": "Note",
                        "noteLiteral": {
                          "en": "Gran Via de les Corts Catalanes, 585, 08007 Barcelona, Spain"
                        }
                      }
                    }
                  ]
                }
              }
            }
          }
        ]
      }
    ]
  },
  "issuanceDate": "2025-07-01T09:00:00Z",
  "issued": "2025-07-01T09:00:00Z",
  "validFrom": "2025-07-01T09:00:00Z",
  "credentialSchema": [
    {
      "id": "https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/0xe9d256a96313a24d5884d56f0835047febc0ebf46fbdd20c906f49057a1e0f02",
      "type": "JsonSchema"
    },
    {
      "id": "https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/0x690878adbdbc2c6b2865829003a1e34800df5d173d302ff11958836f8f977a26",
      "type": "JsonSchema"
    }
  ],
  "credentialStatus": [
    {
      "id": "urn:status:7b8c9d0e-f12a-43b5-9c7d-558766221111",
      "type": "StatusList2021Entry",
      "statusPurpose": "revocation",
      "statusListIndex": "0",
      "statusListCredential": "https://api-pilot.ebsi.eu/status-list/2025/07"
    }
  ]
}
```