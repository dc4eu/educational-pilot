# Annex C: Data models

## Introduction

Standardised data models are fundamental building blocks in modern information systems, providing a consistent framework for data organisation, storage, and exchange across different platforms and applications. Their implementation offers several key benefits:

1. **Interoperability**: Standardised data models enable seamless integration between different systems and stakeholders, reducing the complexity of data exchange and integration processes.
2. **Data quality**: By establishing uniform data structures and relationships, these models help maintain data consistency and reduce errors that often arise from disparate data formats.
3. **Efficiency**: Development and maintenance costs are significantly reduced as standardised models eliminate the need for custom data mapping and transformation between systems.
4. **Scalability**: As organisations grow and evolve, standardised data models provide a stable foundation for system expansion and modification.

## Structure and navigation

This chapter presents four essential data models that form the backbone of our information architecture. Each model is designed to address specific business needs while maintaining consistency with the overall system architecture described in previous sections.

The data models covered in this chapter are:

1. [AllianceID Data Model](#allianceid-data-model)
2. [Educational ID Data Model](#educational-id-data-model)
3. [MyAcademicId Data Model](#myacademicid-data-model)
4. [European Learning Model (ELM) Data Model](#european-learning-model-elm-data-model)

Each data model section includes:

- Purpose and scope
- Entity relationships
- Attribute definitions
- Implementation considerations

## Relationship to previous sections

The data models presented in this annex build upon and support the concepts, requirements, and frameworks established in previous sections:

### Connection to Chapter 2: European Education Landscape
- The data models accommodate the diverse approaches to educational licensing and credential management described in [Section 2.1](chapter2.md#21-decentralised-authority-and-member-state-autonomy)
- Support for both administrative and legislative approaches outlined in [Section 2.4](chapter2.md#24-administrative-vs-legislative-approaches)
- Integration with electronic diploma issuance practices discussed in [Section 2.7](chapter2.md#27-electronic-diploma-issuance)
- Alignment with existing data models and ontologies covered in [Section 2.9](chapter2.md#29-data-models-and-ontologies)

### Alignment with Chapter 3: Current Challenges
- Addresses credential issuance and verification challenges outlined in [Section 3.1](chapter3.md#31-credential-issuance-and-verification)
- Supports qualification recognition needs described in [Section 3.2](chapter3.md#32-recognition-of-qualifications)
- Resolves data management and interoperability issues identified in [Section 3.3](chapter3.md#33-data-management-and-interoperability)
- Accommodates stakeholder needs and concerns from [Section 3.6](chapter3.md#36-stakeholder-needs-and-concerns)

### Support for Chapter 4: Operational Model
- Implements the trust model and governance framework detailed in [Section 4.1](chapter4.md#41-trust-model-and-governance-framework)
- Enables credential lifecycle management processes outlined in [Section 4.2](chapter4.md#42-credential-lifecycle-management)
- Supports roles and responsibilities defined in [Section 4.3](chapter4.md#43-roles-and-responsibilities)
- Facilitates compliance monitoring requirements from [Section 4.4](chapter4.md#44-compliance-and-monitoring-framework)

### Implementation of Chapter 5: Onboarding Processes
- Provides data structures needed for educational onboarding ([Section 5.1](chapter5.md#51-educational-onboarding-process))
- Supports professional qualifications onboarding ([Section 5.2](chapter5.md#52-professional-qualifications-onboarding-process))
- Enables secure credential issuance and management throughout onboarding

### Foundation for Chapter 6: Use Cases
- Enables non-foundational identity scenarios from [Section 6.1](chapter6.md#61-natural-persons-identity)
- Supports learning achievement use cases from [Section 6.7](chapter6.md#67-education-and-professional-qualifications-ontology---european-learning-model-elm)
- Facilitates professional qualification processes from [Section 6.8](chapter6.md#68-issuance)

### Technical Framework Integration (Chapter 8)
- Forms core component of technical architecture ([Section 8.2](chapter8.md#82-core-data-model-architecture))
- Supports country-specific implementations ([Section 8.4](chapter8.md#84-country-specific-implementations))
- Enables maintenance and updates described in [Section 8.6](chapter8.md#86-maintenance-and-updates)

These data models serve as the technical foundation that enables the business processes, governance frameworks, and user journeys described throughout the document. By implementing standardised formats based on W3C-VCDM and ELM specifications, they ensure interoperability while supporting the specific requirements of educational and professional credentialing across Europe.

## AllianceID Data Model

### Introduction

The Verifiable AllianceID is a JSON-schema based data model designed to represent and validate digital identifiers for natural persons participating in University Alliances. This data model implements the W3C Verifiable Credentials Data Model 1.1 specification, providing a standardised way to issue and verify digital credentials for alliance members.

**Key benefits of this data model include:**

- Standardised identification across European University Alliances
- Interoperability with abroad initiatives (e.g. OpenBadges)
- Flexible identifier scheme for different alliance contexts

### Implementation considerations

#### Identifier Format
- Validate identifier format: `urn:schac:europeanUniversityAllianceCode:int:euai:<sHO>:<code>`
- Implement proper escaping for special characters
- Consider backward compatibility with legacy systems

#### Schema Inheritance
- Handle proper extension of VCDM1.1 attestation schema
- Implement validation for both base and extended schemas
- Consider version management for schema updates

### Field Specifications

| Field | Path | Description | Type | Mandatory |
|-------|------|-------------|------|-----------|
| **Schema Reference** | `$schema` | JSON Schema version reference | string | Yes |
| **Title** | `title` | Credential type identifier | string | Yes |
| **Credential Subject ID** | `credentialSubject.id` | Unique identifier of the credential subject | string | Yes |
| **Identifier** | `credentialSubject.identifier` | Container for alliance identification details | object | Yes |
| **Scheme ID** | `credentialSubject.identifier.schemeID` | Schema used for alternative identification | string | Yes |
| **Value** | `credentialSubject.identifier.value` | Alternative identification value | string | Yes |
| **Identifier URI** | `credentialSubject.identifier.id` | URI of the identifier | string (URI) | No |

### Schema Structure Visualisation

![AllianceID Schema Structure](../../images/bbp-image31.png)

### JSON serialisation

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Verifiable AllianceID",
  "description": "Schema of an EBSI Verifiable University Alliance ID for a natural person participating in the Alliance",
  "type": "object",
  "allOf": [
    {
      "$ref": "./node_modules/@cef-ebsi/vcdm1.1-attestation-schema/schema.json"
    },
    {
      "properties": {
        "credentialSubject": {
          "description": "Defines additional properties on credentialSubject to describe IDs that do not have a substantial level of assurance.",
          "type": "object",
          "properties": {
            "id": {
              "description": "Defines a unique identifier of the credential subject",
              "type": "string"
            },
            "identifier": {
              "type": "object",
              "description": "Defines the identifier for the University Alliance. Format: urn:schac:europeanUniversityAllianceCode:int:euai:<sHO>:<code>. sHO: the schacHomeOrganization of the Alliance that issued the credential, <code> the university alliance code",
              "$ref": "#/$defs/identifier"
            }
          },
          "required": ["id", "identifier"]
        }
      }
    }
  ],
  "$defs": {
    "identifier": {
      "description": "Defines an alternative Identifier object",
      "type": "object",
      "properties": {
        "schemeID": {
          "description": "Defines the schema used to define alternative identification",
          "type": "string"
        },
        "value": {
          "description": "Define the alternative identification value",
          "type": "string"
        },
        "id": {
          "description": "The URI of the identifier",
          "type": "string",
          "format": "uri"
        }
      },
      "required": ["schemeID", "value"]
    }
  }
}
```

## Educational ID Data Model

### Introduction

The Verifiable Educational ID is a comprehensive data model designed to represent educational identity credentials for natural persons participating in educational use cases. This model extends the VCDM1.1 attestation schema and incorporates standard educational attributes aligned with eduGAIN and SCHAC (SCHema for ACademia) specifications. It provides a robust framework for representing educational identities with various attributes including personal information, institutional affiliations, and identity assurance levels.

**Key benefits:**

- Standardised representation of educational identities across institutions
- Integration with existing educational identity frameworks (eduGAIN)
- Support for multiple affiliation types and roles
- Flexible identity assurance mechanisms

### Implementation considerations

#### Identity Management
- Implement proper handling of multiple affiliation types
- Consider privacy implications of educational data
- Manage credential expiration and renewal

#### Data Validation
- Validate email format and institutional domains
- Implement proper date formatting (yyyyMMdd)
- Handle multi-value fields (eduPersonAffiliation)

#### Integration
- Interface with eduGAIN infrastructure
- Handle SCHAC attribute synchronisation
- Implement proper error handling for missing required fields

### Field Specifications

| Field | Path | Description | Type | Mandatory |
|-------|------|-------------|------|-----------|
| **ID** | `credentialSubject.id` | DID:Key value generated by user wallet | string | Yes |
| **Identifier** | `credentialSubject.identifier` | Global unique identifier (eduPersonPrincipalName) | string | Yes |
| **Scoped Affiliation** | `credentialSubject.eduPersonScopedAffiliation` | Affiliations within Home Organisation | array of strings | Yes |
| **Personal Unique Code** | `credentialSubject.schacPersonalUniqueCode` | Institution or country-specific unique codes | array of strings | No |
| **Personal Unique ID** | `credentialSubject.schacPersonalUniqueID` | Country-specific unique identifier | string | No |
| **Home Organisation** | `credentialSubject.schacHomeOrganization` | Home institution identifier | string | No |
| **Family Name** | `credentialSubject.familyName` | Current family name(s) | string | No |
| **First Name** | `credentialSubject.firstName` | Current first name(s) | string | No |
| **Display Name** | `credentialSubject.displayName` | Name for white-pages applications | string | No |
| **Date of Birth** | `credentialSubject.dateOfBirth` | Birth date (yyyyMMdd format) | string (date) | No |
| **Common Name** | `credentialSubject.commonName` | Birth name | string | No |
| **Email** | `credentialSubject.mail` | Primary institutional email | string | No |
| **Principal Name** | `credentialSubject.eduPersonPrincipalName` | Unique persistent identifier | string | No |
| **Primary Affiliation** | `credentialSubject.eduPersonPrimaryAffiliation` | Primary role within organisation | string | No |
| **Affiliations** | `credentialSubject.eduPersonAffiliation` | All roles within organisation | array of strings | No |
| **Assurance** | `credentialSubject.eduPersonAssurance` | Identity assurance profiles | array of strings | No |
| **Image** | `credentialSubject.image` | Profile image data | MediaObject | No |

### Schema Structure Visualisation

![Educational ID Schema Structure](../../images/bbp-image32.png)

### JSON serialisation

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Verifiable Educational ID",
  "description": "Schema of a Verifiable Educational ID for a natural person participating in the educational use cases",
  "type": "object",
  "allOf": [
    {
      "$ref": "./node_modules/@cef-ebsi/vcdm1.1-attestation-schema/schema.json"
    },
    {
      "properties": {
        "credentialSubject": {
          "description": "Defines additional properties on credentialSubject to describe IDs that do not have a substantial level of assurance.",
          "type": "object",
          "properties": {
            "id": {
              "description": "Defines a unique identifier of the credential subject. DID:Key value, generated by the user wallet and associated to the credential holder. Refer specification available at https://api-pilot.ebsi.eu/docs/specs/did-methods/did-method-for-natural-person",
              "type": "string"
            },
            "identifier": {
              "description": "Defines an alternative identifier for the credential subject and has as value the value of eduPersonPrincipalName attribute of the credential subject within the Home Organisation (needs to be globally unique and persistent).",
              "type": "string"
            },
            "schacPersonalUniqueCode": {
              "description": "schacPersonalUniqueCode can have different forms urn:schac:personalUniqueCode:int:esi:<sHO>:<code> (where <sHO> is the Higher Education Institution's schacHomeOrganization) and urn:schac:personalUniqueCode:int:esi:<country-code>:<code> (<code> is a string that uniquely identifies the person).",
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "schacPersonalUniqueID": {
              "description": "value is different in different countries, mostly urn:schac:personalUniqueID:<country-code>:<code>.",
              "type": "string"
            },
            "schacHomeOrganization": {
              "description": "Specifies the home organisation of the credential subject",
              "type": "string"
            },
            "familyName": {
              "description": "Defines current family name(s) of the credential subject which corresponds to the eduGAIN attribute sn",
              "type": "string"
            },
            "firstName": {
              "description": "Defines current first name(s) of the credential subject which corresponds to the eduGAIN attribute givenName",
              "type": "string"
            },
            "displayName": {
              "description": "The name(s) that should appear in white-pages-like applications",
              "type": "string"
            },
            "dateOfBirth": {
              "description": "Defines date of birth of the credential subject (format: yyyyMMdd)",
              "type": "string",
              "format": "date"
            },
            "commonName": {
              "description": "Defines the first and the family name(s) of the credential subject at the time of their birth",
              "type": "string"
            },
            "mail": {
              "description": "(primary) e-mail address of the credential subject as registered by the educational institution issuing the Verifiable Educational ID",
              "type": "string"
            },
            "eduPersonPrincipalName": {
              "description": "Unique, persistent identifier of the credential subject",
              "type": "string"
            },
            "eduPersonPrimaryAffiliation": {
              "description": "Primary Affiliation within Home Organisation",
              "type": "string"
            },
            "eduPersonAffiliation": {
              "description": "Affiliation within Home Organisation. It can contain multiple values such as member, student, employee, faculty, staff, affiliate, alumni, etc.",
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "eduPersonScopedAffiliation": {
              "description": "The person's affiliations within Home Organisation scoped with the Home Organisation",
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "eduPersonAssurance": {
              "description": "represents identity assurance profiles (IAPs) https://wiki.refeds.org/display/ASS/REFEDS+Assurance+Framework+ver+1.0",
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "image": {
              "$ref": "#/$defs/MediaObjectType"
            }
          },
          "required": ["id", "identifier", "eduPersonScopedAffiliation"]
        }
      }
    }
  ],
  "$defs": {
    "URIType": {
      "type": "string",
      "format": "uri"
    },
    "StringType": {
      "type": "string"
    },
    "LiteralType": {
      "$ref": "#/$defs/StringType"
    },
    "IntegerType": {
      "type": "integer"
    },
    "GenericIdType": {
      "allOf": [
        {
          "$ref": "#/$defs/URIType"
        },
        {
          "if": {
            "type": "string",
            "pattern": "^(http|urn)"
          },
          "then": {
            "type": "string",
            "pattern": "^(http://data.europa.eu/snb/|http://publications.europa.eu/resource/authority/|urn:epass:.+:[0-9]+$|urn:epass:concept(Scheme)?:[0-9A-Za-z\\-]*$)"
          }
        }
      ]
    },
    "Many!LangStringType": {
      "type": "object",
      "propertyNames": {
        "pattern": "^(aa|ab|ae|af|ak|am|an|ar|as|av|ay|az|ba|be|bg|bh|bi|bm|bn|bo|br|bs|ca|ce|ch|co|cr|cs|cu|cv|cy|da|de|dv|dz|ee|el|en|eo|es|et|eu|fa|ff|fi|fj|fo|fr|fy|ga|gd|gl|gn|gu|gv|ha|he|hi|ho|hr|ht|hu|hy|hz|ia|id|ie|ig|ii|ik|in|io|is|it|iu|iw|ja|ji|jv|jw|ka|kg|ki|kj|kk|kl|km|kn|ko|kr|ks|ku|kv|kw|ky|la|lb|lg|li|ln|lo|lt|lu|lv|mg|mh|mi|mk|ml|mn|mo|mr|ms|mt|my|na|nb|nd|ne|ng|nl|nn|no|nr|nv|ny|oc|oj|om|or|os|pa|pi|pl|ps|pt|qu|rm|rn|ro|ru|rw|sa|sc|sd|se|sg|sh|si|sk|sl|sm|sn|so|sq|sr|ss|st|su|sv|sw|ta|te|tg|th|ti|tk|tl|tn|to|tr|ts|tt|tw|ty|ug|uk|ur|uz|ve|vi|vo|wa|wo|xh|yi|yo|za|zh|zu)$"
      },
      "minProperties": 1
    },
    "ConceptSchemeType": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "id": {
          "$ref": "#/$defs/GenericIdType"
        },
        "type": {
          "const": "ConceptScheme"
        }
      },
      "required": []
    },
    "ConceptType": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "id": {
          "$ref": "#/$defs/GenericIdType"
        },
        "type": {
          "const": "Concept"
        },
        "prefLabel": {
          "$ref": "#/$defs/Many!LangStringType"
        },
        "notation": {
          "$ref": "#/$defs/LiteralType"
        },
        "inScheme": {
          "$ref": "#/$defs/ConceptSchemeType"
        },
        "definition": {
          "$ref": "#/$defs/Many!LangStringType"
        }
      },
      "required": []
    },
    "MediaObjectType": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "id": {
          "$ref": "#/$defs/GenericIdType"
        },
        "type": {
          "const": "MediaObject"
        },
        "title": {
          "$ref": "#/$defs/Many!LangStringType"
        },
        "description": {
          "$ref": "#/$defs/Many!LangStringType"
        },
        "contentType": {
          "$ref": "#/$defs/ConceptType"
        },
        "attachmentType": {
          "$ref": "#/$defs/ConceptType"
        },
        "contentEncoding": {
          "$ref": "#/$defs/ConceptType"
        },
        "contentSize": {
          "$ref": "#/$defs/IntegerType"
        },
        "content": {
          "$ref": "#/$defs/StringType"
        },
        "contentURL": {
          "$ref": "#/$defs/URIType"
        }
      },
      "required": ["contentType", "contentEncoding", "content"]
    }
  }
}
```

## MyAcademicId Data Model

### Introduction

The MyAcademicId data model defines a schema for verifiable credentials specifically designed for academic identity management across European educational institutions. This model implements the eduPerson standard attributes and incorporates the European Student Identifier (ESI) framework, making it particularly valuable for academic mobility and cross-institutional identity management.

**Key benefits:**

- Standardised academic identity representation across European institutions
- Support for student mobility through European Student Identifier (ESI)
- Integration with REFEDS Assurance Framework (RAF)
- Compatibility with eduPerson attribute schema
- Persistent and non-revocable identification through community identifiers

### Implementation considerations

#### Identifier Management
- Implement hex-based identifier generation (64 digits max)
- Ensure identifier uniqueness within erasmus.eduteams.org scope
- Handle identifier persistence requirements

#### Affiliation Handling
- Validate affiliation syntax against eduPerson standard
- Implement proper scope handling for affiliations
- Manage multiple organisation affiliations

#### Integration Requirements
- Interface with REFEDS Assurance Framework
- Handle proper URI formatting for assurance values
- Implement proper ESI lifecycle management

### Field Specifications

| Field | Path | Description | Type | Mandatory |
|-------|------|-------------|------|-----------|
| **ID** | `credentialSubject.id` | User's DID identifier | string | Yes |
| **Community User ID** | `credentialSubject.communityUserIdentifier` | Unique, persistent identifier in MyAcademicId namespace | string | Yes |
| **Display Name** | `credentialSubject.displayName` | User's full name (firstname lastname) | string | Yes |
| **Given Name** | `credentialSubject.givenName` | User's given name(s) | string | Yes |
| **Family Name** | `credentialSubject.familyName` | User's surname(s) | string | Yes |
| **Email Address** | `credentialSubject.emailAddress` | User's email address | string (email) | Yes |
| **Assurance** | `credentialSubject.assurance` | Identity assurance levels (RAF) | array of URIs | Yes |
| **European Student ID** | `credentialSubject.europeanStudentIdentifier` | ESI for student mobility | array of strings | No |
| **External Affiliation** | `credentialSubject.externalAffiliation` | Affiliations with home organisations | array of strings | No |
| **Organisation** | `credentialSubject.organization` | User's primary organisation | string | No |
| **Entitlements** | `credentialSubject.entitlements` | User's rights and privileges | array of strings | No |

### Schema Structure Visualisation

![MyAcademicId Schema Structure](../../images/bbp-image33.png)

### JSON serialisation

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "MyAcademicId",
  "description": "Schema of an MyAcademicId Verifiable Credential",
  "type": "object",
  "allOf": [
    {
      "$ref": "./node_modules/@cef-ebsi/vcdm1.1-attestation-schema/schema.json"
    },
    {
      "properties": {
        "credentialSubject": {
          "description": "Defines additional properties on credentialSubject to describe IDs that do not have a substantial level of assurance.",
          "type": "object",
          "properties": {
            "id": {
              "description": "Defines a unique identifier of the credential subject. DID of the user",
              "type": "string"
            },
            "communityUserIdentifier": {
              "description": "User's Community Identifier is an opaque and non-revocable identifier (i.e. it cannot change over time) that follows the syntax of eduPersonUniqueId attribute of eduPerson. It consists of "uniqueID" part and fixed scope "erasmus.eduteams.org", separated by at sign. The uniqueID part contains up to 64 hexadecimal digits (a-f, 0-9). The identifier is unique and persistent within the MyAcademicId namespace. The identifier can be used for identity matching, etc. OID: 1.3.6.1.4.1.5923.1.1.1.13 Definition: https://wiki.refeds.org/display/STAN/eduPerson+2021-11#eduPerson202111-eduPersonUniqueId",
              "type": "string"
            },
            "europeanStudentIdentifier": {
              "description": "The European Student Identifier (ESI) of the user. ESI ensures mobility. Lifetime is limited to the period of student's mobility. ESI structure is defined in the document referenced below. ESI SHOULD NOT be parsed to extract information about the originating organisation of the student since the identifier structure is subject to a change. OID: 1.3.6.1.4.1.25178.1.2.14 Definition: https://wiki.geant.org/display/SM/European+Student+Identifier",
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "externalAffiliation": {
              "description": "Affiliation within Home Organisation. One or more home organisations (such as, universities, research institutions or private companies) this user is affiliated with. The syntax and semantics follows eduPersonScopedAffiliation attribute. Affiliation is external to the MyAcademicId. OID: 1.3.6.1.4.1.25178.4.1.11 Definition: https://wiki.refeds.org/display/STAN/eduPerson+2021-11#eduPerson202111-eduPersonScopedAffiliation",
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "organization": {
              "description": "This attribute describes the organisation of this user. OID: 1.3.6.1.4.1.25178.1.2.9",
              "type": "string"
            },
            "displayName": {
              "description": "User's name (firstname lastname). For more complex names. OID: 2.16.840.1.113730.3.1.241 Definition: https://wiki.refeds.org/display/STAN/eduPerson+2021-11#eduPerson202111-displayName",
              "type": "string"
            },
            "givenName": {
              "description": "strings that are the part of a person's name that is not their surname (see RFC4519). OID: 2.5.4. Definition: https://wiki.refeds.org/display/STAN/eduPerson+2021-11#eduPerson202111-givenName",
              "type": "string"
            },
            "familyName": {
              "description": "strings that are a person's surname (see RFC4519). OID: 2.5.4.4 Definition: https://wiki.refeds.org/display/STAN/eduPerson+2021-11#eduPerson202111-sn",
              "type": "string"
            },
            "emailAddress": {
              "description": "address of the user. OID: 0.9.2342.19200300.100.1.3 Definition: https://wiki.refeds.org/display/STAN/eduPerson+2021-11#eduPerson202111-homePostalAddress",
              "type": "string",
              "format": "email"
            },
            "entitlements": {
              "description": "This attribute describes the entitlements of this user. OID: 1.3.6.1.4.1.5923.1.1.1.7 Definition: https://wiki.refeds.org/display/STAN/eduPerson+2021-11#eduPerson202111-eduPersonEntitlement",
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "assurance": {
              "description": "Assurance of the identity of the user, following REFEDS Assurance Framework (RAF). OID: 1.3.6.1.4.1.5923.1.1.1.11 Definition: https://wiki.refeds.org/display/STAN/eduPerson+2021-11#eduPerson202111-eduPersonAssurance",
              "type": "array",
              "items": {
                "type": "string",
                "format": "uri"
              }
            }
          },
          "required": [
            "id",
            "communityUserIdentifier",
            "displayName",
            "givenName",
            "familyName",
            "emailAddress",
            "assurance"
          ]
        }
      }
    }
  ]
}
```

## European Learning Model (ELM) Data Model

### Introduction

The Europass EDC schema defines the structure for European Digital Credentials based on ELM (European Learning Model) 3.2. This comprehensive data model implements the W3C Verifiable Credentials Data Model and provides a standardised way to represent educational credentials in the European context.

**Key benefits:**

- Full compliance with European Learning Model 3.2
- Support for multilingual content
- Rich metadata for credential display and verification
- Comprehensive learning outcome documentation
- Flexible credential profiling system
- Support for multiple assessment and grading schemes
- Integration with European educational frameworks

### Implementation considerations

#### Multilingual Support
- Implement proper language tag handling
- Handle right-to-left script requirements
- Manage translation consistency

#### Display Requirements
- Implement proper rendering of credential displays
- Handle different device and format requirements
- Manage credential visualisation standards

#### Technical Integration
- Interface with European Learning Model
- Handle proper version management
- Implement assessment and grading schemes

### Field Specifications

| Field | Path | Description | Type | Mandatory |
|-------|------|-------------|------|-----------|
| **Credential Profiles** | `credentialProfiles` | Defines the credential's classification | ConceptType array | Yes |
| **Display Parameter** | `displayParameter` | Visual presentation parameters | DisplayParameterType | Yes |
| **Issuer** | `issuer` | Credential issuing organisation | Agent/Person/Organisation | Yes |
| **Credential Subject** | `credentialSubject` | The recipient of the credential | Agent/Person/Organisation | Yes |
| **Issue Date** | `issued` | Credential issuance date | DateTime | Yes |
| **Valid From** | `validFrom` | Credential validity start date | DateTime | Yes |
| **Credential Schema** | `credentialSchema` | Schema validation information | CredentialSchemaType | Yes |
| **Identifier** | `identifier` | Credential unique identifiers | Identifier/LegalIdentifier | No |
| **Attachment** | `attachment` | Associated media objects | MediaObject array | No |
| **Expiration Date** | `expirationDate` | Credential expiry date | DateTime | No |
| **Evidence** | `evidence` | Supporting evidence | EvidenceType array | No |
| **Terms of Use** | `termsOfUse` | Usage conditions | TermsOfUseType array | No |
| **Credential Status** | `credentialStatus` | Verification status | CredentialStatusType | No |
| **Proof** | `proof` | Cryptographic proof | ProofType array | No |

### Schema Structure Visualisation

![ELM Schema Structure](../../images/bbp-image34.png)

### JSON serialisation

*Note: Due to the extensive nature of the complete ELM JSON schema (containing thousands of lines), the full serialisation is provided in the complete technical documentation. The schema includes comprehensive definitions for all European Learning Model entities including:*

- **Learning achievements and specifications**
- **Learning activities and assessments**
- **Qualification frameworks and credit systems**
- **Multilingual content support**
- **Accreditation and quality assurance**
- **Display and presentation parameters**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Europass EDC credential",
  "description": "Schema for EDC credential based on ELM 3.2",
  "type": "object",
  "allOf": [
    {
      "$ref": "./node_modules/@cef-ebsi/vcdm1.1-attestation-schema/schema.json"
    },
    {
      "$ref": "#/$defs/EuropeanDigitalCredentialType"
    }
  ],
  "$defs": {
    "EuropeanDigitalCredentialType": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/GenericIdType"
        },
        "type": {
          "type": "array",
          "items": {
            "type": "string",
            "enum": [
              "VerifiableCredential",
              "VerifiableAttestation",
              "EuropeanDigitalCredential"
            ]
          },
          "minItems": 3,
          "uniqueItems": true
        },
        "credentialProfiles": {
          "$ref": "#/$defs/Many!ConceptType"
        },
        "displayParameter": {
          "$ref": "#/$defs/DisplayParameterType"
        },
        "issuer": {
          "anyOf": [
            {
              "$ref": "#/$defs/AgentOrPersonOrOrganisationType"
            },
            {
              "$ref": "#/$defs/GenericIdType"
            }
          ]
        },
        "credentialSubject": {
          "$ref": "#/$defs/AgentOrPersonOrOrganisationType"
        },
        "issued": {
          "$ref": "#/$defs/DateTimeType"
        },
        "validFrom": {
          "$ref": "#/$defs/DateTimeType"
        },
        "credentialSchema": {
          "$ref": "#/$defs/Many!CredentialSchemaType"
        }
      },
      "required": [
        "credentialProfiles",
        "displayParameter",
        "issuer",
        "credentialSubject",
        "issued",
        "validFrom",
        "credentialSchema"
      ]
    }
  }
}
```

*The complete schema definition includes extensive type definitions for all ELM entities as detailed in [Chapter 9](chapter9.md) of the main document.*

---

*This annex provides the complete data model specifications that enable the operational framework described in [Chapter 4](chapter4.md) and support the use cases demonstrated in [Chapter 7](chapter7.md). These standardised formats ensure interoperability whilst maintaining the flexibility required for diverse European educational contexts.*