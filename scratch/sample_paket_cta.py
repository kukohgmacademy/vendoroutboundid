import glob, re

for f in sorted(glob.glob('paket/*.html')):
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    
    m = re.search(r'(<div[^>]*class=[\'"]cta-band-luxury[\'"][^>]*>.*?</div>\s*</div>)', c, re.DOTALL)
    if m:
        print(f"=== {f} ===")
        print(m.group(1)[:300])
    else:
        print(f"=== {f} NOT FOUND ===")
