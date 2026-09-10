with open('blog/pentingnya-manajemen-risiko-outbound-terbuka.html', 'r', encoding='utf-8') as f:
    ref = f.read()

with open('blog/peran-karakter-soft-skills-kesiapan-kerja.html', 'r', encoding='utf-8') as f:
    art1 = f.read()

import re

def get_style(html):
    m = re.search(r'<style>(.*?)</style>', html, re.DOTALL)
    return m.group(1) if m else ''

def get_scripts(html):
    return re.findall(r'<script(?![^>]*ld\+json)[^>]*>(.*?)</script>', html, re.DOTALL)

style_ref = get_style(ref)
style_art1 = get_style(art1)

print(f"Style ref length: {len(style_ref)}, art1 length: {len(style_art1)}")
if style_ref == style_art1:
    print("Styles are 100% IDENTICAL!")
else:
    print("Styles DIFFER!")
    import difflib
    diff = list(difflib.unified_diff(style_ref.splitlines(), style_art1.splitlines(), lineterm=''))
    for l in diff[:40]:
        print(l)

scripts_ref = get_scripts(ref)
scripts_art1 = get_scripts(art1)
print(f"\nScripts ref count: {len(scripts_ref)}, art1 count: {len(scripts_art1)}")
for i, (sr, sa) in enumerate(zip(scripts_ref, scripts_art1)):
    if sr.strip() == sa.strip():
        print(f"Script {i} is identical")
    else:
        print(f"Script {i} differs!")
        diff = list(difflib.unified_diff(sr.splitlines(), sa.splitlines(), lineterm=''))
        for l in diff[:30]:
            print(l)
