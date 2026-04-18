# EUHEMC JAdES D-Zero Verification Guide

## Overview

This guide provides step-by-step instructions for verifying European Higher Education Microcredentials (EUHEMC) signed with the JAdES D-Zero profile. It includes practical code examples and tool recommendations for both technical and non-technical verifiers.

## Prerequisites

- **JWS Format**: `header.payload.signature` (Base64URL encoded)
- **Signature Algorithm**: ES256 (ECDSA with P-256 curve and SHA-256)
- **Profile**: JAdES D-Zero as specified by EBSI
- **Trust Infrastructure**: EBSI registries for DID resolution and trust validation

## Verification Tools

### Option 1: EBSI Wallet Application
- **EBSI Wallet**: Official verification tool supporting JAdES D-Zero
- **Web Interface**: Access via EBSI's verification portal
- **Mobile App**: Download from official app stores

### Option 2: Command Line Tools
- **OpenSSL**: For cryptographic operations
- **jq**: For JSON processing
- **curl**: For API interactions with EBSI registries

### Option 3: Programming Libraries
- **Node.js**: `jsonwebtoken`, `jose`, `did-resolver`
- **Python**: `jose`, `cryptography`, `did-resolver-python`
- **Java**: `nimbus-jose-jwt`, `did-common-java`

## Step-by-Step Verification Process

### Step 1: Parse the JWS Structure

First, split the JWS into its three components:

