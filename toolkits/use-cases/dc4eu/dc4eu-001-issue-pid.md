# Issue PID v1.0

**Authors:**

* Angel Palomares (<angel.palomares@eviden.com>)

**Reviewers:**

* LLuis Ariño ()


**Status:** Approved for v1.0

**Table of Contents:**

* [1 Summary](#1-summary)
* [2 Issue PID](#2-issue-pid)
* [3 Message Details](#3-message-details)
  * [3.1 Initiate Credential Offer](#31-initiate-credential-offer)
  * [3.2 Credential Offer Response](#32-credential-offer-response)
  * [3.3 Token request](#33-token-request)
  * [3.4 Token Response](#34-token-response)
  * [3.5 Credential Request](#35-credential-request)
  * [3.6 Credential Response](#36-credential-response)
* [4 References](#4-references)

## [1 Summary](#1-summary)

As one of the pre-requisites for obtaining a verifiable credential from the University it will be necessary to obtain a PID. This section describes how an student can obtain a PID.

## [2 Issue PID](#2-issue-pid)

Figure 1 shows how an student obtains a PID following a Pre Authorize flow:

``` mermaid
  sequenceDiagram
    autonumber
    actor student as Student
    participant mobile as Mobile Wallet
    participant pidGUI as uSelf PID Generator
    participant agent as uSelf Issuer Agent
    participant authSource as Authentic Source
    participant db as Postgres DB
    participant ip as Identity Provider
    

Note over student,ip: Pre Authentication/Authorization
    student->pidGUI: GET http://student-web/issue
    activate pidGUI 
    pidGUI->ip: GET http://identity-provider/authorize
    activate ip 
    ip-->pidGUI: student authenticated
    deactivate ip
  

Note over student,ip: Issuing PID 
    pidGUI->agent: GET http://uself-agent/issuer/crendential-offer
    activate agent 
    agent-->pidGUI: credential_offer
    deactivate agent
    pidGUI->pidGUI: generate QRCode
    mobile->pidGUI: read QRCode & user_pin
    
    activate mobile 
    mobile-->mobile: redirect - http status = 302

    
   
    mobile->agent:**GET** http://uself-agent/auth/token?user_pin
    activate agent 
    agent-->mobile: access_token
    deactivate agent
    mobile->agent:**POST** http://uself-agent/issuer/credential
    activate agent 
    agent->authSource:**GET** http://auth-source/educationalId/pid_identifier
    activate authSource 
    authSource->db: SELECT * FROM educationalId\n WHERE pid = pid_identifier
    activate db 
    db-->authSource: educationalId info
    deactivate db
    authSource-->agent: educationalId info
    deactivate authSource
    agent-->pidGUI: send event credential_issued
    agent-->student: credential
    deactivate agent
    deactivate mobile
    deactivate pidGUI
```

          Figure 1: Verification Flow with a Relaying Party with a Front End and a Back End

## [3 Message Details](#3-message-details)

### [3.1 Initiate Credential Offer](#31-initiate-credential-offer)

Although the standard doesn't specify how to trigger the credential offer, we define the initialize of the credential offer following the suggestions proposed by EBSI.

```http
GET https://issuer.eu/issuer/initiate-credential-offer?
  credential_type=VerifiableCredentialDiploma
  &bearer_token=Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJib3pCbU1NRGR6YVZRVDEyekQtYmJ2aEczWTZOdUNWdGN0Vi01WDdwNmFVIn0.eyJleHAiOjE3Mzg1NzE5NTAsImlhdCI6MTczODU3MTY1MCwiYXV0aF90aW1lIjoxNzM4NTY4NTI5LCJqdGkiOiJjNDEzYjU1MS05ZjQ4LTRiOTUtYTkwNS1lZjJiMTliZjk4MjEiLCJpc3MiOiJodHRwOi8vdXNlbGYta2V5Y2xvYWsubG9jYWwvcmVhbG1zL3VzZWxmLXJlYWxtIiwiYXVkIjoiYWNjb3VudCIsInN1YiI6ImQ1ODRjY2U2LTZhMGYtNDVlZi05ODYxLTRhMWFiY2E4MTE2YyIsInR5cCI6IkJlYXJlciIsImF6cCI6InVzZWxmLWlzc3Vlci1ndWkiLCJub25jZSI6IlRXUjJXR2x5ZEZCMlNVOUdXVzFVVW1SNGNtUi1VMzVWZUd4RE0wWkhiVzFHVEVkblIzSlBkVWMxVWw5RiIsInNlc3Npb25fc3RhdGUiOiI1NWU3Nzk4My00MWU5LTRmYTktODQzYy03ZDA0N2E5N2I4MTciLCJhY3IiOiIxIiwiYWxsb3dlZC1vcmlnaW5zIjpbImh0dHA6Ly91c2VsZi1pc3N1ZXItZ3VpLmxvY2FsIl0sInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIiwiZGVmYXVsdC1yb2xlcy11c2VsZi1yZWFsbSJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJzaWQiOiI1NWU3Nzk4My00MWU5LTRmYTktODQzYy03ZDA0N2E5N2I4MTciLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZG9jdW1lbnRfbnVtYmVyIjoiMTIzNDU2Nzg5IiwibmFtZSI6InVzZWxmIGFkbWluIiwicHJlZmVycmVkX3VzZXJuYW1lIjoidXNlbGYtYWRtaW4iLCJnaXZlbl9uYW1lIjoidXNlbGYiLCJmYW1pbHlfbmFtZSI6ImFkbWluIiwiZW1haWwiOiJhZG1pbkB0ZXN0LmNvbSJ9.C-DHYpncTu4e4xgQ_wROXzn01AXfr4nhe1x-iUT5KJZ5rQKiQY_DwXg2Oew_IaOeuSjeKqA3Juqu18J1VUq6cr5AeDlEl9SOl8yXz0ok2uzvYXtvKTCvxNhIOzoe4faDHAnJUdDorSX76CfnEPZIjgiC2TgqW0t94TQp0C94zVVCN8dFoFiRy0-YyiygHpGIG8Cyurnjp3T0tgrRhiZ7OZzj58yTCiwc-wEIPZ7ytf1bBK4jx-OAYUHJMXqQEbBf3XhKKeyqOn32K-MZ2EYBsEjsmaIme1gmbf2w3djlccB6VDzsQ2cic4JfRDEFVrMz_LrUtzUznNLz47M49FO92w
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
            "VerifiableAttestation",
            "eu.europa.ec.eudi.pid"
         ],

         "display":[
            {
               "name":"eu.europa.ec.eudi.pid",
               "description":"eu.europa.ec.eudi.pid for DC4EU Project"
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
            "document_number":{
               "display":[
                  {
                     "name":"document_number"
                  }
               ]
            },
            "given_name":{
               "display":[
                  {
                     "name":"given_name"
                  }
               ]
            },
            "family_name":{
               "display":[
                  {
                     "name":"family_name"
                  }
               ]
            },
            "birth_date":{
               "display":[
                  {
                     "name":"birth_date"
                  }
               ]
            },
            "age_over_18":{
               "display":[
                  {
                     "name":"age_over_18"
                  }
               ]
            }
         }
      }
   ],
   "grants":{
      "urn:ietf:params:oauth:grant-type:pre-authorized_code":{
         "pre-authorized_code":"eyJraWQiOiJkaWQ6ZWJzaTp6dFJvWXlKTmRHcjh0bUF0Vmg5Y2c5biIsInR5cCI6IkpXVCIsImFsZyI6IkVTMjU2In0.eyJhdWQiOiJodHRwczovL3RhZHBvbGUtaW50ZXJuYWwtbWFtbWFsLm5ncm9rLWZyZWUuYXBwL2F1dGgiLCJzdWIiOiIiLCJhdXRob3JpemF0aW9uX2RldGFpbHMiOnsiZm9ybWF0Ijoiand0X3ZjIiwidHlwZXMiOlsiVmVyaWZpYWJsZUNyZWRlbnRpYWwiLCJWZXJpZmlhYmxlQXR0ZXN0YXRpb24iLCJldS5ldXJvcGEuZWMuZXVkaS5waWQiXSwidHJ1c3RGcmFtZXdvcmsiOnsibmFtZSI6InVTZWxmIEFnZW50IElzc3VlciIsInR5cGUiOiJldS5ldXJvcGEuZWMuZXVkaS5waWQiLCJ1cmkiOiJldS5ldXJvcGEuZWMuZXVkaS5waWQgdGVzdGluZyJ9LCJzY29wZSI6bnVsbCwiY3J5cHRvZ3JhcGhpY0JpbmRpbmdNZXRob2RzU3VwcG9ydGVkIjpudWxsLCJjcmVkZW50aWFsU2lnbmluZ0FsZ1ZhbHVlc1N1cHBvcnRlZCI6bnVsbCwiZGlzcGxheSI6W3sibmFtZSI6ImV1LmV1cm9wYS5lYy5ldWRpLnBpZCIsImxvY2FsZSI6ImVuLUdCIiwibG9nbyI6bnVsbCwiZGVzY3JpcHRpb24iOiJldS5ldXJvcGEuZWMuZXVkaS5waWQgZm9yIERDNEVVIFByb2plY3QiLCJiYWNrZ3JvdW5kQ29sb3IiOm51bGwsImJhY2tncm91bmRJbWFnZSI6bnVsbCwidGV4dENvbG9yIjpudWxsfV0sImNyZWRlbnRpYWxTdWJqZWN0Ijp7ImlkIjp7Im1hbmRhdG9yeSI6ZmFsc2UsInZhbHVlVHlwZSI6bnVsbCwiZGlzcGxheSI6W3sibmFtZSI6ImlkIiwibG9jYWxlIjoiZW4tR0IiLCJsb2dvIjpudWxsLCJkZXNjcmlwdGlvbiI6bnVsbCwiYmFja2dyb3VuZENvbG9yIjpudWxsLCJiYWNrZ3JvdW5kSW1hZ2UiOm51bGwsInRleHRDb2xvciI6bnVsbH1dfSwiZG9jdW1lbnRfbnVtYmVyIjp7Im1hbmRhdG9yeSI6ZmFsc2UsInZhbHVlVHlwZSI6bnVsbCwiZGlzcGxheSI6W3sibmFtZSI6ImRvY3VtZW50X251bWJlciIsImxvY2FsZSI6ImVuLUdCIiwibG9nbyI6bnVsbCwiZGVzY3JpcHRpb24iOm51bGwsImJhY2tncm91bmRDb2xvciI6bnVsbCwiYmFja2dyb3VuZEltYWdlIjpudWxsLCJ0ZXh0Q29sb3IiOm51bGx9XX0sImdpdmVuX25hbWUiOnsibWFuZGF0b3J5IjpmYWxzZSwidmFsdWVUeXBlIjpudWxsLCJkaXNwbGF5IjpbeyJuYW1lIjoiZ2l2ZW5fbmFtZSIsImxvY2FsZSI6ImVuLUdCIiwibG9nbyI6bnVsbCwiZGVzY3JpcHRpb24iOm51bGwsImJhY2tncm91bmRDb2xvciI6bnVsbCwiYmFja2dyb3VuZEltYWdlIjpudWxsLCJ0ZXh0Q29sb3IiOm51bGx9XX0sImZhbWlseV9uYW1lIjp7Im1hbmRhdG9yeSI6ZmFsc2UsInZhbHVlVHlwZSI6bnVsbCwiZGlzcGxheSI6W3sibmFtZSI6ImZhbWlseV9uYW1lIiwibG9jYWxlIjoiZW4tR0IiLCJsb2dvIjpudWxsLCJkZXNjcmlwdGlvbiI6bnVsbCwiYmFja2dyb3VuZENvbG9yIjpudWxsLCJiYWNrZ3JvdW5kSW1hZ2UiOm51bGwsInRleHRDb2xvciI6bnVsbH1dfSwiYmlydGhfZGF0ZSI6eyJtYW5kYXRvcnkiOmZhbHNlLCJ2YWx1ZVR5cGUiOm51bGwsImRpc3BsYXkiOlt7Im5hbWUiOiJiaXJ0aF9kYXRlIiwibG9jYWxlIjoiZW4tR0IiLCJsb2dvIjpudWxsLCJkZXNjcmlwdGlvbiI6bnVsbCwiYmFja2dyb3VuZENvbG9yIjpudWxsLCJiYWNrZ3JvdW5kSW1hZ2UiOm51bGwsInRleHRDb2xvciI6bnVsbH1dfSwiYWdlX292ZXJfMTgiOnsibWFuZGF0b3J5IjpmYWxzZSwidmFsdWVUeXBlIjpudWxsLCJkaXNwbGF5IjpbeyJuYW1lIjoiYWdlX292ZXJfMTgiLCJsb2NhbGUiOiJlbi1HQiIsImxvZ28iOm51bGwsImRlc2NyaXB0aW9uIjpudWxsLCJiYWNrZ3JvdW5kQ29sb3IiOm51bGwsImJhY2tncm91bmRJbWFnZSI6bnVsbCwidGV4dENvbG9yIjpudWxsfV19fSwiY3JlZGVudGlhbERlZmluaXRpb24iOm51bGwsInZjdCI6bnVsbCwiY2xhaW1zIjpudWxsLCJvcmRlciI6bnVsbH0sImlzcyI6Imh0dHBzOi8vdGFkcG9sZS1pbnRlcm5hbC1tYW1tYWwubmdyb2stZnJlZS5hcHAvaXNzdWVyIiwiZXhwIjoxNzM4NTgwNjEyLCJpYXQiOjE3Mzg1NzcwMTIsIm5vbmNlIjoiNzQ1NDI4MTQ1Njg4ODY0NjUzNSIsImNsaWVudF9pZCI6IiJ9.qXeHCeAnGRTaCBL0hj2D4EITZVeuhNBgFrr5pz2ZJHhy4O01tQ8x7lyBrkRon3gQb0rFgjzBgn5WPn3_eu5OmQ",
         "user_pin_required":true
      }
   }
}
```

Where the `issuer_state` or `pre_authorized_code` parameters, depending on the flow, will be required later on during the issue process.


### [3.3 Token request](#33-token-request)

The following section describes the process for obtaining an access token, that can be used later on for authorize to the end user to perform subsequence operations

```http
POST https://issuer.eu/token
Content-Type: application/x-www-form-urlencoded

grant_type=urn:ietf:params:oauth:grant-type:pre-authorized_code
&redirect_uri=https://client.example.com
&pre_authorized_code=eyJraWQiOiJkaWQ6ZWJzaTp6dFJvWXlKTmRHcjh0bUF0Vmg5Y2c5biIsInR5cCI6IkpXVCIsImFsZyI6IkVTMjU2In0.eyJhdWQiOiJodHRwczovL3RhZHBvbGUtaW50ZXJuYWwtbWFtbWFsLm5ncm9rLWZyZWUuYXBwL2F1dGgiLCJzdWIiOiIiLCJhdXRob3JpemF0aW9uX2RldGFpbHMiOnsiZm9ybWF0Ijoiand0X3ZjIiwidHlwZXMiOlsiVmVyaWZpYWJsZUNyZWRlbnRpYWwiLCJWZXJpZmlhYmxlQXR0ZXN0YXRpb24iLCJldS5ldXJvcGEuZWMuZXVkaS5waWQiXSwidHJ1c3RGcmFtZXdvcmsiOnsibmFtZSI6InVTZWxmIEFnZW50IElzc3VlciIsInR5cGUiOiJldS5ldXJvcGEuZWMuZXVkaS5waWQiLCJ1cmkiOiJldS5ldXJvcGEuZWMuZXVkaS5waWQgdGVzdGluZyJ9LCJzY29wZSI6bnVsbCwiY3J5cHRvZ3JhcGhpY0JpbmRpbmdNZXRob2RzU3VwcG9ydGVkIjpudWxsLCJjcmVkZW50aWFsU2lnbmluZ0FsZ1ZhbHVlc1N1cHBvcnRlZCI6bnVsbCwiZGlzcGxheSI6W3sibmFtZSI6ImV1LmV1cm9wYS5lYy5ldWRpLnBpZCIsImxvY2FsZSI6ImVuLUdCIiwibG9nbyI6bnVsbCwiZGVzY3JpcHRpb24iOiJldS5ldXJvcGEuZWMuZXVkaS5waWQgZm9yIERDNEVVIFByb2plY3QiLCJiYWNrZ3JvdW5kQ29sb3IiOm51bGwsImJhY2tncm91bmRJbWFnZSI6bnVsbCwidGV4dENvbG9yIjpudWxsfV0sImNyZWRlbnRpYWxTdWJqZWN0Ijp7ImlkIjp7Im1hbmRhdG9yeSI6ZmFsc2UsInZhbHVlVHlwZSI6bnVsbCwiZGlzcGxheSI6W3sibmFtZSI6ImlkIiwibG9jYWxlIjoiZW4tR0IiLCJsb2dvIjpudWxsLCJkZXNjcmlwdGlvbiI6bnVsbCwiYmFja2dyb3VuZENvbG9yIjpudWxsLCJiYWNrZ3JvdW5kSW1hZ2UiOm51bGwsInRleHRDb2xvciI6bnVsbH1dfSwiZG9jdW1lbnRfbnVtYmVyIjp7Im1hbmRhdG9yeSI6ZmFsc2UsInZhbHVlVHlwZSI6bnVsbCwiZGlzcGxheSI6W3sibmFtZSI6ImRvY3VtZW50X251bWJlciIsImxvY2FsZSI6ImVuLUdCIiwibG9nbyI6bnVsbCwiZGVzY3JpcHRpb24iOm51bGwsImJhY2tncm91bmRDb2xvciI6bnVsbCwiYmFja2dyb3VuZEltYWdlIjpudWxsLCJ0ZXh0Q29sb3IiOm51bGx9XX0sImdpdmVuX25hbWUiOnsibWFuZGF0b3J5IjpmYWxzZSwidmFsdWVUeXBlIjpudWxsLCJkaXNwbGF5IjpbeyJuYW1lIjoiZ2l2ZW5fbmFtZSIsImxvY2FsZSI6ImVuLUdCIiwibG9nbyI6bnVsbCwiZGVzY3JpcHRpb24iOm51bGwsImJhY2tncm91bmRDb2xvciI6bnVsbCwiYmFja2dyb3VuZEltYWdlIjpudWxsLCJ0ZXh0Q29sb3IiOm51bGx9XX0sImZhbWlseV9uYW1lIjp7Im1hbmRhdG9yeSI6ZmFsc2UsInZhbHVlVHlwZSI6bnVsbCwiZGlzcGxheSI6W3sibmFtZSI6ImZhbWlseV9uYW1lIiwibG9jYWxlIjoiZW4tR0IiLCJsb2dvIjpudWxsLCJkZXNjcmlwdGlvbiI6bnVsbCwiYmFja2dyb3VuZENvbG9yIjpudWxsLCJiYWNrZ3JvdW5kSW1hZ2UiOm51bGwsInRleHRDb2xvciI6bnVsbH1dfSwiYmlydGhfZGF0ZSI6eyJtYW5kYXRvcnkiOmZhbHNlLCJ2YWx1ZVR5cGUiOm51bGwsImRpc3BsYXkiOlt7Im5hbWUiOiJiaXJ0aF9kYXRlIiwibG9jYWxlIjoiZW4tR0IiLCJsb2dvIjpudWxsLCJkZXNjcmlwdGlvbiI6bnVsbCwiYmFja2dyb3VuZENvbG9yIjpudWxsLCJiYWNrZ3JvdW5kSW1hZ2UiOm51bGwsInRleHRDb2xvciI6bnVsbH1dfSwiYWdlX292ZXJfMTgiOnsibWFuZGF0b3J5IjpmYWxzZSwidmFsdWVUeXBlIjpudWxsLCJkaXNwbGF5IjpbeyJuYW1lIjoiYWdlX292ZXJfMTgiLCJsb2NhbGUiOiJlbi1HQiIsImxvZ28iOm51bGwsImRlc2NyaXB0aW9uIjpudWxsLCJiYWNrZ3JvdW5kQ29sb3IiOm51bGwsImJhY2tncm91bmRJbWFnZSI6bnVsbCwidGV4dENvbG9yIjpudWxsfV19fSwiY3JlZGVudGlhbERlZmluaXRpb24iOm51bGwsInZjdCI6bnVsbCwiY2xhaW1zIjpudWxsLCJvcmRlciI6bnVsbH0sImlzcyI6Imh0dHBzOi8vdGFkcG9sZS1pbnRlcm5hbC1tYW1tYWwubmdyb2stZnJlZS5hcHAvaXNzdWVyIiwiZXhwIjoxNzM4NTgwNjEyLCJpYXQiOjE3Mzg1NzcwMTIsIm5vbmNlIjoiNzQ1NDI4MTQ1Njg4ODY0NjUzNSIsImNsaWVudF9pZCI6IiJ9.qXeHCeAnGRTaCBL0hj2D4EITZVeuhNBgFrr5pz2ZJHhy4O01tQ8x7lyBrkRon3gQb0rFgjzBgn5WPn3_eu5OmQ
&user_pin=1234
}
```

### [3.4 Token Response](#34-token-response)
  
The response from the issuer will have the following aspect:

```http
HTTP Response Payload: Content-Type application/json
{
   "access_token":"eyJraWQiOiJkaWQ6ZWJzaTp6dFJvWXlKTmRHcjh0bUF0Vmg5Y2c5biIsInR5cCI6IkpXVCIsImFsZyI6IkVTMjU2In0.eyJhdWQiOiJodHRwczovL3RhZHBvbGUtaW50ZXJuYWwtbWFtbWFsLm5ncm9rLWZyZWUuYXBwL2lzc3VlciIsInN1YiI6ImRpZDplYnNpOnp0Um9ZeUpOZEdyOHRtQXRWaDljZzluIiwiaXNzIjoiaHR0cHM6Ly90YWRwb2xlLWludGVybmFsLW1hbW1hbC5uZ3Jvay1mcmVlLmFwcC9hdXRoIiwiY2xhaW1zIjp7ImNOb25jZSI6IjgyNzgxOTczMzA3NjE2MDUwNTkiLCJjTm9uY2VFeHBpcmVzSW4iOjE3Mzg1Nzc2MjIyMTksImNsaWVudElkIjoiZGlkOmVic2k6enRSb1l5Sk5kR3I4dG1BdFZoOWNnOW4ifSwiZXhwIjoxNzM4NTc3NjIyLCJpYXQiOjE3Mzg1NzcwMjIsIm5vbmNlIjoiODI3ODE5NzMzMDc2MTYwNTA1OSJ9.HDEhSlzz24OlyxdGm-0IGX3dOL1wyKDRdPsv84mJMytZg7NZN2a7mJhLNodVExU66d8zCfEoMlHtw6uMd4cJ1g",
   "id_token":"eyJraWQiOiJkaWQ6ZWJzaTp6dFJvWXlKTmRHcjh0bUF0Vmg5Y2c5biIsInR5cCI6IkpXVCIsImFsZyI6IkVTMjU2In0.eyJzdWIiOiJkaWQ6ZWJzaTp6dFJvWXlKTmRHcjh0bUF0Vmg5Y2c5biIsImF1ZCI6ImRpZDplYnNpOnp0Um9ZeUpOZEdyOHRtQXRWaDljZzluIiwiaXNzIjoiaHR0cHM6Ly90YWRwb2xlLWludGVybmFsLW1hbW1hbC5uZ3Jvay1mcmVlLmFwcC9hdXRoIiwiZXhwIjoxNzM4NTc3NjIyLCJpYXQiOjE3Mzg1NzcwMjIsIm5vbmNlIjoiODI3ODE5NzMzMDc2MTYwNTA1OSJ9.ei_lEkDGLisMEOLu1s88XusNP6bAJg9moaSD0rCbLUbRXJD_J9zQ2akEe3PNoBw9TJdZ197VanWvFsSsPoPBTA",
   "token_type":"Bearer",
   "expires_in":1711532112851,
   "c_nonce":"d527c191-6e1d-4c3d-9843-9eaf2005fba9",
   "c_nonce_expires_in":1711532112851
}
```

### [3.5 Credential Request](#35-credential-request)

Once the access token has been obtained in the previous step, the end user can now request to obtain the issued verifiable credential. An example of this request is as follows:

```http
POST /credential
Content-Type: application/json
Authorization: Bearer eyJ0eXAi...

{
   "format":"jwt_vc",
   "types":[
      "VerifiableCredential","VerifiableAttestation","eu.europa.ec.eudi.pid"
   ],
   "proof":{
      "proof_type":"jwt",
      "jwt":"eyJ0eXAiOiJvcGVuaWQ0dmNpLXByb29mK2p3dCIsImtpZCI6ImRpZDprZXk6ejJkbXpEODFjZ1B4OFZraTdKYnV1TW1GWXJXUGdZb3l0eWtVWjNleXFodDFqOUtibmRpNEZ6RTdicTlpclBHUVZ5Wkc3U1dIeThpcXBLTWpqaG10QjdKRjNlRlluTTY3U3hOZDRnalQzRHNLVWI3TktlS0xjTlRFb2NZVWYya3BCUVJRcUN2R01DdkM4N0Y4amd5ZFNoRkNQVHdyRHB2SktyWk1kcTh6alFMUXh3VzJrTCN6MmRtekQ4MWNnUHg4VmtpN0pidXVNbUZZcldQZ1lveXR5a1VaM2V5cWh0MWo5S2JuZGk0RnpFN2JxOWlyUEdRVnlaRzdTV0h5OGlxcEtNampobXRCN0pGM2VGWW5NNjdTeE5kNGdqVDNEc0tVYjdOS2VLTGNOVEVvY1lVZjJrcEJRUlFxQ3ZHTUN2Qzg3RjhqZ3lkU2hGQ1BUd3JEcHZKS3JaTWRxOHpqUUxReHdXMmtMIiwiYWxnIjoiRVMyNTYifQ.eyJpYXQiOjE3Mzg1NzcwMjguMzg2LCJpc3MiOiJkaWQ6a2V5OnoyZG16RDgxY2dQeDhWa2k3SmJ1dU1tRllyV1BnWW95dHlrVVozZXlxaHQxajlLYm5kaTRGekU3YnE5aXJQR1FWeVpHN1NXSHk4aXFwS01qamhtdEI3SkYzZUZZbk02N1N4TmQ0Z2pUM0RzS1ViN05LZUtMY05URW9jWVVmMmtwQlFSUXFDdkdNQ3ZDODdGOGpneWRTaEZDUFR3ckRwdkpLclpNZHE4empRTFF4d1cya0wiLCJhdWQiOiJodHRwczovL3RhZHBvbGUtaW50ZXJuYWwtbWFtbWFsLm5ncm9rLWZyZWUuYXBwL2lzc3VlciIsImV4cCI6MTczODU3NzMyOCwibm9uY2UiOiI4Mjc4MTk3MzMwNzYxNjA1MDU5In0.1pK5ilDx20z0CE7ylygYtDatIU6HWJ7BXCerBZTOgiAtXw6XwovkWz99WjLvoGsa5mNj9j_NnoVMHHUzyo0Qag"
   }
}
```

### [3.6 Credential Response](#36-credential-response)

Finally, the issuer response with the verifiable credential requested. An example of the response of the server is as follows:

```json
{
   "format":"jwt_vc",
   "credential":"eyJraWQiOiJkaWQ6ZWJzaTp6dFJvWXlKTmRHcjh0bUF0Vmg5Y2c5biM1Rk41UWdSMmpPdzdRRHFwXzJHc1JsenBBRmliOGwzVUEzNGRGSDdnWTRJIiwidHlwIjoiSldUIiwiYWxnIjoiRVMyNTYifQ.eyJzdWIiOiJkaWQ6a2V5OnoyZG16RDgxY2dQeDhWa2k3SmJ1dU1tRllyV1BnWW95dHlrVVozZXlxaHQxajlLYm5kaTRGekU3YnE5aXJQR1FWeVpHN1NXSHk4aXFwS01qamhtdEI3SkYzZUZZbk02N1N4TmQ0Z2pUM0RzS1ViN05LZUtMY05URW9jWVVmMmtwQlFSUXFDdkdNQ3ZDODdGOGpneWRTaEZDUFR3ckRwdkpLclpNZHE4empRTFF4d1cya0wiLCJuYmYiOjE3Mzg1NzcwMjcsImlzcyI6ImRpZDplYnNpOnp0Um9ZeUpOZEdyOHRtQXRWaDljZzluIiwiZXhwIjoxNzcwMDI2NjI3LCJpYXQiOjE3Mzg1NzcwMjcsInZjIjp7IkBjb250ZXh0IjpbImh0dHBzOi8vd3d3LnczLm9yZy8yMDE4L2NyZWRlbnRpYWxzL3YxIl0sInR5cGUiOlsiVmVyaWZpYWJsZUNyZWRlbnRpYWwiLCJWZXJpZmlhYmxlQXR0ZXN0YXRpb24iLCJldS5ldXJvcGEuZWMuZXVkaS5waWQiXSwiaWQiOiJ2Yzp1c2VsZjphZ2VudCM4MTAwMjgxNzkwMDAxMzMzNjUwIiwiaXNzdWVkIjoiMjAyNS0wMi0wM1QxMDowMzo0N1oiLCJ2YWxpZEZyb20iOiIyMDI1LTAyLTAzVDEwOjAzOjQ3WiIsImNyZWRlbnRpYWxTY2hlbWEiOnsiaWQiOiJodHRwczovL2FwaS1jb25mb3JtYW5jZS5lYnNpLmV1L3RydXN0ZWQtc2NoZW1hcy1yZWdpc3RyeS92Mi9zY2hlbWFzL3ozTWdVRlVrYjcyMnVxNHgzZHY1eUFKbW5ObXpERmVLNVVDOHg4M1FvZUxKTSIsInR5cGUiOiJGdWxsSnNvblNjaGVtYVZhbGlkYXRvcjIwMjEifSwidGVybXNPZlVzZSI6eyJpZCI6Imh0dHBzOi8vYXBpLXBpbG90LmVic2kuZXUvdHJ1c3RlZC1pc3N1ZXJzLXJlZ2lzdHJ5L3Y1L2lzc3VlcnMvZGlkOmVic2k6enRSb1l5Sk5kR3I4dG1BdFZoOWNnOW4vYXR0cmlidXRlcy9jN2MzOTg0Y2JlYzUzMGQ4ZGE5M2IyYzU2MGZhNjg5ZjYzNDBkOWY1NmM4Mzk2ZGU5YmM5Y2U4ZGEwYTYwOTJjIiwidHlwZSI6Iklzc3VhbmNlQ2VydGlmaWNhdGUifSwiaXNzdWVyIjoiZGlkOmVic2k6enRSb1l5Sk5kR3I4dG1BdFZoOWNnOW4iLCJpc3N1YW5jZURhdGUiOiIyMDI1LTAyLTAzVDEwOjAzOjQ3WiIsImV4cGlyYXRpb25EYXRlIjoiMjAyNi0wMi0wMlQxMDowMzo0N1oiLCJjcmVkZW50aWFsU3ViamVjdCI6eyJpZCI6ImRpZDprZXk6ejJkbXpEODFjZ1B4OFZraTdKYnV1TW1GWXJXUGdZb3l0eWtVWjNleXFodDFqOUtibmRpNEZ6RTdicTlpclBHUVZ5Wkc3U1dIeThpcXBLTWpqaG10QjdKRjNlRlluTTY3U3hOZDRnalQzRHNLVWI3TktlS0xjTlRFb2NZVWYya3BCUVJRcUN2R01DdkM4N0Y4amd5ZFNoRkNQVHdyRHB2SktyWk1kcTh6alFMUXh3VzJrTCIsImRvY3VtZW50X251bWJlciI6IjEyMzQ1Njc4OSIsImdpdmVuX25hbWUiOiJKb2huIiwiZmFtaWx5X25hbWUiOiJEb2UiLCJiaXJ0aF9kYXRlIjoiMTk5MC0wMS0wMSIsImFnZV9vdmVyXzE4IjoidHJ1ZSJ9LCJjcmVkZW50aWFsU3RhdHVzIjp7InR5cGUiOiJTdGF0dXNMaXN0MjAyMUVudHJ5IiwiaWQiOiJodHRwczovL3RhZHBvbGUtaW50ZXJuYWwtbWFtbWFsLm5ncm9rLWZyZWUuYXBwL3N0YXR1cy92MSMwIiwic3RhdHVzTGlzdEluZGV4IjoiMCIsInN0YXR1c0xpc3RDcmVkZW50aWFsIjoiaHR0cHM6Ly90YWRwb2xlLWludGVybmFsLW1hbW1hbC5uZ3Jvay1mcmVlLmFwcC9zdGF0dXMvdjEiLCJzdGF0dXNQdXJwb3NlIjoicmV2b2NhdGlvbiJ9fSwianRpIjoidmM6dXNlbGY6YWdlbnQjODEwMDI4MTc5MDAwMTMzMzY1MCJ9.6chCpZeWq9E6vvkuD8tIC_qbgXz83zlXQwHKSnaeWoDB7BoSZC5hImEavOuJukhAKxaEuJcya44ttT8yu0JNRQ"
}
```

## [4 References](#4-references)

1. [OpenID for Verifiable Credential Issuance (VCI) Draft 11](https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0-11.html)
2. [The European Digital Identity Wallet Architecture and Reference Framework (v1.4.0)](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/releases/tag/v1.4.0)
3. [RFC 9101 OAuth 2.0 Authorization Framework: JWT-Secured Authorization Request (JAR)](https://www.rfc-editor.org/rfc/rfc9101.html#name-request-using-the-request_u)
4. [DIF Presentation Exchange](https://identity.foundation/presentation-exchange)
