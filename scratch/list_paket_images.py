import glob, re

for f in sorted(glob.glob('paket/*.html')):
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', c)
    content_imgs = [i for i in imgs if not any(x in i.lower() for x in ['logo', 'icon', 'avatar'])]
    print(f"=== {f} ({len(content_imgs)} content images) ===")
    for img in content_imgs[:5]:
        print(f"  {img}")
