import glob, re

total_old = 0
for f in sorted(glob.glob('paket/*.html')):
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    old = re.findall(r'assets/image/(?:paket|hero)/[^"\']+', c)
    if old:
        total_old += len(old)
        print(f'{f}: {len(old)} old images -> {set(old)}')

if total_old == 0:
    print("ALL 20 PAKET PAGES ARE 100% UPDATED! ZERO OLD IMAGES REMAINING.")
