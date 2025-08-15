# Annex G: Registry URLs and Schema Locations

## Introduction

This annex provides a comprehensive directory of all registry URLs, schema locations, and service endpoints for the DC4EU sectoral EAA catalogue. The directory serves as the authoritative reference for implementers, system integrators, and auditors requiring access to trust registries, schema repositories, and supporting infrastructure components.

## G.1 European Blockchain Services Infrastructure (EBSI) Endpoints

### G.1.1 Core EBSI Infrastructure

#### G.1.1.1 Primary EBSI Endpoints

```json
{
  "ebsiInfrastructure": {
    "production": {
      "baseUrl": "https://api.ebsi.eu",
      "description": "Production EBSI API endpoint",
      "status": "operational",
      "availability": "24/7",
      "supportedVersions": ["v4", "v5"]
    },
    "pilot": {
      "baseUrl": "https://api-pilot.ebsi.eu",
      "description": "Pilot environment for testing and development",
      "status": "operational",
      "availability": "24/7 (best effort)",
      "supportedVersions": ["v3", "v4", "v5"]
    },
    "conformance": {
      "baseUrl": "https://api-conformance.ebsi.eu",
      "description": "Conformance testing environment",
      "status": "operational",
      "availability": "business hours",
      "supportedVersions": ["v4", "v5"]
    }
  }
}
```

#### G.1.1.2 EBSI Service Components

```json
{
  "ebsiServices": {
    "didRegistry": {
      "endpoint": "https://api-pilot.ebsi.eu/did-registry/v4",
      "description": "Decentralised Identifier Registry",
      "operations": ["register", "resolve", "update", "deactivate"],
      "authentication": "Bearer token or DID Auth"
    },
    "trustedIssuersRegistry": {
      "endpoint": "https://api-pilot.ebsi.eu/trusted-issuers-registry/v4",
      "description": "Registry of authorised credential issuers",
      "operations": ["query", "register", "update"],
      "authentication": "Qualified certificate required"
    },
    "trustedSchemasRegistry": {
      "endpoint": "https://api-pilot.ebsi.eu/trusted-schemas-registry/v3",
      "description": "Repository of verified credential schemas",
      "operations": ["query", "register", "validate"],
      "authentication": "Public read, qualified cert for write"
    },
    "timestamping": {
      "endpoint": "https://api-pilot.ebsi.eu/timestamp/v4",
      "description": "Qualified timestamping service",
      "operations": ["timestamp", "verify"],
      "authentication": "API key or qualified certificate"
    },
    "ledger": {
      "endpoint": "https://api-pilot.ebsi.eu/ledger/v4",
      "description": "Blockchain ledger access",
      "operations": ["query", "submit"],
      "authentication": "Read public, write requires authorization"
    }
  }
}
```

### G.1.2 Trust Registry Endpoints

#### G.1.2.1 Trusted Issuer Registry (TIR)

```json
{
  "trustedIssuerRegistry": {
    "apiEndpoints": {
      "production": "https://api.ebsi.eu/trusted-issuers-registry/v4",
      "pilot": "https://api-pilot.ebsi.eu/trusted-issuers-registry/v4",
      "conformance": "https://api-conformance.ebsi.eu/trusted-issuers-registry/v4"
    },
    "operations": {
      "queryIssuer": {
        "method": "GET",
        "path": "/issuers/{did}",
        "description": "Retrieve issuer information by DID",
        "authentication": "none",
        "rateLimit": "1000 requests/hour"
      },
      "queryByCredentialType": {
        "method": "GET", 
        "path": "/issuers?credentialType={type}",
        "description": "Find issuers authorised for specific credential type",
        "authentication": "none",
        "rateLimit": "1000 requests/hour"
      },
      "registerIssuer": {
        "method": "POST",
        "path": "/issuers",
        "description": "Register new authorised issuer",
        "authentication": "qualified certificate",
        "authorisation": "TAOR member only"
      },
      "updateIssuer": {
        "method": "PUT",
        "path": "/issuers/{did}",
        "description": "Update issuer authorisation scope",
        "authentication": "qualified certificate",
        "authorisation": "TAOR member or issuer self-update"
      }
    },
    "dataFormat": {
      "request": "application/json",
      "response": "application/json",
      "schema": "https://schemas.dc4eu.eu/registries/tir/v1.0/entry.json"
    }
  }
}
```

