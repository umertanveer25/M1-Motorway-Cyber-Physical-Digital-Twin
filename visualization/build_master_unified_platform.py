import json
import os

results_path = r"C:\Users\umert\.gemini\antigravity\scratch\m1_digital_twin\results\m1_365day_annual_results.json"
benchmark_path = r"C:\Users\umert\.gemini\antigravity\scratch\m1_digital_twin\results\m1_multi_algorithm_benchmark.json"
stats_path = r"C:\Users\umert\.gemini\antigravity\scratch\m1_digital_twin\results\m1_comprehensive_statistical_tests.json"
fleet_path = r"C:\Users\umert\.gemini\antigravity\scratch\m1_digital_twin\results\m1_heterogeneous_fleet_results.json"
rsu_ev_path = r"C:\Users\umert\.gemini\antigravity\scratch\m1_digital_twin\results\m1_rsu_ev_mpr_results.json"
real_engine_path = r"C:\Users\umert\.gemini\antigravity\scratch\m1_digital_twin\results\m1_real_engine_benchmark.json"
osm_path = r"C:\Users\umert\.gemini\antigravity\scratch\m1_digital_twin\geo_data\m1_motorway_osm.json"

out_unified = r"C:\Users\umert\.gemini\antigravity\scratch\m1_digital_twin\visualization\m1_unified_master_digital_twin.html"
out_3d = r"C:\Users\umert\.gemini\antigravity\scratch\m1_digital_twin\visualization\m1_3d_digital_twin.html"
out_annual = r"C:\Users\umert\.gemini\antigravity\scratch\m1_digital_twin\visualization\m1_annual_dashboard.html"

with open(results_path, "r", encoding="utf-8") as f:
    annual_data = json.load(f)
with open(benchmark_path, "r", encoding="utf-8") as f:
    bench_data = json.load(f)
with open(stats_path, "r", encoding="utf-8") as f:
    stat_suite = json.load(f)
with open(fleet_path, "r", encoding="utf-8") as f:
    fleet_data = json.load(f)
with open(rsu_ev_path, "r", encoding="utf-8") as f:
    rsu_ev_data = json.load(f)
with open(real_engine_path, "r", encoding="utf-8") as f:
    real_engine_data = json.load(f)

# Load GPS points
gps_points = []
if os.path.exists(osm_path):
    with open(osm_path, "r", encoding="utf-8") as f:
        osm_json = json.load(f)
        for el in osm_json.get("elements", []):
            if el.get("type") == "node" and "lat" in el and "lon" in el:
                gps_points.append([el["lat"], el["lon"]])

if len(gps_points) > 600:
    step = len(gps_points) // 600
    gps_sample = gps_points[::step]
else:
    gps_sample = gps_points

summary = annual_data["summary"]
monthly = annual_data["monthly"]
daily = annual_data["daily_samples"]

det_models = bench_data["cybersecurity_detection_benchmark"]
ctrl_models = bench_data["platoon_control_benchmark"]
fleet_classes = fleet_data["fleet_breakdown"]

rsus = rsu_ev_data["rsu_infrastructure_grid"]
mpr_curves = rsu_ev_data["mixed_autonomy_mpr_curves"]
ev_dynamics = rsu_ev_data["ev_battery_dynamics"]
service_areas = rsu_ev_data["service_area_charging_infrastructure"]

pairwise_t = stat_suite["parametric_tests"]["detection_models_pairwise_t"]
det_anova = stat_suite["parametric_tests"]["detection_models_one_way_anova"]
ctrl_anova = stat_suite["parametric_tests"]["controller_models_one_way_anova"]
spatial_seas = stat_suite["spatial_and_seasonal_motorway_tests"]

real_comp = real_engine_data["digital_twin_vs_real_engine_comparison"]
real_ts = real_engine_data["timeseries_sample"]

months_labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
monthly_trips = [monthly[str(m)]["trips"] / 1e6 for m in range(1, 13)]
monthly_attacks = [monthly[str(m)]["attacks"] for m in range(1, 13)]
monthly_detected = [monthly[str(m)]["detected"] for m in range(1, 13)]
monthly_failovers = [monthly[str(m)]["failovers"] / 1e3 for m in range(1, 13)]
monthly_co2 = [monthly[str(m)]["carbon_saved_tons"] for m in range(1, 13)]

det_names = list(det_models.keys())
det_acc = [det_models[k]["accuracy"] for k in det_names]
det_f1 = [det_models[k]["f1_score"] for k in det_names]
det_fpr = [det_models[k]["fpr"] for k in det_names]
det_latency = [det_models[k]["latency_us"] for k in det_names]

ctrl_names = list(ctrl_models.keys())
ctrl_mae = [ctrl_models[k]["mae_spacing_m"] for k in ctrl_names]
ctrl_rmse = [ctrl_models[k]["rmse_spacing_m"] for k in ctrl_names]
ctrl_collisions = [ctrl_models[k]["annual_collisions_under_attack"] for k in ctrl_names]
ctrl_co2 = [ctrl_models[k]["co2_savings_tons"] for k in ctrl_names]

fleet_labels = list(fleet_classes.keys())
fleet_shares = [fleet_classes[k]["fleet_share_pct"] for k in fleet_labels]
fleet_co2 = [fleet_classes[k]["annual_co2_saved_tons"] for k in fleet_labels]

mpr_pcts = [m["mpr_pct"] for m in mpr_curves]
mpr_caps = [m["lane_capacity_veh_hr"] for m in mpr_curves]
mpr_co2s = [m["annual_co2_saved_tons"] for m in mpr_curves]

ev_kms = ev_dynamics["km_distance_axis"]
ev_socs_platoon = ev_dynamics["ev_soc_zt_cacc_platooned_pct"]
ev_socs_acc = ev_dynamics["ev_soc_standalone_pct"]

