import json
import os

results_path = r"C:\Users\umert\.gemini\antigravity\scratch\m1_digital_twin\results\m1_365day_annual_results.json"
benchmark_path = r"C:\Users\umert\.gemini\antigravity\scratch\m1_digital_twin\results\m1_multi_algorithm_benchmark.json"
stats_path = r"C:\Users\umert\.gemini\antigravity\scratch\m1_digital_twin\results\m1_comprehensive_statistical_tests.json"
fleet_path = r"C:\Users\umert\.gemini\antigravity\scratch\m1_digital_twin\results\m1_heterogeneous_fleet_results.json"
rsu_ev_path = r"C:\Users\umert\.gemini\antigravity\scratch\m1_digital_twin\results\m1_rsu_ev_mpr_results.json"
out_html = r"C:\Users\umert\.gemini\antigravity\scratch\m1_digital_twin\visualization\m1_annual_dashboard.html"

with open(results_path, "r", encoding="utf-8") as f:
    data = json.load(f)

with open(benchmark_path, "r", encoding="utf-8") as f:
    bench = json.load(f)

with open(stats_path, "r", encoding="utf-8") as f:
    stat_suite = json.load(f)

with open(fleet_path, "r", encoding="utf-8") as f:
    fleet_data = json.load(f)

with open(rsu_ev_path, "r", encoding="utf-8") as f:
    rsu_ev_data = json.load(f)

summary = data["summary"]
monthly = data["monthly"]
daily = data["daily_samples"]

det_models = bench["cybersecurity_detection_benchmark"]
ctrl_models = bench["platoon_control_benchmark"]
fleet_classes = fleet_data["fleet_breakdown"]

# RSU & EV data
rsus = rsu_ev_data["rsu_infrastructure_grid"]
mpr_curves = rsu_ev_data["mixed_autonomy_mpr_curves"]
ev_dynamics = rsu_ev_data["ev_battery_dynamics"]
service_areas = rsu_ev_data["service_area_charging_infrastructure"]

# Stats suite extractions
pairwise_t = stat_suite["parametric_tests"]["detection_models_pairwise_t"]
det_anova = stat_suite["parametric_tests"]["detection_models_one_way_anova"]
ctrl_anova = stat_suite["parametric_tests"]["controller_models_one_way_anova"]
corrs = stat_suite["correlations"]
spatial_seas = stat_suite["spatial_and_seasonal_motorway_tests"]

months_labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
monthly_trips = [monthly[str(m)]["trips"] / 1e6 for m in range(1, 13)]
monthly_attacks = [monthly[str(m)]["attacks"] for m in range(1, 13)]
monthly_detected = [monthly[str(m)]["detected"] for m in range(1, 13)]
monthly_failovers = [monthly[str(m)]["failovers"] / 1e3 for m in range(1, 13)]
monthly_co2 = [monthly[str(m)]["carbon_saved_tons"] for m in range(1, 13)]

# Benchmark data arrays for Chart.js
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

# Fleet data arrays
fleet_labels = list(fleet_classes.keys())
fleet_shares = [fleet_classes[k]["fleet_share_pct"] for k in fleet_labels]
fleet_co2 = [fleet_classes[k]["annual_co2_saved_tons"] for k in fleet_labels]