#### G.1.2.2 Trusted Accreditation Organisation Registry (TAOR)

```json
{
  "trustedAccreditationRegistry": {
    "apiEndpoints": {
      "production": "https://api.ebsi.eu/trusted-accreditation-registry/v4",
      "pilot": "https://api-pilot.ebsi.eu/trusted-accreditation-registry/v4"
    },
    "operations": {
      "queryAccreditor": {
        "method": "GET",
        "path": "/accreditors/{did}",
        "description": "Retrieve accreditation authority information",
        "authentication": "none"
      },
      "listAccreditors": {
        "method": "GET",
        "path": "/accreditors?sector={sector}&jurisdiction={country}",
        "description": "List accreditation authorities by sector and jurisdiction",
        "authentication": "none"
      },
      "validateAccreditation": {
        "method": "POST",
        "path": "/validate",
        "description": "Validate accreditation chain",
        "authentication": "none",
        "payload": "accreditation credential"
      }
    },
    "supportedSectors": [
      "higher_education",
      "vocational_education", 
      "professional_qualifications",
      "quality_assurance"
    ]
  }
}
```

#### G.1.2.3 Trusted Schema Registry (TSR)

```json
{
  "trustedSchemaRegistry": {
    "apiEndpoints": {
      "production": "https://api.ebsi.eu/trusted-schemas-registry/v3",
      "pilot": "https://api-pilot.ebsi.eu/trusted-schemas-registry/v3"
    },
    "operations": {
      "getSchema": {
        "method": "GET",
        "path": "/schemas/{schemaId}",
        "description": "Retrieve schema by identifier",
        "authentication": "none",
        "caching": "24 hours"
      },
      "querySchemas": {
        "method": "GET",
        "path": "/schemas?type={credentialType}&sector={sector}",
        "description": "Search schemas by type and sector",
        "authentication": "none"
      },
      "validateCredential": {
        "method": "POST",
        "path": "/schemas/{schemaId}/validate",
        "description": "Validate credential against schema",
        "authentication": "none",
        "payload": "verifiable credential"
      },
      "registerSchema": {
        "method": "POST",
        "path": "/schemas",
        "description": "Register new schema",
        "authentication": "qualified certificate",
        "authorisation": "schema governance board"
      }
    },
    "contextDocuments": {
      "baseContext": "https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/contexts/european-digital-credential-v3.jsonld",
      "educationContext": "https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/contexts/education-v1.jsonld",
      "professionalContext": "https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/contexts/professional-v1.jsonld"
    }
  }
}
```

## G.2 Schema Repository Locations

### G.2.1 Formal Education Schemas

#### G.2.1.1 Higher Education Credentials

