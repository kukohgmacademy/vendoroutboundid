import re, glob

def check_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # look for cta-band-luxury or similar
    m = re.search(r'(<div[^>]*class="[^"]*cta-[^"]*"[^>]*>.*?</div>\s*</div>)', content, re.DOTALL)
    if not m:
        m = re.search(r'(<section[^>]*class="[^"]*cta[^"]*"[^>]*>.*?</section>)', content, re.DOTALL)
    
    print(f"=== {filepath} ===")
    if m:
        # print first 500 chars
        snippet = m.group(0)[:400].replace('\n', ' ')
        print(f"Found CTA: {snippet}...")
    else:
        print("NO CTA MATCH FOUND")

for p in ['index.html', 'tentang-kami.html', 'paket.html', 'gallery.html', 'blog.html']:
    check_file(p)

for p in glob.glob('paket/*.html')[:3]:
    check_file(p)
