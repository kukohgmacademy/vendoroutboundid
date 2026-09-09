import os, glob, re

files = glob.glob('**/*.html', recursive=True)
non_matching = []
for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    match = re.search(r'(<a[^>]*class="[^"]*btn-wander-cta[^"]*"[^>]*>.*?</a>)', content, re.DOTALL)
    if not match:
        match = re.search(r'(<a[^>]*class="[^"]*nav-cta[^"]*"[^>]*>.*?</a>)', content, re.DOTALL)
    if match:
        tag = match.group(1).strip()
        if 'Hubungi Kami' not in tag or 'fa-whatsapp' not in tag:
            non_matching.append((f, tag))
    else:
        non_matching.append((f, 'NO_MATCH'))

print(f"Total HTML files: {len(files)}")
print(f"Total needing update: {len(non_matching)}")
for f, t in non_matching:
    print(f"\n--- {f} ---")
    print(t)