#### Using Command Line (bash/zsh)
```bash
# Set the JWS token
JWS_TOKEN="eyJhbGciOiJFUzI1NiIsInR5cCI6ImphZGVzLWQteiIsImN0eSI6InZjK2xkK2pzb24iLCJraWQiOiJkaWQ6ZWJzaTp6aXVGUU5SV3I2dk5lRXBUZ2ltbUNwdyNrZXlzLTEiLCJjcml0IjpbInNpZ1QiLCJzaWdQbCJdLCJzaWdUIjoiMjAyNS0wNS0wNFQxMDowMDowMFoiLCJzaWdQbCI6eyJhZGRyZXNzQ291bnRyeSI6IkVTIiwiYWRkcmVzc0xvY2FsaXR5IjoiVGFycmFnb25hIiwicG9zdGFsQ29kZSI6IjQzMDA3Iiwic3RyZWV0QWRkcmVzcyI6IkNhcnJlciBkZSBsJ0VzY29yeGFkb3IsIHMvbiJ9fQ.eyJAY29udGV4dCI6WyJodHRwczovL3d3dy53My5vcmcvMjAxOC9jcmVkZW50aWFscy92MSIsImh0dHBzOi8vdzNpZC5vcmcvZWRjL3YxIl0sImlkIjoidXJuOnV1aWQ6NGY4ZDdjOWUtOWExYi00YjFlLThmMmEtNWMzZTZkN2I5YzBkIiwidHlwZSI6WyJWZXJpZmlhYmxlQ3JlZGVudGlhbCIsIkV1cm9wZWFuRGlnaXRhbENyZWRlbnRpYWwiLCJFdXJvcGVhbkhpZ2hlckVkdWNhdGlvbk1pY3JvQ3JlZGVudGlhbHMiXSwiaXNzdWVyIjp7ImlkIjoiZGlkOmVic2k6eml1RlFOUldyNnZOZUVwVGdpbW1DcHcifSwiaXNzdWVyQ291bnRyeSI6eyJpZCI6InVybjpjb25jZXB0OmVzIiwidHlwZSI6IkNvbmNlcnQiLCJwcmVmTGFiZWwiOnsiZW4iOiJTcGFpbiJ9fSwiaXNzdWFuY2VEYXRlIjoiMjAyNS0wNS0wNFQxMDowMDowMFoiLCJpc3N1ZWQiOiIyMDI1LTA1LTA0VDEwOjAwOjAwWiIsInZhbGlkRnJvbSI6IjIwMjUtMDUtMDRUMTA6MDA6MDBaIiwicXVhbGl0eUFzc3VyYW5jZSI6eyJpZCI6InVybjpjb25jZXB0OmVzZyIsInR5cGUiOiJDb25jZXB0IiwicHJlZkxhYmVsIjp7ImVuIjoiRVNHLWNvbXBsaWFudCJ9fSwiY3JlZGVudGlhbFN1YmplY3QiOnsiaWQiOiJkaWQ6ZWJzaTpleGFtcGxlOnN0dWRlbnQxMjMiLCJ0eXBlIjoiUGVyc29uIiwiZnVsbE5hbWUiOnsiZW4iOiJKdWFuIFDDqXJleiBHYXJj7WEifSwiZ2l2ZW5OYW1lIjp7ImVuIjoiSnVhbiJ9LCJmYW1pbHlOYW1lIjp7ImVuIjoiUMOpcmV6In0sIm5hdGlvbmFsSUQiOnsiaWQiOiJ1cm46bGVnYWw6ZXM6RE5JOjEyMzQ1Njc4WiIsInR5cGUiOiJMZWdhbElkZW50aWZpZXIiLCJub3RhdGlvbiI6IjEyMzQ1Njc4WiJ9LCJoYXNDbGFpbSI6W3siaWQiOiJ1cm46dXVpZDoxMjM0LTU2NzgtOTBhYi1jZGVmIiwidHlwZSI6IkxlYXJuaW5nQWNoaWV2ZW1lbnQiLCJ0aXRsZSI6eyJlbiI6IlN0YXRpc3RpY2FsIERhdGEgQW5hbHlzaXMgTWljcm9jcmVkZW50aWFsIn0sImRlc2NyaXB0aW9uIjp7ImVuIjoiQSBjb21wcmVoZW5zaXZlIG1pY3JvY3JlZGVudGlhbCBjb3ZlcmluZyBzdGF0aXN0aWNhbCBkYXRhIGFuYWx5c2lzIG1ldGhvZHMgYW5kIGFwcGxpY2F0aW9ucy4ifSwiY3JlZGl0UmVjZWl2ZWQiOnsiaWQiOiJ1cm46dXVpZDoyMzQ1LTY3ODktMGFiYy1kZWZnIiwidHlwZSI6IkVDVFNDcmVkaXRQb2ludHMiLCJwb2ludCI6NX0sImxlYXJuaW5nT3V0Y29tZSI6W3siaWQiOiJ1cm46dXVpZDozNDU2LTc4OTAtYWJjZC1lZmdoIiwidHlwZSI6IkxlYXJuaW5nT3V0Y29tZSIsInRpdGxlIjp7ImVuIjoiU3RhdGlzdGljYWwgRGF0YSBBbmFseXNpcyJ9fV19LCJhd2FyZGVkQnkiOnsiaWQiOiJ1cm46dXVpZDphd2FyZC0xIiwidHlwZSI6IkF3YXJkaW5nUHJvY2VzcyIsImF3YXJkaW5nQm9keSI6eyJpZCI6ImRpZDplYnNpOnppdUZRTlJXcjZ2TmVFcFRnaW1tQ3B3IiwidHlwZSI6Ik9yZ2FuaXNhdGlvbiIsImxlZ2FsTmFtZSI6eyJlbiI6IlJvdmlyYSBpIFZpcmdpbGkgVW5pdmVyc2l0eSJ9fX19XX0sImNyZWRlbnRpYWxTY2hlbWEiOnsiaWQiOiJodHRwczovL3RydXN0ZWQtcmVnaXN0cmllcy5lYnNpLmV1L3NjaGVtYXMvZXVoZW1jLzEuMCIsInR5cGUiOiJKc29uU2NoZW1hIn0sImRpc3BsYXlQYXJhbWV0ZXIiOnsiaWQiOiJ1cm46dXVpZDo2ZjdnOGg5aS0wajFrLTJsM20tNG41by02cDdxOHI5czB0MXUiLCJ0eXBlIjoiRGlzcGxheVBhcmFtZXRlciIsInRpdGxlIjp7ImVuIjoiRVUIRU1DIERpc3BsYXkifSwibGFuZ3VhZ2UiOlt7ImlkIjoidXJuOmNvbmNlcnQ6ZW4iLCJ0eXBlIjoiQ29uY2VwdCIsInByZWZMYWJlbCI6eyJlbiI6IkVuZ2xpc2gifX1dLCJwcmltYXJ5TGFuZ3VhZ2UiOnsiaWQiOiJ1cm46Y29uY2VwdDplbiIsInR5cGUiOiJDb25jZXB0IiwicHJlZkxhYmVsIjp7ImVuIjoiRW5nbGlzaCJ9fSwiaW5kaXZpZHVhbERpc3BsYXkiOlt7ImlkIjoidXJuOnV1aWQ6N2c4aDlpMGotMWsybC0zbTRuLTVvNnAtN3E4cjlzMHQxdTJ2IiwidHlwZSI6IkluZGl2aWR1YWxEaXNwbGF5IiwiZmllbGRQYXRoIjoiY3JlZGVudGlhbFN1YmplY3QuZnVsbE5hbWUiLCJsYWJlbCI6eyJlbiI6IkZ1bGwgTmFtZSJ9LCJvcmRlciI6MX0seyJpZCI6InVybjp1dWlkOjhoOWkwajFrLTJsM20tNG41by02cDdxLThyOXMwdDF1MnYzd3ciLCJ0eXBlIjoiSW5kaXZpZHVhbERpc3BsYXkiLCJmaWVsZFBhdGgiOiJjcmVkZW50aWFsU3ViamVjdC5oYXNDbGFpbVswXS50aXRsZSIsImxhYmVsIjp7ImVuIjoiQWNoaWV2ZW1lbnQgVGl0bGUifSwib3JkZXIiOjJ9XX19.[signature-placeholder]"

# Split the JWS into components
IFS='.' read -r HEADER PAYLOAD SIGNATURE <<< "$JWS_TOKEN"

echo "Header: $HEADER"
echo "Payload: $PAYLOAD"
echo "Signature: $SIGNATURE"

# Decode header and payload
echo "$HEADER" | base64 -d | jq '.'
echo "$PAYLOAD" | base64 -d | jq '.'
```

