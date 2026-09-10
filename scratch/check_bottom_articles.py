files = [
    'blog/peran-karakter-soft-skills-kesiapan-kerja.html',
    'blog/manfaat-outbound-vs-seminar-motivasi-siswa.html',
    'blog/jasa-fasilitator-outbound-edukasi-sekolah-kampus.html'
]

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    print("=" * 40)
    print(fpath)
    pos_faq = c.find('id="faq-section"')
    if pos_faq != -1:
        print(c[pos_faq-30:pos_faq+1200])
    pos_end_art = c.find('</article>')
    if pos_end_art != -1:
        print("--- AROUND </article> ---")
        print(c[pos_end_art-300:pos_end_art+200])
