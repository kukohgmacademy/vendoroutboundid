import re
import glob
import os

files = [
    'blog/peran-karakter-soft-skills-kesiapan-kerja.html',
    'blog/manfaat-outbound-vs-seminar-motivasi-siswa.html',
    'blog/jasa-fasilitator-outbound-edukasi-sekolah-kampus.html'
]

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    imgs = re.findall(r'assets/image/blog/[^"\'\s>]+', c)
    print(f"=== {fpath} ===")
    for img in set(imgs):
        print(" ", img, "EXISTS:", os.path.exists(img))

print("\n=== RECENT ARTIFACT IMAGES IN BRAIN ===")
brain_dir = r'C:\Users\Leonovo\.gemini\antigravity-ide\brain\ae1a0ec4-43eb-4806-8cd0-c4fcd65264dd'
all_artifacts = glob.glob(os.path.join(brain_dir, '*.*'))
for art in sorted(all_artifacts, key=os.path.getmtime, reverse=True)[:25]:
    if art.endswith(('.jpg', '.jpeg', '.png', '.webp')):
        print(f"{os.path.basename(art)}: {os.path.getsize(art)/1024:.1f} KB")