#### Using Python
```python
import base64
import json
from jose import jws, jwt
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
import requests

def parse_jws(jws_token):
    """Parse JWS into header, payload, and signature components"""
    try:
        header, payload, signature = jws_token.split('.')
        
        # Decode header and payload
        header_decoded = json.loads(base64.urlsafe_b64decode(header + '=='))
        payload_decoded = json.loads(base64.urlsafe_b64decode(payload + '=='))
        
        return header_decoded, payload_decoded, signature
    except Exception as e:
        raise ValueError(f"Invalid JWS format: {e}")

# Example usage
jws_token = "eyJhbGciOiJFUzI1NiIsInR5cCI6ImphZGVzLWQteiI..."
header, payload, signature = parse_jws(jws_token)
print("Header:", json.dumps(header, indent=2))
print("Payload:", json.dumps(payload, indent=2))
```

#### Using Node.js
```javascript
const jwt = require('jsonwebtoken');
const jose = require('jose');

function parseJWS(jwsToken) {
    const [headerB64, payloadB64, signatureB64] = jwsToken.split('.');
    
    const header = JSON.parse(Buffer.from(headerB64, 'base64url').toString());
    const payload = JSON.parse(Buffer.from(payloadB64, 'base64url').toString());
    
    return { header, payload, signature: signatureB64 };
}

// Example usage
const jwsToken = "eyJhbGciOiJFUzI1NiIsInR5cCI6ImphZGVzLWQteiI...";
const { header, payload, signature } = parseJWS(jwsToken);
console.log('Header:', JSON.stringify(header, null, 2));
console.log('Payload:', JSON.stringify(payload, null, 2));
```

### Step 2: Validate Header Fields

Verify the header contains the required JAdES D-Zero fields:

