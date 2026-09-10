import re

# We will update all 3 articles to have the EXACT matching Baca Juga, FAQ structure, and CTA band structure from pentingnya-manajemen-risiko-outbound-terbuka.html

# Helper for Article 1
def fix_art1():
    file_path = r"blog\peran-karakter-soft-skills-kesiapan-kerja.html"
    with open(file_path, "r", encoding="utf-8") as f:
        c = f.read()

    # 1. Fix Baca Juga 1, 2, 3
    # Baca Juga 1: pentingnya-melatih-leadership-sekolah.html
    bj1 = """            <!-- BACA JUGA 1 -->
            <div class="baca-juga-box">
              <div class="icon"><i class="fas fa-book-open"></i></div>
              <div class="content">
                <span class="label">BACA JUGA:</span>
                <a href="pentingnya-melatih-leadership-sekolah.html" class="link">Pentingnya Melatih Leadership Siswa Sejak Sekolah: Metode dan Praktik Lapangan</a>
              </div>
            </div>"""

    # Baca Juga 2: outbound-pelajar.html
    bj2 = """            <!-- BACA JUGA 2 -->
            <div class="baca-juga-box">
              <div class="icon"><i class="fas fa-book-open"></i></div>
              <div class="content">
                <span class="label">BACA JUGA:</span>
                <a href="../paket/outbound-sekolah/outbound-pelajar.html" class="link">Paket Outbound Pelajar &amp; Program Pembentukan Karakter Generasi Muda</a>
              </div>
            </div>"""

    # Baca Juga 3: manfaat-edukasi-outdoor-pelajar.html
    bj3 = """            <!-- BACA JUGA 3 -->
            <div class="baca-juga-box">
              <div class="icon"><i class="fas fa-book-open"></i></div>
              <div class="content">
                <span class="label">BACA JUGA:</span>
                <a href="manfaat-edukasi-outdoor-pelajar.html" class="link">Manfaat Edukasi Outdoor untuk Karakter Pelajar dan Pengembangan Sosial</a>
              </div>
            </div>"""

    c = re.sub(r'<!-- BACA JUGA BOX 1 -->\s*<div class="related-article-box">.*?</div>', bj1, c, flags=re.DOTALL)
    c = re.sub(r'<!-- BACA JUGA BOX 2 -->\s*<div class="related-article-box">.*?</div>', bj2, c, flags=re.DOTALL)
    c = re.sub(r'<!-- BACA JUGA BOX 3 -->\s*<div class="related-article-box">.*?</div>', bj3, c, flags=re.DOTALL)

    # 2. Fix Supporting Image figure class
    c = c.replace('<figure class="article-support-image">', '<figure class="supporting-image">')
    c = c.replace('<figcaption class="support-caption">', '<figcaption class="caption">')

    # 3. Fix CTA Band
    cta_exact = """            <!-- PROMO WA CTA BAND -->
            <div class="cta-band">
              <h3>Asah Soft-Skills Siswa/Mahasiswa Anda Sejak Dini</h3>
              <p>Rancang program outbound edukatif yang disesuaikan dengan profil usia dan tujuan institusi pendidikan Anda bersama tim konsultan kami.</p>
              <a href="https://wa.me/6282211221909?text=Halo%20Vendor%20Outbound%2C%20saya%20ingin%20berkonsultasi%20mengenai%20rancangan%20outbound%20edukasi%20untuk%20sekolah%2Fkampus%20kami."
                target="_blank" rel="noopener" class="btn btn-wa"><i class="fab fa-whatsapp"></i> <span>Kontak Kami di +62 82211221909</span></a>
            </div>"""
    c = re.sub(r'<!-- CTA WHATSAPP BAND -->\s*<div class="cta-band cta-band--editorial">.*?</div>\s*</div>', cta_exact, c, flags=re.DOTALL)

    # 4. Fix FAQ Section
    faq_exact = """            <!-- FAQ SECTION -->
            <div class="faq-section" id="faq-section">
              <h3><i class="fas fa-circle-question" style="color:var(--c-maroon);"></i> Pertanyaan Sering Diajukan (FAQ)</h3>
              <div class="faq-container">

                <div class="faq-item">
                  <button class="faq-question" type="button">
                    <span class="faq-q-badge"><i class="fas fa-question-circle"></i></span>
                    <span class="faq-q-text">Apakah soft skills bisa benar-benar terbentuk hanya dari satu kali outbound?</span>
                    <span class="faq-toggle-badge"><i class="fas fa-chevron-down"></i></span>
                  </button>
                  <div class="faq-answer">
                    <div class="faq-answer-inner">
                      Outbound bukan proses instan pembentukan karakter dalam semalam. Kegiatan outbound lebih tepat diposisikan sebagai pemantik kesadaran diri (self-awareness trigger), laboratorium sosial, latihan perilaku nyata, dan titik awal yang memberikan landasan pengalaman konkret bagi proses pembinaan karakter berkelanjutan di sekolah maupun keluarga.
                    </div>
                  </div>
                </div>

                <div class="faq-item">
                  <button class="faq-question" type="button">
                    <span class="faq-q-badge"><i class="fas fa-question-circle"></i></span>
                    <span class="faq-q-text">Mengapa penguasaan akademis saja dinilai belum cukup saat lulusan mulai bekerja?</span>
                    <span class="faq-toggle-badge"><i class="fas fa-chevron-down"></i></span>
                  </button>
                  <div class="faq-answer">
                    <div class="faq-answer-inner">
                      Nilai akademis dan ijazah memberikan validasi pengetahuan teknis dasar, namun dunia kerja menuntut interaksi manusia yang kompleks. Kemampuan beradaptasi dengan budaya organisasi, bekerja sama di bawah tekanan, berkomunikasi lintas divisi, serta memecahkan problem non-linear hanya dapat dikuasai melalui kematangan soft skills.
                    </div>
                  </div>
                </div>

                <div class="faq-item">
                  <button class="faq-question" type="button">
                    <span class="faq-q-badge"><i class="fas fa-question-circle"></i></span>
                    <span class="faq-q-text">Bagaimana metode experiential learning membantu pelajar menginternalisasi nilai kerja sama?</span>
                    <span class="faq-toggle-badge"><i class="fas fa-chevron-down"></i></span>
                  </button>
                  <div class="faq-answer">
                    <div class="faq-answer-inner">
                      Metode experiential learning menempatkan siswa pada skenario tindakan nyata melalui siklus Experience (mengalami tantangan), Reflection (menganalisis proses dan hambatan), Learning (menarik benang merah konsep), serta Application (merumuskan komitmen tindakan dalam kehidupan nyata dan karier masa depan).
                    </div>
                  </div>
                </div>

                <div class="faq-item">
                  <button class="faq-question" type="button">
                    <span class="faq-q-badge"><i class="fas fa-question-circle"></i></span>
                    <span class="faq-q-text">Apa saja aspek soft skills utama yang paling efektif dilatih melalui aktivitas luar ruang?</span>
                    <span class="faq-toggle-badge"><i class="fas fa-chevron-down"></i></span>
                  </button>
                  <div class="faq-answer">
                    <div class="faq-answer-inner">
                      Aspek utama meliputi adaptability (kemampuan menyesuaikan diri dengan situasi baru), problem solving dalam keterbatasan sumber daya, komunikasi asertif, kepemimpinan situasional, manajemen konflik kelompok, serta daya juang (adversity quotient).
                    </div>
                  </div>
                </div>

                <div class="faq-item">
                  <button class="faq-question" type="button">
                    <span class="faq-q-badge"><i class="fas fa-question-circle"></i></span>
                    <span class="faq-q-text">Bagaimana fasilitator memastikan kegiatan outbound tidak sekadar berakhir menjadi rekreasi bermain?</span>
                    <span class="faq-toggle-badge"><i class="fas fa-chevron-down"></i></span>
                  </button>
                  <div class="faq-answer">
                    <div class="faq-answer-inner">
                      Fasilitator bertindak sebagai pengarah dinamika yang memberikan orientasi tujuan sebelum simulasi dimulai, memantau interaksi kelompok tanpa melakukan intervensi berlebih, dan memimpin sesi debriefing terstruktur melalui pertanyaan eksploratif yang mengaitkan pengalaman simulasi dengan realitas dunia kerja.
                    </div>
                  </div>
                </div>

              </div>
            </div>"""

    c = re.sub(r'<!-- FAQ SECTION -->\s*<section class="faq-editorial-section".*?</section>', faq_exact, c, flags=re.DOTALL)

    # 5. Fix Table class and add data-labels
    c = c.replace('<table class="editorial-table">', '<table class="article-table">')

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(c)
    print("Article 1 fixed cleanly.")


