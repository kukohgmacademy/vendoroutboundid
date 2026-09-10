with open('blog/pentingnya-manajemen-risiko-outbound-terbuka.html', 'r', encoding='utf-8') as f:
    ref = f.read()

with open('blog/peran-karakter-soft-skills-kesiapan-kerja.html', 'r', encoding='utf-8') as f:
    art1 = f.read()

import re, json

print("=== REF SCHEMAS ===")
schemas_ref = re.findall(r'<script type="application/ld\+json">(.*?)</script>', ref, re.DOTALL)
print("Count in ref:", len(schemas_ref))
for i, s in enumerate(schemas_ref):
    data = json.loads(s.strip())
    if '@graph' in data:
        print(f"Ref Schema {i+1} has @graph with types: {[item.get('@type') for item in data['@graph']]}")
    else:
        print(f"Ref Schema {i+1} has type: {data.get('@type')}")

print("\n=== ART1 SCHEMAS ===")
schemas_art1 = re.findall(r'<script type="application/ld\+json">(.*?)</script>', art1, re.DOTALL)
print("Count in art1:", len(schemas_art1))
for i, s in enumerate(schemas_art1):
    data = json.loads(s.strip())
    if '@graph' in data:
        print(f"Art1 Schema {i+1} has @graph with types: {[item.get('@type') for item in data['@graph']]}")
    else:
        print(f"Art1 Schema {i+1} has type: {data.get('@type')}")
