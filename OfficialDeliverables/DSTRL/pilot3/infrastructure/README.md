# Pilot3 Infrastructure Documentation

## Overview

**Pilot3** is a combined implementation approach that runs both **Pilot1** and **Pilot2** simultaneously. Institutions selecting Pilot3 deploy dual infrastructure to support both classical PKI (Pilot1) and decentralised PKI (Pilot2) trust models concurrently.

## Foundation and Basis

Pilot3 is fundamentally defined as:

```
Pilot3 = Pilot1 + Pilot2
```

This means that Pilot3 institutions must:
- Implement **both** classical PKI and decentralised PKI infrastructure
- Deploy **two public endpoints** - one for each pilot
- Provide **both sets of evidence** required for Pilot1 and Pilot2 compliance
- Support **both credential formats** (SD-JWT and W3C Verifiable Credentials)

## Relationship with Pilot1 and Pilot2

### Pilot1 Component (Classical PKI)
- **Trust Model**: Classical PKI with hierarchical certificate authorities
- **Credential Format**: SD-JWT (Selective Disclosure JSON Web Token)
- **Endpoint**: PKI-based public endpoint

### Pilot2 Component (Decentralised PKI)
- **Trust Model**: Combined Classical PKI + Decentralised PKI
- **Credential Format**: W3C Verifiable Credentials
- **Endpoint**: dPKI-based public endpoint

## Implementation Requirements

Pilot3 institutions must fulfill the infrastructure requirements for **both** pilots:

### From Pilot1
- X.509v3 PKI certificate as issuer
- X.509v3 PMI certificate as relying party
- CRL coordinates for trust verification
- Classical PKI infrastructure

### From Pilot2
- DID enabling trust discovery for issuer and relying party
- Complete education/professional qualifications governance documentation
- EBSI integration capabilities
- W3C Verifiable Credentials support

## Related Infrastructure Documentation

For detailed implementation guidance, please refer to the specific pilot documentation:

### Pilot1 Infrastructure References
- [Pilot1 Infrastructure Setup and Requirements](./pilot1/infrastructure.md)
- [Pilot1 PKI Implementation Guide](./pilot1/pki-implementation.md)
- [Pilot1 Certificate Management](./pilot1/certificate-management.md)
- [Pilot1 SD-JWT Processing](./pilot1/sd-jwt-processing.md)

### Pilot2 Infrastructure References
- [Pilot2 Infrastructure Setup and Requirements](./pilot2/infrastructure.md)
- [Pilot2 DID Implementation Guide](./pilot2/did-implementation.md)
- [Pilot2 EBSI Integration](./pilot2/ebsi-integration.md)
- [Pilot2 W3C VC Processing](./pilot2/w3c-vc-processing.md)
*This implementation has been validated using the [DC4EU Technical Validation Methodology](../../../procedures/validation/validation-methodology.md) developed by GRNet.*

## Additional Resources

- [DC4EU Pilot Architecture Overview](./pilots-overview.md)
- [Trust Model Comparison Guide](./trust-models-comparison.md)
- [Pilot Selection Guidelines](./pilot-selection-guide.md)
- [Deployment Best Practices](./deployment-best-practices.md)


**Note**: Pilot3 does not introduce new infrastructure components. It simply requires the deployment and operation of both Pilot1 and Pilot2 infrastructure simultaneously. For comprehensive implementation details, please consult the individual pilot documentation linked above.