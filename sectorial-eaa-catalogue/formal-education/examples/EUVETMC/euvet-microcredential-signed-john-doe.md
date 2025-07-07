# EUVETMC Partially Constructed Signed Credential (JWS)
The jws field in the artifact includes:

header: A JSON object with the required JAdES D-Zero fields (alg: ES256, typ: jades-d-z, cty: vc+ld+json, kid, crit, sigT, sigPl).
header_base64url: The Base64URL-encoded header.
payload_base64url: The Base64URL-encoded unsigned credential (partially shown due to length).
signature_base64url: A placeholder ([signature-placeholder]) instead of an actual signature, as generating a valid ES256 signature requires the issuer’s private key, which is not provided.
compact_jws: The JWS compact serialisation (Header.Payload.Signature), with the placeholder signature.

This represents the signed credential in JAdES D-Zero format, but it is incomplete due to the placeholder signature. In a real implementation, the issuer (e.g., Barcelona Vocational Training Institute) would compute an actual ES256 signature using their private key, replacing [signature-placeholder].
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
},{
  "jws": {
    "header": {
      "alg": "ES256",
      "typ": "jades-d-z",
      "cty": "vc+ld+json",
      "kid": "did:ebsi:987654321#key-1",
      "crit": ["sigT", "sigPl"],
      "sigT": "2025-07-01T09:00:00Z",
      "sigPl": {
        "addressCountry": "ES",
        "addressLocality": "Barcelona",
        "postalCode": "08007",
        "streetAddress": "Gran Via de les Corts Catalanes, 585"
      }
    },
    "header_base64url": "eyJhbGciOiJFUzI1NiIsInR5cCI6ImphZGVzLWQteiIsImN0eSI6InZjK2xkK2pzb24iLCJraWQiOiJkaWQ6ZWJzaTo5ODc2NTQzMjEja2V5LTEiLCJjcml0IjpbInNpZ1QiLCJzaWdQbCJdLCJzaWdUIjoiMjAyNS0wNy0wMVQwOTowMDowMFoiLCJzaWdQbCI6eyJhZGRyZXNzQ291bnRyeSI6IkVTIiwiYWRkcmVzc0xvY2FsaXR5IjoiQmFyY2Vsb25hIiwicG9zdGFsQ29kZSI6IjA4MDA3Iiwic3RyZWV0QWRkcmVzcyI6IkdyYW4gVmlhIGRlIGxlcyBDb3J0cyBDYXRhbGFuZXMsIDU4NSJ9fQ",
    "payload_base64url": "eyJAY29udGV4dCI6WyJodHRwczovL3d3dy53My5vcmcvMjAxOC9jcmVkZW50aWFscy92MSIsImh0dHBzOi8vYXBpLXBpbG90LmVic2kuZXUvdHJ1c3RlZC1zY2hlbWFzLXJlZ2lzdHJ5L3YzL2NvbnRleHRzL2V1cm9wZWFuLWRpZ2l0YWwtY3JlZGVudGlhbC12My5qc29ubGQiXSwiaWQiOiJ1cm46dXVpZDo3YjhjOWQwZS1mMTJhLTQzYjUtOWM3ZC01NTg3NjYyMjExMTEiLCJ0eXBlIjpbIlZlcmlmaWFibGVDcmVkZW50aWFsIiwiVmVyaWZpYWJsZUF0dGVzdGF0aW9uIiwiRXVyb3BlYW5EaWdpdGFsQ3JlZGVudGlhbCIsIkV1cm9wZWFuVm9jYXRpb25hbEVkdWNhdGlvblRyYWluaW5nTWljcm9jcmVkZW50aWFsIl0sImlkZW50aWZpZXIiOlt7ImlkIjoidXJuOmlkZW50aWZpZXI6MTIzNDU3Nzg5LVZFVE1DLTIwMjUiLCJ0eXBlIjoiSWRlbnRpZmllciIsIm5vdGF0aW9uIjoiMTIzNDU3Nzg5LVZFVE1DLTIwMjUiLCJzY2hlbWVBZ2VuY3kiOnsiZW4iOiJCYXJjZWxvbmEgVm9jYXRpb25hbCBUcmFpbmluZyBJbnN0aXR1dGUifSwiZGF0ZUlzc3VlZCI6IjIwMjUtMDctMDFUMDk6MDA6MDBaIn1dLCJjcmVkZW50aWFsUHJvZmlsZXMiOlt7ImlkIjoiaHR0cHM6Ly9kYXRhLmV1cm9wYS5ldS9ldXJvcGFzcy9jcmVkZW50aWFsLXByb2ZpbGVzL3ZldC1taWNyb2NyZWRlbnRpYWwtdjEiLCJ0eXBlIjoiQ29uY2VwdCIsInByZWZMYWJlbCI6eyJlbiI6IlZvY2F0aW9uYWwgRWR1Y2F0aW9uIGFuZCBUcmFpbmluZyBNaWNyb2NyZWRlbnRpYWwgUHJvZmlsZSB2MSJ9fV0sImRpc3BsYXlQYXJhbWV0ZXIiOnsiaWQiOiJ1cm46Z
    ",
    "signature_base64url": "[signature-placeholder]",
    "compact_jws": "eyJhbGciOiJFUzI1NiIsInR5cCI6ImphZGVzLWQteiIsImN0eSI6InZjK2xkK2pzb24iLCJraWQiOiJkaWQ6ZWJzaTo5ODc2NTQzMjEja2V5LTEiLCJjcml0IjpbInNpZ1QiLCJzaWdQbCJdLCJzaWdUIjoiMjAyNS0wNy0wMVQwOTowMDowMFoiLCJzaWdQbCI6eyJhZGRyZXNzQ291bnRyeSI6IkVTIiwiYWRkcmVzc0xvY2FsaXR5IjoiQmFyY2Vsb25hIiwicG9zdGFsQ29kZSI6IjA4MDA3Iiwic3RyZWV0QWRkcmVzcyI6IkdyYW4gVmlhIGRlIGxlcyBDb3J0cyBDYXRhbGFuZXMsIDU4NSJ9fQ.eyJAY29udGV4dCI6WyJodHRwczovL3d3dy53My5vcmcvMjAxOC9jcmVkZW50aWFscy92MSIsImh0dHBzOi8vYXBpLXBpbG90LmVic2kuZXUvdHJ1c3RlZC1zY2hlbWFzLXJlZ2lzdHJ5L3YzL2NvbnRleHRzL2V1cm9wZWFuLWRpZ2l0YWwtY3JlZGVudGlhbC12My5qc29ubGQiXSwiaWQiOiJ1cm46dXVpZDo3YjhjOWQwZS1mMTJhLTQzYjUtOWM3ZC01NTg3NjYyMjExMTEiLCJ0eXBlIjpbIlZlcmlmaWFibGVDcmVkZW50aWFsIiwiVmVyaWZpYWJsZUF0dGVzdGF0aW9uIiwiRXVyb3BlYW5EaWdpdGFsQ3JlZGVudGlhbCIsIkV1cm9wZWFuVm9jYXRpb25hbEVkdWNhdGlvblRyYWluaW5nTWljcm9jcmVkZW50aWFsIl0sImlkZW50aWZpZXIiOlt7ImlkIjoidXJuOmlkZW50aWZpZXI6MTIzNDU3Nzg5LVZFVE1DLTIwMjUiLCJ0eXBlIjoiSWRlbnRpZmllciIsIm5vdGF0aW9uIjoiMTIzNDU3Nzg5LVZFVE1DLTIwMjUiLCJzY2hlbWVBZ2VuY3kiOnsiZW4iOiJCYXJjZWxvbmEgVm9jYXRpb25hbCBUcmFpbmluZyBJbnN0aXR1dGUifSwiZGF0ZUlzc3VlZCI6IjIwMjUtMDctMDFUMDk6MDA6MDBaIn1dLCJjcmVkZW50aWFsUHJvZmlsZXMiOlt7ImlkIjoiaHR0cHM6Ly9kYXRhLmV1cm9wYS5ldS9ldXJvcGFzcy9jcmVkZW50aWFsLXByb2ZpbGVzL3ZldC1taWNyb2NyZWRlbnRpYWwtdjEiLCJ0eXBlIjoiQ29uY2VwdCIsInByZWZMYWJlbCI6eyJlbiI6IlZvY2F0aW9uYWwgRWR1Y2F0aW9uIGFuZCBUcmFpbmluZyBNaWNyb2NyZWRlbnRpYWwgUHJvZmlsZSB2MSJ9fV0sImRpc3BsYXlQYXJhbWV0ZXIiOnsiaWQiOiJ1cm46Z
    .[signature-placeholder]"
  }
}
```