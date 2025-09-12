## <a id="_Toc182376683"></a><a id="_Toc184710030"></a>Chapter 5: Natural persons and legal entities onboarding process

This chapter describes the onboarding process for integrating individuals \- students and professionals \- and legal entities into the digital credential ecosystem\. Covering both educational and professional pathways, the chapter highlights the streamlined approach to verifying user identity and credential eligibility\. Effective onboarding is essential for ensuring security, user control over personal data, and seamless credential issuance, setting a reliable foundation for lifelong credential portability within the European Union\.

### <a id="_Toc182376684"></a><a id="_Toc184710031"></a>5\.1 Educational onboarding process

#### Overview

This chapter describes the student onboarding process within an educational institution\. The process is divided into three distinct phases: admission, enrolment, and credential issuance\. Each phase involves a series of actions, decision points, and interactions between various actors and systems\. The following sections outline the key steps in each phase, the actors involved, and the systems required to execute the process\.

 

#### Process description

The student onboarding process ensures that a prospective student progresses from initial application to full enrolment and finally receives their digital credential\. Each phase is interconnected and relies on the successful completion of the previous phase\.  
The credential issuance process follows standardized formats based on the W3C Verifiable Credentials Data Model and European Learning Model, ensuring that credentials are both human and machine\-readable while maintaining compatibility with European\-wide systems\.

#### Overall process flow

 Once admission, enrolment and first credential issuance phases are completed, the student is fully onboarded into the institution, with their admission approved, enrolment confirmed, and credential issued\.

 

BPMN Diagram 

![Image3](../../images/bbp-image3.png)

#### Phases of the onboarding process

The student onboarding process is structured into three main phases:

 

1\. Admission Phase

2\. Enrolment Phase

3\. Credential Issuance Phase

 

Each phase includes specific tasks, interactions, and decision points, which are detailed below\.

 

##### Phase 1: Admission

 The admission phase is the first stage of the onboarding process\. Prospective students begin by submitting their personal and academic details for review\. Depending on the method chosen, this data can be submitted directly by the student, or by an authorised institution acting on their behalf\.

 

Actors

- Student: Provides personal details\.
- Educational Institution Official: Reviews the application and verifies identity\.
- Authorised Institution Official: Submits data on behalf of the student \(if applicable\)\.

 

Process description

- Data submission: The student can submit their data through the institution's online admission portal\.
- Identity verification: Once the data is submitted, the institution uses an identity verification system to confirm the applicant's identity\.
- Data validation: Following identity verification, the data is validated to ensure its accuracy and compliance with institutional requirements\.
- Alternate submission: If an authorised institution submits the data, the same validation and identity verification steps apply\.

 

The admission phase concludes once the data is successfully validated\.

 

BPMN Diagram Placeholder

![Image4](../../images/bbp-image4.png)

##### Phase 2: Enrolment

 The enrolment phase begins once the admission process has been completed\. During this phase, the student authenticates their identity, selects courses, and completes any necessary payments\.

 

Actors

- Student: Logs into the system, selects courses, and makes payments \(if required\)\.
- Enrolment Management System: Manages the enrolment process and course selection\.
- Authentication System: Verifies the student's identity \(via eID, EUDI wallet, or in\-person\)\.
- Payment System Provider: Processes payments for course enrolment\.

 

Process Description

- Authentication: The student logs into the enrolment management system and is prompted to authenticate their identity using a national eID, a EUDI wallet with personal identity data \(PID\), or in\-person verification\.
- Course selection: Once authenticated, the student gains access to the course catalogue and selects their courses\.
- Payment: If payment is required for the chosen programme, the system directs the student to a secure payment gateway\.
- Enrolment completion: Upon completing the course selection and payment, the student's enrolment is confirmed, and they can proceed to the next phase\.

 

BPMN Diagram 

![Image5](../../images/bbp-image5.png)

 

##### Phase 3: Credential Issuance

 The credential issuance phase involves providing the student with a digital credential \(EducationalID\), which grants them access to institutional services\.

 