```json
{
  "higherEducationSchemas": {
    "europeanHigherEducationDiploma": {
      "schemaId": "0x7663df08b9a50f226e185efb7ec08f3d69f4a95e653ebffd3137b3eb6923dda8",
      "registryUrl": "https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/0x7663df08b9a50f226e185efb7ec08f3d69f4a95e653ebffd3137b3eb6923dda8",
      "localSchema": "https://schemas.dc4eu.eu/formal-education/euhed/v1.0/schema.json",
      "credentialType": "EUHED",
      "description": "European Higher Education Diploma credential schema",
      "version": "1.0",
      "status": "active"
    },
    "europeanHigherEducationDiplomaSupplement": {
      "schemaId": "0x597214a686156123e6603272b72638a615d83037d306b16170ff838168dfaf13",
      "registryUrl": "https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/0x597214a686156123e6603272b72638a615d83037d306b16170ff838168dfaf13",
      "localSchema": "https://schemas.dc4eu.eu/formal-education/euheds/v1.0/schema.json",
      "credentialType": "EUHEDS",
      "description": "European Higher Education Diploma Supplement schema",
      "version": "1.0",
      "status": "active"
    },
    "europeanHigherEducationTranscriptOfRecords": {
      "schemaId": "0x1e4611b4d031fbd282e6cfc241623d3b25f322ed87aee7670f7c1a20a63c14f3",
      "registryUrl": "https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/0x1e4611b4d031fbd282e6cfc241623d3b25f322ed87aee7670f7c1a20a63c14f3",
      "localSchema": "https://schemas.dc4eu.eu/formal-education/euhetor/v1.0/schema.json",
      "credentialType": "EUHETOR",
      "description": "European Higher Education Transcript of Records schema",
      "version": "1.0",
      "status": "active"
    },
    "europeanHigherEducationProofOfEnrolment": {
      "schemaId": "0x9e7bdbe465fbca504ec04df331c47ef6d88eb258312d3471277e84dabda4a92e",
      "registryUrl": "https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/0x9e7bdbe465fbca504ec04df331c47ef6d88eb258312d3471277e84dabda4a92e",
      "localSchema": "https://schemas.dc4eu.eu/formal-education/euhepoe/v1.0/schema.json",
      "credentialType": "EUHEPOE",
      "description": "European Higher Education Proof of Enrolment schema",
      "version": "1.0",
      "status": "active"
    },
    "europeanHigherEducationMicroCredential": {
      "schemaId": "0x05332a9dc53a4a26a15711262904f2a1dd081cf3da735350f42dac20426530a4",
      "registryUrl": "https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/0x05332a9dc53a4a26a15711262904f2a1dd081cf3da735350f42dac20426530a4",
      "localSchema": "https://schemas.dc4eu.eu/formal-education/euhemc/v1.0/schema.json",
      "credentialType": "EUHEMC",
      "description": "European Higher Education Micro-credential schema",
      "version": "1.0",
      "status": "active"
    }
  }
}
```

#### G.2.1.2 Vocational Education and Training Schemas

```json
{
  "vocationalEducationSchemas": {
    "europeanVETMicroCredential": {
      "schemaId": "0x690878adbdbc2c6b2865829003a1e34800df5d173d302ff11958836f8f977a26",
      "registryUrl": "https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/0x690878adbdbc2c6b2865829003a1e34800df5d173d302ff11958836f8f977a26",
      "localSchema": "https://schemas.dc4eu.eu/formal-education/euvetmc/v1.0/schema.json",
      "credentialType": "EUVETMC",
      "description": "European VET Micro-credential schema",
      "version": "1.0",
      "status": "active"
    },
    "europeanUpperSecondaryEducationCertificate": {
      "schemaId": "0x901e24612f601d3f6932b3d20ba50615cfd6d64ce4e8c263312b5c3c3b2f9623",
      "registryUrl": "https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/0x901e24612f601d3f6932b3d20ba50615cfd6d64ce4e8c263312b5c3c3b2f9623",
      "localSchema": "https://schemas.dc4eu.eu/formal-education/euusc/v1.0/schema.json",
      "credentialType": "EUUSC",
      "description": "European Upper Secondary Education Certificate schema",
      "version": "1.0",
      "status": "active"
    },
    "europeanUpperSecondaryEducationTranscript": {
      "schemaId": "0xaf79750aade036da40ba02a0b85f671d7232a1ad13df91b72df2ba0891f91aba",
      "registryUrl": "https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/0xaf79750aade036da40ba02a0b85f671d7232a1ad13df91b72df2ba0891f91aba",
      "localSchema": "https://schemas.dc4eu.eu/formal-education/euustor/v1.0/schema.json",
      "credentialType": "EUUSTOR", 
      "description": "European Upper Secondary Education Transcript of Records schema",
      "version": "1.0",
      "status": "active"
    }
  }
}
```

