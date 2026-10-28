import glob, re

for f in sorted(glob.glob('paket/*.html')):
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    m = re.findall(r'class=[\'"]cta-band-luxury[\'"]', c)
    print(f'{f}: {len(m)} cta-band-luxury found')
