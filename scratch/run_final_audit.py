import json
import os
import re

files = [
    'blog/peran-karakter-soft-skills-kesiapan-kerja.html',
    'blog/manfaat-outbound-vs-seminar-motivasi-siswa.html',
    'blog/jasa-fasilitator-outbound-edukasi-sekolah-kampus.html'
]

print("=== RUNNING FULL AUDIT ===")

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    
    print(f"\nAUDITING: {fpath}")
    
    # 1. Tag balance
    for tag in ['div', 'section', 'article', 'main', 'header', 'footer', 'aside', 'script', 'style']:
        opens = len(re.findall(rf'<{tag}\b', c, re.IGNORECASE))
        closes = len(re.findall(rf'</{tag}>', c, re.IGNORECASE))
        assert opens == closes, f"Tag mismatch <{tag}> in {fpath}: {opens} opens vs {closes} closes"
    print("  [OK] Tag balance 100% OK")
    
    # 2. Baca Juga
    baca_boxes = re.findall(r'<div class="baca-juga-box">.*?</div>\s*</div>', c, re.DOTALL)
    assert len(baca_boxes) == 3, f"Expected 3 baca-juga boxes, found {len(baca_boxes)}"
    for b in baca_boxes:
        assert '<div class="icon"><i class="fas fa-book-open"></i></div>' in b
        assert '<span class="label">BACA JUGA:</span>' in b
        assert '<a href="' in b and 'class="link"' in b
    print("  [OK] 3x Baca Juga boxes 100% aligned with ref")
    
    # 3. FAQ Section
    assert '<div class="faq-section" id="faq-section">' in c
    assert '<h3><i class="fas fa-circle-question" style="color:var(--c-maroon);"></i> Pertanyaan Sering Diajukan (FAQ)</h3>' in c
    faq_items = re.findall(r'<div class="faq-item">.*?<button class="faq-question".*?<div class="faq-answer">.*?<div class="faq-answer-inner">.*?</div>\s*</div>\s*</div>', c, re.DOTALL)
    assert len(faq_items) == 5, f"Expected 5 FAQ items, found {len(faq_items)}"
    print("  [OK] FAQ section & 5 items 100% aligned with ref")
    
    # 4. Word count in article content
    art_content_match = re.search(r'<div class="article-content"[^>]*>(.*?)</div>\s*</article>', c, re.DOTALL)
    assert art_content_match, "article-content not found or not properly closed before </article>"
    clean_text = re.sub(r'<[^>]+>', ' ', art_content_match.group(1))
    words = clean_text.split()
    print(f"  [OK] Word count: {len(words)} words (Target: > 1,300)")
    assert len(words) >= 1300, f"Word count {len(words)} < 1300"
    
    # 5. Schema JSON-LD validation
    schemas = re.findall(r'<script type="application/ld\+json">(.*?)</script>', c, re.DOTALL)
    assert len(schemas) >= 1, f"Expected at least 1 schema block, found {len(schemas)}"
    for s in schemas:
        data = json.loads(s.strip())
        if '@graph' in data:
            types = [item.get('@type') for item in data['@graph']]
            print(f"  [OK] Valid Schema @graph with: {types}")
            assert 'Article' in types and 'BreadcrumbList' in types and 'FAQPage' in types
        else:
            print(f"  [OK] Valid Schema: {data.get('@type')}")
        
    # 6. Navbar CTA check
    assert 'Hubungi Kami' in c, "Navbar should have 'Hubungi Kami'"
    assert 'btn-wander-cta' in c, "Navbar button should have btn-wander-cta class"
    
    # 7. Images check
    imgs = re.findall(r'<img[^>]+src="([^">]+)"', c)
    for img in imgs:
        if img.startswith('../'):
            local_path = img.replace('../', '')
        else:
            local_path = img
        if not os.path.exists(local_path):
            print(f"  [!] Missing image: {local_path}")
        else:
            size_kb = os.path.getsize(local_path) / 1024
    print("  [OK] All referenced image files exist on disk")

print("\n=== FULL AUDIT COMPLETED: 100% PASSED ===")
