import json
import os

osm_path = r"C:\Users\umert\.gemini\antigravity\scratch\m1_digital_twin\geo_data\m1_motorway_osm.json"
out_html = r"C:\Users\umert\.gemini\antigravity\scratch\m1_digital_twin\visualization\m1_interactive_map.html"

with open(osm_path, "r", encoding="utf-8") as f:
    data = json.load(f)

elements = data.get("elements", [])
nodes_dict = {e["id"]: (e["lat"], e["lon"]) for e in elements if e.get("type") == "node"}
ways = [e for e in elements if e.get("type") == "way"]

# Official NHA M-1 Interchanges
interchanges = [
    {"name": "Peshawar Toll Plaza / Northern Bypass", "lat": 34.015, "lon": 71.690, "km": 0},
    {"name": "Charsadda Interchange", "lat": 34.085, "lon": 71.775, "km": 15},
    {"name": "Rashakai / Risalpur / Mardan Interchange (CPEC SEZ)", "lat": 34.088, "lon": 72.035, "km": 45},
    {"name": "Karnal Sher Khan Interchange", "lat": 34.060, "lon": 72.180, "km": 62},
    {"name": "Swabi Interchange (Fog Micro-Zone)", "lat": 34.030, "lon": 72.420, "km": 88},
    {"name": "Chach Interchange", "lat": 33.950, "lon": 72.540, "km": 105},
    {"name": "Ghazi / Indus River Bridge Crossing", "lat": 33.900, "lon": 72.620, "km": 115},
    {"name": "Burhan Interchange (M-15 Hazara Link)", "lat": 33.820, "lon": 72.710, "km": 128},
    {"name": "Brahma Bahtar Interchange", "lat": 33.720, "lon": 72.780, "km": 142},
    {"name": "Islamabad Toll Plaza (M-1/M-2 / Fateh Jang)", "lat": 33.625, "lon": 72.845, "km": 155}
]

# Extract way polyline coordinates
way_polylines = []
for w in ways:
    pts = []
    for nid in w.get("nodes", []):
        if nid in nodes_dict:
            pts.append(nodes_dict[nid])
    if len(pts) > 1:
        way_polylines.append(pts)

html_content = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <title>M-1 Motorway (Peshawar to Islamabad) Digital Twin</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <style>
        body, html {{ margin: 0; padding: 0; height: 100%; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }}
        #map {{ height: 100vh; width: 100%; }}
        .hud-panel {{
            position: absolute; top: 15px; right: 15px; z-index: 1000;
            background: rgba(15, 23, 42, 0.92); color: #f8fafc;
            padding: 16px 20px; border-radius: 12px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.5); backdrop-filter: blur(8px);
            max-width: 340px; border: 1px solid rgba(255,255,255,0.1);
        }}
        .hud-title {{ font-size: 16px; font-weight: 700; color: #38bdf8; margin-bottom: 6px; }}
        .hud-badge {{ display: inline-block; background: #0284c7; color: white; padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: 600; }}
        .hud-stat {{ display: flex; justify-content: space-between; margin: 6px 0; font-size: 13px; }}
        .hud-stat-val {{ font-weight: 600; color: #4ade80; }}
    </style>
</head>
<body>
    <div id="map"></div>
    <div class="hud-panel">
        <div class="hud-title">M-1 Motorway Digital Twin</div>
        <div style="margin-bottom: 10px;">
            <span class="hud-badge">ZT-CACC Active</span>
            <span class="hud-badge" style="background:#10b981;">155 km Corridor</span>
        </div>
        <div class="hud-stat"><span>Start:</span><span class="hud-stat-val">Peshawar (KM 0)</span></div>
        <div class="hud-stat"><span>End:</span><span class="hud-stat-val">Islamabad (KM 155)</span></div>
        <div class="hud-stat"><span>OSM Road Segments:</span><span class="hud-stat-val">{len(way_polylines)} ways</span></div>
        <div class="hud-stat"><span>Coordinate Nodes:</span><span class="hud-stat-val">{len(nodes_dict)} points</span></div>
        <div class="hud-stat"><span>Interchanges:</span><span class="hud-stat-val">11 Toll/Ramps</span></div>
        <div class="hud-stat"><span>Security Policy:</span><span class="hud-stat-val">Zero-Trust Multi-RAT</span></div>
    </div>
    <script>
        var map = L.map('map').setView([33.85, 72.25], 9);
        L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {{
            maxZoom: 18,
            attribution: '© OpenStreetMap contributors | M-1 Digital Twin'
        }}).addTo(map);

        var polylines = {json.dumps(way_polylines)};
        polylines.forEach(function(pts) {{
            L.polyline(pts, {{ color: '#0284c7', weight: 4, opacity: 0.85 }}).addTo(map);
        }});

        var interchanges = {json.dumps(interchanges)};
        interchanges.forEach(function(ic) {{
            var marker = L.circleMarker([ic.lat, ic.lon], {{
                radius: 6,
                fillColor: '#ef4444',
                color: '#ffffff',
                weight: 2,
                opacity: 1,
                fillOpacity: 0.9
            }}).addTo(map);
            marker.bindPopup('<b>' + ic.name + '</b><br>Corridor KM: ' + ic.km + '<br>ZT-CACC RSU: Active');
        }});
    </script>
</body>
</html>
"""

os.makedirs(os.path.dirname(out_html), exist_ok=True)
with open(out_html, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"[SUCCESS] Generated interactive Digital Twin map at: {out_html}")