### G.2.2 Professional Qualifications Schemas

#### G.2.2.1 Professional Competence Credentials

```json
{
  "professionalQualificationSchemas": {
    "certificateOfProfessionalCompetence": {
      "schemaId": "0x8f9d123e456f789a012b345c678d901e234f567a890b123c456d789e012f345a",
      "registryUrl": "https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/0x8f9d123e456f789a012b345c678d901e234f567a890b123c456d789e012f345a",
      "localSchema": "https://schemas.dc4eu.eu/professional-qualifications/cpc/v1.0/schema.json",
      "credentialType": "CPC",
      "description": "Certificate of Professional Competence schema",
      "version": "1.0",
      "status": "active"
    },
    "certificateOfProfessionalSuitability": {
      "schemaId": "0x2d5971743a402de5ba00aad9697200153cbac29ccb5b1852e704cd541213f994",
      "registryUrl": "https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/0x2d5971743a402de5ba00aad9697200153cbac29ccb5b1852e704cd541213f994",
      "localSchema": "https://schemas.dc4eu.eu/professional-qualifications/cps/v1.0/schema.json",
      "credentialType": "CPS",
      "description": "Certificate of Professional Suitability schema",
      "version": "1.0",
      "status": "active"
    },
    "accreditationMedicalTraining": {
      "schemaId": "0xa92c40f0684db3bbcf2bb2600579dfaf7785a421515394c79eb9de41debf17a7",
      "registryUrl": "https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/0xa92c40f0684db3bbcf2bb2600579dfaf7785a421515394c79eb9de41debf17a7",
      "localSchema": "https://schemas.dc4eu.eu/professional-qualifications/amt/v1.0/schema.json",
      "credentialType": "AMT",
      "description": "Accreditation Medical Training schema",
      "version": "1.0",
      "status": "active"
    },
    "continuousProfessionalDevelopment": {
      "schemaId": "z3RwKaN1kZciYkRpkqjwTW6whKV4WefiYx6wviWR7gzow",
      "registryUrl": "https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/z3RwKaN1kZciYkRpkqjwTW6whKV4WefiYx6wviWR7gzow",
      "localSchema": "https://schemas.dc4eu.eu/professional-qualifications/cpd/v1.0/schema.json",
      "credentialType": "CPD",
      "description": "Continuous Professional Development schema",
      "version": "1.0",
      "status": "active"
    },
    "professionalTrainingCertificate": {
      "schemaId": "zCPP3GVyk2bK65E81K8BC6T2gdNYQNEeKgm9wEYuSgHTU",
      "registryUrl": "https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/zCPP3GVyk2bK65E81K8BC6T2gdNYQNEeKgm9wEYuSgHTU",
      "localSchema": "https://schemas.dc4eu.eu/professional-qualifications/ptc/v1.0/schema.json",
      "credentialType": "PTC",
      "description": "Professional Training Certificate schema",
      "version": "1.0",
      "status": "active"
    }
  }
}
```

### G.2.3 Non-Foundational Identity Schemas

#### G.2.3.1 Educational Identity Credentials

