{
  "@context": [
    "https://www.w3.org/2018/credentials/v1",
    "https://essif.europa.eu/schemas/vc-context/v1"
  ],
  "id": "urn:credential:45ddc1d3-4af8-44cf-9237-51a147e54694",
  "type": ["VerifiableCredential", "VerifiableAttestation", "JointDegreeCredential"],
  "issuer": {
    "id": "did:ebsi:issuer:abcd1234efgh5678ijkl9012",
    "name": "Umeå University",
    "homepage": "http://www.umu.se/english/?languageId=1"
  },
  "issuanceDate": "2023-01-01T00:00:00Z",
  "credentialSubject": {
    "id": "did:ebsi:person:87654321abcdef1234567890",
    "givenName": {"en": ["Ana"]},
    "familyName": {"en": ["Andromeda"]},
    "fullName": {"en": ["Ana Andromeda"]},
    "dateOfBirth": "1999-10-02T00:00:00Z",
    "nationalID": {
      "notation": "IT-12345678",
      "country": "Italy"
    },
    "citizenshipCountry": [{
      "id": "http://publications.europa.eu/resource/authority/country/ITA",
      "prefLabel": {"en": ["Italy"]},
      "notation": "country"
    }],
    "hasClaim": [{
      "id": "urn:epass:learningAchievement:11",
      "type": "LearningAchievement",
      "awardedBy": {
        "awardingBody": [{
          "legalName": {"en": ["Umeå University"]},
          "location": [{
            "address": [{
              "countryCode": {
                "id": "http://publications.europa.eu/resource/authority/country/SWE",
                "prefLabel": {"en": ["Sweden"]},
                "notation": "country"
              }
            }]
          }]
        }]
      }
    }]
  },
  "credentialSchema": {
    "id": "https://schema.ebsi.eu/education/joint-degree-v1",
    "type": "JsonSchemaValidator2018"
  }
}
