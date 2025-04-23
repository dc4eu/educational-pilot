json
```
Schema
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Professional Medical Certifications",
  "description": "Schema defining a verifiable credential associated with a registered physician",
  "type": "object",
  "allOf": [
    {
      "$ref": "./node_modules/@cef-ebsi/vcdm1.1-attestation-schema/schema.json"
    },
    {
      "properties": {
        "credentialSubject": {
          "description": "Board Certified Doctor Credential",
          "type": "object",
          "properties": {
            "medical_license_number": {
              "description": "Nationally registered physician number",
              "type": "string"
            },
            "name": {
              "description": "Natural person name",
              "type": "string"
            },
            "surname": {
              "description": "Natural person surname",
              "type": "string"
            },
            "medical_registration_status": {
              "description": "The status of the registered physician",
              "type": "string",
              "enum": ["ACTIVE", "LEAVE", "INHABILITED"]
            },
            "medical_practice_authorization": {
              "description": "Indicates if the physician is authorized to act",
              "type": "string"
            },
            "medical_board": {
              "description": "Corresponds to the official college of physicians where the professional is registered.",
              "type": "boolean"
            },
            "medical_specialties": {
              "description": "Describes the physician's professional specialization",
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
          "required": [
            "medical_license_number",
            "name",
            "surname",
            "medical_registration_status",
            "medical_practice_authorization",
            "medical_board",
            "medical_specialties"
          ]
        }
      }
    }
  ]
}
```
