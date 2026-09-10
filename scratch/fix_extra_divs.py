import re

files = [
    'blog/peran-karakter-soft-skills-kesiapan-kerja.html',
    'blog/manfaat-outbound-vs-seminar-motivasi-siswa.html',
    'blog/jasa-fasilitator-outbound-edukasi-sekolah-kampus.html'
]

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    
    # Remove the extra </div> after cta-band
    c_fixed = re.sub(r'(<div class="cta-band">.*?</div>)\s*</div>\s*(<!-- CONCLUSION BOX -->|<div class="conclusion-box">)', r'\1\n\n            \2', c, flags=re.DOTALL)
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c_fixed)
    print(f"Fixed {fpath}")
