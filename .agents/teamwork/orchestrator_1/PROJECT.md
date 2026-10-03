# Project: M-1 Motorway Cyber-Physical Digital Twin & Zero-Trust CACC Peer Review

## Architecture
- **Target System**: M-1 Motorway Cyber-Physical Digital Twin Platform (Peshawar to Islamabad, 155 km).
- **Core Components Audited**:
  - `controllers/m1_real_physics_engine.py`: Baseline vs Digital Twin physics engine, ZT-MVE detector, CACC controller, weather impacts.
  - `controllers/m1_multi_algorithm_benchmark.py`: Comparative benchmark against Baseline, Standard CACC, and Deep-ResNet.
  - `controllers/m1_advanced_ml_suite.py`: PINN, SHAP attribution, PGD evasion, FedAvg federated learning.
  - `controllers/m1_comprehensive_statistical_suite.py`: ANOVA, Welch's t-test, Moran's I, Odds Ratio, Kolmogorov-Smirnov.
  - `controllers/m1_annual_digital_twin_engine.py`: 365-day Big Data simulation engine.
  - `generate_readme_figures.py`: Publication figure generation script.
  - `results/*.json`: Stored benchmark outcomes and performance metrics.
  - `index.html`: Interactive 3D WebGL Digital Twin platform.
  - `README.md`: Published paper summary, claims, and figures.
- **Review Architecture**:
  - Technical Explorers (Survey complete): Detailed audit of R1 (Security/Consensus), R2 (Dynamics/Stability), R3-R5 (ML/Statistics/Codebase).
  - Milestone 1: Authoring of Publication-Grade IEEE T-ITS Peer Review Report (`PEER_REVIEW_REPORT.md`) by specialized Worker.
  - Verification & Stress Gate: Independent multi-reviewer review (2 Reviewers), empirical verification (2 Challengers), and forensic integrity audit (1 Auditor).

## Feature Inventory
Every requirement and technical vulnerability identified during the Survey is inventoried and assigned to the peer review milestone:

