import glob
import re

files = [
    'blog/pentingnya-manajemen-risiko-outbound-terbuka.html',
    'blog/pentingnya-melatih-leadership-sekolah.html',
    'blog/dampak-positif-komunikasi-efektif-tim-kerja.html',
    'blog/peran-karakter-soft-skills-kesiapan-kerja.html',
    'blog/manfaat-outbound-vs-seminar-motivasi-siswa.html',
    'blog/jasa-fasilitator-outbound-edukasi-sekolah-kampus.html'
]

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    print(f"=== {fpath} ===")
    baca = re.findall(r'<div class="baca-juga[^"]*">.*?</div>\s*</div>', c, re.DOTALL)
    print("BACA JUGA COUNT:", len(baca))
    if baca:
        print("BACA JUGA[0]:\n", baca[0])
    
    faq = re.search(r'<div class="faq-section".*?</div>\s*</div>\s*</div>', c, re.DOTALL)
    print("FAQ SECTION FOUND:", bool(faq))
    if faq:
        # print first 300 chars
        print("FAQ SECTION START:\n", faq.group(0)[:300])
