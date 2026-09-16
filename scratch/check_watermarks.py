import os
from PIL import Image

brain = r"C:\Users\Leonovo\.gemini\antigravity-ide\brain\ae1a0ec4-43eb-4806-8cd0-c4fcd65264dd"
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
    if os.path.exists(p):
        print(s, "exists, size:", os.path.getsize(p))
    else:
        print(s, "NOT FOUND")
