import urllib.request
import urllib.parse
import json
import os
import sys

# Overpass API query for M-1 motorway (Peshawar to Islamabad)
# Bounding box covers Khyber Pakhtunkhwa & Punjab corridor
query = """
[out:json][timeout:90];
(
  relation["ref"="M-1"](33.5,71.5,34.2,73.0);
  way["ref"="M-1"](33.5,71.5,34.2,73.0);
  way["highway"~"motorway|motorway_link"](33.5,71.5,34.2,73.0);
);
out body;
>;
out skel qt;
"""

url = "https://overpass-api.de/api/interpreter"
data = urllib.parse.urlencode({'data': query}).encode('utf-8')

print("Connecting to OpenStreetMap Overpass API for M-1 Motorway...")

req = urllib.request.Request(
    url, 
    data=data, 
    headers={'User-Agent': 'M1-DigitalTwin-Simulation/1.0 (academic research)'}
)

out_dir = r"C:\Users\umert\.gemini\antigravity\scratch\m1_digital_twin\geo_data"
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, "m1_motorway_osm.json")

try:
    with urllib.request.urlopen(req, timeout=120) as response:
        content = response.read()
        with open(out_path, "wb") as f:
            f.write(content)
        parsed = json.loads(content.decode('utf-8'))
        elements = parsed.get("elements", [])
        nodes = [e for e in elements if e.get("type") == "node"]
        ways = [e for e in elements if e.get("type") == "way"]
        print(f"[SUCCESS] Downloaded M-1 Motorway OSM Data!")
        print(f"  - Total Elements: {len(elements)}")
        print(f"  - Highway Ways / Road Segments: {len(ways)}")
        print(f"  - Coordinate Nodes (Lat/Lon): {len(nodes)}")
        print(f"  - Saved File: {out_path} ({len(content)//1024} KB)")
except Exception as e:
    print(f"[ERROR] Failed to fetch from Overpass: {e}")
    sys.exit(1)
