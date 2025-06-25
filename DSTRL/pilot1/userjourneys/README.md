# DC4EU Trusted Lists Pilot: User Journeys Description

The DC4EU Trusted Lists pilot, executed under Work Package 5 (WP5), supports six User Journeys using Classical PKI with CRLs/OCSP for secure credential issuance and verification. These journeys facilitate an International Student Exchange scenario, enabling students to manage and verify digital credentials (e.g., PID, Diploma, Micro-credential, EHIC) cross-border. Below, each User Journey is detailed, including key actors, elements, and their interactions.

## Key Actors and Elements
- **Wallet Holder (End-User/Student)**: The individual (e.g., a student in the pilot, such as "Helen Mirren" with username "mirren") who interacts with the wallet to manage credentials.
- **Wallet**: The EUDI Wallet (wwWallet), a mobile or web-based application provided by WP7, used by the wallet holder to store, manage, and present verifiable credentials.
- **Issuer**: The entity issuing credentials (e.g., educational institutions or authorities), integrated with the DC4EU Interoperability Lab, responsible for generating PIDs, Diplomas, Micro-credentials, and EHIC.
- **Relying Party (RP)**: The entity (e.g., a foreign university or enrollment office) verifying credentials presented by the wallet holder.
- **Relying Party Services**: Systems or APIs that facilitate credential verification, interacting with the wallet and authentic sources.
- **Authentic Source Data Store**: A secure repository holding authoritative data (e.g., identity records, educational records) used by issuers to generate credentials.
- **Database with Educational Records**: A system storing academic data (e.g., diplomas, micro-credentials) accessed by issuers to issue verifiable credentials.
- **Schemes (ELM Schemas)**: Standardized data formats (European Learning Model schemas) defined in WP5, ensuring credentials adhere to EU standards.
- **Trusted Lists with Classical PKI**: A framework using PKI with CRLs/OCSP to ensure trust and verify the validity of issued credentials.
- **DC4EU Interoperability Lab**: The technical environment (SaaS or integrated) provided by WP7, hosting issuer, verifier, and wallet components.
- **Support Channels**: Slack, Teams, email, and GitHub for technical and non-technical support, managed by SURF and WP7.

## User Journeys

### 1. Install Wallet
**Description**: The wallet holder installs the EUDI Wallet (wwWallet) to manage digital credentials.
- **Actors and Elements**:
  - **Wallet Holder**: Downloads and installs the wallet.
  - **Wallet**: Provided by the DC4EU Interoperability Lab (WP7).
  - **Support Channels**: Provide documentation (e.g., step-by-step instructions on pages 16–20 of the pilot document) and support via SURF.
- **Interactions**:
  - The wallet holder accesses the DC4EU Interoperability Lab (SaaS environment) or integrates components (Integration-pilot).
  - The wallet is installed on the user’s device (mobile/web) using provided documentation or a video walkthrough (available early June).
  - The wallet holder logs in using credentials (e.g., username: "mirren", password: "mirren").
- **PKI Role**: No direct PKI interaction; the wallet is pre-configured to trust issuers listed in the Trusted Lists.

### 2. Issue PID
**Description**: The issuer generates a Personal Identification (PID) credential for the wallet holder, which is stored in the wallet.
- **Actors and Elements**:
  - **Wallet Holder**: Initiates the PID issuance process via the wallet.
  - **Issuer**: An authority integrated with the Interoperability Lab, issuing the PID.
  - **Wallet**: Receives and stores the PID.
  - **Authentic Source Data Store**: Provides identity data for PID issuance.
  - **Trusted Lists with Classical PKI**: Ensures the issuer’s certificate is valid using CRLs/OCSP.
- **Interactions**:
  - The wallet holder scans a QR code (e.g., PID QR code for "Helen Mirren") using the wallet.
  - The wallet communicates with the issuer via the Interoperability Lab.
  - The issuer retrieves identity data from the Authentic Source Data Store, signs the PID with its private key, and issues it to the wallet.
  - The wallet verifies the issuer’s certificate against the Trusted Lists using CRLs/OCSP and stores the PID.
- **PKI Role**: The issuer’s certificate is validated to ensure trust; CRLs/OCSP check for revocation.

