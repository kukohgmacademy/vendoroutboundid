import os
from PIL import Image

brain_dir = r"C:\Users\Leonovo\.gemini\antigravity-ide\brain\ae1a0ec4-43eb-4806-8cd0-c4fcd65264dd"
target_dir = r"c:\GM ACADEMY\PROJECT VENDOR OUTBOUND ID\PROJECT YANG SUDAH DIDEPLOY DOMAIN\venroroutboundid\assets\image\blog"

image_mapping = [
    ("indoor_vs_outdoor_support_1789095241101.jpg", "meruntuhkan-silo-mental-divisi-perusahaan-hero.webp"),
    ("dampak_komunikasi_support_1788508388059.jpg", "meruntuhkan-silo-mental-divisi-perusahaan-support-image-1.webp"),
    ("decision_making_hero_1789094850037.jpg", "mengukur-efektivitas-outbound-retensi-karyawan-hero.webp"),
    ("indoor_vs_outdoor_hero_1789095057781.jpg", "mengukur-efektivitas-outbound-retensi-karyawan-support-image-1.webp"),
    ("batu_leadership_hero_1789095497154.jpg", "paket-outbound-corporate-synergy-engagement-hero.webp"),
    ("katalog_paket_support_1788509038797.jpg", "paket-outbound-corporate-synergy-engagement-support-image-1.webp")
]

for src_name, dest_name in image_mapping:
    src_path = os.path.join(brain_dir, src_name)
    dest_path = os.path.join(target_dir, dest_name)
    
    with Image.open(src_path) as im:
        im_resized = im.resize((1600, 900), Image.Resampling.LANCZOS).convert("RGB")
        im_resized.save(dest_path, "WEBP", quality=60, method=1)
        size_kb = os.path.getsize(dest_path) / 1024
        print(f"DONE: {dest_name} -> {size_kb:.1f} KB")