```json
{
  "nonFoundationalIdentitySchemas": {
    "verifiableEducationId": {
      "schemaId": "zEmFZquJtANNz7XNE46thRi1E2cAfpQiXVLSBdDgLyfGP",
      "registryUrl": "https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/zEmFZquJtANNz7XNE46thRi1E2cAfpQiXVLSBdDgLyfGP",
      "localSchema": "https://schemas.dc4eu.eu/non-foundational-id/educational-id/v1.0/schema.json",
      "credentialType": "EducationalID",
      "description": "Verifiable Education ID schema",
      "version": "1.0",
      "status": "active"
    },
    "allianceId": {
      "schemaId": "zCHc3ZfYg2871W2WftjLu4QNMQrDzG57oG5pvGoyHcagB",
      "registryUrl": "https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/zCHc3ZfYg2871W2WftjLu4QNMQrDzG57oG5pvGoyHcagB",
      "localSchema": "https://schemas.dc4eu.eu/non-foundational-id/alliance-id/v1.0/schema.json",
      "credentialType": "AllianceID",
      "description": "European University Alliance ID schema",
      "version": "1.0",
      "status": "active"
    },
    "europeanStudentCard": {
      "schemaId": "0x0e46f9509c52e649d8b461216b66836bd8398b8779469a571404264ea02c3bd9",
      "registryUrl": "https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/0x0e46f9509c52e649d8b461216b66836bd8398b8779469a571404264ea02c3bd9",
      "localSchema": "https://schemas.dc4eu.eu/non-foundational-id/european-student-card/v1.0/schema.json",
      "credentialType": "EuropeanStudentCard",
      "description": "European Student Card schema",
      "version": "1.0",
      "status": "active"
    },
    "myAcademicId": {
      "schemaId": "z3XDm4kDtztE8DzLsVdhfshYvx2upnfLmqHtyVjkaXM1g",
      "registryUrl": "https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/z3XDm4kDtztE8DzLsVdhfshYvx2upnfLmqHtyVjkaXM1g",
      "localSchema": "https://schemas.dc4eu.eu/non-foundational-id/my-academic-id/v1.0/schema.json",
      "credentialType": "MyAcademicID",
      "description": "MyAcademic ID schema for student mobility",
      "version": "1.0",
      "status": "active"
    }
  }
}
```

#### G.2.3.2 Professional Identity Credentials

```json
{
  "professionalIdentitySchemas": {
    "professionalId": {
      "schemaId": "z2CHBovrL2TptHFFtszG5Jn8LZU1SxLfMY6Vg93ctKEAw",
      "registryUrl": "https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/z2CHBovrL2TptHFFtszG5Jn8LZU1SxLfMY6Vg93ctKEAw",
      "localSchema": "https://schemas.dc4eu.eu/non-foundational-id/professional-id/v1.0/schema.json",
      "credentialType": "ProfessionalID",
      "description": "Professional identity credential schema",
      "version": "1.0",
      "status": "active"
    },
    "doctorId": {
      "schemaId": "zDD8wM8F6UsfrdACeph41EFmgEUUsDnC6SVqY4QFh8MFZ",
      "registryUrl": "https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/zDD8wM8F6UsfrdACeph41EFmgEUUsDnC6SVqY4QFh8MFZ",
      "localSchema": "https://schemas.dc4eu.eu/non-foundational-id/doctor-id/v1.0/schema.json",
      "credentialType": "DoctorID",
      "description": "Medical professional identity credential schema",
      "version": "1.0",
      "status": "active"
    },
    "engineerId": {
      "schemaId": "ziwaS92VRyKojd3Xmk9wgvBo5XYwqG8EYENK9zFQNJWG",
      "registryUrl": "https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/schemas/ziwaS92VRyKojd3Xmk9wgvBo5XYwqG8EYENK9zFQNJWG",
      "localSchema": "https://schemas.dc4eu.eu/non-foundational-id/engineer-id/v1.0/schema.json",
      "credentialType": "EngineerID",
      "description": "Engineering professional identity credential schema",
      "version": "1.0",
      "status": "active"
    }
  }
}
```

## G.3 Supporting Infrastructure Endpoints

### G.3.1 Status and Revocation Services

#### G.3.1.1 StatusList2021 Endpoints

