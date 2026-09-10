import re

articles = [
    r"blog\peran-karakter-soft-skills-kesiapan-kerja.html",
    r"blog\manfaat-outbound-vs-seminar-motivasi-siswa.html",
    r"blog\jasa-fasilitator-outbound-edukasi-sekolah-kampus.html"
]

for art in articles:
    with open(art, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Extract only main content inside <article class="article-main-content"> ... </article>
    art_match = re.search(r'<article class="article-main-content">(.*?)</article>', content, re.DOTALL)
    if not art_match:
        print(f"Failed to find article tag in {art}")
        continue
    
    body = art_match.group(1)
    
    # Remove script, style, svg, comments
    body = re.sub(r'<script.*?</script>', '', body, flags=re.DOTALL)
    body = re.sub(r'<style.*?</style>', '', body, flags=re.DOTALL)
    body = re.sub(r'<svg.*?</svg>', '', body, flags=re.DOTALL)
    body = re.sub(r'<!--.*?-->', '', body, flags=re.DOTALL)
    
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', ' ', body)
    
    # Split into words
    words = text.split()
    print(f"File: {art}")
    print(f"  Editorial Word Count: {len(words)} words (Requirement >= 1300)")
    assert len(words) >= 1300, f"Word count {len(words)} is below 1300!"
