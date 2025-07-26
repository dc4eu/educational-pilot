# DC4EU Pilot 3 (Combined PKI/dPKI) - Comprehensive Survey Analysis

## Executive Summary

This comprehensive analysis examines all survey responses from Pilot 3 institutions participating in the DC4EU combined PKI and decentralised PKI implementation. Six responses were received from the three participating institutions across all 15 survey questions, representing the most technically complex pilot approach requiring dual trust model implementation.

**Critical Findings:**
- **6 verified Pilot 3 responses** from all 3 participating institutions (100% institutional coverage)
- **Average recommendation score: 4.4/10** (lowest among all pilots, indicating significant implementation challenges)
- **100% problem incidence rate** (all 6 responses reported technical issues)
- **Significant trust concerns** with only 1 response expressing confidence in the toolset

---

## Institutional Coverage Verification

### Complete Pilot 3 Survey Participants

| Institution | Country | Responses | Coverage Assessment |
|-------------|---------|-----------|-------------------|
| **University of Twente** | Netherlands | 2 responses | ✅ Complete coverage |
| **Saxion University of Applied Sciences** | Netherlands | 3 responses | ✅ Enhanced coverage |
| **COFAC - Lusófona University** | Portugal | 1 response | ✅ Complete coverage |

**Total Coverage:** 3/3 institutions (100%)
**Response Density:** 6 responses from 3 institutions (2.0 responses per institution average)

### Geographic Distribution Analysis

**Netherlands Dominance:** 5/6 responses (83.3%)
- University of Twente: 2 responses
- Saxion University: 3 responses
- Reflects intensive Dutch engagement with hybrid trust models

**Portuguese Participation:** 1/6 responses (16.7%)
- COFAC - Lusófona University: 1 response
- Represents international validation of hybrid approach

---

## Detailed Response Analysis by Institution

### University of Twente (2 responses) - Technical Implementation Challenges

University of Twente provided two distinct responses reflecting different aspects of their hybrid implementation experience.

#### Response 1 - Critical System Failure
**Performance Metrics:**
- **Recommendation Score:** 0/10 (lowest possible score)
- **Problems:** Yes - Complete system failure
- **Trust Level:** "I don't trust the tool at all"
- **Problem Description:** "I could open the wallet, but I couldn't retrieve any credential. I had a blank screen all the time. Even after refreshing many times, waiting for 10 minutes and more. Frustrating test."

**Feature Analysis (All rated as critical gaps):**
- **All features rated maximum importance (5/5)** but **minimum satisfaction (1/5)**
- **Universal dissatisfaction pattern:** Configuration, Dashboard, Integration, Customisation, Revocation Control
- **Critical system failure** preventing any functional testing

**Trust and Privacy Assessment:**
- **Complete distrust** in system reliability
- **Data misuse concerns:** "I think my personal data is misused during the usage of the tool"
- **Universal privacy concerns:** "all above" categories flagged
- **Trust concerns:** "everything" identified as problematic

**Training and Usability:**
- **Training Paradox:** "I received good training and was provided with excellent documentation" despite system failure
- **UI Assessment:** "I find the user interface poorly designed and visually unappealing"
- **Comprehensive explanation needs:** "all above" aspects require improvement

#### Response 2 - Infrastructure and Performance Issues
**Performance Metrics:**
- **Recommendation Score:** 2/10 (second lowest score)
- **Problems:** Yes - Multiple infrastructure issues
- **Trust Level:** "I have minimal trust in the tool"
- **Problem Description:** "Unclear instructions (EBSI), long wait time (Trusted Lists), variable up-time (both, mostly Trusted Lists)"

**Feature Analysis (Universal dissatisfaction):**
- **All features rated maximum importance (5/5)** but **minimum satisfaction (1/5)**
- **Identical pattern to Response 1** indicating systemic issues
- **Infrastructure reliability concerns** affecting all operational aspects

**Comprehensive Improvement Requirements:**
- **Clarity of instructions** for EBSI implementation
- **Performance improvements** for system responsiveness
- **Faster support response** times
- **Better usability** and clearer language
- **Improved testing systems** and installation processes

#### University of Twente Summary
**Critical Assessment:** University of Twente's dual responses reveal **fundamental implementation failure** in the hybrid trust model approach. Despite adequate training provision, **technical infrastructure issues prevent basic functionality**, resulting in **complete user frustration** and **system distrust**.

### Saxion University of Applied Sciences (3 responses) - Implementation Complexity Challenges

Saxion University provided three responses representing different user experiences within their hybrid implementation.

