import os
from PIL import Image

brain_dir = r"C:\Users\Leonovo\.gemini\antigravity-ide\brain\ae1a0ec4-43eb-4806-8cd0-c4fcd65264dd"

files = [
    "karakter_softskills_hero_1789026951725.jpg",
    "karakter_softskills_support_1789027296642.jpg",
    "manfaat_seminar_hero_1789027325113.jpg",
    "manfaat_outbound_support_1789025440119.jpg",
    "jasa_fasilitator_hero_1789025607765.jpg",
    "jasa_fasilitator_support_1789025635314.jpg",
    "peran_karakter_hero_1789025304879.jpg",
    "peran_karakter_support_1789025386275.jpg",
    "manfaat_outbound_hero_1789025409178.jpg"
]

print("Checking raw images in brain...")
for f in files:
    p = os.path.join(brain_dir, f)
    if os.path.exists(p):
        img = Image.open(p)
        print(f"File: {f}, size: {img.size}")
