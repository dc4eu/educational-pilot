# Doctor ID Schema

## Overview

The Doctor ID Schema defines the data structure for representing identity credentials of physicians.

## Schema Structure

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://eaa-rulebook.europa.eu/schemas/doctor-id/0.0.1",
  "title": "Doctor ID",
  "description": "Schema for physicians identity credentials",
  "type": "object",
  "properties": {
    "@context": {
      "type": "array",
      "description": "JSON-LD context",
      "items": {
        "type": "string"
      },
      "default": [
        "https://www.w3.org/2018/credentials/v1",
        "https://eaa-rulebook.europa.eu/2023/credentials/doctor-id/v01"
      ]
    },
    "id": {
      "type": "string",
      "format": "uri",
      "description": "Unique identifier for the doctor ID credential"
    },
    "type": {
      "type": "array",
      "description": "Credential type definitions",
      "items": {
        "type": "string"
      },
      "default": ["VerifiableCredential", "DoctorIdCredential"]
    },
    "issuer": {
      "type": "object",
      "description": "Information about the issuing institution",
      "properties": {
        "id": {
          "type": "string",
          "format": "uri",
          "description": "Unique identifier of the issuing institution"
        },
        "name": {
          "type": "object",
          "description": "Multilingual name of the issuing institution",
          "additionalProperties": {
            "type": "string"
          }
        }
      },
      "required": ["id", "name"]
    },
    "issuanceDate": {
      "type": "string",
      "format": "date",
      "description": "Date when the doctor ID was issued"
    },
    "credentialSubject": {
      "type": "object",
      "description": "Information about the doctor and their status",
      "properties": {
        "id": {
          "type": "string"
        },
        "givenName": {
          "description": "Current first name(s), including middle name(s) where applicable, of the doctor.",  
          "type": "string"
        },
        "familyName": {
          "description": "Current last name(s) or surname(s) of the doctor.",
          "type": "string"
        },
        "medical_board": {
          "description": "Corresponds to the regional professional body of physicians where the professional is registered.",
          "type": "array",
             "items": {
               "type": "string",
               "enum": [
                  "Álava/Áraba",
                  "Albacete",
                  "Alicante",
                  "Almería",
                  "Ávila",
                  "Badajoz",
                  "Islas Baleares/Illes Balears",
                  "Barcelona",
                  "Burgos",
                  "Cáceres",
                  "Cádiz",
                  "Castellón",
                  "Ciudad Real",
                  "Córdoba",
                  "La Coruña/A Coruña",
                  "Cuenca",
                  "Gerona/Girona",
                  "Granada",
                  "Guadalajara",
                  "Guipúzcoa/Gipuzkoa",
                  "Huelva",
                  "Huesca",
                  "Jaén",
                  "León",
                  "Lérida/Lleida",
                  "La Rioja",
                  "Lugo",
                  "Madrid",
                  "Málaga",
                  "Murcia",
                  "Navarra",
                  "Orense/Ourense",
                  "Asturias",
                  "Palencia",
                  "Las Palmas",
                  "Pontevedra",
                  "Salamanca",
                  "Santa Cruz de Tenerife",
                  "Cantabria",
                  "Segovia",
                  "Sevilla",
                  "Soria",
                  "Tarragona",
                  "Teruel",
                  "Toledo",
                  "Valencia",
                  "Valladolid",
                  "Vizcaya/Bizkaia",
                  "Zamora",
                  "Zaragoza",
                  "Ceuta",
                  "Melilla"
               ]
             }
        },
        "personal_administrative_number": {
          "description": "Identification number of the registered physician.",
          "type": "string",
          "pattern": "([0-9]{9})"
        },
        "legally_entitled": {
          "description": "Defines whether the professional is considered to be qualified to practise medicine, and there is no record of the professional having been sanctioned or disqualified from practising as a doctor..",
          "type": "boolean"
        },
        "medical_speciality": {
          "description": "Code representing the clinical specialty of the clinician or provider who interacted with, treated, or provided a service to/for the patient",
          "type": "array",
          "items": {
                    "type": "string",
                    "enum": [
                        "Allergology",
                        "Clinical Analysis",
                        "Pathological Anatomy",
                        "Anesthesiology and Reanimation",
                        "Angiology and Vascular Surgery",
                        "Digestive System",
                        "Clinical Biochemistry",
                        "Cardiology",
                        "Cardiovascular Surgery",
                        "General and Digestive Surgery",
                        "Oral and Maxillofacial Surgery",
                        "Orthopedic Surgery and Traumatology",
                        "Pediatric Surgery",
                        "Plastic, Aesthetic, and Reconstructive Surgery",
                        "Thoracic Surgery",
                        "Medical-Surgical Dermatology and Venereology",
                        "Endocrinology and Nutrition",
                        "Stomatology",
                        "Clinical Pharmacology",
                        "Geriatrics",
                        "Medical Hydrology",
                        "Hematology and Hemotherapy",
                        "Immunology",
                        "Occupational Medicine",
                        "Family and Community Medicine",
                        "Physical Education and Sports Medicine",
                        "Forensic Medicine",
                        "Physical Medicine and Rehabilitation",
                        "Intensive Medicine",
                        "Internal Medicine",
                        "Nuclear Medicine",
                        "Preventive Medicine and Public Health",
                        "Microbiology and Parasitology",
                        "Nephrology",
                        "Pulmonology",
                        "Neurosurgery",
                        "Clinical Neurophysiology",
                        "Neurology",
                        "Obstetrics and Gynecology",
                        "Ophthalmology",
                        "Medical Oncology",
                        "Radiation Oncology",
                        "Otorhinolaryngology",
                        "Pediatrics and its Specific Areas",
                        "Psychiatry",
                        "Radiology",
                        "Rheumatology",
                        "Urology",
                        "General Medicine",
                        "Child and Adolescent Psychiatry",
                        "Certified General Physician"
                    ]
                }
        }
      },
      "required": [ "id", "givenName", "familyName", "personal_administrative_number", "medical_speciality"]
    },
    "proof": {
      "type": "object",
      "description": "Cryptographic proof of the credential",
      "properties": {
        "type": {
          "type": "string",
          "description": "Type of proof"
        },
        "created": {
          "type": "string",
          "format": "date-time",
          "description": "Date and time when the proof was created"
        },
        "proofPurpose": {
          "type": "string",
          "description": "Purpose of the proof"
        },
        "verificationMethod": {
          "type": "string",
          "format": "uri",
          "description": "Method used to verify the proof"
        },
        "proofValue": {
          "type": "string",
          "description": "Value of the proof"
        }
      },
      "required": ["type", "created", "proofPurpose", "verificationMethod", "proofValue"]
    }
  },
  "required": ["@context", "id", "type", "issuer", "issuanceDate", "expirationDate", "credentialSubject"]
}
```

## Example Credential

[Doctor ID example](./examples/DoctorID.json)

## Schema Versioning

- **Version**: 0.0.1
- **Last Updated**: 2025-03-27
- **Status**: Draft

## Implementation Considerations

When implementing this schema:

- Ensure all required fields are provided
- Support multilingual representation of key information
- Implement appropriate privacy protections for personal information
- Include only necessary personal data
- Use standardised classification systems for medical specialities
- Consider selective disclosure requirements for sensitive attributes

## Extensions

The schema can be extended to support:

- Additional institution-specific requirements