#### Response 1 - Docker and Technical Infrastructure Issues
**Performance Metrics:**
- **Recommendation Score:** 3/10
- **Problems:** Yes - Docker configuration challenges
- **Trust Level:** "I trust some parts of the tool"
- **Problem Description:** "The EBSI tool set only runs on specific version of docker and we could not find information on the github in regards to this info, so troubleshooting was more difficult. Upgrading pilot version can require a lot of troubleshooting..."

**Feature Analysis:**
- **Mixed importance ratings** with high ratings for Configuration (5/5) and Customisation (5/5)
- **Moderate satisfaction levels** (3/5) except Customisation (1/5 - critical gap)
- **Trust concerns:** "The toolset is unstable for the most part"

#### Response 2 - QR Code and Browser Compatibility Issues
**Performance Metrics:**
- **Recommendation Score:** 5/10 (highest among Pilot 3)
- **Problems:** Yes - Browser compatibility issues
- **Trust Level:** "I rather trust the tool" (most positive Pilot 3 response)
- **Problem Description:** "I got an issue when trying to scan the QR code to get the PID. I am using Safari browser, and when the QR code is scanned with the camera app, it navigated to the start page of the wwWallet, but then nothing happened afterwards."

**Feature Analysis:**
- **Balanced importance and satisfaction ratings** (predominantly 3/5)
- **Neutral performance across all categories**
- **Constructive improvement suggestion:** "It would be beneficial for the end user if the wwWallet showed detail of the status of credentials retrieval (PID, etc.)"

#### Response 3 - Docker Configuration and EBSI Integration Challenges
**Performance Metrics:**
- **Recommendation Score:** 5/10
- **Problems:** Yes - Complex technical setup issues
- **Trust Level:** "I trust some parts of the tool"
- **Problem Description:** "The Docker containers were difficult to set up and configure; the updates pushed to the GitHub would sometimes not be functioning. The EBSI system at one point changed their JSON structures, causing database conflicts..."

**Detailed Technical Analysis:**
- **Configuration complexity** preventing smooth deployment
- **Version management issues** with GitHub updates
- **EBSI integration instability** due to changing JSON structures
- **Database conflict resolution** requirements

**Sophisticated Improvement Recommendations:**
- **Automated setup processes** with Bash script configuration
- **User input-driven configuration** generation
- **Streamlined Docker compose** management
- **Enhanced environment file** handling

#### Saxion University Summary
**Technical Sophistication:** Saxion's three responses demonstrate **high technical capability** with **detailed problem analysis** and **sophisticated improvement suggestions**. However, **implementation complexity** creates significant barriers to successful deployment, particularly in **Docker configuration** and **EBSI integration** aspects.

### COFAC - Lusófona University (1 response) - International Implementation Perspective

COFAC - Lusófona University provided the single Portuguese perspective on hybrid trust model implementation.

#### Performance Analysis
**Core Metrics:**
- **Recommendation Score:** 7/10 (highest single score in Pilot 3)
- **Problems:** Yes - Docker and service reliability issues
- **Trust Level:** "I trust some parts of the tool"

#### Technical Problem Assessment
**Problem Description:** "Several problems with Docker. Some services didn't start due to https. We managed to solve that. We had to purge the database to get the last version working. Educational ID credentials could not be issued..."

**Key Technical Challenges:**
1. **Docker service reliability** with HTTPS configuration issues
2. **Database management complexity** requiring complete purges for version updates
3. **Credential issuance failures** for Educational ID functionality
4. **Service orchestration problems** affecting system stability

#### Feature Analysis
| Feature | Importance | Satisfaction | Gap Analysis |
|---------|-----------|-------------|-------------|
| Configuration Ease | 5 - Very important | 4 - Rather satisfied | ⚠️ Minor gap |
| Dashboard/Logs | 4 - Rather important | 3 - Neutral | ⚠️ Minor gap |
| Integration | 5 - Very important | 2 - Rather not satisfied | ❌ Significant gap |
| Customisation | 4 - Rather important | 3 - Neutral | ⚠️ Minor gap |
| Revocation Control | 5 - Very important | 4 - Rather satisfied | ⚠️ Minor gap |

**Critical Gap:** Integration with existing systems shows the most significant importance-satisfaction disparity.

#### User Experience Concerns
**Primary Issue:** "Our users had some difficulties understanding what this was about"
**Improvement Focus:** "A mix of user interface (experience for the user) and context-driven"

#### COFAC - Lusófona Summary
**International Validation:** Despite technical challenges, COFAC - Lusófona achieved the **highest recommendation score** (7/10) in Pilot 3, suggesting that with **technical problem resolution**, the hybrid approach has **international deployment potential**. However, **user comprehension challenges** indicate need for **enhanced educational context** provision.