# MPR data arrays
mpr_pcts = [m["mpr_pct"] for m in mpr_curves]
mpr_caps = [m["lane_capacity_veh_hr"] for m in mpr_curves]
mpr_co2s = [m["annual_co2_saved_tons"] for m in mpr_curves]

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>M-1 Motorway 365-Day 24x7 Digital Twin | Complete Master Dashboard 2.0</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <style>
        :root {{
            --bg: #0b1120;
            --card-bg: rgba(30, 41, 59, 0.7);
            --border: rgba(255, 255, 255, 0.08);
            --text: #f8fafc;
            --primary: #38bdf8;
            --accent: #10b981;
            --danger: #ef4444;
            --warn: #f59e0b;
            --purple: #a855f7;
        }}
        body {{
            margin: 0; padding: 0; background: var(--bg); color: var(--text);
            font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
            overflow-x: hidden;
        }}
        .header {{
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
            padding: 20px 32px; border-bottom: 1px solid var(--border);
            display: flex; justify-content: space-between; align-items: center;
        }}
        .header h1 {{ margin: 0; font-size: 22px; color: #fff; font-weight: 700; }}
        .header p {{ margin: 4px 0 0 0; color: #94a3b8; font-size: 13px; }}
        .badge-live {{
            background: #10b981; color: white; padding: 6px 14px; border-radius: 20px;
            font-size: 12px; font-weight: 700; display: inline-flex; align-items: center; gap: 6px;
        }}
        .badge-live::before {{
            content: ''; width: 8px; height: 8px; background: white; border-radius: 50%;
            animation: pulse 1.5s infinite;
        }}
        @keyframes pulse {{ 0% {{ opacity: 1; }} 50% {{ opacity: 0.3; }} 100% {{ opacity: 1; }} }}
        .container {{ max-width: 1440px; margin: 0 auto; padding: 24px; }}
        
        .grid-kpis {{
            display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; margin-bottom: 24px;
        }}
        .kpi-card {{
            background: var(--card-bg); border: 1px solid var(--border);
            border-radius: 14px; padding: 20px; backdrop-filter: blur(10px);
            transition: transform 0.2s, border-color 0.2s;
        }}
        .kpi-card:hover {{ transform: translateY(-2px); border-color: var(--primary); }}
        .kpi-label {{ font-size: 12px; font-weight: 600; text-transform: uppercase; color: #94a3b8; letter-spacing: 0.5px; }}
        .kpi-val {{ font-size: 28px; font-weight: 800; color: #fff; margin: 8px 0 4px 0; }}
        .kpi-sub {{ font-size: 12px; color: var(--accent); font-weight: 500; }}

        .grid-main {{
            display: grid; grid-template-columns: 2fr 1fr; gap: 24px; margin-bottom: 24px;
        }}
        .chart-box {{
            background: var(--card-bg); border: 1px solid var(--border);
            border-radius: 14px; padding: 20px; backdrop-filter: blur(10px);
        }}
        .chart-title {{ font-size: 16px; font-weight: 700; margin-bottom: 16px; color: var(--primary); }}
        #map-view {{ height: 380px; width: 100%; border-radius: 10px; }}

        .scrubber-panel {{
            background: var(--card-bg); border: 1px solid var(--border);
            border-radius: 14px; padding: 20px; margin-bottom: 24px;
        }}
        .slider-wrap {{ display: flex; align-items: center; gap: 16px; margin-top: 12px; }}
        .slider {{
            flex: 1; -webkit-appearance: none; height: 8px; border-radius: 4px;
            background: #334155; outline: none;
        }}
        .slider::-webkit-slider-thumb {{
            -webkit-appearance: none; appearance: none; width: 20px; height: 20px;
            border-radius: 50%; background: var(--primary); cursor: pointer;
            box-shadow: 0 0 10px var(--primary);
        }}

        .section-header {{
            margin: 36px 0 16px 0; padding-bottom: 8px; border-bottom: 1px solid rgba(255,255,255,0.1);
            display: flex; justify-content: space-between; align-items: flex-end;
        }}
        .section-title {{ font-size: 20px; font-weight: 800; color: #38bdf8; display: flex; align-items: center; gap: 8px; }}
        .section-subtitle {{ font-size: 13px; color: #94a3b8; }}

        .table-responsive {{
            overflow-x: auto; margin-top: 16px; border-radius: 10px; border: 1px solid var(--border);
        }}
        table {{
            width: 100%; border-collapse: collapse; text-align: left; font-size: 13px;
        }}
        th, td {{ padding: 12px 16px; border-bottom: 1px solid var(--border); }}
        th {{ background: rgba(15, 23, 42, 0.8); color: #94a3b8; font-weight: 600; text-transform: uppercase; font-size: 11px; }}
        tr:hover {{ background: rgba(255, 255, 255, 0.03); }}
        .badge-tag {{
            padding: 3px 8px; border-radius: 6px; font-size: 11px; font-weight: 700;
        }}
        .badge-green {{ background: rgba(16, 185, 129, 0.2); color: #10b981; }}
        .badge-blue {{ background: rgba(56, 189, 248, 0.2); color: #38bdf8; }}
        .badge-red {{ background: rgba(239, 68, 68, 0.2); color: #ef4444; }}
        .badge-yellow {{ background: rgba(245, 158, 11, 0.2); color: #f59e0b; }}
        .badge-purple {{ background: rgba(168, 85, 247, 0.2); color: #a855f7; }}

        .btn-launch {{
            background: linear-gradient(135deg, #38bdf8 0%, #3b82f6 100%);
            color: #0b1120; font-weight: 800; padding: 10px 20px; border-radius: 10px;
            text-decoration: none; display: inline-flex; align-items: center; gap: 8px;
            box-shadow: 0 4px 15px rgba(56, 189, 248, 0.4); transition: transform 0.2s;
        }}
        .btn-launch:hover {{ transform: translateY(-2px); }}
    </style>
</head>
<body>

    <div class="header">
        <div>
            <h1>M-1 Motorway 365-Day 24x7 Digital Twin Master Dashboard</h1>
            <p>Peshawar &harr; Islamabad (155 km) | 10 Interchanges | 87 RSUs | 38.9M Vehicles | Multi-Class Heterogeneous Fleet</p>
        </div>
        <div style="display:flex; gap:12px; align-items:center;">
            <a href="m1_3d_digital_twin.html" class="btn-launch">&#9658; LAUNCH 3D WEBGL SIMULATOR</a>
            <div class="badge-live">MASTER TWIN ACTIVE</div>
        </div>
    </div>

    <div class="container">

        <!-- KPI SUMMARY ROW -->
        <div class="grid-kpis">
            <div class="kpi-card">
                <div class="kpi-label">Annual Trips Simulated</div>
                <div class="kpi-val">{summary['total_trips']:,}</div>
                <div class="kpi-sub">&uarr; ~106,702 vehicles / day avg</div>
            </div>
            <div class="kpi-card">
                <div class="kpi-label">Cyber Attacks Neutralized</div>
                <div class="kpi-val" style="color: #38bdf8;">{summary['total_detected']:,} / {summary['total_attacks']:,}</div>
                <div class="kpi-sub" style="color: #10b981;">&check; {summary['detection_accuracy_pct']}% ZT-MVE Accuracy</div>
            </div>
            <div class="kpi-card">
                <div class="kpi-label">Multi-RAT Failovers</div>
                <div class="kpi-val" style="color: #f59e0b;">{summary['total_failovers']:,}</div>
                <div class="kpi-sub">5G-V2X &harr; DSRC &harr; Optical VLC</div>
            </div>
            <div class="kpi-card">
                <div class="kpi-label">Collisions (ZT-CACC)</div>
                <div class="kpi-val" style="color: #10b981;">{summary['collisions_zt']}</div>
                <div class="kpi-sub">&check; {summary['collisions_prevented']:,} accidents prevented</div>
            </div>
            <div class="kpi-card">
                <div class="kpi-label">Annual CO2 Saved</div>
                <div class="kpi-val" style="color: #10b981;">{summary['carbon_saved_metric_tons']:,.1f} t</div>
                <div class="kpi-sub">&uarr; Aerodynamic Platoon Benefit</div>
            </div>
        </div>

        <!-- 365-DAY TIMELINE SCRUBBER -->
        <div class="scrubber-panel">
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <div>
                    <strong style="font-size: 16px; color: #38bdf8;">365-Day 24x7 Annual Timeline Scrubber</strong>
                    <div style="font-size: 13px; color: #94a3b8; margin-top: 2px;">Slide across days 1 to 365 to inspect daily traffic surges, seasonal weather, and cyber events</div>
                </div>
                <div id="day-badge" style="background:#38bdf8; color:#0b1120; font-weight:800; padding:6px 16px; border-radius:8px; font-size:14px;">
                    Day 1 (Winter Normal)
                </div>
            </div>
            <div class="slider-wrap">
                <span style="font-size:12px; color:#94a3b8;">Day 1</span>
                <input type="range" min="1" max="365" value="1" class="slider" id="dayRange" oninput="updateDay(this.value)">
                <span style="font-size:12px; color:#94a3b8;">Day 365</span>
            </div>
            <div style="display:grid; grid-template-columns:repeat(5, 1fr); gap:12px; margin-top:16px;" id="day-details">
                <!-- Injected via JS -->
            </div>
        </div>

        <!-- GIS MAP & RSU INFRASTRUCTURE -->
        <div class="grid-main">
            <div class="chart-box">
                <div class="chart-title">&Mapi; M-1 Motorway GIS Corridor (10 Interchanges & 87 Physical RSUs)</div>
                <div id="map-view"></div>
            </div>
            <div class="chart-box">
                <div class="chart-title">&#9889; C-V2X Edge Computing & EV Service Hubs</div>
                <div style="font-size:13px; line-height:1.6;">
                    <div style="background:rgba(255,255,255,0.03); padding:10px; border-radius:8px; margin-bottom:10px;">
                        <strong style="color:#38bdf8;">87 Physical RSU Gantries (Every 1.8 km):</strong>
                        <div>&bull; NVIDIA Jetson AGX Orin Edge Servers (275 TOPS)</div>
                        <div>&bull; 10 Gbps Redundant Underground Fiber Backbone</div>
                        <div>&bull; 5 kW Solar PV + 15 kWh Battery (72h Off-Grid Uptime)</div>
                    </div>
                    <div style="background:rgba(255,255,255,0.03); padding:10px; border-radius:8px;">
                        <strong style="color:#10b981;">EV Fast Charging Service Hubs:</strong>
                        <div>&bull; <strong>Rashakai SEZ (KM 45):</strong> 16x 350kW Chargers (10.4 MW)</div>
                        <div>&bull; <strong>Indus River / Ghazi (KM 116):</strong> 20x 350kW Chargers (13.0 MW)</div>
                        <div>&bull; <strong>Annual Grid Energy Saved:</strong> 34,280 MWh</div>
                    </div>
                </div>
            </div>
        </div>

        <!-- MIXED AUTONOMY (MPR) & EV SOC SECTION -->
        <div class="section-header">
            <div>
                <div class="section-title">&#128663; Mixed-Autonomy Market Penetration (MPR 0%-100%) & EV Battery Dynamics</div>
                <div class="section-subtitle">Highway lane capacity expansion and EV battery SOC drawdown along 155 km elevation profile</div>
            </div>
            <span class="badge-tag badge-purple">TRANSITION DYNAMICS</span>
        </div>

        <div class="grid-main" style="grid-template-columns: 1fr 1fr; margin-bottom: 24px;">
            <div class="chart-box">
                <div class="chart-title">&#9632; Highway Capacity Expansion vs CAV Market Penetration (MPR %)</div>
                <canvas id="mprChart" height="220"></canvas>
            </div>
            <div class="chart-box">
                <div class="chart-title">&#9889; EV Battery SOC (%) along 155 km Peshawar &rarr; Islamabad Corridor</div>
                <canvas id="evSocChart" height="220"></canvas>
            </div>
        </div>

        <!-- HETEROGENEOUS VEHICLE FLEET -->
        <div class="section-header">
            <div>
                <div class="section-title">&#128663; Multi-Class Heterogeneous Vehicle Fleet Taxonomy (Cars, Buses, Trucks, Trailers)</div>
                <div class="section-subtitle">Class-specific mass, aerodynamics, braking dynamics, and diurnal freight vs passenger composition on M-1</div>
            </div>
            <span class="badge-tag badge-blue">MULTI-CLASS FLEET</span>
        </div>

        <div class="grid-main" style="grid-template-columns: 1fr 1fr; margin-bottom: 24px;">
            <div class="chart-box">
                <div class="chart-title">&#9678; M-1 Traffic Share by Vehicle Class (%)</div>
                <canvas id="fleetShareChart" height="220"></canvas>
            </div>
            <div class="chart-box">
                <div class="chart-title">&#9851; Annual CO2 Emission Savings by Class (Metric Tons)</div>
                <canvas id="fleetCo2Chart" height="220"></canvas>
            </div>
        </div>

        <!-- MULTI-ALGORITHM BENCHMARK -->
        <div class="section-header">
            <div>
                <div class="section-title">&#9874; Multi-Algorithm Empirical Benchmark (6 Detectors & 6 Controllers)</div>
                <div class="section-subtitle">Comparative evaluation across 38.9M vehicle trips and 614k attack vectors on M-1</div>
            </div>
            <span class="badge-tag badge-green">EMPIRICAL BENCHMARK</span>
        </div>

        <div class="grid-main" style="grid-template-columns: 1fr 1fr; margin-bottom: 32px;">
            <div class="chart-box">
                <div class="chart-title">&#9632; Security Verification Models: Accuracy vs F1-Score (%)</div>
                <canvas id="detChart" height="220"></canvas>
            </div>
            <div class="chart-box">
                <div class="chart-title">&#9632; Platoon Controllers: Spacing Tracking Errors (MAE vs RMSE in meters)</div>
                <canvas id="ctrlErrorChart" height="220"></canvas>
            </div>
        </div>

    </div>

    <script>
        const dailyData = {json.dumps(daily)};
        const monthsLabels = {json.dumps(months_labels)};
        const monthlyTrips = {json.dumps(monthly_trips)};
        const monthlyAttacks = {json.dumps(monthly_attacks)};
        const monthlyDetected = {json.dumps(monthly_detected)};
        const monthlyFailovers = {json.dumps(monthly_failovers)};
        const monthlyCo2 = {json.dumps(monthly_co2)};

        // Fleet Data
        const fleetLabels = {json.dumps(fleet_labels)};
        const fleetShares = {json.dumps(fleet_shares)};
        const fleetCo2Data = {json.dumps(fleet_co2)};

        // MPR Data
        const mprPcts = {json.dumps(mpr_pcts)};
        const mprCaps = {json.dumps(mpr_caps)};
        const mprCo2s = {json.dumps(mpr_co2s)};

        // EV Data
        const evKm = {json.dumps(ev_dynamics['km_distance_axis'])};
        const evSocAlone = {json.dumps(ev_dynamics['ev_soc_standalone_pct'])};
        const evSocPlatoon = {json.dumps(ev_dynamics['ev_soc_zt_cacc_platooned_pct'])};

        // Benchmark data
        const detNames = {json.dumps(det_names)};
        const detAcc = {json.dumps(det_acc)};
        const detF1 = {json.dumps(det_f1)};
        const ctrlNames = {json.dumps(ctrl_names)};
        const ctrlMae = {json.dumps(ctrl_mae)};
        const ctrlRmse = {json.dumps(ctrl_rmse)};

        // Leaflet Map Initialization
        const map = L.map('map-view').setView([33.85, 72.35], 9);
        L.tileLayer('https://{{s}}.basemaps.cartocdn.com/dark_all/{{z}}/{{x}}/{{y}}{{r}}.png', {{
            attribution: '&copy; OpenStreetMap contributors &copy; CARTO',
            maxZoom: 18
        }}).addTo(map);

        const interchanges = [
            {{ name: "Peshawar Toll Plaza", km: 0.0, lat: 34.053, lon: 71.693, desc: "Northern Bypass / CPEC Gateway" }},
            {{ name: "Charsadda Interchange", km: 15.2, lat: 34.120, lon: 71.745, desc: "Charsadda - Nowshera Link" }},
            {{ name: "Rashakai / Risalpur", km: 45.1, lat: 34.086, lon: 71.979, desc: "CPEC SEZ / Mardan Junction" }},
            {{ name: "Karnal Sher Khan", km: 62.4, lat: 34.072, lon: 72.138, desc: "Swabi / CPEC Western Route" }},
            {{ name: "Swabi Interchange", km: 88.0, lat: 34.041, lon: 72.412, desc: "Winter Fog Hotspot" }},
            {{ name: "Chach Interchange", km: 105.3, lat: 33.952, lon: 72.541, desc: "Attock District Link" }},
            {{ name: "Ghazi / Indus River Bridge", km: 115.8, lat: 33.910, lon: 72.628, desc: "Indus Crossing & Fog Zone" }},
            {{ name: "Burhan Interchange", km: 128.5, lat: 33.821, lon: 72.715, desc: "M-15 Hazara Motorway Junction" }},
            {{ name: "Brahma Bahtar Interchange", km: 142.1, lat: 33.722, lon: 72.801, desc: "Taxila Industrial Area" }},
            {{ name: "Islamabad Toll Plaza", km: 155.0, lat: 33.628, lon: 72.894, desc: "M-1 / M-2 / CPEC South Link" }}
        ];

        const latlngs = interchanges.map(ic => [ic.lat, ic.lon]);
        L.polyline(latlngs, {{ color: '#38bdf8', weight: 4, opacity: 0.8 }}).addTo(map);

        interchanges.forEach(ic => {{
            const marker = L.circleMarker([ic.lat, ic.lon], {{
                radius: 6, fillColor: '#10b981', color: '#fff', weight: 2, fillOpacity: 0.9
            }}).addTo(map);
            marker.bindPopup(`<strong>${{ic.name}}</strong><br>Corridor: KM ${{ic.km.toFixed(1)}}<br><em>${{ic.desc}}</em>`);
        }});

        // MPR Capacity Chart
        new Chart(document.getElementById('mprChart'), {{
            type: 'line',
            data: {{
                labels: mprPcts.map(p => p + '%'),
                datasets: [
                    {{ label: 'Highway Lane Capacity (veh/hr/lane)', data: mprCaps, borderColor: '#38bdf8', backgroundColor: 'rgba(56, 189, 248, 0.2)', fill: true, tension: 0.3 }}
                ]
            }},
            options: {{
                responsive: true,
                scales: {{
                    x: {{ ticks: {{ color: '#94a3b8' }}, grid: {{ color: 'rgba(255,255,255,0.05)' }} }},
                    y: {{ ticks: {{ color: '#94a3b8' }}, grid: {{ color: 'rgba(255,255,255,0.05)' }} }}
                }},
                plugins: {{ legend: {{ labels: {{ color: '#f8fafc' }} }} }}
            }}
        }});

        // EV SOC Chart
        new Chart(document.getElementById('evSocChart'), {{
            type: 'line',
            data: {{
                labels: evKm.map(k => k + ' km'),
                datasets: [
                    {{ label: 'Standalone EV SOC (%)', data: evSocAlone, borderColor: '#ef4444', borderDash: [5, 5], tension: 0.2 }},
                    {{ label: 'ZT-CACC Platooned EV SOC (%)', data: evSocPlatoon, borderColor: '#10b981', backgroundColor: 'rgba(16, 185, 129, 0.15)', fill: true, tension: 0.2 }}
                ]
            }},
            options: {{
                responsive: true,
                scales: {{
                    x: {{ ticks: {{ color: '#94a3b8', font: {{ size: 9 }} }}, grid: {{ color: 'rgba(255,255,255,0.05)' }} }},
                    y: {{ min: 50, max: 100, ticks: {{ color: '#94a3b8' }}, grid: {{ color: 'rgba(255,255,255,0.05)' }} }}
                }},
                plugins: {{ legend: {{ labels: {{ color: '#f8fafc' }} }} }}
            }}
        }});

        // Fleet Share Doughnut Chart
        new Chart(document.getElementById('fleetShareChart'), {{
            type: 'doughnut',
            data: {{
                labels: fleetLabels,
                datasets: [{{
                    data: fleetShares,
                    backgroundColor: ['#38bdf8', '#a855f7', '#f59e0b', '#ef4444'],
                    borderWidth: 0
                }}]
            }},
            options: {{
                responsive: true,
                plugins: {{ legend: {{ labels: {{ color: '#f8fafc', font: {{ size: 11 }} }} }} }}
            }}
        }});

        // Fleet CO2 Saved Bar Chart
        new Chart(document.getElementById('fleetCo2Chart'), {{
            type: 'bar',
            data: {{
                labels: fleetLabels,
                datasets: [{{
                    label: 'CO2 Saved (Metric Tons)',
                    data: fleetCo2Data,
                    backgroundColor: ['#38bdf8', '#a855f7', '#f59e0b', '#ef4444'],
                    borderRadius: 6
                }}]
            }},
            options: {{
                responsive: true,
                scales: {{
                    x: {{ ticks: {{ color: '#94a3b8', font: {{ size: 10 }} }}, grid: {{ color: 'rgba(255,255,255,0.05)' }} }},
                    y: {{ ticks: {{ color: '#94a3b8' }}, grid: {{ color: 'rgba(255,255,255,0.05)' }} }}
                }},
                plugins: {{ legend: {{ display: false }} }}
            }}
        }});

        // Multi-Algorithm Detection Accuracy vs F1
        new Chart(document.getElementById('detChart'), {{
            type: 'bar',
            data: {{
                labels: detNames,
                datasets: [
                    {{ label: 'Accuracy (%)', data: detAcc, backgroundColor: '#38bdf8', borderRadius: 4 }},
                    {{ label: 'F1-Score (%)', data: detF1, backgroundColor: '#10b981', borderRadius: 4 }}
                ]
            }},
            options: {{
                responsive: true,
                scales: {{
                    x: {{ ticks: {{ color: '#94a3b8', font: {{ size: 10 }} }}, grid: {{ color: 'rgba(255,255,255,0.05)' }} }},
                    y: {{ min: 50, max: 100, ticks: {{ color: '#94a3b8' }}, grid: {{ color: 'rgba(255,255,255,0.05)' }} }}
                }},
                plugins: {{ legend: {{ labels: {{ color: '#f8fafc' }} }} }}
            }}
        }});

        // Controller MAE vs RMSE Error
        new Chart(document.getElementById('ctrlErrorChart'), {{
            type: 'bar',
            data: {{
                labels: ctrlNames,
                datasets: [
                    {{ label: 'Mean Absolute Error (MAE - m)', data: ctrlMae, backgroundColor: '#38bdf8', borderRadius: 4 }},
                    {{ label: 'Root Mean Square Error (RMSE - m)', data: ctrlRmse, backgroundColor: '#f59e0b', borderRadius: 4 }}
                ]
            }},
            options: {{
                responsive: true,
                scales: {{
                    x: {{ ticks: {{ color: '#94a3b8', font: {{ size: 10 }} }}, grid: {{ color: 'rgba(255,255,255,0.05)' }} }},
                    y: {{ ticks: {{ color: '#94a3b8' }}, grid: {{ color: 'rgba(255,255,255,0.05)' }} }}
                }},
                plugins: {{ legend: {{ labels: {{ color: '#f8fafc' }} }} }}
            }}
        }});

        function updateDay(dayNum) {{
            const sample = dailyData.find(d => d.day == dayNum) || dailyData[0];
            document.getElementById('day-badge').innerText = `Day ${{sample.day}} (${{sample.date_str || 'Day ' + sample.day}}) - ${{sample.weather}}`;
            
            const html = `
                <div style="background:rgba(255,255,255,0.04); padding:12px; border-radius:8px;">
                    <div style="font-size:11px; color:#94a3b8; text-transform:uppercase;">Daily Vehicles</div>
                    <div style="font-size:18px; font-weight:700; color:#fff;">${{sample.trips.toLocaleString()}}</div>
                </div>
                <div style="background:rgba(255,255,255,0.04); padding:12px; border-radius:8px;">
                    <div style="font-size:11px; color:#94a3b8; text-transform:uppercase;">Attacks Injected</div>
                    <div style="font-size:18px; font-weight:700; color:#ef4444;">${{sample.attacks.toLocaleString()}}</div>
                </div>
                <div style="background:rgba(255,255,255,0.04); padding:12px; border-radius:8px;">
                    <div style="font-size:11px; color:#94a3b8; text-transform:uppercase;">Neutralized (ZT)</div>
                    <div style="font-size:18px; font-weight:700; color:#10b981;">${{sample.detected.toLocaleString()}}</div>
                </div>
                <div style="background:rgba(255,255,255,0.04); padding:12px; border-radius:8px;">
                    <div style="font-size:11px; color:#94a3b8; text-transform:uppercase;">RAT Failovers</div>
                    <div style="font-size:18px; font-weight:700; color:#f59e0b;">${{sample.failovers.toLocaleString()}}</div>
                </div>
                <div style="background:rgba(255,255,255,0.04); padding:12px; border-radius:8px;">
                    <div style="font-size:11px; color:#94a3b8; text-transform:uppercase;">CO2 Saved Today</div>
                    <div style="font-size:18px; font-weight:700; color:#38bdf8;">${{sample.co2_saved_tons.toFixed(1)}} t</div>
                </div>
            `;
            document.getElementById('day-details').innerHTML = html;
        }}

        // Initialize Day 1
        updateDay(1);
    </script>
</body>
</html>
"""

with open(out_html, "w", encoding="utf-8") as f:
    f.write(html)

print(f"[SUCCESS] Master Digital Twin 2.0 Dashboard built at: {out_html}")
