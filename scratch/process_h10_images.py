import os
from PIL import Image, ImageDraw, ImageFont

brain_dir = r"C:\Users\Leonovo\.gemini\antigravity-ide\brain\ae1a0ec4-43eb-4806-8cd0-c4fcd65264dd"
dest_dir = r"assets\image\blog"
os.makedirs(dest_dir, exist_ok=True)

image_mapping = [
    (
        os.path.join(brain_dir, "karakter_softskills_hero_1789026951725.jpg"),
        os.path.join(dest_dir, "peran-karakter-soft-skills-kesiapan-kerja-hero.webp")
    ),
    (
        os.path.join(brain_dir, "karakter_softskills_support_1789027296642.jpg"),
        os.path.join(dest_dir, "peran-karakter-soft-skills-kesiapan-kerja-support-image-1.webp")
    ),
    (
        os.path.join(brain_dir, "manfaat_seminar_hero_1789027325113.jpg"),
        os.path.join(dest_dir, "manfaat-outbound-vs-seminar-motivasi-siswa-hero.webp")
    ),
    (
        os.path.join(brain_dir, "manfaat_outbound_support_1789025440119.jpg"),
        os.path.join(dest_dir, "manfaat-outbound-vs-seminar-motivasi-siswa-support-image-1.webp")
    ),
    (
        os.path.join(brain_dir, "jasa_fasilitator_hero_1789025607765.jpg"),
        os.path.join(dest_dir, "jasa-fasilitator-outbound-edukasi-sekolah-kampus-hero.webp")
    ),
    (
        os.path.join(brain_dir, "jasa_fasilitator_support_1789025635314.jpg"),
        os.path.join(dest_dir, "jasa-fasilitator-outbound-edukasi-sekolah-kampus-support-image-1.webp")
    )
]

def add_watermark_and_compress(src_path, dst_path):
    img = Image.open(src_path).convert("RGBA")
    # Resize to 1600x900 (16:9)
    img = img.resize((1600, 900), Image.Resampling.LANCZOS)
    
    # Check if already has watermark or add single centered watermark
    txt_layer = Image.new("RGBA", img.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(txt_layer)
    text = "venroroutbound.id"
    
    font = None
    for font_name in ["arialbd.ttf", "arial.ttf", "segoeui.ttf", "calibri.ttf"]:
        try:
            font = ImageFont.truetype(font_name, 46)
            break
        except:
            pass
    if not font:
        font = ImageFont.load_default()
        
    bbox = draw.textbbox((0, 0), text, font=font)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    x = (1600 - w) // 2
    y = (900 - h) // 2
    
    # Draw soft shadow + text
    draw.text((x + 2, y + 2), text, fill=(0, 0, 0, 110), font=font)
    draw.text((x, y), text, fill=(255, 255, 255, 190), font=font)
    
    combined = Image.alpha_composite(img, txt_layer).convert("RGB")
    
    # Compress WebP to stay < 150KB
    quality = 85
    while quality >= 30:
        combined.save(dst_path, "WEBP", quality=quality, method=6)
        size_kb = os.path.getsize(dst_path) / 1024
        if size_kb <= 150.0:
            break
        quality -= 5
        
    print(f"Saved: {dst_path} | Quality: {quality} | Size: {os.path.getsize(dst_path)/1024:.2f} KB")

for src, dst in image_mapping:
    if not os.path.exists(src):
        print(f"ERROR: Source file {src} does not exist!")
    else:
        add_watermark_and_compress(src, dst)
