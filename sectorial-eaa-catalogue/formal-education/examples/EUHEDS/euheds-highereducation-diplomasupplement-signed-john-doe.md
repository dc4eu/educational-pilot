#EUHEDS Partially Constructed Signed Credential (JWS)
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
    "EuropeanHigherEducationDiplomaSupplement"
  ],
  "identifier": [
    {
      "id": "urn:identifier:123457789-DIPS-2025",
      "type": "Identifier",
      "notation": "123457789-DIPS-2025",
      "schemeAgency": { "en": "University of Barcelona" },
      "dateIssued": "2025-07-01T09:00:00Z"
    }
  ],
  "credentialProfiles": [
    {
      "id": "https://data.europa.eu/europass/credential-profiles/diploma-supplement-v1",
      "type": "Concept",
      "prefLabel": { "en": "Higher Education Diploma Supplement Profile v1" }
    }
  ],
  "displayParameter": {
    "id": "urn:display:john-doe-diploma-supplement",
    "type": "DisplayParameter",
    "title": { "en": "Diploma Supplement for Bachelor’s Degree in Digital Competences", "es": "Suplemento al Título de Grado en Competencias Digitales" },
    "language": [
      {
        "id": "https://id.eesc.europa.eu/languages/en",
        "type": "Concept",
        "prefLabel": { "en": "English" }
      }
    ],
    "primaryLanguage": {
      "id": "https://id.eesc.europa.eu/languages/en",
      "type": "Concept",
      "prefLabel": { "en": "English" }
    },
    "individualDisplay": [
      {
        "id": "urn:display:individual-1",
        "type": "IndividualDisplay",
        "language": {
          "id": "https://id.eesc.europa.eu/languages/en",
          "type": "Concept",
          "prefLabel": { "en": "English" }
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
                "prefLabel": { "en": "image/png" }
              },
              "contentEncoding": {
                "id": "https://www.iana.org/assignments/character-sets/base64",
                "type": "Concept",
                "prefLabel": { "en": "base64" }
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
    "legalName": { "en": "University of Barcelona" },
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
            "prefLabel": { "en": "Spain" }
          },
          "fullAddress": {
            "id": "urn:note:address",
            "type": "Note",
            "noteLiteral": { "en": "Gran Via de les Corts Catalanes, 585, 08007 Barcelona, Spain" }
          }
        }
      ]
    }
  },
  "credentialSubject": {
    "id": "did:ebsi:123456789",
    "type": "Person",
    "dateOfBirth": "1995-05-15T00:00:00Z",
    "familyName": { "en": "Doe" },
    "givenName": { "en": "John" },
    "hasClaim": [
      {
        "id": "urn:claim:digital-competences-diploma-supplement",
        "type": "LearningAchievement",
        "title": { "en": "Diploma Supplement for Bachelor’s Degree in Digital Competences", "es": "Suplemento al Título de Grado en Competencias Digitales" },
        "description": { "en": "Diploma Supplement detailing the content and outcomes of a bachelor’s degree programme in digital competences, including courses and assessments." },
        "awardedBy": {
          "id": "urn:awarding:university-barcelona",
          "type": "AwardingProcess",
          "awardingBody": {
            "id": "did:ebsi:987654321",
            "type": "Organisation",
            "legalName": { "en": "University of Barcelona" },
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
                    "prefLabel": { "en": "Spain" }
                  },
                  "fullAddress": {
                    "id": "urn:note:address",
                    "type": "Note",
                    "noteLiteral": { "en": "Gran Via de les Corts Catalanes, 585, 08007 Barcelona, Spain" }
                  }
                }
              ]
            }
          },
          "awardingDate": "2025-07-01T09:00:00Z",
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
                  "prefLabel": { "en": "Spain" }
                }
              }
            ]
          }
        },
        "specifiedBy": {
          "id": "urn:spec:digital-competences-diploma-supplement",
          "type": "Qualification",
          "title": { "en": "Qualification in Digital Competences", "es": "Cualificación en Competencias Digitales" },
          "eqfLevel": {
            "id": "urn:eqf:level-6",
            "type": "Concept",
            "notation": "6"
          },
          "educationSubject": [
            {
              "id": "https://digcomp.europa.eu/competence/1.1",
              "type": "Concept",
              "prefLabel": { "en": "Browsing, searching and filtering data, information and digital content" }
            },
            {
              "id": "https://digcomp.europa.eu/competence/2.1",
              "type": "Concept",
              "prefLabel": { "en": "Interacting through digital technologies" }
            },
            {
              "id": "http://data.europa.eu/esco/skill/7a8b9c0d-5e6f-4b3a-9d8e-3c4d5e2f6a7b",
              "type": "Concept",
              "prefLabel": { "en": "Digital literacy" }
            }
          ],
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
          "mode": [
            {
              "id": "http://data.europa.eu/esco/concept/1234",
              "type": "Concept",
              "prefLabel": { "en": "Blended" }
            }
          ],
          "additionalNote": [
            {
              "id": "urn:note:diploma-supplement-details",
              "type": "Note",
              "noteLiteral": { "en": "180 ECTS credits, 3-year programme including coursework and final project" }
            }
          ]
        },
        "entitlesTo": [
          {
            "id": "urn:entitlement:master-eligibility",
            "type": "LearningEntitlement",
            "title": { "en": "Eligibility for Master’s Programme" },
            "awardedBy": {
              "id": "urn:awarding:master-eligibility",
              "type": "AwardingProcess",
              "awardingBody": {
                "id": "did:ebsi:987654321",
                "type": "Organisation",
                "legalName": { "en": "University of Barcelona" },
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
                        "prefLabel": { "en": "Spain" }
                      },
                      "fullAddress": {
                        "id": "urn:note:address",
                        "type": "Note",
                        "noteLiteral": { "en": "Gran Via de les Corts Catalanes, 585, 08007 Barcelona, Spain" }
                      }
                    }
                  ]
                }
              }
            }
          }
        ],
        "wasDerivedFrom": [
          {
            "id": "urn:assessment:digital-competences",
            "type": "LearningAssessment",
            "title": { "en": "Digital Competences Final Project" },
            "creditPoint": [
              {
                "id": "urn:credit:ects-30",
                "type": "CreditPoint",
                "framework": {
                  "id": "urn:framework:ects",
                  "type": "Concept",
                  "notation": "ECTS"
                },
                "point": "30"
              }
            ],
            "grade": {
              "id": "urn:grade:digital-competences",
              "type": "Note",
              "noteLiteral": { "en": "85/100" }
            },
            "temporal": {
              "id": "urn:temporal:final-project",
              "type": "PeriodOfTime",
              "startDate": "2025-01-01T00:00:00Z",
              "endDate": "2025-06-30T00:00:00Z"
            },
            "awardedBy": {
              "id": "urn:awarding:assessment-barcelona",
              "type": "AwardingProcess",
              "awardingBody": {
                "id": "did:ebsi:987654321",
                "type": "Organisation",
                "legalName": { "en": "University of Barcelona" },
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
                        "prefLabel": { "en": "Spain" }
                      },
                      "fullAddress": {
                        "id": "urn:note:address",
                        "type": "Note",
                        "noteLiteral": { "en": "Gran Via de les Corts Catalanes, 585, 08007 Barcelona, Spain" }
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
    "payload_base64url": "eyJAY29udGV4dCI6WyJodHRwczovL3d3dy53My5vcmcvMjAxOC9jcmVkZW50aWFscy92MSIsImh0dHBzOi8vYXBpLXBpbG90LmVic2kuZXUvdHJ1c3RlZC1zY2hlbWFzLXJlZ2lzdHJ5L3YzL2NvbnRleHRzL2V1cm9wZWFuLWRpZ2l0YWwtY3JlZGVudGlhbC12My5qc29ubGQiXSwiaWQiOiJ1cm46dXVpZDo3YjhjOWQwZS1mMTJhLTQzYjUtOWM3ZC01NTg3NjYyMjExMTEiLCJ0eXBlIjpbIlZlcmlmaWFibGVDcmVkZW50aWFsIiwiVmVyaWZpYWJsZUF0dGVzdGF0aW9uIiwiRXVyb3BlYW5EaWdpdGFsQ3JlZGVudGlhbCIsIkV1cm9wZWFuSGlnaGVyRWR1Y2F0aW9uRGlwbG9tYVN1cHBsZW1lbnQiXSwiaWRlbnRpZmllciI6W3siaWQiOiJ1cm46aWRlbnRpZmllcjoxMjM0NTc3ODktRElQUy0yMDI1IiwidHlwZSI6IklkZW50aWZpZXIiLCJub3RhdGlvbiI6IjEyMzQ1Nzc4OS1ESVBTLTIwMjUiLCJzY2hlbWVBZ2VuY3kiOnsiZW4iOiJVbml2ZXJzaXR5IG9mIEJhcmNlbG9uYSJ9LCJkYXRlSXNzdWVkIjoiMjAyNS0wNy0wMVQwOTowMDowMFoifV0sImNyZWRlbnRpYWxQcm9maWxlcyI6W3siaWQiOiJodHRwczovL2RhdGEuZXVyb3BhLmV1L2V1cm9wYXNzL2NyZWRlbnRpYWwtcHJvZmlsZXMvZGlwbG9tYS1zdXBwbGVtZW50LXYxIiwidHlwZSI6IkNvbmNlcnQiLCJwcmVmTGFiZWwiOnsiZW4iOiJIaWdoZXIgRWR1Y2F0aW9uIERpcGxvbWEgU3VwcGxlbWVudCBQcm9maWxlIHYxIn19XSwiZGlzcGxheVBhcmFtZXRlciI6eyJpZCI6InVybjpk
    ",
    "signature_base64url": "[signature-placeholder]",
    "compact_jws": "eyJhbGciOiJFUzI1NiIsInR5cCI6ImphZGVzLWQteiIsImN0eSI6InZjK2xkK2pzb24iLCJraWQiOiJkaWQ6ZWJzaTo5ODc2NTQzMjEja2V5LTEiLCJjcml0IjpbInNpZ1QiLCJzaWdQbCJdLCJzaWdUIjoiMjAyNS0wNy0wMVQwOTowMDowMFoiLCJzaWdQbCI6eyJhZGRyZXNzQ291bnRyeSI6IkVTIiwiYWRkcmVzc0xvY2FsaXR5IjoiQmFyY2Vsb25hIiwicG9zdGFsQ29kZSI6IjA4MDA3Iiwic3RyZWV0QWRkcmVzcyI6IkdyYW4gVmlhIGRlIGxlcyBDb3J0cyBDb3J0cyBDYXRhbGFuZXMsIDU4NSJ9fQ.eyJAY29udGV4dCI6WyJodHRwczovL3d3dy53My5vcmcvMjAxOC9jcmVkZW50aWFscy92MSIsImh0dHBzOi8vYXBpLXBpbG90LmVic2kuZXUvdHJ1c3RlZC1zY2hlbWFzLXJlZ2lzdHJ5L3YzL2NvbnRleHRzL2V1cm9wZWFuLWRpZ2l0YWwtY3JlZGVudGlhbC12My5qc29ubGQiXSwiaWQiOiJ1cm46dXVpZDo3YjhjOWQwZS1mMTJhLTQzYjUtOWM3ZC01NTg3NjYyMjExMTEiLCJ0eXBlIjpbIlZlcmlmaWFibGVDcmVkZW50aWFsIiwiVmVyaWZpYWJsZUF0dGVzdGF0aW9uIiwiRXVyb3BlYW5EaWdpdGFsQ3JlZGVudGlhbCIsIkV1cm9wZWFuSGlnaGVyRWR1Y2F0aW9uRGlwbG9tYVN1cHBsZW1lbnQiXSwiaWRlbnRpZmllciI6W3siaWQiOiJ1cm46aWRlbnRpZmllcjoxMjM0NTc3ODktRElQUy0yMDI1IiwidHlwZSI6IklkZW50aWZpZXIiLCJub3RhdGlvbiI6IjEyMzQ1Nzc4OS1ESVBTLTIwMjUiLCJzY2hlbWVBZ2VuY3kiOnsiZW4iOiJVbml2ZXJzaXR5IG9mIEJhcmNlbG9uYSJ9LCJkYXRlSXNzdWVkIjoiMjAyNS0wNy0wMVQwOTowMDowMFoifV0sImNyZWRlbnRpYWxQcm9maWxlcyI6W3siaWQiOiJodHRwczovL2RhdGEuZXVyb3BhLmV1L2V1cm9wYXNzL2NyZWRlbnRpYWwtcHJvZmlsZXMvZGlwbG9tYS1zdXBwbGVtZW50LXYxIiwidHlwZSI6IkNvbmNlcnQiLCJwcmVmTGFiZWwiOnsiZW4iOiJIaWdoZXIgRWR1Y2F0aW9uIERpcGxvbWEgU3VwcGxlbWVudCBQcm9maWxlIHYxIn19XSwiZGlzcGxheVBhcmFtZXRlciI6eyJpZCI6InVybjpk
    .[signature-placeholder]"
  }
}
```