```python
def validate_header(header):
    """Validate JAdES D-Zero header fields"""
    required_fields = {
        'alg': 'ES256',
        'typ': 'jades-d-z',
        'cty': 'vc+ld+json'
    }
    
    # Check required algorithm and type
    for field, expected_value in required_fields.items():
        if header.get(field) != expected_value:
            raise ValueError(f"Invalid {field}: expected {expected_value}, got {header.get(field)}")
    
    # Validate critical fields
    if 'crit' not in header:
        raise ValueError("Missing critical extensions field")
    
    required_crit = ['sigT', 'sigPl']
    if not all(field in header['crit'] for field in required_crit):
        raise ValueError("Missing required critical extensions")
    
    # Validate key identifier format
    if 'kid' not in header:
        raise ValueError("Missing key identifier")
    
    if not header['kid'].startswith('did:ebsi:'):
        raise ValueError("Invalid DID format in kid field")
    
    # Validate signature timestamp
    if 'sigT' not in header:
        raise ValueError("Missing signature timestamp")
    
    # Validate signing place
    if 'sigPl' not in header:
        raise ValueError("Missing signing place")
    
    required_sigpl_fields = ['addressCountry', 'addressLocality']
    sigpl = header['sigPl']
    for field in required_sigpl_fields:
        if field not in sigpl:
            raise ValueError(f"Missing {field} in signing place")
    
    print("✓ Header validation passed")
    return True
```

### Step 3: Validate Payload Schema

Verify the payload conforms to the EUHEMC schema:

```python
import jsonschema
import requests

def validate_payload_schema(payload):
    """Validate payload against EUHEMC schema"""
    
    # Check required W3C VC fields
    required_vc_fields = ['@context', 'id', 'type', 'issuer', 'credentialSubject']
    for field in required_vc_fields:
        if field not in payload:
            raise ValueError(f"Missing required VC field: {field}")
    
    # Validate context
    required_contexts = [
        "https://www.w3.org/2018/credentials/v1",
        "https://w3id.org/edc/v1"
    ]
    
    for context in required_contexts:
        if context not in payload['@context']:
            raise ValueError(f"Missing required context: {context}")
    
    # Validate credential types
    required_types = ['VerifiableCredential', 'EuropeanDigitalCredential', 'EuropeanHigherEducationMicroCredentials']
    for cred_type in required_types:
        if cred_type not in payload['type']:
            raise ValueError(f"Missing required credential type: {cred_type}")
    
    # Validate Annex I mandatory elements
    annex_i_fields = [
        'issuerCountry',
        'issuanceDate',
        'qualityAssurance'
    ]
    
    for field in annex_i_fields:
        if field not in payload:
            raise ValueError(f"Missing Annex I mandatory field: {field}")
    
    # Validate credential subject
    credential_subject = payload['credentialSubject']
    required_subject_fields = ['id', 'type', 'fullName', 'hasClaim']
    
    for field in required_subject_fields:
        if field not in credential_subject:
            raise ValueError(f"Missing credential subject field: {field}")
    
    # Validate learning achievement claims
    claims = credential_subject['hasClaim']
    if not isinstance(claims, list) or len(claims) == 0:
        raise ValueError("Missing learning achievement claims")
    
    for claim in claims:
        required_claim_fields = ['id', 'type', 'title', 'creditReceived']
        for field in required_claim_fields:
            if field not in claim:
                raise ValueError(f"Missing claim field: {field}")
    
    # Validate credential schema reference(s).
    #
    # IMPORTANT — profile detection:
    #   * VCDM 1.1 profile (mandatory per the 1st batch of Implementing Acts):
    #       `credentialSchema` is a single object (or a one-element array) of
    #       type "JsonSchema". Run JSON Schema syntactic validation only.
    #   * VCDM 2.0 profile (optional, forward-looking, dual validation):
    #       `credentialSchema` is an array containing at least one "JsonSchema"
    #       entry AND one "ShaclValidator2017" entry. Run JSON Schema
    #       validation AND SHACL validation against the RDF graph materialised
    #       from the JSON-LD (using the ELM v3.2 context).
    # Verifiers SHOULD accept both profiles during the transition period and
    # once future Implementing Act updates recognise VCDM 2.0 alongside 1.1.
    if 'credentialSchema' not in payload:
        raise ValueError("Missing credential schema reference")

    schema_refs = payload['credentialSchema']
    if isinstance(schema_refs, dict):
        schema_refs = [schema_refs]            # normalise to list

    has_json_schema = any(s.get('type') == 'JsonSchema' for s in schema_refs)
    has_shacl       = any(s.get('type') == 'ShaclValidator2017' for s in schema_refs)

    if not has_json_schema:
        raise ValueError("credentialSchema[] must contain a JsonSchema entry")

    for ref in schema_refs:
        if ref.get('type') == 'JsonSchema':
            # e.g. validate with jsonschema/ajv against the referenced schema.
            # All referenced schema URIs MUST resolve in the EBSI TSR v3.
            validate_json_schema(payload, ref['id'])
        elif ref.get('type') == 'ShaclValidator2017':
            # VCDM 2.0 only. Example: pyshacl.validate(rdf_graph, shacl_graph).
            validate_shacl_shape(payload, ref['id'])
        else:
            raise ValueError(f"Unsupported credentialSchema type: {ref.get('type')}")

    profile = "VCDM 2.0 (dual validation)" if has_shacl else "VCDM 1.1"
    print(f"✓ Payload schema validation passed ({profile})")
    return True
```

