import glob
import os

brain_dir = r'C:\Users\Leonovo\.gemini\antigravity-ide\brain\ae1a0ec4-43eb-4806-8cd0-c4fcd65264dd'

# Let's search for python scripts in brain or scratch that processed h10 or 10sep images
scripts = glob.glob(os.path.join(brain_dir, 'scratch', '*.py')) + glob.glob('scratch/*.py')

for s in scripts:
    with open(s, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    if 'peran-karakter' in content or 'manfaat-outbound' in content or 'jasa-fasilitator' in content:
        if 'PIL' in content or 'watermark' in content or 'ImageDraw' in content or 'quality' in content:
            print(f"Found image processing script: {s}")
            print(content[:800])
            print("="*40)