Actors

- Student: Receives the digital credential and accepts it into their EUDI wallet\.
- Credential Issuance System: Manages the creation and issuance of the digital credential\.
- QR Code Generation System: Generates a QR code for the credential\.
- Student Information System: Updates the student’s record\.
- Remote Access System: Grants the student access to the institution's remote services\.

 

Process Description

- Credential issuance options: The student has three options to receive their credential:
	- In\-person: The student visits the academic secretary's office, where an official generates a QR code, which the student scans with their EUDI wallet\.
	- Email: The student receives an email containing a secure deep link that directs them to a QR code, which they scan to accept the credential\.
	- Online: The student logs into an online portal, authenticates, and scans the QR code to receive the credential\.
- Credential acceptance: After scanning the QR code, the student accepts the credential into their EUDI wallet\.
- Student information update: The system updates the student’s record to reflect the successful issuance of the credential\.
- Remote access: Once the credential is issued, the student is granted access to the institution's remote services\.

 

BPMN Diagram 


![Image6](../../images/bbp-image6.png)

#### Actors and Systems Overview

Actor/System

Role

 Student                      

 Initiates the admission process, enrols in courses, and receives the digital credential\.          

 Educational Institution Official 

 Reviews applications and verifies student identity\.                                             

 Authorised Institution Official 

 Submits data on behalf of the student \(if applicable\)\.                                           

 Online Admission Portal       

 Receives student data and forwards it for validation and review\.                                 

 Identity Verification System  

 Verifies the identity of the student through online or in\-person methods\.                        

 Data Validation System        

 Confirms the accuracy of the student‚Äôs application data\.                                         

 Enrolment Management System   

 Manages student enrolment, including authentication and course selection\.                        

 Authentication System         

 Provides identity verification for the student during the enrolment process\.                     

 Payment Gateway               

 Processes payments for course enrolment, interacting with the payment system provider\.           

 Payment System Provider       

 Handles secure payments and confirms payment transactions\.                                       

 Credential Issuance System    

 Manages the creation and issuance of the student‚Äôs digital credential\.                           

 QR Code Generation System     

 Generates QR codes used for credential acceptance\.                                               

 Student Information System    

 Updates the student‚Äôs record after credential issuance\.                                          

 Remote Access System          

 Provides access to the institution's remote services after credential issuance\.                   

### <a id="_Toc182376685"></a><a id="_Toc184710032"></a>5\.2 Professional qualifications onboarding process

#### Overview

This chapter describes the professional qualifications onboarding process within authorized professional bodies and associations\. The process is divided into three distinct phases: request, enrolment, and credential issuance\. Each phase involves a series of actions, decision points, and interactions between various actors and systems\. The following sections outline the key steps in each phase, the actors involved, and the systems required to execute the process\.

#### Process description

The professional qualifications onboarding process ensures that a professional progresses from initial request to full enrolment and finally receives their digital credentials\. Each phase is interconnected and relies on the successful completion of the previous phase\.

#### Overall process flow

Once request, enrolment and credential issuance phases are completed, the professional is fully onboarded into the system, with their request approved, enrolment confirmed, and credentials issued\.

#### Phases of the onboarding process

The professional qualifications onboarding process is structured into three main phases:

1. Request Phase
2. Enrolment Phase
3. Credential Issuance Phase

Each phase includes specific tasks, interactions, and decision points, which are detailed below\.

##### Phase 1: Request

The request phase is the first stage of the onboarding process\. Professionals begin by logging into their association's platform and submitting their personal and professional details for review\.

Actors

- Professional: Provides personal and professional details
- Professional Association Official: Reviews the application and verifies identity
- Identity Verification Service Provider: Validates the professional's identity

Process description

- Platform Access: The professional logs into the association's platform using existing credentials
- Identity verification: The professional's identity is verified through online or in\-person methods
- Data validation: Following identity verification, the data is validated to ensure its accuracy and compliance with professional requirements

The request phase concludes once the data is successfully validated\.