### Step 4: Retrieve Public Key from DID

Resolve the issuer's DID to obtain the public key:

```python
def resolve_did_key(did_url):
    """Resolve DID to retrieve public key"""
    
    # Extract DID and key fragment
    if '#' in did_url:
        did, key_fragment = did_url.split('#')
    else:
        raise ValueError("Invalid DID URL format")
    
    # EBSI DID resolution endpoint
    did_resolver_url = f"https://api-pilot.ebsi.eu/did-registry/v4/identifiers/{did}"
    
    try:
        response = requests.get(did_resolver_url)
        response.raise_for_status()
        did_document = response.json()
        
        # Find the verification method
        verification_methods = did_document.get('verificationMethod', [])
        
        for method in verification_methods:
            if method['id'].endswith(f"#{key_fragment}"):
                # Extract public key from JWK format
                public_key_jwk = method['publicKeyJwk']
                
                # Validate key type and curve
                if public_key_jwk.get('kty') != 'EC':
                    raise ValueError("Invalid key type")
                if public_key_jwk.get('crv') != 'P-256':
                    raise ValueError("Invalid curve")
                
                return public_key_jwk
        
        raise ValueError(f"Key {key_fragment} not found in DID document")
        
    except requests.RequestException as e:
        raise ValueError(f"Failed to resolve DID: {e}")

# Example usage
did_url = "did:ebsi:ziuFQNRWr6vNeEpTgimmCpw#keys-1"
public_key_jwk = resolve_did_key(did_url)
print("✓ Public key retrieved successfully")
```

### Step 5: Verify Cryptographic Signature

Verify the ECDSA signature:

```python
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.backends import default_backend
import base64

def verify_signature(jws_token, public_key_jwk):
    """Verify ECDSA signature"""
    
    header_b64, payload_b64, signature_b64 = jws_token.split('.')
    
    # Reconstruct signing input
    signing_input = f"{header_b64}.{payload_b64}".encode('ascii')
    
    # Decode signature
    signature_bytes = base64.urlsafe_b64decode(signature_b64 + '==')
    
    # Convert JWK to cryptography public key
    x = base64.urlsafe_b64decode(public_key_jwk['x'] + '==')
    y = base64.urlsafe_b64decode(public_key_jwk['y'] + '==')
    
    # Create public key object
    public_numbers = ec.EllipticCurvePublicNumbers(
        int.from_bytes(x, byteorder='big'),
        int.from_bytes(y, byteorder='big'),
        ec.SECP256R1()
    )
    public_key = public_numbers.public_key(default_backend())
    
    # Verify signature
    try:
        public_key.verify(
            signature_bytes,
            signing_input,
            ec.ECDSA(hashes.SHA256())
        )
        print("✓ Signature verification passed")
        return True
    except Exception as e:
        raise ValueError(f"Signature verification failed: {e}")

# Alternative using jose library
from jose import jws

def verify_signature_jose(jws_token, public_key_jwk):
    """Verify signature using jose library"""
    try:
        # Verify using jose
        payload = jws.verify(jws_token, public_key_jwk, algorithms=['ES256'])
        print("✓ Signature verification passed (jose)")
        return True
    except Exception as e:
        raise ValueError(f"Signature verification failed: {e}")
```

