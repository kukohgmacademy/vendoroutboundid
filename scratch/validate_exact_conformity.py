import re, json

articles = [
    r"blog\peran-karakter-soft-skills-kesiapan-kerja.html",
    r"blog\manfaat-outbound-vs-seminar-motivasi-siswa.html",
    r"blog\jasa-fasilitator-outbound-edukasi-sekolah-kampus.html"
]

ref = open(r"blog\pentingnya-manajemen-risiko-outbound-terbuka.html", "r", encoding="utf-8").read()

for art in articles:
    content = open(art, "r", encoding="utf-8").read()
    
    # Check word count
    art_match = re.search(r'<article class="article-main">(.*?)</article>', content, re.DOTALL)
    body = art_match.group(1) if art_match else content
    body = re.sub(r'<script.*?</script>', '', body, flags=re.DOTALL)
    body = re.sub(r'<style.*?</style>', '', body, flags=re.DOTALL)
    body = re.sub(r'<svg.*?</svg>', '', body, flags=re.DOTALL)
    body = re.sub(r'<!--.*?-->', '', body, flags=re.DOTALL)
    text = re.sub(r'<[^>]+>', ' ', body)
    words = len(text.split())
    
    # Check JSON-LD
    schemas = re.findall(r'<script type="application/ld\+json">(.*?)</script>', content, re.DOTALL)
    for s in schemas:
        json.loads(s.strip())
        
    # Check tag balance
    tag_errors = []
    for tag in ['header', 'nav', 'ul', 'ol', 'div', 'body', 'html', 'article', 'section', 'aside', 'footer']:
        opens = len(re.findall(f'<{tag}[\\s>]', content, re.I))
        closes = len(re.findall(f'</{tag}>', content, re.I))
        if opens != closes:
            tag_errors.append((tag, opens, closes))
            
    # Check key components from reference
    has_sidebar = '<aside class="article-sidebar">' in content
    has_related_sec = '<section class="related-products-section">' in content
    has_wa_float = 'class="wa-float"' in content
    has_js = 'document.getElementById(\'tocToggle\')' in content
    has_author_avatar = 'author-artikel-arby-ardiansyah.webp' in content
    
    print(f"\nValidated: {art}")
    print(f"  - Word Count: {words} words (Pass: {words >= 1300})")
    print(f"  - Tag Balance: {'OK' if not tag_errors else tag_errors}")
    print(f"  - Has Sidebar: {has_sidebar}")
    print(f"  - Has Related Products Section: {has_related_sec}")
    print(f"  - Has Floating WA: {has_wa_float}")
    print(f"  - Has Interactive JS Functions: {has_js}")
    print(f"  - Has Verified Author Avatar: {has_author_avatar}")
