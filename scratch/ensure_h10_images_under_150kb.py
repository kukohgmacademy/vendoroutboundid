import os
from PIL import Image

images = [
    r"assets\image\blog\peran-karakter-soft-skills-kesiapan-kerja-hero.webp",
    r"assets\image\blog\peran-karakter-soft-skills-kesiapan-kerja-support-image-1.webp",
    r"assets\image\blog\manfaat-outbound-vs-seminar-motivasi-siswa-hero.webp",
    r"assets\image\blog\manfaat-outbound-vs-seminar-motivasi-siswa-support-image-1.webp",
    r"assets\image\blog\jasa-fasilitator-outbound-edukasi-sekolah-kampus-hero.webp",
    r"assets\image\blog\jasa-fasilitator-outbound-edukasi-sekolah-kampus-support-image-1.webp"
]

for img_path in images:
    size_kb = os.path.getsize(img_path) / 1024
    if size_kb > 150.0:
        im = Image.open(img_path)
        for q in range(80, 10, -5):
            im.save(img_path, "WEBP", quality=q, method=6)
            s_kb = os.path.getsize(img_path) / 1024
            if s_kb <= 150.0:
                print(f"Compressed {img_path} to {s_kb:.2f} KB with quality {q}")
                break
    else:
        print(f"OK: {img_path} ({size_kb:.2f} KB)")