### Step 6: Check EBSI Trust Registry

Verify the issuer is in the trusted issuers registry:

```python
def check_trust_registry(issuer_did):
    """Check if issuer is in EBSI Trusted Issuers Registry"""
    
    # EBSI Trusted Issuers Registry endpoint
    trust_registry_url = "https://api-pilot.ebsi.eu/trusted-issuers-registry/v4/issuers"
    
    try:
        response = requests.get(f"{trust_registry_url}/{issuer_did}")
        
        if response.status_code == 200:
            issuer_info = response.json()
            
            # Check if issuer is authorised for EUHEMC
            authorised_schemas = issuer_info.get('authorisedFor', [])
            euhemc_schema = "https://trusted-registries.ebsi.eu/schemas/euhemc/1.0"
            
            if euhemc_schema in authorised_schemas:
                print("✓ Issuer is authorised in EBSI Trust Registry")
                return True
            else:
                raise ValueError("Issuer not authorised for EUHEMC")
        
        elif response.status_code == 404:
            raise ValueError("Issuer not found in Trust Registry")
        else:
            response.raise_for_status()
            
    except requests.RequestException as e:
        raise ValueError(f"Failed to check trust registry: {e}")
```

### Step 7: Check Revocation Status

Verify the credential hasn't been revoked:

```python
def check_revocation_status(credential_id):
    """Check if credential has been revoked"""
    
    # EBSI Revocation Registry endpoint
    revocation_url = "https://api-pilot.ebsi.eu/revocation/v1/credentials"
    
    try:
        response = requests.get(f"{revocation_url}/{credential_id}")
        
        if response.status_code == 200:
            # Credential found in revocation registry - it's revoked
            raise ValueError("Credential has been revoked")
        elif response.status_code == 404:
            # Credential not found in revocation registry - it's valid
            print("✓ Credential is not revoked")
            return True
        else:
            # Other status codes indicate an error
            response.raise_for_status()
            
    except requests.RequestException as e:
        # If we can't reach the revocation registry, we should warn but not fail
        print(f"⚠ Could not check revocation status: {e}")
        return True
```

## Complete Verification Function

Here's a complete verification function that combines all steps:

```python
def verify_euhemc_credential(jws_token):
    """Complete EUHEMC credential verification"""
    
    try:
        print("🔍 Starting EUHEMC verification...")
        
        # Step 1: Parse JWS
        header, payload, signature = parse_jws(jws_token)
        
        # Step 2: Validate header
        validate_header(header)
        
        # Step 3: Validate payload schema
        validate_payload_schema(payload)
        
        # Step 4: Resolve public key
        public_key_jwk = resolve_did_key(header['kid'])
        
        # Step 5: Verify signature
        verify_signature_jose(jws_token, public_key_jwk)
        
        # Step 6: Check trust registry
        check_trust_registry(payload['issuer']['id'])
        
        # Step 7: Check revocation status
        check_revocation_status(payload['id'])
        
        print("✅ EUHEMC credential verification successful!")
        return {
            'valid': True,
            'issuer': payload['issuer']['id'],
            'subject': payload['credentialSubject']['fullName'],
            'achievement': payload['credentialSubject']['hasClaim'][0]['title'],
            'issued': payload['issuanceDate']
        }
        
    except Exception as e:
        print(f"❌ Verification failed: {e}")
        return {
            'valid': False,
            'error': str(e)
        }

# Example usage
if __name__ == "__main__":
    sample_jws = "eyJhbGciOiJFUzI1NiIsInR5cCI6ImphZGVzLWQteiI..."
    result = verify_euhemc_credential(sample_jws)
    print("Verification result:", result)
```