##### Phase 2: Enrolment

The enrolment phase begins once the request process has been completed\. During this phase, the professional authenticates their identity, selects required credentials, and completes any necessary payments\.

Actors

- Professional: Authenticates identity and selects credentials
- Professional Association Official: Oversees the enrolment process
- Authentication System: Verifies the professional's identity
- Payment System Provider: Processes payments if required

Process Description

- Authentication: The professional authenticates their identity using a national eID, a EUDI wallet with personal identity data \(PID\), or in\-person verification
- Credential Selection: Once authenticated, the professional selects the required credentials
- Payment: If payment is required, the system directs the professional to a secure payment gateway
- Enrolment completion: Upon completing the credential selection and payment, the professional's enrolment is confirmed

##### Phase 3: Credential Issuance

The credential issuance phase involves providing the professional with digital credentials that verify their qualifications and enable them to practice their profession\.

Actors

- Professional: Receives the digital credentials and accepts them into their EUDI wallet
- Professional Association Official: Manages credential issuance
- Credential Issuance System: Manages the creation and issuance of digital credentials
- QR Code Generation System: Generates QR codes for credential acceptance
- Central Registry System: Updates the professional's record

Process Description

- Credential issuance options: The professional has three options to receive their credentials:
	- In\-person: Visit to the association office where an official generates a QR code
	- Email: Receive an email containing a secure deep link to a QR code
	- Online: Log into an online portal, authenticate, and scan the QR code
- Credential acceptance: After scanning the QR code, the professional accepts the credentials into their EUDI wallet
- List update: The system updates the professional's record in the central list
- Access grant: Once credentials are issued, the professional can share them with employers or regulatory bodies as needed

##### Actors and Systems Overview

Actor/System

Role

 Professional 

 Initiates the request process, completes enrolment, and receives digital credentials 

 Professional Association Official 

 Reviews applications and verifies professional identity 

 Platform Access System 

 Manages professional login and initial data submission 

 Identity Verification System 

 Verifies the identity through online or in\-person methods 

 Data Validation System 

 Confirms the accuracy of the professional's application data 

 Authentication System 

 Provides identity verification during the enrolment process 

 Payment Gateway 

 Processes payments when required 

 Credential Issuance System 

 Manages the creation and issuance of digital credentials 

 QR Code Generation System 

 Generates QR codes for credential acceptance 

 Central Registry System 

 Updates the professional's records after credential issuance 

 Email System 

 Delivers secure links for online credential acceptance 

 Remote Access System 

 Enables credential sharing with employers and regulatory bodies 

### <a id="_Toc182376686"></a><a id="_Toc184710033"></a>5\.3 Legal entities onboarding process

#### 5\.3\.1 Introduction

Legal entities must join the trust framework through a structured process that maintains quality and trust across the credentialing ecosystem\. This chapter explains how organisations become authorised members of the framework\.

The inclusion of legal entities in the trust framework represents a critical step in establishing a reliable credential ecosystem\. Each organisation's participation adds to the framework's value, creating a network of trusted credential issuers and verifiers across Europe\. This process builds upon existing regulatory structures while adding the necessary digital trust layer for modern credential management\.

The onboarding process follows the non\-delegated trust model from Chapter 4, with each organisation retaining direct control of their credentials within the European framework\. This approach respects institutional autonomy while ensuring consistent standards across the network\.

##### 5\.3\.1\.1 Participating organisations 

The framework's effectiveness depends on the participation of diverse organisations across the education and professional qualification sectors\. Each type of organisation brings specific value to the ecosystem, contributing to a comprehensive network of trusted credential issuers and verifiers\.

The framework accepts these organisations:

- 1\. Educational bodies
	- Universities
	- Higher education institutions
	- Vocational education providers
	- Professional education centres
	- Continuing education organisations

These institutions form the core of the credential issuance network, providing primary academic and professional qualifications that serve as the foundation for career development and further education\.