# Helper for Article 2
def fix_art2():
    file_path = r"blog\manfaat-outbound-vs-seminar-motivasi-siswa.html"
    with open(file_path, "r", encoding="utf-8") as f:
        c = f.read()

    # 1. Fix Baca Juga 1, 2, 3
    bj1 = """            <!-- BACA JUGA 1 -->
            <div class="baca-juga-box">
              <div class="icon"><i class="fas fa-book-open"></i></div>
              <div class="content">
                <span class="label">BACA JUGA:</span>
                <a href="outbound-pelajar-vs-class-meeting.html" class="link">Outbound Pelajar vs Class Meeting: Mana Lebih Efektif Bangun Kebersamaan?</a>
              </div>
            </div>"""

    bj2 = """            <!-- BACA JUGA 2 -->
            <div class="baca-juga-box">
              <div class="icon"><i class="fas fa-book-open"></i></div>
              <div class="content">
                <span class="label">BACA JUGA:</span>
                <a href="../paket/outbound-sekolah/outbound-pelajar.html" class="link">Paket Outbound Pelajar &amp; Program Character Building Terstruktur</a>
              </div>
            </div>"""

    bj3 = """            <!-- BACA JUGA 3 -->
            <div class="baca-juga-box">
              <div class="icon"><i class="fas fa-book-open"></i></div>
              <div class="content">
                <span class="label">BACA JUGA:</span>
                <a href="rundown-outbound-sekolah-2-hari-1-malam.html" class="link">Contoh Susunan Acara dan Rundown Outbound Sekolah 2 Hari 1 Malam</a>
              </div>
            </div>"""

    c = re.sub(r'<!-- BACA JUGA BOX 1 -->\s*<div class="related-article-box">.*?</div>', bj1, c, flags=re.DOTALL)
    c = re.sub(r'<!-- BACA JUGA BOX 2 -->\s*<div class="related-article-box">.*?</div>', bj2, c, flags=re.DOTALL)
    c = re.sub(r'<!-- BACA JUGA BOX 3 -->\s*<div class="related-article-box">.*?</div>', bj3, c, flags=re.DOTALL)

    # 2. Fix Supporting Image figure class
    c = c.replace('<figure class="article-support-image">', '<figure class="supporting-image">')
    c = c.replace('<figcaption class="support-caption">', '<figcaption class="caption">')

    # 3. Fix CTA Band
    cta_exact = """            <!-- PROMO WA CTA BAND -->
            <div class="cta-band">
              <h3>Rancang Program Outbound Edukatif untuk Sekolah Anda</h3>
              <p>Diskusikan kebutuhan rundown, pemilihan lokasi ramah pelajar, dan penyelarasan tema karakter bersama tim konsultan Vendor Outbound.</p>
              <a href="https://wa.me/6282211221909?text=Halo%20Vendor%20Outbound%2C%20saya%20ingin%20meminta%20proposal%20program%20outbound%20edukatif%20untuk%20institusi%20pendidikan%20kami."
                target="_blank" rel="noopener" class="btn btn-wa"><i class="fab fa-whatsapp"></i> <span>Dapatkan Proposal Program Edukatif di +62 82211221909</span></a>
            </div>"""
    c = re.sub(r'<!-- CTA WHATSAPP BAND -->\s*<div class="cta-band cta-band--editorial">.*?</div>\s*</div>', cta_exact, c, flags=re.DOTALL)

    # 4. Fix FAQ Section
    faq_exact = """            <!-- FAQ SECTION -->
            <div class="faq-section" id="faq-section">
              <h3><i class="fas fa-circle-question" style="color:var(--c-maroon);"></i> Pertanyaan Sering Diajukan (FAQ)</h3>
              <div class="faq-container">

                <div class="faq-item">
                  <button class="faq-question" type="button">
                    <span class="faq-q-badge"><i class="fas fa-question-circle"></i></span>
                    <span class="faq-q-text">Dapatkah materi keagamaan atau nilai sekolah disisipkan dalam program outbound?</span>
                    <span class="faq-toggle-badge"><i class="fas fa-chevron-down"></i></span>
                  </button>
                  <div class="faq-answer">
                    <div class="faq-answer-inner">
                      Sangat memungkinkan. Program outbound edukasi dapat dirancang agar skenario simulasi permainan, penugasan kelompok, dan materi refleksi (debrief) selaras dengan visi misi atau nilai keagamaan institusi sekolah, sepanjang hal tersebut dikoordinasikan dalam tahap perencanaan pra-kegiatan.
                    </div>
                  </div>
                </div>

                <div class="faq-item">
                  <button class="faq-question" type="button">
                    <span class="faq-q-badge"><i class="fas fa-question-circle"></i></span>
                    <span class="faq-q-text">Apakah ini berarti seminar motivasi di dalam ruangan sudah tidak efektif lagi bagi siswa?</span>
                    <span class="faq-toggle-badge"><i class="fas fa-chevron-down"></i></span>
                  </button>
                  <div class="faq-answer">
                    <div class="faq-answer-inner">
                      Seminar ruangan tetap memiliki fungsi kuat dalam mentransfer kerangka konseptual, materi teoritis, dan wawasan kognitif. Outbound berfungsi sebagai pelengkap praktis (komplementer) yang mengubah konsep abstrak tersebut menjadi pengalaman nyata dan latihan perilaku di lapangan.
                    </div>
                  </div>
                </div>

                <div class="faq-item">
                  <button class="faq-question" type="button">
                    <span class="faq-q-badge"><i class="fas fa-question-circle"></i></span>
                    <span class="faq-q-text">Bagaimana cara mengukur keberhasilan program outbound edukasi bagi siswa?</span>
                    <span class="faq-toggle-badge"><i class="fas fa-chevron-down"></i></span>
                  </button>
                  <div class="faq-answer">
                    <div class="faq-answer-inner">
                      Keberhasilan dapat diukur melalui lembar observasi dinamika kelompok oleh fasilitator dan guru pendamping, kualitas keterlibatan saat sesi refleksi, serta perubahan perilaku pasca-kegiatan seperti peningkatan kerja sama kelas dan komunikasi yang lebih terbuka.
                    </div>
                  </div>
                </div>

                <div class="faq-item">
                  <button class="faq-question" type="button">
                    <span class="faq-q-badge"><i class="fas fa-question-circle"></i></span>
                    <span class="faq-q-text">Apakah seluruh siswa dengan berbagai kondisi fisik dapat mengikuti outbound?</span>
                    <span class="faq-toggle-badge"><i class="fas fa-chevron-down"></i></span>
                  </button>
                  <div class="faq-answer">
                    <div class="faq-answer-inner">
                      Ya, rancangan aktivitas outbound edukasi berfokus pada dinamika kelompok, komunikasi, dan logika pemecahan masalah, bukan ujian ketahanan fisik militer. Skenario aktivitas selalu disesuaikan dengan profil usia dan catatan kesehatan peserta.
                    </div>
                  </div>
                </div>

                <div class="faq-item">
                  <button class="faq-question" type="button">
                    <span class="faq-q-badge"><i class="fas fa-question-circle"></i></span>
                    <span class="faq-q-text">Berapa durasi ideal untuk program outbound edukasi sekolah?</span>
                    <span class="faq-toggle-badge"><i class="fas fa-chevron-down"></i></span>
                  </button>
                  <div class="faq-answer">
                    <div class="faq-answer-inner">
                      Program satu hari (One Day Program 6-8 jam) sangat ideal untuk penguatan tema spesifik seperti kekompakan kelas. Sedangkan format 2 hari 1 malam (Leadership Camp) memberikan ruang lebih mendalam untuk pembiasaan disiplin dan kemandirian.
                    </div>
                  </div>
                </div>

              </div>
            </div>"""

    c = re.sub(r'<!-- FAQ SECTION -->\s*<section class="faq-editorial-section".*?</section>', faq_exact, c, flags=re.DOTALL)

    # 5. Fix Table class
    c = c.replace('<table class="editorial-table">', '<table class="article-table">')

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(c)
    print("Article 2 fixed cleanly.")


