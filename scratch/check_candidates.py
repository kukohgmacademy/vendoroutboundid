import os
from PIL import Image

brain = r"C:\Users\Leonovo\.gemini\antigravity-ide\brain\ae1a0ec4-43eb-4806-8cd0-c4fcd65264dd"
candidates = [
    "decision_making_support_1789094980955.jpg",
    "batu_leadership_support_1789096185134.jpg",
    "karakter_softskills_support_1789027296642.jpg",
    "fasilitator_ldks_support_1789204503604.jpg"
]

for c in candidates:
    p = os.path.join(brain, c)
    if os.path.exists(p):
        im = Image.open(p)
        print(f"{c}: size={im.size}")
