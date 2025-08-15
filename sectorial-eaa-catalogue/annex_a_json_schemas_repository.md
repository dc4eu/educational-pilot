# Annex A: Complete JSON-LD Schemas Repository

## Introduction

This annex provides the complete repository of JSON-LD schemas for Electronic Attestations of Attributes (EAAs) within the DC4EU sectoral catalogue. These schemas are designed to support eIDAS2 compliance whilst maintaining interoperability with existing European Digital Credentials (EDC) and European Learning Model (ELM) implementations.

## A.1 Schema Organisation and Structure

### A.1.1 Schema Categories

The schemas are organised into the following primary categories:

- **Foundational Identity Schemas**: Core identity data models including Person Identifier (PID) and legal entity identification
- **Formal Education Schemas**: Academic credentials, diplomas, certificates, and transcripts
- **Professional Qualifications Schemas**: Professional certifications, competence attestations, and continuous development records
- **Non-Foundational Identity Schemas**: Educational IDs, student cards, and alliance identifiers
- **Quality Assurance Schemas**: Institutional accreditation and quality framework schemas

### A.1.2 Schema Versioning and Compatibility

All schemas follow semantic versioning principles:
- **Major versions** (x.0.0): Breaking changes requiring migration
- **Minor versions** (x.y.0): Backward-compatible feature additions
- **Patch versions** (x.y.z): Bug fixes and clarifications

Current stable version: **3.2.x** (aligned with ELM v3.2)

## A.2 Core Base Schema Definitions

### A.2.1 EDC-W3C VCDM Base Schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://schemas.dc4eu.eu/edc-w3c-vcdm/v3.2/base-schema.json",
  "title": "EDC-W3C VCDM Base Schema",
  "description": "Base schema for European Digital Credentials compliant with W3C Verifiable Credentials Data Model",
  "type": "object",
  "properties": {
    "@context": {
      "type": "array",
      "items": [
        {
          "const": "https://www.w3.org/2018/credentials/v1"
        },
        {
          "const": "https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/contexts/european-digital-credential-v3.jsonld"
        }
      ],
      "additionalItems": {
        "anyOf": [
          {"type": "string", "format": "uri"},
          {"type": "object"}
        ]
      }
    },
    "id": {
      "type": "string",
      "format": "uri"
    },
    "type": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "contains": {
        "const": "VerifiableCredential"
      }
    },
    "issuer": {
      "oneOf": [
        {"type": "string", "format": "uri"},
        {
          "type": "object",
          "properties": {
            "id": {"type": "string", "format": "uri"},
            "type": {"type": "string"}
          },
          "required": ["id"]
        }
      ]
    },
    "issuanceDate": {
      "type": "string",
      "format": "date-time"
    },
    "expirationDate": {
      "type": "string",
      "format": "date-time"
    },
    "credentialSubject": {
      "type": "object",
      "properties": {
        "id": {"type": "string", "format": "uri"}
      }
    },
    "credentialStatus": {
      "type": "object",
      "properties": {
        "id": {"type": "string", "format": "uri"},
        "type": {"type": "string"}
      },
      "required": ["id", "type"]
    },
    "proof": {
      "oneOf": [
        {"$ref": "#/$defs/ProofType"},
        {
          "type": "array",
          "items": {"$ref": "#/$defs/ProofType"}
        }
      ]
    }
  },
  "required": ["@context", "type", "issuer", "issuanceDate", "credentialSubject"],
  "$defs": {
    "ProofType": {
      "type": "object",
      "properties": {
        "type": {"type": "string"},
        "created": {"type": "string", "format": "date-time"},
        "verificationMethod": {"type": "string", "format": "uri"},
        "proofPurpose": {"type": "string"},
        "proofValue": {"type": "string"}
      },
      "required": ["type", "verificationMethod", "proofPurpose"]
    }
  }
}
```

### A.2.2 ELM Core Types Schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://schemas.dc4eu.eu/elm/v3.2/core-types.json",
  "title": "European Learning Model Core Types",
  "description": "Core type definitions for ELM v3.2 compatible schemas",
  "$defs": {
    "LangStringType": {
      "type": "object",
      "propertyNames": {
        "pattern": "^(aa|ab|ae|af|ak|am|an|ar|as|av|ay|az|ba|be|bg|bh|bi|bm|bn|bo|br|bs|ca|ce|ch|co|cr|cs|cu|cv|cy|da|de|dv|dz|ee|el|en|eo|es|et|eu|fa|ff|fi|fj|fo|fr|fy|ga|gd|gl|gn|gu|gv|ha|he|hi|ho|hr|ht|hu|hy|hz|ia|id|ie|ig|ii|ik|in|io|is|it|iu|iw|ja|ji|jv|jw|ka|kg|ki|kj|kk|kl|km|kn|ko|kr|ks|ku|kv|kw|ky|la|lb|lg|li|ln|lo|lt|lu|lv|mg|mh|mi|mk|ml|mn|mo|mr|ms|mt|my|na|nb|nd|ne|ng|nl|nn|no|nr|nv|ny|oc|oj|om|or|os|pa|pi|pl|ps|pt|qu|rm|rn|ro|ru|rw|sa|sc|sd|se|sg|sh|si|sk|sl|sm|sn|so|sq|sr|ss|st|su|sv|sw|ta|te|tg|th|ti|tk|tl|tn|to|tr|ts|tt|tw|ty|ug|uk|ur|uz|ve|vi|vo|wa|wo|xh|yi|yo|za|zh|zu)$"
      },
      "minProperties": 1
    },
    "IdentifierType": {
      "type": "object",
      "properties": {
        "id": {"type": "string", "format": "uri"},
        "type": {"const": "Identifier"},
        "notation": {"type": "string"},
        "schemeAgency": {"$ref": "#/$defs/LangStringType"},
        "dateIssued": {"type": "string", "format": "date-time"}
      },
      "required": ["notation"]
    },
    "ConceptType": {
      "type": "object",
      "properties": {
        "id": {"type": "string", "format": "uri"},
        "type": {"const": "Concept"},
        "prefLabel": {"$ref": "#/$defs/LangStringType"},
        "notation": {"type": "string"}
      }
    },
    "OrganisationType": {
      "type": "object",
      "properties": {
        "id": {"type": "string", "format": "uri"},
        "type": {"const": "Organisation"},
        "legalName": {"$ref": "#/$defs/LangStringType"},
        "identifier": {
          "type": "array",
          "items": {"$ref": "#/$defs/IdentifierType"}
        }
      },
      "required": ["legalName"]
    },
    "PersonType": {
      "type": "object",
      "properties": {
        "id": {"type": "string", "format": "uri"},
        "type": {"const": "Person"},
        "givenName": {"$ref": "#/$defs/LangStringType"},
        "familyName": {"$ref": "#/$defs/LangStringType"},
        "dateOfBirth": {"type": "string", "format": "date"}
      }
    }
  }
}
```

