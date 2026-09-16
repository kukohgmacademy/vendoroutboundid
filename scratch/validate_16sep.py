import os, json, re
from PIL import Image

articles = [
    "blog/meruntuhkan-silo-mental-divisi-perusahaan.html",
    "blog/mengukur-efektivitas-outbound-retensi-karyawan.html",
    "blog/paket-outbound-corporate-synergy-engagement.html"
]

images = [
    "assets/image/blog/meruntuhkan-silo-mental-divisi-perusahaan-hero.webp",
    "assets/image/blog/meruntuhkan-silo-mental-divisi-perusahaan-support-image-1.webp",
    "assets/image/blog/mengukur-efektivitas-outbound-retensi-karyawan-hero.webp",
    "assets/image/blog/mengukur-efektivitas-outbound-retensi-karyawan-support-image-1.webp",
    "assets/image/blog/paket-outbound-corporate-synergy-engagement-hero.webp",
    "assets/image/blog/paket-outbound-corporate-synergy-engagement-support-image-1.webp"
]

print("=== 1. VERIFY IMAGES ===")
for img_path in images:
    if os.path.exists(img_path):
        size_kb = os.path.getsize(img_path) / 1024
        im = Image.open(img_path)
        print(f"[OK] {img_path}: {im.size}, {size_kb:.1f} KB")
    else:
        print(f"[FAIL] {img_path} NOT FOUND")

print("\n=== 2. VERIFY ARTICLES ===")
for art in articles:
    if not os.path.exists(art):
        print(f"[FAIL] {art} NOT FOUND")
        continue
    with open(art, "r", encoding="utf-8") as f:
        html = f.read()

    # Word count
    m = re.search(r'<article class="article-main">(.*?)</article>', html, re.DOTALL)
    if m:
        text = re.sub(r'<[^>]+>', ' ', m.group(1))
        words = len(text.split())
    else:
        words = 0

    # Check JSON-LD
    schemas = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.DOTALL)
    schema_ok = True
    for s in schemas:
        try:
            json.loads(s)
        except Exception as e:
            schema_ok = False
            print(f"  [SCHEMA ERROR] {e}")

    # Check TOC
    has_toc = 'id="tocList"' in html and 'id="tocToggle"' in html
    # Check Answer-First
    has_answer_first = 'class="answer-first-box' in html
    # Check FAQ
    faqs_count = len(re.findall(r'class="faq-item', html))
    # Check Table
    has_table = '<table' in html
    # Check Baca Juga
    baca_juga_count = len(re.findall(r'class="baca-juga-box"', html))
    # Check Internal link
    has_internal_link = '../paket/team-building.html' in html

    print(f"[OK] {art}")
    print(f"     Words: {words} (Min 1,300)")
    print(f"     Schema: {schema_ok}, TOC: {has_toc}, Answer-First: {has_answer_first}")
    print(f"     FAQs: {faqs_count} (Min 5), Table: {has_table}, Baca Juga: {baca_juga_count}, Internal Link: {has_internal_link}")

print("\n=== 3. VERIFY BLOG.HTML & SITEMAP.XML ===")
with open("blog.html", "r", encoding="utf-8") as f:
    b = f.read()
for slug in ["meruntuhkan-silo-mental-divisi-perusahaan", "mengukur-efektivitas-outbound-retensi-karyawan", "paket-outbound-corporate-synergy-engagement"]:
    in_mosaic = slug in b
    print(f"Slug {slug} in blog.html: {in_mosaic}")

with open("sitemap.xml", "r", encoding="utf-8") as f:
    s = f.read()
for slug in ["meruntuhkan-silo-mental-divisi-perusahaan", "mengukur-efektivitas-outbound-retensi-karyawan", "paket-outbound-corporate-synergy-engagement"]:
    in_sitemap = f"https://venroroutbound.id/blog/{slug}.html" in s
    print(f"Slug {slug} in sitemap.xml: {in_sitemap}")