```json
{
  "statusServices": {
    "production": {
      "baseUrl": "https://status.dc4eu.eu",
      "description": "Production status list service",
      "availability": "99.9% SLA"
    },
    "pilot": {
      "baseUrl": "https://status-pilot.dc4eu.eu", 
      "description": "Pilot status list service for testing",
      "availability": "Best effort"
    },
    "endpoints": {
      "statusLists": {
        "higherEducation": "https://status.dc4eu.eu/credentials/higher-education/2025",
        "vocationalEducation": "https://status.dc4eu.eu/credentials/vocational-education/2025",
        "professionalQualifications": "https://status.dc4eu.eu/credentials/professional/2025",
        "nonFoundationalId": "https://status.dc4eu.eu/credentials/identity/2025"
      },
      "operations": {
        "checkStatus": {
          "method": "GET",
          "path": "/status/{credentialId}",
          "description": "Check individual credential status"
        },
        "listStatus": {
          "method": "GET", 
          "path": "/status-list/{listId}",
          "description": "Retrieve complete status list"
        },
        "updateStatus": {
          "method": "POST",
          "path": "/status/{credentialId}",
          "description": "Update credential status",
          "authentication": "Issuer signature required"
        }
      }
    }
  }
}
```

### G.3.2 Policy and Terms of Reference Repositories

#### G.3.2.1 Disclosure Policy Repository

```json
{
  "policyRepositories": {
    "disclosurePolicies": {
      "baseUrl": "https://policies.dc4eu.eu",
      "endpoints": {
        "formalEducation": "https://policies.dc4eu.eu/formal-education",
        "professionalQualifications": "https://policies.dc4eu.eu/professional-qualifications",
        "nonFoundationalId": "https://policies.dc4eu.eu/non-foundational-id"
      },
      "policyTypes": {
        "catalogueLevel": "https://policies.dc4eu.eu/{sector}/{eaa-type}/disclosure-policy.json",
        "presentationLevel": "https://policies.dc4eu.eu/{sector}/{eaa-type}/presentation-policy.json",
        "consentLevel": "https://policies.dc4eu.eu/{sector}/{eaa-type}/consent-policy.json"
      }
    },
    "termsOfReference": {
      "baseUrl": "https://tsr.dc4eu.eu/tor",
      "format": "application/json",
      "authentication": "none",
      "examples": {
        "euhed": "https://tsr.dc4eu.eu/tor/euhed.json",
        "cpc": "https://tsr.dc4eu.eu/tor/cpc.json",
        "educationalId": "https://tsr.dc4eu.eu/tor/educational-id.json"
      }
    }
  }
}
```

### G.3.3 Monitoring and Health Check Endpoints

#### G.3.3.1 Service Health Monitoring

```json
{
  "monitoringEndpoints": {
    "serviceHealth": {
      "ebsiHealth": "https://api-pilot.ebsi.eu/health",
      "tirHealth": "https://api-pilot.ebsi.eu/trusted-issuers-registry/v4/health",
      "tsrHealth": "https://api-pilot.ebsi.eu/trusted-schemas-registry/v3/health",
      "statusHealth": "https://status.dc4eu.eu/health"
    },
    "metrics": {
      "performanceMetrics": "https://metrics.dc4eu.eu/performance",
      "uptimeMetrics": "https://metrics.dc4eu.eu/uptime",
      "usageStatistics": "https://metrics.dc4eu.eu/usage"
    },
    "statusPages": {
      "ebsiStatus": "https://status.ebsi.eu",
      "dc4euStatus": "https://status.dc4eu.eu",
      "maintenanceSchedule": "https://status.dc4eu.eu/maintenance"
    }
  }
}
```

## G.4 Local Development and Testing Resources

### G.4.1 Development Environment Endpoints

#### G.4.1.1 Local Schema Repository