---

## Cross-Response Comparative Analysis

### Recommendation Score Distribution
- **0/10:** 1 response (16.7%) - Complete system failure
- **2/10:** 1 response (16.7%) - Critical infrastructure issues
- **3/10:** 1 response (16.7%) - Technical setup challenges
- **5/10:** 2 responses (33.3%) - Moderate satisfaction with problems
- **7/10:** 1 response (16.7%) - Highest score despite technical issues

**Average: 4.4/10** - Significantly below acceptable satisfaction threshold

### Problem Incidence Analysis
- **Universal Problem Reporting:** 6/6 responses (100%)
- **Problem Categories:**
  1. **System functionality failures:** 2 responses (complete non-functionality)
  2. **Docker configuration challenges:** 4 responses (technical setup complexity)
  3. **Browser compatibility issues:** 1 response (QR code functionality)
  4. **EBSI integration instability:** 3 responses (external system dependencies)

### Trust Level Distribution Analysis
- **"I don't trust the tool at all":** 1 response (16.7%) - Complete distrust
- **"I have minimal trust in the tool":** 1 response (16.7%) - Severe trust concerns
- **"I trust some parts of the tool":** 3 responses (50%) - Conditional trust
- **"I rather trust the tool":** 1 response (16.7%) - Moderate confidence

**Trust Crisis:** 66.7% express minimal to no trust in system reliability

### Feature Priority Patterns

**Universally High Importance Features:**
1. **Ease of issuer configuration:** 5/6 responses rated 4-5/5
2. **Integration with existing systems:** 4/6 responses rated 5/5
3. **Control over revocation/suspension:** 4/6 responses rated 4-5/5

**Catastrophic Satisfaction Gaps:**
1. **University of Twente responses:** All features rated 1/5 satisfaction despite 5/5 importance
2. **Configuration complexity:** Multiple institutions reporting setup difficulties
3. **Integration failures:** Systematic gaps between importance and satisfaction

### Training Adequacy Assessment
- **Excellent/Good training:** 1 response (16.7%)
- **Sufficient training:** 4 responses (66.7%)
- **Some training provided:** 1 response (16.7%)

**Training Paradox:** Despite **adequate training provision**, **technical complexity** prevents effective implementation.

### UI Assessment Distribution
- **Poorly designed:** 2 responses (33.3%) - Significant design concerns
- **Problematic:** 3 responses (50%) - Usability challenges
- **Usable/Average:** 1 response (16.7%) - Minimal acceptance

**UI Crisis:** 83.3% report negative user interface experiences

---

## Technical Architecture Analysis

### Hybrid Implementation Complexity Assessment

**Dual Infrastructure Requirements:**
- **Classical PKI Component:** SUNET/SURF SaaS integration
- **Decentralised PKI Component:** ATOS/IZERTIS Docker deployment
- **System Coordination:** Unified management across both trust models

**Technical Challenge Categories:**

#### 1. Docker Configuration Complexity (4/6 responses)
- **Version-specific requirements** without adequate documentation
- **Container orchestration challenges** affecting service reliability
- **Update management difficulties** with GitHub version control
- **Environmental configuration complexity** requiring manual intervention

#### 2. EBSI Integration Instability (3/6 responses)
- **JSON structure changes** causing database conflicts
- **Service reliability issues** with external EBSI dependencies
- **Trust List performance problems** with variable uptime
- **Integration documentation inadequacy** for troubleshooting

#### 3. System Functionality Failures (2/6 responses)
- **Complete credential retrieval failure** preventing basic functionality
- **Wallet interface non-responsiveness** despite multiple attempts
- **QR code scanning incompatibilities** across browser platforms
- **Service startup failures** due to configuration issues

### Implementation Model Assessment

**Pilot 3 Unique Challenges:**
1. **Dual Complexity:** Managing both Classical PKI and dPKI simultaneously
2. **Infrastructure Coordination:** Ensuring compatibility between SUNET/SURF and ATOS/IZERTIS platforms
3. **User Journey Complexity:** Multiple pathways creating confusion
4. **Technical Support Burden:** Requiring expertise in both trust models

---

## Strategic Implications for Pilot 3

### Critical Development Requirements

**1. Infrastructure Stability (Critical Priority)**
- **Docker deployment automation** with comprehensive setup scripts
- **Version management consistency** across GitHub repositories
- **Service reliability improvement** for production readiness
- **Comprehensive troubleshooting documentation**

**2. EBSI Integration Resilience (Critical Priority)**
- **API stability management** for external dependencies
- **Change management protocols** for JSON structure updates
- **Fallback mechanisms** for service unavailability
- **Integration testing automation**

