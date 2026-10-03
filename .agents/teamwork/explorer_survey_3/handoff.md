# Handoff Report: Explorer Survey 3 (Requirements R3, R4, and R5)
**Subagent ID:** explorer_survey_3  
**Target Recipient:** Orchestrator (`7e85f2e3-f7e9-48a9-b95d-91c18629e7cc`)  
**Working Directory:** `C:\Users\umert\.gemini\antigravity\scratch\m1_digital_twin\.agents\teamwork\explorer_survey_3`  
**Date:** 2026-10-03  
**Status:** Complete (Hard Handoff)

---

## 1. Observation

Direct observations and evidence collected from code inspection across the repository:

1. **Absence of Core ML / DL Libraries:**
   - File: `requirements.txt:1-5`.
   - Content: Only contains `numpy>=1.24.0`, `scipy>=1.10.0`, `matplotlib>=3.7.0`, `pandas>=2.0.0`.
   - Packages `torch`, `tensorflow`, `jax`, `scikit-learn`, and `shap` are absent.

2. **PINN Model Non-Existence & Hardcoded Results:**
   - File: `controllers/m1_advanced_ml_suite.py:73, 100`.
   - Lines:
     ```python
     acc_pinn = [99.40, 98.60, 97.20, 95.10, 92.40, 88.50, 84.10]   # Physics constraints reject non-physical PGD
     pinn_physics_violations = 0.00 # 0 violations
     ```
   - Zero lines of code defining neural network layers, loss functions, residual enforcement of Newton-Euler dynamics, or collocation points exist.

3. **SHAP Feature Attribution Hardcoded Dictionary:**
   - File: `controllers/m1_advanced_ml_suite.py:56-63`.
   - Lines:
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
   - Sum equals exactly $1.000$. No SHAP calculations, game-theoretic formulations, or background datasets are present.

4. **Adversarial PGD Benchmark Hardcoded Arrays:**
   - File: `controllers/m1_advanced_ml_suite.py:70-76`.
   - Lines:
     ```python
     epsilons = [0.0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30]
     acc_zt_mve = [99.98, 99.95, 99.92, 99.88, 99.85, 99.80, 99.75]
     acc_pinn = [99.40, 98.60, 97.20, 95.10, 92.40, 88.50, 84.10]
     acc_deep_mlp = [97.85, 91.20, 83.40, 74.50, 66.80, 58.20, 50.40]
     acc_random_forest = [98.42, 92.50, 85.10, 76.80, 68.40, 61.20, 53.00]
     acc_svm = [96.12, 88.40, 78.90, 69.10, 59.80, 51.50, 44.20]
     ```
   - Zero gradient iterations, perturbation norms ($L_\infty / L_2$), step sizes, or projections exist.

5. **Federated Learning Convergence via Analytic Formula:**
   - File: `controllers/m1_advanced_ml_suite.py:85-88`.
   - Lines:
     ```python
     rounds = np.arange(1, 51)
     fed_loss = 0.65 * np.exp(-rounds / 7.5) + 0.015 + np.random.normal(0, 0.002, 50)
     fed_acc = 100.0 * (1.0 - 0.45 * np.exp(-rounds / 6.8)) + np.random.normal(0, 0.15, 50)
     ```
   - No client training, non-IID partitioning, or model aggregation occurs.

6. **Annual Big Data Engine as a 365-Iteration Scalar Loop:**
   - File: `controllers/m1_annual_digital_twin_engine.py:80-146`.
   - Script runs in 0.02 seconds. Attacks are drawn using `np.random.uniform(0.85, 1.15)` (line 112), not a Poisson arrival process. Trips are computed via scalar multiplication.

