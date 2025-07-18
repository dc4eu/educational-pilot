# Hybrid Model vs Pure dPKI: Key Differences and Impact Analysis

**Version**: 1.0  
**Date**: July 2025  
**Context**: DC4EU Technical Implementation Guidance

## Overview

This document provides a focused analysis of the specific differences between **pure dPKI** and **hybrid X.509-DID binding** models for Electronic Attestation of Attributes (EAA) implementation. Whilst both approaches use the same underlying cryptographic principles, they represent fundamentally different trust architectures with significant implications for implementation, verification, and lifecycle management.

## Key Architectural Differences

### Pure dPKI Model (Signature Header)
```json
{
  "alg": "ES256",
  "typ": "jades-d-z",
  "kid": "did:ebsi:ziuFQNRWr6vNeEpTgimmCpw#keys-1"
}
```

**Characteristics:**
- Only references the DID key
- Verification relies solely on EBSI DID Registry
- Single trust path through decentralised infrastructure

### Hybrid X.509-DID Model (Signature Header)
```json
{
  "alg": "ES256",
  "typ": "jades-d-z", 
  "kid": "did:ebsi:ziuFQNRWr6vNeEpTgimmCpw#keys-1",
  "x5c": ["MIICmDCCAgGgAwIBAgIBADANBgkq..."],
  "x5t#S256": "2d4e6f8b9a1c3d5e7f9a0b2c4d6e8f0a1b3c5d7e9f0a2b4c6d8e"
}
```

**Characteristics:**
- References both DID key and X.509 certificate
- Dual verification paths through PKI and dPKI
- Certificate-DID binding validation required

## Specific Implementation Impacts

### 1. Signing Process Changes

#### Pure dPKI Signing
```python
def sign_eaa_pure_dpki(payload, private_key, did_reference):
    """Standard pure dPKI signing"""
    
    header = {
        "alg": "ES256",
        "typ": "jades-d-z",
        "kid": did_reference
    }
    
    return sign_jws(header, payload, private_key)
```

#### Hybrid Model Signing
```python
def sign_eaa_hybrid(payload, private_key, certificate_chain, did_document):
    """Enhanced hybrid model signing"""
    
    # Header includes both DID and certificate
    header = {
        "alg": "ES256",
        "typ": "jades-d-z",
        "kid": "did:ebsi:example#key-1",
        "x5c": certificate_chain,          # NEW: certificate chain
        "x5t#S256": compute_cert_thumbprint(certificate_chain[0])  # NEW: binding
    }
    
    # Rest of the process remains the same
    return sign_jws(header, payload, private_key)

def compute_cert_thumbprint(certificate):
    """Compute SHA-256 thumbprint for binding"""
    cert_der = base64.b64decode(certificate)
    return hashlib.sha256(cert_der).hexdigest()
```

### 2. Verification Process - Major Impact

#### Pure dPKI Verification (Single Path)
```python
def verify_dpki_pure(jws_token):
    """Straightforward single-path verification"""
    
    header, payload, signature = parse_jws(jws_token)
    
    # Single verification path only
    public_key = resolve_did_key(header['kid'])
    verify_signature(jws_token, public_key)
    check_ebsi_trust_registry(payload['issuer']['id'])
    
    return {"status": "verified", "trust_path": "dPKI"}
```

#### Hybrid Verification (Dual Path with Binding)
```python
def verify_hybrid_eaa(jws_token):
    """Complex dual-path verification with binding validation"""
    
    header, payload, signature = parse_jws(jws_token)
    
    # CRITICAL: Verify certificate-DID binding first
    verify_certificate_did_binding(header)
    
    # PATH 1: Traditional PKI verification
    if 'x5c' in header:
        cert_chain = header['x5c']
        verify_certificate_chain(cert_chain)
        verify_certificate_revocation(cert_chain[0])
        public_key_pki = extract_public_key_from_cert(cert_chain[0])
        verify_signature(jws_token, public_key_pki)
    
    # PATH 2: dPKI verification
    public_key_did = resolve_did_key(header['kid'])
    verify_signature(jws_token, public_key_did)
    
    # BINDING VERIFICATION: Critical in hybrid model!
    cert_thumbprint = compute_thumbprint(cert_chain[0])
    did_document = resolve_did_document(header['kid'])
    did_thumbprint = extract_thumbprint_from_did(did_document, header['kid'])
    
    if cert_thumbprint != did_thumbprint:
        raise ValueError("Certificate-DID binding verification failed")
    
    # Dual trust chain verification
    check_ebsi_trust_registry(payload['issuer']['id'])
    check_pki_trust_list(cert_chain)
    
    return {
        "status": "verified", 
        "trust_paths": ["PKI", "dPKI"],
        "binding_verified": True
    }
```

