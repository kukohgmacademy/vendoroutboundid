import re

articles = [
    r"blog\peran-karakter-soft-skills-kesiapan-kerja.html",
    r"blog\manfaat-outbound-vs-seminar-motivasi-siswa.html",
    r"blog\jasa-fasilitator-outbound-edukasi-sekolah-kampus.html"
]

for art in articles:
    content = open(art, "r", encoding="utf-8").read()
    opens = len(re.findall(r'<div[\s>]', content))
    closes = len(re.findall(r'</div>', content))
    print(f"{art}: div opens={opens}, closes={closes}")
    
    # Check around CTA band and FAQ
    match = re.search(r'(<!-- PROMO WA CTA BAND -->.*?<!-- AUTHOR BIO BOX -->)', content, re.DOTALL)
    if match:
        block = match.group(1)
        b_opens = len(re.findall(r'<div[\s>]', block))
        b_closes = len(re.findall(r'</div>', block))
        print(f"  CTA+FAQ block: opens={b_opens}, closes={b_closes}")
