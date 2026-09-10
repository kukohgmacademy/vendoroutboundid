import os, glob, re, json
import xml.etree.ElementTree as ET

print("=== 1. VALIDATING SITEMAP.XML ===")
try:
    tree = ET.parse("sitemap.xml")
    root = tree.getroot()
    urls = root.findall("{http://www.sitemaps.org/schemas/sitemap/0.9}url")
    print(f"Sitemap XML is 100% valid! Total URL count: {len(urls)}")
except Exception as e:
    print(f"Sitemap XML Error: {e}")

print("\n=== 2. VALIDATING H-10 IMAGES ===")
h10_images = [
    r"assets\image\blog\peran-karakter-soft-skills-kesiapan-kerja-hero.webp",
    r"assets\image\blog\peran-karakter-soft-skills-kesiapan-kerja-support-image-1.webp",
    r"assets\image\blog\manfaat-outbound-vs-seminar-motivasi-siswa-hero.webp",
    r"assets\image\blog\manfaat-outbound-vs-seminar-motivasi-siswa-support-image-1.webp",
    r"assets\image\blog\jasa-fasilitator-outbound-edukasi-sekolah-kampus-hero.webp",
    r"assets\image\blog\jasa-fasilitator-outbound-edukasi-sekolah-kampus-support-image-1.webp"
]
for img in h10_images:
    if not os.path.exists(img):
        print(f"Missing Image: {img}")
    else:
        sz = os.path.getsize(img) / 1024
        print(f"Image OK: {img} | Size: {sz:.2f} KB (<= 150KB: {sz <= 150.0})")

print("\n=== 3. VALIDATING H-10 ARTICLES ===")
articles = [
    r"blog\peran-karakter-soft-skills-kesiapan-kerja.html",
    r"blog\manfaat-outbound-vs-seminar-motivasi-siswa.html",
    r"blog\jasa-fasilitator-outbound-edukasi-sekolah-kampus.html"
]

for art in articles:
    content = open(art, "r", encoding="utf-8").read()
    
    # Check word count
    art_match = re.search(r'<article class="article-main-content">(.*?)</article>', content, re.DOTALL)
    body = art_match.group(1) if art_match else content
    body = re.sub(r'<script.*?</script>', '', body, flags=re.DOTALL)
    body = re.sub(r'<style.*?</style>', '', body, flags=re.DOTALL)
    body = re.sub(r'<svg.*?</svg>', '', body, flags=re.DOTALL)
    body = re.sub(r'<!--.*?-->', '', body, flags=re.DOTALL)
    text = re.sub(r'<[^>]+>', ' ', body)
    words = len(text.split())
    
    # Check JSON-LD
    schemas = re.findall(r'<script type="application/ld\+json">(.*?)</script>', content, re.DOTALL)
    schema_ok = True
    for s in schemas:
        try:
            json.loads(s.strip())
        except Exception as e:
            schema_ok = False
            print(f"Schema error in {art}: {e}")
            
    # Check tags balance
    tag_errors = []
    for tag in ['header', 'nav', 'ul', 'ol', 'div', 'body', 'html', 'article', 'section', 'details']:
        opens = len(re.findall(f'<{tag}[\\s>]', content, re.I))
        closes = len(re.findall(f'</{tag}>', content, re.I))
        if opens != closes:
            tag_errors.append((tag, opens, closes))
            
    # Check navbar WhatsApp icon
    has_wa_icon = 'fab fa-whatsapp' in content
    has_btn_wander = 'btn-wander-cta' in content
    
    print(f"Article: {art}")
    print(f"  - Word Count: {words} words (Pass: {words >= 1300})")
    print(f"  - Schema Valid: {schema_ok} ({len(schemas)} scripts)")
    print(f"  - Tag Balance: {'OK' if not tag_errors else tag_errors}")
    print(f"  - Navbar CTA WhatsApp: {has_wa_icon and has_btn_wander}")

print("\n=== 4. VALIDATING BLOG.HTML ===")
blog_content = open("blog.html", "r", encoding="utf-8").read()
b_errors = []
for tag in ['header', 'nav', 'ul', 'div', 'body', 'html', 'main', 'section']:
    opens = len(re.findall(f'<{tag}[\\s>]', blog_content, re.I))
    closes = len(re.findall(f'</{tag}>', blog_content, re.I))
    if opens != closes:
        b_errors.append((tag, opens, closes))
print(f"blog.html tag balance: {'OK' if not b_errors else b_errors}")