## A.3 Formal Education Schemas

### A.3.1 European Higher Education Diploma (EUHED)

**Schema URI**: `https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/0x7663df08b9a50f226e185efb7ec08f3d69f4a95e653ebffd3137b3eb6923dda8`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://schemas.dc4eu.eu/formal-education/euhed/v1.0/schema.json",
  "title": "European Higher Education Diploma",
  "description": "Schema for European Higher Education Diploma credentials",
  "allOf": [
    {"$ref": "https://schemas.dc4eu.eu/edc-w3c-vcdm/v3.2/base-schema.json"}
  ],
  "properties": {
    "type": {
      "type": "array",
      "items": {"type": "string"},
      "contains": {"const": "EuropeanHigherEducationDiploma"}
    },
    "credentialSubject": {
      "type": "object",
      "allOf": [
        {"$ref": "https://schemas.dc4eu.eu/elm/v3.2/core-types.json#/$defs/PersonType"}
      ],
      "properties": {
        "hasClaim": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "id": {"type": "string", "format": "uri"},
              "type": {"const": "LearningAchievement"},
              "title": {"$ref": "https://schemas.dc4eu.eu/elm/v3.2/core-types.json#/$defs/LangStringType"},
              "description": {"$ref": "https://schemas.dc4eu.eu/elm/v3.2/core-types.json#/$defs/LangStringType"},
              "awardedBy": {
                "type": "object",
                "properties": {
                  "awardingBody": {
                    "type": "array",
                    "items": {"$ref": "https://schemas.dc4eu.eu/elm/v3.2/core-types.json#/$defs/OrganisationType"}
                  }
                }
              },
              "specifiedBy": {
                "type": "object",
                "properties": {
                  "eqfLevel": {"$ref": "https://schemas.dc4eu.eu/elm/v3.2/core-types.json#/$defs/ConceptType"},
                  "nqfLevel": {
                    "type": "array",
                    "items": {"$ref": "https://schemas.dc4eu.eu/elm/v3.2/core-types.json#/$defs/ConceptType"}
                  }
                }
              }
            },
            "required": ["type", "title", "awardedBy"]
          }
        }
      },
      "required": ["hasClaim"]
    }
  }
}
```

### A.3.2 European Higher Education Diploma Supplement (EUHEDS)

**Schema URI**: `https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/0x597214a686156123e6603272b72638a615d83037d306b16170ff838168dfaf13`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://schemas.dc4eu.eu/formal-education/euheds/v1.0/schema.json",
  "title": "European Higher Education Diploma Supplement",
  "description": "Schema for European Higher Education Diploma Supplement credentials",
  "allOf": [
    {"$ref": "https://schemas.dc4eu.eu/edc-w3c-vcdm/v3.2/base-schema.json"}
  ],
  "properties": {
    "type": {
      "type": "array",
      "contains": {"const": "EuropeanHigherEducationDiplomaSupplement"}
    },
    "credentialSubject": {
      "allOf": [
        {"$ref": "https://schemas.dc4eu.eu/elm/v3.2/core-types.json#/$defs/PersonType"}
      ],
      "properties": {
        "hasClaim": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "type": {"const": "LearningAchievement"},
              "title": {"$ref": "https://schemas.dc4eu.eu/elm/v3.2/core-types.json#/$defs/LangStringType"},
              "description": {"$ref": "https://schemas.dc4eu.eu/elm/v3.2/core-types.json#/$defs/LangStringType"},
              "learningOutcome": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "type": {"const": "LearningOutcome"},
                    "title": {"$ref": "https://schemas.dc4eu.eu/elm/v3.2/core-types.json#/$defs/LangStringType"},
                    "relatedSkill": {
                      "type": "array",
                      "items": {"$ref": "https://schemas.dc4eu.eu/elm/v3.2/core-types.json#/$defs/ConceptType"}
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
```

