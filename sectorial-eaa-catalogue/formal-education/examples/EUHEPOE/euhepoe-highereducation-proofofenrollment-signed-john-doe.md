#EUHEPOE Partially Constructed Signed Credential (JWS)
The jws field in the artifact includes:

header: A JSON object with the required JAdES D-Zero fields (alg: ES256, typ: jades-d-z, cty: vc+ld+json, kid, crit, sigT, sigPl).
header_base64url: The Base64URL-encoded header.
payload_base64url: The Base64URL-encoded unsigned credential (partially shown due to length).
signature_base64url: A placeholder ([signature-placeholder]) instead of an actual signature, as generating a valid ES256 signature requires the issuer’s private key, which is not provided.
compact_jws: The JWS compact serialisation (Header.Payload.Signature), with the placeholder signature.

This represents the signed credential in JAdES D-Zero format, but it is incomplete due to the placeholder signature. In a real implementation, the issuer (e.g., University of Barcelona) would compute an actual ES256 signature using their private key, replacing [signature-placeholder].


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
    "EuropeanHigherEducationProofOfEnrolment"
  ],
  "identifier": [
    {
      "id": "urn:identifier:123457789-POE-2025",
      "type": "Identifier",
      "notation": "123457789-POE-2025",
      "schemeAgency": {
        "en": "University of Barcelona"
      },
      "dateIssued": "2025-07-01T09:00:00Z"
    }
  ],
  "credentialProfiles": [
    {
      "id": "https://data.europa.eu/europass/credential-profiles/proof-of-enrolment-v1",
      "type": "Concept",
      "prefLabel": {
        "en": "Higher Education Proof of Enrolment Profile v1"
      }
    }
  ],
  "displayParameter": {
    "id": "urn:display:john-doe-proof-of-enrolment",
    "type": "DisplayParameter",
    "title": {
      "en": "Proof of Enrolment in Bachelor’s Degree in Digital Competences",
      "es": "Prueba de Matriculación en Grado en Competencias Digitales"
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
        "id": "urn:claim:enrolment-digital-competences",
        "type": "LearningAchievement",
        "title": {
          "en": "Enrolment in Bachelor’s Degree in Digital Competences",
          "es": "Matriculación en Grado en Competencias Digitales"
        },
        "description": {
          "en": "Proof of active enrolment in a bachelor’s degree programme in digital competences at the University of Barcelona."
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
        "specifiedBy": {
          "id": "urn:spec:enrolment-digital-competences",
          "type": "Qualification",
          "creditPoint": [
            {
              "id": "urn:credit:ects-180",
              "type": "CreditPoint",
              "framework": {
                "id": "urn:framework:ects",
                "type": "Concept",
                "notation": "ECTS"
              },
              "point": "180"
            }
          ],
          "duration": "P3Y"
        }
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
      "id": "https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/0x9e7bdbe465fbca504ec04df331c47ef6d88eb258312d3471277e84dabda4a92e",
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
    "payload_base64url": "eyJAY29udGV4dCI6WyJodHRwczovL3d3dy53My5vcmcvMjAxOC9jcmVkZW50aWFscy92MSIsImh0dHBzOi8vYXBpLXBpbG90LmVic2kuZXUvdHJ1c3RlZC1zY2hlbWFzLXJlZ2lzdHJ5L3YzL2NvbnRleHRzL2V1cm9wZWFuLWRpZ2l0YWwtY3JlZGVudGlhbC12My5qc29ubGQiXSwiaWQiOiJ1cm46dXVpZDo3YjhjOWQwZS1mMTJhLTQzYjUtOWM3ZC01NTg3NjYyMjExMTEiLCJ0eXBlIjpbIlZlcmlmaWFibGVDcmVkZW50aWFsIiwiVmVyaWZpYWJsZUF0dGVzdGF0aW9uIiwiRXVyb3BlYW5EaWdpdGFsQ3JlZGVudGlhbCIsIkV1cm9wZWFuSGlnaGVyRWR1Y2F0aW9uUHJvb2ZPZkVucm9sbWVudCJdLCJpZGVudGlmaWVyIjpbeyJpZCI6InVybjppZGVudGlmaWVyOjEyMzQ1Nzc4OS1QT0UtMjAyNSIsInR5cGUiOiJJZGVudGlmaWVyIiwibm90YXRpb24iOiIxMjM0NTc3ODktUE9FLTIwMjUiLCJzY2hlbWVBZ2VuY3kiOnsiZW4iOiJVbml2ZXJzaXR5IG9mIEJhcmNlbG9uYSJ9LCJkYXRlSXNzdWVkIjoiMjAyNS0wNy0wMVQwOTowMDowMFoifV0sImNyZWRlbnRpYWxQcm9maWxlcyI6W3siaWQiOiJodHRwczovL2RhdGEuZXVyb3BhLmV1L2V1cm9wYXNzL2NyZWRlbnRpYWwtcHJvZmlsZXMvcHJvb2Ytb2YtZW5yb2xtZW50LXYxIiwidHlwZSI6IkNvbmNlcnQiLCJwcmVmTGFiZWwiOnsiZW4iOiJIaWdoZXIgRWR1Y2F0aW9uIFByb29mIG9mIEVucm9sbWVudCBQcm9maWxlIHYxIn19XSwiZGlzcGxheVBhcmFtZXRlciI6eyJpZCI6InVybjpk
    ",
    "signature_base64url": "[signature-placeholder]",
    "compact_jws": "eyJhbGciOiJFUzI1NiIsInR5cCI6ImphZGVzLWQteiIsImN0eSI6InZjK2xkK2pzb24iLCJraWQiOiJkaWQ6ZWJzaTo5ODc2NTQzMjEja2V5LTEiLCJjcml0IjpbInNpZ1QiLCJzaWdQbCJdLCJzaWdUIjoiMjAyNS0wNy0wMVQwOTowMDowMFoiLCJzaWdQbCI6eyJhZGRyZXNzQ291bnRyeSI6IkVTIiwiYWRkcmVzc0xvY2FsaXR5IjoiQmFyY2Vsb25hIiwicG9zdGFsQ29kZSI6IjA4MDA3Iiwic3RyZWV0QWRkcmVzcyI6IkdyYW4gVmlhIGRlIGxlcyBDb3J0cyBDYXRhbGFuZXMsIDU4NSJ9fQ.eyJAY29udGV4dCI6WyJodHRwczovL3d3dy53My5vcmcvMjAxOC9jcmVkZW50aWFscy92MSIsImh0dHBzOi8vYXBpLXBpbG90LmVic2kuZXUvdHJ1c3RlZC1zY2hlbWFzLXJlZ2lzdHJ5L3YzL2NvbnRleHRzL2V1cm9wZWFuLWRpZ2l0YWwtY3JlZGVudGlhbC12My5qc29ubGQiXSwiaWQiOiJ1cm46dXVpZDo3YjhjOWQwZS1mMTJhLTQzYjUtOWM3ZC01NTg3NjYyMjExMTEiLCJ0eXBlIjpbIlZlcmlmaWFibGVDcmVkZW50aWFsIiwiVmVyaWZpYWJsZUF0dGVzdGF0aW9uIiwiRXVyb3BlYW5EaWdpdGFsQ3JlZGVudGlhbCIsIkV1cm9wZWFuSGlnaGVyRWR1Y2F0aW9uUHJvb2ZPZkVucm9sbWVudCJdLCJpZGVudGlmaWVyIjpbeyJpZCI6InVybjppZGVudGlmaWVyOjEyMzQ1Nzc4OS1QT0UtMjAyNSIsInR5cGUiOiJJZGVudGlmaWVyIiwibm90YXRpb24iOiIxMjM0NTc3ODktUE9FLTIwMjUiLCJzY2hlbWVBZ2VuY3kiOnsiZW4iOiJVbml2ZXJzaXR5IG9mIEJhcmNlbG9uYSJ9LCJkYXRlSXNzdWVkIjoiMjAyNS0wNy0wMVQwOTowMDowMFoifV0sImNyZWRlbnRpYWxQcm9maWxlcyI6W3siaWQiOiJodHRwczovL2RhdGEuZXVyb3BhLmV1L2V1cm9wYXNzL2NyZWRlbnRpYWwtcHJvZmlsZXMvcHJvb2Ytb2YtZW5yb2xtZW50LXYxIiwidHlwZSI6IkNvbmNlcnQiLCJwcmVmTGFiZWwiOnsiZW4iOiJIaWdoZXIgRWR1Y2F0aW9uIFByb29mIG9mIEVucm9sbWVudCBQcm9maWxlIHYxIn19XSwiZGlzcGxheVBhcmFtZXRlciI6eyJpZCI6InVybjpk
    .[signature-placeholder]"
  }
}
```