### 3. Issue Diploma
**Description**: The issuer generates a Diploma credential, which the wallet holder stores in the wallet.
- **Actors and Elements**:
  - **Wallet Holder**: Requests the Diploma via the wallet.
  - **Issuer**: An educational institution issuing the Diploma.
  - **Wallet**: Stores the Diploma.
  - **Database with Educational Records**: Provides academic data for the Diploma.
  - **Schemes (ELM Schemas)**: Ensures the Diploma adheres to EU standards.
  - **Trusted Lists with Classical PKI**: Validates the issuer’s certificate.
- **Interactions**:
  - The wallet holder scans a Diploma QR code (e.g., for "Helen Mirren").
  - The wallet requests the Diploma from the issuer via the Interoperability Lab.
  - The issuer retrieves academic data from the Database with Educational Records, formats it per ELM schemas, signs it, and issues it.
  - The wallet verifies the issuer’s certificate and stores the Diploma.
- **PKI Role**: The issuer’s certificate is checked via CRLs/OCSP to ensure it is not revoked.

### 4. Issue Micro-credential
**Description**: The issuer generates a Micro-credential, which is stored in the wallet.
- **Actors and Elements**:
  - **Wallet Holder**: Requests the Micro-credential.
  - **Issuer**: An institution issuing the Micro-credential.
  - **Wallet**: Stores the Micro-credential.
  - **Database with Educational Records**: Provides data for the Micro-credential.
  - **Schemes (ELM Schemas)**: Ensures standardization.
  - **Trusted Lists with Classical PKI**: Validates the issuer’s certificate.
- **Interactions**:
  - The wallet holder scans a Micro-credential QR code.
  - The wallet requests the credential from the issuer.
  - The issuer retrieves data, formats it per ELM schemas, signs it, and issues it.
  - The wallet verifies the issuer’s certificate and stores the Micro-credential.
- **PKI Role**: CRLs/OCSP ensure the issuer’s certificate is valid.

### 5. Verify PID and Diploma
**Description**: The relying party verifies the wallet holder’s PID and Diploma for enrollment or exchange purposes.
- **Actors and Elements**:
  - **Wallet Holder**: Presents the PID and Diploma via the wallet.
  - **Relying Party**: Verifies the credentials (e.g., a university).
  - **Relying Party Services**: Facilitate verification.
  - **Wallet**: Shares the credentials securely.
  - **Authentic Source Data Store**: May be queried for PID validation.
  - **Database with Educational Records**: May be queried for Diploma validation.
  - **Trusted Lists with Classical PKI**: Validates the issuer’s certificate.
- **Interactions**:
  - The wallet holder presents the PID and Diploma to the relying party via the wallet (e.g., scanning a verification QR code).
  - The wallet shares the credentials with the relying party services.
  - The relying party services verify the issuer’s certificate against the Trusted Lists using CRLs/OCSP.
  - The relying party may query the Authentic Source Data Store (for PID) or Database with Educational Records (for Diploma) to confirm authenticity.
  - The relying party confirms the credentials’ validity.
- **PKI Role**: CRLs/OCSP ensure the issuer’s certificate is not revoked during verification.

### 6. Verify PID and Micro-credential
**Description**: The relying party verifies the wallet holder’s PID and Micro-credential.
- **Actors and Elements**:
  - **Wallet Holder**: Presents the PID and Micro-credential.
  - **Relying Party**: Verifies the credentials.
  - **Relying Party Services**: Facilitate verification.
  - **Wallet**: Shares the credentials.
  - **Authentic Source Data Store**: May be queried for PID.
  - **Database with Educational Records**: May be queried for Micro-credential.
  - **Trusted Lists with Classical PKI**: Validates the issuer’s certificate.
- **Interactions**:
  - The wallet holder presents the PID and Micro-credential via the wallet.
  - The wallet shares the credentials with the relying party services.
  - The relying party services verify the issuer’s certificate using CRLs/OCSP.
  - The relying party may query the Authentic Source Data Store or Database with Educational Records.
  - The relying party confirms the credentials’ validity.
- **PKI Role**: CRLs/OCSP validate the issuer’s certificate.