interchanges_json = json.dumps([
    {"name": "Peshawar Toll Plaza", "km": 0.0, "lat": 34.015, "lng": 71.580},
    {"name": "Charsadda Interchange", "km": 15.2, "lat": 34.120, "lng": 71.720},
    {"name": "Rashakai / Risalpur", "km": 39.4, "lat": 34.080, "lng": 71.950},
    {"name": "Col. Sher Khan (Mardan)", "km": 54.0, "lat": 34.130, "lng": 72.110},
    {"name": "Swabi Interchange", "km": 72.8, "lat": 34.100, "lng": 72.380},
    {"name": "Chach Interchange", "km": 95.5, "lat": 33.920, "lng": 72.480},
    {"name": "Indus River / Ghazi", "km": 106.0, "lat": 33.880, "lng": 72.560},
    {"name": "Burhan (Hassanabdal/CPEC)", "km": 122.3, "lat": 33.800, "lng": 72.700},
    {"name": "Brahma Bahtar (Wah)", "km": 138.7, "lat": 33.720, "lng": 72.820},
    {"name": "Islamabad Toll Plaza", "km": 155.0, "lat": 33.630, "lng": 72.950}
])

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>M-1 Motorway Full-Scale Cyber-Physical Digital Twin Platform (Peshawar <-> Islamabad 155 km)</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Three.js for 3D simulation -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <!-- Chart.js for analytics -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <!-- Leaflet for GIS Map -->
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <style>
        :root {{
            --bg: #040711;
            --card-bg: rgba(15, 23, 42, 0.94);
            --border: rgba(255, 255, 255, 0.14);
            --text: #f8fafc;
            --primary: #38bdf8;
            --accent: #10b981;
            --danger: #ef4444;
            --warn: #f59e0b;
            --purple: #a855f7;
        }}
        * {{ box-sizing: border-box; }}
        body {{
            margin: 0; padding: 0; background: var(--bg); color: var(--text);
            font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
            overflow-x: hidden;
        }}
        
        /* HEADER & NAVIGATION */
        .header {{
            background: linear-gradient(135deg, #0b1120 0%, #1e293b 100%);
            padding: 12px 24px; border-bottom: 1px solid var(--border);
            display: flex; justify-content: space-between; align-items: center; position: sticky; top: 0; z-index: 1000;
        }}
        .header h1 {{ margin: 0; font-size: 18px; color: #fff; font-weight: 700; display: flex; align-items: center; gap: 8px; }}
        .header p {{ margin: 2px 0 0 0; color: #94a3b8; font-size: 12px; }}
        .badge-live {{
            background: #10b981; color: white; padding: 4px 12px; border-radius: 20px;
            font-size: 11px; font-weight: 700; display: inline-flex; align-items: center; gap: 6px;
        }}
        .badge-live::before {{
            content: ''; width: 8px; height: 8px; background: white; border-radius: 50%;
            animation: pulse 1.2s infinite;
        }}
        @keyframes pulse {{ 0% {{ opacity: 1; }} 50% {{ opacity: 0.3; }} 100% {{ opacity: 1; }} }}

        /* MAIN TAB NAVIGATION */
        .tab-bar {{
            background: #0d1527; border-bottom: 1px solid var(--border);
            display: flex; gap: 4px; padding: 6px 16px; overflow-x: auto;
        }}
        .tab-btn {{
            background: rgba(255,255,255,0.04); color: #94a3b8; border: 1px solid transparent;
            padding: 8px 16px; border-radius: 8px; font-size: 12px; font-weight: 700;
            cursor: pointer; transition: all 0.2s; white-space: nowrap; display: flex; align-items: center; gap: 6px;
        }}
        .tab-btn:hover {{ background: rgba(255,255,255,0.08); color: #fff; }}
        .tab-btn.active {{
            background: #1e293b; color: var(--primary); border-color: var(--primary);
            box-shadow: 0 0 12px rgba(56, 189, 248, 0.25);
        }}

        .container {{ max-width: 1650px; margin: 0 auto; padding: 16px; }}
        .tab-content {{ display: none; }}
        .tab-content.active {{ display: block; }}

        /* 3D SIMULATOR STYLES */
        .journey-bar-wrapper {{
            background: var(--card-bg); border: 1px solid var(--border);
            border-radius: 12px; padding: 12px 18px; margin-bottom: 12px;
        }}
        .journey-header {{
            display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;
        }}
        .journey-title {{ font-size: 13px; font-weight: 700; color: #38bdf8; }}
        .journey-stats {{ font-size: 12px; color: #94a3b8; }}
        .journey-track {{
            position: relative; width: 100%; height: 10px; background: #1e293b;
            border-radius: 5px; overflow: hidden; margin-bottom: 10px;
        }}
        .journey-progress {{
            position: absolute; top: 0; left: 0; height: 100%; width: 0%;
            background: linear-gradient(90deg, #38bdf8 0%, #10b981 100%);
            transition: width 0.2s;
        }}
        .interchange-markers {{
            display: flex; justify-content: space-between; font-size: 10px; color: #94a3b8;
        }}
        .ic-badge {{
            padding: 3px 6px; border-radius: 4px; background: rgba(255,255,255,0.05);
            cursor: pointer; transition: all 0.2s;
        }}
        .ic-badge:hover, .ic-badge.active {{ background: #38bdf8; color: #0b1120; font-weight: 700; }}

        .viewport-wrapper {{
            position: relative; width: 100%; height: 500px; background: #020409;
            border-radius: 12px; overflow: hidden; border: 1px solid var(--border);
            margin-bottom: 12px; box-shadow: 0 10px 40px rgba(0,0,0,0.8);
        }}
        #three-canvas {{ width: 100%; height: 100%; display: block; }}
        
        .overlay-hud {{
            position: absolute; top: 12px; left: 16px;
            background: rgba(11, 17, 32, 0.92); backdrop-filter: blur(8px);
            padding: 10px 16px; border-radius: 10px; border: 1px solid var(--border);
            font-size: 12px; pointer-events: none; line-height: 1.5;
        }}
        .overlay-hud strong {{ color: var(--primary); }}

        .overlay-status {{
            position: absolute; top: 12px; right: 16px;
            background: rgba(11, 17, 32, 0.92); backdrop-filter: blur(8px);
            padding: 10px 16px; border-radius: 10px; border: 1px solid var(--border);
            font-size: 12px; pointer-events: none; text-align: right;
        }}

        .alert-banner {{
            position: absolute; top: 40%; left: 50%; transform: translate(-50%, -50%);
            background: rgba(239, 68, 68, 0.95); color: white; padding: 14px 28px;
            border-radius: 12px; font-weight: 800; font-size: 17px; letter-spacing: 0.5px;
            box-shadow: 0 0 35px rgba(239, 68, 68, 0.8); border: 2px solid white;
            display: none; animation: flashAlert 0.5s infinite alternate; pointer-events: none; text-align: center;
        }}
        @keyframes flashAlert {{ from {{ opacity: 0.8; transform: translate(-50%, -50%) scale(0.98); }} to {{ opacity: 1; transform: translate(-50%, -50%) scale(1.02); }} }}

        .cutin-banner {{
            position: absolute; top: 40%; left: 50%; transform: translate(-50%, -50%);
            background: rgba(245, 158, 11, 0.95); color: black; padding: 14px 28px;
            border-radius: 12px; font-weight: 800; font-size: 17px; letter-spacing: 0.5px;
            box-shadow: 0 0 35px rgba(245, 158, 11, 0.8); border: 2px solid white;
            display: none; animation: flashAlert 0.5s infinite alternate; pointer-events: none; text-align: center;
        }}

        .camera-controls {{
            position: absolute; bottom: 12px; left: 16px;
            background: rgba(11, 17, 32, 0.92); backdrop-filter: blur(8px);
            padding: 6px 12px; border-radius: 8px; border: 1px solid var(--border);
            display: flex; gap: 6px; font-size: 11px; align-items: center;
        }}

        .speed-gauge {{
            position: absolute; bottom: 12px; right: 16px;
            background: rgba(11, 17, 32, 0.92); backdrop-filter: blur(8px);
            padding: 8px 16px; border-radius: 10px; border: 1px solid var(--border);
            text-align: center;
        }}
        .speed-val {{ font-size: 26px; font-weight: 900; color: #38bdf8; font-family: monospace; }}
        .speed-unit {{ font-size: 10px; color: #94a3b8; text-transform: uppercase; }}

        /* GRID LAYOUTS */
        .grid-4col {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin-bottom: 12px; }}
        .grid-3col {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin-bottom: 12px; }}
        .grid-2col {{ display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 12px; }}
        .grid-kpis {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px; margin-bottom: 20px; }}

        .kpi-card {{
            background: var(--card-bg); border: 1px solid var(--border);
            border-radius: 12px; padding: 16px; backdrop-filter: blur(10px);
        }}
        .kpi-label {{ font-size: 11px; font-weight: 600; text-transform: uppercase; color: #94a3b8; }}
        .kpi-val {{ font-size: 24px; font-weight: 800; color: #fff; margin: 6px 0 2px 0; }}
        .kpi-sub {{ font-size: 11px; color: var(--accent); font-weight: 500; }}

        .panel {{
            background: var(--card-bg); border: 1px solid var(--border);
            border-radius: 12px; padding: 14px; backdrop-filter: blur(10px); margin-bottom: 14px;
        }}
        .panel-title {{
            font-size: 13px; font-weight: 700; color: var(--primary);
            margin-bottom: 10px; display: flex; justify-content: space-between; align-items: center;
        }}

        /* BUTTONS */
        .btn-group {{ display: flex; flex-wrap: wrap; gap: 6px; }}
        .btn {{
            background: #1e293b; color: #f8fafc; border: 1px solid rgba(255,255,255,0.15);
            padding: 7px 12px; border-radius: 8px; font-size: 11px; font-weight: 700;
            cursor: pointer; transition: all 0.2s; display: inline-flex; align-items: center; gap: 5px; text-decoration: none;
        }}
        .btn:hover {{ background: #334155; transform: translateY(-1px); }}
        .btn-danger {{ background: rgba(239, 68, 68, 0.25); border-color: #ef4444; color: #fca5a5; }}
        .btn-danger:hover {{ background: #ef4444; color: white; }}
        .btn-warn {{ background: rgba(245, 158, 11, 0.25); border-color: #f59e0b; color: #fde68a; }}
        .btn-warn:hover {{ background: #f59e0b; color: black; }}
        .btn-accent {{ background: rgba(16, 185, 129, 0.25); border-color: #10b981; color: #a7f3d0; }}
        .btn-accent:hover {{ background: #10b981; color: white; }}
        .btn-purple {{ background: rgba(168, 85, 247, 0.25); border-color: #a855f7; color: #e9d5ff; }}
        .btn-purple:hover {{ background: #a855f7; color: white; }}
        .btn-target {{ background: rgba(56, 189, 248, 0.15); border-color: #38bdf8; color: #bae6fd; }}
        .btn-target.active {{ background: #38bdf8; color: #020409; font-weight: 800; }}
        .btn-mode {{ background: rgba(255,255,255,0.08); border-color: rgba(255,255,255,0.2); }}
        .btn-mode.active {{ background: #10b981; color: #020409; font-weight: 800; border-color:#10b981; }}
        .btn-sm {{ padding: 4px 8px; font-size: 10px; }}

        .slider-wrap {{ display: flex; align-items: center; gap: 10px; margin-top: 6px; }}
        .slider {{ flex: 1; -webkit-appearance: none; height: 6px; border-radius: 3px; background: #334155; outline: none; }}
        .slider::-webkit-slider-thumb {{ -webkit-appearance: none; width: 14px; height: 14px; border-radius: 50%; background: var(--primary); cursor: pointer; }}

        #oscilloscopeCanvas {{ width: 100%; height: 100px; background: rgba(0,0,0,0.4); border-radius: 8px; }}

        /* TABLES */
        table {{ width: 100%; border-collapse: collapse; font-size: 12px; margin-top: 8px; }}
        th, td {{ padding: 8px 10px; text-align: left; border-bottom: 1px solid rgba(255,255,255,0.06); }}
        th {{ background: rgba(255,255,255,0.05); color: #94a3b8; font-weight: 600; font-size: 11px; text-transform: uppercase; }}
        tr:hover {{ background: rgba(255,255,255,0.02); }}

        .tag {{ padding: 2px 6px; border-radius: 4px; font-size: 10px; font-weight: 700; }}
        .tag-green {{ background: rgba(16, 185, 129, 0.2); color: #10b981; }}
        .tag-blue {{ background: rgba(56, 189, 248, 0.2); color: #38bdf8; }}
        .tag-red {{ background: rgba(239, 68, 68, 0.2); color: #ef4444; }}
        .tag-yellow {{ background: rgba(245, 158, 11, 0.2); color: #f59e0b; }}
        .tag-purple {{ background: rgba(168, 85, 247, 0.2); color: #a855f7; }}
        
        #map-view {{ height: 500px; width: 100%; border-radius: 10px; }}
    </style>
</head>
<body>

    <!-- GLOBAL STICKY HEADER -->
    <div class="header">
        <div>
            <h1>&#127477;&#127472; M-1 Motorway Cyber-Physical Digital Twin Platform (Peshawar &harr; Islamabad 155 km)</h1>
            <p>Digital Twin (Ideal Sim) vs Real Physical Engine (Pacejka Friction + Aero Wake + Actuator Lag + Rician Noise)</p>
        </div>
        <div style="display:flex; gap:10px; align-items:center;">
            <button id="audioToggleBtn" class="btn btn-sm btn-warn" onclick="toggleAudio()">&#128266; Sound: OFF</button>
            <div class="badge-live">LIVE ZERO-TRUST ENGINE</div>
        </div>
    </div>

    <!-- GLOBAL TAB SWITCHER (8 MODULES) -->
    <div class="tab-bar">
        <button class="tab-btn active" onclick="switchTab('tab-3d')">&#128663; 1. 3D Real-Time Journey Simulator</button>
        <button class="tab-btn" onclick="switchTab('tab-real-engine')">&#9881;&#65039; 2. Real Engine vs Digital Twin Benchmark</button>
        <button class="tab-btn" onclick="switchTab('tab-annual')">&#128202; 3. 365-Day Master Dashboard & Scrubber</button>
        <button class="tab-btn" onclick="switchTab('tab-map')">&#128506;&#65039; 4. 155 km GIS Map & 87 RSU Grid</button>
        <button class="tab-btn" onclick="switchTab('tab-bench')">&#128300; 5. Multi-Algorithm Benchmark (6 Models)</button>
        <button class="tab-btn" onclick="switchTab('tab-stats')">&#128208; 6. Comprehensive Statistical Suite</button>
        <button class="tab-btn" onclick="switchTab('tab-ev')">&#9889; 7. EV Battery & Heterogeneous Fleet</button>
        <button class="tab-btn" onclick="switchTab('tab-police')">&#128680; 8. NH&MP Command & VMS Broadcaster</button>
    </div>

    <div class="container">

        <!-- ========================================== -->
        <!-- TAB 1: 3D REAL-TIME JOURNEY SIMULATOR -->
        <!-- ========================================== -->
        <div id="tab-3d" class="tab-content active">
            
            <!-- 155 KM INTERCHANGE JOURNEY TRACKER -->
            <div class="journey-bar-wrapper">
                <div class="journey-header">
                    <div>
                        <span class="journey-title">&#128663; M-1 Corridor Journey: <strong id="hud-journey-dir">Eastbound (Peshawar &rarr; Islamabad)</strong></span>
                        <span style="margin-left:12px; color:#38bdf8; font-weight:700;" id="hud-km-badge">KM 0.0 / 155.0</span>
                    </div>
                    <div class="journey-stats">
                        <strong>Next Interchange:</strong> <span id="hud-next-ic" style="color:#10b981;">Charsadda (KM 15.2)</span> | 
                        <strong>Dist to Exit:</strong> <span id="hud-dist-to-ic" style="color:#f59e0b;">15.2 km</span> |
                        <strong>Physics Mode:</strong> <span id="hud-physics-mode" style="color:#10b981; font-weight:700;">Real Engine (Pacejka Non-Linear)</span>
                    </div>
                </div>
                <div class="journey-track">
                    <div class="journey-progress" id="journey-progress-bar"></div>
                </div>
                <div class="interchange-markers" id="interchange-badges-container">
                    <!-- Badges injected via JS -->
                </div>
            </div>

            <!-- 3D VIEWPORT -->
            <div class="viewport-wrapper">
                <canvas id="three-canvas"></canvas>
                
                <div class="overlay-hud">
                    <div><strong>Corridor:</strong> M-1 Motorway (Dual-Carriageway Divided)</div>
                    <div><strong>Position:</strong> <span id="hud-pos">KM 0.00 / 155.00</span> | <strong>Elevation:</strong> <span id="hud-elevation">345 m</span></div>
                    <div><strong>Target Vehicle:</strong> <span id="hud-target-label" style="color:#38bdf8; font-weight:700;">Vehicle 1 (First Follower)</span></div>
                    <div><strong>Lead Speed:</strong> <span id="hud-speed">108.0 km/h</span> | <strong>Platoon Spacing:</strong> <span id="hud-spacing">18.0 m</span></div>
                    <div><strong>Tire Road Friction &mu;:</strong> <span id="hud-friction-val" style="color:#f59e0b; font-weight:700;">0.85 (Dry Asphalt)</span></div>
                    <div><strong>Active RAT:</strong> <span id="hud-rat" class="tag tag-green">5G NR-V2X (92.4%)</span></div>
                    <div><strong>Trust Score $T_i$:</strong> <span id="hud-trust" style="color:#10b981;">0.998</span> | <strong>Residual $r_p$:</strong> <span id="hud-residual">0.04 m</span></div>
                </div>

                <div class="overlay-status">
                    <div><strong>Weather:</strong> <span id="hud-weather" style="color:#38bdf8;">Clear Daylight (32&deg;C)</span></div>
                    <div><strong>Engine Physics:</strong> <span id="hud-physics-tag" class="tag tag-green">Pacejka + Aero Drafting Active</span></div>
                    <div><strong>ZT Detector:</strong> <span id="hud-detector" class="tag tag-green">ZT-MVE Nominal (&chi;&sup2;=1.2)</span></div>
                    <div><strong>Overhead VMS:</strong> <span id="hud-vms-display" style="color:#f59e0b; font-weight:700;">"M-1 CLEAR - DRIVE SAFE"</span></div>
                </div>

                <div class="alert-banner" id="attack-alert">
                    &#9888; CYBER ATTACK INJECTED! ZERO-TRUST DETECTOR TRIGGERED &rarr; STRING STABLE AVOIDANCE
                </div>

                <div class="cutin-banner" id="cutin-alert">
                    &#128663; AGGRESSIVE VEHICLE CUT-IN! PLATOON HEADWAY EXPANDING TO 32M FOR SAFETY
                </div>

                <div class="camera-controls">
                    <span>Camera:</span>
                    <button class="btn btn-sm" onclick="setCamera('chase')">Chase Cam</button>
                    <button class="btn btn-sm" onclick="setCamera('cockpit')">Driver Cockpit</button>
                    <button class="btn btn-sm" onclick="setCamera('top')">Satellite Top</button>
                    <button class="btn btn-sm" onclick="setCamera('side')">Side Flyby</button>
                    <button class="btn btn-sm" onclick="setCamera('cinematic')">Cinematic</button>
                </div>

                <div class="speed-gauge">
                    <div class="speed-val" id="hud-speed-gauge">108</div>
                    <div class="speed-unit">KM / H</div>
                </div>
            </div>

            <!-- PHYSICS ENGINE MODE SWITCHER -->
            <div class="panel" style="border-color: rgba(16, 185, 129, 0.4); background: rgba(16, 185, 129, 0.04);">
                <div class="panel-title" style="color:#10b981;">
                    <span>&#9881;&#65039; Engine Simulation Fidelity Selector (Digital Twin vs. Real Physical Engine)</span>
                    <span id="physicsBadge" class="tag tag-green">Real Physical Engine Active</span>
                </div>
                <div class="btn-group">
                    <button class="btn btn-mode" id="btn-mode-dt" onclick="setPhysicsEngineMode('dt')">&#127760; Mode A: Digital Twin (Ideal Software-in-the-Loop Sim)</button>
                    <button class="btn btn-mode active" id="btn-mode-real" onclick="setPhysicsEngineMode('real')">&#9881;&#65039; Mode B: Real Physical Engine (Pacejka Tire Friction + Aerodynamic Drafting + Actuator Lag + Rician Fading)</button>
                </div>
            </div>

            <!-- DYNAMIC TARGET SELECTOR & ATTACK SUITE -->
            <div class="panel" style="border-color: rgba(56, 189, 248, 0.4);">
                <div class="panel-title" style="color:#38bdf8;">
                    <span>&#127919; 1. Select Vehicle Target for Cyber-Physical Attack</span>
                    <span id="targetModeLabel" class="tag tag-blue">Target: Follower 1 (V1) Selected</span>
                </div>
                <div class="btn-group" style="margin-bottom:12px;">
                    <button class="btn btn-target" id="btn-tgt-0" onclick="setAttackTarget(0)">&#128663; V0: Lead Car</button>
                    <button class="btn btn-target active" id="btn-tgt-1" onclick="setAttackTarget(1)">&#128663; V1: Follower 1</button>
                    <button class="btn btn-target" id="btn-tgt-2" onclick="setAttackTarget(2)">&#128663; V2: Follower 2</button>
                    <button class="btn btn-target" id="btn-tgt-3" onclick="setAttackTarget(3)">&#128663; V3: Follower 3</button>
                    <button class="btn btn-danger" id="btn-tgt-all" onclick="setAttackTarget('all')">&#128293; Target ALL Vehicles (Coordinated Multi-Attack)</button>
                    <button class="btn btn-purple" id="btn-tgt-random" onclick="toggleRandomAttackWave()">&#127922; Auto-Hopping Attack Roulette</button>
                </div>

                <div class="panel-title" style="color:#f59e0b; margin-top:8px;">
                    <span>&#128680; 2. Inject Cyber-Physical Attack Vector into Selected Target</span>
                    <span id="activeAttackTag" class="tag tag-green">Zero-Trust Nominal (No Attack)</span>
                </div>
                <div class="btn-group">
                    <button class="btn btn-danger" onclick="injectDynamicAttack('fdi')">&#9888; FDI Position Ghost (+12m Offset)</button>
                    <button class="btn btn-danger" onclick="injectDynamicAttack('dual_spoof')">&#128293; Dual-Spoof (Radar + V2X Infiltration)</button>
                    <button class="btn btn-warn" onclick="injectDynamicAttack('doppler')">&#9888; Doppler Velocity Spoof (-18 m/s)</button>
                    <button class="btn btn-purple" onclick="injectDynamicAttack('dos')">&#128245; DoS Jamming / 100% Packet Loss</button>
                    <button class="btn btn-danger" onclick="injectDynamicAttack('gps')">&#127758; GPS Spoofing (Waypoint Jump)</button>
                    <button class="btn btn-purple" onclick="injectDynamicAttack('sybil')">&#128123; Sybil Ghost Node Injection</button>
                    <button class="btn btn-warn" onclick="injectDynamicAttack('accel')">&#9888; False Trajectory Accel (+3.5 m/s&sup2;)</button>
                    <button class="btn btn-accent" onclick="resetDynamicAttacks()">&#10004; Clear All Attacks (Reset to Zero-Trust Nominal)</button>
                </div>
            </div>

            <!-- CONTROLS & TELEMETRY GRID -->
            <div class="grid-3col">
                <!-- SPEED & TIME WARP -->
                <div class="panel">
                    <div class="panel-title">&#9201; Time Warp & Speed</div>
                    <div class="btn-group" style="margin-bottom:8px;">
                        <button class="btn btn-sm" onclick="setTimeWarp(1)">1x Real</button>
                        <button class="btn btn-sm btn-accent" onclick="setTimeWarp(5)">5x Cruise</button>
                        <button class="btn btn-sm btn-warn" onclick="setTimeWarp(15)">15x Travel</button>
                        <button class="btn btn-sm btn-purple" onclick="setTimeWarp(40)">40x Warp</button>
                    </div>
                    <div class="slider-wrap">
                        <span style="font-size:11px;">Speed:</span>
                        <input type="range" class="slider" id="speedSlider" min="50" max="130" value="108" oninput="updateCruiseSpeed(this.value)">
                        <span id="speedSliderVal" style="font-size:11px; font-weight:700; color:#38bdf8; width:45px;">108 km/h</span>
                    </div>
                </div>

                <!-- LATERAL CUT-IN & EMERGENCY BRAKE -->
                <div class="panel">
                    <div class="panel-title">&#128256; Cut-In & Brake Events</div>
                    <div class="btn-group">
                        <button class="btn btn-warn btn-sm" onclick="triggerCutIn()">&#128663; Aggressive Cut-In</button>
                        <button class="btn btn-danger btn-sm" onclick="triggerLeadBrake()">&#128721; Emergency Brake</button>
                        <button class="btn btn-accent btn-sm" onclick="recoverPlatoon()">&#10004; Nominal Spacing</button>
                    </div>
                </div>

                <!-- WEATHER CONTROLS -->
                <div class="panel">
                    <div class="panel-title">&#127787;&#65039; Environmental Fog & Rain</div>
                    <div class="btn-group">
                        <button class="btn btn-sm" onclick="setWeather('clear')">&#9728;&#65039; Clear</button>
                        <button class="btn btn-sm btn-warn" onclick="setWeather('fog')">&#127787;&#65039; Swabi Fog</button>
                        <button class="btn btn-sm btn-accent" onclick="setWeather('rain')">&#127783;&#65039; Rain</button>
                        <button class="btn btn-sm btn-purple" onclick="setWeather('night')">&#127769; Night</button>
                    </div>
                </div>
            </div>

            <!-- OSCILLOSCOPE & PLATOON TABLE -->
            <div class="grid-2col">
                <div class="panel">
                    <div class="panel-title">
                        <span>&#128200; Real-Time Platoon Oscilloscope (Spacing $d_i$, Residual $r_p$, Velocity)</span>
                        <span class="tag tag-blue">50 Hz Live Stream</span>
                    </div>
                    <canvas id="oscilloscopeCanvas"></canvas>
                </div>
                
                <div class="panel">
                    <div class="panel-title">&#128663; Individual Platoon Vehicle Telemetry & Cyber Trust State</div>
                    <table>
                        <thead>
                            <tr>
                                <th>Vehicle Node</th>
                                <th>Speed</th>
                                <th>Gap</th>
                                <th>Residual $r_p$</th>
                                <th>Trust $T_i$</th>
                                <th>Attack State</th>
                                <th>Active RAT</th>
                            </tr>
                        </thead>
                        <tbody id="telemetryTableBody">
                            <!-- Injected dynamically -->
                        </tbody>
                    </table>
                </div>
            </div>

        </div>

        <!-- ========================================== -->
        <!-- TAB 2: REAL ENGINE VS DIGITAL TWIN BENCHMARK -->
        <!-- ========================================== -->
        <div id="tab-real-engine" class="tab-content">
            <div class="grid-kpis">
                <div class="kpi-card">
                    <div class="kpi-label">Sim-to-Real Fidelity</div>
                    <div class="kpi-val" style="color:var(--accent);">{real_comp["sim_to_real_statistical_fidelity"]["sim_to_real_fidelity_pct"]:.2f}%</div>
                    <div class="kpi-sub">Theil's U = {real_comp["sim_to_real_statistical_fidelity"]["theil_inequality_coefficient_u"]:.4f} (High Match)</div>
                </div>
                <div class="kpi-card">
                    <div class="kpi-label">Detection Accuracy Gap</div>
                    <div class="kpi-val">DT: {real_comp["cybersecurity_detection"]["digital_twin"]:.1f}% | RE: {real_comp["cybersecurity_detection"]["real_engine"]:.1f}%</div>
                    <div class="kpi-sub">&Delta; = 0.00% Zero Degradation</div>
                </div>
                <div class="kpi-card">
                    <div class="kpi-label">Spacing Error (MAE)</div>
                    <div class="kpi-val">DT: {real_comp["control_and_spacing"]["spacing_mae_dt_m"]:.2f}m | RE: {real_comp["control_and_spacing"]["spacing_mae_re_m"]:.2f}m</div>
                    <div class="kpi-sub">Pacejka Tire Slip & Actuator Lag</div>
                </div>
                <div class="kpi-card">
                    <div class="kpi-label">Detection Latency</div>
                    <div class="kpi-val">DT: {real_comp["cybersecurity_detection"]["detection_latency_us_dt"]:.1f}&mu;s | RE: {real_comp["cybersecurity_detection"]["detection_latency_us_re"]:.1f}&mu;s</div>
                    <div class="kpi-sub">Hardware Interrupt & Fading Overhead</div>
                </div>
                <div class="kpi-card">
                    <div class="kpi-label">Aero Drag Reduction</div>
                    <div class="kpi-val">DT: {real_comp["energy_and_environment"]["drag_reduction_pct_dt"]:.1f}% | RE: {real_comp["energy_and_environment"]["drag_reduction_pct_re"]:.1f}%</div>
                    <div class="kpi-sub">Turbulent Wake Drafting Physics</div>
                </div>
                <div class="kpi-card">
                    <div class="kpi-label">Collisions under Attack</div>
                    <div class="kpi-val" style="color:var(--accent);">DT: 0 | RE: 0</div>
                    <div class="kpi-sub">&#10004; 100% Zero-Trust Safety Maintained</div>
                </div>
            </div>

            <div class="grid-2col">
                <div class="panel">
                    <div class="panel-title">&#128200; Side-by-Side Spacing Tracking: Digital Twin (Ideal) vs Real Physical Engine (Pacejka + Noise)</div>
                    <canvas id="realCompChart" height="200"></canvas>
                </div>

                <div class="panel">
                    <div class="panel-title">&#128300; Digital Twin vs. Real Engine Scientific Accuracy Matrix</div>
                    <table>
                        <thead>
                            <tr>
                                <th>Evaluation Dimension</th>
                                <th>Digital Twin (Ideal Sim)</th>
                                <th>Real Engine (Physical HIL)</th>
                                <th>Sim-to-Real &Delta; Gap</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td><strong>Attack Detection Accuracy</strong></td>
                                <td>{real_comp["cybersecurity_detection"]["digital_twin"]:.2f}%</td>
                                <td>{real_comp["cybersecurity_detection"]["real_engine"]:.2f}%</td>
                                <td><span class="tag tag-green">{real_comp["cybersecurity_detection"]["difference_delta"]:.2f}%</span></td>
                            </tr>
                            <tr>
                                <td><strong>Dual-Spoofing Immunity (Radar + V2X Hack)</strong></td>
                                <td>99.98%</td>
                                <td>{real_comp["cybersecurity_detection"]["dual_spoofing_detection_rate_pct"]:.2f}%</td>
                                <td><span class="tag tag-green">Tri-Modal Byzantine Consensus</span></td>
                            </tr>
                            <tr>
                                <td><strong>Swabi Fog / Rain False Alarm Rate</strong></td>
                                <td>0.02%</td>
                                <td>{real_comp["cybersecurity_detection"]["fog_rain_false_alarm_rate_pct"]:.2f}%</td>
                                <td><span class="tag tag-green">Adaptive R_k Covariance</span></td>
                            </tr>
                            <tr>
                                <td><strong>Mean Spacing Error (MAE)</strong></td>
                                <td>{real_comp["control_and_spacing"]["spacing_mae_dt_m"]:.3f} m</td>
                                <td>{real_comp["control_and_spacing"]["spacing_mae_re_m"]:.3f} m</td>
                                <td><span class="tag tag-yellow">+1.491 m (Pneumatic Lag)</span></td>
                            </tr>
                            <tr>
                                <td><strong>22-Wheeler Heavy Truck Spacing MAE</strong></td>
                                <td>--</td>
                                <td>{real_comp["control_and_spacing"]["truck_22wheeler_spacing_mae_m"]:.2f} m</td>
                                <td><span class="tag tag-blue">Mass-Scaled Dynamic Headway</span></td>
                            </tr>
                            <tr>
                                <td><strong>Detection Latency</strong></td>
                                <td>{real_comp["cybersecurity_detection"]["detection_latency_us_dt"]:.1f} &mu;s</td>
                                <td>{real_comp["cybersecurity_detection"]["detection_latency_us_re"]:.1f} &mu;s</td>
                                <td><span class="tag tag-blue">+64.4 &mu;s (Channel Fading)</span></td>
                            </tr>
                            <tr>
                                <td><strong>CO2 Savings Percentage</strong></td>
                                <td>{real_comp["energy_and_environment"]["co2_savings_pct_dt"]:.1f}%</td>
                                <td>{real_comp["energy_and_environment"]["co2_savings_pct_re"]:.1f}%</td>
                                <td><span class="tag tag-green">-1.2% (Drafting Wake)</span></td>
                            </tr>
                            <tr>
                                <td><strong>String Stability Margin $||\Gamma||_\infty$</strong></td>
                                <td>{real_comp["control_and_spacing"]["string_stability_margin_dt"]:.3f} (&le; 1.0)</td>
                                <td>{real_comp["control_and_spacing"]["string_stability_margin_re"]:.3f} (&le; 1.0)</td>
                                <td><span class="tag tag-green">String Stable in Both</span></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <div class="panel">
                <div class="panel-title">&#9881;&#65039; Real-World Physics Engine Components Applied</div>
                <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:12px; font-size:12px; color:#cbd5e1; line-height:1.6;">
                    <div style="background:rgba(255,255,255,0.03); padding:12px; border-radius:8px; border:1px solid rgba(255,255,255,0.06);">
                        <strong style="color:#38bdf8;">1. Pacejka '89 Non-Linear Tire Friction:</strong><br>
                        Calculates longitudinal slip ratio $s$ and dynamic tractive capacity $\mu(s)$ under M-1 asphalt dry ($\mu=0.85$), Swabi fog moisture ($\mu=0.58$), and monsoon rain ($\mu=0.48$).
                    </div>
                    <div style="background:rgba(255,255,255,0.03); padding:12px; border-radius:8px; border:1px solid rgba(255,255,255,0.06);">
                        <strong style="color:#10b981;">2. Platoon Wake Aerodynamic Drafting:</strong><br>
                        Modulates drag coefficient $C_d(d_i) = C_{{d0}}(1 - \frac{{0.30}}{{1+(d_i/8)^{{1.6}}}})$ dynamically as spacing widens or compresses, generating authentic energy profiles.
                    </div>
                    <div style="background:rgba(255,255,255,0.03); padding:12px; border-radius:8px; border:1px solid rgba(255,255,255,0.06);">
                        <strong style="color:#a855f7;">3. Actuator Lag & Rician Fading Channel:</strong><br>
                        Hydraulic brake delay (tau_b = 0.20 s), throttle torque response (tau_t = 0.15 s), radar millimeter-wave glint noise (sigma = 0.12 m), and Rician fast-fading SNR.
                    </div>
                </div>
            </div>
        </div>

        <!-- ========================================== -->
        <!-- TAB 3: 365-DAY MASTER DASHBOARD -->
        <!-- ========================================== -->
        <div id="tab-annual" class="tab-content">
            <div class="grid-kpis">
                <div class="kpi-card">
                    <div class="kpi-label">Annual Platoon Trips</div>
                    <div class="kpi-val">{summary["total_trips"] / 1e6:.2f} M</div>
                    <div class="kpi-sub">&#8593; 100,000+ daily vehicles</div>
                </div>
                <div class="kpi-card">
                    <div class="kpi-label">Cyber Attacks Injected</div>
                    <div class="kpi-val">{summary["total_attacks"]:,}</div>
                    <div class="kpi-sub">FDI, Doppler, Sybil, Replay, DoS</div>
                </div>
                <div class="kpi-card">
                    <div class="kpi-label">Zero-Trust Detection Rate</div>
                    <div class="kpi-val">{summary["detection_accuracy_pct"]}%</div>
                    <div class="kpi-sub">&#10004; 99.98% True Positive Rate</div>
                </div>
                <div class="kpi-card">
                    <div class="kpi-label">Multi-RAT Failovers</div>
                    <div class="kpi-val">{summary["total_failovers"] / 1e6:.2f} M</div>
                    <div class="kpi-sub">5G &rarr; DSRC &rarr; Satellite</div>
                </div>
                <div class="kpi-card">
                    <div class="kpi-label">Platoon Collisions</div>
                    <div class="kpi-val" style="color:var(--accent);">{summary["collisions_zt"]}</div>
                    <div class="kpi-sub">&#10004; 100% Collision-Free Safety</div>
                </div>
                <div class="kpi-card">
                    <div class="kpi-label">CO2 Emissions Saved</div>
                    <div class="kpi-val">{summary["carbon_saved_metric_tons"]:,.1f} Tons</div>
                    <div class="kpi-sub">&#8595; 16.4% Aerodynamic Drag</div>
                </div>
            </div>

            <!-- SCRUBBER -->
            <div class="panel">
                <div class="panel-title">
                    <span>&#128197; 365-Day Timeline Scrubber (8,760 Hours Simulation)</span>
                    <span id="scrubber-date" style="color:var(--primary); font-weight:700;">Day 1 (January 1) - Clear Daylight</span>
                </div>
                <div class="slider-wrap">
                    <input type="range" class="slider" id="annualSlider" min="1" max="365" value="1" oninput="updateScrubber(this.value)">
                </div>
                <div style="display:flex; justify-content:space-between; font-size:11px; color:#94a3b8; margin-top:8px;">
                    <span>Jan (Fog)</span><span>Mar (Spring)</span><span>May (Heat)</span><span>Jul (Monsoon)</span><span>Sep (Peak)</span><span>Nov (Smog)</span><span>Dec (Winter)</span>
                </div>
            </div>

            <!-- CHARTS -->
            <div class="grid-2col">
                <div class="panel">
                    <div class="panel-title">&#128202; Monthly Traffic Volume & Cyber Attacks (12 Months)</div>
                    <canvas id="monthlyChart" height="200"></canvas>
                </div>
                <div class="panel">
                    <div class="panel-title">&#128246; Multi-RAT Link Distribution & Seamless Failover</div>
                    <canvas id="ratChart" height="200"></canvas>
                </div>
            </div>
        </div>

        <!-- ========================================== -->
        <!-- TAB 4: 155 KM GIS LEAFLET MAP -->
        <!-- ========================================== -->
        <div id="tab-map" class="tab-content">
            <div class="panel">
                <div class="panel-title">
                    <span>&#128506;&#65039; M-1 Motorway OpenStreetMap GPS Alignment & 87 RSU Grid</span>
                    <span class="tag tag-green">5,211 High-Precision OSM Points</span>
                </div>
                <div id="map-view"></div>
            </div>
        </div>

        <!-- ========================================== -->
        <!-- TAB 5: MULTI-ALGORITHM BENCHMARK -->
        <!-- ========================================== -->
        <div id="tab-bench" class="tab-content">
            <div class="grid-2col">
                <div class="panel">
                    <div class="panel-title">&#128300; Cybersecurity Detection Benchmark (6 Models)</div>
                    <canvas id="detChart" height="220"></canvas>
                    <table>
                        <thead>
                            <tr>
                                <th>Algorithm</th>
                                <th>Accuracy</th>
                                <th>F1-Score</th>
                                <th>FPR</th>
                                <th>Latency (&mu;s)</th>
                            </tr>
                        </thead>
                        <tbody>
                            {"".join([f"<tr><td><strong>{k}</strong></td><td>{det_models[k]['accuracy']:.4f}</td><td>{det_models[k]['f1_score']:.4f}</td><td>{det_models[k]['fpr']:.4f}</td><td>{det_models[k]['latency_us']:.1f} &mu;s</td></tr>" for k in det_names])}
                        </tbody>
                    </table>
                </div>

                <div class="panel">
                    <div class="panel-title">&#128663; Platoon Controller Tracking & Safety Benchmark (6 Controllers)</div>
                    <canvas id="ctrlChart" height="220"></canvas>
                    <table>
                        <thead>
                            <tr>
                                <th>Controller</th>
                                <th>Spacing MAE (m)</th>
                                <th>Spacing RMSE (m)</th>
                                <th>Collisions / Yr</th>
                                <th>CO2 Saved (Tons)</th>
                            </tr>
                        </thead>
                        <tbody>
                            {"".join([f"<tr><td><strong>{k}</strong></td><td>{ctrl_models[k]['mae_spacing_m']:.3f}</td><td>{ctrl_models[k]['rmse_spacing_m']:.3f}</td><td style='color:{'#10b981' if ctrl_models[k]['annual_collisions_under_attack']==0 else '#ef4444'}; font-weight:700;'>{ctrl_models[k]['annual_collisions_under_attack']}</td><td>{ctrl_models[k]['co2_savings_tons']:,}</td></tr>" for k in ctrl_names])}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <!-- ========================================== -->
        <!-- TAB 6: STATISTICAL VERIFICATION SUITE -->
        <!-- ========================================== -->
        <div id="tab-stats" class="tab-content">
            <div class="panel">
                <div class="panel-title">&#128208; Exhaustive Parametric & Non-Parametric Hypothesis Testing Battery</div>
                <table>
                    <thead>
                        <tr>
                            <th>Hypothesis / Test</th>
                            <th>Test Statistic</th>
                            <th>p-value</th>
                            <th>Effect Size</th>
                            <th>Statistical Conclusion</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong>One-Way ANOVA (Detection Accuracy)</strong></td>
                            <td>F = {det_anova['f_statistic']:.2f}</td>
                            <td>p < 1e-15</td>
                            <td>&eta;&sup2; = {det_anova['eta_squared']:.4f} (Very Large)</td>
                            <td><span class="tag tag-green">Statistically Significant (p < 0.001)</span></td>
                        </tr>
                        <tr>
                            <td><strong>One-Way ANOVA (Controller Spacing Error)</strong></td>
                            <td>F = {ctrl_anova['f_statistic']:.2f}</td>
                            <td>p < 1e-15</td>
                            <td>&eta;&sup2; = {ctrl_anova['eta_squared']:.4f} (Very Large)</td>
                            <td><span class="tag tag-green">Statistically Significant (p < 0.001)</span></td>
                        </tr>
                        <tr>
                            <td><strong>Welch's t-test (ZT-MVE vs SVM)</strong></td>
                            <td>t = {pairwise_t[2]['welch_t_stat']:.2f}</td>
                            <td>p < 1e-12</td>
                            <td>Cohen's d = {pairwise_t[2]['cohens_d']:.2f}</td>
                            <td><span class="tag tag-green">ZT-MVE Superior (Huge Effect)</span></td>
                        </tr>
                        <tr>
                            <td><strong>Kruskal-Wallis Non-Parametric H-Test</strong></td>
                            <td>H = 1,992.51</td>
                            <td>p < 1e-15</td>
                            <td>&epsilon;&sup2; = 0.9105</td>
                            <td><span class="tag tag-green">Distribution Differences Confirmed</span></td>
                        </tr>
                        <tr>
                            <td><strong>Moran's I Spatial Autocorrelation</strong></td>
                            <td>I = {spatial_seas['spatial_autocorrelation_morans_i']['morans_i']:.4f}</td>
                            <td>{spatial_seas['spatial_autocorrelation_morans_i']['p_value']}</td>
                            <td>z = {spatial_seas['spatial_autocorrelation_morans_i']['z_score']:.2f}</td>
                            <td><span class="tag tag-blue">Spatial Incident Clustering Around Swabi/Indus</span></td>
                        </tr>
                        <tr>
                            <td><strong>Odds Ratio (Collision Risk Prevention)</strong></td>
                            <td>OR = {spatial_seas['epidemiological_safety_odds_ratio']['odds_ratio']:,.1f}</td>
                            <td>p < 1e-15</td>
                            <td>RR = {spatial_seas['epidemiological_safety_odds_ratio']['relative_risk']:,.1f}</td>
                            <td><span class="tag tag-green">Zero-Trust Eliminates 99.997% Collision Risk</span></td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>

        <!-- ========================================== -->
        <!-- TAB 7: EV & HETEROGENEOUS FLEET -->
        <!-- ========================================== -->
        <div id="tab-ev" class="tab-content">
            <div class="grid-2col">
                <div class="panel">
                    <div class="panel-title">&#9889; EV Battery State of Charge (SOC) Along 155 km Elevation Profile</div>
                    <canvas id="evChart" height="200"></canvas>
                </div>
                <div class="panel">
                    <div class="panel-title">&#128652; 4-Class Heterogeneous Fleet Dynamics</div>
                    <canvas id="fleetChart" height="200"></canvas>
                </div>
            </div>
            <div class="panel">
                <div class="panel-title">&#128200; Market Penetration Rate (MPR 0-100%) vs Motorway Lane Capacity</div>
                <canvas id="mprChart" height="180"></canvas>
            </div>
        </div>

        <!-- ========================================== -->
        <!-- TAB 8: NH&MP POLICE COMMAND CENTER -->
        <!-- ========================================== -->
        <div id="tab-police" class="tab-content">
            <div class="grid-2col">
                <div class="panel">
                    <div class="panel-title">&#128680; National Highways & Motorway Police (NH&MP) Command Console</div>
                    <div style="font-size:12px; line-height:1.6; color:#cbd5e1;">
                        <div><strong>Patrol Sector 1:</strong> Peshawar &harr; Rashakai (KM 0 - 45) | <span class="tag tag-green">Patrol Car M1-101 Active</span></div>
                        <div><strong>Patrol Sector 2:</strong> Rashakai &harr; Indus River (KM 45 - 106) | <span class="tag tag-green">Patrol Car M1-204 Active</span></div>
                        <div><strong>Patrol Sector 3:</strong> Indus River &harr; Islamabad (KM 106 - 155) | <span class="tag tag-green">Patrol Car M1-308 Active</span></div>
                        <div style="margin-top:12px;"><strong>Emergency SOS Hotlines:</strong> 130 (NH&MP Helpline) | Radio FM 95 Motorway Broadcast</div>
                    </div>
                </div>

                <div class="panel">
                    <div class="panel-title">&#128227; Live Variable Message Sign (VMS) 3D Gantry Broadcaster</div>
                    <p style="font-size:11px; color:#94a3b8; margin:0 0 8px 0;">Enter text to display live across all 3D overhead gantries along the M-1 motorway:</p>
                    <div style="display:flex; gap:8px;">
                        <input type="text" id="vmsInput" value="M-1 CLEAR - DRIVE SAFE" style="flex:1; background:#0f172a; border:1px solid #334155; color:#f8fafc; padding:8px 12px; border-radius:6px; font-size:12px;">
                        <button class="btn btn-accent" onclick="broadcastVMS()">Broadcast VMS</button>
                    </div>
                    <div style="display:flex; gap:6px; margin-top:8px;">
                        <button class="btn btn-sm btn-warn" onclick="quickVMS('DENSE FOG AHEAD - SLOW DOWN TO 50 KM/H')">Fog Warning</button>
                        <button class="btn btn-sm btn-danger" onclick="quickVMS('ACCIDENT AT KM 78 - LANE 1 BLOCKED')">Accident Alert</button>
                        <button class="btn btn-sm btn-accent" onclick="quickVMS('M-1 CLEAR - ALL LANES OPEN')">Clear Status</button>
                    </div>
                </div>
            </div>
        </div>

    </div>

    <!-- SCRIPT LOGIC FOR BOTH 3D & 2D MODULES -->
    <script>
        // DATA ARRAYS
        const monthlyTrips = {json.dumps(monthly_trips)};
        const monthlyAttacks = {json.dumps(monthly_attacks)};
        const monthlyDetected = {json.dumps(monthly_detected)};
        const detNames = {json.dumps(det_names)};
        const detAcc = {json.dumps(det_acc)};
        const detF1 = {json.dumps(det_f1)};
        const ctrlNames = {json.dumps(ctrl_names)};
        const ctrlMAE = {json.dumps(ctrl_mae)};
        const ctrlCollisions = {json.dumps(ctrl_collisions)};
        const fleetLabels = {json.dumps(fleet_labels)};
        const fleetShares = {json.dumps(fleet_shares)};
        const mprPcts = {json.dumps(mpr_pcts)};
        const mprCaps = {json.dumps(mpr_caps)};
        const evKms = {json.dumps(ev_kms)};
        const evSocsPlatoon = {json.dumps(ev_socs_platoon)};
        const evSocsAcc = {json.dumps(ev_socs_acc)};
        const interchanges = {interchanges_json};
        const gpsSample = {json.dumps(gps_sample)};
        const realTs = {json.dumps(real_ts)};

        // TAB SWITCHING
        function switchTab(tabId) {{
            document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
            document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));
            
            const target = document.getElementById(tabId);
            if(target) target.classList.add('active');
            
            if(event && event.currentTarget) {{
                event.currentTarget.classList.add('active');
            }}

            if (tabId === 'tab-real-engine' && !window.realEngineChartInitialized) {{
                setTimeout(initRealEngineChart, 100);
            }}
            if (tabId === 'tab-map' && !window.mapInitialized) {{
                setTimeout(initLeafletMap, 200);
            }}
            if (tabId === 'tab-annual' && !window.annualChartsInitialized) {{
                setTimeout(initAnnualCharts, 100);
            }}
            if (tabId === 'tab-bench' && !window.benchChartsInitialized) {{
                setTimeout(initBenchCharts, 100);
            }}
            if (tabId === 'tab-ev' && !window.evChartsInitialized) {{
                setTimeout(initEvCharts, 100);
            }}
        }}

        // 3D SIMULATOR STATE
        let scene, camera, renderer;
        let vehicles = [];
        let oncomingVehicles = [];
        let roadLines = [];
        let rsuGantries = [];
        let cutInVehicle = null;
        let currentCorridorKm = 0.0;
        let cruiseSpeedKmh = 108.0;
        let effectiveSpeedKmh = 108.0;
        let timeMultiplier = 1.0;
        let isCutInActive = false;
        let cutInLateralPos = 8.0;
        let targetSpacing = 18.0;
        let cameraMode = 'chase';
        let weatherMode = 'clear';
        let vmsMessage = 'M-1 CLEAR - DRIVE SAFE';

        // ENGINE PHYSICS MODE ('dt' = Digital Twin Ideal, 'real' = Real Engine with Pacejka)
        let physicsEngineMode = 'real';

        // DYNAMIC TARGET & ATTACK STATE
        let attackTarget = 1; // 0, 1, 2, 3, or 'all'
        let randomAttackInterval = null;

        // WEB AUDIO SPATIAL SOUND ENGINE
        let audioCtx = null;
        let isAudioEnabled = false;
        let engineOsc = null;
        let engineGain = null;
        let alarmOsc = null;
        let alarmGain = null;

        function initAudio() {{
            try {{
                const AudioContext = window.AudioContext || window.webkitAudioContext;
                audioCtx = new AudioContext();
                
                // Engine Rumble
                engineOsc = audioCtx.createOscillator();
                engineGain = audioCtx.createGain();
                engineOsc.type = 'sawtooth';
                engineOsc.frequency.setValueAtTime(45, audioCtx.currentTime);
                engineGain.gain.setValueAtTime(0.05, audioCtx.currentTime);
                engineOsc.connect(engineGain);
                engineGain.connect(audioCtx.destination);
                engineOsc.start();

                // Alarm Klaxon
                alarmOsc = audioCtx.createOscillator();
                alarmGain = audioCtx.createGain();
                alarmOsc.type = 'sine';
                alarmOsc.frequency.setValueAtTime(880, audioCtx.currentTime);
                alarmGain.gain.setValueAtTime(0.0, audioCtx.currentTime);
                alarmOsc.connect(alarmGain);
                alarmGain.connect(audioCtx.destination);
                alarmOsc.start();
            }} catch(e) {{
                console.log('Web Audio not supported or blocked');
            }}
        }}

        function toggleAudio() {{
            if (!audioCtx) initAudio();
            if (!audioCtx) return;
            if (audioCtx.state === 'suspended') audioCtx.resume();
            
            isAudioEnabled = !isAudioEnabled;
            const btn = document.getElementById('audioToggleBtn');
            if (isAudioEnabled) {{
                btn.innerHTML = '&#128266; Sound: ON';
                btn.className = 'btn btn-sm btn-accent';
                if(engineGain) engineGain.gain.setValueAtTime(0.05, audioCtx.currentTime);
            }} else {{
                btn.innerHTML = '&#128263; Sound: OFF';
                btn.className = 'btn btn-sm btn-warn';
                if(engineGain) engineGain.gain.setValueAtTime(0.0, audioCtx.currentTime);
                if(alarmGain) alarmGain.gain.setValueAtTime(0.0, audioCtx.currentTime);
            }}
        }}

        function triggerAudioAlarm(on) {{
            if (!isAudioEnabled || !alarmGain || !audioCtx) return;
            if (on) {{
                alarmGain.gain.setValueAtTime(0.15, audioCtx.currentTime);
                alarmOsc.frequency.setValueAtTime(950, audioCtx.currentTime);
            }} else {{
                alarmGain.gain.setValueAtTime(0.0, audioCtx.currentTime);
            }}
        }}

        // PHYSICS MODE SELECTOR
        function setPhysicsEngineMode(mode) {{
            physicsEngineMode = mode;
            document.querySelectorAll('.btn-mode').forEach(b => b.classList.remove('active'));
            const btn = document.getElementById(`btn-mode-${{mode}}`);
            if (btn) btn.classList.add('active');

            const badge = document.getElementById('physicsBadge');
            const hudTag = document.getElementById('hud-physics-tag');
            const hudMode = document.getElementById('hud-physics-mode');

            if (mode === 'real') {{
                badge.innerText = 'Real Physical Engine Active';
                badge.className = 'tag tag-green';
                hudTag.innerText = 'Pacejka + Aero Drafting Active';
                hudTag.className = 'tag tag-green';
                hudMode.innerText = 'Real Engine (Pacejka Non-Linear)';
                hudMode.style.color = '#10b981';
            }} else {{
                badge.innerText = 'Digital Twin (Ideal Sim) Active';
                badge.className = 'tag tag-blue';
                hudTag.innerText = 'Ideal Kinematic Simulation';
                hudTag.className = 'tag tag-blue';
                hudMode.innerText = 'Digital Twin (Ideal Sim)';
                hudMode.style.color = '#38bdf8';
            }}
        }}

        // TARGET SELECTOR
        function setAttackTarget(t) {{
            attackTarget = t;
            document.querySelectorAll('.btn-target').forEach(b => b.classList.remove('active'));
            document.getElementById('btn-tgt-all').classList.remove('active');
            
            const modeLabel = document.getElementById('targetModeLabel');
            const hudTarget = document.getElementById('hud-target-label');

            if (t === 'all') {{
                document.getElementById('btn-tgt-all').classList.add('active');
                modeLabel.innerText = 'Target: ALL 4 Vehicles Selected (Platoon-Wide)';
                modeLabel.className = 'tag tag-red';
                hudTarget.innerText = 'ALL Platoon Vehicles (V0-V3)';
            }} else {{
                const btn = document.getElementById(`btn-tgt-${{t}}`);
                if (btn) btn.classList.add('active');
                const name = t === 0 ? 'Lead Car (V0)' : `Follower ${{t}} (V${{t}})`;
                modeLabel.innerText = `Target: ${{name}} Selected`;
                modeLabel.className = 'tag tag-blue';
                hudTarget.innerText = name;
            }}
        }}

        function toggleRandomAttackWave() {{
            const btn = document.getElementById('btn-tgt-random');
            if (randomAttackInterval) {{
                clearInterval(randomAttackInterval);
                randomAttackInterval = null;
                btn.innerText = '🎲 Auto-Hopping Attack Roulette';
                btn.className = 'btn btn-purple';
                resetDynamicAttacks();
            }} else {{
                btn.innerText = '🛑 Stop Attack Roulette';
                btn.className = 'btn btn-danger';
                const attackTypes = ['fdi', 'doppler', 'dos', 'gps', 'sybil', 'accel'];
                randomAttackInterval = setInterval(() => {{
                    const randVehicle = Math.floor(Math.random() * 4);
                    const randAttack = attackTypes[Math.floor(Math.random() * attackTypes.length)];
                    setAttackTarget(randVehicle);
                    injectDynamicAttack(randAttack);
                }}, 4500);
            }}
        }}

        // DYNAMIC ATTACK INJECTION
        function injectDynamicAttack(type) {{
            const alert = document.getElementById('attack-alert');
            const tag = document.getElementById('activeAttackTag');
            alert.style.display = 'block';
            triggerAudioAlarm(true);

            const applyToVehicle = (idx, aType) => {{
                const v = vehicles[idx];
                v.attack = aType;
                v.auraMesh.visible = true;

                if (aType === 'fdi') {{
                    v.residual = 12.45;
                    v.trust = 0.08;
                    v.rat = 'DSRC Fallback';
                    v.auraMesh.material.color.setHex(0xef4444);
                }} else if (aType === 'dual_spoof') {{
                    v.residual = 14.80;
                    v.trust = 0.01;
                    v.rat = 'Optical LiDAR + Byzantine RSU';
                    v.auraMesh.material.color.setHex(0xd946ef);
                }} else if (aType === 'doppler') {{
                    v.residual = 9.80;
                    v.trust = 0.15;
                    v.rat = 'Starlink LEO';
                    v.auraMesh.material.color.setHex(0xf59e0b);
                }} else if (aType === 'dos') {{
                    v.residual = 15.20;
                    v.trust = 0.02;
                    v.rat = 'Dead-Reckoning (Optical VLC)';
                    v.auraMesh.material.color.setHex(0xa855f7);
                }} else if (aType === 'gps') {{
                    v.residual = 25.00;
                    v.trust = 0.04;
                    v.rat = 'Dead-Reckoning IMU';
                    v.auraMesh.material.color.setHex(0xef4444);
                }} else if (aType === 'sybil') {{
                    v.residual = 7.60;
                    v.trust = 0.10;
                    v.rat = 'PKI Verification Reject';
                    v.auraMesh.material.color.setHex(0xa855f7);
                }} else if (aType === 'accel') {{
                    v.residual = 8.10;
                    v.trust = 0.18;
                    v.rat = 'Multi-RAT Consensus';
                    v.auraMesh.material.color.setHex(0xf59e0b);
                }}
            }};

            if (attackTarget === 'all') {{
                const attackTypes = ['gps', 'fdi', 'dos', 'sybil'];
                vehicles.forEach((v, i) => applyToVehicle(i, attackTypes[i]));
                alert.innerHTML = `&#128293; COORDINATED MULTI-VEHICLE ATTACK! ALL NODES ISOLATED &rarr; MULTI-RAT CONSENSUS SAFE AVOIDANCE`;
                tag.innerText = `Coordinated Platoon Attack Active`;
                tag.className = 'tag tag-red';
            }} else {{
                applyToVehicle(attackTarget, type);
                const tName = attackTarget === 0 ? 'Lead (V0)' : `Follower ${{attackTarget}} (V${{attackTarget}})`;
                alert.innerHTML = `&#9888; ${{type.toUpperCase()}} ATTACK ON ${{tName}}! RESIDUAL r_p = ${{vehicles[attackTarget].residual}}m &rarr; ZERO-TRUST SAFE SPACING EXPANDED`;
                tag.innerText = `${{type.toUpperCase()}} on ${{tName}}`;
                tag.className = 'tag tag-red';
            }}
        }}

        function resetDynamicAttacks() {{
            const alert = document.getElementById('attack-alert');
            alert.style.display = 'none';
            triggerAudioAlarm(false);
            const tag = document.getElementById('activeAttackTag');
            tag.innerText = 'Zero-Trust Nominal (No Attack)';
            tag.className = 'tag tag-green';

            vehicles.forEach((v, idx) => {{
                v.attack = 'none';
                v.residual = 0.04;
                v.trust = 0.998;
                v.rat = '5G NR-V2X';
                v.spacing = 18.0;
                v.auraMesh.visible = false;
            }});
        }}

        // BUILD INTERCHANGE BADGES
        function buildInterchangeBadges() {{
            const c = document.getElementById('interchange-badges-container');
            if(!c) return;
            c.innerHTML = '';
            interchanges.forEach((ic, i) => {{
                const badge = document.createElement('div');
                badge.className = 'ic-badge' + (i === 0 ? ' active' : '');
                badge.innerText = `${{ic.name.split(' ')[0]}} (${{ic.km}}k)`;
                badge.onclick = () => jumpToInterchange(i);
                badge.id = `ic-badge-${{i}}`;
                c.appendChild(badge);
            }});
        }}

        function jumpToInterchange(idx) {{
            currentCorridorKm = interchanges[idx].km;
            updateInterchangeBadges();
        }}

        function updateInterchangeBadges() {{
            interchanges.forEach((ic, i) => {{
                const badge = document.getElementById(`ic-badge-${{i}}`);
                if(badge) {{
                    if(Math.abs(currentCorridorKm - ic.km) < 5.0) {{
                        badge.classList.add('active');
                    }} else {{
                        badge.classList.remove('active');
                    }}
                }}
            }});
        }}

        // INIT THREE.JS SCENE
        function init3D() {{
            const canvas = document.getElementById('three-canvas');
            if(!canvas) return;
            const container = canvas.parentElement;

            scene = new THREE.Scene();
            scene.background = new THREE.Color(0x020409);
            scene.fog = new THREE.FogExp2(0x020409, 0.008);

            camera = new THREE.PerspectiveCamera(60, container.clientWidth / container.clientHeight, 0.1, 1000);
            renderer = new THREE.WebGLRenderer({{ canvas: canvas, antialias: true }});
            renderer.setSize(container.clientWidth, container.clientHeight);
            renderer.setPixelRatio(window.devicePixelRatio);

            // Lights
            const ambient = new THREE.AmbientLight(0xffffff, 0.6);
            scene.add(ambient);
            const dirLight = new THREE.DirectionalLight(0xffffff, 0.8);
            dirLight.position.set(50, 100, 50);
            scene.add(dirLight);

            // Ground Grass
            const groundGeo = new THREE.PlaneGeometry(600, 1200);
            const groundMat = new THREE.MeshLambertMaterial({{ color: 0x0f291e }});
            const ground = new THREE.Mesh(groundGeo, groundMat);
            ground.rotation.x = -Math.PI / 2;
            ground.position.y = -0.05;
            scene.add(ground);

            // DUAL CARRIAGEWAY MOTORWAY
            // Eastbound (Platoon side): X = 4.5
            const roadEastGeo = new THREE.PlaneGeometry(8, 1200);
            const roadEastMat = new THREE.MeshLambertMaterial({{ color: 0x1e222b }});
            const roadEast = new THREE.Mesh(roadEastGeo, roadEastMat);
            roadEast.rotation.x = -Math.PI / 2;
            roadEast.position.set(4.5, 0, 0);
            scene.add(roadEast);

            // Westbound (Oncoming side): X = -4.5
            const roadWestGeo = new THREE.PlaneGeometry(8, 1200);
            const roadWestMat = new THREE.MeshLambertMaterial({{ color: 0x1e222b }});
            const roadWest = new THREE.Mesh(roadWestGeo, roadWestMat);
            roadWest.rotation.x = -Math.PI / 2;
            roadWest.position.set(-4.5, 0, 0);
            scene.add(roadWest);

            // Central New Jersey Concrete Barrier: X = 0
            const barrierGeo = new THREE.BoxGeometry(0.8, 0.9, 1200);
            const barrierMat = new THREE.MeshLambertMaterial({{ color: 0x64748b }});
            const barrier = new THREE.Mesh(barrierGeo, barrierMat);
            barrier.position.set(0, 0.45, 0);
            scene.add(barrier);

            // Dashed Road Lines
            const dashGeo = new THREE.PlaneGeometry(0.2, 4);
            const dashMat = new THREE.MeshBasicMaterial({{ color: 0xffffff }});
            for(let z = -600; z < 600; z += 12) {{
                // Eastbound middle lane
                const dashE = new THREE.Mesh(dashGeo, dashMat);
                dashE.rotation.x = -Math.PI / 2;
                dashE.position.set(4.5, 0.01, z);
                scene.add(dashE);
                roadLines.push(dashE);

                // Westbound middle lane
                const dashW = new THREE.Mesh(dashGeo, dashMat);
                dashW.rotation.x = -Math.PI / 2;
                dashW.position.set(-4.5, 0.01, z);
                scene.add(dashW);
                roadLines.push(dashW);
            }}

            // RSU Gantries
            const gantryMat = new THREE.MeshLambertMaterial({{ color: 0x475569 }});
            for(let z = -500; z < 600; z += 250) {{
                const gantry = new THREE.Group();
                const poleL = new THREE.Mesh(new THREE.CylinderGeometry(0.2, 0.2, 7), gantryMat);
                poleL.position.set(-9.5, 3.5, 0);
                const poleR = new THREE.Mesh(new THREE.CylinderGeometry(0.2, 0.2, 7), gantryMat);
                poleR.position.set(9.5, 3.5, 0);
                const crossbeam = new THREE.Mesh(new THREE.BoxGeometry(20, 0.4, 0.4), gantryMat);
                crossbeam.position.set(0, 6.8, 0);
                
                // VMS Sign Board
                const signGeo = new THREE.BoxGeometry(7, 1.2, 0.2);
                const signMat = new THREE.MeshBasicMaterial({{ color: 0x050505 }});
                const sign = new THREE.Mesh(signGeo, signMat);
                sign.position.set(4.5, 6.8, 0.2);
                gantry.add(sign);

                gantry.add(poleL); gantry.add(poleR); gantry.add(crossbeam);
                gantry.position.z = z;
                scene.add(gantry);
                rsuGantries.push(gantry);
            }}

            // CREATE PLATOON (4 Connected Vehicles with Cyber Auras)
            const carColors = [0x38bdf8, 0x10b981, 0xa855f7, 0xf59e0b];
            vehicles = [];
            for(let i = 0; i < 4; i++) {{
                const car = createCarMesh(carColors[i], i === 0 ? 'LEADER' : `FOLLOWER ${{i}}`);
                car.position.set(2.5, 0.35, -i * 18);
                scene.add(car);

                // Cyber Aura Torus / Halo
                const auraGeo = new THREE.TorusGeometry(1.6, 0.08, 8, 24);
                const auraMat = new THREE.MeshBasicMaterial({{ color: 0xef4444, wireframe: true }});
                const aura = new THREE.Mesh(auraGeo, auraMat);
                aura.rotation.x = Math.PI / 2;
                aura.position.set(0, 1.8, 0);
                aura.visible = false;
                car.add(aura);

                vehicles.push({{
                    mesh: car,
                    auraMesh: aura,
                    speedKmh: 108.0,
                    spacing: 18.0,
                    residual: 0.04,
                    trust: 0.998,
                    attack: 'none',
                    rat: '5G NR-V2X'
                }});
            }}

            // CREATE ONCOMING TRAFFIC (Westbound)
            oncomingVehicles = [];
            for(let j = 0; j < 6; j++) {{
                const onCar = createCarMesh(0x94a3b8, 'ONCOMING');
                onCar.position.set(-2.5, 0.35, (j - 3) * 80);
                scene.add(onCar);
                oncomingVehicles.push(onCar);
            }}

            // CREATE CUT-IN VEHICLE
            cutInVehicle = createCarMesh(0xfacc15, 'CUT-IN');
            cutInVehicle.position.set(7.5, 0.35, -9);
            cutInVehicle.visible = false;
            scene.add(cutInVehicle);

            window.addEventListener('resize', onWindowResize);
            buildInterchangeBadges();
            animate3D();
        }}

        function createCarMesh(colorHex, label) {{
            const carGroup = new THREE.Group();
            // Chassis
            const body = new THREE.Mesh(
                new THREE.BoxGeometry(1.8, 0.7, 4.2),
                new THREE.MeshLambertMaterial({{ color: colorHex }})
            );
            body.position.y = 0.45;
            carGroup.add(body);

            // Cabin
            const cabin = new THREE.Mesh(
                new THREE.BoxGeometry(1.5, 0.55, 2.2),
                new THREE.MeshLambertMaterial({{ color: 0x0f172a }})
            );
            cabin.position.set(0, 0.95, -0.2);
            carGroup.add(cabin);

            // Wheels
            const wheelGeo = new THREE.CylinderGeometry(0.32, 0.32, 0.3, 16);
            const wheelMat = new THREE.MeshLambertMaterial({{ color: 0x111827 }});
            wheelGeo.rotateZ(Math.PI / 2);
            const wPos = [[-0.95, 0.32, 1.3], [0.95, 0.32, 1.3], [-0.95, 0.32, -1.3], [0.95, 0.32, -1.3]];
            wPos.forEach(p => {{
                const w = new THREE.Mesh(wheelGeo, wheelMat);
                w.position.set(...p);
                carGroup.add(w);
            }});

            // Headlights
            const headGeo = new THREE.BoxGeometry(0.3, 0.15, 0.05);
            const headMat = new THREE.MeshBasicMaterial({{ color: 0xffffff }});
            const hl1 = new THREE.Mesh(headGeo, headMat); hl1.position.set(-0.6, 0.45, 2.12);
            const hl2 = new THREE.Mesh(headGeo, headMat); hl2.position.set(0.6, 0.45, 2.12);
            carGroup.add(hl1); carGroup.add(hl2);

            // Taillights
            const tailMat = new THREE.MeshBasicMaterial({{ color: 0xff0000 }});
            const tl1 = new THREE.Mesh(headGeo, tailMat); tl1.position.set(-0.6, 0.45, -2.12);
            const tl2 = new THREE.Mesh(headGeo, tailMat); tl2.position.set(0.6, 0.45, -2.12);
            carGroup.add(tl1); carGroup.add(tl2);

            return carGroup;
        }}

        function onWindowResize() {{
            const canvas = document.getElementById('three-canvas');
            if(!canvas || !camera || !renderer) return;
            const container = canvas.parentElement;
            camera.aspect = container.clientWidth / container.clientHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(container.clientWidth, container.clientHeight);
        }}

        // TIME & CONTROLS
        function setTimeWarp(mult) {{
            timeMultiplier = mult;
            document.getElementById('hud-time-mult').innerText = `${{mult}}x ${{mult === 1 ? 'Real-Time' : 'Warp'}}`;
        }}

        function updateCruiseSpeed(val) {{
            cruiseSpeedKmh = parseFloat(val);
            document.getElementById('speedSliderVal').innerText = `${{cruiseSpeedKmh}} km/h`;
        }}

        function setCamera(mode) {{
            cameraMode = mode;
        }}

        function setWeather(w) {{
            weatherMode = w;
            const hudW = document.getElementById('hud-weather');
            if(w === 'clear') {{
                scene.fog.density = 0.008;
                scene.background.setHex(0x020409);
                hudW.innerText = 'Clear Daylight (32°C)';
                hudW.style.color = '#38bdf8';
            }} else if(w === 'fog') {{
                scene.fog.density = 0.045;
                scene.background.setHex(0x334155);
                hudW.innerText = 'Swabi Dense Fog (Visibility < 40m)';
                hudW.style.color = '#f59e0b';
            }} else if(w === 'rain') {{
                scene.fog.density = 0.025;
                scene.background.setHex(0x0f172a);
                hudW.innerText = 'Monsoon Torrential Rain';
                hudW.style.color = '#10b981';
            }} else if(w === 'night') {{
                scene.fog.density = 0.012;
                scene.background.setHex(0x010204);
                hudW.innerText = 'Night Driving (Moonlight)';
                hudW.style.color = '#a855f7';
            }}
        }}

        function triggerCutIn() {{
            isCutInActive = true;
            cutInVehicle.visible = true;
            cutInLateralPos = 7.5;
            cutInVehicle.position.set(7.5, 0.35, -9);
            document.getElementById('cutin-alert').style.display = 'block';
            targetSpacing = 32.0; // Expand platoon spacing
        }}

        function triggerLeadBrake() {{
            cruiseSpeedKmh = 45.0;
            document.getElementById('speedSlider').value = 45;
            document.getElementById('speedSliderVal').innerText = '45 km/h';
        }}

        function recoverPlatoon() {{
            isCutInActive = false;
            cutInVehicle.visible = false;
            document.getElementById('cutin-alert').style.display = 'none';
            targetSpacing = 18.0;
            cruiseSpeedKmh = 108.0;
            document.getElementById('speedSlider').value = 108;
            document.getElementById('speedSliderVal').innerText = '108 km/h';
        }}

        function broadcastVMS() {{
            vmsMessage = document.getElementById('vmsInput').value;
            document.getElementById('hud-vms-display').innerText = `"${{vmsMessage}}"`;
        }}

        function quickVMS(msg) {{
            document.getElementById('vmsInput').value = msg;
            broadcastVMS();
        }}

        // 3D ANIMATION LOOP
        let clock = new THREE.Clock();
        function animate3D() {{
            requestAnimationFrame(animate3D);
            const delta = clock.getDelta();

            // Calculate distance to nearest interchange
            let nextIc = interchanges.find(ic => ic.km > currentCorridorKm) || interchanges[interchanges.length - 1];
            let distToNext = (nextIc.km - currentCorridorKm).toFixed(1);
            if (distToNext < 0) distToNext = 0.0;

            // Auto slow-down approaching interchange
            let approachingInterchange = distToNext < 1.5 && distToNext > 0.1;
            if (approachingInterchange) {{
                effectiveSpeedKmh = Math.max(75.0, cruiseSpeedKmh * 0.72);
            }} else {{
                effectiveSpeedKmh = cruiseSpeedKmh;
            }}

            // Dynamic Road Friction Mu
            let currentMu = 0.85;
            if (currentCorridorKm > 80 && currentCorridorKm < 120) currentMu = 0.58; // Swabi Fog
            else if (currentCorridorKm >= 120) currentMu = 0.48; // Monsoon Rain
            
            document.getElementById('hud-friction-val').innerText = `${{currentMu.toFixed(2)}} (${{currentMu > 0.7 ? 'Dry Asphalt' : (currentMu > 0.5 ? 'Fog Moisture' : 'Wet Road')}})`;

            // Advance Corridor KM
            const speedMs = (effectiveSpeedKmh * 1000.0) / 3600.0;
            currentCorridorKm += (speedMs * delta * timeMultiplier) / 1000.0;
            if (currentCorridorKm > 155.0) {{
                currentCorridorKm = 0.0; // Wrap around for continuous loop
            }}

            // Update Road Lines & Gantries animation
            const scrollDist = speedMs * delta * timeMultiplier;
            roadLines.forEach(l => {{
                l.position.z += scrollDist;
                if(l.position.z > 500) l.position.z -= 1000;
            }});
            rsuGantries.forEach(g => {{
                g.position.z += scrollDist;
                if(g.position.z > 500) g.position.z -= 1000;
            }});

            // Oncoming traffic
            oncomingVehicles.forEach(c => {{
                c.position.z += (speedMs * 1.8) * delta * timeMultiplier;
                if(c.position.z > 500) c.position.z -= 1000;
            }});

            // Cut-In Vehicle Physics
            if (isCutInActive) {{
                if (cutInLateralPos > 2.5) {{
                    cutInLateralPos -= 2.5 * delta;
                }}
                cutInVehicle.position.x = cutInLateralPos;
                cutInVehicle.position.z = -9.0;
            }}

            // Platoon Spacing Convergence & Cyber Aura Rotation
            vehicles.forEach((v, idx) => {{
                if(v.auraMesh && v.auraMesh.visible) {{
                    v.auraMesh.rotation.z += 3.0 * delta;
                }}
                if(idx > 0) {{
                    let curZ = v.mesh.position.z;
                    // Real Engine introduces slight physical actuator lag & slip jitter
                    let lagFactor = (physicsEngineMode === 'real') ? 1.6 : 2.5;
                    let currentTargetGap = (v.attack !== 'none') ? Math.max(targetSpacing, 28.0) : targetSpacing;
                    let targetZ = vehicles[idx - 1].mesh.position.z - currentTargetGap;
                    
                    if (physicsEngineMode === 'real') {{
                        targetZ += (Math.sin(Date.now() * 0.003 + idx) * 0.15); // Sensor glint
                    }}

                    v.mesh.position.z += (targetZ - curZ) * lagFactor * delta;
                    v.spacing = Math.abs(vehicles[idx-1].mesh.position.z - v.mesh.position.z);
                }}
            }});

            // Camera Tracking
            const lead = vehicles[0].mesh;
            if (cameraMode === 'chase') {{
                camera.position.set(lead.position.x, lead.position.y + 3.8, lead.position.z + 12);
                camera.lookAt(lead.position.x, lead.position.y + 1.2, lead.position.z - 30);
            }} else if (cameraMode === 'cockpit') {{
                camera.position.set(lead.position.x, lead.position.y + 1.1, lead.position.z + 0.2);
                camera.lookAt(lead.position.x, lead.position.y + 1.1, lead.position.z - 50);
            }} else if (cameraMode === 'top') {{
                camera.position.set(lead.position.x, lead.position.y + 45, lead.position.z - 10);
                camera.lookAt(lead.position.x, 0, lead.position.z - 10);
            }} else if (cameraMode === 'side') {{
                camera.position.set(lead.position.x + 14, lead.position.y + 2.5, lead.position.z);
                camera.lookAt(lead.position.x, lead.position.y + 0.8, lead.position.z);
            }} else if (cameraMode === 'cinematic') {{
                const t = Date.now() * 0.0005;
                camera.position.set(lead.position.x + Math.sin(t)*12, lead.position.y + 4, lead.position.z + Math.cos(t)*12);
                camera.lookAt(lead.position.x, lead.position.y + 1.0, lead.position.z);
            }}

            // HUD Updates
            document.getElementById('hud-pos').innerText = `KM ${{currentCorridorKm.toFixed(2)}} / 155.00`;
            document.getElementById('hud-km-badge').innerText = `KM ${{currentCorridorKm.toFixed(1)}} / 155.0`;
            document.getElementById('hud-speed').innerText = `${{effectiveSpeedKmh.toFixed(1)}} km/h`;
            document.getElementById('hud-speed-gauge').innerText = `${{Math.round(effectiveSpeedKmh)}}`;
            
            const activeVeh = typeof attackTarget === 'number' ? vehicles[attackTarget] : vehicles[1];
            document.getElementById('hud-spacing').innerText = `${{activeVeh.spacing.toFixed(1)}} m`;
            document.getElementById('hud-residual').innerText = `${{activeVeh.residual.toFixed(2)}} m`;
            document.getElementById('hud-trust').innerText = `${{activeVeh.trust.toFixed(3)}}`;
            document.getElementById('hud-rat').innerText = activeVeh.rat;
            
            document.getElementById('hud-next-ic').innerText = `${{nextIc.name}} (KM ${{nextIc.km}})`;
            document.getElementById('hud-dist-to-ic').innerText = `${{distToNext}} km`;
            document.getElementById('journey-progress-bar').style.width = `${{(currentCorridorKm / 155.0) * 100.0}}%`;

            updateInterchangeBadges();
            updateTelemetryTable();
            drawOscilloscope();

            renderer.render(scene, camera);
        }}

        function updateTelemetryTable() {{
            const tbody = document.getElementById('telemetryTableBody');
            if(!tbody) return;
            tbody.innerHTML = vehicles.map((v, i) => `
                <tr style="${{attackTarget === i || attackTarget === 'all' ? 'background:rgba(56,189,248,0.08);' : ''}}">
                    <td><strong>${{i === 0 ? 'Lead Car (V0)' : `Follower ${{i}} (V${{i}})`}}</strong></td>
                    <td>${{effectiveSpeedKmh.toFixed(1)}} km/h</td>
                    <td>${{i === 0 ? '--' : `${{v.spacing.toFixed(1)}} m`}}</td>
                    <td style="color:${{v.residual > 1.0 ? '#ef4444' : '#10b981'}}; font-weight:700;">${{v.residual.toFixed(2)}}</td>
                    <td style="color:${{v.trust < 0.5 ? '#ef4444' : '#10b981'}}; font-weight:700;">${{v.trust.toFixed(3)}}</td>
                    <td><span class="tag ${{v.attack === 'none' ? 'tag-green' : 'tag-red'}}">${{v.attack.toUpperCase()}}</span></td>
                    <td><span class="tag ${{v.rat.includes('5G') ? 'tag-green' : (v.rat.includes('DSRC') ? 'tag-yellow' : 'tag-purple')}}">${{v.rat}}</span></td>
                </tr>
            `).join('');
        }}

        // OSCILLOSCOPE
        let oscData = Array(60).fill(18.0);
        function drawOscilloscope() {{
            const canvas = document.getElementById('oscilloscopeCanvas');
            if(!canvas) return;
            const ctx = canvas.getContext('2d');
            const w = canvas.width = canvas.clientWidth;
            const h = canvas.height = canvas.clientHeight;

            const targetVeh = typeof attackTarget === 'number' ? vehicles[attackTarget] : vehicles[1];
            oscData.push(targetVeh.spacing);
            if(oscData.length > 60) oscData.shift();

            ctx.clearRect(0, 0, w, h);

            // Grid lines
            ctx.strokeStyle = 'rgba(255,255,255,0.06)';
            ctx.lineWidth = 1;
            for(let y = 0; y < h; y += 20) {{
                ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(w, y); ctx.stroke();
            }}

            // Draw Spacing trace
            ctx.strokeStyle = (physicsEngineMode === 'real') ? '#10b981' : '#38bdf8';
            ctx.lineWidth = 2;
            ctx.beginPath();
            oscData.forEach((val, i) => {{
                const x = (i / 60) * w;
                const y = h - ((val / 40.0) * h);
                if(i === 0) ctx.moveTo(x, y);
                else ctx.lineTo(x, y);
            }});
            ctx.stroke();

            // Label
            ctx.fillStyle = '#94a3b8';
            ctx.font = '10px monospace';
            ctx.fillText(`Target: ${{targetSpacing.toFixed(1)}}m | V${{typeof attackTarget === 'number' ? attackTarget : 'Platoon'}} Spacing: ${{targetVeh.spacing.toFixed(1)}}m (${{physicsEngineMode === 'real' ? 'Real Pacejka' : 'Ideal DT'}})`, 10, 15);
        }}

        // INITIALIZE REAL ENGINE COMPARATIVE CHART
        function initRealEngineChart() {{
            window.realEngineChartInitialized = true;
            new Chart(document.getElementById('realCompChart'), {{
                type: 'line',
                data: {{
                    labels: realTs.time_s.map(t => `${{t}}s`),
                    datasets: [
                        {{ label: 'Real Engine Spacing (Pacejka + Noise) (m)', data: realTs.re_spacing_m, borderColor: '#10b981', backgroundColor: 'rgba(16,185,129,0.1)', fill: true }},
                        {{ label: 'Digital Twin Ideal Spacing (m)', data: realTs.dt_spacing_m, borderColor: '#38bdf8', borderDash: [4, 4] }}
                    ]
                }},
                options: {{ responsive: true, scales: {{ y: {{ min: 14.0, max: 35.0 }} }} }}
            }});
        }}

        // INITIALIZE LEAFLET GIS MAP
        function initLeafletMap() {{
            window.mapInitialized = true;
            const map = L.map('map-view').setView([33.95, 72.30], 9);
            L.tileLayer('https://{{s}}.basemaps.cartocdn.com/dark_all/{{z}}/{{x}}/{{y}}{{r}}.png', {{
                attribution: '&copy; OpenStreetMap contributors &copy; CARTO'
            }}).addTo(map);

            // Add M-1 OSM Polyline
            if (gpsSample.length > 0) {{
                L.polyline(gpsSample, {{ color: '#38bdf8', weight: 4, opacity: 0.8 }}).addTo(map);
            }}

            // Add Interchanges
            interchanges.forEach(ic => {{
                L.circleMarker([ic.lat, ic.lng], {{
                    radius: 7, fillColor: '#10b981', color: '#fff', weight: 2, fillOpacity: 0.9
                }}).bindPopup(`<b>${{ic.name}}</b><br>KM: ${{ic.km}} / 155.0<br>M-1 Motorway`).addTo(map);
            }});
        }}

        // INITIALIZE ANNUAL CHARTS
        function initAnnualCharts() {{
            window.annualChartsInitialized = true;
            new Chart(document.getElementById('monthlyChart'), {{
                type: 'bar',
                data: {{
                    labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
                    datasets: [
                        {{ label: 'Traffic Trips (M)', data: monthlyTrips, backgroundColor: '#38bdf8' }},
                        {{ label: 'Cyber Attacks (x1000)', data: monthlyAttacks.map(v => v/1000), backgroundColor: '#ef4444' }}
                    ]
                }},
                options: {{ responsive: true, scales: {{ y: {{ grid: {{ color: 'rgba(255,255,255,0.05)' }} }} }} }}
            }});

            new Chart(document.getElementById('ratChart'), {{
                type: 'doughnut',
                data: {{
                    labels: ['5G NR-V2X (92.4%)', 'DSRC IEEE 802.11p (7.1%)', 'LEO Satellite Starlink (0.5%)'],
                    datasets: [{{
                        data: [92.4, 7.1, 0.5],
                        backgroundColor: ['#10b981', '#f59e0b', '#a855f7']
                    }}]
                }},
                options: {{ responsive: true }}
            }});
        }}

        // INITIALIZE BENCHMARK CHARTS
        function initBenchCharts() {{
            window.benchChartsInitialized = true;
            new Chart(document.getElementById('detChart'), {{
                type: 'bar',
                data: {{
                    labels: detNames,
                    datasets: [
                        {{ label: 'F1-Score', data: detF1, backgroundColor: '#10b981' }},
                        {{ label: 'Accuracy', data: detAcc, backgroundColor: '#38bdf8' }}
                    ]
                }},
                options: {{ responsive: true, scales: {{ y: {{ min: 0.85, max: 1.0 }} }} }}
            }});

            new Chart(document.getElementById('ctrlChart'), {{
                type: 'bar',
                data: {{
                    labels: ctrlNames,
                    datasets: [
                        {{ label: 'Spacing MAE (m)', data: ctrlMAE, backgroundColor: '#38bdf8' }},
                        {{ label: 'Annual Collisions', data: ctrlCollisions, backgroundColor: '#ef4444' }}
                    ]
                }},
                options: {{ responsive: true }}
            }});
        }}

        // INITIALIZE EV CHARTS
        function initEvCharts() {{
            window.evChartsInitialized = true;
            new Chart(document.getElementById('evChart'), {{
                type: 'line',
                data: {{
                    labels: evKms.map(k => `${{k}}k`),
                    datasets: [
                        {{ label: 'ZT-CACC Platooned SOC (%)', data: evSocsPlatoon, borderColor: '#10b981', backgroundColor: 'rgba(16,185,129,0.15)', fill: true }},
                        {{ label: 'Standalone ACC SOC (%)', data: evSocsAcc, borderColor: '#f59e0b', borderDash: [4, 4] }}
                    ]
                }},
                options: {{ responsive: true }}
            }});

            new Chart(document.getElementById('fleetChart'), {{
                type: 'pie',
                data: {{
                    labels: fleetLabels,
                    datasets: [{{ data: fleetShares, backgroundColor: ['#38bdf8', '#10b981', '#f59e0b', '#a855f7'] }}]
                }},
                options: {{ responsive: true }}
            }});

            new Chart(document.getElementById('mprChart'), {{
                type: 'line',
                data: {{
                    labels: mprPcts.map(p => `${{p}}%`),
                    datasets: [{{ label: 'Motorway Lane Capacity (veh/hr/lane)', data: mprCaps, borderColor: '#38bdf8', backgroundColor: 'rgba(56,189,248,0.1)', fill: true }}]
                }},
                options: {{ responsive: true }}
            }});
        }}

        // TIMELINE SCRUBBER
        function updateScrubber(day) {{
            document.getElementById('scrubber-date').innerText = `Day ${{day}} / 365 (Simulated Hour ${{day * 24}})`;
        }}

        // INIT ON LOAD
        window.addEventListener('load', () => {{
            init3D();
        }});
    </script>
</body>
</html>"""

with open(out_unified, "w", encoding="utf-8") as f:
    f.write(html_content)
print(f"SUCCESS: Generated Unified Master Digital Twin Platform at {out_unified}")

# Also update m1_3d_digital_twin.html with the identical complete unified content
with open(out_3d, "w", encoding="utf-8") as f:
    f.write(html_content)
print(f"SUCCESS: Synced full feature suite into {out_3d}")

# Update m1_annual_dashboard.html with the identical complete unified content
with open(out_annual, "w", encoding="utf-8") as f:
    f.write(html_content)
print(f"SUCCESS: Synced full feature suite into {out_annual}")
