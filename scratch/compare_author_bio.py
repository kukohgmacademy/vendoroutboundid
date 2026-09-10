with open('blog/pentingnya-manajemen-risiko-outbound-terbuka.html', 'r', encoding='utf-8') as f:
    ref = f.read()

with open('blog/peran-karakter-soft-skills-kesiapan-kerja.html', 'r', encoding='utf-8') as f:
    art1 = f.read()

import re

print("=== REF AUTHOR BIO ===")
ref_bio = re.search(r'<!-- AUTHOR BIO BOX -->.*?(?=<!-- SHARE BUTTONS -->)', ref, re.DOTALL)
print(ref_bio.group(0) if ref_bio else "NOT FOUND")

print("\n=== ART1 AUTHOR BIO ===")
art1_bio = re.search(r'<!-- AUTHOR BIO BOX -->.*?(?=<!-- SHARE BUTTONS -->)', art1, re.DOTALL)
print(art1_bio.group(0) if art1_bio else "NOT FOUND")