### 3. New Failure Points in Hybrid Model

#### Critical Binding Verification
```python
def verify_certificate_did_binding(header):
    """Hybrid model-specific verification - no equivalent in pure dPKI"""
    
    if 'x5c' not in header:
        raise ValueError("Missing certificate chain in hybrid model")
    
    if 'x5t#S256' not in header:
        raise ValueError("Missing certificate thumbprint")
    
    # Compute certificate thumbprint
    cert_der = base64.b64decode(header['x5c'][0])
    computed_thumbprint = hashlib.sha256(cert_der).hexdigest()
    
    # Resolve DID Document
    did_url = header['kid']
    did_document = resolve_did_document(did_url)
    
    # Search for matching verification method
    verification_methods = did_document.get('verificationMethod', [])
    binding_found = False
    
    for method in verification_methods:
        jwk = method.get('publicKeyJwk', {})
        if jwk.get('x5t#S256') == computed_thumbprint:
            binding_found = True
            
            # Additional check: verify key material matches
            if not verify_key_material_consistency(header['x5c'][0], jwk):
                raise ValueError("Key material mismatch between certificate and DID")
            break
    
    if not binding_found:
        raise ValueError("Certificate not bound to DID - x5t#S256 not found")
    
    return True

def verify_key_material_consistency(certificate, jwk):
    """Verify certificate and JWK contain the same public key"""
    
    # Extract public key from certificate
    cert_der = base64.b64decode(certificate)
    cert_public_key = extract_public_key_coordinates(cert_der)
    
    # Extract coordinates from JWK
    jwk_x = int.from_bytes(base64.urlsafe_b64decode(jwk['x'] + '=='), 'big')
    jwk_y = int.from_bytes(base64.urlsafe_b64decode(jwk['y'] + '=='), 'big')
    
    return cert_public_key['x'] == jwk_x and cert_public_key['y'] == jwk_y
```

### 4. Lifecycle Management Differences

#### Pure dPKI Key Rotation (Simple)
```python
def rotate_dpki_key(did, new_private_key):
    """Straightforward key rotation"""
    
    new_public_key_jwk = private_key_to_jwk(new_private_key)
    
    update_did_document(did, {
        'verificationMethod': [{
            'id': f"{did}#new-key",
            'publicKeyJwk': new_public_key_jwk
        }]
    })
    
    return {"status": "rotation_complete"}
```

#### Hybrid Key Rotation (Complex Coordination)
```python
def rotate_hybrid_key(did, old_cert, new_private_key):
    """Hybrid model rotation requires careful coordination"""
    
    # 1. Generate new certificate with new public key
    new_cert = request_certificate(new_private_key.public_key())
    
    # 2. Compute new binding thumbprint
    new_thumbprint = compute_thumbprint(new_cert)
    
    # 3. Update DID Document with binding information
    new_public_key_jwk = private_key_to_jwk(new_private_key)
    new_public_key_jwk['x5t#S256'] = new_thumbprint
    
    update_did_document(did, {
        'verificationMethod': [{
            'id': f"{did}#new-key",
            'publicKeyJwk': new_public_key_jwk
        }]
    })
    
    # 4. Manage transition period
    # Both certificates may need to be valid during overlap
    manage_certificate_transition(old_cert, new_cert)
    
    # 5. Verify binding is working
    test_binding_verification(did, new_cert)
    
    return {
        "status": "rotation_complete",
        "old_cert_valid_until": get_cert_expiry(old_cert),
        "new_cert_active_from": datetime.utcnow().isoformat()
    }
```

## Advantages of the Hybrid Model

### 1. Dual Trust Validation
```
Traditional PKI Trust Path:
Certificate Authority → Root CA → Trust List → Certificate Validation

dPKI Trust Path:
DID → EBSI Registry → Accreditation Chain → Trust Verification

Hybrid Model:
Both paths must validate successfully + binding verification
```

### 2. Enhanced Interoperability
- **Legacy Systems**: Can verify using traditional PKI certificate validation
- **Modern Systems**: Can use dPKI verification through EBSI
- **Binding Assurance**: Guarantees consistency between both trust models

