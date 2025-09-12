```json
{
      "id": "did:ebsi:123456789",
      "type": "Person",
      "dateOfBirth": "1995-05-15T00:00:00Z",
      "familyName": { "en": "Doe" },
      "givenName": { "en": "John" },
      "hasClaim": [
        {
          "id": "urn:claim:digital-competences",
          "type": "LearningAchievement",
          "title": { "en": "Microcredential in Digital Competences", "es": "Microcredencial en Competencias Digitales" },
          "description": { "en": "Completion of a higher education microcredential programme in digital competences." },
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
          "provenBy": [
            {
              "id": "urn:assessment:digital-competences",
              "type": "LearningAssessment",
              "title": { "en": "Digital Competences Assessment" },
              "grade": {
                "id": "urn:grade:digital-competences",
                "type": "Note",
                "noteLiteral": { "en": "Pass" }
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
                "id": "urn:spec:assessment-digital-competences",
                "type": "LearningAssessmentSpecification",
                "title": { "en": "Digital Competences Assessment Specification" }
              }
            }
          ],
          "specifiedBy": {
            "id": "urn:spec:digital-competences",
            "type": "Qualification",
            "title": { "en": "Qualification in Digital Competences", "es": "Cualificación en Competencias Digitales" },
            "creditPoint": [
              {
                "id": "urn:credit:ects-3",
                "type": "CreditPoint",
                "framework": {
                  "id": "urn:framework:ects",
                  "type": "Concept",
                  "notation": "ECTS"
                },
                "point": "3"
              }
            ],
            "mode": [
              {
                "id": "http://data.europa.eu/esco/concept/1234",
                "type": "Concept",
                "prefLabel": { "en": "Blended" }
              }
            ],
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
            ]
          }
        }
      ]
 }
```