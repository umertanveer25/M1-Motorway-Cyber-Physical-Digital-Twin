# Comprehensive Technical Survey & Code-Level Audit Report: Requirements R3, R4, and R5
**Project:** M-1 Motorway Cyber-Physical Digital Twin & Zero-Trust CACC  
**Auditor:** Technical Explorer (Machine Learning, Statistical Rigor & Scientific Reproducibility)  
**Date:** 2026-10-03  
**Target Venue:** IEEE Transactions on Intelligent Transportation Systems (T-ITS)

---

## 1. Executive Summary & Audit Overview

This report provides an exhaustive, ruthlessly critical, code-level investigation of **Requirements R3 (Advanced Machine Learning, XAI & Adversarial Robustness)**, **R4 (Statistical Rigor, Dataset Independence & Annual Big Data)**, and **R5 (Codebase & Reproducibility Verification)** for the M-1 Motorway Cyber-Physical Digital Twin repository.

### Summary of Major Findings
1. **Total Non-Existence of Core Machine Learning Frameworks (R3):**
   Despite prominent claims of a *Physics-Informed Neural Network (PINN)*, *SHAP Explainable AI*, *Projected Gradient Descent (PGD)* adversarial benchmarks, and an *87-node Edge Federated Learning (FedAvg)* architecture, the codebase contains **zero** PyTorch, TensorFlow, JAX, Scikit-Learn, or SHAP imports. The PINN model, loss function, and collocation points do not exist. SHAP values are stored as a static hardcoded dictionary. PGD accuracies are hardcoded floating-point arrays. Federated Learning convergence is computed via a single analytic exponential decay formula (`0.65 * exp(-t / 7.5)`).
2. **Macroscopic Toy Aggregation Masquerading as "Big Data" (R4):**
   The claimed *"365-day Big Data simulation processing 38.95M vehicle trips and 614,992 cyber-attacks"* (`controllers/m1_annual_digital_twin_engine.py`) is a 220-line script executing a simple 365-step scalar for-loop in **0.02 seconds**. Individual vehicle trajectories, packet logs, and Kalman filter executions across 38.95 million trips do not exist. Attacks are generated using `np.random.uniform`, not a Non-Homogeneous Poisson Arrival Process.
3. **Fictitious Spatial-Temporal Holdout Partition (R4):**
   The claimed spatial split (Peshawar–Rashakai KM 0–39.4 training, Rashakai–Swabi KM 39.4–72.8 validation, and Swabi–Islamabad KM 72.8–155.0 strict holdout) has **zero** implementation in any script. No dataset partition functions, data loaders, or isolated evaluation routines exist.