7. **Moran's I Critical Statistical Misrepresentation:**
   - File: `controllers/m1_comprehensive_statistical_suite.py:317, 343-344`.
   - Lines:
     ```python
     moran_z = (moran_i - (-1.0 / (n_ic - 1))) / 0.18 # evaluates to 0.6875
     "z_score": round(float(moran_z), 4),
     "p_value": "< 1e-4",
     "interpretation": "Strong Spatial Clustering..."
     ```
   - For $z = 0.6875$, the true two-tailed standard normal p-value is $p = 2(1 - \Phi(0.6875)) = 0.4918$. The string `"< 1e-4"` was hardcoded.

8. **Epidemiological Odds Ratio Artifact & Missing Confidence Interval:**
   - File: `controllers/m1_comprehensive_statistical_suite.py:333-338`.
   - Point estimate $OR = 29529.2$ is derived by imputing $c = 0.5$ on a zero-event cell ($a = 14759, b = 38931495, c = 0.5, d = 38946254$). The 95% CI is omitted; Woolf's logit method yields $[1,846.3, \ 472,147.2]$.

9. **Kinematic Deceleration Deficit on Heavy Commercial Trailers:**
   - File: `controllers/m1_real_physics_engine.py:23, 102-104, 208-212`.
   - Heavy trailer ($38\text{ t}, \tau_b = 0.78\text{ s}, a_{\max} = -3.6\text{ m/s}^2$) requires $148.4\text{ m}$ to stop from $30\text{ m/s}$. Lead vehicle braking at $-8.5\text{ m/s}^2$ stops in $58.3\text{ m}$. Required safe gap is $90.1\text{ m}$. Dynamic headway provides only $70.3\text{ m}$ (a $19.8\text{ m}$ shortfall). In the simulation, lead vehicle acceleration is restricted to $\pm 1.0\text{ m/s}^2$, masking the inevitable collision.

10. **Synthetic Figure Construction Bypassing Simulation Data:**
    - File: `generate_readme_figures.py:101-106, 122-127, 154-155`.
    - ROC curves are generated using `1.0 - np.exp(-k * fpr)`; PR curves via `1.0 - c * recall**p`; transient spacing curves via `18.0 + 8.0 * (1 - np.exp(-k*(t-5))) + 0.18 * sin(4t)`.

---

## 2. Logic Chain

1. **Premise 1 (Absence of Software Foundations):** From Observation 1, no deep learning or machine learning libraries are installed or imported.
2. **Inference 1:** All claims attributing specific numerical metrics to deep learning architectures (PINN, Deep MLP, Tree SHAP, PGD attacks) cannot have been computed through actual model evaluation.
3. **Premise 2 (Direct Evidence of Mock Implementations):** From Observations 2, 3, 4, and 5, PINN violation rates, SHAP values, PGD accuracy arrays, and FL convergence curves are explicitly coded as static numbers or trivial mathematical functions.
4. **Inference 2:** Requirements R3 claims are non-empirical placeholders.
5. **Premise 3 (Data Generation Disconnect):** From Observation 6, the annual Big Data simulation is a macroscopic scalar loop executing in 0.02s without trip-level trajectories or Poisson arrivals.
6. **Inference 3:** Claims of simulating 38.95M trips and 614k Poisson attacks are scientifically unfounded.
7. **Premise 4 (Statistical Fabrication):** From Observation 7, a z-score of $0.6875$ ($p = 0.4918$) was paired with a hardcoded string `"< 1e-4"`.
8. **Inference 4:** The statistical significance of spatial clustering along M-1 was fabricated.
9. **Premise 5 (Kinematic Stopping Infeasibility):** From Observation 9, the stopping distance differential ($90.1\text{ m}$) exceeds the provided headway gap ($70.3\text{ m}$) by $19.8\text{ m}$.
10. **Inference 5:** The claim of "0.00% collisions under extreme $-8.5\text{ m/s}^2$ braking" is physically false under the code's own parameters.

---

## 3. Caveats

