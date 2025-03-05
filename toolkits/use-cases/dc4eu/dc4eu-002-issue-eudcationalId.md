# Issue a Verifiable Educational Id - v1.0

**Authors:**

* Angel Palomares (<angel.palomares@eviden.com>)

**Reviewers:**

* LLuis Ariño (lluisalfons.arino@urv.cat)

**Status:** Approved for v1.0

**Table of Contents:**

* [1 Summary](#1-summary)
* [2 Issue a Verifiable Educational Id Flow](#2-issue-a-verifiable-educational-id-flow)
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

This section defines in detail how to obtain a Verifiable Educational Id. This flow is based a No Authorize OpenID VCI flow, providing a Verifiable Presentation probing the possession of a PID.

## [2 Issue a Verifiable Educational Id Flow](#2-issue-a-verifiable-educational-id-flow)

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
  student->mobile: consent to send PID
  mobile-->mobile: redirect - http status = 302
  mobile->agent: POST http://uself-agent/direct_post
  activate agent
  note left of agent: sent the pid of the student to be verified
  agent->agent: verify PID VP

  

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
  agent->authSource: GET http://auth-source/educationalId/pid_identifier
  activate authSource 
  authSource->db: SELECT * FROM educationalId\n WHERE pid = pid_identifier
  activate db 
  db-->authSource: educationalId info
  deactivate db
  authSource-->agent: educationalId info
  deactivate authSource
  agent-->stdGUI: send event credential_issued
  agent-->mobile: credential
  deactivate agent
  deactivate mobile
  deactivate stdGUI

```

          Figure 1: No Authorize OpenID VCI Flow providing a PID Verifiable Presentation

## [3 Message Details](#3-message-details)

### [3.1 Initiate Credential Offer](#31-initiate-credential-offer)

Although the standard doesn't specify how to trigger the credential offer, we define the initialize of the credential offer following the suggestions proposed by EBSI.

```http
GET https://issuer.eu/issuer/initiate-credential-offer?
  &credential_type=VerifiableEducationalID
  &nonce=d527c191-6e1d-4c3d-9843-9eaf2005fba9
```

### [3.2 Credential Offer Response](#32-credential-offer-response)

In order to avoid overloading the result of the QRCode, the standard defines a entry point based on `credential_offer_uri`parameter:

```bash
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
            "VerifiableEducationalID"
         ],
         "trust_framework":{
            "name":"uSelf Agent Issuer",
            "type":"VerifiableEducationalID",
            "uri":"VerifiableEducationalID testing"
         },
         "display":[
            {
               "name":"VerifiableEducationalID",
               "description":"Schema of a Verifiable Educational ID for a natural person participating in the educational use cases"
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
            "identifier":{
               "display":[
                  {
                     "name":"identifier"
                  }
               ]
            },
            "schacPersonalUniqueCode":{
               "display":[
                  {
                     "name":"schacPersonalUniqueCode"
                  }
               ]
            },
            "schacPersonalUniqueID":{
               "display":[
                  {
                     "name":"schacPersonalUniqueID"
                  }
               ]
            },
            "schacHomeOrganization":{
               "display":[
                  {
                     "name":"schacHomeOrganization"
                  }
               ]
            },
            "familyName":{
               "display":[
                  {
                     "name":"familyName"
                  }
               ]
            },
            "firstName":{
               "display":[
                  {
                     "name":"firstName"
                  }
               ]
            },
            "displayName":{
               "display":[
                  {
                     "name":"displayName"
                  }
               ]
            },
            "dateOfBirth":{
               "display":[
                  {
                     "name":"dateOfBirth"
                  }
               ]
            },
            "commonName":{
               "display":[
                  {
                     "name":"commonName"
                  }
               ]
            },
            "mail":{
               "display":[
                  {
                     "name":"mail"
                  }
               ]
            },
            "eduPersonPrincipalName":{
               "display":[
                  {
                     "name":"eduPersonPrincipalName"
                  }
               ]
            },
            "eduPersonPrimaryAffiliation":{
               "display":[
                  {
                     "name":"eduPersonPrimaryAffiliation"
                  }
               ]
            },
            "eduPersonScopedAffiliation":{
               "display":[
                  {
                     "name":"eduPersonScopedAffiliation"
                  }
               ]
            },
            "eduPersonAssurance":{
               "display":[
                  {
                     "name":"eduPersonAssurance"
                  }
               ]
            },
            "image":{
               "display":[
                  {
                     "name":"image"
                  }
               ]
            }
         }
      }
   ],
   "grants":{
      "authorization_code":{
         "issuer_state":"eyJraWQiOiJkaWQ6ZWJzaTp6dFJvWXlKTmRHcjh0bUF0Vmg5Y2c5biIsInR5cCI6IkpXVCIsImFsZyI6IkVTMjU2In0.eyJhdWQiOiJodHRwczovL3RhZHBvbGUtaW50ZXJuYWwtbWFtbWFsLm5ncm9rLWZyZWUuYXBwL2F1dGgiLCJzdWIiOiIiLCJpc3MiOiJodHRwczovL3RhZHBvbGUtaW50ZXJuYWwtbWFtbWFsLm5ncm9rLWZyZWUuYXBwL2lzc3VlciIsImNyZWRlbnRpYWxfdHlwZXMiOlsiVmVyaWZpYWJsZUNyZWRlbnRpYWwiLCJWZXJpZmlhYmxlRWR1Y2F0aW9uYWxJRCJdLCJleHAiOjE3Mzg1ODA3NzMsImlhdCI6MTczODU3NzE3Mywibm9uY2UiOiI3OTQ5MzQ0MDU0NTM1ODU5MjYwIiwiY2xpZW50X2lkIjoiIn0.1V6rm18C6Lo8WflxnC_9DYUEvDTqI6uoVO2mYeHtAZHFZvE4rALSAZ7tFgoTP-tzi796if0QgXIdrdy4TSak9g"
      }
   }
}
```

### [3.3 Authorization request](#33-authorization-request)

Once the Mobile Wallet has read the credential offer, it will request an authorization with the following parameters:

```http
GET https://issuer.eu/auth/authorize?
  &client_id=did:key:z2dmzD81cg...
  &response_type=code
  &scope=openid
  &response_uri=https://client.example.com
  &response_mode=direct_post
  &state=8d8b6a3d-4bc0-4234-9a9a-ed1928815502
  &nonce=d527c191-6e1d-4c3d-9843-9eaf2005fba9
  &issuer_state=eyJraWQiOiJkaWQ6ZWJzaTp6dFJvWXlKTmRHcjh0bUF0Vmg5Y2c5biIsInR5cCI6IkpXVCIsImFsZyI6IkVTMjU2In0.eyJhdWQiOiJodHRwczovL3RhZHBvbGUtaW50ZXJuYWwtbWFtbWFsLm5ncm9rLWZyZWUuYXBwL2F1dGgiLCJzdWIiOiIiLCJpc3MiOiJodHRwczovL3RhZHBvbGUtaW50ZXJuYWwtbWFtbWFsLm5ncm9rLWZyZWUuYXBwL2lzc3VlciIsImNyZWRlbnRpYWxfdHlwZXMiOlsiVmVyaWZpYWJsZUNyZWRlbnRpYWwiLCJWZXJpZmlhYmxlRWR1Y2F0aW9uYWxJRCJdLCJleHAiOjE3Mzg1ODA3NzMsImlhdCI6MTczODU3NzE3Mywibm9uY2UiOiI3OTQ5MzQ0MDU0NTM1ODU5MjYwIiwiY2xpZW50X2lkIjoiIn0.1V6rm18C6Lo8WflxnC_9DYUEvDTqI6uoVO2mYeHtAZHFZvE4rALSAZ7tFgoTP-tzi796if0QgXIdrdy4TSak9g
  &code_challenge=wQ7kWVb4OwAxCtsMYALu9JXJjEujyZYUaD8k4tD0bMc
  &authorization_details=[{"type":"openid_credential","format":"jwt_vc_json","types":["VerifiableCredential","VerifiableEducationalID"]}]
  &client_metadata={"authorization_endpoint":"https://client.example.com","response_types_supported":["vp_token","id_token"],"vp_formats_supported":{"jwt_vp":{"alg_values_supported":["ES256"]},"jwt_vc":{"alg_values_suppor["ES256"]}}}
```

### [3.4 Authorization response](#34-authorization-response)

The issuer then will respond with the following answer:

```bash
https://client.example.com?
client_id=https%3A%2F%2Fussuer.eu%2Fauth&redirect_uri=https%3A%2F%2Fissuer.eu%2Fauth%2Fdirect_post
&response_type=vp_token
&response_mode=direct_post
&scope=openid
&state=8d8b6a3d-4bc0-4234-9a9a-ed1928815502
&nonce=d527c191-6e1d-4c3d-9843-9eaf2005fba9
&request_uri=https%3A%2F%2Fussuer.eu%2Fauth%2Frequest_uri%2F7598206819520970972
&request=eyJraWQiOiJkaWQ6ZWJzaTp6dFJvWXlKTmRHcjh0bUF0Vmg5Y2c5biIsInR5cCI6IkpXVCIsImFsZyI6IkVTMjU2In0.eyJpc3MiOiJkaWQ6ZWJzaTp6dFJvWXlKTmRHcjh0bUF0Vmg5Y2c5biIsInJlc3BvbnNlX3R5cGUiOiJ2cF90b2tlbiIsIm5vbmNlIjoiZ2xrRkZvaXNkZkV1aTQzMTIiLCJjbGllbnRfaWQiOiJodHRwczovL3RhZHBvbGUtaW50ZXJuYWwtbWFtbWFsLm5ncm9rLWZyZWUuYXBwL2F1dGgiLCJyZXNwb25zZV9tb2RlIjoiZGlyZWN0X3Bvc3QiLCJhdWQiOiJodHRwczovL3RhZHBvbGUtaW50ZXJuYWwtbWFtbWFsLm5ncm9rLWZyZWUuYXBwL2F1dGgiLCJzY29wZSI6Im9wZW5pZCIsInByZXNlbnRhdGlvbl9kZWZpbml0aW9uIjp7ImlkIjoiaG9sZGVyLXdhbGxldC1xdWFsaWZpY2F0aW9uLXByZXNlbnRhdGlvbiIsImZvcm1hdCI6eyJqd3RfdnBfanNvbiI6eyJhbGciOlsiRVMyNTYiXX0sImp3dF92cCI6eyJhbGciOlsiRVMyNTYiXX0sImp3dF92Y19qc29uIjp7ImFsZyI6WyJFUzI1NiJdfSwiand0X3ZjIjp7ImFsZyI6WyJFUzI1NiJdfX0sImlucHV0X2Rlc2NyaXB0b3JzIjpbeyJpZCI6IjUwMjAwOTI3NTkxNzQ3MzQ4NzYiLCJuYW1lIjoiaG9sZGVyLXdhbGxldC1xdWFsaWZpY2F0aW9uLXByZXNlbnRhdGlvbiBvZiBldS5ldXJvcGEuZWMuZXVkaS5waWQiLCJwdXJwb3NlIjoiVGhpcyBpcyBhIHByZXNlbnRhdGlvbiBkZWZpbml0aW9uIGZvciB0aGUgaG9sZGVyIHdhbGxldCBxdWFsaWZpY2F0aW9uIiwiZm9ybWF0Ijp7Imp3dF92YyI6eyJhbGciOlsiRVMyNTYiXX19LCJjb25zdHJhaW50cyI6eyJmaWVsZHMiOlt7InBhdGgiOlsiJC52Yy50eXBlIl0sImZpbHRlciI6eyJ0eXBlIjoiYXJyYXkiLCJjb250YWlucyI6eyJjb25zdCI6ImV1LmV1cm9wYS5lYy5ldWRpLnBpZCJ9fX1dfX1dfSwicmVkaXJlY3RfdXJpIjoiaHR0cHM6Ly90YWRwb2xlLWludGVybmFsLW1hbW1hbC5uZ3Jvay1mcmVlLmFwcC9hdXRoL2RpcmVjdF9wb3N0Iiwic3RhdGUiOiI5MmI2ZTA1Yy01YzNiLTQxOTQtYmJhOC0xZGExYjJhNWRkNjIiLCJleHAiOjE3Mzg1Nzc3ODQsImlhdCI6MTczODU3NzE4NH0.skDMvwDZ-4w-HZAP0aqEIBBGVRUMVlP7AhMrypA7s7WZHH22txLmMBXK93h0BtiAfyXBojjQXHWYkTvC9LboLw
&presentation_definition=%7B%22id%22%3A%22holder-wallet-qualification-presentation%22%2C%22format%22%3A%7B%22jwt_vp_json%22%3A%7B%22alg%22%3A%5B%22ES256%22%5D%7D%2C%22jwt_vp%22%3A%7B%22alg%22%3A%5B%22ES256%22%5D%7D%2C%22jwt_vc_json%22%3A%7B%22alg%22%3A%5B%22ES256%22%5D%7D%2C%22jwt_vc%22%3A%7B%22alg%22%3A%5B%22ES256%22%5D%7D%7D%2C%22input_descriptors%22%3A%5B%7B%22id%22%3A%225020092759174734876%22%2C%22name%22%3A%22holder-wallet-qualification-presentation+of+eu.europa.ec.eudi.pid%22%2C%22purpose%22%3A%22This+is+a+presentation+definition+for+the+holder+wallet+qualification%22%2C%22format%22%3A%7B%22jwt_vc%22%3A%7B%22alg%22%3A%5B%22ES256%22%5D%7D%7D%2C%22constraints%22%3A%7B%22fields%22%3A%5B%7B%22path%22%3A%5B%22%24.vc.type%22%5D%2C%22filter%22%3A%7B%22type%22%3A%22array%22%2C%22contains%22%3A%7B%22const%22%3A%22eu.europa.ec.eudi.pid%22%7D%7D%7D%5D%7D%7D%5D%7D

```

After this the Mobile Wallet has all the details for presenting the PID associated to the student in order to authenticate the end user.

```http
POST https://issuer.eu/auth/direct_post
Content-Type: application/json

{
   "vp_token":"eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJub25jZSI6Imdsa0ZGb2lzZGZFdWk0MzEyIiwic3RhdGUiOiI5MmI2ZTA1Yy01YzNiLTQxOTQtYmJhOC0xZGExYjJhNWRkNjIiLCJ2cCI6eyJAY29udGV4dCI6WyJodHRwczovL3d3dy53My5vcmcvMjAxOC9jcmVkZW50aWFscy92MSJdLCJpZCI6InVybjp1dWlkOjI5N2IyOWE5LTQ4NzItNDljZC1hNjczLWU3ZTJiMjM5YTlhNyIsInR5cGUiOlsiVmVyaWZpYWJsZVByZXNlbnRhdGlvbiJdLCJob2xkZXIiOiJkaWQ6a2V5OnoyZG16RDgxY2dQeDhWa2k3SmJ1dU1tRllyV1BnWW95dHlrVVozZXlxaHQxajlLYm5kaTRGekU3YnE5aXJQR1FWeVpHN1NXSHk4aXFwS01qamhtdEI3SkYzZUZZbk02N1N4TmQ0Z2pUM0RzS1ViN05LZUtMY05URW9jWVVmMmtwQlFSUXFDdkdNQ3ZDODdGOGpneWRTaEZDUFR3ckRwdkpLclpNZHE4empRTFF4d1cya0wiLCJ2ZXJpZmlhYmxlQ3JlZGVudGlhbCI6WyJleUpyYVdRaU9pSmthV1E2WldKemFUcDZkRkp2V1hsS1RtUkhjamgwYlVGMFZtZzVZMmM1YmlNMVJrNDFVV2RTTW1wUGR6ZFJSSEZ3WHpKSGMxSnNlbkJCUm1saU9Hd3pWVUV6TkdSR1NEZG5XVFJKSWl3aWRIbHdJam9pU2xkVUlpd2lZV3huSWpvaVJWTXlOVFlpZlEuZXlKemRXSWlPaUprYVdRNmEyVjVPbm95WkcxNlJEZ3hZMmRRZURoV2EyazNTbUoxZFUxdFJsbHlWMUJuV1c5NWRIbHJWVm96WlhseGFIUXhhamxMWW01a2FUUkdla1UzWW5FNWFYSlFSMUZXZVZwSE4xTlhTSGs0YVhGd1MwMXFhbWh0ZEVJM1NrWXpaVVpaYmswMk4xTjRUbVEwWjJwVU0wUnpTMVZpTjA1TFpVdE1ZMDVVUlc5aldWVm1NbXR3UWxGU1VYRkRka2ROUTNaRE9EZEdPR3BuZVdSVGFFWkRVRlIzY2tSd2RrcExjbHBOWkhFNGVtcFJURkY0ZDFjeWEwd2lMQ0p1WW1ZaU9qRTNNemcxTnpjd01qY3NJbWx6Y3lJNkltUnBaRHBsWW5OcE9ucDBVbTlaZVVwT1pFZHlPSFJ0UVhSV2FEbGpaemx1SWl3aVpYaHdJam94Tnpjd01ESTJOakkzTENKcFlYUWlPakUzTXpnMU56Y3dNamNzSW5aaklqcDdJa0JqYjI1MFpYaDBJanBiSW1oMGRIQnpPaTh2ZDNkM0xuY3pMbTl5Wnk4eU1ERTRMMk55WldSbGJuUnBZV3h6TDNZeElsMHNJblI1Y0dVaU9sc2lWbVZ5YVdacFlXSnNaVU55WldSbGJuUnBZV3dpTENKV1pYSnBabWxoWW14bFFYUjBaWE4wWVhScGIyNGlMQ0psZFM1bGRYSnZjR0V1WldNdVpYVmthUzV3YVdRaVhTd2lhV1FpT2lKMll6cDFjMlZzWmpwaFoyVnVkQ000TVRBd01qZ3hOemt3TURBeE16TXpOalV3SWl3aWFYTnpkV1ZrSWpvaU1qQXlOUzB3TWkwd00xUXhNRG93TXpvME4xb2lMQ0oyWVd4cFpFWnliMjBpT2lJeU1ESTFMVEF5TFRBelZERXdPakF6T2pRM1dpSXNJbU55WldSbGJuUnBZV3hUWTJobGJXRWlPbnNpYVdRaU9pSm9kSFJ3Y3pvdkwyRndhUzFqYjI1bWIzSnRZVzVqWlM1bFluTnBMbVYxTDNSeWRYTjBaV1F0YzJOb1pXMWhjeTF5WldkcGMzUnllUzkyTWk5elkyaGxiV0Z6TDNvelRXZFZSbFZyWWpjeU1uVnhOSGd6WkhZMWVVRktiVzVPYlhwRVJtVkxOVlZET0hnNE0xRnZaVXhLVFNJc0luUjVjR1VpT2lKR2RXeHNTbk52YmxOamFHVnRZVlpoYkdsa1lYUnZjakl3TWpFaWZTd2lkR1Z5YlhOUFpsVnpaU0k2ZXlKcFpDSTZJbWgwZEhCek9pOHZZWEJwTFhCcGJHOTBMbVZpYzJrdVpYVXZkSEoxYzNSbFpDMXBjM04xWlhKekxYSmxaMmx6ZEhKNUwzWTFMMmx6YzNWbGNuTXZaR2xrT21WaWMyazZlblJTYjFsNVNrNWtSM0k0ZEcxQmRGWm9PV05uT1c0dllYUjBjbWxpZFhSbGN5OWpOMk16T1RnMFkySmxZelV6TUdRNFpHRTVNMkl5WXpVMk1HWmhOamc1WmpZek5EQmtPV1kxTm1NNE16azJaR1U1WW1NNVkyVTRaR0V3WVRZd09USmpJaXdpZEhsd1pTSTZJa2x6YzNWaGJtTmxRMlZ5ZEdsbWFXTmhkR1VpZlN3aWFYTnpkV1Z5SWpvaVpHbGtPbVZpYzJrNmVuUlNiMWw1U2s1a1IzSTRkRzFCZEZab09XTm5PVzRpTENKcGMzTjFZVzVqWlVSaGRHVWlPaUl5TURJMUxUQXlMVEF6VkRFd09qQXpPalEzV2lJc0ltVjRjR2x5WVhScGIyNUVZWFJsSWpvaU1qQXlOaTB3TWkwd01sUXhNRG93TXpvME4xb2lMQ0pqY21Wa1pXNTBhV0ZzVTNWaWFtVmpkQ0k2ZXlKcFpDSTZJbVJwWkRwclpYazZlakprYlhwRU9ERmpaMUI0T0ZacmFUZEtZblYxVFcxR1dYSlhVR2RaYjNsMGVXdFZXak5sZVhGb2RERnFPVXRpYm1ScE5FWjZSVGRpY1RscGNsQkhVVlo1V2tjM1UxZEllVGhwY1hCTFRXcHFhRzEwUWpkS1JqTmxSbGx1VFRZM1UzaE9aRFJuYWxRelJITkxWV0kzVGt0bFMweGpUbFJGYjJOWlZXWXlhM0JDVVZKUmNVTjJSMDFEZGtNNE4wWTRhbWQ1WkZOb1JrTlFWSGR5UkhCMlNrdHlXazFrY1RoNmFsRk1VWGgzVnpKclRDSXNJbVJ2WTNWdFpXNTBYMjUxYldKbGNpSTZJakV5TXpRMU5qYzRPU0lzSW1kcGRtVnVYMjVoYldVaU9pSktiMmh1SWl3aVptRnRhV3g1WDI1aGJXVWlPaUpFYjJVaUxDSmlhWEowYUY5a1lYUmxJam9pTVRrNU1DMHdNUzB3TVNJc0ltRm5aVjl2ZG1WeVh6RTRJam9pZEhKMVpTSjlMQ0pqY21Wa1pXNTBhV0ZzVTNSaGRIVnpJanA3SW5SNWNHVWlPaUpUZEdGMGRYTk1hWE4wTWpBeU1VVnVkSEo1SWl3aWFXUWlPaUpvZEhSd2N6b3ZMM1JoWkhCdmJHVXRhVzUwWlhKdVlXd3RiV0Z0YldGc0xtNW5jbTlyTFdaeVpXVXVZWEJ3TDNOMFlYUjFjeTkyTVNNd0lpd2ljM1JoZEhWelRHbHpkRWx1WkdWNElqb2lNQ0lzSW5OMFlYUjFjMHhwYzNSRGNtVmtaVzUwYVdGc0lqb2lhSFIwY0hNNkx5OTBZV1J3YjJ4bExXbHVkR1Z5Ym1Gc0xXMWhiVzFoYkM1dVozSnZheTFtY21WbExtRndjQzl6ZEdGMGRYTXZkakVpTENKemRHRjBkWE5RZFhKd2IzTmxJam9pY21WMmIyTmhkR2x2YmlKOWZTd2lhblJwSWpvaWRtTTZkWE5sYkdZNllXZGxiblFqT0RFd01ESTRNVGM1TURBd01UTXpNelkxTUNKOS42Y2hDcFplV3E5RTZ2dmt1RDh0SUNfcWJnWHo4M3psWFF3SEtTbmFlV29EQjdCb1NaQzVoSW1FYXZPdUp1a2hBS3hhRXVKY3lhNDR0dFQ4eXUwSk5SUSJdfSwiaWF0IjoxNzM4NTc3MTkwLCJpc3MiOiJodHRwczovL3RhZHBvbGUtaW50ZXJuYWwtbWFtbWFsLm5ncm9rLWZyZWUuYXBwL2F1dGgiLCJzdWIiOiJodHRwczovL3RhZHBvbGUtaW50ZXJuYWwtbWFtbWFsLm5ncm9rLWZyZWUuYXBwL2F1dGgiLCJhdWQiOiJodHRwczovL3RhZHBvbGUtaW50ZXJuYWwtbWFtbWFsLm5ncm9rLWZyZWUuYXBwL2F1dGgiLCJuYmYiOjE3Mzg1NzcxOTAsImV4cCI6MTczODU3ODA5MH0.nyvMtelcVT_OIG5M0o9_MMZlaEEAV0dsgDqrtWu0GNTD_6NXgHUXZRxYVkE6Z7vimxWIWh00eoISXLrHGPl0JA",
   "presentation_submission":"{\"id\":\"9a402f43-53a5-4599-a2e3-dc9b2d5deff0\",\"definition_id\":\"holder-wallet-qualification-presentation\",\"descriptor_map\":[{\"id\":\"5020092759174734876\",\"path\":\"$\",\"format\":\"jwt_vp\",\"path_nested\":{\"id\":\"5020092759174734876\",\"format\":\"jwt_vc\",\"path\":\"$.vp.verifiableCredential[0]\"}}]}",
   "state":"92b6e05c-5c3b-4194-bba8-1da1b2a5dd62"
}
```

The issuer then must verify the verifiable presentation presented by the student and validate that the verifiable credential contained is valid and complies with all the trust model requirements. If the verifiable presentation complies with all the requirements the issuer will response will the following answer:

```bash
https://client.example.com?code=glkFFoisdfEui4312&state=92b6e05c-5c3b-4194-bba8-1da1b2a5dd62
```

### [3.5 Token request](#35-token-request)

The following section describes the process for obtaining an access token, that can be used later on for authorize to the end user to perform subsequence operations

```http
POST https://issuer.eu/token
Content-Type: application/x-www-form-urlencoded

&grant_type=authorization_code
&client_id=did:key:z2dmzD81cgPx8Vki7JbuuMmFYrWPgYoytykUZ3eyqht1j9Kbndi4FzE7bq9irPGQVyZG7SWHy8iqpKMjjhmtB7JF3eFYnM67SxNd4gjT3DsKUb7NKeKLcNTEocYUf2kpBQRQqCvGMCvC87F8jgydShFCPTwrDpvJKrZMdq8zjQLQxwW2kL
&redirect_uri=https://client.example.com
&code=glkFFoisdfEui4312
&code_verifier=FF4uUpKOK7LkTEvwMM9O~qf4.NL1._~p6QrEnngvT0kne_tbUw17NYUGFexiNbN0Wecp2cOuIkMal8EbXxS4rQ5PQe7Ou1EvHoqLr8obdJeeUcjM8bRDZTVIIkgXTEzT
```

### [3.6 Token Response](#36-token-response)
  
The response from the issuer will have the following aspect:

```http
{
   "access_token":"eyJraWQiOiJkaWQ6ZWJzaTp6dFJvWXlKTmRHcjh0bUF0Vmg5Y2c5biIsInR5cCI6IkpXVCIsImFsZyI6IkVTMjU2In0.eyJhdWQiOiJodHRwczovL3RhZHBvbGUtaW50ZXJuYWwtbWFtbWFsLm5ncm9rLWZyZWUuYXBwL2lzc3VlciIsInN1YiI6ImRpZDprZXk6ejJkbXpEODFjZ1B4OFZraTdKYnV1TW1GWXJXUGdZb3l0eWtVWjNleXFodDFqOUtibmRpNEZ6RTdicTlpclBHUVZ5Wkc3U1dIeThpcXBLTWpqaG10QjdKRjNlRlluTTY3U3hOZDRnalQzRHNLVWI3TktlS0xjTlRFb2NZVWYya3BCUVJRcUN2R01DdkM4N0Y4amd5ZFNoRkNQVHdyRHB2SktyWk1kcTh6alFMUXh3VzJrTCIsImlzcyI6Imh0dHBzOi8vdGFkcG9sZS1pbnRlcm5hbC1tYW1tYWwubmdyb2stZnJlZS5hcHAvYXV0aCIsImNsYWltcyI6eyJhdXRob3JpemF0aW9uRGV0YWlscyI6W3sidHlwZSI6Im9wZW5pZF9jcmVkZW50aWFsIiwiZm9ybWF0Ijoiand0X3ZjIiwibG9jYXRpb25zIjpbImh0dHBzOi8vdGFkcG9sZS1pbnRlcm5hbC1tYW1tYWwubmdyb2stZnJlZS5hcHAvaXNzdWVyIl0sInR5cGVzIjpbIlZlcmlmaWFibGVDcmVkZW50aWFsIiwiVmVyaWZpYWJsZUVkdWNhdGlvbmFsSUQiXSwiY3JlZGVudGlhbENvbmZpZ3VyYXRpb25JZCI6bnVsbCwiY3JlZGVudGlhbERlZmluaXRpb24iOm51bGwsInZjdCI6bnVsbH1dLCJjTm9uY2UiOiJnbGtGRm9pc2RmRXVpNDMxMiIsImNOb25jZUV4cGlyZXNJbiI6MTczODU3Nzc5MDgyMiwiY2xpZW50SWQiOiJkaWQ6a2V5OnoyZG16RDgxY2dQeDhWa2k3SmJ1dU1tRllyV1BnWW95dHlrVVozZXlxaHQxajlLYm5kaTRGekU3YnE5aXJQR1FWeVpHN1NXSHk4aXFwS01qamhtdEI3SkYzZUZZbk02N1N4TmQ0Z2pUM0RzS1ViN05LZUtMY05URW9jWVVmMmtwQlFSUXFDdkdNQ3ZDODdGOGpneWRTaEZDUFR3ckRwdkpLclpNZHE4empRTFF4d1cya0wifSwiZXhwIjoxNzM4NTc3NzkwLCJpYXQiOjE3Mzg1NzcxOTAsIm5vbmNlIjoiZ2xrRkZvaXNkZkV1aTQzMTIifQ.2aR_d9W2yMN20LEG9j7tvvqnYtx2VsZjbXvmk9nl_GzH7bCadiLmaGm4gR1C2PYT7wYgJXYYNJVe_CFYKOkeHA",
   "id_token":"eyJraWQiOiJkaWQ6ZWJzaTp6dFJvWXlKTmRHcjh0bUF0Vmg5Y2c5biIsInR5cCI6IkpXVCIsImFsZyI6IkVTMjU2In0.eyJzdWIiOiJkaWQ6a2V5OnoyZG16RDgxY2dQeDhWa2k3SmJ1dU1tRllyV1BnWW95dHlrVVozZXlxaHQxajlLYm5kaTRGekU3YnE5aXJQR1FWeVpHN1NXSHk4aXFwS01qamhtdEI3SkYzZUZZbk02N1N4TmQ0Z2pUM0RzS1ViN05LZUtMY05URW9jWVVmMmtwQlFSUXFDdkdNQ3ZDODdGOGpneWRTaEZDUFR3ckRwdkpLclpNZHE4empRTFF4d1cya0wiLCJhdWQiOiJkaWQ6a2V5OnoyZG16RDgxY2dQeDhWa2k3SmJ1dU1tRllyV1BnWW95dHlrVVozZXlxaHQxajlLYm5kaTRGekU3YnE5aXJQR1FWeVpHN1NXSHk4aXFwS01qamhtdEI3SkYzZUZZbk02N1N4TmQ0Z2pUM0RzS1ViN05LZUtMY05URW9jWVVmMmtwQlFSUXFDdkdNQ3ZDODdGOGpneWRTaEZDUFR3ckRwdkpLclpNZHE4empRTFF4d1cya0wiLCJpc3MiOiJodHRwczovL3RhZHBvbGUtaW50ZXJuYWwtbWFtbWFsLm5ncm9rLWZyZWUuYXBwL2F1dGgiLCJleHAiOjE3Mzg1Nzc3OTAsImlhdCI6MTczODU3NzE5MCwibm9uY2UiOiJnbGtGRm9pc2RmRXVpNDMxMiJ9.xrMJ_vYVsdOJEhTCLIeGA08TuKrthnE4XCZcnF13rPr2FRJYmR4SNR--wvsnqVNCVCP9h38Gvt8MVUyQ9tpWlQ",
   "token_type":"Bearer",
   "expires_in":1738577790822,
   "c_nonce":"glkFFoisdfEui4312",
   "c_nonce_expires_in":1738577790822
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
      "VerifiableEducationalID"
   ],
   "proof":{
      "proof_type":"jwt",
      "jwt":"eyJ0eXAiOiJvcGVuaWQ0dmNpLXByb29mK2p3dCIsImtpZCI6ImRpZDprZXk6ejJkbXpEODFjZ1B4OFZraTdKYnV1TW1GWXJXUGdZb3l0eWtVWjNleXFodDFqOUtibmRpNEZ6RTdicTlpclBHUVZ5Wkc3U1dIeThpcXBLTWpqaG10QjdKRjNlRlluTTY3U3hOZDRnalQzRHNLVWI3TktlS0xjTlRFb2NZVWYya3BCUVJRcUN2R01DdkM4N0Y4amd5ZFNoRkNQVHdyRHB2SktyWk1kcTh6alFMUXh3VzJrTCN6MmRtekQ4MWNnUHg4VmtpN0pidXVNbUZZcldQZ1lveXR5a1VaM2V5cWh0MWo5S2JuZGk0RnpFN2JxOWlyUEdRVnlaRzdTV0h5OGlxcEtNampobXRCN0pGM2VGWW5NNjdTeE5kNGdqVDNEc0tVYjdOS2VLTGNOVEVvY1lVZjJrcEJRUlFxQ3ZHTUN2Qzg3RjhqZ3lkU2hGQ1BUd3JEcHZKS3JaTWRxOHpqUUxReHdXMmtMIiwiYWxnIjoiRVMyNTYifQ.eyJpYXQiOjE3Mzg1NzcxOTEuOTYsImlzcyI6ImRpZDprZXk6ejJkbXpEODFjZ1B4OFZraTdKYnV1TW1GWXJXUGdZb3l0eWtVWjNleXFodDFqOUtibmRpNEZ6RTdicTlpclBHUVZ5Wkc3U1dIeThpcXBLTWpqaG10QjdKRjNlRlluTTY3U3hOZDRnalQzRHNLVWI3TktlS0xjTlRFb2NZVWYya3BCUVJRcUN2R01DdkM4N0Y4amd5ZFNoRkNQVHdyRHB2SktyWk1kcTh6alFMUXh3VzJrTCIsImF1ZCI6Imh0dHBzOi8vdGFkcG9sZS1pbnRlcm5hbC1tYW1tYWwubmdyb2stZnJlZS5hcHAvaXNzdWVyIiwiZXhwIjoxNzM4NTc3NDkxLCJub25jZSI6Imdsa0ZGb2lzZGZFdWk0MzEyIn0.l5Bg8OHvFhiS-BykNoivLmOOzxNZHk99tDELPpWpUcE1nhV4wl6Avtuf0kpCM15jv1ocvZyvdySromHzryk0Zw"
   }
}
```

### [3.8 Credential Response](#38-credential-response)

Finally, the issuer response with the verifiable credential requested. An example of the response of the server is as follows:

```json
{
   "format":"jwt_vc",
   "credential":"eyJraWQiOiJkaWQ6ZWJzaTp6dFJvWXlKTmRHcjh0bUF0Vmg5Y2c5biM1Rk41UWdSMmpPdzdRRHFwXzJHc1JsenBBRmliOGwzVUEzNGRGSDdnWTRJIiwidHlwIjoiSldUIiwiYWxnIjoiRVMyNTYifQ.eyJzdWIiOiJkaWQ6a2V5OnoyZG16RDgxY2dQeDhWa2k3SmJ1dU1tRllyV1BnWW95dHlrVVozZXlxaHQxajlLYm5kaTRGekU3YnE5aXJQR1FWeVpHN1NXSHk4aXFwS01qamhtdEI3SkYzZUZZbk02N1N4TmQ0Z2pUM0RzS1ViN05LZUtMY05URW9jWVVmMmtwQlFSUXFDdkdNQ3ZDODdGOGpneWRTaEZDUFR3ckRwdkpLclpNZHE4empRTFF4d1cya0wiLCJuYmYiOjE3Mzg1NzcxOTEsImlzcyI6ImRpZDplYnNpOnp0Um9ZeUpOZEdyOHRtQXRWaDljZzluIiwiZXhwIjoxNzcwMDI2NzkxLCJpYXQiOjE3Mzg1NzcxOTEsInZjIjp7IkBjb250ZXh0IjpbImh0dHBzOi8vd3d3LnczLm9yZy8yMDE4L2NyZWRlbnRpYWxzL3YxIl0sInR5cGUiOlsiVmVyaWZpYWJsZUNyZWRlbnRpYWwiLCJWZXJpZmlhYmxlRWR1Y2F0aW9uYWxJRCJdLCJpZCI6InZjOnVzZWxmOmFnZW50Izc4Mjg5NDg1NTYxMTcwODk3ODciLCJpc3N1ZWQiOiIyMDI1LTAyLTAzVDEwOjA2OjMxWiIsInZhbGlkRnJvbSI6IjIwMjUtMDItMDNUMTA6MDY6MzFaIiwiY3JlZGVudGlhbFNjaGVtYSI6eyJpZCI6Imh0dHBzOi8vYXBpLWNvbmZvcm1hbmNlLmVic2kuZXUvdHJ1c3RlZC1zY2hlbWFzLXJlZ2lzdHJ5L3YyL3NjaGVtYXMvejNNZ1VGVWtiNzIydXE0eDNkdjV5QUptbk5tekRGZUs1VUM4eDgzUW9lTEpNIiwidHlwZSI6IkZ1bGxKc29uU2NoZW1hVmFsaWRhdG9yMjAyMSJ9LCJ0ZXJtc09mVXNlIjp7ImlkIjoiaHR0cHM6Ly9hcGktcGlsb3QuZWJzaS5ldS90cnVzdGVkLWlzc3VlcnMtcmVnaXN0cnkvdjUvaXNzdWVycy9kaWQ6ZWJzaTp6dFJvWXlKTmRHcjh0bUF0Vmg5Y2c5bi9hdHRyaWJ1dGVzL2M3YzM5ODRjYmVjNTMwZDhkYTkzYjJjNTYwZmE2ODlmNjM0MGQ5ZjU2YzgzOTZkZTliYzljZThkYTBhNjA5MmMiLCJ0eXBlIjoiSXNzdWFuY2VDZXJ0aWZpY2F0ZSJ9LCJpc3N1ZXIiOiJkaWQ6ZWJzaTp6dFJvWXlKTmRHcjh0bUF0Vmg5Y2c5biIsImlzc3VhbmNlRGF0ZSI6IjIwMjUtMDItMDNUMTA6MDY6MzFaIiwiZXhwaXJhdGlvbkRhdGUiOiIyMDI2LTAyLTAyVDEwOjA2OjMxWiIsImNyZWRlbnRpYWxTdWJqZWN0Ijp7ImlkIjoiZGlkOmtleTp6MmRtekQ4MWNnUHg4VmtpN0pidXVNbUZZcldQZ1lveXR5a1VaM2V5cWh0MWo5S2JuZGk0RnpFN2JxOWlyUEdRVnlaRzdTV0h5OGlxcEtNampobXRCN0pGM2VGWW5NNjdTeE5kNGdqVDNEc0tVYjdOS2VLTGNOVEVvY1lVZjJrcEJRUlFxQ3ZHTUN2Qzg3RjhqZ3lkU2hGQ1BUd3JEcHZKS3JaTWRxOHpqUUxReHdXMmtMIiwiaWRlbnRpZmllciI6IjEyMzQ1Njc4OSIsImZhbWlseU5hbWUiOiJEb2UiLCJmaXJzdE5hbWUiOiJKb2huIiwiZGlzcGxheU5hbWUiOiJKb2huIERvZSIsImRhdGVPZkJpcnRoIjoiMTk5MC0wMS0wMSIsImNvbW1vbk5hbWUiOiJKb2huIERvZSIsIm1haWwiOiJqb2huLmRvZUBleGFtcGxlLmNvbSIsImVkdVBlcnNvblByaW5jaXBhbE5hbWUiOiI0NDQ0NDQ0NC1BQHVydi5jYXQiLCJlZHVQZXJzb25QcmltYXJ5QWZmaWxpYXRpb24iOiJzdHVkZW50IiwiZWR1UGVyc29uU2NvcGVkQWZmaWxpYXRpb24iOiJbc3R1ZGVudEB1cnYuY2F0XSIsImVkdVBlcnNvbkFzc3VyYW5jZSI6IltodHRwczovL3JlZmVkcy5vcmcvYXNzdXJhbmNlL0lBUC9sb3ddIn0sImNyZWRlbnRpYWxTdGF0dXMiOnsidHlwZSI6IlN0YXR1c0xpc3QyMDIxRW50cnkiLCJpZCI6Imh0dHBzOi8vdGFkcG9sZS1pbnRlcm5hbC1tYW1tYWwubmdyb2stZnJlZS5hcHAvc3RhdHVzL3YxIzAiLCJzdGF0dXNMaXN0SW5kZXgiOiIwIiwic3RhdHVzTGlzdENyZWRlbnRpYWwiOiJodHRwczovL3RhZHBvbGUtaW50ZXJuYWwtbWFtbWFsLm5ncm9rLWZyZWUuYXBwL3N0YXR1cy92MSIsInN0YXR1c1B1cnBvc2UiOiJyZXZvY2F0aW9uIn19LCJqdGkiOiJ2Yzp1c2VsZjphZ2VudCM3ODI4OTQ4NTU2MTE3MDg5Nzg3In0.Pf5pAPzHoTwIT6S-yRpSI5_fthJ_dBen5O7LXYbF3s7uRzCQPo2OlnMFcvOHNv5tYupDVZBjuuD64M8_cTa3FA"
}
```

## [4 References](#4-references)

1. [OpenID for Verifiable Credential Issuance (VCI) Draft 11](https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0-11.html)
2. [The European Digital Identity Wallet Architecture and Reference Framework (v1.4.0)](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/releases/tag/v1.4.0)
3. [RFC 9101 OAuth 2.0 Authorization Framework: JWT-Secured Authorization Request (JAR)](https://www.rfc-editor.org/rfc/rfc9101.html#name-request-using-the-request_u)
4. [DIF Presentation Exchange](https://identity.foundation/presentation-exchange)