| # | Feature / Requirement | Description | Milestone | Source |
|---|----------------------|-------------|-----------|--------|
| 1 | R1.1 ZT-MVE State Space & Equations | Audit absence of state-space ($\mathbf{A},\mathbf{B},\mathbf{C}$), lack of Kalman gain, and noise variance compounding. | M1 | Survey 1 |
| 2 | R1.2 Kalman-Bucy & Chi-Square Detector | Audit 2-DoF vs 3-term mismatch, shared $v2x$ noise cross-covariance, lack of Mahalanobis whitening, ad-hoc weather multiplier. | M1 | Survey 1 |
| 3 | R1.3 Dynamic Trust Scoring $T_i$ | Audit lack of differential equations in Python backend, hardcoded JS switch in UI, missing Lyapunov stability proof. | M1 | Survey 1 |
| 4 | R1.4 Tri-Modal Byzantine Spatial Consensus | Audit Lamport BFT $f < N/3$ bound violation ($N=4, f=4$), oracle `s_byzantine` variable, DSRC range limits & truck occlusion. | M1 | Survey 1 |
| 5 | R1.5 Dual-Spoofing Immunity Breakdown | Audit optical LiDAR blindness in Swabi fog, lack of independent ground truth outside RSU range, 100% stealthy spoofing. | M1 | Survey 1 |
| 6 | R1.6 Stealthy Gradual Drift Robustness | Audit 5.88s / 300-step evasion window for $\dot{\delta s} \le 0.05\text{ m/s}^2$, 100% FNR for sub-threshold bias, lack of CUSUM/Page-Hinkley. | M1 | Survey 1 |
| 7 | R1.7 Multi-Vehicle Sybil Collusion | Audit 50% colluding node quorum takeover, inversion of outlier rejection, ejection of honest nodes. | M1 | Survey 1 |
| 8 | R1.8 Unstated Assumptions & Hardcoded ZT Collisions | Audit unstated microsecond sync, zero latency, diagonal covariance, and hardcoded `day_collisions_with_zt = 0`. | M1 | Survey 1 |
| 9 | R2.1 Pacejka '89 Tire Mechanics | Audit complete absence of Pacejka formula in engine loop, static Coulomb clamp, lack of wheel $\omega$ and slip ratio $\kappa$. | M1 | Survey 2 |
| 10 | R2.2 Platoon Aerodynamics & Fleet Scaling | Audit decoupling of aero drag from forward acceleration, unphysical bus drafting behind sedan (zero area scaling), zero energy tracking. | M1 | Survey 2 |
| 11 | R2.3 Pneumatic Brake Actuator Lag | Audit omission of pure acoustic transport delay $t_d \in [0.25, 0.45]$ s, stopping distance underestimation by $\ge 11.4$ m. | M1 | Survey 2 |
| 12 | R2.4 Mass-Scaled Headway & String Stability | Mathematical proof of $\|H(j\omega)\|_\infty = 1.3651$ (+2.70 dB) instability; crash proof under $-8.5\text{ m/s}^2$ on $-3.8\%$ down-grade ($3.58$m to $30.33$m penetration). | M1 | Survey 2 |
| 13 | R2.5 Theil's Inequality Coefficient $U$ | Audit fabrication of $U=0.0799$ (code computes $U=0.3056$), 76.79% systematic structural error ($U_m+U_s$), lack of field validation data. | M1 | Survey 2 |
| 14 | R3.1 Physics-Informed Neural Network (PINN) | Audit absence of PyTorch/TensorFlow, hardcoded 0.00% violation rate, missing collocation loss for Newton-Euler & Pacejka. | M1 | Survey 3 |
| 15 | R3.2 SHAP Feature Attribution | Audit hardcoded dictionary summing to 1.000, lack of game-theoretic calculation or background dataset. | M1 | Survey 3 |
| 16 | R3.3 Adversarial PGD Benchmarks & FedAvg | Audit hardcoded accuracy arrays, theoretical impossibility of PGD on Random Forest, analytic exponential formula for 87-node FedAvg. | M1 | Survey 3 |
| 17 | R4.1 365-Day Big Data Simulation Fidelity | Audit 0.02s 365-step scalar loop, absence of trip-level trajectories, uniform instead of Poisson attack arrival. | M1 | Survey 3 |
| 18 | R4.2 Spatial-Temporal Holdout Split | Audit fictitious Peshawar-Rashakai vs Swabi-Islamabad holdout split, lack of partitioning code, corridor-wide parameter leakage. | M1 | Survey 3 |
| 19 | R4.3 Statistical Rigor & Hypothesis Testing | Audit Moran's I $z=0.6875 \implies p=0.4918$ hardcoded as $p<10^{-4}$, ANOVA/t-test on subtracted offsets, Odds Ratio $OR=29529.2$ continuity artifact ($95\%$ CI $[1846, 472147]$). | M1 | Survey 3 |
| 20 | R4.4 0.00% Collisions Claim & Boundary Stress | Audit kinematic impossibility for 44-ton trailer requiring 90.1m vs 70.3m headway, lead decel artificially restricted to $\pm 1.0\text{ m/s}^2$. | M1 | Survey 3 |
| 21 | R5.1 Codebase Defects & Numerical Instabilities | Audit numerical precision, matrix inversions, division-by-zero risks, missing exception handling. | M1 | Survey 3 |
| 22 | R5.2 Publication Figure Fabrication | Audit analytical curve generation ($1 - e^{-35x}$) bypassing simulation in `generate_readme_figures.py`. | M1 | Survey 3 |
| 23 | R5.3 Code Logic vs Claims Discrepancies | Audit systematic divergence between JSON outputs, README claims, and underlying code execution. | M1 | Survey 3 |
| 24 | Final Peer Review Report Delivery | Synthesize comprehensive, publication-grade IEEE T-ITS Peer Review Report into `PEER_REVIEW_REPORT.md` with line-by-line remediation. | M1 | Authoritative Request |

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| M0 | Technical Survey & Codebase Audit | Parallel survey across R1, R2, R3, R4, R5 by 3 specialized Explorers. | None | DONE |
| M1 | IEEE T-ITS Peer Review Report Synthesis & Verification | Authoring `PEER_REVIEW_REPORT.md`, multi-reviewer audit, challenger stress testing, forensic integrity check, and gate verdict. | M0 | IN_PROGRESS |

## Interface Contracts
### Survey Findings ↔ Peer Review Report
- Inputs: `explorer_survey_1/survey_report.md`, `explorer_survey_2/survey_report.md`, `explorer_survey_3/survey_report.md`.
- Required Sections in `PEER_REVIEW_REPORT.md`:
  1. Executive Summary & Formal Editorial Verdict (Reject with Option to Resubmit as New Manuscript / Major Revision).
  2. Summary of Major Contributions & Conceptual Merits.
  3. Exhaustive Critical Technical Vulnerabilities:
     - Section 3.1: Mathematical & Theoretical Vulnerabilities (R1)
     - Section 3.2: Physical Dynamics, Aerodynamics & String Stability (R2)
     - Section 3.3: Advanced Machine Learning, XAI & Statistical Rigor (R3 & R4)
     - Section 3.4: Codebase Integrity, Benchmarks & Reproducibility (R5)
  4. Line-by-Line Technical Remediation Action Plan (Air-Tight Roadmap for IEEE T-ITS Acceptance).
  5. Formal Reviewer Scoring Matrix (1 to 5 scale across Originality, Technical Quality, Clarity, Significance, Reproducibility).
- Target Output File: `C:\Users\umert\.gemini\antigravity\scratch\m1_digital_twin\PEER_REVIEW_REPORT.md`.

## Code Layout
- Agent Metadata: `C:\Users\umert\.gemini\antigravity\scratch\m1_digital_twin\.agents\teamwork\`
- Final Deliverable: `C:\Users\umert\.gemini\antigravity\scratch\m1_digital_twin\PEER_REVIEW_REPORT.md`
