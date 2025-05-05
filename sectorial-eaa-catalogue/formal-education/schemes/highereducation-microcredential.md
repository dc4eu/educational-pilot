# EUHEMC JSON Schema

The European Higher Education Microcredential (EUHEMC) JSON Schema defines the structure and constraints for issuing verifiable microcredentials based on the European Learning Model (ELM) 3.2 and EBSI Verifiable Credentials. Below is the schema, annotated with comments to highlight mandatory ELM elements and EUHEMC-specific requirements.


## Key Notes

The schema enforces mandatory ELM elements (e.g., PersonType, LearningAchievementType, LearningAssessmentType) and EUHEMC-specific requirements (e.g., 1–15 ECTS, at least one competence).
Comments (//) clarify which fields are mandatory and why, aiding developers in implementation and validation.
The schema is designed for use with EBSI’s JSON-LD Verifiable Credentials, ensuring interoperability and security.

## Schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "European Higher Education Microcredential (EUHEMC)",
  "description": "Schema for a microcredential of higher education based on ELM 3.2 and EBSI W3C-VC, issued by Rovira i Virgili University",
  "type": "object",
  "allOf": [
    { "$ref": "#/$defs/EuropeanDigitalCredentialType" },
    {
      "type": "object",
      "properties": {
        "type": {
          "type": "array",
          "items": { "type": "string" },
          "contains": [
            { "const": "EuropeanDigitalCredential" },
            { "const": "EuropeanHigherEducationMicroCredentials" }
          ],
          "minItems": 2,
          "uniqueItems": true,
          "//": "Mandatory: EUHEMC requires 'EuropeanDigitalCredential' and 'EuropeanHigherEducationMicroCredentials' in the type array to specify the credential subtype."
        },
        "credentialSubject": {
          "description": "Must include a PersonType with name, surname, and national ID, plus at least one LearningAchievement and LearningAssessment",
          "type": "object",
          "allOf": [
            { "$ref": "#/$defs/PersonType" },
            {
              "properties": {
                "fullName": {
                  "$ref": "#/$defs/LangStringType",
                  "//": "Mandatory (EUHEMC): Full name of the credential holder, required for person identification per ELM."
                },
                "familyName": {
                  "$ref": "#/$defs/LangStringType",
                  "//": "Mandatory (EUHEMC): Family name (surname) of the credential holder, required per ELM."
                },
                "givenName": {
                  "$ref": "#/$defs/LangStringType",
                  "//": "Mandatory (EUHEMC): Given name (first name) of the credential holder, required per ELM."
                },
                "nationalID": {
                  "$ref": "#/$defs/LegalIdentifierType",
                  "//": "Mandatory (EUHEMC): National identifier (e.g., DNI) for the credential holder, required for legal identification per ELM."
                },
                "hasClaim": {
                  "type": "array",
                  "items": { "$ref": "#/$defs/ClaimNodeType" },
                  "minItems": 2,
                  "contains": [
                    { "$ref": "#/$defs/LearningAchievementType" },
                    { "$ref": "#/$defs/LearningAssessmentType" }
                  ],
                  "//": "Mandatory (EUHEMC): Must include at least one LearningAchievement and one LearningAssessment to describe the microcredential's educational outcome and evaluation."
                }
              },
              "required": ["fullName", "familyName", "givenName", "nationalID", "hasClaim"],
              "//": "Mandatory (EUHEMC): These fields are required to ensure the credential holder is fully identified and the microcredential includes educational claims."
            }
          ]
        }
      },
      "required": ["type", "credentialSubject"],
      "//": "Mandatory: The credential must specify its type and include a credentialSubject to define the holder's details and claims."
    }
  ],
  "$defs": {
    "GenericIdType": {
      "type": "string",
      "format": "uri",
      "//": "Reusable type for unique identifiers (e.g., URIs) used across ELM objects."
    },
    "LangStringType": {
      "type": "object",
      "propertyNames": { "pattern": "^[a-z]{2}$" },
      "minProperties": 1,
      "maxProperties": 1,
      "//": "Reusable type for language-tagged strings (e.g., 'en': 'text') used for names, titles, etc."
    },
    "LegalIdentifierType": {
      "type": "object",
      "properties": {
        "id": { "$ref": "#/$defs/GenericIdType" },
        "type": { "const": "LegalIdentifier" },
        "notation": { "type": "string" },
        "spatial": { "$ref": "#/$defs/ConceptType" }
      },
      "required": ["notation", "spatial"],
      "//": "Mandatory (EUHEMC): Defines the national ID structure, requiring a notation (e.g., '12345678Z') and spatial context (e.g., country)."
    },
    "PersonType": {
      "type": "object",
      "properties": {
        "id": { "$ref": "#/$defs/GenericIdType" },
        "type": { "const": "Person" },
        "fullName": { "$ref": "#/$defs/LangStringType" },
        "givenName": { "$ref": "#/$defs/LangStringType" },
        "familyName": { "$ref": "#/$defs/LangStringType" },
        "nationalID": { "$ref": "#/$defs/LegalIdentifierType" },
        "hasClaim": { "$ref": "#/$defs/Many!ClaimNodeType" }
      },
      "required": ["id", "type"],
      "//": "Mandatory (ELM): PersonType requires an identifier and type to represent the credential holder."
    },
    "ClaimNodeType": {
      "anyOf": [
        { "$ref": "#/$defs/LearningAchievementType" },
        { "$ref": "#/$defs/LearningAssessmentType" }
      ],
      "//": "Reusable type to allow either LearningAchievement or LearningAssessment in hasClaim."
    },
    "Many!ClaimNodeType": {
      "anyOf": [
        { "$ref": "#/$defs/ClaimNodeType" },
        { "type": "array", "items": { "$ref": "#/$defs/ClaimNodeType" } }
      ],
      "//": "Allows single or multiple claims (LearningAchievement or LearningAssessment)."
    },
    "LearningAchievementType": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "id": { "$ref": "#/$defs/GenericIdType" },
        "type": { "const": "LearningAchievement" },
        "title": { "$ref": "#/$defs/Many!LangStringType" },
        "creditReceived": {
          "type": "array",
          "items": { "$ref": "#/$defs/CreditPointType" },
          "minItems": 1,
          "maxItems": 1,
          "//": "Mandatory (EUHEMC): Exactly one CreditPoint to specify ECTS credits (1–15)."
        },
        "learningOutcome": {
          "type": "array",
          "items": { "$ref": "#/$defs/LearningOutcomeType" },
          "minItems": 1,
          "//": "Mandatory (EUHEMC): At least one LearningOutcome to describe the educational result."
        },
        "awardedBy": {
          "$ref": "#/$defs/AwardingProcessType",
          "//": "Mandatory (ELM): Specifies the awarding body (e.g., Rovira i Virgili University)."
        }
      },
      "required": ["id", "type", "title", "creditReceived", "learningOutcome", "awardedBy"],
      "//": "Mandatory (EUHEMC): LearningAchievement requires a title, credits, outcome, and awarding details to fully describe the microcredential's educational achievement."
    },
    "LearningAssessmentType": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "id": { "$ref": "#/$defs/GenericIdType" },
        "type": { "const": "LearningAssessment" },
        "title": { "$ref": "#/$defs/Many!LangStringType" },
        "grade": {
          "$ref": "#/$defs/NoteType",
          "//": "Mandatory (EUHEMC): Grade to evaluate the achievement."
        },
        "awardedBy": {
          "$ref": "#/$defs/AwardingProcessType",
          "//": "Mandatory (ELM): Specifies the awarding body for the assessment."
        }
      },
      "required": ["id", "type", "title", "grade", "awardedBy"],
      "//": "Mandatory (EUHEMC): LearningAssessment requires a title, grade, and awarding details to document the evaluation process."
    },
    "LearningOutcomeType": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "id": { "$ref": "#/$defs/GenericIdType" },
        "type": { "const": "LearningOutcome" },
        "title": { "$ref": "#/$defs/Many!LangStringType" },
        "relatedCompetence": {
          "type": "array",
          "items": { "$ref": "#/$defs/ConceptType" },
          "minItems": 1,
          "//": "Mandatory (EUHEMC): At least one competence to describe the skills or knowledge gained."
        },
        "relatedESCOSkill": {
          "type": "array",
          "items": { "$ref": "#/$defs/ConceptType" },
          "//": "Optional (EUHEMC): ESCO skills can be linked to competences for interoperability with European skill frameworks."
        }
      },
      "required": ["id", "type", "title", "relatedCompetence"],
      "//": "Mandatory (EUHEMC): LearningOutcome requires a title and at least one competence; ESCO skills are optional."
    },
    "CreditPointType": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "id": { "$ref": "#/$defs/GenericIdType" },
        "type": { "const": "CreditPoint" },
        "framework": { "$ref": "#/$defs/ConceptType" },
        "point": {
          "type": "string",
          "pattern": "^(1[0-5]|[1-9])$",
          "//": "Mandatory (EUHEMC): ECTS credits must be between 1 and 15."
        }
      },
      "required": ["id", "type", "framework", "point"],
      "//": "Mandatory (EUHEMC): Defines the ECTS credits awarded, constrained to 1–15."
    },
    "ConceptType": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "id": { "$ref": "#/$defs/GenericIdType" },
        "type": { "const": "Concept" },
        "prefLabel": { "$ref": "#/$defs/Many!LangStringType" }
      },
      "required": ["id", "type", "prefLabel"],
      "//": "Reusable type for competences and ESCO skills, requiring a label."
    },
    "NoteType": {
      "type": "object",
      "properties": {
        "id": { "$ref": "#/$defs/GenericIdType" },
        "type": { "const": "Note" },
        "noteLiteral": { "$ref": "#/$defs/Many!LangStringType" }
      },
      "required": ["id", "type", "noteLiteral"],
      "//": "Mandatory (ELM): Defines the grade or evaluation result for the assessment."
    },
    "AwardingProcessType": {
      "type": "object",
      "properties": {
        "id": { "$ref": "#/$defs/GenericIdType" },
        "type": { "const": "AwardingProcess" },
        "awardingBody": { "$ref": "#/$defs/AgentOrPersonOrOrganisationType" }
      },
      "required": ["id", "type", "awardingBody"],
      "//": "Mandatory (ELM): Links the achievement or assessment to the issuing organization."
    },
    "AgentOrPersonOrOrganisationType": {
      "anyOf": [
        { "$ref": "#/$defs/OrganisationType" }
      ],
      "//": "Reusable type for the awarding body (restricted to Organisation for EUHEMC)."
    },
    "OrganisationType": {
      "type": "object",
      "properties": {
        "id": { "$ref": "#/$defs/GenericIdType" },
        "type": { "const": "Organisation" },
        "legalName": { "$ref": "#/$defs/Many!LangStringType" }
      },
      "required": ["id", "type", "legalName"],
      "//": "Mandatory (ELM): Defines the issuing organization (e.g., Rovira i Virgili University)."
    },
    "Many!LangStringType": {
      "type": "object",
      "propertyNames": { "pattern": "^[a-z]{2}$" },
      "minProperties": 1,
      "//": "Reusable type for multi-language strings."
    },
    "EuropeanDigitalCredentialType": {
      "type": "object",
      "properties": {
        "@context": {
          "type": "array",
          "items": { "type": "string" },
          "contains": { "const": "https://www.w3.org/2018/credentials/v1" },
          "//": "Mandatory (ELM): JSON-LD context for W3C Verifiable Credentials."
        },
        "id": { "$ref": "#/$defs/GenericIdType" },
        "type": {
          "type": "array",
          "items": { "type": "string" },
          "contains": { "const": "EuropeanDigitalCredential" }
        },
        "issuer": { "$ref": "#/$defs/IssuerNodeType" },
        "issuanceDate": { "$ref": "#/$defs/DateTimeType" },
        "issued": { "$ref": "#/$defs/DateTimeType" },
        "validFrom": { "$ref": "#/$defs/DateTimeType" },
        "credentialSubject": { "$ref": "#/$defs/PersonType" },
        "credentialSchema": { "$ref": "#/$defs/CredentialSchemaType" },
        "displayParameter": { "$ref": "#/$defs/DisplayParameterType" },
        "proof": { "$ref": "#/$defs/Many!ProofType" }
      },
      "required": [
        "@context", "id", "type", "issuer", "issuanceDate", "issued",
        "validFrom", "credentialSubject", "credentialSchema", "displayParameter"
      ],
      "//": "Mandatory (ELM): Core structure for EBSI Verifiable Credentials, requiring issuer, dates, and schema."
    },
    "IssuerNodeType": {
      "type": "object",
      "properties": {
        "id": { "$ref": "#/$defs/GenericIdType" }
      },
      "required": ["id"],
      "//": "Mandatory (ELM): Identifies the issuer (e.g., university DID)."
    },
    "CredentialSchemaType": {
      "type": "object",
      "properties": {
        "id": { "$ref": "#/$defs/GenericIdType" },
        "type": { "enum": ["ShaclValidator2017", "JsonSchema"] }
      },
      "required": ["id", "type"],
      "//": "Mandatory (ELM): References the schema for validation."
    },
    "DisplayParameterType": {
      "type": "object",
      "properties": {
        "id": { "$ref": "#/$defs/GenericIdType" },
        "type": { "const": "DisplayParameter" },
        "title": { "$ref": "#/$defs/Many!LangStringType" },
        "language": { "$ref": "#/$defs/Many!ConceptType" },
        "primaryLanguage": { "$ref": "#/$defs/ConceptType" },
        "individualDisplay": { "$ref": "#/$defs/Many!IndividualDisplayType" }
      },
      "required": ["id", "type", "title", "language", "primaryLanguage", "individualDisplay"],
      "//": "Mandatory (ELM): Defines how the credential is displayed (e.g., in a wallet)."
    },
    "IndividualDisplayType": {
      "type": "object",
      "properties": {
        "id": { "$ref": "#/$defs/GenericIdType" },
        "type": { "const": "IndividualDisplay" },
        "fieldPath": { "type": "string" },
        "label": { "$ref": "#/$defs/Many!LangStringType" },
        "order": { "type": "integer" }
      },
      "required": ["id", "type", "fieldPath", "label"],
      "//": "Mandatory (ELM): Specifies display fields (e.g., name, achievement title)."
    },
    "DateTimeType": {
      "type": "string",
      "format": "date-time",
      "//": "Reusable type for timestamps (e.g., issuanceDate)."
    },
    "Many!ConceptType": {
      "anyOf": [
        { "$ref": "#/$defs/ConceptType" },
        { "type": "array", "items": { "$ref": "#/$defs/ConceptType" } }
      ],
      "//": "Allows single or multiple concepts (e.g., languages)."
    },
    "Many!IndividualDisplayType": {
      "anyOf": [
        { "$ref": "#/$defs/IndividualDisplayType" },
        { "type": "array", "items": { "$ref": "#/$defs/IndividualDisplayType" } }
      ],
      "//": "Allows single or multiple display parameters."
    },
    "ProofType": {
      "type": "object",
      "properties": {
        "type": { "type": "string" },
        "created": { "$ref": "#/$defs/DateTimeType" },
        "verificationMethod": { "$ref": "#/$defs/GenericIdType" },
        "proofPurpose": { "type": "string" },
        "jws": { "type": "string" }
      },
      "required": ["type", "created", "verificationMethod", "proofPurpose", "jws"],
      "//": "Optional (ELM): Defines the cryptographic proof for signed credentials."
    },
    "Many!ProofType": {
      "anyOf": [
        { "$ref": "#/$defs/ProofType" },
        { "type": "array", "items": { "$ref": "#/$defs/ProofType" } }
      ],
      "//": "Allows single or multiple proofs."
    }
  }
}