# Helper for Article 3
def fix_art3():
    file_path = r"blog\jasa-fasilitator-outbound-edukasi-sekolah-kampus.html"
    with open(file_path, "r", encoding="utf-8") as f:
        c = f.read()

    # 1. Fix Baca Juga 1, 2, 3
    bj1 = """            <!-- BACA JUGA 1 -->
            <div class="baca-juga-box">
              <div class="icon"><i class="fas fa-book-open"></i></div>
              <div class="content">
                <span class="label">BACA JUGA:</span>
                <a href="kriteria-menentukan-lokasi-outbound-aman.html" class="link">Kriteria Menentukan Lokasi Outbound yang Aman untuk Kegiatan Pelajar</a>
              </div>
            </div>"""

    bj2 = """            <!-- BACA JUGA 2 -->
            <div class="baca-juga-box">
              <div class="icon"><i class="fas fa-book-open"></i></div>
              <div class="content">
                <span class="label">BACA JUGA:</span>
                <a href="../paket/outbound-sekolah/outbound-pelajar.html" class="link">Paket Outbound Sekolah: Pilihan Program SD, SMP, SMA, dan Kampus</a>
              </div>
            </div>"""

    bj3 = """            <!-- BACA JUGA 3 -->
            <div class="baca-juga-box">
              <div class="icon"><i class="fas fa-book-open"></i></div>
              <div class="content">
                <span class="label">BACA JUGA:</span>
                <a href="jasa-outbound-karakter-sekolah-terpercaya.html" class="link">Jasa Outbound Karakter Sekolah Terpercaya: Panduan untuk Pendidik</a>
              </div>
            </div>"""

    c = re.sub(r'<!-- BACA JUGA BOX 1 -->\s*<div class="related-article-box">.*?</div>', bj1, c, flags=re.DOTALL)
    c = re.sub(r'<!-- BACA JUGA BOX 2 -->\s*<div class="related-article-box">.*?</div>', bj2, c, flags=re.DOTALL)
    c = re.sub(r'<!-- BACA JUGA BOX 3 -->\s*<div class="related-article-box">.*?</div>', bj3, c, flags=re.DOTALL)

    # 2. Fix Supporting Image figure class
    c = c.replace('<figure class="article-support-image">', '<figure class="supporting-image">')
    c = c.replace('<figcaption class="support-caption">', '<figcaption class="caption">')

    # 3. Fix CTA Band
    cta_exact = """            <!-- PROMO WA CTA BAND -->
            <div class="cta-band">
              <h3>Rencanakan Petualangan Edukatif Sekolah Anda Bersama Tim Ahli</h3>
              <p>Dapatkan pendampingan fasilitator profesional, pemilihan venue aman, dan penawaran paket outbound sekolah yang disesuaikan dengan anggaran institusi Anda.</p>
              <a href="https://wa.me/6282211221909?text=Halo%20Vendor%20Outbound%2C%20saya%20ingin%20berkonsultasi%20mengenai%20perencanaan%20paket%20outbound%20sekolah%20dan%20jasa%20fasilitator%20edukasi."
                target="_blank" rel="noopener" class="btn btn-wa"><i class="fab fa-whatsapp"></i> <span>Rencanakan di WhatsApp +62 82211221909</span></a>
            </div>"""
    c = re.sub(r'<!-- CTA WHATSAPP BAND -->\s*<div class="cta-band cta-band--editorial">.*?</div>\s*</div>', cta_exact, c, flags=re.DOTALL)

    # 4. Fix FAQ Section
    faq_exact = """            <!-- FAQ SECTION -->
            <div class="faq-section" id="faq-section">
              <h3><i class="fas fa-circle-question" style="color:var(--c-maroon);"></i> Pertanyaan Sering Diajukan (FAQ)</h3>
              <div class="faq-container">

                <div class="faq-item">
                  <button class="faq-question" type="button">
                    <span class="faq-q-badge"><i class="fas fa-question-circle"></i></span>
                    <span class="faq-q-text">Apakah kami bisa meminta pertemuan presentasi program terlebih dahulu?</span>
                    <span class="faq-toggle-badge"><i class="fas fa-chevron-down"></i></span>
                  </button>
                  <div class="faq-answer">
                    <div class="faq-answer-inner">
                      Tentu, tim konsultan Vendor Outbound dapat melakukan pembahasan, audiensi teknis, atau presentasi rancangan proposal program secara daring maupun tatap muka sesuai kesepakatan jadwal dan kebutuhan institusi sekolah Anda.
                    </div>
                  </div>
                </div>

                <div class="faq-item">
                  <button class="faq-question" type="button">
                    <span class="faq-q-badge"><i class="fas fa-question-circle"></i></span>
                    <span class="faq-q-text">Apakah program paket outbound sekolah dapat disesuaikan dengan jenjang usia peserta?</span>
                    <span class="faq-toggle-badge"><i class="fas fa-chevron-down"></i></span>
                  </button>
                  <div class="faq-answer">
                    <div class="faq-answer-inner">
                      Ya, rancangan simulasi dan tingkat kesulitan rintangan selalu disesuaikan secara khusus untuk jenjang SD, SMP, SMA/SMK, hingga mahasiswa perguruan tinggi agar selaras dengan tahap perkembangan kognitif dan fisik peserta.
                    </div>
                  </div>
                </div>

                <div class="faq-item">
                  <button class="faq-question" type="button">
                    <span class="faq-q-badge"><i class="fas fa-question-circle"></i></span>
                    <span class="faq-q-text">Apakah dewan guru dan panitia sekolah dapat turut serta dalam aktivitas?</span>
                    <span class="faq-toggle-badge"><i class="fas fa-chevron-down"></i></span>
                  </button>
                  <div class="faq-answer">
                    <div class="faq-answer-inner">
                      Sangat dianjurkan. Guru dapat berperan sebagai pengamat proses (observer) untuk mencatat dinamika kepribadian siswa, atau ikut serta dalam beberapa sesi permainan keakraban guna mempererat kedekatan emosional antara pendidik dan murid.
                    </div>
                  </div>
                </div>

                <div class="faq-item">
                  <button class="faq-question" type="button">
                    <span class="faq-q-badge"><i class="fas fa-question-circle"></i></span>
                    <span class="faq-q-text">Bagaimana prosedur keselamatan yang diterapkan untuk kegiatan luar ruang pelajar?</span>
                    <span class="faq-toggle-badge"><i class="fas fa-chevron-down"></i></span>
                  </button>
                  <div class="faq-answer">
                    <div class="faq-answer-inner">
                      Keselamatan dikelola melalui survei kelayakan medan (risk assessment), inspeksi peralatan sebelum digunakan, safety briefing wajib, rasio pengawasan fasilitator yang memadai, ketersediaan P3K lapangan, serta pemetaan jalur evakuasi darurat medis terdekat.
                    </div>
                  </div>
                </div>

                <div class="faq-item">
                  <button class="faq-question" type="button">
                    <span class="faq-q-badge"><i class="fas fa-question-circle"></i></span>
                    <span class="faq-q-text">Bagaimana pihak sekolah mempersiapkan peserta didik sebelum hari pelaksanaan outbound?</span>
                    <span class="faq-toggle-badge"><i class="fas fa-chevron-down"></i></span>
                  </button>
                  <div class="faq-answer">
                    <div class="faq-answer-inner">
                      Sekolah disarankan membagikan lembar panduan perlengkapan pribadi (pakaian olahraga, obat pribadi, botol minum), melakukan screening riwayat kesehatan siswa, serta memberikan arahan awal mengenai pentingnya sikap disiplin dan saling menghormati selama di lapangan.
                    </div>
                  </div>
                </div>

              </div>
            </div>"""

    c = re.sub(r'<!-- FAQ SECTION -->\s*<section class="faq-editorial-section".*?</section>', faq_exact, c, flags=re.DOTALL)

    # 5. Fix Table class
    c = c.replace('<table class="editorial-table">', '<table class="article-table">')

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(c)
    print("Article 3 fixed cleanly.")

fix_art1()
fix_art2()
fix_art3()
