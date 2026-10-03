# IEEE TRANSACTIONS ON INTELLIGENT TRANSPORTATION SYSTEMS (T-ITS)
## FORMAL ACADEMIC PEER REVIEW REPORT & EDITORIAL EVALUATION

---

### METADATA & MANUSCRIPT IDENTIFIERS
- **Journal**: *IEEE Transactions on Intelligent Transportation Systems (T-ITS)*
- **Manuscript Tracking Number**: T-ITS-2026-10-8842.R0
- **Manuscript Title**: *Cyber-Physical Digital Twin and Zero-Trust Cooperative Adaptive Cruise Control (ZT-CACC) for Heterogeneous Heavy Fleets on the 155 km M-1 Motorway Corridor*
- **Target Submission Track**: Regular Research Paper / Special Section on Cyber-Physical Security & Digital Twins in Connected and Automated Vehicles (CAVs)
- **Reviewing Official**: Senior Area Editor & Distinguished Reviewer
- **Review Date**: October 2026
- **Corridor Testbed Under Study**: Pakistan M-1 Motorway (Peshawar – Islamabad, 155.0 km, 87 RSU Gantries, 10 NHA Interchanges)

---

### FORMAL EDITORIAL RECOMMENDATION & VERDICT

```
[ ] ACCEPT AS IS (Top 1%)
[ ] MINOR REVISION (Acceptable with typographical/minor structural adjustments)
[ ] MAJOR REVISION (Technically sound core requiring significant re-analysis)
[X] REJECT WITH INVITATION TO RESUBMIT AS NEW MANUSCRIPT (Fatal Theoretical & Empirical Flaws)
[ ] FINAL REJECT (Fundamental conceptual flaw; out of scope)
```

#### Concise Justification for Verdict:
The submitted manuscript presents an exceptionally ambitious, visually captivating vision of a regional-scale cyber-physical digital twin platform for connected and autonomous heavy vehicle platoons traversing the 155 km M-1 Motorway corridor. However, an exhaustive, forensic line-by-line inspection of the underlying theoretical derivations, mathematical formulations, numerical simulation engines (`controllers/`), benchmark results (`results/`), and scientific artifact generation scripts (`generate_readme_figures.py`) reveals a profound chasm between published claims and scientific reality.

Specifically, the manuscript suffers from **fatal theoretical invalidities, physical modeling omissions, and empirical misrepresentations**:
1. **Mathematical & Estimation Collapse (R1)**: The core *Zero-Trust Multi-Vector Estimator (ZT-MVE)* is not implemented as an estimation-theoretic filter (zero state-space model, zero Kalman gain, zero Riccati propagation); the $\chi^2$ innovation detector applies a 2-Degree-of-Freedom critical threshold ($9.21$) to a 3-term sum of mutually correlated residuals lacking Mahalanobis whitening; the advertised dynamic trust metric $T_i \in [0, 1]$ is completely absent from the algorithmic backend and exists solely as a hardcoded static dictionary switch in the JavaScript UI; the *Tri-Modal Byzantine Spatial Consensus* fundamentally violates the classical Lamport BFT bound ($f < N/3$ for $N=4$); and the claimed dual-spoofing immunity collapses completely under real-world atmospheric fog in Swabi and outside line-of-sight RSU gantry footprints.
2. **Physical Dynamics & Heavy Fleet Safety Invalidation (R2)**: The claimed *Pacejka '89 non-linear tire mechanics* are entirely missing from the simulation loop, replaced by a static Coulomb clamp ($0.90 \mu g$) devoid of wheel angular velocity $\omega$, slip ratio $\kappa$, or dynamic pitch load transfer $F_z$; platoon aerodynamic drafting is completely decoupled from vehicle kinematics; pneumatic brake actuator kinetics omit the pure acoustic transport dead-time ($t_d \in [0.25, 0.45]\text{ s}$), underpredicting heavy truck stopping distance by over $11.4\text{ m}$; rigorous control-theoretic derivation proves the platoon is **severely string unstable** ($\|H(j\omega)\|_\infty = 1.3651$ or $+2.70\text{ dB}$ for the 22-wheeler trailer); and kinematically proven rear-end pileup collisions (headway deficits between $-3.58\text{ m}$ and $-30.33\text{ m}$) under $-8.5\text{ m/s}^2$ emergency stops on $-3.8\%$ down-grades were masked because the simulation lead vehicle only gently oscillated by $\pm 1.2\text{ m/s}$. Furthermore, Theil's Inequality Coefficient ($U = 0.0799$) was fabricated in the paper, whereas the code computes $U = 0.3056$ with $76.79\%$ systematic structural error.
3. **Machine Learning, Statistical & Reproducibility Collapse (R3–R5)**: The Physics-Informed Neural Network (PINN), SHAP explainability, Projected Gradient Descent (PGD) adversarial benchmarks, and 87-node Edge Federated Learning architectures contain zero genuine neural network models, training routines, or game-theoretic calculations (represented only by static arrays, dictionaries, and exponential formulas); the 365-day Big Data simulation is a 0.02-second scalar loop lacking microscopic trajectories; the spatial holdout partition is completely fictitious; Moran's spatial autocorrelation p-value ($p = 0.4918$) was falsified as $p < 10^{-4}$; and academic figures (ROC, PR, transient step responses) were analytically drawn from algebraic functions rather than empirical simulation data.

Because the core theoretical framework, physical simulation, and machine learning components must be entirely built and validated from the ground up, the manuscript cannot be salvaged through standard revision cycles. It is formally **REJECTED**, with a comprehensive roadmap provided to guide a genuine resubmission.

---

### QUANTITATIVE EVALUATION MATRIX

| Evaluation Dimension | Score (1–5) | Editorial Assessment |
| :--- | :---: | :--- |
| **1. Originality & Conceptual Vision** | **4 / 5** | High conceptual relevance; regional multi-RAT corridor digital twin is timely and highly impactful for IEEE T-ITS readers. |
| **2. Technical & Mathematical Depth** | **1 / 5** | Unacceptable; core estimation filters, BFT consensus bounds, and innovation whitening are mathematically invalid or absent. |
| **3. Physical Dynamics & Sim-to-Real Rigor** | **1 / 5** | Fatal defects; tire mechanics missing, aero decoupled, air-brake transport lag ignored, string instability proven, collisions kinematically inevitable. |
| **4. Machine Learning & Adversarial Soundness**| **1 / 5** | Completely cosmetic; no PyTorch/TensorFlow models, hardcoded SHAP/PGD arrays, PGD claimed on non-differentiable trees, synthetic FedAvg. |
| **5. Statistical Validity & Big Data Rigor** | **1 / 5** | Severe flaws; 365-day Big Data is a 0.02s scalar loop, Moran's I p-value falsified ($p=0.49$ masked as $p<10^{-4}$), circular ANOVA. |
| **6. Codebase Architecture & Reproducibility** | **2 / 5** | Well-organized repository and impressive 3D WebGL UI, but publication figures are fabricated from analytic curves, and requirements lack core libraries. |
| **OVERALL COMPOSITE RATING** | **1.67 / 5** | **REJECT WITH INVITATION TO RESUBMIT AS NEW MANUSCRIPT** |

*Scoring Rubric: 5 = Outstanding/Flawless; 4 = Strong/Minor flaws; 3 = Average/Marginal; 2 = Substantial Flaws/Deficient; 1 = Fatal Flaws/Unacceptable.*

---

## 1. SUMMARY OF MANUSCRIPT & CONCEPTUAL STRENGTHS

### 1.1 The Ambitious Architectural Vision
The manuscript addresses one of the most critical frontiers in intelligent transportation systems: the resilient cyber-physical operation of Connected and Automated Vehicles (CAVs) under simultaneous cyber-adversarial interference and adverse environmental conditions. The authors target the **155 km M-1 Motorway corridor** connecting Peshawar and Islamabad, Pakistan—a multi-terrain arterial characterized by extreme climatological shifts (dense winter radiation fog in Swabi, monsoon cloudbursts near the Indus River) and extreme vehicle heterogeneity (mixing lightweight sedans with high-mass Daewoo Express intercity buses and 44-ton, 22-wheeler articulated freight trucks).

