import re, glob

def find_images(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        c = f.read()
    
    imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\'][^>]*>', c)
    # also check background-image: url(...)
    bg_imgs = re.findall(r'url\(["\']?([^"\')]+\.(?:jpg|jpeg|png|webp))["\']?\)', c)
    return imgs, bg_imgs

pages = ['index.html', 'tentang-kami.html', 'paket.html', 'gallery.html']
for p in pages:
    imgs, bg_imgs = find_images(p)
    print(f"=== {p} ===")
    print(f"Total imgs: {len(imgs)}, Total bg: {len(bg_imgs)}")
    for i in imgs:
        if 'logo' not in i.lower() and 'icon' not in i.lower() and 'avatar' not in i.lower():
            print(f"  img: {i}")

paket_pages = sorted(glob.glob('paket/*.html'))
print(f"\n=== Paket pages ({len(paket_pages)}) ===")
for p in paket_pages[:3]:
    imgs, bg_imgs = find_images(p)
    print(f"{p}: {len(imgs)} imgs, {len(bg_imgs)} bg")
    for i in imgs:
        if 'logo' not in i.lower() and 'icon' not in i.lower() and 'avatar' not in i.lower():
            print(f"  img: {i}")
