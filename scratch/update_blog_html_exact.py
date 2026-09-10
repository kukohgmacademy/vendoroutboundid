import re

blog_file = "blog.html"
with open(blog_file, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update stat count
content = re.sub(
    r'(<span class="subpage-hero-stat-num">)\d+(</span>\s*<span class="subpage-hero-stat-label">Artikel Panduan</span>)',
    r'\g<1>30\g<2>',
    content
)

# 2. Update filter button count
content = re.sub(
    r'(<button class="news-filter-btn active" data-filter="all"><i class="fas fa-layer-group"></i> Semua\s*\()\d+(\)</button>)',
    r'\g<1>30\g<2>',
    content
)

# 3. Update news-mosaic-grid
new_mosaic = """        <!-- 1. TOP NEWS MAGAZINE MOSAIC (1 Large + 4 Sub-Featured) -->
        <div class="news-mosaic-grid">

          <!-- Left Large Featured Story (50% Width) - Artikel 1 (10 Sep 2026) -->
          <a href="blog/peran-karakter-soft-skills-kesiapan-kerja.html" class="news-mosaic-item news-mosaic-main">
            <img src="assets/image/blog/peran-karakter-soft-skills-kesiapan-kerja-hero.webp"
              alt="Peran Karakter dan Soft Skills dalam Kesiapan Memasuki Dunia Kerja bagi Lulusan Sekolah" class="news-mosaic-bg" loading="eager">
            <div class="news-mosaic-overlay"></div>
            <div class="news-mosaic-content">
              <span class="news-badge badge-maroon"><i class="fas fa-graduation-cap"></i> EDUKASI &amp; SOFT SKILLS &bull; TERBARU 10 SEP 2026</span>
              <h2 class="news-mosaic-title-main">Peran Karakter &amp; Soft Skills dalam Kesiapan Memasuki Dunia Kerja bagi Lulusan Sekolah</h2>
              <div class="news-meta">
                <span>Arby Ardiansyah</span>
                <span class="dot"></span>
                <span>10 September 2026</span>
                <span class="dot"></span>
                <span>8 Menit Baca</span>
              </div>
            </div>
          </a>

          <!-- Right 2x2 Sub-Grid (4 Stories) -->
          <div class="news-mosaic-subgrid">

            <!-- Sub 1: Artikel 2 (10 Sep 2026) -->
            <a href="blog/manfaat-outbound-vs-seminar-motivasi-siswa.html" class="news-mosaic-item news-mosaic-sub">
              <img src="assets/image/blog/manfaat-outbound-vs-seminar-motivasi-siswa-hero.webp"
                alt="5 Manfaat Nyata Outbound Dibandingkan Seminar Motivasi Ruangan Bagi Siswa" class="news-mosaic-bg" loading="lazy">
              <div class="news-mosaic-overlay"></div>
              <div class="news-mosaic-content">
                <span class="news-badge badge-emerald">KOMPARASI EDUKASI</span>
                <h3 class="news-mosaic-title-sub">5 Manfaat Nyata Outbound Dibandingkan Seminar Motivasi Ruangan Bagi Siswa</h3>
                <div class="news-meta">
                  <span>10 Sep 2026</span>
                  <span class="dot"></span>
                  <span>Edukasi Karakter</span>
                </div>
              </div>
            </a>

            <!-- Sub 2: Artikel 3 (10 Sep 2026) -->
            <a href="blog/jasa-fasilitator-outbound-edukasi-sekolah-kampus.html" class="news-mosaic-item news-mosaic-sub">
              <img src="assets/image/blog/jasa-fasilitator-outbound-edukasi-sekolah-kampus-hero.webp"
                alt="Jasa Fasilitator Outbound Edukasi Terpercaya untuk Sekolah dan Kampus" class="news-mosaic-bg" loading="lazy">
              <div class="news-mosaic-overlay"></div>
              <div class="news-mosaic-content">
                <span class="news-badge badge-gold">FASILITATOR EDUKASI</span>
                <h3 class="news-mosaic-title-sub">Jasa Fasilitator Outbound Edukasi Terpercaya untuk Sekolah &amp; Kampus</h3>
                <div class="news-meta">
                  <span>10 Sep 2026</span>
                  <span class="dot"></span>
                  <span>Paket Sekolah 2026</span>
                </div>
              </div>
            </a>

            <!-- Sub 3: Artikel 1 H-09 (9 Sep 2026) -->
            <a href="blog/pentingnya-manajemen-risiko-outbound-terbuka.html" class="news-mosaic-item news-mosaic-sub">
              <img src="assets/image/blog/pentingnya-manajemen-risiko-outbound-terbuka-hero.webp"
                alt="Pentingnya Manajemen Risiko Outbound di Alam Terbuka" class="news-mosaic-bg" loading="lazy">
              <div class="news-mosaic-overlay"></div>
              <div class="news-mosaic-content">
                <span class="news-badge badge-maroon">K3 OUTDOOR</span>
                <h3 class="news-mosaic-title-sub">Pentingnya Manajemen Risiko dalam Outbound di Alam Terbuka</h3>
                <div class="news-meta">
                  <span>9 Sep 2026</span>
                  <span class="dot"></span>
                  <span>Risk Management</span>
                </div>
              </div>
            </a>

            <!-- Sub 4: Artikel 2 H-09 (9 Sep 2026) -->
            <a href="blog/tips-mempersiapkan-perlengkapan-outbound-camping.html" class="news-mosaic-item news-mosaic-sub">
              <img src="assets/image/blog/tips-mempersiapkan-perlengkapan-outbound-camping-hero.webp"
                alt="Tips Mempersiapkan Perlengkapan Outbound Camping" class="news-mosaic-bg" loading="lazy">
              <div class="news-mosaic-overlay"></div>
              <div class="news-mosaic-content">
                <span class="news-badge badge-gold">PANDUAN PACKING</span>
                <h3 class="news-mosaic-title-sub">Tips Perlengkapan Pribadi untuk Outbound + Camping 2 Hari</h3>
                <div class="news-meta">
                  <span>9 Sep 2026</span>
                  <span class="dot"></span>
                  <span>Camping Gear</span>
                </div>
              </div>
            </a>

          </div>
        </div>"""

content = re.sub(
    r'<!-- 1\. TOP NEWS MAGAZINE MOSAIC.*?</div>\s*</div>',
    new_mosaic,
    content,
    flags=re.DOTALL
)

# 4. Remove any duplicate previous cards if any, and place the 3 new cards cleanly at the top of #newsArticlesGrid
new_feed_cards = """              <!-- 1. Peran Karakter & Soft Skills (10 Sep 2026) -->
              <article class="news-article-card" data-category="outbound-sekolah">
                <div class="news-card-thumb-wrap">
                  <img src="assets/image/blog/peran-karakter-soft-skills-kesiapan-kerja-hero.webp"
                    alt="Peran Karakter dan Soft Skills dalam Kesiapan Kerja Lulusan Sekolah" class="news-card-thumb" loading="lazy">
                </div>
                <div class="news-card-body">
                  <div class="news-card-meta">
                    <span class="news-badge badge-maroon" style="padding:3px 8px;font-size:0.68rem;margin:0;">OUTBOUND PELAJAR</span>
                    <span>&bull;</span>
                    <span>10 Sep 2026</span>
                  </div>
                  <h4 class="news-card-title">
                    <a href="blog/peran-karakter-soft-skills-kesiapan-kerja.html">Peran Karakter &amp; Soft Skills dalam Kesiapan Memasuki Dunia Kerja bagi Lulusan Sekolah</a>
                  </h4>
                  <p class="news-card-excerpt">
                    Membahas pentingnya adaptabilitas, pemecahan masalah, dan kerja sama tim dalam menjembatani kesiapan transisi siswa menuju dunia industri melalui simulasi luar ruang.
                  </p>
                  <div class="news-card-footer">
                    <span style="font-size:0.75rem;color:#888;"><i class="far fa-user"></i> Arby Ardiansyah</span>
                    <a href="blog/peran-karakter-soft-skills-kesiapan-kerja.html" class="news-card-readmore">Baca
                      Selengkapnya &rarr;</a>
                  </div>
                </div>
              </article>

              <!-- 2. 5 Manfaat Outbound vs Seminar Motivasi (10 Sep 2026) -->
              <article class="news-article-card" data-category="outbound-sekolah">
                <div class="news-card-thumb-wrap">
                  <img src="assets/image/blog/manfaat-outbound-vs-seminar-motivasi-siswa-hero.webp"
                    alt="5 Manfaat Nyata Outbound Dibandingkan Seminar Motivasi Ruangan Bagi Siswa" class="news-card-thumb" loading="lazy">
                </div>
                <div class="news-card-body">
                  <div class="news-card-meta">
                    <span class="news-badge badge-emerald" style="padding:3px 8px;font-size:0.68rem;margin:0;">EDUKASI SISWA</span>
                    <span>&bull;</span>
                    <span>10 Sep 2026</span>
                  </div>
                  <h4 class="news-card-title">
                    <a href="blog/manfaat-outbound-vs-seminar-motivasi-siswa.html">5 Manfaat Nyata Outbound Dibandingkan Seminar Motivasi Ruangan Bagi Siswa</a>
                  </h4>
                  <p class="news-card-excerpt">
                    Mengapa siswa lebih mudah mengingat dan menginternalisasi pembelajaran melalui pengalaman aktif ketimbang ceramah di aula? Simak analisis komparatifnya.
                  </p>
                  <div class="news-card-footer">
                    <span style="font-size:0.75rem;color:#888;"><i class="far fa-user"></i> Arby Ardiansyah</span>
                    <a href="blog/manfaat-outbound-vs-seminar-motivasi-siswa.html" class="news-card-readmore">Baca
                      Selengkapnya &rarr;</a>
                  </div>
                </div>
              </article>

              <!-- 3. Jasa Fasilitator Outbound Edukasi (10 Sep 2026) -->
              <article class="news-article-card" data-category="outbound-sekolah">
                <div class="news-card-thumb-wrap">
                  <img src="assets/image/blog/jasa-fasilitator-outbound-edukasi-sekolah-kampus-hero.webp"
                    alt="Jasa Fasilitator Outbound Edukasi Terpercaya untuk Sekolah dan Kampus" class="news-card-thumb" loading="lazy">
                </div>
                <div class="news-card-body">
                  <div class="news-card-meta">
                    <span class="news-badge badge-gold" style="padding:3px 8px;font-size:0.68rem;margin:0;">PAKET SEKOLAH</span>
                    <span>&bull;</span>
                    <span>10 Sep 2026</span>
                  </div>
                  <h4 class="news-card-title">
                    <a href="blog/jasa-fasilitator-outbound-edukasi-sekolah-kampus.html">Jasa Fasilitator Outbound Edukasi Terpercaya untuk Sekolah &amp; Kampus</a>
                  </h4>
                  <p class="news-card-excerpt">
                    Panduan memilih instruktur profesional untuk merancang paket outbound edukatif yang aman, terarah, dan ramah bagi peserta didik sekolah maupun perguruan tinggi.
                  </p>
                  <div class="news-card-footer">
                    <span style="font-size:0.75rem;color:#888;"><i class="far fa-user"></i> Arby Ardiansyah</span>
                    <a href="blog/jasa-fasilitator-outbound-edukasi-sekolah-kampus.html" class="news-card-readmore">Baca
                      Selengkapnya &rarr;</a>
                  </div>
                </div>
              </article>
"""

# Remove old card insertion if any
content = re.sub(r'<!-- Card H-10.*?<!-- 1\. Manajemen Risiko', '<!-- 1. Manajemen Risiko', content, flags=re.DOTALL)

# Insert the news-article-cards cleanly at the top of #newsArticlesGrid
content = re.sub(
    r'(<div class="news-unified-grid" id="newsArticlesGrid">\s*)',
    r'\1' + new_feed_cards,
    content,
    count=1
)

with open(blog_file, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Cleanly updated: {blog_file}")