- 2\. Professional organisations
	- Professional associations
	- Industry certification bodies
	- Regulatory bodies
	- Quality control agencies

Professional organisations add sector\-specific expertise and validation, ensuring credentials meet industry standards and professional requirements\.

- 3\. Accreditation bodies
	- National accreditors
	- Subject\-specific accreditors
	- International accreditors

Accreditation bodies provide quality assurance across the network, validating the standards of both educational and professional credentials\.

- 4\. Public authorities
	- Education ministries
	- Professional regulators
	- Quality oversight bodies

Public authorities establish the regulatory framework and provide official recognition of credentials at national and European levels\.

#### 5\.3\.2 Entry requirements

The entry requirements establish baseline standards for participation in the trust framework\. These requirements balance the need for rigorous verification with practical implementation considerations, ensuring that participating organisations can maintain high standards while operating efficiently\.

##### 5\.3\.2\.1 Legal standards

Legal standards protect the integrity of the credential ecosystem and ensure compliance with European and national regulations\. These requirements create a foundation of trust through verified legal status and demonstrated compliance with relevant education and professional standards\.

Organisations must meet these requirements:

- Legal position
	- Registration in home country
	- Education law compliance
	- Qualification authority
	- Good standing proof
- Rules compliance
	- Education standards met
	- Professional recognition
	- Data protection measures
	- Cross\-border permissions
- Quality checks
	- Current accreditation
	- Quality systems
	- External reviews
	- Written procedures

##### 5\.3\.2\.2 Technical standards

Technical standards ensure that participating organisations can interact securely and efficiently within the digital credential ecosystem\. These requirements focus on practical capabilities needed for secure credential management while maintaining flexibility in specific implementation approaches\.

Organisations need these capabilities:

- Systems
	- Protected IT setup
	- Data safeguards
	- Digital signatures
	- Recovery plans
- Connection methods
	- API readiness
	- Identity systems
	- Credential tools
	- Checking processes
- Work methods
	- File management
	- Record tracking
	- Staff preparation
	- Problem response

#### 5\.3\.3 The joining process

The joining process addresses three distinct governance types that shape how legal entities participate in the trust framework:

##### 5\.3\.3\.1 Entitlement governance onboarding

This process establishes an organisation's legal authority to act within the education or professional qualifications domain:

- Verification of legal basis
	- National authority confirmation
	- Legal scope definition
	- Cross\-border recognition status
	- Regulatory compliance check
- Domain authority establishment
	- Qualification issuing rights
	- Professional recognition scope
	- Geographic coverage
	- Authority limitations
- Framework registration
	- Legal entity identifier assignment
	- Authority scope documentation
	- Public registry inclusion
	- Status publication

##### 5\.3\.3\.2 Quality assurance regime onboarding

This process integrates organisations into the quality assurance framework:

- Quality framework alignment
	- Standards mapping
	- Assessment processes
	- Review cycles
	- Improvement mechanisms
- Audit process establishment
	- Audit schedule setting
	- Assessment criteria
	- Evidence requirements
	- Review procedures
- Accreditation integration
	- Recognition processes
	- Standard alignment
	- Cross\-border applicability
	- Renewal procedures

##### 5\.3\.3\.3 Non\-foundational identity governance onboarding

This process enables organisations to participate in non\-foundational identity credential issuance \(credentials under trust services legal regime, not eID legal regime\):

- Identity credential authority
	- Credential type definition
	- Issuance scope
	- Verification mechanisms
	- Privacy safeguards
- Technical integration
	- Identity systems setup
	- Verification infrastructure
	- Privacy controls
	- Security measures
- Operational procedures
	- Identity verification processes
	- Credential lifecycle management
	- Status update mechanisms
	- Privacy protection measures

#### 5\.3\.4 Flow diagram

The onboarding of legal entities into the trust framework follows a structured process that addresses three distinct governance types: entitlement, quality assurance, and non\-foundational identity\. Each flow represents a specific aspect of establishing trust and authority within the framework\.

![Image7](../../images/bbp-image7.png)