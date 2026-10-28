hero_reps = {
    'paket/family-gathering.html': ('assets/image/hero/hero-famili-gathering.webp', 'assets/image/kebutuhan-gambar/family-gathering-mountain.webp'),
    'paket/outbound-perusahaan.html': ('assets/image/hero/hero-outbound-perusahaan.webp', 'assets/image/kebutuhan-gambar/employees-corporate-banner.webp'),
    'paket/outbound-sekolah.html': ('assets/image/hero/hero-outbound-sekola.webp', 'assets/image/kebutuhan-gambar/students-cheering-puzzle.webp'),
    'paket/outbound-wisata.html': ('assets/image/hero/hero-outbound-wisata.webp', 'assets/image/kebutuhan-gambar/group-whitewater-rafting.webp'),
}

for fpath, (old, new) in hero_reps.items():
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    c = c.replace(old, new)
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"Updated hero in {fpath}")