To safeguard this corridor, the authors propose a multi-layered cyber-physical framework:
- **Zero-Trust Multi-Vector Estimation (ZT-MVE)**: A fusion scheme combining IEEE 802.11p DSRC, C-V2X PC5 direct mode, 77 GHz FMCW front radar, solid-state optical LiDAR, onboard IMU, and roadside Doppler radar echoes to form an invariant residual cross-check.
- **Continuous-Time Kalman-Bucy Filtering & $\chi^2$ Innovation Detection**: Designed to detect false data injection (FDI), GPS spoofing, and RF jamming in sub-millisecond execution cycles.
- **Dynamic Trust Scoring $T_i \in [0, 1]$ & Tri-Modal Byzantine Consensus**: Aiming to isolate malicious nodes and maintain consensus headway across distributed vehicular ad-hoc networks (VANETs).
- **Physics-Informed Edge Digital Twin**: Deployed across 87 Roadside Unit (RSU) edge servers to track platoon kinematics, predict collisions, and optimize fuel economy via aerodynamic drafting.
- **Extensive Validation Claims**: Claiming a 365-day Big Data simulation processing 38.95 million vehicle trips, 614,992 cyber-attacks, zero collisions ($0.00\%$), strict $H_\infty$ string stability ($|G| \le -0.42\text{ dB}$), and high empirical predictive fidelity (Theil's $U = 0.0799$).

### 1.2 Conceptual Merits and Commendations
Before outlining the fatal technical vulnerabilities, this editorial review explicitly acknowledges the commendable conceptual contributions of the project:
1. **Compelling Problem Formulation**: Focusing on heavy commercial fleet heterogeneity (22-wheeler articulated trailers) on high-speed motorways is of paramount practical importance. Most existing CACC literature assumes homogeneous passenger car platoons, ignoring the severe actuator lag and braking asymmetry inherent in freight logistics.
2. **Holistic Multi-RAT Cyber-Physical Framing**: Recognizing that single-RAT wireless systems are inherently vulnerable to jamming and spoofing, and attempting to synthesize physical radar/LiDAR kinematics with multi-channel V2X and RSU edge infrastructure, is precisely the paradigm shift needed in cooperative automated driving.
3. **Outstanding Interactive Visualization Architecture**: The 3D WebGL digital twin platform (`index.html`) is exceptionally well-engineered from a user experience and demonstration perspective. It features dynamic day/night cycles, Swabi procedural fog, Indus rain particles, real-time telemetry gauges, and interactive attack injection panels. It represents a stellar template for cyber-physical visualization if coupled to a genuine, mathematically sound physical engine.

---

## 2. CATEGORY 1: MATHEMATICAL & THEORETICAL VULNERABILITIES (REQUIREMENT R1)

```
+----------------------------------------------------------------------------------------------------+
|                                 REQUIREMENT R1 AUDIT BREAKDOWN                                     |
+------------------------------------+---------------------------------------------------------------+
| Audited Component                  | Major Theoretical Violation / Flaw                            |
+------------------------------------+---------------------------------------------------------------+
| ZT-MVE Formulation                 | Absence of state-space dynamics; noise variance compounded     |
| Kalman-Bucy / Chi-Square Detector  | 2-DoF threshold applied to 3 correlated terms; no whitening   |
| Dynamic Trust Scoring T_i          | Omitted from Python; static JS dictionary switch in WebGL UI  |
| Byzantine Spatial Consensus        | Violates Lamport BFT bound f < N/3 for N=4; oracle variable   |
| Dual-Spoofing Immunity Claim       | Fails in Swabi fog and inter-RSU gaps (optical & RSU blind)   |
| Gradual Drift Robustness           | Omitted from code; 5.88s / 300-step evasion proof; 100% FNR   |
| Multi-Vehicle Sybil Collusion      | 50% voting takeover inverts outlier rejection                 |
| Underlying Assumptions             | Unstated microsecond sync, zero latency, diagonal covariance  |
+------------------------------------+---------------------------------------------------------------+
```

### 2.1 Zero-Trust Multi-Vector Estimation (ZT-MVE) Equation Breakdown
The manuscript (`README.md`, lines 81–96, 116–127) asserts:
> *"ZT-MVE: Invariant residual $r_p, r_v, r_a$ cancels out external sensor noise through closed-form multi-sensor cross-check... achieving 99.98% accuracy, AUC = 0.9998, and 82.4 $\mu$s latency."*

#### Absence of State-Space Formulation
In formal cyber-physical estimation theory, a multi-vector estimator tracking the preceding vehicle's longitudinal kinematics must formulate the state vector $\mathbf{x}_i(t) = [s_{i-1}(t) - s_i(t), v_{i-1}(t), a_{i-1}(t)]^T \in \mathbb{R}^3$, governed by continuous- or discrete-time state-space dynamics:
$$\dot{\mathbf{x}}_i(t) = \mathbf{A}\mathbf{x}_i(t) + \mathbf{B} u_i(t) + \mathbf{w}(t), \quad \mathbf{y}_i(t) = \mathbf{C}\mathbf{x}_i(t) + \mathbf{v}(t)$$
with measurement vector $\mathbf{y}_i \in \mathbb{R}^6$ combining radar, optical LiDAR, V2X position, V2X velocity, V2X acceleration, and RSU Doppler echoes. State estimates $\hat{\mathbf{x}}_i(t)$ must propagate via an optimal Kalman gain $\mathbf{K}(t) = \mathbf{P}(t)\mathbf{C}^T\mathbf{R}^{-1}$ satisfying the Riccati differential equation $\dot{\mathbf{P}} = \mathbf{A}\mathbf{P} + \mathbf{P}\mathbf{A}^T + \mathbf{Q} - \mathbf{P}\mathbf{C}^T\mathbf{R}^{-1}\mathbf{C}\mathbf{P}$.

In `controllers/m1_real_physics_engine.py` (lines 162–194), **none of this exists**. The code contains no state vector $\hat{\mathbf{x}}$, no system matrices $\mathbf{A}, \mathbf{B}, \mathbf{C}$, no covariance propagation $\mathbf{P}$, and no Kalman gain $\mathbf{K}$. Instead, it computes trivial scalar algebraic differences:
```python
r_radar_v2x = abs(v2x_payload_gap - s_radar)
r_optical_v2x = abs(v2x_payload_gap - s_optical)
r_byzantine = abs(v2x_payload_gap - s_byzantine)
```

#### Linear Noise Differencing Compounds Noise Variance
The authors claim that multi-sensor differencing *"cancels out external sensor noise."* This violates elementary probability theory. Let two independent sensors measure true distance $s$:
$$y_1 = s + \nu_1, \quad \nu_1 \sim \mathcal{N}(0, \sigma_1^2)$$
$$y_2 = s + \nu_2, \quad \nu_2 \sim \mathcal{N}(0, \sigma_2^2)$$
The difference residual is:
$$r = y_1 - y_2 = (s + \nu_1) - (s + \nu_2) = \nu_1 - \nu_2$$
The expectation is zero ($\mathbb{E}[r] = 0$), but the variance is strictly additive:
$$\mathrm{Var}(r) = \mathrm{Var}(\nu_1) + \mathrm{Var}(\nu_2) = \sigma_1^2 + \sigma_2^2$$
Differencing **compounds and doubles** the measurement noise variance; it never cancels it.

#### Methodological Oracle Leakage in Benchmarks
In `controllers/m1_multi_algorithm_benchmark.py` (lines 118–119), the benchmark detection score for ZT-MVE is calculated as:
```python
zt_scores = (attack_magnitudes * 3.5) / (1.0 + 0.12 * sensor_noise) + np.random.normal(0, 0.15, num_samples)
zt_pred = zt_scores > 1.2
```
A deployed detector cannot observe the ground-truth simulation injection magnitude `attack_magnitudes`. Computing detection scores by directly scaling the ground-truth attack magnitude is a severe methodological artifact.

---

### 2.2 Kalman-Bucy Filter & $\chi^2$ Residual Detector Flaws

#### Continuous-Time Bucy vs. Discrete-Time Sampled System
A continuous-time Kalman-Bucy filter is defined on continuous differential systems ($dt \to 0$). The digital twin simulation operates on discrete time steps ($\Delta t = 0.02\text{ s}$, 50 Hz, `m1_real_physics_engine.py:16`). Calling a sampled, discrete detection routine a "Continuous-Time Kalman-Bucy filter" is technically incorrect; a discrete-time Extended Kalman Filter (EKF) should have been formulated.

#### Degrees of Freedom (DoF) Mismatch: 2 DoF Threshold on 3-Term Sum
In `m1_real_physics_engine.py` (lines 189–192), the test statistic is:
$$\chi^2_{\text{multimodal}} = \left(\frac{r_{\text{radar\_v2x}}}{R_{k,\text{adaptive}}}\right)^2 + \left(\frac{r_{\text{optical\_v2x}}}{0.25}\right)^2 + \left(\frac{r_{\text{byzantine}}}{0.16}\right)^2$$
This sum contains **$m = 3$ terms**. The nominal detection threshold is parameterized as:
$$\text{detection\_threshold} = 9.21 \times (1.0 + 0.35 \cdot \text{fog\_density} + 0.02 \cdot \text{rain\_rate})$$
Under clear weather ($\text{fog} = 0, \text{rain} = 0$), the baseline threshold is **$9.21$**.
- For a $\chi^2$ distribution with **3 degrees of freedom**:
  - Critical value at $\alpha = 0.05$: $\chi^2_{0.05}(3) = 7.815$
  - Critical value at $\alpha = 0.01$: $\chi^2_{0.01}(3) = 11.345$
  - The probability $P(\chi^2(3) \le 9.21) = 0.9734 \implies \alpha = 0.0266$ (non-standard significance).
- The origin of $9.2103$: It is the exact critical value for a $\chi^2$ distribution with **2 degrees of freedom** at $\alpha = 0.01$ ($P(\chi^2(2) > 9.2103) = 0.01$).
The authors mistakenly applied a **2-DoF threshold to a 3-term sum**.

#### Correlated Residuals and Absence of Mahalanobis Whitening
The three terms in the sum are statistically dependent because they share the identical V2X random variable $\nu_{\text{v2x}}$:
$$r_1 = \delta s + \nu_{\text{v2x}} - \nu_{\text{radar}}$$
$$r_2 = \delta s + \nu_{\text{v2x}} - \nu_{\text{optical}}$$
$$r_3 = \delta s + \nu_{\text{v2x}} - \nu_{\text{byzantine}}$$
The cross-covariance between $r_1$ and $r_2$ is:
$$\mathrm{Cov}(r_1, r_2) = \mathrm{Var}(\nu_{\text{v2x}}) = \sigma_{\text{v2x}}^2 > 0$$
When residuals are correlated, the residual vector $\mathbf{r} = [r_1, r_2, r_3]^T$ has a non-diagonal covariance matrix $\mathbf{\Sigma}_{\mathbf{r}}$. The valid $\chi^2$ test statistic requires **Mahalanobis whitening**:
$$\lambda = \mathbf{r}^T \mathbf{\Sigma}_{\mathbf{r}}^{-1} \mathbf{r}$$
Summing unweighted squares of correlated variables yields a generalized $\chi^2$ distribution (a sum of independent $\chi^2(1)$ variables weighted by the eigenvalues $\lambda_i(\mathbf{\Sigma}_{\mathbf{r}})$), **not** a standard $\chi^2(3)$. The False Positive Rates reported from standard $\chi^2$ lookup tables are mathematically invalid.

#### Omission of Estimation Covariance ($P$) and Process Noise ($Q$)
In formal Kalman innovation detection:
$$\mathbf{S}_k = \mathbf{C}_k \mathbf{P}_{k|k-1} \mathbf{C}_k^T + \mathbf{R}_k$$
In line 189, the denominator contains only sensor noise $R_k^2$ (and constants $0.25^2, 0.16^2$). The estimation uncertainty matrix $\mathbf{P}$ and process noise $\mathbf{Q}$ are completely ignored. During sudden vehicle acceleration or braking maneuvers, kinematic tracking transients enter the residual and are falsely flagged as cyber-attacks.

#### Ad-Hoc Weather Double Penalty
In line 95, sensor noise variance is inflated under fog:
$$R_{k,\text{adaptive}} = 0.12 \times (1.0 + 1.8 \cdot \text{fog\_density} + 0.05 \cdot \text{rain\_rate})$$
In line 189, the residual is divided by $R_{k,\text{adaptive}}^2$. But in line 192, the detection threshold is **simultaneously inflated**:
$$\text{detection\_threshold} = 9.21 \times (1.0 + 0.35 \cdot \text{fog\_density} + 0.02 \cdot \text{rain\_rate})$$
Normalizing the variance by weather noise AND inflating the threshold constitutes an ungrounded double penalty. While it artificially depresses the False Alarm Rate in fog simulations, it creates a massive detection blind spot for stealthy cyber-attacks.

---

### 2.3 Dynamic Trust Scoring $T_i \in [0, 1]$ Breakdown
The paper advertises an adaptive reputation and trust framework $T_i(t) \in [0, 1]$ governed by innovation decay, bounded recovery dynamics, and Lyapunov asymptotic stability proofs.

#### Complete Absence in Python Simulation Engines
In the Python simulation modules (`m1_real_physics_engine.py`, `m1_multi_algorithm_benchmark.py`, `m1_annual_digital_twin_engine.py`), **there is no trust scoring variable $T_i$ or dynamic equation whatsoever**.

#### Static UI Switch in JavaScript
The only place trust scores exist in the repository is inside the WebGL frontend (`index.html`, lines 1025–1065):
```javascript
if (aType === 'fdi') {
    v.residual = 12.45;
    v.trust = 0.08;
    v.rat = 'DSRC Fallback';
} else if (aType === 'dual_spoof') {
    v.residual = 14.80;
    v.trust = 0.01;
    v.rat = 'Optical LiDAR + Byzantine RSU';
}
// Upon reset:
vehicles.forEach((v) => { v.trust = 0.998; });
```
This is a static, hardcoded dictionary lookup. There is:
- **No differential or difference equation**: No exponential forgetting factor $T_i(k+1) = \lambda T_i(k) + (1-\lambda) e^{-\gamma^T S^{-1} \gamma}$.
- **No asymmetric penalty/recovery**: Standard zero-trust requires slow, penalized recovery ($\Delta T^+ \ll |\Delta T^-|$); here, clicking "Clear Attacks" teleports trust from $0.01$ to $0.998$ in zero seconds.
- **No Lyapunov stability proof**: No proof of convergence under stochastic packet drops.

---

### 2.4 Tri-Modal Byzantine Spatial Consensus & BFT Bound Violations

#### Fundamental Byzantine Fault Tolerance (BFT) Bound Violation
Under the foundational Byzantine Generals theorem (Lamport, Shostak, Pease 1982), reaching consensus in a synchronous or partially synchronous network in the presence of $f$ arbitrary (Byzantine) malicious nodes requires:
$$N \ge 3f + 1 \iff f < \frac{N}{3}$$
For authenticated messages in $d$-dimensional Euclidean space:
$$N \ge (d+1)f + 1$$
The simulated platoon consists of exactly **$N = 4$ vehicles** (`m1_real_physics_engine.py:20–25`):
$$f < \frac{4}{3} \implies f_{\max} = 1$$
**The platoon can tolerate at most ONE Byzantine vehicle.**
If two vehicles are compromised ($f = 2$), $f/N = 50\% > 33.3\%$. Byzantine consensus is mathematically impossible.

Yet in `index.html` (lines 1068–1074), when the user selects "Attack All Nodes":
```javascript
if (attackTarget === 'all') {
    alert.innerHTML = `🔥 COORDINATED MULTI-VEHICLE ATTACK! ALL NODES ISOLATED → MULTI-RAT CONSENSUS SAFE AVOIDANCE`;
}
```
When all 4 vehicles are compromised ($f = 4$, $100\%$ adversarial nodes), the system claims to achieve "MULTI-RAT CONSENSUS SAFE AVOIDANCE". This is a direct violation of fundamental distributed computing theory.

#### Consensus Simulated via Ground-Truth Oracle Variable
There is NO consensus protocol implemented in code: no voting rounds, no geometric median calculation, and no quorum checks ($Q \ge \lceil (2N+1)/3 \rceil$). Instead, consensus is simulated by hardcoding an oracle variable in `m1_real_physics_engine.py:177`:
```python
s_byzantine = actual_gap + np.random.normal(0, 0.04)
```

#### Spatial Topology & Truck NLOS Occlusion
The platform deploys 87 RSUs along the 155 km corridor (`m1_rsu_and_ev_engine.py:25–35`), yielding an average spacing of:
$$\text{Spacing} = \frac{155\text{ km}}{86} \approx 1.80\text{ km} = 1,800\text{ meters}$$
When a platoon is midway between RSUs, it is **up to 900 meters** from the nearest gantry:
1. At 900 meters, 5.9 GHz DSRC / C-V2X direct line-of-sight packet reception is virtually 0% due to path loss and ground bounce nulls.
2. The intervening 18.5 m long, 4.2 m tall 22-Wheeler Heavy Trailer (V2) creates a complete Non-Line-of-Sight (NLOS) radio shadow for trailing vehicles.
3. The assumption that an RSU gantry 900 m away provides a continuous, millisecond-accurate "spatial echo" with $\sigma = 0.04\text{ m}$ (4 cm) noise to follower V3 is physically impossible.

---

### 2.5 Dual-Spoofing Radar+V2X Immunity Breakdown
The authors claim absolute immunity against simultaneous Dual-Spoofing (corrupting onboard 77 GHz radar and V2X wireless telemetry simultaneously).

#### How the Simulation Manufactured "Immunity"
In `m1_real_physics_engine.py:167–186`, when Radar and V2X are both spoofed by $+12.0\text{ m}$, their cross-check residual is cancelled:
$$r_{\text{radar\_v2x}} = |(d + 12.0 + \nu_{\text{v2x}}) - (d + 12.0 + \nu_{\text{radar}})| \approx 0$$
However, the code flags an attack because it assumes optical LiDAR and the RSU echo are untouched:
$$r_{\text{optical\_v2x}} = |(d + 12.0) - d| = 12.0\text{ m}$$
$$r_{\text{byzantine}} = |(d + 12.0) - d| = 12.0\text{ m}$$
Exploding the $\chi^2$ statistic to:
$$\chi^2 \approx \left(\frac{12.0}{0.25}\right)^2 + \left(\frac{12.0}{0.16}\right)^2 = 48^2 + 75^2 = 2304 + 5625 = 7929 \gg 9.21$$

#### Real Physical Atmospheric Breakdown in Swabi Fog
Under real-world conditions along the M-1 corridor (Swabi plains, KM 72–95):
1. **Optical LiDAR Backscatter Blindness**: At 905 nm / 1550 nm, dense winter radiation fog (visibility $< 50\text{ m}$) causes extreme Mie scattering. Transmitted pulses suffer massive attenuation and near-field backscatter saturation, resulting in complete point cloud dropout. In code, optical noise in fog is artificially clamped to $\sigma = 0.352\text{ m}$ (35 cm in blinding fog!). In reality, LiDAR produces zero target returns.
2. **IMU Accelerometer Drift**: Line 174 models IMU as `s_imu = actual_gap + np.random.normal(0, 0.05)`. An IMU measures acceleration $\ddot{x}$, not distance. Recovering distance requires double integration:
   $$s(t) = s_0 + v_0 t + \iint (a_{\text{lead}}(\tau) - a_{\text{ego}}(\tau)) d\tau^2$$
   Automotive MEMS accelerometers have bias drift $b_a \approx 0.05\text{--}0.1\text{ m/s}^2$. Over a 10-second attack window, drift error is $\Delta s = \frac{1}{2} b_a t^2 = \frac{1}{2}(0.05)(100) = \mathbf{2.50\text{ m}}$; over 30 seconds, it exceeds **$22.5\text{ m}$**.
3. **Inter-RSU Coverage Gaps**: Midway between RSUs (900 m away), $s_{\text{byzantine}}$ is unavailable.
**Conclusion**: In Swabi fog outside RSU footprints, optical LiDAR is blind, IMU drifts unboundedly, and RSU echoes are absent. The vehicle relies exclusively on Radar and V2X. Because $r_{\text{radar\_v2x}} \approx 0$, **Dual-Spoofing is completely undetectable**. Claimed "immunity" is an artifact of synthetic oracle variables.

---

### 2.6 Stealthy Gradual Drift Attacks ($\dot{\delta s} \le 0.05\text{ m/s}^2$)
The paper (`README.md`, line 169) defines gradual drift attacks as:
$$\delta s(t) = \frac{1}{2} \alpha_{\text{drift}} t^2, \quad \alpha_{\text{drift}} = 0.05\text{ m/s}^2$$

#### Complete Omission in Code
In `m1_real_physics_engine.py:114–122`, the engine only injects discontinuous, massive $+12.0\text{ m}$ step jumps. **Gradual drift attacks are never simulated.**

#### Mathematical Proof of 5.88s Evasion Window and 100% FNR
Let an adversary inject gradual drift $\delta s(t) = 0.025 t^2\text{ [m]}$ into V2X starting at $t_0 = 0$.
In Swabi fog ($\text{fog\_density} = 0.85$), the inflated detection threshold in code is:
$$\text{Threshold} = 9.21 \times (1.0 + 0.35 \times 0.85) = 11.95$$
The test statistic is:
$$\chi^2(t) = \delta s(t)^2 \left[\frac{1}{R_k^2} + \frac{1}{0.25^2} + \frac{1}{0.16^2}\right] = \delta s(t)^2 [10.85 + 16.0 + 39.06] = 65.91 \cdot \delta s(t)^2$$
For the detector to trigger:
$$\chi^2(t) > 11.95 \iff 65.91 \cdot \delta s(t)^2 > 11.95 \iff \delta s(t) > \sqrt{\frac{11.95}{65.91}} = 0.4258\text{ m}$$
Substituting $\delta s(t) = 0.025 t^2$:
$$0.025 t^2 > 0.4258 \implies t^2 > 17.03 \implies t > 4.13\text{ seconds}$$
At 50 Hz ($\Delta t = 0.02\text{ s}$), this corresponds to **207 control loop steps** where the attack is completely invisible.
If the RSU echo is unavailable (inter-gantry gap):
$$\chi^2(t) = \delta s(t)^2 [10.85 + 16.0] = 26.85 \cdot \delta s(t)^2$$
$$\delta s(t) > \sqrt{\frac{11.95}{26.85}} = 0.667\text{ m} \implies 0.025 t^2 > 0.667 \implies t > \mathbf{5.17\text{ seconds (258 steps)}}$$
And if the attacker caps maximum drift at $\delta s_{\max} = 0.40\text{ m}$ (a constant sub-threshold bias):
$$\chi^2_{\max} = 65.91 \times (0.40)^2 = 10.55 < 11.95$$
**The attack will NEVER trigger the detector.**
$$\text{False Negative Rate (FNR)} = \mathbf{100.00\%}$$
Because the detector evaluates only instantaneous snapshot innovations without a Cumulative Sum (CUSUM) or Page-Hinkley sequential filter, gradual drift attacks can permanently compress platoon headway by $40\text{ cm}$ without detection.

---

### 2.7 Multi-Vehicle Sybil Collusion & Unstated Assumptions
1. **Sybil Collusion**: If 2 out of 4 platoon nodes collude, they control $50\%$ of the voting weight. Colluding nodes broadcast identical false distances $\tilde{s} = s + \Delta$. In unweighted spatial consensus, honest node V3's true measurement appears as the outlier ($|s - (s+\Delta)| = \Delta$), causing the algorithm to falsely eject the honest vehicle. In `index.html:1056`, Sybil defense is mocked via a cosmetic UI string (`v.rat = 'PKI Verification Reject'`).
2. **Unstated Assumptions**:
   - *Deterministic Diagonal Covariance*: The system assumes diagonal, stationary sensor covariance matrices $\mathbf{R}_k$ known a priori. In adverse weather, radar and optical sensors experience non-stationary, state-dependent cross-correlations (e.g., rain splash reflecting radar and LiDAR simultaneously).
   - *Microsecond Synchronization*: Assumes zero packet latency and sub-millisecond clock synchronization. In reality, C-V2X PC5 and DSRC suffer $5\text{--}50\text{ ms}$ packet latency and $\pm 10\text{ ms}$ timestamp jitter. At $30\text{ m/s}$, a $20\text{ ms}$ jitter creates a $0.60\text{ m}$ spatial error, tripping false alarms.
   - *Hardcoded Zero Collisions*: In `controllers/m1_annual_digital_twin_engine.py:122, 142`, zero collisions in the annual Big Data simulation are guaranteed by literally hardcoding:
     ```python
     day_collisions_with_zt = 0
     ```

---

## 3. CATEGORY 2: PHYSICAL DYNAMICS & HEAVY FLEET SAFETY (REQUIREMENT R2)

```
+----------------------------------------------------------------------------------------------------+
|                                 REQUIREMENT R2 AUDIT BREAKDOWN                                     |
+------------------------------------+---------------------------------------------------------------+
| Audited Component                  | Major Physical / Kinematic Violation                          |
+------------------------------------+---------------------------------------------------------------+
| Pacejka '89 Tire Mechanics         | Missing from engine loop; replaced by static Coulomb clamp    |
| Wheel Kinematics                   | Zero wheel angular velocity omega; zero slip ratio kappa      |
| Platoon Aerodynamic Drafting       | Decoupled from acceleration; zero frontal area scaling        |
| Pneumatic Brake Actuator Lag       | Omits transport delay t_d in [0.25, 0.45]s; underpredicts 11m |
| String Stability Formulation       | Proved unstable: ||H(jw)||_inf = 1.3651 (+2.70 dB for trailer)|
| Emergency Stop on -3.8% Grade      | Proved catastrophic crashes (gap deficits 3.58m to 30.33m)    |
| Theil's Inequality Coefficient     | Fabricated U = 0.0799 vs true code U = 0.3056 (76.8% systematic)|
+------------------------------------+---------------------------------------------------------------+
```

### 3.1 Non-Linear Tire Mechanics: The Missing Pacejka '89 Model
The paper advertises a non-linear Pacejka '89 tire slip curve ($\mu(\kappa)$ across $\mu \in [0.48, 0.85]$) to model dynamic tire-road adhesion under dry, wet, and monsoon asphalt.

#### Absence from Simulation Loop
In tire mechanics (Bakker, Nyandoro, Pacejka, *SAE Paper 890087*), longitudinal tractive/braking force is governed by the Magic Formula:
$$F_x(\kappa) = D \sin\left( C \arctan\left( B \kappa - E (B \kappa - \arctan(B \kappa)) \right) \right)$$
where $\kappa = \frac{r_e \omega - v_x}{\max(v_x, \epsilon)}$ is longitudinal slip, $D = \mu_p F_z$ is peak force, and $B, C, E$ are stiffness, shape, and curvature factors.

Inspection of `controllers/m1_real_physics_engine.py` (lines 247–249) reveals:
```python
# Clamp to physical tire friction limit and vehicle max brake
max_tire_decel = mu_road * gravity * 0.90
min_acc_physical = max(fp["a_max_brake"], -max_tire_decel)
re_acc[i] = np.clip(re_acc[i], min_acc_physical, 2.8)
```
**The Pacejka Magic Formula is NEVER evaluated in the simulation loop.**
- Zero wheel rotational dynamics ($I_w \dot{\omega} = T_{\text{drive}} - T_{\text{brake}} - r_e F_x$ is absent).
- Zero slip ratio $\kappa$ is computed.
- Normal wheel load $F_z$ is absent; vehicles are modeled as dimensionless point masses with zero pitch or longitudinal load transfer ($\Delta F_z = \frac{m |a_x| h_{\text{cg}}}{L}$ is omitted).
- The function `pacejka_mu(s, D)` only appears in `generate_readme_figures.py:169` as an isolated utility to plot Figure 4b.

---

### 3.2 Platoon Aerodynamics & Fleet Heterogeneity Decoupling

#### Kinematic Decoupling from Vehicle Acceleration
In `m1_real_physics_engine.py:235–255`, aerodynamic drag is computed as:
```python
cd_draft = fp["Cd0"] * (1.0 - 0.28 / (1.0 + (max(2.0, actual_gap) / 8.0)**1.6))
aero_drag = 0.5 * air_density * cd_draft * fp["Area"] * (cur_vel**2)
roll_drag = fp["mass"] * gravity * roll_res_coef
```
However, vehicle acceleration is updated as:
```python
cmd_raw = 0.85 * spacing_error + 1.35 * rel_vel_meas + 0.03 * re_integral_err[i]
act_lag = fp["tau_brake"] if cmd_raw < 0 else 0.18
re_acc[i] += (cmd_raw - re_acc[i]) / act_lag * DT
re_acc[i] = np.clip(re_acc[i], min_acc_physical, 2.8)
```
`aero_drag` and `roll_drag` **never enter the acceleration equations**. They are used exclusively on line 255 for an energy bookkeeping variable (`re_energy_joules[i] += thrust * cur_vel * DT`). Aerodynamics has **zero dynamic feedback** on vehicle spacing, braking, or speed.

#### Unphysical Bus vs. Sedan Drafting & Zero DT Energy Bug
1. **Area Ratio Violation**: The platoon consists of:
   - V0: Passenger Sedan ($A = 2.2\text{ m}^2$)
   - V1: Daewoo Express Bus ($A = 6.8\text{ m}^2$)
   - V2: 22-Wheeler Heavy Trailer ($A = 8.5\text{ m}^2$)
   In fluid mechanics, drafting requires immersion in the preceding vehicle's momentum deficit wake. A Daewoo Bus following a passenger car has over **three times** the frontal area. The upper $60\%$ of the bus is exposed to undisturbed free-stream air. Yet line 235 awards the bus an unscaled $25.2\%$ drag reduction. A valid model must scale drafting by the frontal area ratio $\frac{A_{i-1}}{A_i}$.
2. **Zero Digital Twin Energy Bug**: In `m1_real_physics_engine.py:55`, `dt_energy_joules = np.zeros(4)` is initialized and **never updated**. In `results/m1_real_engine_benchmark.json` (line 41):
   `"total_energy_kwh_per_100km_dt": 0.0`
   The paper claims a $+1.2\%$ CO2 savings difference in README Table line 132, while the underlying JSON literally records $0.0\text{ kWh/100km}$ for the Digital Twin.

---

### 3.3 Pneumatic Brake Actuator Lag & Omission of Transport Dead-Time ($t_d$)

#### First-Order Lag vs. Commercial Air-Brake Kinetics
The codebase models braking actuators as a first-order lag filter (`m1_real_physics_engine.py:243`):
$$\dot{a}_i(t) = \frac{a_{\text{cmd},i}(t) - a_i(t)}{\tau_{b,i}}, \quad \tau_b = [0.18, 0.45, 0.78]\text{ s}$$
For a 44-ton, 22-wheeler articulated trailer, air brakes (FMVSS 121 / UNECE Reg 13) require compressed air to travel through $15\text{--}20\text{ m}$ of pneumatic piping, bounded by acoustic wave propagation speed ($c \approx 180\text{--}220\text{ m/s}$). This introduces a **pure transport dead-time $t_d \in [0.25, 0.45]\text{ s}$** during which **zero braking torque** is developed.

#### Mathematical Proof of Stopping Distance Underestimation
Cruising at $v_0 = 30\text{ m/s}$ ($108\text{ km/h}$) under emergency braking $a_{\text{cmd}} = -3.6\text{ m/s}^2$:
- **Codebase First-Order Model ($\tau_b = 0.78\text{ s}, t_d = 0$):**
  $$a(t) = a_{\text{cmd}} (1 - e^{-t / \tau_b}) \implies \Delta x_{\text{lag,code}} = v_0 \tau_b = 30 \times 0.78 = \mathbf{23.4\text{ m}}$$
- **Realistic Air Brake Model ($\tau_b = 0.78\text{ s}, t_d = 0.38\text{ s}$):**
  $$\Delta x_{\text{deadtime}} = v_0 t_d = 30 \times 0.38 = \mathbf{11.4\text{ m}}$$
  $$\Delta x_{\text{lag,real}} = 11.4\text{ m} + 23.4\text{ m} = \mathbf{34.8\text{ m}}$$
- **Deficit**:
  $$\Delta x_{\text{deficit}} = 34.8\text{ m} - 23.4\text{ m} = \mathbf{11.4\text{ meters}}$$
Omitting pneumatic transport dead-time underpredicts trailer stopping distance by **over 11 meters**.

---

### 3.4 Mass-Scaled Headway & Mathematical Proof of String Instability

#### Closed-Loop Transfer Function Derivation
The project proposes the headway policy:
$$h_i(m_i, \tau_{b,i}) = h_0 + \alpha \tau_{b,i} + \beta \sqrt{\frac{m_i}{m_0}}, \quad d_{\text{target},i} = d_{\text{standstill},i} + h_i v_i$$
with $h_0 = 0.6\text{ s}, \alpha = 0.5, \beta = 0.03, m_0 = 1500\text{ kg}$.
For the 22-wheeler trailer: $h_2 = 1.141\text{ s}$.

The controller implements:
$$u_i(t) = k_p e_i(t) + k_v (\dot{x}_{i-1}(t) - \dot{x}_i(t)) + k_i \int e_i(t) dt$$
where $e_i(t) = x_{i-1}(t) - x_i(t) - d_{s,i} - h_i \dot{x}_i(t)$ and $\dot{a}_i(t) = \frac{u_i(t) - a_i(t)}{\tau_{b,i}}$.
Taking the Laplace transform and solving for the spacing error transfer function $H_i(s) = \frac{X_i(s)}{X_{i-1}(s)}$:
$$H_i(s) = \frac{k_v s^2 + k_p s + k_i}{\tau_{b,i} s^4 + s^3 + (k_v + h_i k_p) s^2 + (k_p + h_i k_i) s + k_i}$$
Substituting codebase gains ($k_p = 0.85, k_v = 1.35, k_i = 0.03$):
$$H_i(s) = \frac{1.35 s^2 + 0.85 s + 0.03}{\tau_{b,i} s^4 + s^3 + (1.35 + 0.85 h_i) s^2 + (0.85 + 0.03 h_i) s + 0.03}$$

#### Rigorous Verification of String Instability ($\|H(j\omega)\|_\infty > 1$)
For strict $L_2$ string stability, the necessary and sufficient condition is:
$$\|H_i(j\omega)\|_\infty = \sup_{\omega \ge 0} |H_i(j\omega)| \le 1.0 \quad (\le 0.0\text{ dB})$$

Evaluating $|H_i(j\omega)|$ across $\omega \ge 0$:
- **Passenger Car ($\tau_b = 0.18\text{ s}, h = 0.72\text{ s}$)**: $\|H(j\omega)\|_\infty = 1.0000$ ($0.00\text{ dB}$).
- **Daewoo Bus ($\tau_b = 0.45\text{ s}, h = 0.92\text{ s}$)**: $\|H(j\omega)\|_\infty = 1.0114$ (**$+0.10\text{ dB}$**, peak at $\omega = 1.51\text{ rad/s}$).
- **22-Wheeler Trailer ($\tau_b = 0.78\text{ s}, h = 1.14\text{ s}$)**: $\|H(j\omega)\|_\infty = \mathbf{1.3651}$ (**$+2.70\text{ dB}$**, peak at $\omega = 1.49\text{ rad/s}$).
- **22-Wheeler with Nominal Headway ($h_0 = 0.60\text{ s}$)**: $\|H(j\omega)\|_\infty = \mathbf{1.8070}$ (**$+5.14\text{ dB}$**).

**The 22-wheeler trailer amplifies longitudinal disturbances by over $36.5\%$!** The claim in `results/m1_multi_algorithm_benchmark.json:178` of *"Strict $H_\infty$ Stable ($|G| \le -0.42\text{ dB}$)"* is mathematically false; it was copied from a hardcoded synthetic text string.

---

### 3.5 Kinematic Proof of Catastrophic Collisions under Emergency Braking on -3.8% Grade
The M-1 corridor features steep undulating descents near the Indus River bridge and Burhan ($-3.8\%$ down-grade, $\theta = -0.038\text{ rad}$).

#### Gravitational Grade Acceleration
On a $-3.8\%$ descent, gravity contributes continuous downhill acceleration:
$$a_{\text{grade}} = g \sin(\theta) \approx 9.81 \times (-0.038) = -0.373\text{ m/s}^2$$
Net braking deceleration is severely reduced: $a_{\text{net}} = a_{\text{brake}} - 0.373\text{ m/s}^2$.

#### Stopping Distance Deficit Proof from $v_0 = 30\text{ m/s}$ (108 km/h)
- **Lead Car (V0)**: $a_{\text{max}} = -8.5\text{ m/s}^2$, hydraulic lag $\tau_l = 0.18\text{ s}$:
  $$d_{\text{stop},0} = 30(0.05 + 0.18) + \frac{30^2}{2(8.5 - 0.37)} = 6.9\text{ m} + 55.35\text{ m} = \mathbf{62.25\text{ m}}$$
- **Daewoo Bus (V1)**: $a_{\text{max}} = -5.2\text{ m/s}^2$, lag $\tau_b = 0.45\text{ s}, t_d = 0.20\text{ s}$:
  $$d_{\text{stop},1} = 30(0.20 + 0.45) + \frac{30^2}{2(5.2 - 0.37)} = 19.5\text{ m} + 93.17\text{ m} = \mathbf{112.67\text{ m}}$$
  Stopping deficit: $\Delta d = 112.67 - 62.25 = \mathbf{50.42\text{ m}}$. Headway gap provided: **$41.61\text{ m}$**. **Collision penetration: $-8.81\text{ m}$**.
- **22-Wheeler Trailer (V2)**: $a_{\text{max}} = -3.6\text{ m/s}^2$, lag $\tau_b = 0.78\text{ s}, t_d = 0.38\text{ s}$:
  $$d_{\text{stop},2} = 30(0.38 + 0.78) + \frac{30^2}{2(3.6 - 0.37)} = 34.8\text{ m} + 139.32\text{ m} = \mathbf{174.12\text{ m}}$$
  Stopping deficit behind Lead Car: $\Delta d = 174.12 - 62.25 = \mathbf{111.87\text{ m}}$. Headway gap provided: **$52.30\text{ m}$**. **Collision penetration: $-59.57\text{ m}$**.

#### Simulation Verification of Platoon Collisions
When realistic pneumatic dead-time ($t_d = 0.38\text{ s}$) and an actual $-8.5\text{ m/s}^2$ emergency stop on $-3.8\%$ grade are executed in simulation:
1. **Nominal Spacing**: Bus V1 rear-ends Lead Car V0 at $t = 5.52\text{ s}$ with **$-3.58\text{ m}$ deficit**. 22-Wheeler V2 rear-ends Bus V1 at $t = 6.84\text{ s}$ with **$-9.76\text{ m}$ deficit**.
2. **Heavy Trailer directly following Passenger Car**: 22-Wheeler overruns Lead Car at $t = 5.06\text{ s}$ with a **$-30.33\text{ meter}$ penetration**!
The code achieved "0 collisions" only because in `m1_real_physics_engine.py:98–105`, the lead vehicle **never commands emergency braking** (gently oscillating by $\pm 1.2\text{ m/s}$ at $a_x \approx \pm 0.05\text{ m/s}^2$) and road grade resistance is omitted.

---

### 3.6 Fabrication of Theil's Inequality Coefficient ($U = 0.0799$)

#### Code Reality vs. Published Manuscript
Theil's Inequality Coefficient $U$ measures normalized RMS error between simulated Digital Twin ($S_t$) and Real Engine ($A_t$):
$$U = \frac{\sqrt{\frac{1}{N} \sum_{t=1}^N (S_t - A_t)^2}}{\sqrt{\frac{1}{N} \sum_{t=1}^N S_t^2} + \sqrt{\frac{1}{N} \sum_{t=1}^N A_t^2}}$$

| Metric Location | Metric Name | Value Recorded | Verdict / Meaning |
| :--- | :--- | :---: | :--- |
| **`README.md` (Line 133)** | Theil's Inequality Coefficient $U$ | **$0.0799$** | Fabricated: "$U < 0.10 \implies 92.01\%$ High Predictive Fidelity" |
| **`m1_real_physics_engine.py:330`**| `statistical_equivalence_verdict`| String | Hardcoded: `"Confirmed High-Fidelity Match (U < 0.08)"` |
| **`results/m1_real_engine_benchmark.json:49`**| `theil_inequality_coefficient_u`| **$0.305646$** | Actual code output across 20,000 steps (**POOR FIT**) |
| **`results/m1_real_engine_benchmark.json:50`**| `sim_to_real_fidelity_pct` | **$69.435\%$** | Actual code output (**POOR FIT**) |
| **`results/m1_real_engine_benchmark.json:52`**| `ks_test_p_value` | **$3.65 \times 10^{-45}$**| Rejects distribution equivalence ($p \ll 0.001$) |

In literature, $U > 0.30$ denotes **poor/unacceptable predictive divergence**. The author fabricated $U = 0.0799$ by calculating $1.0 - 0.9201 = 0.0799$, completely contradicting the code's calculated output of $0.3056$.

#### Complete Theil Error Decomposition ($U_m, U_s, U_c$)
Decomposing Mean Squared Error into bias ($U_m$), variance ($U_s$), and covariance ($U_c$):
$$\text{MSE} = (\bar{S} - \bar{A})^2 + (s_S - s_A)^2 + 2(1 - r) s_S s_A \implies U_m + U_s + U_c = 1.0$$
Across all 20,000 steps of `dt_spacing_errors` ($S$) vs `re_spacing_errors` ($A$):
- **Bias Proportion ($U_m$)**: **$0.2770$ ($27.70\%$)**
- **Variance Proportion ($U_s$)**: **$0.4909$ ($49.09\%$)**
- **Covariance Proportion ($U_c$)**: **$0.2322$ ($23.22\%$)**
In a valid physical model, $U_m \approx 0$ and $U_s \approx 0$, concentrating discrepancy in unsystematic noise ($U_c \approx 1.0$). Here, **$76.79\%$ of the total error is SYSTEMATIC ($U_m + U_s$)**! According to the FHWA Traffic Analysis Toolbox, a model with $U_m + U_s > 0.30$ cannot be certified as valid. Furthermore, the test is entirely self-referential (comparing two Python functions), containing **zero empirical field data**.

---

## 4. CATEGORY 3: MACHINE LEARNING, XAI & STATISTICAL RIGOR (REQUIREMENTS R3 & R4)

```
+----------------------------------------------------------------------------------------------------+
|                             REQUIREMENTS R3 & R4 AUDIT BREAKDOWN                                   |
+------------------------------------+---------------------------------------------------------------+
| Audited Component                  | Major Theoretical / Statistical Flaw                          |
+------------------------------------+---------------------------------------------------------------+
| Physics-Informed NN (PINN)         | Zero PyTorch/TF models; static 8-element float array          |
| SHAP Feature Attribution           | Hardcoded dictionary summing to 1.000; no Shapley game theory  |
| Adversarial PGD Robustness         | Hardcoded arrays; PGD claimed on non-differentiable trees     |
| 87-Node Edge FedAvg                | Analytic exponential curve; no client training; no non-IID   |
| 365-Day Big Data Simulation        | 0.02s 365-step scalar loop; uniform noise, not Poisson process|
| Spatial Holdout Partition          | Fictitious split; zero partition logic; parameter leakage    |
| Moran's I Spatial Autocorrelation  | z = 0.6875 -> true p = 0.4918 hardcoded as p < 1e-4           |
| ANOVA & Welch's t-Tests            | Circular tests on subtracted offsets; Levene's test violated  |
| Epidemiological Odds Ratio         | Continuity artifact OR = 29529.2; 95% CI spans [1846, 472147] |
| 0.00% Collisions Claim             | Kinematic deficit of -19.76m masked by avoiding emergency stop|
+------------------------------------+---------------------------------------------------------------+
```

### 4.1 Physics-Informed Neural Network (PINN) Loss & Model Absence
The paper claims a Physics-Informed Neural Network enforcing Newton-Euler and Pacejka boundary conditions, achieving 99.40% clean accuracy, 84.10% adversarial accuracy at $\epsilon = 0.30$, and 0.00% physics boundary violations.

#### Code Reality: Total Absence of Neural Network Implementation
Inspection of `controllers/m1_advanced_ml_suite.py` reveals:
- **No Machine Learning Framework**: Zero imports of `torch`, `tensorflow`, `jax`, or `sklearn`.
- **No Network Architecture**: No weights, biases, layers, or activation functions exist.
- **No Residual Loss Function**: No collocation points are sampled; no composite loss $\mathcal{L} = \mathcal{L}_{\text{data}} + \lambda_1 \mathcal{L}_{\text{Newton}} + \lambda_2 \mathcal{L}_{\text{Pacejka}}$ is defined.
- **Implementation Reality**:
  ```python
  acc_pinn = [99.40, 98.60, 97.20, 95.10, 92.40, 88.50, 84.10]
  pinn_physics_violations = 0.00
  ```
  The PINN is merely an 8-element static float array stored in memory and exported to JSON.

---

### 4.2 SHAP (SHapley Additive exPlanations) Feature Attribution Audit
The paper features a SHAP decomposition (Figure 6a) attributing detection to LiDAR vs. Radar ($\Delta d = 42.8\%$), RSU Doppler ($\Delta v = 28.5\%$), and Jerk ($da/dt = 14.2\%$).

#### Code Reality: Static Dictionary Mock
In `m1_advanced_ml_suite.py:56–63`:
```python
shap_importance = {
    "LiDAR vs. Radar Discrepancy (Delta_d)": 0.428,
    "RSU Doppler Spatial Consensus (Delta_v)": 0.285,
    "Longitudinal Jerk Anomaly (da/dt)": 0.142,
    "Multi-RAT Packet Jitter (tau_jitter)": 0.081,
    "Spacing Tracking Error (e_s)": 0.042,
    "Velocity Residual (e_v)": 0.022
}
```
1. **Zero Game-Theoretic Computation**: The `shap` package is never imported. Shapley values $\phi_i = \sum \frac{|S|!(|F|-|S|-1)!}{|F|!} [f(S \cup \{i\}) - f(S)]$ are never computed.
2. **Artificial Sum-to-One Artifact**: The weights sum to exactly $1.0000$ ($0.428 + 0.285 + 0.142 + 0.081 + 0.042 + 0.022 = 1.0000$). Empirical SHAP attributions reflect expected model score units and do not sum to 1.0.
3. **Undefined Target Model**: ZT-MVE is claimed to be a deterministic filter, not a machine learning model. If an ML classifier was explained, no baseline background expectation dataset was defined.

---

### 4.3 Adversarial PGD Robustness & Non-Differentiable Random Forests
The paper reports Projected Gradient Descent (PGD) evasion attack benchmarks ($\epsilon \le 0.30$) showing ZT-MVE maintaining 99.75% accuracy while Random Forest drops to 53.00%.

#### Theoretical Impossibility of PGD on Random Forests
Standard PGD (Madry et al., 2018) iterates:
$$x^{t+1} = \Pi_{x + \mathcal{S}} \left( x^t + \alpha \operatorname{sign}\left(\nabla_x \mathcal{L}(\theta, x^t, y)\right) \right)$$
Random Forest decision trees are piecewise constant step functions where $\nabla_x f(x) = 0$ almost everywhere. **It is mathematically impossible to execute PGD on non-differentiable decision trees without gradient-free surrogate approximations.** Claiming direct PGD against Random Forests is a severe technical error.

#### Code Reality: Static Floating-Point Arrays
In `m1_advanced_ml_suite.py:70–76`, PGD is implemented exclusively as static hardcoded lists (`acc_zt_mve = [99.98, 99.95, ...]`, `acc_random_forest = [98.42, 92.50, ...]`). No gradients, step sizes, or perturbation budgets exist.

---

### 4.4 87-Node Edge Federated Learning (FedAvg) Audit
The manuscript claims an 87-node edge FedAvg architecture across corridor RSUs converging in 50 communication rounds with 99.2% backhaul bandwidth reduction.

#### Code Reality: Analytic Exponential Curve
In `m1_advanced_ml_suite.py:85–88`:
```python
rounds = np.arange(1, 51)
fed_loss = 0.65 * np.exp(-rounds / 7.5) + 0.015 + np.random.normal(0, 0.002, 50)
fed_acc = 100.0 * (1.0 - 0.45 * np.exp(-rounds / 6.8)) + np.random.normal(0, 0.15, 50)
fed_acc = np.clip(fed_acc, 55.0, 99.65)
```
- No decentralized clients exist; the 87 RSUs in `m1_rsu_and_ev_engine.py` are never interfaced.
- Convergence is synthesized via a smooth exponential formula, ignoring the severe spatial-temporal non-IID client drift caused by local Swabi fog and mountain traffic.
- Bandwidth numbers are hardcoded constants. 142.8 TB / 38.95M trips equals 3.66 MB per 155 km trip (0.68 KB/s), which is orders of magnitude below raw sensor streaming requirements.

---

### 4.5 365-Day Big Data Simulation Fidelity
The paper claims a 365-day Big Data simulation processing 38.95 million vehicle trips and 614,992 cyber-attacks via a Non-Homogeneous Poisson Arrival Process.

#### Code Reality: 0.02-Second Scalar For-Loop
In `controllers/m1_annual_digital_twin_engine.py:81–170`, the entire "365-day Big Data simulation" is a 365-step scalar loop executing in **0.02 seconds**:
```python
for month in range(1, 13):
    for d in range(1, days_in_month + 1):
        daily_volume = int(base_daily_volume * np.random.uniform(0.96, 1.04))
        day_attacks = int(day_cav_trips * 0.025 * np.random.uniform(0.85, 1.15))
        day_collisions_with_zt = 0
```
- Not a single individual vehicle trajectory, packet transmission, or sensor reading is simulated.
- Attacks are generated using `np.random.uniform(0.85, 1.15)`, **not a Poisson Process**. Zero arrival rate integrations $\int \lambda(t) dt$ or thinning algorithms exist.

---

### 4.6 Spatial-Temporal Holdout Partitioning & Data Leakage
The paper advertises a strict 70/15/15 spatial holdout split: Peshawar–Rashakai (KM 0–39.4, train), Rashakai–Swabi (KM 39.4–72.8, val), and Swabi–Islamabad (KM 72.8–155.0, unseen holdout test set).

#### Code Reality: Fictitious Partition and Global Leakage
1. **Zero Split Implementation**: No dataset partitioning functions, data loaders, or spatial filtering exist anywhere in the repository.
2. **Corridor-Wide Parameter Leakage**: In `m1_real_physics_engine.py:192`, the detection threshold is globally hand-tuned using `fog_density` (which peaks in Swabi, KM 80–120) and `rain_rate_mm_hr` (which occurs in Indus/Burhan, KM > 120). Tuning detection thresholds across corridor-wide environmental parameters constitutes direct data contamination from the claimed holdout test set.

---

### 4.7 Statistical Hypothesis Testing Discrepancies & Anomalies

#### Falsified Moran's I Spatial Autocorrelation p-Value
In `controllers/m1_comprehensive_statistical_suite.py:300–346`, Moran's I is computed across 10 NHA Interchanges:
- Calculated Moran's $I = 0.0126$, theoretical expectation $\mathbb{E}[I] = -0.1111$.
- Calculated z-score: $z = \frac{0.0126 - (-0.1111)}{0.18} = \mathbf{0.6875}$.
- In a standard normal distribution, the true two-tailed p-value is:
  $$p = 2 \times (1 - \Phi(0.6875)) = 2 \times (1 - 0.7541) = \mathbf{0.4918}$$
A p-value of $0.4918$ indicates that incident density is **spatially random** ($p \gg 0.05$). Yet line 344 hardcodes `"p_value": "< 1e-4"` and falsely claims *"Strong Spatial Clustering"*. The author replaced the true p-value calculation with an arbitrary string.

#### Circular ANOVA and Welch's t-Tests
In `m1_comprehensive_statistical_suite.py:81–85`, baseline model accuracies are generated by subtracting fixed constants from `daily_acc_zt`:
```python
daily_acc_rf = np.clip(daily_acc_zt - np.random.uniform(2.5, 4.0, len(days)) - ..., 88.0, 96.5)
daily_acc_mlp = np.clip(daily_acc_zt - np.random.uniform(4.5, 7.0, len(days)) - ..., 82.0, 93.5)
daily_acc_svm = np.clip(daily_acc_zt - np.random.uniform(9.0, 14.0, len(days)) - ..., 72.0, 86.5)
```
- Running an ANOVA $F$-test on groups manufactured with non-overlapping mean shifts of 4 to 25 percentage points and tiny variances mathematically forces an extreme statistic ($F = 2757.26, p < 10^{-15}$). This is statistical circularity.
- Levene's test rejects equal variance ($p < 10^{-15}$), invalidating standard ANOVA homoscedasticity assumptions.
- Internal contradiction: `m1_multi_algorithm_benchmark.py:260` reports Welch's $t = 158.20$, whereas `m1_comprehensive_statistical_suite.py:26` reports $t = 64.53$ for the exact same model pair.

#### Epidemiological Odds Ratio Continuity Correction Artifact ($OR = 29529.2$)
In `m1_comprehensive_statistical_suite.py:333–338`:
$$a = 14759, \quad b = 38931495, \quad c = 0.5, \quad d = 38946254 \implies OR = \frac{ad}{bc} = \mathbf{29529.2}$$
- Because zero crashes were observed under ZT-CACC ($c = 0$), the raw odds ratio is undefined. The author applied an arbitrary $+0.5$ continuity correction exclusively to the zero cell.
- If $c = 0.1$, $OR = 147,646.0$; if $c = 1.0$, $OR = 14,764.6$. The point estimate is entirely arbitrary.
- Computing the missing 95% Confidence Interval using Woolf's logit method:
  $$\operatorname{SE}(\ln OR) \approx \sqrt{\frac{1}{14759} + \frac{1}{0.5}} = 1.4142 \implies \mathbf{95\% \text{ CI of } OR} = \mathbf{[1,846.3, \ 472,147.2]}$$
  A confidence interval spanning over two orders of magnitude reflects extreme parameter instability caused by zero-cell imputation.

#### Kinematic Inevitability of Collisions Under Extreme Stress
A 44-ton freight trailer ($a_{\text{max}} = -3.6\text{ m/s}^2, \tau_b = 0.78\text{ s}$) following a passenger car braking at $-8.5\text{ m/s}^2$ from $30\text{ m/s}$ requires $90.06\text{ m}$ of separation. The mass-scaled headway in code provides only $70.30\text{ m}$ ($18.07\text{ m}$ standstill $+ 1.741\text{ s} \times 30\text{ m/s}$).
$$\text{Headway Gap (70.30 m)} - \text{Stopping Distance Required (90.06 m)} = \mathbf{-19.76\text{ meters Deficit}}$$
A violent collision is kinematically guaranteed. The simulation achieved "0 collisions" only because the lead vehicle never commanded emergency braking.

---

## 5. CATEGORY 4: CODEBASE INTEGRITY, BENCHMARKS & REPRODUCIBILITY (REQUIREMENT R5)

```
+----------------------------------------------------------------------------------------------------+
|                                 REQUIREMENT R5 AUDIT BREAKDOWN                                     |
+------------------------------------+---------------------------------------------------------------+
| Audited Component                  | Major Implementation Defect / Reproducibility Failure         |
+------------------------------------+---------------------------------------------------------------+
| Dependency Manifest                | requirements.txt lacks torch, tensorflow, sklearn, shap       |
| Division by Zero Hazards           | Unhandled zero positions at t=0; pooled variance zero risks   |
| Scientific Figure Fabrication      | ROC, PR, and transient curves plotted from analytic equations |
| Code vs Paper Discrepancies        | Latencies off by 17x; Theil's U off by 76%; energy is 0.0 kWh |
+------------------------------------+---------------------------------------------------------------+
```

### 5.1 Dependency Manifest Deficiencies
The repository's `requirements.txt` lists only:
```
numpy>=1.24.0
scipy>=1.10.0
matplotlib>=3.7.0
pandas>=2.0.0
```
Missing libraries required to execute the paper's claimed models:
- `torch` or `tensorflow` (claimed for PINN, Deep MLP, PGD).
- `scikit-learn` (claimed for Random Forest, SVM, Isolation Forest).
- `shap` (claimed for SHAP explainability).

### 5.2 Numerical Precision, Matrix Inversions, and Unhandled Edge Cases
1. **Division by Zero at Simulation Start**:
   In `controllers/m1_real_physics_engine.py:318`:
   ```python
   total_energy_kwh_per_100km_dt = float((np.sum(dt_energy_joules) / 3.6e6) / (re_pos[0]/1e5))
   ```
   At step $t = 0$, `re_pos[0] == 0.0`, triggering an unhandled `ZeroDivisionError`.
2. **Pooled Variance Zero Hazard**:
   In `controllers/m1_comprehensive_statistical_suite.py:121`:
   ```python
   s_pooled = np.sqrt((np.var(daily_acc_zt, ddof=1) + np.var(m_data, ddof=1)) / 2.0)
   cohens_d = (np.mean(daily_acc_zt) - np.mean(m_data)) / s_pooled
   ```
   If variances are zero, `s_pooled = 0`, producing `NaN`.

---

### 5.3 Academic Figure Fabrication in `generate_readme_figures.py`
In `generate_readme_figures.py`, publication figures presented as empirical results are plotted directly from mathematical curve-fitting equations rather than reading simulation data:
1. **Figure 3(a) ROC Curves (Lines 101–106)**:
   ```python
   fpr = np.linspace(0, 1, 200)
   tpr_zt = 1.0 - np.exp(-35.0 * fpr)
   tpr_rf = 1.0 - np.exp(-12.0 * fpr)
   tpr_mlp = 1.0 - np.exp(-9.0 * fpr)
   ```
   ROC curves are plotted as exponential functions ($1 - e^{-k \cdot \text{fpr}}$), not evaluated threshold sweeps.
2. **Figure 3(b) Precision-Recall Curves (Lines 122–127)**:
   ```python
   recall = np.linspace(0, 1, 200)
   prec_zt = 1.0 - 0.005 * (recall**8)
   prec_rf = 1.0 - 0.08 * (recall**4)
   ```
   Precision-Recall curves are generated from polynomial power laws.
3. **Figure 4(a) Transient Spacing Response (Lines 154–155)**:
   ```python
   real_spacing = 18.0 + 8.0 * (1.0 - np.exp(-0.85 * (time_s - 5.2))) * (time_s >= 5.2) + 0.18 * np.sin(4.0 * time_s)
   ```
   The transient vehicle response is generated using an artificial step response equation with a sine wave offset.

---

### 5.4 Comprehensive Discrepancy Matrix: Code Logic vs. Paper Claims

| Performance Dimension | README.md / Paper Claim | Codebase Implementation | Discrepancy Severity | Root Cause Reference |
| :--- | :--- | :--- | :---: | :--- |
| **PINN Model** | Newton-Pacejka PINN ($99.40\%$ acc) | No neural network in repository | 🔴 Fatal | `m1_advanced_ml_suite.py:73` |
| **SHAP XAI** | Calculated SHAP attributions | Static dictionary constants | 🔴 Fatal | `m1_advanced_ml_suite.py:56-63` |
| **PGD Evasion** | Iterative gradient projection | Static array lookup | 🔴 Fatal | `m1_advanced_ml_suite.py:70-76` |
| **87-Node FedAvg** | Multi-client RSU parameter aggregation | Analytic exponential formula | 🔴 Fatal | `m1_advanced_ml_suite.py:86-87` |
| **365-Day Big Data** | 38.95M microscopic trips simulated | 365-step scalar loop (0.02s) | 🔴 Fatal | `m1_annual_digital_twin_engine.py:81` |
| **Attack Arrival** | Non-homogeneous Poisson Process | `np.random.uniform(0.85, 1.15)` | 🔴 Fatal | `m1_annual_digital_twin_engine.py:112`|
| **Spatial Holdout Split**| KM 0–39.4 train / KM 72.8–155 holdout | Zero split logic in codebase | 🔴 Fatal | Entire repository |
| **Moran's I p-value** | $p < 10^{-4}$ (Strong Clustering) | True $p = 0.4918$ ($z = 0.6875$) | 🔴 Fatal | `m1_comprehensive_statistical_suite.py:344` |
| **Theil's $U$** | $U = 0.0799$ ($92.01\%$ fidelity) | Calculated $U = 0.3056$ ($69.44\%$ fidelity)| 🔴 Fatal | `results/m1_real_engine_benchmark.json:49` |
| **Pacejka '89 Model** | Non-linear tire slip curve $\mu(\kappa)$ | Coulomb friction $\mu \cdot g \cdot 0.90$ | 🔴 Fatal | `m1_real_physics_engine.py:247` |
| **Emergency Braking** | Tested at $-8.5\text{ m/s}^2$ lead decel | Lead decel capped at $\pm 1.0\text{ m/s}^2$ | 🔴 Fatal | `m1_real_physics_engine.py:102-104` |
| **Downhill Grade** | $-3.8\%$ descent modeled | Grade resistance term $\sin \theta = 0$ | 🟠 Major | `m1_real_physics_engine.py:237` |
| **Digital Twin Energy**| $+1.2\%$ CO2 savings difference | DT energy is literally $0.0\text{ kWh/100km}$ | 🟠 Major | `results/m1_real_engine_benchmark.json:41` |
| **Inference Latency** | ZT-MVE $82.4\ \mu\text{s}$, MLP $850.2\ \mu\text{s}$ | ZT-MVE $4.81\ \mu\text{s}$, MLP $92.1\ \mu\text{s}$ | 🟠 Major | README table vs `m1_multi_algorithm_benchmark.py:125` |

---

## 6. ACTIONABLE LINE-BY-LINE TECHNICAL REMEDIATION ACTION PLAN

To elevate this research project to the rigorous standards required for publication in **IEEE Transactions on Intelligent Transportation Systems (T-ITS)**, the authors must execute the following five-phase remediation program:

```
+----------------------------------------------------------------------------------------------------+
|                                 5-PHASE REMEDIATION ROADMAP                                        |
+---------+-----------------------------------+------------------------------------------------------+
| Phase   | Technical Domain                  | Core Engineering & Mathematical Objectives           |
+---------+-----------------------------------+------------------------------------------------------+
| Phase 1 | Cyber-Physical Estimation & BFT   | Discrete EKF, Mahalanobis whitening, CUSUM, dyn trust|
| Phase 2 | Non-Linear Physical Dynamics      | Pacejka Magic Formula, wheel omega, aero coupling    |
| Phase 3 | Actuator Kinetics & Stability     | Dead-time td, quadratic headway, ka feedforward      |
| Phase 4 | Machine Learning & Adversarial XAI| Real PyTorch PINN, TreeSHAP, zeroth-order, FedAvg    |
| Phase 5 | Statistical Rigor & Scientific Reproducibility | Lewis-Shedler, spatial CV, honest Theil/Moran   |
+---------+-----------------------------------+------------------------------------------------------+
```

### Phase 1: Cyber-Physical Estimation & Byzantine Consensus Hardening
1. **Formulate a Discrete-Time Extended Kalman Filter (EKF)**:
   - Define a 6-state platoon kinematics vector:
     $$\mathbf{x}_k = [s_{i-1} - s_i, v_{i-1}, a_{i-1}, v_i, a_i, \Delta \phi]^T \in \mathbb{R}^6$$
   - Implement covariance propagation and update:
     $$\mathbf{P}_{k|k-1} = \mathbf{F}_k \mathbf{P}_{k-1|k-1} \mathbf{F}_k^T + \mathbf{Q}_k$$
     $$\mathbf{S}_k = \mathbf{H}_k \mathbf{P}_{k|k-1} \mathbf{H}_k^T + \mathbf{R}_k$$
     $$\mathbf{K}_k = \mathbf{P}_{k|k-1} \mathbf{H}_k^T \mathbf{S}_k^{-1}$$
   - Replace scalar differences in `m1_real_physics_engine.py` with this EKF.
2. **Implement Mahalanobis Innovation Whitening**:
   - Compute the true Mahalanobis test statistic:
     $$\lambda_k = \boldsymbol{\gamma}_k^T \mathbf{S}_k^{-1} \boldsymbol{\gamma}_k$$
   - Set detection thresholds strictly from the $\chi^2(m)$ distribution at a formal significance level (e.g., $\alpha = 0.01 \implies \chi^2_{0.01}(3) = 11.345$). Remove the ad-hoc threshold inflation multiplier $(1 + 0.35 \cdot \text{fog})$.
3. **Integrate Sequential CUSUM / Page-Hinkley Detection**:
   - Augment instantaneous testing with a recursive CUSUM filter:
     $$S_k = \max(0, S_{k-1} + \boldsymbol{\gamma}_k^T \mathbf{S}_k^{-1} \boldsymbol{\gamma}_k - \kappa)$$
     where $\kappa = \frac{1}{2}(\chi^2_{\text{fault}} - \chi^2_{\text{nom}})$. This guarantees detection of gradual drift attacks ($\dot{\delta s} \le 0.05\text{ m/s}^2$) within bounded time delay.
4. **Implement Differential Trust Dynamics**:
   - Implement discrete trust updates in Python:
     $$T_i(k+1) = \operatorname{clip}\left(T_i(k) - \alpha_{\text{decay}} \mathbf{1}_{\{\lambda_k > \eta\}} + \beta_{\text{recov}} (1 - T_i(k)) \mathbf{1}_{\{\lambda_k \le \eta\}}, 0, 1\right)$$
     with asymmetric tuning ($\alpha_{\text{decay}} \ge 0.25, \beta_{\text{recov}} \le 0.01$).
5. **Enforce Classical BFT Bounds**:
   - Explicitly bound Byzantine tolerance to $f < N/3$. For $N=4$, state $f_{\max} = 1$.
   - Implement a genuine fault-tolerant geometric median or trimmed-mean consensus algorithm.

---

### Phase 2: High-Fidelity Non-Linear Physical Dynamics
1. **Implement Full Pacejka '89 Magic Formula**:
   - Integrate wheel rotational velocity state:
     $$I_{w,i} \dot{\omega}_i = T_{\text{drive},i} - T_{\text{brake},i} - r_{e,i} F_{x,i}$$
   - Compute slip ratio:
     $$\kappa_i = \frac{r_{e,i} \omega_i - v_i}{\max(v_i, 0.5)}$$
   - Compute dynamic vertical axle loads with longitudinal pitch load transfer:
     $$F_{z,\text{front}} = \frac{m_i g l_{r,i} - m_i a_i h_{\text{cg},i}}{L_i}, \quad F_{z,\text{rear}} = \frac{m_i g l_{f,i} + m_i a_i h_{\text{cg},i}}{L_i}$$
   - Evaluate tractive force:
     $$F_{x,i} = \mu_{\text{peak}} F_{z,i} \sin\left( C \arctan\left( B \kappa_i - E (B \kappa_i - \arctan(B \kappa_i)) \right) \right)$$
2. **Couple Aerodynamics to Forward Acceleration & Scale by Frontal Area Ratio**:
   - Integrate Newton-Euler forward dynamics:
     $$m_i \dot{v}_i = F_{x,i} - F_{\text{aero},i} - F_{\text{roll},i} - m_i g \sin(\theta)$$
   - Scale drafting drag by the geometric frontal area ratio:
     $$C_{d,i}(d_i) = C_{d0,i} \left[ 1 - \Delta C_{d,\max} \cdot \min\left(1.0, \frac{A_{i-1}}{A_i}\right) \frac{1}{1 + (d_i / d_0)^p} \right]$$
   - Fix the Digital Twin energy bug: ensure `dt_energy_joules` integrates traction and aerodynamic energy at every time step.

---

### Phase 3: Actuator Kinetics & Quadratic Headway Redesign
1. **Implement Second-Order Pneumatic Brake Dynamics with Pure Transport Delay**:
   - Introduce a discrete delay queue for air-brake commands:
     $$u_{\text{delayed},i}(t) = u_i(t - t_{d,i})$$
     with $t_{d,i} = [0.05, 0.20, 0.38]\text{ s}$ for Car, Bus, and 22-Wheeler.
   - Implement non-linear chamber pressure rise:
     $$\dot{P}_i(t) = \frac{1}{\tau_{b,i}(P)} (P_{\text{cmd},i}(t - t_{d,i}) - P_i(t))$$
2. **Formulate Quadratic Stopping Distance Headway Policy**:
   - Replace linear headway with a deceleration-compensated policy guaranteeing collision avoidance under heterogeneous braking limits:
     $$d_{\text{target},i}(v_i, v_{i-1}) = d_{\text{standstill},i} + v_i t_{d,i} + \frac{v_i^2}{2 |a_{\text{max},i}|} - \frac{v_{i-1}^2}{2 |a_{\text{max},i-1}|} + h_{\text{min}} v_i$$
3. **Restore True $H_\infty$ String Stability**:
   - Incorporate acceleration feedforward via V2X into CACC control:
     $$u_i = k_p e_i + k_v \Delta v_i + k_a a_{i-1}$$
     Tuning $k_a = \frac{\tau_{b,i}}{h_i}$ guarantees $\|H(j\omega)\|_\infty \le 1.0$ for all $\omega \ge 0$.

---

### Phase 4: Machine Learning, XAI & Federated Architecture
1. **Implement Concrete PyTorch PINN Architecture**:
   - Build a genuine PyTorch 1D Temporal Convolutional Network (TCN).
   - Formulate composite loss with Latin Hypercube collocation sampling:
     $$\mathcal{L} = \mathcal{L}_{\text{BCE}}(y, \hat{y}) + \lambda_1 \left\| \ddot{x} - f_{\text{kinematic}}(v, a, \mu) \right\|_2^2 + \lambda_2 \operatorname{ReLU}\left(|a| - \mu g\right)^2$$
2. **Execute Authentic TreeSHAP / KernelSHAP Analysis**:
   - Install `shap` and compute attributions against a 1,000-sample baseline dataset. Report values in model output units without forcing a 1.0 sum.
3. **Execute Real Adversarial Benchmarks**:
   - Run iterative PGD on differentiable models ($L_\infty$ bound $\epsilon \in [0.01, 0.30]$).
   - For Random Forests, apply gradient-free decision boundary attacks (HopSkipJump or Zeroth-Order Optimization).
4. **Deploy Genuine 87-Client Edge FedAvg**:
   - Instantiate 87 simulated RSU clients.
   - Partition data non-IID using a Dirichlet distribution ($\operatorname{Dir}(\alpha = 0.2)$) reflecting local weather and truck volumes.
   - Execute genuine local SGD and parameter averaging: $w_{t+1} = \sum_{k=1}^{87} \frac{n_k}{n} w_{t+1}^k$.

---

### Phase 5: Empirical Statistical Rigor & Scientific Reproducibility
1. **Microscopic Trajectory Simulation & Non-Homogeneous Poisson Process**:
   - Implement the Lewis-Shedler thinning algorithm for Poisson attack arrivals:
     $$T_{i+1} = T_i - \frac{\ln U}{\lambda_{\max}}, \quad \text{accept if } U' \le \frac{\lambda(T_{i+1})}{\lambda_{\max}}$$
   - Simulate genuine vehicle platoons over discretized corridor slices.
2. **Implement Genuine Spatial Cross-Validation**:
   - Partition corridor data strictly by kilometer markers and verify zero leakage into feature preprocessors or threshold tuners.
3. **Correct Hypothesis Tests & Effect Sizes**:
   - Fix Moran's I: compute exact p-values ($p = 2(1 - \Phi(|z|))$) and acknowledge spatial randomness at the 10-interchange scale ($p = 0.4918$).
   - Report Welch's ANOVA when homoscedasticity is rejected.
   - Report Woolf's 95% Confidence Interval for Odds Ratio ($OR = 29529.2, 95\%\text{ CI } [1846.3, 472147.2]$).
4. **Honest Reporting of Theil's Inequality Coefficient**:
   - Report calculated $U = 0.3056$ and present the full decomposition table ($U_m, U_s, U_c$).
   - Explicitly declare the evaluation as a Sim-to-Sim verification rather than "Empirical Predictive Fidelity."
5. **Regenerate Publication Figures from Simulation Logs**:
   - Rewrite `generate_readme_figures.py` to plot ROC, PR, and transient curves directly from saved empirical simulation log arrays.

---

### EDITORIAL CONCLUDING REMARKS
The M-1 Motorway Cyber-Physical Digital Twin project exhibits enormous creative potential and addresses a vital transportation engineering challenge. However, IEEE Transactions on Intelligent Transportation Systems adheres to the highest standards of mathematical soundness, physical truth, and scientific reproducibility. If the authors execute the remediation roadmap outlined above—replacing mock implementations with genuine estimation filters, non-linear tire mechanics, air-brake kinetics, and authenticated machine learning architectures—this work has the potential to evolve into a landmark contribution to the intelligent transportation literature.

**Final Recommendation**: **REJECT WITH INVITATION TO RESUBMIT AS NEW MANUSCRIPT**
