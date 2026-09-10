import re

with open('blog/pentingnya-manajemen-risiko-outbound-terbuka.html', 'r', encoding='utf-8') as f:
    ref = f.read()

ref_script = re.search(r'<script>(.*?)</script>', ref, re.DOTALL).group(0)

files = [
    'blog/peran-karakter-soft-skills-kesiapan-kerja.html',
    'blog/manfaat-outbound-vs-seminar-motivasi-siswa.html',
    'blog/jasa-fasilitator-outbound-edukasi-sekolah-kampus.html'
]

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    c = re.sub(r'<script>(.*?)</script>', ref_script, c, flags=re.DOTALL)
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)

print("Standardized scripts across all 3 files.")