## Browser-Based Verification Tool

For non-technical users, here's a simple HTML interface:

```html
<!DOCTYPE html>
<html>
<head>
    <title>EUHEMC Verifier</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.1.1/crypto-js.min.js"></script>
</head>
<body>
    <h1>EUHEMC Credential Verifier</h1>
    
    <textarea id="jwsInput" placeholder="Paste EUHEMC JWS token here..." rows="10" cols="80"></textarea>
    <br><br>
    
    <button onclick="verifyCredential()">Verify Credential</button>
    
    <div id="result"></div>
    
    <script>
        async function verifyCredential() {
            const jwsToken = document.getElementById('jwsInput').value;
            const resultDiv = document.getElementById('result');
            
            try {
                // Parse JWS (simplified client-side version)
                const [header, payload, signature] = jwsToken.split('.');
                
                const headerDecoded = JSON.parse(atob(header));
                const payloadDecoded = JSON.parse(atob(payload));
                
                resultDiv.innerHTML = `
                    <h3>Verification Results</h3>
                    <p><strong>Issuer:</strong> ${payloadDecoded.issuer.id}</p>
                    <p><strong>Subject:</strong> ${payloadDecoded.credentialSubject.fullName.en}</p>
                    <p><strong>Achievement:</strong> ${payloadDecoded.credentialSubject.hasClaim[0].title.en}</p>
                    <p><strong>Issue Date:</strong> ${payloadDecoded.issuanceDate}</p>
                    <p><em>Note: Full cryptographic verification requires server-side processing</em></p>
                `;
                
            } catch (error) {
                resultDiv.innerHTML = `<p style="color: red;">Error: ${error.message}</p>`;
            }
        }
    </script>
</body>
</html>
```

## Quick Verification Checklist

For manual verification, use this checklist:

### ✅ Visual Inspection Checklist

1. **JWS Format**: Does the token have three dot-separated parts?
2. **Header Algorithm**: Is `alg` set to `ES256`?
3. **Header Type**: Is `typ` set to `jades-d-z`?
4. **Key Reference**: Does `kid` start with `did:ebsi:`?
5. **Credential Type**: Does the payload include `EuropeanHigherEducationMicroCredentials`?
6. **Schema Reference**: Does it reference the official EUHEMC schema?
7. **Mandatory Fields**: Are all Annex I fields present?
8. **Issuer Information**: Is the issuer a recognised educational institution?

### 🔍 Technical Verification Steps

1. **Parse JWS Structure**
2. **Validate Header Fields**
3. **Validate Payload Schema**
4. **Resolve DID Document**
5. **Verify ECDSA Signature**
6. **Check Trust Registry**
7. **Verify Revocation Status**

## Troubleshooting Common Issues

### Invalid Base64 Encoding
```bash
# Fix padding issues
echo "$HEADER==" | base64 -d
```

### DID Resolution Failures
```python
# Retry with different endpoints
endpoints = [
    "https://api-pilot.ebsi.eu/did-registry/v4/identifiers/",
    "https://api.ebsi.eu/did-registry/v4/identifiers/"
]
```

### Certificate Chain Issues
```python
# Verify certificate chain
import ssl
import socket

def verify_ssl_chain(hostname):
    context = ssl.create_default_context()
    with socket.create_connection((hostname, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            return ssock.getpeercert_chain()
```

## Additional Resources

- **EBSI Documentation**: https://api-pilot.ebsi.eu/docs/
- **JAdES Specification**: ETSI TS 119 182-1
- **W3C Verifiable Credentials**: https://www.w3.org/TR/vc-data-model/
- **RFC 7515 (JWS)**: https://tools.ietf.org/html/rfc7515
- **EBSI Wallet**: Download from official app stores

This guide provides comprehensive verification capabilities for EUHEMC credentials, from simple visual inspection to full cryptographic verification, ensuring both technical and non-technical verifiers can validate credential authenticity and integrity.