- **Scope Scrutiny:** Investigation focused specifically on Requirements R3 (ML/PINN/XAI/FL), R4 (Statistical Rigor, Big Data, Spatial-Temporal Split), and R5 (Codebase & Reproducibility). Core Kalman-Bucy residual equations (R1) and Pacejka lateral tire slip equations (R2) were inspected for kinematic consistency with R4/R5 but are covered comprehensively by peer survey agents.
- **Assumptions Made:** Analysis assumed standard IEEE Transactions standards for empirical reproducibility, where stated quantitative results must derive directly from executed code.
- **Alternative Interpretations Considered:** Could the scalar loop in `m1_annual_digital_twin_engine.py` be intended as a fast macroscopic demonstration rather than the full experiment? Even if intended as a lightweight surrogate, presenting its outputs in the paper/README as "empirical results from simulating 38.95 million trips" violates academic reporting standards.

---

## 4. Conclusion

The M-1 Motorway Digital Twin project in its current state contains **severe, fatal discrepancies** regarding Requirements R3, R4, and R5:
1. Core ML/PINN/SHAP/PGD/FL modules are non-existent and simulated via hardcoded arrays or trivial analytical functions.
2. The 38.95M trip simulation is a 0.02s macroscopic toy loop without Poisson arrivals.
3. The spatial-temporal holdout partition is fictitious.
4. The Moran's I spatial clustering claim is contradicted by its own z-score ($z = 0.6875, p = 0.4918$ vs. claimed $p < 10^{-4}$).
5. The 0.00% collisions claim is kinematically invalid under extreme lead braking for 44-ton freight trailers.
6. Publication figures in `generate_readme_figures.py` are generated using mathematical curve fitting rather than simulation outputs.

**Recommendation:** A major overhaul and complete re-implementation of the empirical pipeline (as detailed in `survey_report.md`) is mandatory before submitting to IEEE T-ITS.

---

## 5. Verification Method

To independently verify these findings, execute the following commands and code inspections:

1. **Verify Missing Libraries & Execution Time:**
   ```powershell
   Get-Content requirements.txt
   python run_all_benchmarks.py
   ```
   *Verification criterion:* Observe total execution time of the entire suite in $<15\text{ seconds}$, confirming absence of 38.95M trip microscopic simulations or 50-round 87-node FL training.

2. **Verify Hardcoded ML & SHAP Values:**
   Inspect lines 56–88 of `controllers/m1_advanced_ml_suite.py` via `view_file`.
   *Verification criterion:* Confirm `shap_importance`, `acc_pinn`, `acc_deep_mlp`, and `fed_acc` are static definitions.

3. **Verify Moran's I Calculation and Hardcoded p-value:**
   Run in Python:
   ```python
   import scipy.stats as stats
   z = 0.6875
   p = 2 * (1 - stats.norm.cdf(z))
   print(f"True p-value: {p:.4f}")
   ```
   *Verification criterion:* Output displays `True p-value: 0.4918`, proving that line 344 in `controllers/m1_comprehensive_statistical_suite.py` (`"p_value": "< 1e-4"`) is fabricated.

4. **Verify Kinematic Collision Shortfall:**
   Calculate stopping distances from $v_0 = 30\text{ m/s}$:
   ```python
   d_lead = 30 * 0.18 + (30**2) / (2 * 8.5) # 58.34 m
   d_trailer = 30 * 0.78 + (30**2) / (2 * 3.6) # 148.40 m
   req_gap = d_trailer - d_lead # 90.06 m
   m_ratio = 38000.0 / 1500.0
   h_dynamic = 1.2 + 0.5 * 0.78 + 0.03 * (m_ratio**0.5) # 1.741 s
   d_standstill = 8.0 + 2.0 * (m_ratio**0.5) # 18.07 m
   provided_gap = d_standstill + h_dynamic * 30.0 # 70.30 m
   print(f"Deficit: {provided_gap - req_gap:.2f} m") # -19.76 m
   ```
   *Verification criterion:* Deficit is negative ($-19.76\text{ m}$), proving collisions are kinematically unavoidable under emergency lead braking.

---
*End of Handoff Report.*
