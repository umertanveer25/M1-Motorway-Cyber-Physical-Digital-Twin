import urllib.request
import urllib.parse
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

queries = [
    "digital twin connected autonomous vehicle platooning",
    "digital twin motorway highway traffic CACC",
    "cyber-physical digital twin V2X CACC",
    "Pakistan motorway digital twin M1 CPEC",
    "zero trust digital twin vehicular network"
]

results = {}

for q in queries:
    print(f"[*] Searching OpenAlex for: '{q}'...")
    encoded = urllib.parse.quote(q)
    url = f"https://api.openalex.org/works?search={encoded}&per-page=5&mailto=researcher@example.com"
    req = urllib.request.Request(url, headers={"User-Agent": "AntigravityResearch/1.0 (mailto:researcher@example.com)"})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            works = []
            for item in data.get("results", []):
                works.append({
                    "id": item.get("id"),
                    "doi": item.get("doi"),
                    "title": item.get("title"),
                    "year": item.get("publication_year"),
                    "citations": item.get("cited_by_count"),
                    "authors": [a.get("author", {}).get("display_name") for a in item.get("authorships", [])[:3]],
                    "venue": item.get("primary_location", {}).get("source", {}).get("display_name") if item.get("primary_location") and item.get("primary_location").get("source") else "Unknown Venue",
                    "abstract_inverted_index_len": len(item.get("abstract_inverted_index", {}) or {})
                })
            results[q] = works
            print(f"  -> Found {len(works)} relevant works.")
    except Exception as e:
        print(f"  [!] Error: {e}")

out_path = r"C:\Users\umert\.gemini\antigravity\scratch\m1_digital_twin\results\openalex_search_digital_twin.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)

print(f"[SUCCESS] OpenAlex search results saved to {out_path}")