4. **Severe Statistical Flaws and Manufactured Significances (R4):**
   - The ANOVA ($F = 2757.26, p < 10^{-15}$) and Welch's t-test ($t = 64.53$) are calculated on synthetic numbers created by manually subtracting arbitrary offsets (e.g., $-9\%$ to $-14\%$ for SVM) from the proposed model with narrow noise.
   - Spatial autocorrelation (Moran's I) has a z-score of $z = 0.6875$, yielding a true two-tailed p-value of $p \approx 0.4918$ (statistically non-significant spatial randomness). Yet the script hardcodes `"p_value": "< 1e-4"` and falsely claims *"Strong Spatial Clustering"*.
   - The Epidemiological Odds Ratio ($OR = 29529.2$) is an artifact of setting an arbitrary $+0.5$ continuity correction against an arbitrarily chosen count of $14,759$ unprotected crashes. The 95% confidence interval ($[1,846.3, 472,147.2]$) spans over two orders of magnitude and was omitted.
5. **Physical Inevitability of Collisions Under Extreme Stress (R2/R4):**
   The claim of *"0.00% collisions across extreme stress conditions ($-8.5\text{ m/s}^2$ emergency lead braking on $-3.8\%$ grades with 44-ton freight trailers)"* is mathematically disproven by the code's own parameterization. A 44-ton trailer with pneumatic lag $\tau_b = 0.78\text{ s}$ and max deceleration $-3.6\text{ m/s}^2$ following a vehicle braking at $-8.5\text{ m/s}^2$ from $30\text{ m/s}$ requires an additional $95.5\text{ m}$ of stopping distance, whereas the mass-scaled headway gap provided is only $70.3\text{ m}$. A collision is kinematically guaranteed; the simulation achieved zero collisions only because the lead vehicle never executed emergency braking.
6. **Academic Figure Fabrication (R5):**
   `generate_readme_figures.py` generates publication ROC curves, PR curves, transient tracking responses, and PGD robustness plots directly from mathematical curve-fitting functions (e.g., $1 - e^{-35x}$, $1 - 0.005x^8$), completely bypassing actual simulation data.

---

## 2. Requirement R3: Advanced Machine Learning, XAI & Adversarial Robustness

### 2.1 Physics-Informed Neural Network (PINN) Audit
**Paper / README Claims:**
- Line 106, Table: *"Physics-Informed NN (PINN)"* achieving 99.40% Clean Test Accuracy, 95.10% Adversarial Accuracy at $\epsilon = 0.15$, 84.10% at $\epsilon = 0.30$, and 0.00% Physics Boundary Violations.
- Line 5, `controllers/m1_advanced_ml_suite.py`: *"Physics-Informed Temporal Neural Network (PI-TNN / PINN) with Newton-Pacejka constraints."*

**Code-Level Investigation:**
- **File Checked:** `controllers/m1_advanced_ml_suite.py`, `generate_readme_figures.py`, `results/m1_advanced_ml_benchmark.json`.
- **Findings:**
  1. *Architecture:* Non-existent. No `torch.nn.Module`, `tf.keras.Model`, or custom NumPy weight matrix forward-pass definition exists anywhere in the repository.
  2. *Residual Loss Formulation:* In literature (Raissi et al., 2019), a longitudinal PINN enforces Newton-Euler residual dynamics:
     $$\mathcal{L}_{\text{dyn}} = \frac{1}{N_c} \sum_{k=1}^{N_c} \left\| m_i \ddot{x}_i(t_k) - \left( F_{\text{traction}}(t_k) - F_{\text{brake}}(t_k) - F_{\text{aero}}(t_k) - F_{\text{roll}}(t_k) - m_i g \sin \theta(t_k) \right) \right\|^2$$
     and Pacejka friction boundary constraints:
     $$\mathcal{L}_{\text{tire}} = \frac{1}{N_c} \sum_{k=1}^{N_c} \max\left(0, |F_x(t_k)| - \mu_{\max} F_z(t_k)\right)^2$$
     **Zero** residual loss functions are implemented.
  3. *Collocation Points:* No sampling scheme (Latin Hypercube, Sobol, uniform spatio-temporal grid) exists.
  4. *Implementation Reality:* In `controllers/m1_advanced_ml_suite.py`:
     ```python
     # Line 73:
     acc_pinn = [99.40, 98.60, 97.20, 95.10, 92.40, 88.50, 84.10]   # Physics constraints reject non-physical PGD
     
     # Line 100:
     pinn_physics_violations = 0.00 # 0 violations
     ```
     The PINN is merely an 8-element static float array stored in memory and exported to JSON.

---

### 2.2 SHAP (SHapley Additive exPlanations) Feature Attribution Audit
**Paper / README Claims:**
- Line 102, 112, Figure 6(a): SHAP feature attribution decomposition: LiDAR vs. Radar Discrepancy ($\Delta d$) = 42.8%, RSU Doppler Spatial Consensus ($\Delta v$) = 28.5%, Longitudinal Jerk Anomaly ($da/dt$) = 14.2%, Multi-RAT Packet Jitter ($\tau_{\text{jitter}}$) = 8.1%, Spacing Error ($e_s$) = 4.2%, Velocity Residual ($e_v$) = 2.2%.

**Code-Level Investigation:**
- **File Checked:** `controllers/m1_advanced_ml_suite.py:56-68`, `generate_readme_figures.py:240-260`.
- **Findings:**
  1. *Methodology Evaluation:* SHAP (Lundberg & Lee, 2017) computes local Shapley values based on cooperative game theory:
     $$\phi_i(f, x) = \sum_{S \subseteq F \setminus \{i\}} \frac{|S|!(|F| - |S| - 1)!}{|F|!} \left[ f_x(S \cup \{i\}) - f_x(S) \right]$$
     Satisfying local efficiency: $\sum_{i=1}^M \phi_i(f, x) = f(x) - \mathbb{E}[f(X)]$. Global feature importance is defined as the mean absolute attribution: $I_j = \frac{1}{N} \sum_{k=1}^N |\phi_j(x^{(k)})|$.
  2. *Code Reality:* The SHAP library is neither imported nor installed. The entire "XAI analysis" in `m1_advanced_ml_suite.py` is:
     ```python
     # Lines 56-63:
     shap_importance = {
         "LiDAR vs. Radar Discrepancy (Delta_d)": 0.428,
         "RSU Doppler Spatial Consensus (Delta_v)": 0.285,
         "Longitudinal Jerk Anomaly (da/dt)": 0.142,
         "Multi-RAT Packet Jitter (tau_jitter)": 0.081,
         "Spacing Tracking Error (e_s)": 0.042,
         "Velocity Residual (e_v)": 0.022
     }
     ```
  3. *Artificial Sum-to-One Property:* The weights sum to exactly:
     $$0.428 + 0.285 + 0.142 + 0.081 + 0.042 + 0.022 = 1.0000$$
     In empirical SHAP applications, raw mean absolute Shapley values do not naturally sum to 1.0; they are measured in the model's output units (e.g., log-odds or probabilities).
  4. *Undefined Target Model & Baseline:* What model is being explained? ZT-MVE is claimed to be a deterministic Kalman-Bucy / $\chi^2$ statistical filter, not a machine learning model. If an ML classifier was explained, no background expectation dataset ($\mathbb{E}[f(x)]$) was defined or passed.

---

### 2.3 Adversarial Robustness & PGD Evasion Attack Benchmark
**Paper / README Claims:**
- Line 102, 108–110, Figure 6(b): Projected Gradient Descent (PGD) evasion attack benchmark for perturbation budgets $\epsilon \le 0.30$. ZT-MVE retains 99.75% accuracy; PINN achieves 84.10%; Deep MLP collapses to 50.40%; Random Forest drops to 53.00%.

**Code-Level Investigation:**
- **File Checked:** `controllers/m1_advanced_ml_suite.py:70-83`.
- **Findings:**
  1. *Lack of PGD Formulation:* Standard PGD (Madry et al., 2018) iterates:
     $$x^{t+1} = \Pi_{x + \mathcal{S}} \left( x^t + \alpha \operatorname{sign}\left(\nabla_x \mathcal{L}(\theta, x^t, y)\right) \right)$$
     The codebase defines:
     - No perturbation budget norm ($L_\infty$, $L_2$, or $L_1$).
     - No step size $\alpha$.
     - No iteration count $K$ (e.g., PGD-10, PGD-20).
     - No projection operator $\Pi_{\mathcal{S}}$ onto physical sensor limits.
     - No loss gradient calculation $\nabla_x \mathcal{L}$.
  2. *Theoretical Impossibility of Direct PGD on Random Forests:* Random Forest decision trees consist of step-wise piecewise constant partitions where $\nabla_x f(x) = 0$ almost everywhere. PGD cannot compute gradients through non-differentiable trees. Gradient-free or MILP attacks (Kantchelian et al.) are required. Claiming standard PGD against Random Forest is a technical red flag for IEEE reviewers.
  3. *Code Reality:* The benchmark consists solely of hardcoded lists:
     ```python
     # Lines 70-76:
     epsilons = [0.0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30]
     acc_zt_mve = [99.98, 99.95, 99.92, 99.88, 99.85, 99.80, 99.75]
     acc_pinn = [99.40, 98.60, 97.20, 95.10, 92.40, 88.50, 84.10]
     acc_deep_mlp = [97.85, 91.20, 83.40, 74.50, 66.80, 58.20, 50.40]
     acc_random_forest = [98.42, 92.50, 85.10, 76.80, 68.40, 61.20, 53.00]
     acc_svm = [96.12, 88.40, 78.90, 69.10, 59.80, 51.50, 44.20]
     ```

---

### 2.4 Federated Learning (87-Node Edge FedAvg) Audit
**Paper / README Claims:**
- Line 102, 113, Figure 6(c): 87-node edge Federated Learning (FedAvg) across 155 km corridor RSUs achieving 99.65% consensus accuracy in 50 communication rounds, with 99.2% backhaul bandwidth reduction (142.8 TB/year down to 1.14 TB/year).

**Code-Level Investigation:**
- **File Checked:** `controllers/m1_advanced_ml_suite.py:85-98`, `controllers/m1_rsu_and_ev_engine.py:30-70`.
- **Findings:**
  1. *Algorithm Formulation:* FedAvg (McMahan et al., 2017) requires client local updates and weighted parameter aggregation:
     $$w_{t+1} = \sum_{k=1}^K \frac{n_k}{n} w_{t+1}^k, \quad w_{t+1}^k = \operatorname{LocalSGD}(w_t, \mathcal{D}_k, E)$$
  2. *Code Reality:* The 50-round convergence is generated by evaluating an analytical formula:
     ```python
     # Lines 85-88:
     rounds = np.arange(1, 51)
     fed_loss = 0.65 * np.exp(-rounds / 7.5) + 0.015 + np.random.normal(0, 0.002, 50)
     fed_acc = 100.0 * (1.0 - 0.45 * np.exp(-rounds / 6.8)) + np.random.normal(0, 0.15, 50)
     fed_acc = np.clip(fed_acc, 55.0, 99.65)
     ```
  3. *Disconnection from RSU Topology:* In `m1_rsu_and_ev_engine.py`, 87 RSUs are created as metadata dictionaries with names like `M1-RSU-001` and `"processor": "NVIDIA Jetson AGX Orin 64GB"`. However, `m1_advanced_ml_suite.py` never imports or interfaces with this list. No simulated RSU client holds local datasets or trains local weights.
  4. *Absence of Non-IID Handling:* In reality, M-1 traffic exhibits severe spatial-temporal non-IID skew: Swabi RSUs experience dense winter fog ($>80\%$ moisture noise), Rashakai RSUs handle overnight 22-wheeler container freight, and Islamabad/Peshawar RSUs process daytime commuter sedans. Under non-IID data distributions ($\alpha_{\text{Dirichlet}} < 0.2$), standard FedAvg suffers from severe client drift and oscillations. Synthesizing smooth exponential convergence without addressing client drift is scientifically invalid.
  5. *Bandwidth Claims:*
     ```python
     centralized_bandwidth_tb_year = 142.8 # Raw video/radar streaming
     federated_bandwidth_tb_year = 1.14     # Gradient sync only (99.2% bandwidth reduction)
     ```
     These are hardcoded constants. 142.8 TB / 38.95M trips equals 3.66 MB per 155 km trip (equivalent to 0.68 KB/s), which is orders of magnitude too low for raw video/radar streaming (typically 5–10 GB/hour).

---

## 3. Requirement R4: Statistical Rigor, Dataset Independence & Annual Big Data

### 3.1 365-Day Big Data Simulation (38.95M Trips, 614,992 Attacks)
**Paper / README Claims:**
- Line 171–172: *"The 614,992 cyber-attacks across 38.95M trips were generated using a Non-Homogeneous Poisson Arrival Process ($N(t) \sim \text{Poisson}(\lambda(t))$) with baseline $\lambda_0 = 70.2\text{ attacks/hour}$, incorporating seasonal and spatial burst multipliers near Swabi winter fog ($\times 2.4$) and Indus River downpours ($\times 1.8$)."*

**Code-Level Investigation:**
- **File Checked:** `controllers/m1_annual_digital_twin_engine.py:80-184`.
- **Findings:**
  1. *Scalar Loop Execution:* The 365-day "Big Data simulation" executes in **0.02 seconds** on a standard CPU:
     ```python
     # Line 81:
     for month in range(1, 13):
         ...
         for d in range(1, days_in_month + 1):
             day_of_year += 1
             ...
             daily_volume = int(base_daily_volume * np.random.uniform(0.96, 1.04))
             day_cav_trips = int(daily_volume * cav_penetration)
             day_attacks = int(day_cav_trips * 0.025 * np.random.uniform(0.85, 1.15))
             day_detected = int(day_attacks * detection_rate)
             day_collisions_with_zt = 0
             day_collisions_without_zt = int(day_attacks * (1.0 - 0.15) * (0.02 if not is_foggy else 0.08))
             day_co2_saved_kg = day_cav_trips * 1.85 * (day_flow_gain_pct / 100.0)
     ```
  2. *Absence of Microscopic Trips:* Not a single individual vehicle trip, platoon interaction, or physical trajectory is computed in this annual engine. It is an annual macroscopic scalar accounting tally.
  3. *Absence of Poisson Process:* The code uses `np.random.uniform(0.85, 1.15)`, not a Non-Homogeneous Poisson Arrival Process. There is no intensity integration $\Lambda(t) = \int_0^t \lambda(s) ds$, no thinning algorithm (Lewis-Shedler), and no exponential inter-arrival generation.

---

### 3.2 Spatial-Temporal Holdout Partitioning & Data Leakage
**Paper / README Claims:**
- Line 173–176:
  - *Training Set (70%):* Simulated trajectories from Peshawar to Rashakai (KM 0.0–39.4).
  - *Validation Set (15%):* Rashakai to Swabi (KM 39.4–72.8).
  - *Strict Holdout Test Set (15%):* Swabi to Islamabad (KM 72.8–155.0) — completely unseen corridor topology, mountain grades, and adverse weather profiles during training.

**Code-Level Investigation:**
- **Files Checked:** `controllers/*.py`, `run_all_benchmarks.py`.
- **Findings:**
  1. *Complete Non-Existence of Dataset Partitions:* A search for partition functions, training routines, or spatial segment filtering across the entire `controllers/` directory yields zero occurrences.
  2. *Contamination and Data Leakage:* In `controllers/m1_real_physics_engine.py`:
     ```python
     # Line 192:
     detection_threshold = 9.21 * (1.0 + 0.35 * fog_density + 0.02 * rain_rate_mm_hr)
     ```
     The detection threshold is a global hand-tuned formula parameterized by `fog_density` (which reaches 0.85 specifically in Swabi, KM 80–120) and `rain_rate_mm_hr` (which occurs in Indus/Burhan, KM > 120). If this threshold was tuned using corridor-wide parameters, it constitutes direct information leakage from the supposed holdout test set into the detection rule.

---

### 3.3 Spatial Autocorrelation & Moran's I Audit
**Paper / README Claims:**
- Line 29: Moran's I spatial autocorrelation test across 10 NHA Interchanges proving spatial clustering around Swabi and Indus Bridge ($p < 10^{-4}$).

**Code-Level Investigation:**
- **File Checked:** `controllers/m1_comprehensive_statistical_suite.py:298-346`.
- **Code Snippet:**
  ```python
  # Lines 300-317:
  ic_kms = np.array([0.0, 15.2, 45.1, 62.4, 88.0, 105.3, 115.8, 128.5, 142.1, 155.0])
  incident_density = np.array([320, 480, 890, 710, 2450, 1120, 2180, 840, 520, 610])
  
  # Compute Moran's I
  z = incident_density - np.mean(incident_density)
  s0 = np.sum(W)
  moran_i = (n_ic / s0) * np.sum(W * np.outer(z, z)) / np.sum(z**2)
  moran_z = (moran_i - (-1.0 / (n_ic - 1))) / 0.18 # Spatial standard deviation approx
  
  # Lines 341-346:
  "spatial_autocorrelation_morans_i": {
      "morans_i": round(float(moran_i), 4),
      "z_score": round(float(moran_z), 4),
      "p_value": "< 1e-4",
      "interpretation": "Strong Spatial Clustering of Cyber/Weather Incidents..."
  }
  ```
- **Rigorous Mathematical Verification:**
  - Calculated Moran's $I = 0.0126$.
  - Theoretical expectation under spatial randomness: $\mathbb{E}[I] = -\frac{1}{N-1} = -\frac{1}{9} \approx -0.1111$.
  - Calculated z-score:
    $$z = \frac{0.0126 - (-0.1111)}{0.18} = 0.6875$$
  - In a standard normal distribution $\mathcal{N}(0, 1)$, the two-tailed p-value for $z = 0.6875$ is:
    $$p = 2 \times \left(1 - \Phi(0.6875)\right) = 2 \times (1 - 0.7541) = \mathbf{0.4918}$$
  - **The Blatant Scientific Misrepresentation:** A p-value of $0.4918$ indicates that the observed spatial pattern is **entirely consistent with random chance** ($p \gg 0.05$). Yet line 344 hardcodes `"p_value": "< 1e-4"`. The author falsified the p-value by substituting an arbitrary string instead of computing `2 * (1 - stats.norm.cdf(abs(moran_z)))`.

---

### 3.4 Parametric & Non-Parametric Hypothesis Tests (ANOVA & Welch's t-Test)
**Paper / README Claims:**
- One-Way ANOVA across detection models ($F = 2757.26, p < 10^{-15}, \eta^2 = 0.8632$).
- Welch's Two-Sample t-test ($t = 64.53, p < 10^{-15}$).

**Code-Level Investigation:**
- **File Checked:** `controllers/m1_comprehensive_statistical_suite.py:74-147`.
- **How the Data Was Generated:**
  ```python
  # Lines 81-85:
  daily_acc_rf  = np.clip(daily_acc_zt - np.random.uniform(2.5, 4.0, len(days)) - fog_mask * 3.5 - rain_mask * 2.0, 88.0, 96.5)
  daily_acc_mlp = np.clip(daily_acc_zt - np.random.uniform(4.5, 7.0, len(days)) - fog_mask * 5.5 - rain_mask * 3.0, 82.0, 93.5)
  daily_acc_svm = np.clip(daily_acc_zt - np.random.uniform(9.0, 14.0, len(days)) - fog_mask * 9.0 - rain_mask * 5.0, 72.0, 86.5)
  daily_acc_rb  = np.clip(daily_acc_zt - np.random.uniform(14.0, 19.0, len(days)) - fog_mask * 12.0 - rain_mask * 7.0, 65.0, 82.0)
  daily_acc_if  = np.clip(daily_acc_zt - np.random.uniform(22.0, 32.0, len(days)) - fog_mask * 18.0 - rain_mask * 10.0, 52.0, 72.0)
  ```
- **Methodological Evaluation:**
  1. The baseline comparisons are not generated by running alternative models on test data. They are synthesized by subtracting fixed, non-overlapping offsets from `daily_acc_zt` with artificially suppressed variance.
  2. An ANOVA $F$-test on groups constructed to have non-overlapping mean shifts of 4 to 25 percentage points with tiny variances ($<1.0$) mathematically guarantees an extreme $F$-statistic ($F = 2757.26$). This is statistical circularity.
  3. *Homoscedasticity Violation:* Levene's test (`stats.levene`) and Bartlett's test in line 242 reject equal variance ($p < 10^{-15}$). Standard ANOVA assumes homoscedasticity; when variances differ by orders of magnitude, standard ANOVA $F$-tests are biased and invalid.
  4. *Internal Contradiction:* In `controllers/m1_multi_algorithm_benchmark.py:260`, the hardcoded test table reports:
     `{"pair": "ZT-MVE vs. SVM RBF", "t_stat": 158.20, "cohens_d": 17.84}`
     Whereas `m1_comprehensive_statistical_suite.py:26` reports:
     `"welch_t_stat": 64.5333, "cohens_d": 4.777`
     The repository contradicts itself by a factor of 2.5× on the exact same metric.

---

### 3.5 Epidemiological Odds Ratio ($OR = 29529.2$) & Relative Risk Audit
**Paper / README Claims:**
- Line 29, 353: Epidemiological Odds Ratio $OR = 29529.2$ and Relative Risk $RR = 29518.0$, demonstrating that unprotected CACC has $>29,500\times$ higher risk of collision.

**Code-Level Investigation:**
- **File Checked:** `controllers/m1_comprehensive_statistical_suite.py:327-356`.
- **2x2 Contingency Table in Code:**
  ```python
  # Lines 333-338:
  a = 14759          # Crashes under Standard CACC
  b = 38931495       # No Crash under Standard CACC
  c = 0.5            # Continuity correction for ZT-CACC (0 observed crashes)
  d = 38946254       # No Crash under ZT-CACC
  odds_ratio = (a * d) / (b * c)
  relative_risk = (a / (a + b)) / (c / (c + d))
  ```
- **Flaws & Derivation of Missing 95% Confidence Interval:**
  1. The cell count $a = 14,759$ was arbitrarily chosen in `controllers/m1_rsu_and_ev_engine.py:87`.
  2. Because ZT-CACC observed exactly zero crashes ($c = 0$), the raw odds ratio is undefined ($\infty$). To circumvent this, the author applied an asymmetric continuity correction ($c = 0.5$) only to the zero cell while leaving the other cells unadjusted.
  3. The resulting point estimate is completely arbitrary:
     - If $c = 0.1$, $OR = 147,646.0$.
     - If $c = 0.5$, $OR = 29,529.2$.
     - If $c = 1.0$, $OR = 14,764.6$.
  4. The code failed to report the 95% Confidence Interval. Using Woolf's logit variance:
     $$\operatorname{SE}(\ln OR) = \sqrt{\frac{1}{a} + \frac{1}{b} + \frac{1}{c} + \frac{1}{d}} \approx \sqrt{\frac{1}{14759} + 0 + \frac{1}{0.5} + 0} = \sqrt{2.000068} \approx 1.4142$$
     $$95\% \text{ CI of } \ln OR = \ln(29529.2) \pm 1.96 \times 1.4142 = 10.2931 \pm 2.7719 = [7.5212, 13.0650]$$
     $$\mathbf{95\% \text{ CI of } OR} = [\exp(7.5212), \exp(13.0650)] = \mathbf{[1,846.3, \ 472,147.2]}$$
     A confidence interval spanning nearly three orders of magnitude reflects extreme parameter sensitivity caused by zero-cell imputation, making it unpublishable without exact Poisson/binomial mid-$p$ adjustments.

---

### 3.6 Boundary Stress Conditions & 0.00% Collisions Claim
**Paper / README Claims:**
- Line 184–192: *"Zero collisions ($0.00\%$)" across $N = 20,000$ closed-loop stress scenarios*, including:
  - Emergency lead braking at maximum friction limit ($a_{\text{lead}} = -8.5\text{ m/s}^2$).
  - 44-ton heavy freight trailers with pneumatic brake lag $\tau_b = 0.78\text{ s}$.
  - Severe downhill grades ($-3.8\%$ descent near Burhan / Hasanabdal).
  - Reduced tire adhesion down to monsoon rain limits ($\mu = 0.48$).

**Kinematic Proof of Inevitable Collision Under Code Parameters:**
Let us analyze whether a 44-ton trailer following a passenger car under these parameters can avoid a rear-end collision:
1. **Initial Conditions:** Speed $v_0 = 30.0\text{ m/s}$ (108 km/h).
2. **Lead Vehicle Deceleration:** $a_{\text{lead}} = -8.5\text{ m/s}^2$. Hydraulic lag $\tau_l = 0.18\text{ s}$.
   Stopping distance of lead car:
   $$d_{\text{stop, lead}} \approx v_0 \tau_l + \frac{v_0^2}{2 |a_{\text{lead}}|} = 30 \times 0.18 + \frac{900}{17.0} = 5.4 + 52.94 = \mathbf{58.34\text{ m}}$$
3. **Follower Trailer Deceleration:** Mass $m = 38,000\text{ kg}$, pneumatic actuator lag $\tau_b = 0.78\text{ s}$.
   In `controllers/m1_real_physics_engine.py:23`, max brake deceleration is capped at:
   $$a_{\text{max\_brake}} = -3.6\text{ m/s}^2$$
   (Under wet asphalt $\mu = 0.48$, the tire limit is $-0.48 \times 9.81 \times 0.90 = -4.24\text{ m/s}^2$, so the vehicle is actuator-limited to $-3.6\text{ m/s}^2$).
   Stopping distance of follower trailer:
   $$d_{\text{stop, trailer}} = v_0 \tau_b + \frac{v_0^2}{2 |a_{\text{trailer}}|} = 30 \times 0.78 + \frac{900}{2 \times 3.6} = 23.4 + 125.0 = \mathbf{148.40\text{ m}}$$
4. **Minimum Safe Separation Required:**
   $$d_{\text{required}} = d_{\text{stop, trailer}} - d_{\text{stop, lead}} = 148.40 - 58.34 = \mathbf{90.06\text{ meters}}$$
   (On a $-3.8\%$ downgrade, gravity adds $+g \sin(0.038) \approx +0.37\text{ m/s}^2$, reducing effective braking to $-3.23\text{ m/s}^2$, expanding required gap to $>105\text{ m}$).
5. **Separation Provided by the Code:**
   In `controllers/m1_real_physics_engine.py:205-212`:
   ```python
   tau_b = 0.78
   m_ratio = 38000.0 / 1500.0 = 25.333
   base_h = 1.2 # under attack detection
   h_dynamic = 1.2 + 0.5 * 0.78 + 0.03 * math.sqrt(25.333) = 1.2 + 0.39 + 0.151 = 1.741 s
   d_standstill = 8.0 + 2.0 * math.sqrt(25.333) = 8.0 + 10.066 = 18.07 m
   target_gap = d_standstill + h_dynamic * cur_vel = 18.07 + 1.741 * 30.0 = 70.30 meters
   ```
6. **The Collision Deficit:**
   $$\text{Headway Gap Provided} = 70.30\text{ m} \quad < \quad \text{Distance Required} = 90.06\text{ m}$$
   $$\mathbf{\text{Deficit} = -19.76\text{ meters}}$$
   **Kinematic Conclusion:** If the lead vehicle executes emergency braking at $-8.5\text{ m/s}^2$, the heavy trailer following at $70.3\text{ m}$ **must collide** with the lead vehicle at an impact velocity of approximately $\Delta v_{\text{impact}} \approx \sqrt{2 \times (4.9) \times 19.76} \approx 13.9\text{ m/s}$ (50 km/h).
7. **Why Did the Code Report 0 Collisions?**
   In `controllers/m1_real_physics_engine.py`:
   ```python
   # Lines 102-104:
   target_lead_vel = 30.0 + 1.2 * math.sin(0.04 * t)
   lead_acc_cmd = 0.8 * (target_lead_vel - dt_vel[0])
   ```
   The lead vehicle **never brakes at $-8.5\text{ m/s}^2$**! It gently oscillates by $\pm 1.2\text{ m/s}$ around $30\text{ m/s}$, never exceeding accelerations of $\pm 1.0\text{ m/s}^2$. Furthermore, downhill grade resistance ($m g \sin \theta$) is omitted entirely from the equations of motion. The claimed extreme stress envelope was never executed.

---

## 4. Requirement R5: Codebase Architecture & Reproducibility Verification

### 4.1 Dependency Manifest (`requirements.txt`) Deficiencies
`requirements.txt` contains only 4 dependencies:
```
numpy>=1.24.0
scipy>=1.10.0
matplotlib>=3.7.0
pandas>=2.0.0
```
Missing dependencies necessary to support paper claims:
- `torch` or `tensorflow` (claimed for PINN, Deep MLP, PGD).
- `scikit-learn` (claimed for Random Forest, SVM, Isolation Forest).
- `shap` (claimed for SHAP explainability).

---

### 4.2 Numerical Precision, Matrix Inversions, and Edge Cases
1. **Division by Zero Hazards:**
   - In `controllers/m1_real_physics_engine.py:318`:
     `total_energy_kwh_per_100km_dt = float((np.sum(dt_energy_joules) / 3.6e6) / (re_pos[0]/1e5))`
     If `re_pos[0] == 0.0` (at simulation start), division by zero will raise an unhandled exception.
   - In `controllers/m1_comprehensive_statistical_suite.py:121`:
     `s_pooled = np.sqrt((np.var(daily_acc_zt, ddof=1) + np.var(m_data, ddof=1)) / 2.0)`
     `cohens_d = (np.mean(daily_acc_zt) - np.mean(m_data)) / s_pooled`
     If variances are identical and zero, `s_pooled = 0`, producing `NaN`.
2. **Arbitrary Epsilon Term Distortion:**
   In `controllers/m1_multi_algorithm_benchmark.py:138-140`:
   ```python
   prec = tp / (tp + fp + 1e-9) * 100
   rec = tp / (tp + fn + 1e-9) * 100
   f1 = 2 * (prec * rec) / (prec + rec + 1e-9)
   ```
   When `tp = 0, fp = 0`, `prec` becomes $0.0$; however, if scaled improperly, $10^{-9}$ denominators can create numerical precision artifacts across floating-point representations.

---

### 4.3 Systematic Discrepancy Matrix: Code Logic vs. README Claims

| Performance Dimension | README.md Claim | Codebase Reality | Discrepancy Severity | Root Cause / File Reference |
| :--- | :--- | :--- | :--- | :--- |
| **PINN Model** | Residual-enforced PINN ($99.40\%$ acc) | No NN model in repository | 🔴 Fatal | `m1_advanced_ml_suite.py:73` (static array) |
| **SHAP XAI** | Calculated SHAP attributions | Static dictionary constants | 🔴 Fatal | `m1_advanced_ml_suite.py:56-63` |
| **PGD Evasion** | Iterative gradient projection | Static array lookup | 🔴 Fatal | `m1_advanced_ml_suite.py:70-76` |
| **87-Node FedAvg** | Multi-client RSU federated aggregation | Analytic exponential formula | 🔴 Fatal | `m1_advanced_ml_suite.py:86-87` |
| **365-Day Big Data** | 38.95M microscopic trips simulated | 365-iteration scalar loop (0.02s) | 🔴 Fatal | `m1_annual_digital_twin_engine.py:81` |
| **Cyber Attack Model** | Non-homogeneous Poisson Process | `np.random.uniform(0.85, 1.15)` | 🔴 Fatal | `m1_annual_digital_twin_engine.py:112` |
| **Spatial Holdout Split** | KM 0–39.4 train / KM 72.8–155 holdout | Zero split logic in codebase | 🔴 Fatal | Entire repository lacks train/test splits |
| **Moran's I p-value** | $p < 10^{-4}$ (Strong Clustering) | True $p = 0.4918$ ($z = 0.6875$) | 🔴 Fatal | `m1_comprehensive_statistical_suite.py:344` |
| **Pacejka '89 Model** | Non-linear tire slip curve $\mu(\kappa)$ | Coulomb friction $\mu \cdot g \cdot 0.90$ | 🟠 Major | `m1_real_physics_engine.py:247` |
| **Lead Emergency Braking**| Tested at $-8.5\text{ m/s}^2$ lead decel | Lead decel capped at $\pm 1.0\text{ m/s}^2$ | 🔴 Fatal | `m1_real_physics_engine.py:102-104` |
| **Burhan Downhill Grade**| $-3.8\%$ descent modeled | Grade resistance term $\sin \theta = 0$ | 🟠 Major | `m1_real_physics_engine.py:237` |
| **ML Inference Latency** | ZT-MVE $82.4\ \mu\text{s}$, MLP $850.2\ \mu\text{s}$ | ZT-MVE $4.81\ \mu\text{s}$, MLP $92.1\ \mu\text{s}$ | 🟠 Major | Table in README vs `m1_multi_algorithm_benchmark.py:125` |

---

### 4.4 Academic Figure Generation Analysis (`generate_readme_figures.py`)
In `generate_readme_figures.py`, academic figures presented as empirical results are generated using mathematical equations rather than reading simulation output:
1. **Figure 3(a) ROC Curves (Lines 101–106):**
   ```python
   fpr = np.linspace(0, 1, 200)
   tpr_zt = 1.0 - np.exp(-35.0 * fpr)
   tpr_rf = 1.0 - np.exp(-12.0 * fpr)
   tpr_mlp = 1.0 - np.exp(-9.0 * fpr)
   tpr_svm = 1.0 - np.exp(-6.0 * fpr)
   tpr_rule = 1.0 - np.exp(-4.0 * fpr)
   ```
   The ROC curves are exponential functions ($1 - e^{-k \cdot \text{fpr}}$), not evaluated threshold sweeps.
2. **Figure 3(b) Precision-Recall Curves (Lines 122–127):**
   ```python
   recall = np.linspace(0, 1, 200)
   prec_zt = 1.0 - 0.005 * (recall**8)
   prec_rf = 1.0 - 0.08 * (recall**4)
   ```
   The Precision-Recall curves are generated from polynomial power laws.
3. **Figure 4(a) Transient Spacing Response (Lines 154–155):**
   ```python
   ideal_spacing = 18.0 + 8.0 * (1.0 - np.exp(-1.5 * (time_s - 5.0))) * (time_s >= 5.0)
   real_spacing = 18.0 + 8.0 * (1.0 - np.exp(-0.85 * (time_s - 5.2))) * (time_s >= 5.2) + 0.18 * np.sin(4.0 * time_s)
   ```
   The physical transient response under attack is generated using an artificial step response formula with a sine wave offset.

---

## 5. Actionable Line-by-Line Remediation Recommendations for Top-Tier Publication

To elevate this codebase to the standards of **IEEE Transactions on Intelligent Transportation Systems (T-ITS)**, the following remediation steps are required:

### Phase 1: Genuine Machine Learning & Explainability Implementation
1. **Implement Concrete PyTorch Models:**
   - Define a genuine PyTorch 1D Temporal Convolutional Network (TCN) or LSTM for baseline temporal anomaly detection.
   - For the PINN, formulate the composite loss:
     $$\mathcal{L} = \mathcal{L}_{\text{BCE}}(y, \hat{y}) + \lambda_1 \left\| \ddot{x} - f_{\text{kinematic}}(v, a, \mu) \right\|_2^2 + \lambda_2 \operatorname{ReLU}\left(|a| - \mu g\right)^2$$
   - Implement actual Latin Hypercube Collocation sampling and train the model using Adam + L-BFGS.
2. **Execute Authentic SHAP Analysis:**
   - Install `shap` and compute KernelExplainer or TreeExplainer on a 1,000-sample background baseline dataset.
   - Report mean absolute Shapley values ($|\phi_j|$) in original units without forcing a 100% sum.
3. **Execute Real PGD Adversarial Attacks:**
   - Implement the iterative projected gradient descent loop on differentiable models under an explicit $L_\infty$ bound ($\epsilon \in [0.01, 0.30]$, step size $\alpha = \epsilon / 10$, iterations $K = 20$).
   - For decision trees and Random Forests, replace PGD with a gradient-free attack (e.g., HopSkipJump or Zeroth-Order Optimization).
4. **Implement True Federated Learning:**
   - Instantiate 87 simulated client nodes corresponding to corridor RSUs.
   - Partition data non-IID across nodes using a Dirichlet distribution ($\operatorname{Dir}(\alpha = 0.2)$) reflecting local weather and truck ratios.
   - Implement authentic FedAvg parameter averaging: $w_{t+1} = \sum_{k=1}^{87} \frac{n_k}{n} w_{t+1}^k$.

### Phase 2: Microscopic Simulation Engine Scaling
1. **Replace Scalar Loop with Mesoscopic / Microscopic Batch Simulation:**
   - Simulate genuine vehicle platoons over discretized corridor slices using vectorization (e.g., simulating 1,000 platoons across 10 weather scenarios, yielding $10^6$ vehicle-km).
2. **Implement True Non-Homogeneous Poisson Arrival Process:**
   - Use the Lewis-Shedler thinning algorithm:
     $$T_{i+1} = T_i - \frac{\ln U}{\lambda_{\max}}, \quad \text{accept if } U' \le \frac{\lambda(T_{i+1})}{\lambda_{\max}}$$
     with $\lambda(t) = \lambda_0 \cdot S_{\text{season}}(t) \cdot M_{\text{spatial}}(x)$.

### Phase 3: Statistical Rigor & Scientific Integrity
1. **Fix Moran's I Calculation:**
   - Replace the hardcoded string `"< 1e-4"` in `m1_comprehensive_statistical_suite.py:344` with the true p-value calculation:
     ```python
     moran_p = 2.0 * (1.0 - stats.norm.cdf(abs(moran_z)))
     ```
   - Acknowledge that at the 10-interchange level, spatial autocorrelation is not statistically significant ($p = 0.49$), or compute Moran's I at the 87-RSU resolution where fine-grained fog clustering may produce significant results.
2. **Sanitize Hypothesis Tests:**
   - Run ANOVA and t-tests exclusively on real cross-validation folds from distinct simulation runs, rather than manually subtracting constants.
   - Report Welch's ANOVA or Brown-Forsythe when homoscedasticity is rejected by Levene's test.
3. **Correct Epidemiological Odds Ratio:**
   - Calculate and report the complete 95% Confidence Interval using Woolf's logit method or exact Poisson mid-$p$ intervals.
   - Acknowledge the zero-cell event constraint rather than presenting an arbitrary point estimate ($29,529.2$).

### Phase 4: Extreme Kinematic Stress Hardening
1. **Correct Headway Formula for Heavy Commercial Fleets:**
   - To guarantee zero collisions during an emergency stop ($a_{\text{lead}} = -8.5\text{ m/s}^2$) with a 44-ton trailer ($a_{\text{trailer}} = -3.6\text{ m/s}^2, \tau_b = 0.78\text{ s}$), dynamic headway must satisfy the physical stopping distance deficit:
     $$h_i(m_i, \tau_b) \ge \tau_b + \frac{v_0}{2} \left( \frac{1}{|a_{\text{max}, i}|} - \frac{1}{|a_{\text{lead, max}}|} \right)$$
     At $v_0 = 30\text{ m/s}$, the headway must be at least:
     $$h \ge 0.78 + 15 \times \left( \frac{1}{3.6} - \frac{1}{8.5} \right) = 0.78 + 15 \times (0.2778 - 0.1176) = 0.78 + 2.40 = \mathbf{3.18\text{ seconds}}$$
     (corresponding to a separation gap of $>95\text{ meters}$).
2. **Incorporate Road Grade Dynamics:**
   - Add road grade force $F_{\text{grade}} = m g \sin \theta$ to vehicle state acceleration equations.
3. **Execute True Emergency Stop In Simulation:**
   - Subject the follower platoon to an actual $-8.5\text{ m/s}^2$ step deceleration in `m1_real_physics_engine.py` to empirically validate collision avoidance under the expanded headway policy.

---
*End of Technical Survey Report.*
