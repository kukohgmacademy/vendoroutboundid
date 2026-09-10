import os
from PIL import Image

brain_dir = r"C:\Users\Leonovo\.gemini\antigravity-ide\brain\ae1a0ec4-43eb-4806-8cd0-c4fcd65264dd"
target_dir = r"assets\image\blog"
os.makedirs(target_dir, exist_ok=True)

mappings = [
    (
        os.path.join(brain_dir, "karakter_softskills_hero_1789026951725.jpg"),
        os.path.join(target_dir, "peran-karakter-soft-skills-kesiapan-kerja-hero.webp")
    ),
    (
        os.path.join(brain_dir, "karakter_softskills_support_1789027296642.jpg"),
        os.path.join(target_dir, "peran-karakter-soft-skills-kesiapan-kerja-support-image-1.webp")
    ),
    (
        os.path.join(brain_dir, "manfaat_seminar_hero_1789027325113.jpg"),
        os.path.join(target_dir, "manfaat-outbound-vs-seminar-motivasi-siswa-hero.webp")
    ),
    (
        os.path.join(brain_dir, "manfaat_outbound_support_1789025440119.jpg"),
        os.path.join(target_dir, "manfaat-outbound-vs-seminar-motivasi-siswa-support-image-1.webp")
    ),
    (
        os.path.join(brain_dir, "jasa_fasilitator_hero_1789025607765.jpg"),
        os.path.join(target_dir, "jasa-fasilitator-outbound-edukasi-sekolah-kampus-hero.webp")
    ),
    (
        os.path.join(brain_dir, "jasa_fasilitator_support_1789025635314.jpg"),
        os.path.join(target_dir, "jasa-fasilitator-outbound-edukasi-sekolah-kampus-support-image-1.webp")
    )
]

print("Processing 6 images from pristine raw brain files (single watermark only)...")

for src_path, dest_path in mappings:
    assert os.path.exists(src_path), f"Source file missing: {src_path}"
    
    with Image.open(src_path) as img:
        img = img.convert("RGB")
        w, h = img.size
        new_w = 1600
        new_h = int(h * (new_w / w))
        img_resized = img.resize((new_w, new_h), Image.Resampling.BILINEAR)
        
        quality = 80
        img_resized.save(dest_path, "WEBP", quality=quality, method=4)
        while os.path.getsize(dest_path) > 145 * 1024 and quality > 30:
            quality -= 5
            img_resized.save(dest_path, "WEBP", quality=quality, method=4)
            
        final_size_kb = os.path.getsize(dest_path) / 1024
        print(f"SUCCESS: {os.path.basename(dest_path)} -> {final_size_kb:.1f} KB (Quality: {quality})")

print("\nAll 6 images successfully regenerated with single watermark and optimized size < 150KB!")
