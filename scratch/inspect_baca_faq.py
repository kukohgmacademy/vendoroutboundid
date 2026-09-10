import re

with open('blog/pentingnya-manajemen-risiko-outbound-terbuka.html', 'r', encoding='utf-8') as f:
    ref = f.read()

with open('blog/peran-karakter-soft-skills-kesiapan-kerja.html', 'r', encoding='utf-8') as f:
    art1 = f.read()

print("=== REF CSS FOR BACA JUGA AND FAQ ===")
for match in re.finditer(r'/\*.*?(?:baca-juga|faq).*?\*/.*?(?=\n\s*/\*|\n\s*</style>)', ref, re.DOTALL | re.IGNORECASE):
    print(match.group(0)[:500])
    print("-" * 40)

print("\n=== REF BACA JUGA SAMPLE ===")
baca_ref = re.findall(r'<div class="baca-juga-box".*?</div>\s*</div>', ref, re.DOTALL)
for b in baca_ref[:2]:
    print(b)
    print("." * 30)

print("\n=== ART1 BACA JUGA SAMPLE ===")
baca_art1 = re.findall(r'<div class="baca-juga-box".*?</div>\s*</div>', art1, re.DOTALL)
for b in baca_art1[:2]:
    print(b)
    print("." * 30)

print("\n=== REF FAQ SNIPPET ===")
faq_ref_pos = ref.find('class="faq-section"')
if faq_ref_pos != -1:
    print(ref[faq_ref_pos-50:faq_ref_pos+800])

print("\n=== ART1 FAQ SNIPPET ===")
faq_art1_pos = art1.find('class="faq-section"')
if faq_art1_pos != -1:
    print(art1[faq_art1_pos-50:faq_art1_pos+800])
