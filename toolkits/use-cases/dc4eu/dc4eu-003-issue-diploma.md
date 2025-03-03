# Issue a Diploma - v1.0

**Authors:**

* Angel Palomares (<angel.palomares@eviden.com>)

**Reviewers:**

* LLuis Ariño (lluisalfons.arino@urv.cat)

**Status:** Approved for v1.0

**Table of Contents:**

* [1 Summary](#1-summary)
* [2 Issue a Diploma Flow](#2-issue-a-diploma-flow)
* [3 Message Details](#3-message-details)
  * [3.1 Initiate Credential Offer](#31-initiate-credential-offer)
  * [3.2 Credential Offer Response](#32-credential-offer-response)
  * [3.3 Authorization request](#33-authorization-request)
  * [3.4 Authorization response](#34-authorization-response)
  * [3.5 Token request](#35-token-request)
  * [3.6 Token Response](#36-token-response)
  * [3.7 Credential Request](#37-credential-request)
  * [3.8 Credential Response](#38-credential-response)

* [4 References](#4-references)

## [1 Summary](#1-summary)

This section defines in detail how to obtain a Diploma. This flow is based a No Authorize OpenID VCI flow, providing a Verifiable Presentation probing the possession of a Verifiable Education ID.

## [2 Issue a Diploma Flow](#2-issue-a-diploma-flow)

Figure 1 shows the different steps for a Student for obtaining a Verifiable Educational Id

```mermaid
sequenceDiagram
autonumber
  actor student as Student
  participant mobile as Mobile Wallet 

  box LightGreen University Infrastructure
    participant stdGUI as Student GUI
    participant agent as uSelf Issuer Agent
    participant authSource as Authentic Source
    participant db as Postgres DB
  end
  box LightBlue EBSI Infrastructure
    participant didr as EBSI DID Registry
    participant trr as EBSI TR Registry
    participant sr as EBSI Schema Registry
    participant proxy as EBSI Proxy
    participant issuer as uSelf PID Issuer Agent
  end


  student->stdGUI: GET http://student-web/issue
  activate stdGUI
  stdGUI->agent: GET http://uself-agent/issuer/crendential-offer
  
  activate agent
  agent-->stdGUI: credential_offer
  deactivate agent
  stdGUI->stdGUI: generate QRCode
  mobile->stdGUI: read QRCode
  activate mobile 
  mobile-->mobile: redirect - http status = 302
  mobile->agent: GET http://uself-agent/auth/authorize
  activate agent 
  agent-->mobile: redirect direct_post
  deactivate agent
  student->mobile: consent to send Verifiable Education ID
  mobile-->mobile: redirect - http status = 302
  mobile->agent: POST http://uself-agent/direct_post
  activate agent
  note left of agent: sent the verifiable educational Id of the student to be verified
  agent->agent: verify VerifiableEducationID VP

  

  agent->didr: GET http://ebsi-did-registry/did
  activate didr 
  didr-->agent: did
  deactivate didr

  agent->trr:GET http://ebsi-tr-registry/tr
  activate trr 
  trr-->agent: tr
  deactivate trr

  agent->sr:GET http://ebsi-schema-registry/schema
  activate sr 
  sr-->agent: schema
  deactivate sr

  agent->proxy: GET http://ebsi-proxy/verify
  activate proxy 
      proxy->issuer: GET http://uself-issuer/status
      activate issuer 
      issuer-->proxy: status
      deactivate issuer
  proxy-->agent: status
  deactivate proxy
  

  
  agent-->mobile: code
  deactivate agent
  mobile-->mobile: redirect - http status = 302 
  mobile->agent: GET http://uself-agent/auth/token
  activate agent 
  agent-->mobile: access_token
  deactivate agent
  mobile->agent: POST http://uself-agent/issuer/credential
  activate agent 
  agent->authSource: GET http://auth-source/diploma/diploma
  activate authSource 
  authSource->db: SELECT * FROM diploma\n WHERE id = diploma_identifier
  activate db 
  db-->authSource: diploma info
  deactivate db
  authSource-->agent: diploma info
  deactivate authSource
  agent-->stdGUI: send event credential_issued
  agent-->mobile: credential
  deactivate agent
  deactivate mobile
  deactivate stdGUI

```

          Figure 1: No Authorize OpenID VCI Flow providing a Verifiable Educational Id Verifiable Presentation

## [3 Message Details](#3-message-details)

### [3.1 Initiate Credential Offer](#31-initiate-credential-offer)

Although the standard doesn't specify how to trigger the credential offer, we define the initialize of the credential offer following the suggestions proposed by EBSI.

```http
GET from https://issuer.eu/issuer/initiate-credential-offer?
  credential_type=CertificateProfessionalCompetence
  &nonce=d527c191-6e1d-4c3d-9843-9eaf2005fba9
```

### [3.2 Credential Offer Response](#32-credential-offer-response)

In order to avoid overloading the result of the QRCode, the standard defines a entry point based on `credential_offer_uri`parameter:

```http
openid-credential-offer://?credential_offer_uri=https://issuer.eu/issuer/offers/719307744250317677
```

The response to resolving the  `credential_offer_uri` will be different depending if is an No Authorize flow or a Pre Authorize flow.

```json
{
   "credential_issuer":"https://issuer.eu/issuer",
   "credentials":[
      {
         "format":"jwt_vc",
         "types":[
            "VerifiableCredential",
            "CertificateProfessionalCompetence"
         ],
         "trust_framework":{
            "name":"uSelf Agent Issuer",
            "type":"CertificateProfessionalCompetence",
            "uri":"CertificateProfessionalCompetence testing"
         },
         "display":[
            {
               "name":"CertificateProfessionalCompetence",
               "description":"Schema defining a verifiable credential that validates whether a registered physician has an up to date certificate of professional competence"
            }
         ],
         "credentialSubject":{
            "id":{
               "display":[
                  {
                     "name":"id"
                  }
               ]
            },
            "personal_administrative_number":{
               "display":[
                  {
                     "name":"personal_administrative_number",
                     "description":"Nationally registered physician number"
                  }
               ]
            },
            "given_name":{
               "display":[
                  {
                     "name":"given_name",
                     "description":"Natural person name"
                  }
               ]
            },
            "family_name":{
               "display":[
                  {
                     "name":"family_name",
                     "description":"Natural person surname"
                  }
               ]
            },
            "is_entitled":{
               "value_type":"boolean",
               "display":[
                  {
                     "name":"is_entitled",
                     "description":"Indicates whether the physician is legally entitled to practice as a doctor."
                  }
               ]
            }
         }
      }
   ],
   "grants":{
      "authorization_code":{
         "issuer_state":"eyJraWQiOiJkaWQ6ZWJzaTp6dFJvWXlKTmRHcjh0bUF0Vmg5Y2c5biIsInR5cCI6IkpXVCIsImFsZyI6IkVTMjU2In0.eyJhdWQiOiJodHRwczovL3RhZHBvbGUtaW50ZXJuYWwtbWFtbWFsLm5ncm9rLWZyZWUuYXBwL2F1dGgiLCJpc3MiOiJodHRwczovL3RhZHBvbGUtaW50ZXJuYWwtbWFtbWFsLm5ncm9rLWZyZWUuYXBwL2lzc3VlciIsImNyZWRlbnRpYWxfdHlwZXMiOlsiVmVyaWZpYWJsZUNyZWRlbnRpYWwiLCJDZXJ0aWZpY2F0ZVByb2Zlc3Npb25hbENvbXBldGVuY2UiXSwiZXhwIjoxNzQxMDE1NTcxLCJpYXQiOjE3NDEwMTE5NzEsIm5vbmNlIjoiNTQyMGJjMGQtNTk0Zi00NzIxLWIyNDEtMTZhMDU3NDJjZGY2In0.0f7DSlfYaID-FpL35x3AEliE6yX_CxvuYfh2ZUVeJnDo-1J91_fregjFgcyDqVr4tOYcAftFdVehid9NBvdaRA"
      }
   }
}
```

### [3.3 Authorization request](#33-authorization-request)

Once the Mobile Wallet has read the credential offer, it will request an authorization with the following parameters:

```http
GET from https://issuer.eu/auth/authorize?
  client_id=did:key:z2dmzD81cg...
  &response_type=code
  &scope=openid
  &response_uri=https://client.example.com
  &response_mode=direct_post
  &state=8d8b6a3d-4bc0-4234-9a9a-ed1928815502
  &nonce=d527c191-6e1d-4c3d-9843-9eaf2005fba9
  &issuer_state=eyJraWQiOiJkaWQ6ZWJzaTp6dFJvWXlKTmRHcjh0bUF0Vmg5Y2c5biIsInR5cCI6IkpXVCIsImFsZyI6IkVTMjU2In0.eyJhdWQiOiJodHRwczovL3RhZHBvbGUtaW50ZXJuYWwtbWFtbWFsLm5ncm9rLWZyZWUuYXBwL2F1dGgiLCJpc3MiOiJodHRwczovL3RhZHBvbGUtaW50ZXJuYWwtbWFtbWFsLm5ncm9rLWZyZWUuYXBwL2lzc3VlciIsImNyZWRlbnRpYWxfdHlwZXMiOlsiVmVyaWZpYWJsZUNyZWRlbnRpYWwiLCJDZXJ0aWZpY2F0ZVByb2Zlc3Npb25hbENvbXBldGVuY2UiXSwiZXhwIjoxNzQxMDE1NTcxLCJpYXQiOjE3NDEwMTE5NzEsIm5vbmNlIjoiNTQyMGJjMGQtNTk0Zi00NzIxLWIyNDEtMTZhMDU3NDJjZGY2In0.0f7DSlfYaID-FpL35x3AEliE6yX_CxvuYfh2ZUVeJnDo-1J91_fregjFgcyDqVr4tOYcAftFdVehid9NBvdaRA
  &code_challenge=wQ7kWVb4OwAxCtsMYALu9JXJjEujyZYUaD8k4tD0bMc
  &authorization_details=[{"type":"openid_credential","format":"jwt_vc_json","types":["VerifiableCredential","CertificateProfessionalCompetence"]}]
  &client_metadata={"authorization_endpoint":"https://client.example.com","response_types_supported":["vp_token","id_token"],"vp_formats_supported":{"jwt_vp":{"alg_values_supported":["ES256"]},"jwt_vc":{"alg_values_suppor["ES256"]}}}
```

### [3.4 Authorization response](#34-authorization-response)

The issuer then will respond with the following answer:

```http
https://client.example.com?
client_id=https%3A%2F%2Fissuer.eu%2Fauth&redirect_uri=https%3A%2F%2Fissuer.eu%2Fauth%2Fdirect_post
&response_type=vp_token
&response_mode=direct_post
&scope=openid
&state=92918a76-428b-4b60-bc1d-fd39cbec7cd7
&nonce=37e37fc43e5b1fd69cf8735f837a5e5c
&request_uri=https%3A%2F%2Fissuer.eu%2Fauth%2Frequest_uri%2F7440435569263425479
&request=eyJraWQiOiJkaWQ6ZWJzaTp6dFJvWXlKTmRHcjh0bUF0Vmg5Y2c5biIsInR5cCI6IkpXVCIsImFsZyI6IkVTMjU2In0.eyJpc3MiOiJkaWQ6ZWJzaTp6dFJvWXlKTmRHcjh0bUF0Vmg5Y2c5biIsInJlc3BvbnNlX3R5cGUiOiJ2cF90b2tlbiIsIm5vbmNlIjoiMzdlMzdmYzQzZTViMWZkNjljZjg3MzVmODM3YTVlNWMiLCJjbGllbnRfaWQiOiJodHRwczovL3RhZHBvbGUtaW50ZXJuYWwtbWFtbWFsLm5ncm9rLWZyZWUuYXBwL2F1dGgiLCJyZXNwb25zZV9tb2RlIjoiZGlyZWN0X3Bvc3QiLCJhdWQiOiJodHRwczovL3RhZHBvbGUtaW50ZXJuYWwtbWFtbWFsLm5ncm9rLWZyZWUuYXBwL2F1dGgiLCJzY29wZSI6Im9wZW5pZCIsInByZXNlbnRhdGlvbl9kZWZpbml0aW9uIjp7ImlkIjoiaG9sZGVyLXdhbGxldC1xdWFsaWZpY2F0aW9uLXByZXNlbnRhdGlvbiIsImZvcm1hdCI6eyJqd3RfdnBfanNvbiI6eyJhbGciOlsiRVMyNTYiXX0sImp3dF92cCI6eyJhbGciOlsiRVMyNTYiXX0sImp3dF92Y19qc29uIjp7ImFsZyI6WyJFUzI1NiJdfSwiand0X3ZjIjp7ImFsZyI6WyJFUzI1NiJdfX0sImlucHV0X2Rlc2NyaXB0b3JzIjpbeyJpZCI6Ijg5MTI3NDc0MTM4NjY0NTYyMzkiLCJuYW1lIjoiaG9sZGVyLXdhbGxldC1xdWFsaWZpY2F0aW9uLXByZXNlbnRhdGlvbiBvZiBWZXJpZmlhYmxlRWR1Y2F0aW9uYWxJRCIsInB1cnBvc2UiOiJUaGlzIGlzIGEgcHJlc2VudGF0aW9uIGRlZmluaXRpb24gZm9yIHRoZSBob2xkZXIgd2FsbGV0IHF1YWxpZmljYXRpb24iLCJmb3JtYXQiOnsiand0X3ZjIjp7ImFsZyI6WyJFUzI1NiJdfX0sImNvbnN0cmFpbnRzIjp7ImZpZWxkcyI6W3sicGF0aCI6WyIkLnZjLnR5cGUiXSwiZmlsdGVyIjp7InR5cGUiOiJhcnJheSIsImNvbnRhaW5zIjp7ImNvbnN0IjoiVmVyaWZpYWJsZUVkdWNhdGlvbmFsSUQifX19XX19XX0sInJlZGlyZWN0X3VyaSI6Imh0dHBzOi8vdGFkcG9sZS1pbnRlcm5hbC1tYW1tYWwubmdyb2stZnJlZS5hcHAvYXV0aC9kaXJlY3RfcG9zdCIsInN0YXRlIjoiOTI5MThhNzYtNDI4Yi00YjYwLWJjMWQtZmQzOWNiZWM3Y2Q3IiwiZXhwIjoxNzQxMDEyNTg0LCJpYXQiOjE3NDEwMTE5ODR9.bI0ajxVWWPFpy-Cp2YG9RytEhShqDjGbNi7T002fTKFaj8PQ1ESSLJdYsSRXIKFkfBB6BX-eOyj7BOG5xT6uFg
&presentation_definition=%7B%22id%22%3A%22holder-wallet-qualification-presentation%22%2C%22format%22%3A%7B%22jwt_vp_json%22%3A%7B%22alg%22%3A%5B%22ES256%22%5D%7D%2C%22jwt_vp%22%3A%7B%22alg%22%3A%5B%22ES256%22%5D%7D%2C%22jwt_vc_json%22%3A%7B%22alg%22%3A%5B%22ES256%22%5D%7D%2C%22jwt_vc%22%3A%7B%22alg%22%3A%5B%22ES256%22%5D%7D%7D%2C%22input_descriptors%22%3A%5B%7B%22id%22%3A%228912747413866456239%22%2C%22name%22%3A%22holder-wallet-qualification-presentation+of+VerifiableEducationalID%22%2C%22purpose%22%3A%22This+is+a+presentation+definition+for+the+holder+wallet+qualification%22%2C%22format%22%3A%7B%22jwt_vc%22%3A%7B%22alg%22%3A%5B%22ES256%22%5D%7D%7D%2C%22constraints%22%3A%7B%22fields%22%3A%5B%7B%22path%22%3A%5B%22%24.vc.type%22%5D%2C%22filter%22%3A%7B%22type%22%3A%22array%22%2C%22contains%22%3A%7B%22const%22%3A%22VerifiableEducationalID%22%7D%7D%7D%5D%7D%7D%5D%7D

```

After this the Mobile Wallet has all the details for presenting the PID associated to the student in order to authenticate the end user.

```http
POST https://issuer.eu/auth/direct_post
Content-Type: application/json

{
   "vp_token":"eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImRpZDprZXk6ejJkbXpEODFjZ1B4OFZraTdKYnV1TW1GWXJXUGdZb3l0eWtVWjNleXFodDFqOUticzVpc0Uyc0pjWk1oaFpyOUN4UHVBOVBqNXFQNk5uU0pmTVhnS3RQZWdNRG53eXc2ODh3QjJCc1VmazNnSlJBMnFnUWNVRGttVE5wRHJYNjhwRFlzZE1hS3EzV29Tc1JqdGN3WXBzYVh1MkVFVVdFTkZEMTMxZVdYc0VDN3F0cGRrZyN6MmRtekQ4MWNnUHg4VmtpN0pidXVNbUZZcldQZ1lveXR5a1VaM2V5cWh0MWo5S2JzNWlzRTJzSmNaTWhoWnI5Q3hQdUE5UGo1cVA2Tm5TSmZNWGdLdFBlZ01Ebnd5dzY4OHdCMkJzVWZrM2dKUkEycWdRY1VEa21UTnBEclg2OHBEWXNkTWFLcTNXb1NzUmp0Y3dZcHNhWHUyRUVVV0VORkQxMzFlV1hzRUM3cXRwZGtnIn0.eyJub25jZSI6IjM3ZTM3ZmM0M2U1YjFmZDY5Y2Y4NzM1ZjgzN2E1ZTVjIiwic3RhdGUiOiI5MjkxOGE3Ni00MjhiLTRiNjAtYmMxZC1mZDM5Y2JlYzdjZDciLCJ2cCI6eyJAY29udGV4dCI6WyJodHRwczovL3d3dy53My5vcmcvMjAxOC9jcmVkZW50aWFscy92MSJdLCJpZCI6InVybjp1dWlkOjVhM2EzYzNkLWM3NTQtNDkxYy1iOGYxLTg2OTgwY2Q2YTNlMSIsInR5cGUiOlsiVmVyaWZpYWJsZVByZXNlbnRhdGlvbiJdLCJob2xkZXIiOiJkaWQ6a2V5OnoyZG16RDgxY2dQeDhWa2k3SmJ1dU1tRllyV1BnWW95dHlrVVozZXlxaHQxajlLYnM1aXNFMnNKY1pNaGhacjlDeFB1QTlQajVxUDZOblNKZk1YZ0t0UGVnTURud3l3Njg4d0IyQnNVZmszZ0pSQTJxZ1FjVURrbVROcERyWDY4cERZc2RNYUtxM1dvU3NSanRjd1lwc2FYdTJFRVVXRU5GRDEzMWVXWHNFQzdxdHBka2ciLCJ2ZXJpZmlhYmxlQ3JlZGVudGlhbCI6WyJleUpyYVdRaU9pSmthV1E2WldKemFUcDZkRkp2V1hsS1RtUkhjamgwYlVGMFZtZzVZMmM1YmlJc0luUjVjQ0k2SWtwWFZDSXNJbUZzWnlJNklrVlRNalUySW4wLmV5SnpkV0lpT2lKa2FXUTZhMlY1T25veVpHMTZSRGd4WTJkUWVEaFdhMmszU21KMWRVMXRSbGx5VjFCbldXOTVkSGxyVlZvelpYbHhhSFF4YWpsTFluTTFhWE5GTW5OS1kxcE5hR2hhY2psRGVGQjFRVGxRYWpWeFVEWk9ibE5LWmsxWVowdDBVR1ZuVFVSdWQzbDNOamc0ZDBJeVFuTlZabXN6WjBwU1FUSnhaMUZqVlVScmJWUk9jRVJ5V0RZNGNFUlpjMlJOWVV0eE0xZHZVM05TYW5SamQxbHdjMkZZZFRKRlJWVlhSVTVHUkRFek1XVlhXSE5GUXpkeGRIQmthMmNpTENKdVltWWlPakUzTkRBMk5UWTJNREFzSW1semN5STZJbVJwWkRwbFluTnBPbnAwVW05WmVVcE9aRWR5T0hSdFFYUldhRGxqWnpsdUlpd2laWGh3SWpveE56Y3lNVEEyTWpBd0xDSnBZWFFpT2pFM05EQTJOVFkyTURBc0luWmpJanA3SWtCamIyNTBaWGgwSWpwYkltaDBkSEJ6T2k4dmQzZDNMbmN6TG05eVp5OHlNREU0TDJOeVpXUmxiblJwWVd4ekwzWXhJbDBzSW5SNWNHVWlPbHNpVm1WeWFXWnBZV0pzWlVOeVpXUmxiblJwWVd3aUxDSldaWEpwWm1saFlteGxSV1IxWTJGMGFXOXVZV3hKUkNKZExDSnBaQ0k2SW5aak9uVnpaV3htT21GblpXNTBJelEzTlRVM09UTXlOakExT1RZM01qSTBNallpTENKcGMzTjFaV1FpT2lJeU1ESTFMVEF5TFRJM1ZERXhPalF6T2pJd1dpSXNJblpoYkdsa1JuSnZiU0k2SWpJd01qVXRNREl0TWpkVU1URTZORE02TWpCYUlpd2lZM0psWkdWdWRHbGhiRk5qYUdWdFlTSTZleUpwWkNJNkltaDBkSEJ6T2k4dllYQnBMV052Ym1admNtMWhibU5sTG1WaWMya3VaWFV2ZEhKMWMzUmxaQzF6WTJobGJXRnpMWEpsWjJsemRISjVMM1l5TDNOamFHVnRZWE12ZWpOTloxVkdWV3RpTnpJeWRYRTBlRE5rZGpWNVFVcHRiazV0ZWtSR1pVczFWVU00ZURnelVXOWxURXBOSWl3aWRIbHdaU0k2SWtaMWJHeEtjMjl1VTJOb1pXMWhWbUZzYVdSaGRHOXlNakF5TVNKOUxDSjBaWEp0YzA5bVZYTmxJanA3SW1sa0lqb2lhSFIwY0hNNkx5OWhjR2t0Y0dsc2IzUXVaV0p6YVM1bGRTOTBjblZ6ZEdWa0xXbHpjM1ZsY25NdGNtVm5hWE4wY25rdmRqVXZhWE56ZFdWeWN5OWthV1E2WldKemFUcDZkRkp2V1hsS1RtUkhjamgwYlVGMFZtZzVZMmM1Ymk5aGRIUnlhV0oxZEdWekwyTTNZek01T0RSalltVmpOVE13WkRoa1lUa3pZakpqTlRZd1ptRTJPRGxtTmpNME1HUTVaalUyWXpnek9UWmtaVGxpWXpsalpUaGtZVEJoTmpBNU1tTWlMQ0owZVhCbElqb2lTWE56ZFdGdVkyVkRaWEowYVdacFkyRjBaU0o5TENKcGMzTjFaWElpT2lKa2FXUTZaV0p6YVRwNmRGSnZXWGxLVG1SSGNqaDBiVUYwVm1nNVkyYzViaUlzSW1semMzVmhibU5sUkdGMFpTSTZJakl3TWpVdE1ESXRNamRVTVRFNk5ETTZNakJhSWl3aVpYaHdhWEpoZEdsdmJrUmhkR1VpT2lJeU1ESTJMVEF5TFRJMlZERXhPalF6T2pJd1dpSXNJbU55WldSbGJuUnBZV3hUZFdKcVpXTjBJanA3SW1sa0lqb2laR2xrT210bGVUcDZNbVJ0ZWtRNE1XTm5VSGc0Vm10cE4wcGlkWFZOYlVaWmNsZFFaMWx2ZVhSNWExVmFNMlY1Y1doME1XbzVTMkp6TldselJUSnpTbU5hVFdob1duSTVRM2hRZFVFNVVHbzFjVkEyVG01VFNtWk5XR2RMZEZCbFowMUVibmQ1ZHpZNE9IZENNa0p6Vldack0yZEtVa0V5Y1dkUlkxVkVhMjFVVG5CRWNsZzJPSEJFV1hOa1RXRkxjVE5YYjFOelVtcDBZM2RaY0hOaFdIVXlSVVZWVjBWT1JrUXhNekZsVjFoelJVTTNjWFJ3Wkd0bklpd2lhV1JsYm5ScFptbGxjaUk2SWpFeU16UTFOamM0T1NJc0ltWmhiV2xzZVU1aGJXVWlPaUpFYjJVaUxDSm1hWEp6ZEU1aGJXVWlPaUpLYjJodUlpd2laR2x6Y0d4aGVVNWhiV1VpT2lKS2IyaHVJRVJ2WlNJc0ltUmhkR1ZQWmtKcGNuUm9Jam9pTVRrNU1DMHdNUzB3TVNJc0ltTnZiVzF2Yms1aGJXVWlPaUpLYjJodUlFUnZaU0lzSW0xaGFXd2lPaUpxYjJodUxtUnZaVUJsZUdGdGNHeGxMbU52YlNJc0ltVmtkVkJsY25OdmJsQnlhVzVqYVhCaGJFNWhiV1VpT2lJME5EUTBORFEwTkMxQlFIVnlkaTVqWVhRaUxDSmxaSFZRWlhKemIyNVFjbWx0WVhKNVFXWm1hV3hwWVhScGIyNGlPaUp6ZEhWa1pXNTBJaXdpWldSMVVHVnljMjl1VTJOdmNHVmtRV1ptYVd4cFlYUnBiMjRpT2lKYmMzUjFaR1Z1ZEVCMWNuWXVZMkYwWFNJc0ltVmtkVkJsY25OdmJrRnpjM1Z5WVc1alpTSTZJbHRvZEhSd2N6b3ZMM0psWm1Wa2N5NXZjbWN2WVhOemRYSmhibU5sTDBsQlVDOXNiM2RkSW4wc0ltTnlaV1JsYm5ScFlXeFRkR0YwZFhNaU9uc2lkSGx3WlNJNklsTjBZWFIxYzB4cGMzUXlNREl4Ulc1MGNua2lMQ0pwWkNJNkltaDBkSEJ6T2k4dmRHRmtjRzlzWlMxcGJuUmxjbTVoYkMxdFlXMXRZV3d1Ym1keWIyc3RabkpsWlM1aGNIQXZjM1JoZEhWekwzWXhJekVpTENKemRHRjBkWE5NYVhOMFNXNWtaWGdpT2lJeElpd2ljM1JoZEhWelRHbHpkRU55WldSbGJuUnBZV3dpT2lKb2RIUndjem92TDNSaFpIQnZiR1V0YVc1MFpYSnVZV3d0YldGdGJXRnNMbTVuY205ckxXWnlaV1V1WVhCd0wzTjBZWFIxY3k5Mk1TSXNJbk4wWVhSMWMxQjFjbkJ2YzJVaU9pSnlaWFp2WTJGMGFXOXVJbjE5TENKcWRHa2lPaUoyWXpwMWMyVnNaanBoWjJWdWRDTTBOelUxTnprek1qWXdOVGsyTnpJeU5ESTJJbjAubmx2bTl1d1hsTEZhODZKVmhFT3gzQ05vc1BXY0pmcnRlWEtIaHVpb3FFVnY3UXQwb09TTXhnVl9fMTAyby0wSzBKcGxxVVJNc1N2V3BRSDM5T3RDTlEiXX0sImlhdCI6MTc0MTAxMTk5MiwiaXNzIjoiZGlkOmtleTp6MmRtekQ4MWNnUHg4VmtpN0pidXVNbUZZcldQZ1lveXR5a1VaM2V5cWh0MWo5S2JzNWlzRTJzSmNaTWhoWnI5Q3hQdUE5UGo1cVA2Tm5TSmZNWGdLdFBlZ01Ebnd5dzY4OHdCMkJzVWZrM2dKUkEycWdRY1VEa21UTnBEclg2OHBEWXNkTWFLcTNXb1NzUmp0Y3dZcHNhWHUyRUVVV0VORkQxMzFlV1hzRUM3cXRwZGtnIiwic3ViIjoiZGlkOmtleTp6MmRtekQ4MWNnUHg4VmtpN0pidXVNbUZZcldQZ1lveXR5a1VaM2V5cWh0MWo5S2JzNWlzRTJzSmNaTWhoWnI5Q3hQdUE5UGo1cVA2Tm5TSmZNWGdLdFBlZ01Ebnd5dzY4OHdCMkJzVWZrM2dKUkEycWdRY1VEa21UTnBEclg2OHBEWXNkTWFLcTNXb1NzUmp0Y3dZcHNhWHUyRUVVV0VORkQxMzFlV1hzRUM3cXRwZGtnIiwiYXVkIjoiaHR0cHM6Ly90YWRwb2xlLWludGVybmFsLW1hbW1hbC5uZ3Jvay1mcmVlLmFwcC9hdXRoIiwibmJmIjoxNzQxMDExOTkyLCJleHAiOjE3NDEwMTI4OTJ9.VGcA23UeVVKW7YXdcjdGNbNdJXTE4M2TyfAWv9QNJUwHm0HkFhJPbrtAR7A4P_6zfLLDcHku-Nd3J-sRbWpfQA",
   "presentation_submission":"{\"id\":\"07375b93-f6f4-4f57-af1e-3e565b8a18cf\",\"definition_id\":\"holder-wallet-qualification-presentation\",\"descriptor_map\":[{\"id\":\"8912747413866456239\",\"path\":\"$\",\"format\":\"jwt_vp\",\"path_nested\":{\"id\":\"8912747413866456239\",\"format\":\"jwt_vc\",\"path\":\"$.vp.verifiableCredential[0]\"}}]}",
   "state":"92918a76-428b-4b60-bc1d-fd39cbec7cd7"
}
```

The issuer then must verify the verifiable presentation presented by the student and validate that the verifiable credential contained is valid and complies with all the trust model requirements. If the verifiable presentation complies with all the requirements the issuer will response will the following answer:

```http
https://client.example.com?code=7711230612178833271&state=92918a76-428b-4b60-bc1d-fd39cbec7cd7"
```

### [3.5 Token request](#35-token-request)

The following section describes the process for obtaining an access token, that can be used later on for authorize to the end user to perform subsequence operations

```http
POST https://issuer.eu/token
Content-Type: application/x-www-form-urlencoded

grant_type=authorization_code
&client_id=did:key:z2dmzD81cgPx8Vki7JbuuMmFYrWPgYoytykUZ3eyqht1j9Kbndi4FzE7bq9irPGQVyZG7SWHy8iqpKMjjhmtB7JF3eFYnM67SxNd4gjT3DsKUb7NKeKLcNTEocYUf2kpBQRQqCvGMCvC87F8jgydShFCPTwrDpvJKrZMdq8zjQLQxwW2kL
&redirect_uri=https://client.example.com
&code=7711230612178833271
&code_verifier=aJkAL61GwJ0tN~llJWnjVXbfvoBG5C~czfQU6RBQw1R0M02pa6iCUWDsbCCF.d3WKhGllsHW4dOQc~sgp4skFfsBsSNexhXb36q~_nstQMEL.KLomKLaEHYtECj11ixB
}
```

### [3.6 Token Response](#36-token-response)
  
The response from the issuer will have the following aspect:

```http
HTTP Response Payload: Content-Type application/json

{
   "access_token":"eyJraWQiOiJkaWQ6ZWJzaTp6dFJvWXlKTmRHcjh0bUF0Vmg5Y2c5biIsInR5cCI6IkpXVCIsImFsZyI6IkVTMjU2In0.eyJhdWQiOiJodHRwczovL3RhZHBvbGUtaW50ZXJuYWwtbWFtbWFsLm5ncm9rLWZyZWUuYXBwL2lzc3VlciIsInN1YiI6ImRpZDprZXk6ejJkbXpEODFjZ1B4OFZraTdKYnV1TW1GWXJXUGdZb3l0eWtVWjNleXFodDFqOUticzVpc0Uyc0pjWk1oaFpyOUN4UHVBOVBqNXFQNk5uU0pmTVhnS3RQZWdNRG53eXc2ODh3QjJCc1VmazNnSlJBMnFnUWNVRGttVE5wRHJYNjhwRFlzZE1hS3EzV29Tc1JqdGN3WXBzYVh1MkVFVVdFTkZEMTMxZVdYc0VDN3F0cGRrZyIsImlzcyI6Imh0dHBzOi8vdGFkcG9sZS1pbnRlcm5hbC1tYW1tYWwubmdyb2stZnJlZS5hcHAvYXV0aCIsImNsYWltcyI6eyJhdXRob3JpemF0aW9uRGV0YWlscyI6W3sidHlwZSI6Im9wZW5pZF9jcmVkZW50aWFsIiwiZm9ybWF0Ijoiand0X3ZjIiwibG9jYXRpb25zIjpbImh0dHBzOi8vdGFkcG9sZS1pbnRlcm5hbC1tYW1tYWwubmdyb2stZnJlZS5hcHAvaXNzdWVyIl0sInR5cGVzIjpbIlZlcmlmaWFibGVDcmVkZW50aWFsIiwiQ2VydGlmaWNhdGVQcm9mZXNzaW9uYWxDb21wZXRlbmNlIl0sImNyZWRlbnRpYWxDb25maWd1cmF0aW9uSWQiOm51bGwsImNyZWRlbnRpYWxEZWZpbml0aW9uIjpudWxsLCJ2Y3QiOm51bGx9XSwiY05vbmNlIjoiODQ1MDIwNjY4OTIxNDcxMjAxMCIsImNOb25jZUV4cGlyZXNJbiI6MTc0MTAxMjU5NDMzMSwiY2xpZW50SWQiOiJkaWQ6a2V5OnoyZG16RDgxY2dQeDhWa2k3SmJ1dU1tRllyV1BnWW95dHlrVVozZXlxaHQxajlLYnM1aXNFMnNKY1pNaGhacjlDeFB1QTlQajVxUDZOblNKZk1YZ0t0UGVnTURud3l3Njg4d0IyQnNVZmszZ0pSQTJxZ1FjVURrbVROcERyWDY4cERZc2RNYUtxM1dvU3NSanRjd1lwc2FYdTJFRVVXRU5GRDEzMWVXWHNFQzdxdHBka2ciLCJ1c2VySW5mbyI6eyJjb21tb25OYW1lIjoiSm9obiBEb2UiLCJkYXRlT2ZCaXJ0aCI6IjE5OTAtMDEtMDEiLCJkaXNwbGF5TmFtZSI6IkpvaG4gRG9lIiwiZWR1UGVyc29uQXNzdXJhbmNlIjoiW2h0dHBzOi8vcmVmZWRzLm9yZy9hc3N1cmFuY2UvSUFQL2xvd10iLCJlZHVQZXJzb25QcmltYXJ5QWZmaWxpYXRpb24iOiJzdHVkZW50IiwiZWR1UGVyc29uUHJpbmNpcGFsTmFtZSI6IjQ0NDQ0NDQ0LUFAdXJ2LmNhdCIsImVkdVBlcnNvblNjb3BlZEFmZmlsaWF0aW9uIjoiW3N0dWRlbnRAdXJ2LmNhdF0iLCJmYW1pbHlOYW1lIjoiRG9lIiwiZmlyc3ROYW1lIjoiSm9obiIsImlkIjoiZGlkOmtleTp6MmRtekQ4MWNnUHg4VmtpN0pidXVNbUZZcldQZ1lveXR5a1VaM2V5cWh0MWo5S2JzNWlzRTJzSmNaTWhoWnI5Q3hQdUE5UGo1cVA2Tm5TSmZNWGdLdFBlZ01Ebnd5dzY4OHdCMkJzVWZrM2dKUkEycWdRY1VEa21UTnBEclg2OHBEWXNkTWFLcTNXb1NzUmp0Y3dZcHNhWHUyRUVVV0VORkQxMzFlV1hzRUM3cXRwZGtnIiwiaWRlbnRpZmllciI6IjEyMzQ1Njc4OSIsIm1haWwiOiJqb2huLmRvZUBleGFtcGxlLmNvbSJ9fSwiZXhwIjoxNzQxMDEyNTk0LCJpYXQiOjE3NDEwMTE5OTQsIm5vbmNlIjoiODQ1MDIwNjY4OTIxNDcxMjAxMCJ9.ddt68cM78coeJwcgWeDm0-98J7NQtkzCvL-GqPqJbuRKDadIWbx4PXfPXgoVgWMJ-rJhiRY3bV8J0IBciIVdAQ",
   "id_token":"eyJraWQiOiJkaWQ6ZWJzaTp6dFJvWXlKTmRHcjh0bUF0Vmg5Y2c5biIsInR5cCI6IkpXVCIsImFsZyI6IkVTMjU2In0.eyJzdWIiOiJkaWQ6a2V5OnoyZG16RDgxY2dQeDhWa2k3SmJ1dU1tRllyV1BnWW95dHlrVVozZXlxaHQxajlLYnM1aXNFMnNKY1pNaGhacjlDeFB1QTlQajVxUDZOblNKZk1YZ0t0UGVnTURud3l3Njg4d0IyQnNVZmszZ0pSQTJxZ1FjVURrbVROcERyWDY4cERZc2RNYUtxM1dvU3NSanRjd1lwc2FYdTJFRVVXRU5GRDEzMWVXWHNFQzdxdHBka2ciLCJhdWQiOiJkaWQ6a2V5OnoyZG16RDgxY2dQeDhWa2k3SmJ1dU1tRllyV1BnWW95dHlrVVozZXlxaHQxajlLYnM1aXNFMnNKY1pNaGhacjlDeFB1QTlQajVxUDZOblNKZk1YZ0t0UGVnTURud3l3Njg4d0IyQnNVZmszZ0pSQTJxZ1FjVURrbVROcERyWDY4cERZc2RNYUtxM1dvU3NSanRjd1lwc2FYdTJFRVVXRU5GRDEzMWVXWHNFQzdxdHBka2ciLCJ1c2VyX2luZm8iOnsiY29tbW9uTmFtZSI6IkpvaG4gRG9lIiwiZGF0ZU9mQmlydGgiOiIxOTkwLTAxLTAxIiwiZGlzcGxheU5hbWUiOiJKb2huIERvZSIsImVkdVBlcnNvbkFzc3VyYW5jZSI6IltodHRwczovL3JlZmVkcy5vcmcvYXNzdXJhbmNlL0lBUC9sb3ddIiwiZWR1UGVyc29uUHJpbWFyeUFmZmlsaWF0aW9uIjoic3R1ZGVudCIsImVkdVBlcnNvblByaW5jaXBhbE5hbWUiOiI0NDQ0NDQ0NC1BQHVydi5jYXQiLCJlZHVQZXJzb25TY29wZWRBZmZpbGlhdGlvbiI6IltzdHVkZW50QHVydi5jYXRdIiwiZmFtaWx5TmFtZSI6IkRvZSIsImZpcnN0TmFtZSI6IkpvaG4iLCJpZCI6ImRpZDprZXk6ejJkbXpEODFjZ1B4OFZraTdKYnV1TW1GWXJXUGdZb3l0eWtVWjNleXFodDFqOUticzVpc0Uyc0pjWk1oaFpyOUN4UHVBOVBqNXFQNk5uU0pmTVhnS3RQZWdNRG53eXc2ODh3QjJCc1VmazNnSlJBMnFnUWNVRGttVE5wRHJYNjhwRFlzZE1hS3EzV29Tc1JqdGN3WXBzYVh1MkVFVVdFTkZEMTMxZVdYc0VDN3F0cGRrZyIsImlkZW50aWZpZXIiOiIxMjM0NTY3ODkiLCJtYWlsIjoiam9obi5kb2VAZXhhbXBsZS5jb20ifSwiaXNzIjoiaHR0cHM6Ly90YWRwb2xlLWludGVybmFsLW1hbW1hbC5uZ3Jvay1mcmVlLmFwcC9hdXRoIiwiZXhwIjoxNzQxMDEyNTk0LCJpYXQiOjE3NDEwMTE5OTQsIm5vbmNlIjoiODQ1MDIwNjY4OTIxNDcxMjAxMCJ9.1n7Oo77mPW5_4oXExLlIBybSYoIRdXBkWPlk3pnMpHOOqIPPCBZbRWj-k-_JwnIXJIuw2QVa0pKyM5fkqIf6-w",
   "token_type":"Bearer",
   "expires_in":1741012594331,
   "c_nonce":"8450206689214712010",
   "c_nonce_expires_in":1741012594331
}
```

### [3.7 Credential Request](#37-credential-request)

Once the access token has been obtained in the previous step, the end user can now request to obtain the issued verifiable credential. An example of this request is as follows:

```http
POST /credential
Content-Type: application/json
Authorization: Bearer eyJ0eXAi...

{
   "format":"jwt_vc",
   "types":[
      "VerifiableCredential",
      "CertificateProfessionalCompetence"
   ],
   "proof":{
      "proof_type":"jwt",
      "jwt":"eyJ0eXAiOiJvcGVuaWQ0dmNpLXByb29mK2p3dCIsImtpZCI6ImRpZDprZXk6ejJkbXpEODFjZ1B4OFZraTdKYnV1TW1GWXJXUGdZb3l0eWtVWjNleXFodDFqOUticzVpc0Uyc0pjWk1oaFpyOUN4UHVBOVBqNXFQNk5uU0pmTVhnS3RQZWdNRG53eXc2ODh3QjJCc1VmazNnSlJBMnFnUWNVRGttVE5wRHJYNjhwRFlzZE1hS3EzV29Tc1JqdGN3WXBzYVh1MkVFVVdFTkZEMTMxZVdYc0VDN3F0cGRrZyN6MmRtekQ4MWNnUHg4VmtpN0pidXVNbUZZcldQZ1lveXR5a1VaM2V5cWh0MWo5S2JzNWlzRTJzSmNaTWhoWnI5Q3hQdUE5UGo1cVA2Tm5TSmZNWGdLdFBlZ01Ebnd5dzY4OHdCMkJzVWZrM2dKUkEycWdRY1VEa21UTnBEclg2OHBEWXNkTWFLcTNXb1NzUmp0Y3dZcHNhWHUyRUVVV0VORkQxMzFlV1hzRUM3cXRwZGtnIiwiYWxnIjoiRVMyNTYifQ.eyJpYXQiOjE3NDEwMTE5OTQuMDY3LCJpc3MiOiJkaWQ6a2V5OnoyZG16RDgxY2dQeDhWa2k3SmJ1dU1tRllyV1BnWW95dHlrVVozZXlxaHQxajlLYnM1aXNFMnNKY1pNaGhacjlDeFB1QTlQajVxUDZOblNKZk1YZ0t0UGVnTURud3l3Njg4d0IyQnNVZmszZ0pSQTJxZ1FjVURrbVROcERyWDY4cERZc2RNYUtxM1dvU3NSanRjd1lwc2FYdTJFRVVXRU5GRDEzMWVXWHNFQzdxdHBka2ciLCJhdWQiOiJodHRwczovL3RhZHBvbGUtaW50ZXJuYWwtbWFtbWFsLm5ncm9rLWZyZWUuYXBwL2lzc3VlciIsImV4cCI6MTc0MTAxMjI5NCwibm9uY2UiOiI4NDUwMjA2Njg5MjE0NzEyMDEwIn0.SBGk5rshNgCMO49dNiSAxkMO-LVbP2aUWADFxclTzz8uDNvZAkqGAvKqFJGCyUvzA5u_pSZYnY6nODi6atOC6g"
   }
}
```

### [3.8 Credential Response](#38-credential-response)

Finally, the issuer response with the verifiable credential requested. An example of the response of the server is as follows:

```json
{
   "format":"jwt_vc",
   "credential":"eyJraWQiOiJkaWQ6ZWJzaTp6dFJvWXlKTmRHcjh0bUF0Vmg5Y2c5biIsInR5cCI6IkpXVCIsImFsZyI6IkVTMjU2In0.eyJzdWIiOiJkaWQ6a2V5OnoyZG16RDgxY2dQeDhWa2k3SmJ1dU1tRllyV1BnWW95dHlrVVozZXlxaHQxajlLYnM1aXNFMnNKY1pNaGhacjlDeFB1QTlQajVxUDZOblNKZk1YZ0t0UGVnTURud3l3Njg4d0IyQnNVZmszZ0pSQTJxZ1FjVURrbVROcERyWDY4cERZc2RNYUtxM1dvU3NSanRjd1lwc2FYdTJFRVVXRU5GRDEzMWVXWHNFQzdxdHBka2ciLCJuYmYiOjE3NDEwMTE5OTQsImlzcyI6ImRpZDplYnNpOnp0Um9ZeUpOZEdyOHRtQXRWaDljZzluIiwiZXhwIjoxNzcyNDYxNTk0LCJpYXQiOjE3NDEwMTE5OTQsInZjIjp7IkBjb250ZXh0IjpbImh0dHBzOi8vd3d3LnczLm9yZy8yMDE4L2NyZWRlbnRpYWxzL3YxIl0sInR5cGUiOlsiVmVyaWZpYWJsZUNyZWRlbnRpYWwiLCJDZXJ0aWZpY2F0ZVByb2Zlc3Npb25hbENvbXBldGVuY2UiXSwiaWQiOiJ2Yzp1c2VsZjphZ2VudCM2MTY3MjI0MjEzNzYwNDA5NTA0IiwiaXNzdWVkIjoiMjAyNS0wMy0wM1QxNDoyNjozNFoiLCJ2YWxpZEZyb20iOiIyMDI1LTAzLTAzVDE0OjI2OjM0WiIsImNyZWRlbnRpYWxTY2hlbWEiOnsiaWQiOiJodHRwczovL2FwaS1jb25mb3JtYW5jZS5lYnNpLmV1L3RydXN0ZWQtc2NoZW1hcy1yZWdpc3RyeS92Mi9zY2hlbWFzL3ozTWdVRlVrYjcyMnVxNHgzZHY1eUFKbW5ObXpERmVLNVVDOHg4M1FvZUxKTSIsInR5cGUiOiJGdWxsSnNvblNjaGVtYVZhbGlkYXRvcjIwMjEifSwidGVybXNPZlVzZSI6eyJpZCI6Imh0dHBzOi8vYXBpLXBpbG90LmVic2kuZXUvdHJ1c3RlZC1pc3N1ZXJzLXJlZ2lzdHJ5L3Y1L2lzc3VlcnMvZGlkOmVic2k6enRSb1l5Sk5kR3I4dG1BdFZoOWNnOW4vYXR0cmlidXRlcy9jN2MzOTg0Y2JlYzUzMGQ4ZGE5M2IyYzU2MGZhNjg5ZjYzNDBkOWY1NmM4Mzk2ZGU5YmM5Y2U4ZGEwYTYwOTJjIiwidHlwZSI6Iklzc3VhbmNlQ2VydGlmaWNhdGUifSwiaXNzdWVyIjoiZGlkOmVic2k6enRSb1l5Sk5kR3I4dG1BdFZoOWNnOW4iLCJpc3N1YW5jZURhdGUiOiIyMDI1LTAzLTAzVDE0OjI2OjM0WiIsImV4cGlyYXRpb25EYXRlIjoiMjAyNi0wMy0wMlQxNDoyNjozNFoiLCJjcmVkZW50aWFsU3ViamVjdCI6eyJpZCI6ImRpZDprZXk6ejJkbXpEODFjZ1B4OFZraTdKYnV1TW1GWXJXUGdZb3l0eWtVWjNleXFodDFqOUticzVpc0Uyc0pjWk1oaFpyOUN4UHVBOVBqNXFQNk5uU0pmTVhnS3RQZWdNRG53eXc2ODh3QjJCc1VmazNnSlJBMnFnUWNVRGttVE5wRHJYNjhwRFlzZE1hS3EzV29Tc1JqdGN3WXBzYVh1MkVFVVdFTkZEMTMxZVdYc0VDN3F0cGRrZyIsInBlcnNvbmFsX2FkbWluaXN0cmF0aXZlX251bWJlciI6IjEyMzQ1Njc4OSIsImdpdmVuX25hbWUiOiJKb2huIiwiZmFtaWx5X25hbWUiOiJEb2UiLCJpc19lbnRpdGxlZCI6InRydWUifSwiY3JlZGVudGlhbFN0YXR1cyI6eyJ0eXBlIjoiU3RhdHVzTGlzdDIwMjFFbnRyeSIsImlkIjoiaHR0cHM6Ly90YWRwb2xlLWludGVybmFsLW1hbW1hbC5uZ3Jvay1mcmVlLmFwcC9zdGF0dXMvdjEjMCIsInN0YXR1c0xpc3RJbmRleCI6IjAiLCJzdGF0dXNMaXN0Q3JlZGVudGlhbCI6Imh0dHBzOi8vdGFkcG9sZS1pbnRlcm5hbC1tYW1tYWwubmdyb2stZnJlZS5hcHAvc3RhdHVzL3YxIiwic3RhdHVzUHVycG9zZSI6InJldm9jYXRpb24ifX0sImp0aSI6InZjOnVzZWxmOmFnZW50IzYxNjcyMjQyMTM3NjA0MDk1MDQifQ.HSyd8NopKbBkI_moXJP0XZ1-RXseg-gpHcHlxI9T-i1EQi7NnW96rA-Ij7sxS7vHCKdhgJB0feWVh_Sq73fkaQ"
}
```

## [4 References](#4-references)

1. [OpenID for Verifiable Credential Issuance (VCI) Draft 11](https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0-11.html)
2. [The European Digital Identity Wallet Architecture and Reference Framework (v1.4.0)](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/releases/tag/v1.4.0)
3. [RFC 9101 OAuth 2.0 Authorization Framework: JWT-Secured Authorization Request (JAR)](https://www.rfc-editor.org/rfc/rfc9101.html#name-request-using-the-request_u)
4. [DIF Presentation Exchange](https://identity.foundation/presentation-exchange)
