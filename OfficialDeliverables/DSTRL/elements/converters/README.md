# DC4EU Converters: Bridging Educational Credential Formats

## Overview

The DC4EU project is developing a suite of **converters** to facilitate seamless interoperability between different educational credential formats across Europe. These converters are essential tools that transform existing data models into the standardised **European Learning Model (ELM)** format, ensuring compatibility with the **EU Digital Identity Wallet (EUDIW)**.

## Why Are Converters Necessary?

Currently, there are multiple data models used across Europe to describe digital certificates in the educational domain:

- **ELMO/EMREX** - European Learner Mobility format
- **OpenBadges** - Digital badge credentials
- **Microcredentials** - Short-form learning achievements
- **National formats** - Country-specific credential models

To avoid requiring the EUDIW to support all these different formats, DC4EU converters standardise credentials into the **European Learning Model (ELM) version 3.2**, creating a unified approach to digital educational credentials.

## Available Converters

### 1. ELMO2ELM Converter

**Purpose**: Converts European Learner Mobility (ELMO) credentials to ELM format and vice versa.

**Key Features**:
- Supports ELMO version 1.7 to ELM version 3.2 conversion
- Bidirectional conversion capability
- 100% semantic equivalence between ELMO 1.7 and ELM version 3
- XML to JSON-LD format conversion

**Use Cases**:
- Student mobility within European Higher Education Area
- Integration with EMREX network
- Academic transcript transfer between institutions

### 2. OpenBadges Converter

**Purpose**: Transforms OpenBadges credentials into ELM format and back.

**Key Features**:
- Supports OpenBadges 3.0 (OBv3) to ELM conversion
- Bidirectional transformation
- Alignment with W3C Verifiable Credentials specification
- Command Line Interface (CLI) available

**Technical Highlights**:
- Compatible with SURF EduBadges platform
- Multi-language support for error feedback
- Configurable mapping system
- Open source development

### 3. Microcredentials Converter

**Purpose**: Converts EU microcredentials to ELM format following European Council recommendations.

**Key Features**:
- Aligns with EU Council Recommendation on microcredentials
- Supports JSON-LD format conversion
- Compatible with Europass microcredential mapping
- Bidirectional conversion capability

**Standards Compliance**:
- Based on EU guidelines for microcredentials
- Follows European approach to lifelong learning
- Supports portable, validated credentials

## Technical Architecture

### Common Foundations

All DC4EU converters share these technical principles:

- **Verifiable Credentials (VCs)**: Implementation of W3C standards
- **Decentralized Identifiers (DIDs)**: Support for decentralised identity
- **European Learning Model**: Target format for all conversions
- **EUDIW Integration**: Designed for seamless wallet compatibility

### Conversion Scope

**What converters handle**:
- Semantic conversion of educational content
- Data model transformation
- Credential metadata mapping
- Multi-language support

**What converters don't handle**:
- VC ID elements (DIDs)
- Cryptographic proofs
- Digital signatures and seals
- Context elements

## How to Use the Converters

### Online Demo Platform

Access the converters through our demonstration website:
**https://converters.dc4eu.eu**

**Important**: This is a demonstration platform only. **Do not upload production or personal data**.

### API Integration

All converters provide a consistent REST API interface:

```json
{
  "From": {"Name": "elmo", "Version": "1.7"},
  "To": {"Name": "elm", "Version": "3.2"},
  "Parameters": {"PreferredLanguages": ["en", "sv"]},
  "Content": "[base64-encoded-credential]"
}
```

### Example Usage

**ELMO to ELM Conversion**:
```bash
curl -L 'http://localhost:8080/rest/request' \
  -H 'Content-Type: application/json' \
  -d '{"From": {"Name": "elmo", "Version": "1.7"}, 
       "To": {"Name": "elm", "Version": "3.2"}, 
       "Parameters": {"PreferredLanguages": ["en", "sv"]}, 
       "Content": "[base64-encoded-content]"}'
```

## Implementation Guide

### For Educational Institutions

**Step 1: Assessment**
- Identify current credential formats in use
- Determine integration requirements
- Assess technical capabilities

**Step 2: Pilot Implementation**
- Start with test credentials
- Validate conversion accuracy
- Train technical staff

**Step 3: Full Deployment**
- Integrate with existing systems
- Implement quality assurance processes
- Monitor conversion results

### For Developers

**Integration Requirements**:
- RESTful API integration
- JSON format handling
- Base64 encoding/decoding
- Error handling implementation

**Documentation Resources**:
- OpenAPI specifications
- Semantic mapping guides
- Technical integration examples
- Testing frameworks

## Quality Assurance and Compliance

### Data Protection

- **GDPR Compliance**: No permanent storage of personal data
- **Privacy by Design**: Data processed only during conversion
- **Temporary Storage**: Automatic deletion of conversion artifacts
- **Transparent Processing**: Clear documentation of data handling

### Testing and Validation

- **Module Testing**: Individual converter validation
- **Interoperability Testing**: Cross-system compatibility
- **Data Integrity**: Verification of conversion accuracy
- **Performance Testing**: System reliability under load

## Support and Training

### Training Resources

- **Technical Workshops**: For IT teams and developers
- **Documentation**: Comprehensive guides and tutorials
- **Use Cases**: Real-world implementation examples
- **Community Support**: Forums and knowledge sharing

### Ongoing Support

- **Regular Updates**: Adapting to evolving standards
- **Maintenance**: Continued functionality assurance
- **Community Forums**: Peer learning and troubleshooting
- **Professional Support**: Technical assistance for implementation

## Future Development

### Planned Enhancements

- **National Format Support**: Additional country-specific converters
- **Extended Mappings**: Support for more credential types
- **Performance Improvements**: Optimised conversion processes
- **Enhanced Validation**: Stronger quality assurance mechanisms

### Community Involvement

- **Open Source Development**: Community contributions welcome
- **Standards Evolution**: Participation in European education standards
- **Pilot Programmes**: Collaboration with educational institutions
- **Feedback Integration**: Continuous improvement based on user needs

## Getting Started

1. **Explore the Demo**: Visit https://converters.dc4eu.eu
2. **Review Documentation**: Access technical specifications
3. **Contact Support**: Reach out for implementation guidance
4. **Join the Community**: Participate in forums and discussions

## Technical Support

For technical assistance, integration support, or questions about the converters:

- **Project Website**: https://www.dc4eu.eu
- **Documentation**: OpenAPI specifications available online
- **Community Forums**: Technical discussions and peer support
- **Professional Services**: Implementation assistance available

---

*The DC4EU converters represent a significant step towards unified digital credentialing across Europe, enabling seamless recognition of educational achievements and supporting lifelong learning mobility.*