import os
from PIL import Image

# Let's crop the center 500x200 of each raw source image and save to scratch to inspect
brain = r"C:\Users\Leonovo\.gemini\antigravity-ide\brain\ae1a0ec4-43eb-4806-8cd0-c4fcd65264dd"
scratch = os.path.join(brain, "scratch")

sources = [
    "indoor_vs_outdoor_support_1789095241101.jpg",
    "dampak_komunikasi_support_1788508388059.jpg",
    "decision_making_hero_1789094850037.jpg",
    "indoor_vs_outdoor_hero_1789095057781.jpg",
    "batu_leadership_hero_1789095497154.jpg",
    "katalog_paket_support_1788509038797.jpg"
]

for s in sources:
    p = os.path.join(brain, s)
    im = Image.open(p)
    w, h = im.size
    cx, cy = w // 2, h // 2
    # crop center
    crop = im.crop((cx - 250, cy - 100, cx + 250, cy + 100))
    crop_path = os.path.join(scratch, f"center_{s}.jpg")
    crop.save(crop_path)
    print(f"Saved center crop for {s}")