### A.3.3 European VET Micro-credential (EUVETMC)

**Schema URI**: `https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/0x123abc456def789...` (placeholder)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://schemas.dc4eu.eu/formal-education/euvetmc/v1.0/schema.json",
  "title": "European VET Micro-credential",
  "description": "Schema for European Vocational Education and Training micro-credentials",
  "allOf": [
    {"$ref": "https://schemas.dc4eu.eu/edc-w3c-vcdm/v3.2/base-schema.json"}
  ],
  "properties": {
    "type": {
      "type": "array",
      "contains": {"const": "EuropeanVETMicroCredential"}
    },
    "credentialSubject": {
      "allOf": [
        {"$ref": "https://schemas.dc4eu.eu/elm/v3.2/core-types.json#/$defs/PersonType"}
      ],
      "properties": {
        "hasClaim": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "type": {"const": "LearningAchievement"},
              "title": {"$ref": "https://schemas.dc4eu.eu/elm/v3.2/core-types.json#/$defs/LangStringType"},
              "description": {"$ref": "https://schemas.dc4eu.eu/elm/v3.2/core-types.json#/$defs/LangStringType"},
              "learningOutcome": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "type": {"const": "LearningOutcome"},
                    "relatedESCOSkill": {
                      "type": "array",
                      "items": {"$ref": "https://schemas.dc4eu.eu/elm/v3.2/core-types.json#/$defs/ConceptType"}
                    }
                  }
                }
              },
              "specifiedBy": {
                "type": "object",
                "properties": {
                  "workload": {
                    "type": "object",
                    "properties": {
                      "type": {"const": "Duration"},
                      "value": {"type": "number"},
                      "unit": {"$ref": "https://schemas.dc4eu.eu/elm/v3.2/core-types.json#/$defs/ConceptType"}
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
```

## A.4 Professional Qualifications Schemas

### A.4.1 Certificate of Professional Competence (CPC)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://schemas.dc4eu.eu/professional-qualifications/cpc/v1.0/schema.json",
  "title": "Certificate of Professional Competence",
  "description": "Schema for Certificate of Professional Competence credentials",
  "allOf": [
    {"$ref": "https://schemas.dc4eu.eu/edc-w3c-vcdm/v3.2/base-schema.json"}
  ],
  "properties": {
    "type": {
      "type": "array",
      "contains": {"const": "CertificateOfProfessionalCompetence"}
    },
    "credentialSubject": {
      "allOf": [
        {"$ref": "https://schemas.dc4eu.eu/elm/v3.2/core-types.json#/$defs/PersonType"}
      ],
      "properties": {
        "hasClaim": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "type": {"const": "LearningAchievement"},
              "title": {"$ref": "https://schemas.dc4eu.eu/elm/v3.2/core-types.json#/$defs/LangStringType"},
              "professionalCompetence": {
                "type": "array",
                "items": {"$ref": "https://schemas.dc4eu.eu/elm/v3.2/core-types.json#/$defs/ConceptType"}
              },
              "relatedOccupation": {
                "type": "array",
                "items": {"$ref": "https://schemas.dc4eu.eu/elm/v3.2/core-types.json#/$defs/ConceptType"}
              }
            }
          }
        }
      }
    }
  }
}
```

## A.5 Non-Foundational Identity Schemas

### A.5.1 Educational ID (EAA1)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://schemas.dc4eu.eu/non-foundational-id/educational-id/v1.0/schema.json",
  "title": "Educational ID",
  "description": "Schema for Educational ID credentials",
  "allOf": [
    {"$ref": "https://schemas.dc4eu.eu/edc-w3c-vcdm/v3.2/base-schema.json"}
  ],
  "properties": {
    "type": {
      "type": "array",
      "contains": {"const": "EducationalID"}
    },
    "credentialSubject": {
      "allOf": [
        {"$ref": "https://schemas.dc4eu.eu/elm/v3.2/core-types.json#/$defs/PersonType"}
      ],
      "properties": {
        "educationalIdentifier": {
          "type": "object",
          "properties": {
            "type": {"const": "Identifier"},
            "notation": {"type": "string"},
            "schemeAgency": {"$ref": "https://schemas.dc4eu.eu/elm/v3.2/core-types.json#/$defs/LangStringType"}
          },
          "required": ["notation"]
        },
        "enrolmentStatus": {
          "type": "object",
          "properties": {
            "type": {"const": "Concept"},
            "prefLabel": {"$ref": "https://schemas.dc4eu.eu/elm/v3.2/core-types.json#/$defs/LangStringType"}
          }
        },
        "institution": {"$ref": "https://schemas.dc4eu.eu/elm/v3.2/core-types.json#/$defs/OrganisationType"}
      },
      "required": ["educationalIdentifier", "institution"]
    }
  }
}
```

## A.6 Schema Registry and Validation

### A.6.1 Registry Locations

All schemas are published in the following registries:

- **EBSI Trusted Schemas Registry**: Production schemas for live credentials
- **DC4EU Local Repository**: Development and testing schemas
- **European Commission Code Repository**: Version-controlled schema sources

### A.6.2 Validation Requirements

All schemas must pass:

1. **JSON Schema Draft 2020-12 validation**
2. **W3C VCDM 2.0 compliance checks**
3. **ELM v3.2 compatibility validation**
4. **eIDAS2 regulatory compliance assessment**

### A.6.3 Schema Lifecycle Management

- **Development**: Schemas created in local repository with `-dev` suffix
- **Testing**: Validated schemas moved to test registry with `-test` suffix
- **Production**: Final schemas published to EBSI TSR with semantic version

## A.7 Implementation Guidelines

### A.7.1 Schema Extension Points

All schemas provide extension points for:
- **National adaptations**: Country-specific requirements
- **Institutional customisations**: Institution-specific fields
- **Sectoral extensions**: Domain-specific attributes

### A.7.2 Backward Compatibility

- **Migration paths** defined for major version changes
- **Deprecation policies** for obsolete schema elements
- **Conversion utilities** provided for legacy credential formats

### A.7.3 Quality Assurance

- **Automated testing** for all schema changes
- **Peer review** process for schema modifications
- **Stakeholder consultation** for breaking changes

---

**Note**: This annex is maintained as a living document. For the most current schema versions and registry locations, consult the [DC4EU Schema Registry](https://schemas.dc4eu.eu) and the [EBSI Trusted Schemas Registry](https://api-pilot.ebsi.eu/trusted-schemas-registry).