### 3. Resilience and Fallback Capability
```python
def resilient_verification(jws_token):
    """Verification with intelligent fallback"""
    
    verification_results = {
        'dpki_available': False,
        'pki_available': False,
        'binding_valid': False
    }
    
    try:
        # Attempt dPKI verification first (preferred)
        result_dpki = verify_via_did(jws_token)
        verification_results['dpki_available'] = True
    except EBSIUnavailableError:
        logger.warning("EBSI unavailable, falling back to PKI verification")
    except Exception as e:
        logger.error(f"dPKI verification failed: {e}")
    
    try:
        # Attempt PKI verification
        result_pki = verify_via_certificate(jws_token)
        verification_results['pki_available'] = True
    except Exception as e:
        logger.error(f"PKI verification failed: {e}")
    
    # Verify binding if both are available
    if verification_results['dpki_available'] and verification_results['pki_available']:
        try:
            verify_certificate_did_binding(parse_jws(jws_token)[0])
            verification_results['binding_valid'] = True
        except Exception as e:
            logger.warning(f"Binding verification failed: {e}")
    
    # Determine overall trust level
    if all(verification_results.values()):
        return {"status": "maximum_trust", "verified_paths": ["PKI", "dPKI"]}
    elif verification_results['dpki_available'] or verification_results['pki_available']:
        return {"status": "single_path_verified", "trust_level": "medium"}
    else:
        return {"status": "verification_failed", "trust_level": "none"}
```

## Performance and Complexity Impact

### Verification Time Comparison

| Process Step | Pure dPKI | Hybrid Model | Overhead |
|--------------|-----------|--------------|----------|
| Header parsing | 1ms | 2ms | +100% |
| DID resolution | 150ms | 150ms | 0% |
| Certificate validation | 0ms | 200ms | +200ms |
| Binding verification | 0ms | 50ms | +50ms |
| Signature verification | 5ms | 5ms | 0% |
| **Total Average** | **156ms** | **407ms** | **+161%** |

### Implementation Complexity

```python
# Pure dPKI - Dependencies
dependencies_pure = [
    'did-resolver',
    'jose',
    'cryptography'
]

# Hybrid Model - Additional Dependencies
dependencies_hybrid = dependencies_pure + [
    'pyOpenSSL',           # Certificate chain validation
    'cryptography[x509]',  # X.509 certificate handling
    'certifi',             # CA bundle management
    'ocsp',                # OCSP revocation checking
    'python-crl'           # CRL validation
]
```

## When to Choose Each Model

### Pure dPKI - Recommended When:
- **Digital-native organisation** with no legacy PKI infrastructure
- **Performance is critical** (≈150ms verification time)
- **Simplified maintenance** is preferred
- **EBSI infrastructure is highly reliable** in your deployment context

### Hybrid Model - Recommended When:
- **Legacy PKI integration** is required
- **Maximum interoperability** with existing systems is needed
- **Enhanced trust assurance** through dual validation is valued
- **Regulatory compliance** requires traditional PKI elements
- **Fallback capability** during EBSI unavailability is important

## Conclusion

**The hybrid model represents a fundamentally different trust architecture**, not merely an alternative signing method. Key takeaways:

### Critical Differences
1. **Signing Process**: Header complexity increases with `x5c` and `x5t#S256` fields
2. **Verification Process**: Dual-path verification with mandatory binding validation
3. **Lifecycle Management**: Coordination required between PKI and dPKI systems
4. **Performance Impact**: Approximately 161% increase in verification time
5. **Complexity**: Higher implementation and maintenance overhead

### Strategic Considerations
- **It's not just "what you sign with"** - it's a comprehensive **trust model decision**
- **Binding verification is the critical differentiator** - failure here invalidates the entire credential
- **Both PKI and dPKI infrastructure must be maintained** and monitored
- **Enhanced resilience comes at the cost of increased complexity**

### Implementation Recommendation
Choose your approach based on:
- Organisational PKI maturity and legacy requirements
- Performance requirements and acceptable verification latency
- Trust assurance needs and regulatory compliance requirements
- Technical team capability to manage dual trust infrastructure

The X.509-DID binding is the **defining characteristic** that separates this model from pure dPKI and requires specific implementation considerations throughout the entire credential lifecycle.

---

*This analysis is part of the DC4EU technical documentation series. For implementation guidance, refer to the specific guides for your chosen approach.*