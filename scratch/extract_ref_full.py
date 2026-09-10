with open('blog/pentingnya-manajemen-risiko-outbound-terbuka.html', 'r', encoding='utf-8') as f:
    ref = f.read()

import re

print("=== ALL BACA JUGA IN REF ===")
for i, m in enumerate(re.finditer(r'<div class="baca-juga-box">.*?</div>\s*</div>', ref, re.DOTALL)):
    print(f"--- BACA JUGA {i+1} ---")
    print(m.group(0))

print("\n=== COMPLETE FAQ IN REF ===")
faq_m = re.search(r'<!-- FAQ SECTION -->.*?(?=<!-- AUTHOR BIO|<!-- CTA BAND|<div class="author-box"|<div class="author-bio-card")', ref, re.DOTALL)
if faq_m:
    print(faq_m.group(0))
else:
    print("FAQ match not found with regex, finding by id...")
    pos = ref.find('id="faq-section"')
    print(ref[pos-50:pos+3000])

print("\n=== FAQ JS IN REF ===")
js_faq = re.search(r'//\s*FAQ.*?Accordion.*?(?=\n\s*//|\n\s*</script>)', ref, re.DOTALL | re.IGNORECASE)
if js_faq:
    print(js_faq.group(0))
else:
    print("FAQ JS search general:")
    for s in re.findall(r'<script(?![^>]*ld\+json)[^>]*>(.*?)</script>', ref, re.DOTALL):
        if 'faq' in s.lower():
            print(s)
