# EUHETOR Unsigned Credential
The unsigned_credential field in the artifact contains the full JSON-LD representation of the European Higher Education Transcript of Records (EUHETOR) without a signature. This is the payload that would be signed using the JAdES D-Zero profile.
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
    "EuropeanHigherEducationTranscriptOfRecords"
  ],
  "identifier": [
    {
      "id": "urn:identifier:123457789-TOR-2025",
      "type": "Identifier",
      "notation": "123457789-TOR-2025",
      "schemeAgency": {
        "en": "University of Barcelona"
      },
      "dateIssued": "2025-07-01T09:00:00Z"
    }
  ],
  "credentialProfiles": [
    {
      "id": "https://data.europa.eu/europass/credential-profiles/transcript-of-records-v1",
      "type": "Concept",
      "prefLabel": {
        "en": "Higher Education Transcript of Records Profile v1"
      }
    }
  ],
  "displayParameter": {
    "id": "urn:display:john-doe-transcript",
    "type": "DisplayParameter",
    "title": {
      "en": "Transcript of Records for Bachelor’s Degree in Digital Competences",
      "es": "Certificado de Notas para Grado en Competencias Digitales"
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
      "en": "University of Barcelona"
    },
    "location": {
      "id": "urn:location:university-barcelona",
      "type": "Location",
      "address": [
        {
          "id": "urn:address:university-barcelona",
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
        "id": "urn:claim:transcript-digital-competences",
        "type": "LearningAchievement",
        "title": {
          "en": "Transcript of Records for Bachelor’s Degree in Digital Competences",
          "es": "Certificado de Notas para Grado en Competencias Digitales"
        },
        "description": {
          "en": "Academic transcript detailing courses completed in a bachelor’s degree programme in digital competences."
        },
        "awardedBy": {
          "id": "urn:awarding:university-barcelona",
          "type": "AwardingProcess",
          "awardingBody": {
            "id": "did:ebsi:987654321",
            "type": "Organisation",
            "legalName": {
              "en": "University of Barcelona"
            },
            "location": {
              "id": "urn:location:university-barcelona",
              "type": "Location",
              "address": [
                {
                  "id": "urn:address:university-barcelona",
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
          "location": {
            "id": "urn:location:university-barcelona",
            "type": "Location",
            "address": [
              {
                "id": "urn:address:university-barcelona",
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
        "wasDerivedFrom": [
          {
            "id": "urn:assessment:digital-literacy",
            "type": "LearningAssessment",
            "title": {
              "en": "Digital Literacy Course"
            },
            "creditPoint": [
              {
                "id": "urn:credit:ects-6",
                "type": "CreditPoint",
                "framework": {
                  "id": "urn:framework:ects",
                  "type": "Concept",
                  "notation": "ECTS"
                },
                "point": "6"
              }
            ],
            "grade": {
              "id": "urn:grade:digital-literacy",
              "type": "Note",
              "noteLiteral": {
                "en": "85/100"
              }
            },
            "temporal": {
              "id": "urn:temporal:digital-literacy",
              "type": "PeriodOfTime",
              "startDate": "2024-09-01",
              "endDate": "2024-12-15"
            }
          },
          {
            "id": "urn:assessment:web-technologies",
            "type": "LearningAssessment",
            "title": {
              "en": "Web Technologies Course"
            },
            "creditPoint": [
              {
                "id": "urn:credit:ects-6",
                "type": "CreditPoint",
                "framework": {
                  "id": "urn:framework:ects",
                  "type": "Concept",
                  "notation": "ECTS"
                },
                "point": "6"
              }
            ],
            "grade": {
              "id": "urn:grade:web-technologies",
              "type": "Note",
              "noteLiteral": {
                "en": "90/100"
              }
            },
            "temporal": {
              "id": "urn:temporal:web-technologies",
              "type": "PeriodOfTime",
              "startDate": "2024-09-01",
              "endDate": "2024-12-15"
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
      "id": "https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/0x1e4611b4d031fbd282e6cfc241623d3b25f322ed87aee7670f7c1a20a63c14f3",
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