```json
{
  "developmentResources": {
    "localSchemaRepository": {
      "baseUrl": "https://schemas.dc4eu.eu",
      "description": "Local schema repository for development and testing",
      "structure": {
        "formalEducation": "https://schemas.dc4eu.eu/formal-education/",
        "professionalQualifications": "https://schemas.dc4eu.eu/professional-qualifications/",
        "nonFoundationalId": "https://schemas.dc4eu.eu/non-foundational-id/",
        "foundationalIdentity": "https://schemas.dc4eu.eu/foundational-identity/"
      },
      "versioningScheme": "https://schemas.dc4eu.eu/{category}/{credential-type}/v{major}.{minor}/schema.json"
    },
    "validationServices": {
      "schemaValidation": "https://validator.dc4eu.eu/schema",
      "credentialValidation": "https://validator.dc4eu.eu/credential",
      "complianceCheck": "https://validator.dc4eu.eu/compliance"
    },
    "testDataSets": {
      "sampleCredentials": "https://samples.dc4eu.eu/credentials/",
      "testVectors": "https://samples.dc4eu.eu/test-vectors/",
      "conformanceTests": "https://samples.dc4eu.eu/conformance/"
    }
  }
}
```

### G.4.2 Integration Testing Endpoints

#### G.4.2.1 Sandbox Environments

```json
{
  "sandboxEnvironments": {
    "integrationTesting": {
      "baseUrl": "https://sandbox.dc4eu.eu",
      "description": "Integration testing environment",
      "authentication": "API key required",
      "dataRetention": "7 days",
      "resetSchedule": "Weekly on Sundays"
    },
    "conformanceTesting": {
      "baseUrl": "https://conformance.dc4eu.eu",
      "description": "Conformance testing environment",
      "testSuites": {
        "w3cVcdm": "https://conformance.dc4eu.eu/test-suites/w3c-vcdm",
        "eidas2": "https://conformance.dc4eu.eu/test-suites/eidas2",
        "ebsiCompatibility": "https://conformance.dc4eu.eu/test-suites/ebsi"
      }
    },
    "performanceTesting": {
      "baseUrl": "https://performance.dc4eu.eu",
      "description": "Performance testing environment",
      "loadTesting": "https://performance.dc4eu.eu/load-test",
      "stressTesting": "https://performance.dc4eu.eu/stress-test"
    }
  }
}
```

## G.5 Documentation and Support Resources

### G.5.1 Technical Documentation

#### G.5.1.1 API Documentation

```json
{
  "documentationResources": {
    "apiDocumentation": {
      "openApiSpecs": {
        "tirApi": "https://docs.dc4eu.eu/api/tir/openapi.json",
        "tsrApi": "https://docs.dc4eu.eu/api/tsr/openapi.json",
        "statusApi": "https://docs.dc4eu.eu/api/status/openapi.json"
      },
      "swaggerUI": {
        "tirApi": "https://docs.dc4eu.eu/api/tir/",
        "tsrApi": "https://docs.dc4eu.eu/api/tsr/",
        "statusApi": "https://docs.dc4eu.eu/api/status/"
      }
    },
    "implementationGuides": {
      "gettingStarted": "https://docs.dc4eu.eu/guides/getting-started",
      "integrationGuide": "https://docs.dc4eu.eu/guides/integration",
      "bestPractices": "https://docs.dc4eu.eu/guides/best-practices",
      "troubleshooting": "https://docs.dc4eu.eu/guides/troubleshooting"
    },
    "schemaDocumentation": {
      "catalogueOverview": "https://docs.dc4eu.eu/schemas/",
      "schemaRegistry": "https://docs.dc4eu.eu/schemas/registry",
      "validationRules": "https://docs.dc4eu.eu/schemas/validation"
    }
  }
}
```

### G.5.2 Support and Community Resources

#### G.5.2.1 Community Support

