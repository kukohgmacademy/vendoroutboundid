import re
import difflib

with open('blog/pentingnya-manajemen-risiko-outbound-terbuka.html', 'r', encoding='utf-8') as f:
    ref = f.read()

files = [
    'blog/peran-karakter-soft-skills-kesiapan-kerja.html',
    'blog/manfaat-outbound-vs-seminar-motivasi-siswa.html',
    'blog/jasa-fasilitator-outbound-edukasi-sekolah-kampus.html'
]

script_ref = re.search(r'<script>(.*?)</script>', ref, re.DOTALL).group(1).strip()

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    script_c = re.search(r'<script>(.*?)</script>', c, re.DOTALL).group(1).strip()
    if script_ref == script_c:
        print(f"[EXACT MATCH] Inline script in {fpath}")
    else:
        print(f"[DIFF] Inline script in {fpath}")
        diff = list(difflib.unified_diff(script_ref.splitlines(), script_c.splitlines()))
        for d in diff:
            print("  ", d)