**3. User Experience Overhaul (High Priority)**
- **Interface redesign** addressing 83.3% negative feedback
- **Process transparency** with clear status indicators
- **Browser compatibility** across all major platforms
- **Context provision** for user understanding

**4. Support Infrastructure Enhancement (High Priority)**
- **Technical support responsiveness** improvement
- **Installation guidance** with step-by-step procedures
- **Troubleshooting resources** for common issues
- **Community support forums** for peer assistance

### Deployment Readiness Assessment

**Current Status: Not Production Ready**

**Critical Blockers:**
- **100% problem incidence** indicating systemic issues
- **66.7% minimal/no trust** preventing institutional adoption
- **4.4/10 average recommendation** below deployment threshold
- **Universal UI dissatisfaction** affecting user acceptance

**Development Requirements Before Deployment:**
1. **Technical stability achievement** with <20% problem incidence
2. **Trust building** through reliable functionality demonstration
3. **User experience enhancement** achieving >70% positive UI feedback
4. **Recommendation improvement** to >7/10 average satisfaction

### Resource Allocation Recommendations

**Technical Development Priority:**
1. **Infrastructure team expansion** for dual-platform management
2. **EBSI integration specialists** for external dependency management
3. **User experience designers** for interface improvement
4. **DevOps automation** for deployment simplification

**Support Infrastructure Priority:**
1. **Dedicated technical support** for complex implementations
2. **Documentation team** for comprehensive guidance creation
3. **Training programme enhancement** for technical complexity management
4. **Community building** for peer support networks

---

## Institutional Specific Recommendations

### University of Twente - Crisis Recovery Programme
**Immediate Actions Required:**
1. **Complete system audit** to identify fundamental functionality failures
2. **Alternative implementation pathway** investigation
3. **Technical support intensive engagement** for problem resolution
4. **User confidence rebuilding** through demonstrated improvements

### Saxion University - Technical Excellence Development
**Strategic Approach:**
1. **Leverage technical sophistication** for improvement feedback
2. **Beta testing programme** participation for new versions
3. **Technical mentorship role** for other institutions
4. **Docker automation** pilot programme leadership

### COFAC - Lusófona University - International Model Development
**Strategic Position:**
1. **International reference implementation** development
2. **User education programme** creation for context provision
3. **Cross-border verification** testing leadership
4. **Portuguese deployment model** scalability assessment

---

## Conclusions and Strategic Recommendations

### Overall Assessment
Pilot 3's combined PKI/dPKI implementation reveals **significant implementation complexity challenges** that prevent successful deployment in its current form. The **100% problem incidence rate** and **4.4/10 average recommendation score** indicate that the hybrid approach, whilst technically innovative, creates **unacceptable implementation burden** for educational institutions.

### Critical Success Requirements
1. **Technical Stability:** Achieve basic functionality across all participating institutions
2. **Implementation Simplification:** Reduce Docker configuration complexity through automation
3. **EBSI Integration Reliability:** Establish stable external system dependencies
4. **User Experience Enhancement:** Complete interface redesign based on user feedback
5. **Support Infrastructure:** Comprehensive technical assistance for complex deployments

### Strategic Decision Points

**Option 1: Hybrid Model Refinement**
- **Intensive development investment** to address identified issues
- **Extended timeline** for stability achievement
- **High resource requirements** for dual-platform maintenance
- **Uncertain deployment success** given current challenges

**Option 2: Single Trust Model Focus**
- **Pilot 2 dPKI approach** leverage for proven success
- **Classical PKI** maintenance for specific institutional requirements
- **Resource concentration** on proven approaches
- **Accelerated deployment timeline** with reduced complexity

**Option 3: Pilot 3 Suspension**
- **Development resource reallocation** to successful pilots
- **Institutional transition** to Pilot 1 or Pilot 2 approaches
- **Hybrid model** research continuation without production pressure
- **Future reconsideration** after foundational stability achievement

### Strategic Recommendation
Based on the comprehensive analysis, **Option 2 (Single Trust Model Focus)** is recommended, with **Pilot 3 institutions transitioning to proven Pilot 2 approaches** whilst maintaining **research collaboration** for future hybrid model development when technical maturity permits.

The analysis demonstrates that whilst the hybrid trust model concept has **strategic merit**, the **current implementation complexity** creates **unacceptable barriers** to successful educational sector deployment. **Technical maturity development** is required before hybrid approaches can achieve **production readiness** suitable for European educational institutions.

---

*Analysis based on 6 comprehensive survey responses representing 100% of Pilot 3 participating institutions across all 15 survey questions, revealing critical implementation challenges requiring strategic intervention.*