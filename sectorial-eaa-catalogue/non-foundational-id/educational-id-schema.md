# Educational ID Schema

## Overview

The Educational ID Schema defines the data structure for representing educational identity credentials that confirm a student's affiliation with an educational institution. This schema supports verification of student status, programme enrolment, and access rights.

## Schema Structure

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://eaa-rulebook.europa.eu/schemas/educational-id/1.0.0",
  "title": "Educational ID",
  "description": "Schema for educational identity credentials",
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
        "https://eaa-rulebook.europa.eu/2023/credentials/educational-id/v1"
      ]
    },
    "id": {
      "type": "string",
      "format": "uri",
      "description": "Unique identifier for the educational ID credential"
    },
    "type": {
      "type": "array",
      "description": "Credential type definitions",
      "items": {
        "type": "string"
      },
      "default": ["VerifiableCredential", "EducationalIdCredential"]
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
        },
        "type": {
          "type": "string",
          "description": "Type of educational institution",
          "enum": [
            "University",
            "College",
            "VocationalSchool",
            "SecondarySchool",
            "PrimarySchool",
            "ResearchInstitute",
            "Other"
          ]
        }
      },
      "required": ["id", "name"]
    },
    "issuanceDate": {
      "type": "string",
      "format": "date",
      "description": "Date when the educational ID was issued"
    },
    "expirationDate": {
      "type": "string",
      "format": "date",
      "description": "Date when the educational ID expires"
    },
    "credentialSubject": {
      "type": "object",
      "description": "Information about the student and their status",
      "properties": {
        "id": {
          "type": "string",
          "format": "uri",
          "description": "Identifier of the credential subject"
        },
        "fullName": {
          "type": "string",
          "description": "Full name of the student"
        },
        "dateOfBirth": {
          "type": "string",
          "format": "date",
          "description": "Date of birth of the student"
        },
        "studentId": {
          "type": "string",
          "description": "Institutional student identifier"
        },
        "academicStatus": {
          "type": "string",
          "description": "Academic status of the student",
          "enum": [
            "EnrolledFull",
            "EnrolledPart",
            "Exchange",
            "OnLeave",
            "
