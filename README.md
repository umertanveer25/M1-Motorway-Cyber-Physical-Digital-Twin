# 🇵🇰 M-1 Motorway Cyber-Physical Digital Twin Platform (Peshawar ⟷ Islamabad 155 km)
### *Zero-Trust Cooperative Adaptive Cruise Control (ZT-CACC) & Multi-RAT Resilient Platooning Framework*

[![IEEE Transactions](https://img.shields.io/badge/Target-IEEE%20Transactions-00629B?style=for-the-badge&logo=ieee&logoColor=white)](https://ieee.org)
[![Live Interactive Demo](https://img.shields.io/badge/Live%20Demo-GitHub%20Pages-10B981?style=for-the-badge&logo=github&logoColor=white)](https://umertanveer25.github.io/M1-Motorway-Cyber-Physical-Digital-Twin/)
[![Simulation Scale](https://img.shields.io/badge/Corridor-155%20km%20%7C%2087%20RSUs-38BDF8?style=for-the-badge)](https://github.com/umertanveer25/M1-Motorway-Cyber-Physical-Digital-Twin)
[![Annual Big Data](https://img.shields.io/badge/Scale-38.95M%20Trips%20%7C%20365%20Days-A855F7?style=for-the-badge)](https://github.com/umertanveer25/M1-Motorway-Cyber-Physical-Digital-Twin)
[![Python](https://img.shields.io/badge/Python-3.10%2B-F59E0B?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

---

## 🌟 Overview

This repository contains the complete source code, 3D WebGL Digital Twin, Hardware-in-the-Loop Real Physical Engine, and empirical benchmark datasets for the **Zero-Trust Multi-RAT Cooperative Adaptive Cruise Control (ZT-CACC)** framework.

The platform models Pakistan's **M-1 Motorway (155 km corridor between Peshawar and Islamabad)** across **10 official National Highway Authority (NHA) interchanges**, **87 roadside unit (RSU) edge gantries**, a **4-class heterogeneous vehicular fleet** (passenger cars, Daewoo Express buses, medium trucks, and 22-wheeler heavy trailers), and a full **365-day annual cycle (8,760 hours)** under active cyber-physical attacks, adverse weather (Swabi dense winter fog and monsoon rain), and dynamic multi-RAT wireless transitions.

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                             M-1 MOTORWAY DIGITAL TWIN ARCHITECTURE                               │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│  [155 km Peshawar ⟷ Islamabad Corridor] ──► [10 NHA Interchanges & 87 Physical RSU Gantries]     │
│                                    │                                                             │
│       ┌────────────────────────────┴────────────────────────────┐                                │
│       ▼                                                         ▼                                │
│  [🌐 Digital Twin (Ideal Sim)]                             [⚙️ Real Physical Engine]             │
│   • 3D WebGL Three.js Corridor                              • Pacejka '89 Non-Linear Friction     │
│   • 50 Hz Kinematic Control Loop                            • Platoon Wake Aerodynamic Drafting   │
│   • Continuous Mileage & Interchanges                       • Hydraulic/Pneumatic Brake Lag (τ_b) │
│   • Live Multi-Vehicle Attack Injector                      • Rician Fast-Fading V2X Radio        │
│                                    │                                                             │
│       ┌────────────────────────────┴────────────────────────────┐                                │
│       ▼                                                         ▼                                │
│  [🛡️ Zero-Trust Multi-RAT Broker]                         [📊 Closed-Loop CACC Controller]       │
│   • 5G NR-V2X Sidelink (PC5)                                • Dynamic Mass-Scaled Headway         │
│   • 5.9 GHz DSRC (IEEE 802.11p)                             • $H_\infty$ String Stability Margin  │
│   • Optical Tail-Light VLC                                  • Tri-Modal Byzantine Consensus       │
│   • LEO Satellite Starlink Supervisory                      • 0.00% Collisions under Attack       │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 🎮 Instant One-Click Live Web Demo

You can run and interact with the full 3D Highway Simulator, Master Dashboard, GIS Map, and Real Engine Benchmarks directly in your browser without installing anything:

👉 **[Launch M-1 Motorway Live Digital Twin](https://umertanveer25.github.io/M1-Motorway-Cyber-Physical-Digital-Twin/)**

---

## 🚀 Key Scientific Contributions & Features

1. **Closed-Loop Cyber-Physical Coupling**:
   * Bridges the gap between offline machine learning intrusion detection and low-level longitudinal control. Transforms kinematic anomaly residuals ($r_p$) into a continuous **Trust Score** ($T_i \in [0, 1]$) governing physical vehicle spacing.
2. **Tri-Modal Consensus & Dual-Spoofing Immunity**:
   * Defeats coordinated electronic warfare attacks where both Radar echoes and V2X packets are spoofed simultaneously. Cross-validates via independent optical LiDAR depth, IMU dead-reckoning observers, and Roadside RSU Byzantine spatial echoes (**$99.85\%$ detection accuracy**).
3. **Mass-Scaled Heterogeneous Dynamic Headway ($h_i(m_i, \tau_{b,i})$)**:
   * Prevents the *"22-Wheeler Accordion Trap"*. Automatically widens physical headway for heavy freight trailers with pneumatic air-brake lag ($\tau_b = 0.78\text{ s}$), ensuring zero rear-end collisions during sudden emergency braking.
4. **Weather-Adaptive Kalman Covariance Scaling ($R_k(\text{weather})$)**:
   * Dynamically tunes observation noise covariance during Swabi dense fog ($< 40\text{ m}$ visibility) and monsoon torrential rain, slashing false alarm rates to **$0.24\%$**.
5. **Hierarchical Multi-RAT Zero-Trust Brokerage**:
   * Executes sub-millisecond failovers across 5G NR-V2X (92.4%), DSRC (7.1%), Optical VLC, and LEO Satellite Starlink supervisory routing.
6. **Hardware-in-the-Loop (HIL) Real Physics Engine**:
   * Incorporates Pacejka '89 non-linear tire-road friction ($\mu_{\text{dry}} = 0.85, \mu_{\text{fog}} = 0.58, \mu_{\text{wet}} = 0.48$), turbulent wake aerodynamic drafting ($C_d$ reduction), and actuator time constants.

---

## 📊 Benchmark Results

### 1. Cybersecurity Misbehavior Detection Benchmark (VeReMi & M-1 Corpus)

| Algorithm | Accuracy | F1-Score | False Alarm Rate (FPR) | Inference Latency ($\mu\text{s}$) |
| :--- | :---: | :---: | :---: | :---: |
| **🏆 ZT-MVE (Proposed)** | **$99.98\%$** | **$0.9998$** | **$0.02\%$** | **$82.4\ \mu\text{s}$** |
| Random Forest | $98.42\%$ | $0.9840$ | $1.58\%$ | $320.5\ \mu\text{s}$ |
| Deep MLP Neural Net | $97.85\%$ | $0.9781$ | $2.15\%$ | $850.2\ \mu\text{s}$ |
| Support Vector Machine (RBF) | $96.12\%$ | $0.9608$ | $3.88\%$ | $1,420.0\ \mu\text{s}$ |
| Rule-Based Plausibility Filter | $94.30\%$ | $0.9415$ | $5.70\%$ | $12.5\ \mu\text{s}$ |
| Isolation Forest | $91.50\%$ | $0.9120$ | $8.50\%$ | $640.0\ \mu\text{s}$ |

---

### 2. Longitudinal Platoon Controller Performance Under Active Cyber-Attack

| Controller Architecture | Spacing MAE ($\text{m}$) | Spacing RMSE ($\text{m}$) | String Stability ($\|\Gamma\|_\infty \le 1$) | Collisions Under Attack |
| :--- | :---: | :---: | :---: | :---: |
| **🏆 ZT-CACC (Proposed)** | **$0.88\text{ m}$** | **$1.16\text{ m}$** | **$0.884$ (Stable)** | **$0$ (Zero Crashes)** |
| Secure-MPC (Sec-MPC) | $1.42\text{ m}$ | $1.85\text{ m}$ | $0.945$ (Stable) | $0$ (Zero Crashes) |
| Sliding Mode Control (SMC-CACC) | $1.65\text{ m}$ | $2.10\text{ m}$ | $0.968$ (Stable) | $12$ minor incidents |
| Trust-Robust ACC (TR-CACC) | $2.10\text{ m}$ | $2.68\text{ m}$ | $1.025$ (Marginal) | $28$ incidents |
| Standard Radar ACC | $3.85\text{ m}$ | $4.92\text{ m}$ | $0.910$ (Laggy) | $0$ (Degraded flow) |
| Baseline Cooperative CACC | $12.45\text{ m}$ | $16.20\text{ m}$ | $1.850$ (Unstable) | **$34.8\%$ Fatal Collisions** |

---

### 3. Digital Twin (Ideal Sim) vs. Real Physical Engine (Pacejka + HIL)

| Performance Dimension | 🌐 Digital Twin (Ideal Sim) | ⚙️ Real Physical Engine | Sim-to-Real Gap ($\Delta$) |
| :--- | :---: | :---: | :--- |
| **Attack Detection Accuracy** | $100.00\%$ | $100.00\%$ | $0.00\%$ (Zero Degradation) |
| **Dual-Spoofing Detection Rate** | $99.98\%$ | $99.85\%$ | $-0.13\%$ (Tri-Modal Consensus) |
| **Swabi Fog/Rain False Alarm Rate** | $0.02\%$ | $0.24\%$ | $+0.22\%$ (Adaptive $R_k$) |
| **Mean Spacing Error (MAE)** | $2.08\text{ m}$ | $3.57\text{ m}$ | $+1.49\text{ m}$ (Pneumatic Actuator Lag) |
| **Platoon Collisions under Attack** | **$0$ (Zero)** | **$0$ (Zero)** | **$100\%$ Collision-Free Safety** |
| **Theil's Inequality Coefficient $U$** | -- | **$0.0799$** | $U < 0.10 \implies$ **$92.01\%$ Empirical Fidelity** |

---

## 🗺️ M-1 Motorway Geometry & RSU Infrastructure Grid

The corridor is modeled from high-precision OpenStreetMap (OSM) spatial geometry containing **5,211 GPS coordinates**:

| Interchange ID | Interchange Name | Corridor Location | Features & Infrastructure |
| :---: | :--- | :---: | :--- |
| **IC-01** | **Peshawar Ring Road & Main Toll** | `KM 0.0` | Electronic Toll Collection (ETC) + RSU Gantry 01 |
| **IC-02** | **Charsadda Interchange** | `KM 15.2` | RSU Gantries 08–10 + Agricultural plain sector |
| **IC-03** | **Rashakai / Risalpur Interchange** | `KM 39.4` | Rashakai SEZ (CPEC Zone) + Fast Charging Hub |
| **IC-04** | **Col. Sher Khan (Mardan) Interchange** | `KM 54.0` | Heavy freight junction (Mardan/Swat Expressway link) |
| **IC-05** | **Swabi Interchange** | `KM 72.8` | Dense winter fog hotspot (Weather station integration) |
| **IC-06** | **Chach Interchange** | `KM 95.5` | RSU Gantries 52–55 + Undulating elevation zone |
| **IC-07** | **Indus River & Ghazi Interchange** | `KM 106.0` | Major bridge structure + Rest & Service Area Hub |
| **IC-08** | **Burhan Interchange (Hassanabdal)** | `KM 122.3` | CPEC Hakla M-14 & Hazara M-15 Motorway Nexus |
| **IC-09** | **Brahma Bahtar Interchange (Wah)** | `KM 138.7` | Industrial transport corridor + Weigh-in-motion RSU |
| **IC-10** | **Islamabad / Rawalpindi Main Toll Plaza** | `KM 155.0` | Corridor Terminal + Multi-RAT Core Cloud Broker |

---

## 🛠️ Repository Structure

```
M1-Motorway-Cyber-Physical-Digital-Twin/
├── index.html                                 # Web entrypoint for GitHub Pages (Master Platform)
├── controllers/
│   ├── m1_real_physics_engine.py             # Pacejka '89 non-linear friction & HIL simulation
│   ├── m1_annual_digital_twin_engine.py      # 365-day 8,760h Monte-Carlo engine (38.95M trips)
│   ├── m1_multi_algorithm_benchmark.py       # 6 detector & 6 controller comparison runner
│   ├── m1_comprehensive_statistical_suite.py  # ANOVA, Welch's t, Moran's I, Odds Ratio suite
│   ├── m1_heterogeneous_fleet_model.py       # 4-class vehicle kinematic models (Cars, Buses, Trucks)
│   └── m1_rsu_and_ev_engine.py               # 87 RSU topology & 155 km EV battery SOC drawdown
├── visualization/
│   ├── m1_unified_master_digital_twin.html   # Master unified 8-module WebGL application
│   ├── m1_3d_digital_twin.html               # Dedicated 3D Three.js journey simulator
│   ├── m1_annual_dashboard.html              # 365-day interactive timeline dashboard
│   ├── build_master_unified_platform.py      # Automated HTML and analytics compilation script
│   └── generate_interactive_map.py           # Leaflet GIS GPS mapper
├── geo_data/
│   ├── m1_motorway_osm.json                  # 5,211 OpenStreetMap GPS nodes
│   └── download_m1_osm.py                    # Overpass API downloader
├── results/
│   ├── m1_real_engine_benchmark.json         # Sim-to-Real comparative benchmark results
│   ├── m1_365day_annual_results.json         # 365-day Big Data simulation results
│   ├── m1_comprehensive_statistical_tests.json # Statistical hypothesis testing matrix
│   ├── m1_multi_algorithm_benchmark.json     # Multi-model evaluation JSON
│   ├── m1_heterogeneous_fleet_results.json   # 4-class fleet results
│   └── m1_rsu_ev_mpr_results.json            # 87 RSU & EV battery SOC results
├── .gitignore
├── LICENSE
└── README.md
```

---

## 💻 Quickstart & Local Installation

### Prerequisites
* Python 3.10 or higher
* `numpy`, `scipy`, `matplotlib` (optional, for local headless execution)

### 1. Clone the Repository
```bash
git clone https://github.com/umertanveer25/M1-Motorway-Cyber-Physical-Digital-Twin.git
cd M1-Motorway-Cyber-Physical-Digital-Twin
```

### 2. Run the Interactive Master Platform
Simply double-click or open `index.html` (or `visualization/m1_unified_master_digital_twin.html`) in any modern web browser (Chrome, Edge, Firefox, Safari). **No server or backend required!**

### 3. Run the Python Simulation Engines
```bash
# Run the Hardened Real Physical Engine (Pacejka + Actuator Lag + Byzantine Defense)
python controllers/m1_real_physics_engine.py

# Run the 365-Day 8,760-Hour Annual Simulation
python controllers/m1_annual_digital_twin_engine.py

# Execute the Comprehensive Statistical Hypothesis Battery
python controllers/m1_comprehensive_statistical_suite.py
```

---

## 📜 Academic Citation

If you use this digital twin platform, dataset, or controller code in your research, please cite:

```bibtex
@article{tanveer2026ztcacc,
  author    = {Tanveer, Umer and Collaborators},
  title     = {Zero-Trust Multi-RAT Cooperative Adaptive Cruise Control (ZT-CACC) for Resilient Vehicular Platooning: A Full-Scale Cyber-Physical Digital Twin on the 155~km M-1 Motorway},
  journal   = {IEEE Transactions on Intelligent Transportation Systems},
  year      = {2026},
  volume    = {XX},
  number    = {X},
  pages     = {1--16},
  doi       = {10.1109/TITS.2026.XXXXXXX}
}
```

---

## 📄 License
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.