```json
{
  "supportResources": {
    "communitySupport": {
      "discussionForum": "https://community.dc4eu.eu",
      "developerChat": "https://chat.dc4eu.eu",
      "githubRepositories": {
        "schemas": "https://github.com/dc4eu/schemas",
        "tools": "https://github.com/dc4eu/tools",
        "documentation": "https://github.com/dc4eu/docs"
      }
    },
    "officialSupport": {
      "helpDesk": "https://support.dc4eu.eu",
      "ticketSystem": "https://tickets.dc4eu.eu",
      "escalationProcess": "https://support.dc4eu.eu/escalation",
      "slaInformation": "https://support.dc4eu.eu/sla"
    },
    "trainingSources": {
      "onlineTutorials": "https://training.dc4eu.eu/tutorials",
      "webinarSchedule": "https://training.dc4eu.eu/webinars",
      "certificationProgram": "https://training.dc4eu.eu/certification"
    }
  }
}
```

## G.6 Registry Maintenance and Updates

### G.6.1 Update Notification Services

#### G.6.1.1 Change Notification System

```json
{
  "updateNotifications": {
    "webhookEndpoints": {
      "schemaUpdates": "https://notifications.dc4eu.eu/webhooks/schema-updates",
      "registryChanges": "https://notifications.dc4eu.eu/webhooks/registry-changes",
      "statusChanges": "https://notifications.dc4eu.eu/webhooks/status-changes"
    },
    "rssFeeds": {
      "allUpdates": "https://feeds.dc4eu.eu/all-updates.xml",
      "schemaUpdates": "https://feeds.dc4eu.eu/schema-updates.xml",
      "registryUpdates": "https://feeds.dc4eu.eu/registry-updates.xml"
    },
    "subscriptionManagement": {
      "subscribe": "https://notifications.dc4eu.eu/subscribe",
      "unsubscribe": "https://notifications.dc4eu.eu/unsubscribe",
      "preferences": "https://notifications.dc4eu.eu/preferences"
    }
  }
}
```

### G.6.2 Backup and Archive Services

#### G.6.2.1 Data Preservation

```json
{
  "dataPreservation": {
    "backupServices": {
      "dailyBackups": "https://backup.dc4eu.eu/daily",
      "weeklyArchives": "https://backup.dc4eu.eu/weekly",
      "monthlyArchives": "https://backup.dc4eu.eu/monthly"
    },
    "historicalVersions": {
      "schemaVersions": "https://archive.dc4eu.eu/schemas",
      "registrySnapshots": "https://archive.dc4eu.eu/registries",
      "configurationHistory": "https://archive.dc4eu.eu/config"
    },
    "accessPolicies": {
      "publicAccess": "Read-only access to current versions",
      "authenticatedAccess": "Historical version access with authentication",
      "authorisedAccess": "Administrative access for authorised personnel"
    }
  }
}
```

## G.7 Registry URL Quick Reference

### G.7.1 Essential URLs Summary

```json
{
  "quickReference": {
    "primaryEndpoints": {
      "ebsiPilot": "https://api-pilot.ebsi.eu",
      "trustedSchemas": "https://api-pilot.ebsi.eu/trusted-schemas-registry/v3",
      "trustedIssuers": "https://api-pilot.ebsi.eu/trusted-issuers-registry/v4",
      "statusService": "https://status.dc4eu.eu",
      "policyRepository": "https://policies.dc4eu.eu"
    },
    "documentationHubs": {
      "dc4euDocs": "https://docs.dc4eu.eu",
      "ebsiDocs": "https://api-pilot.ebsi.eu/docs",
      "schemaRegistry": "https://schemas.dc4eu.eu",
      "apiReference": "https://docs.dc4eu.eu/api"
    },
    "supportChannels": {
      "technicalSupport": "https://support.dc4eu.eu",
      "communityForum": "https://community.dc4eu.eu",
      "statusPage": "https://status.dc4eu.eu",
      "updateNotifications": "https://notifications.dc4eu.eu"
    }
  }
}
```

---

**Note**: All URLs and endpoints listed in this annex are maintained and updated regularly. For the most current information, always consult the official DC4EU documentation at https://docs.dc4eu.eu and the EBSI documentation at https://api-pilot.ebsi.eu/docs. Registry endpoints may be subject to versioning changes, and implementers should monitor update notifications for any modifications to service locations or API versions.