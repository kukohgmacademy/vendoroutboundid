import re

files = [
    r"blog/meruntuhkan-silo-mental-divisi-perusahaan.html",
    r"blog/mengukur-efektivitas-outbound-retensi-karyawan.html",
    r"blog/paket-outbound-corporate-synergy-engagement.html"
]

for fpath in files:
    try:
        with open(fpath, "r", encoding="utf-8") as f:
            html = f.read()
        art = re.search(r'<article class="article-main">(.*?)</article>', html, re.DOTALL)
        if art:
            content = art.group(1)
            content = re.sub(r'<script.*?</script>', '', content, flags=re.DOTALL)
            text = re.sub(r'<[^>]+>', ' ', content)
            words = [w for w in text.split() if w]
            print(f"{fpath}: {len(words)} editorial words")
        else:
            print(f"{fpath}: article tag not found")
    except Exception as e:
        print(f"{fpath}: {e}")
