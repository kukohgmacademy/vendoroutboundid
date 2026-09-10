import re

articles = [
    r"blog\peran-karakter-soft-skills-kesiapan-kerja.html",
    r"blog\manfaat-outbound-vs-seminar-motivasi-siswa.html",
    r"blog\jasa-fasilitator-outbound-edukasi-sekolah-kampus.html"
]

for art in articles:
    with open(art, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check tag balance
    for tag in ['header', 'nav', 'ul', 'ol', 'div', 'body', 'html', 'article', 'section', 'aside', 'footer']:
        opens = len(re.findall(f'<{tag}[\\s>]', content, re.I))
        closes = len(re.findall(f'</{tag}>', content, re.I))
        assert opens == closes, f'{art} has unbalanced {tag}: opens={opens}, closes={closes}'

    # Check baca-juga-box count
    bj_count = len(re.findall(r'class="baca-juga-box"', content))
    assert bj_count == 3, f'{art} has {bj_count} baca-juga-box (expected 3)'
    
    # Check faq-item count
    faq_count = len(re.findall(r'class="faq-item"', content))
    assert faq_count >= 5, f'{art} has {faq_count} faq-item (expected >= 5)'
    
    # Check word count
    art_match = re.search(r'<article class="article-main">(.*?)</article>', content, re.DOTALL)
    body = art_match.group(1) if art_match else content
    body = re.sub(r'<script.*?</script>', '', body, flags=re.DOTALL)
    body = re.sub(r'<style.*?</style>', '', body, flags=re.DOTALL)
    body = re.sub(r'<svg.*?</svg>', '', body, flags=re.DOTALL)
    body = re.sub(r'<!--.*?-->', '', body, flags=re.DOTALL)
    text = re.sub(r'<[^>]+>', ' ', body)
    words = len(text.split())
    assert words >= 1300, f'{art} has only {words} words!'

    print(f"OK: {art} | Words: {words} | Baca Juga: {bj_count} | FAQ: {faq_count} | Balance: 100%")

print("\nAll 3 articles are 100% verified and aligned with reference!")
