# DC4EU Deployment and Testing Scenarios Results Library (DTSRL) – Scenario: University of Bologna (UNIBO)

## 1. Scenario identification
- **Piloting agent name**: University of Bologna (UNIBO)  
- **Scenario title**: EducationID and HED Credential Issuance & Verification  
- **Date of submission**: [To be filled]  
- **Point of contact (SPOC)**: SGAD【45†source】  

## 2. Scenario characterisation
- **Number of end-users involved**: 30 pilot students (as per Datastore setup)【25†source】
- **User journeys**: Onboarding students, PID retrieval, EducationID issuance, HED issuance, cross-border verification  
- **Target groups**: Final-year students, administrative staff  
- **EAAs involved**: EducationID, Higher Education Diploma (HED)  
- **Institutional systems**: Keycloak, PID generator, Verifier GUI, Datastore  
- **Technical components**:
  - Pilot option: Pilot 2 (Decentralised PKI)
  - DNS endpoint: lspdc4edu.unibo.it  
  - Issuer/Verifier: uSelf components by ATOS/IZERTIS  
  - Wallet: EUDIW via TestFlight/Google Play  
  - PID service: uSelf PID Generator  
- **Governance configuration**:
  - Trust model: Decentralised PKI (dPKI)  
  - Issuer X.509v3 cert: [Link to PEM or screenshot]  
  - Relying Party cert: [Access cert and scope for HED verification]  
  - DIDs: [If dPKI used]  
- **Monitoring and feedback mechanisms**: Weekly reports submitted, KPI status tracked  

## 3. Legal, organisational and operational details
- **Regulatory context**: GDPR compliance, national HE rules  
- **Risk management**: Credential revocation/removal not yet supported in EUDIW  
- **Credential lifecycle management**: Pending clarification on deletion/removal of credentials  
- **Infrastructure readiness**: Datastore with 30 pilot users (demo setup)  
- **Training and onboarding**: Demo session with master’s students (June 2025)  
- **Issue escalation**: SPOC support channel with WP5 technical partners  
- **Success indicators and KPIs**: Number of credentials issued, verified, and validated cross-border  

## 4. Trust model onboarding evidences
- **Issuer X.509v3 certificate**: Not applicable (dPKI pilot)  
- **Relying party access certificate**: Not applicable (dPKI pilot)  
- **PID credentials and metadata**: uSelf PID Generator setup and verified  
- **DIDs**: Issuer and Verifier DID registered (per Tracker)【37†source】  
- **Registry reference**: Registered in EAA governance catalogue and trust list  

## 5. Implementation and testing progress
- **Credentials issued**: 20 EducationIDs and 20 HED credentials【25†source】
- **Credentials verified**: At least one successful cross-border verification with URV【25†source】
- **Status**: In progress (as of June 2025)  
- **Users onboarded**: 30 pilot users  
- **Credentials issued**: ~20 EducationIDs and HEDs  
- **Successes**: Demo conducted with students; PID, EducationID, and HED issued  
- **Issues**: Inability to remove credentials; cross-border validation inconsistencies  
- **Deviation from plan**: None major noted  

## 6. Testing results and observations
- **What worked**: Infrastructure setup, issuance pipeline up to wallet  
- **Issues**: Deletion of credentials; verification integration across borders  
- **User feedback**: Collected from demo sessions (to be summarised)  
- **Impact**: Functional but needs support on lifecycle and trust interoperability  

## 7. Evidence archive and references
- **Screenshots/logs**: Keycloak, wallet installation, issuance steps  
- **Links**:  
  - Keycloak: https://uself-keycloak.lspdc4edu.unibo.it/  
  - Wallet: https://testflight.apple.com/join/Z7WhgfKC  
  - PID: https://uself-pid-generator.lspdc4edu.unibo.it  
  - Verifier: https://uself-verifier-gui.lspdc4edu.unibo.it/  
- **Documents**: [To be filled]  
- **KPI data**: Weekly Excel logs provided (May–June 2025)  

## 8. Next steps and recommendations
- **Pending**: Enable credential removal; finalise DID registry entries  
- **Recommendations**: Clarify lifecycle actions in EUDIW wallet  
- **Methodology improvements**: Include error management and credential recovery protocols  


## 9. Summary of end-user feedback (students, staff, verifiers)
- General impressions: [To be summarised based on user survey]  
- Ease of use of EUDIW wallet: [To be added]  
- Challenges encountered: [To be added]  
- Suggestions from users: [To be added]  
- Willingness to use the service again: [To be added]  

## 10. Summary of piloting agent insights
- Feedback on support from SPOC/WP5: [To be added]  
- Main barriers during implementation: [To be added]  
- Lessons learned: [To be added]  
- Observed impact and value: [To be added]  
- Recommendations for improvement: [To be added]  
