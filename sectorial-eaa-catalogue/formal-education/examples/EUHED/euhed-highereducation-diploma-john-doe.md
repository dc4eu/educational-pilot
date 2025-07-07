# EUHED Unsigned Credential
The unsigned_credential field in the artifact contains the full JSON-LD representation of the European Higher Education Diploma (EUHED) without a signature. This is the payload that would be signed using the JAdES D-Zero profile.
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
    "EuropeanHigherEducationDiploma"
  ],
  "identifier": [
    {
      "id": "urn:identifier:123457789-DIP-2025",
      "type": "Identifier",
      "notation": "123457789-DIP-2025",
      "schemeAgency": { "en": "University of Barcelona" },
      "dateIssued": "2025-07-01T09:00:00Z"
    }
  ],
  "credentialProfiles": [
    {
      "id": "https://data.europa.eu/europass/credential-profiles/diploma-v1",
      "type": "Concept",
      "prefLabel": { "en": "Higher Education Diploma Profile v1" }
    }
  ],
  "displayParameter": {
    "id": "urn:display:john-doe-diploma",
    "type": "DisplayParameter",
    "title": { "en": "Bachelor’s Degree in Digital Competences", "es": "Grado en Competencias Digitales" },
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
        "id": "urn:claim:digital-competences-diploma",
        "type": "LearningAchievement",
        "title": { "en": "Bachelor’s Degree in Digital Competences", "es": "Grado en Competencias Digitales" },
        "description": { "en": "Completion of a higher education bachelor’s degree programme in digital competences, covering advanced digital skills and technologies." },
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
          "id": "urn:spec:digital-competences-diploma",
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
          "additionalNote": [
            {
              "id": "urn:note:diploma-details",
              "type": "Note",
              "noteLiteral": { "en": "180 ECTS credits, 3-year programme" }
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
      "id": "https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/0x7663df08b9a50f226e185efb7ec08f3d69f4a95e653ebffd3137b3eb6923dda8",
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
````