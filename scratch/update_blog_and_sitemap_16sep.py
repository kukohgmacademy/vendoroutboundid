import re

# 1. Update blog.html
with open("blog.html", "r", encoding="utf-8") as f:
    blog_html = f.read()

# Update hero stat count 45 -> 48
blog_html = blog_html.replace(
    '<span class="subpage-hero-stat-num">45</span>',
    '<span class="subpage-hero-stat-num">48</span>'
)

# New Mosaic Section
new_mosaic = """        <!-- 1. TOP NEWS MAGAZINE MOSAIC (1 Large + 4 Sub-Featured) -->
        <div class="news-mosaic-grid">

          <!-- Left Large Featured Story (50% Width) - Artikel 1 (16 Sep 2026) -->
          <a href="blog/meruntuhkan-silo-mental-divisi-perusahaan.html" class="news-mosaic-item news-mosaic-main">
            <img src="assets/image/blog/meruntuhkan-silo-mental-divisi-perusahaan-hero.webp"
              alt="Strategi Meruntuhkan Silo Mental Antar Divisi Perusahaan Lewat Experiential Games" class="news-mosaic-bg" loading="eager" width="1600" height="900">
            <div class="news-mosaic-overlay"></div>
            <div class="news-mosaic-content">
              <span class="news-badge badge-maroon"><i class="fas fa-sitemap"></i> TEAM BUILDING &bull; TERBARU 16 SEP 2026</span>
              <h2 class="news-mosaic-title-main">Strategi Meruntuhkan Silo Mental Antar Divisi Perusahaan Lewat Experiential Games</h2>
              <div class="news-meta">
                <span>Arby Ardiansyah</span>
                <span class="dot"></span>
                <span>16 September 2026</span>
                <span class="dot"></span>
                <span>12 Menit Baca</span>
              </div>
            </div>
          </a>

          <!-- Right 2x2 Sub-Grid (4 Stories) -->
          <div class="news-mosaic-subgrid">

            <!-- Sub 1: Artikel 2 (16 Sep 2026) -->
            <a href="blog/mengukur-efektivitas-outbound-retensi-karyawan.html" class="news-mosaic-item news-mosaic-sub">
              <img src="assets/image/blog/mengukur-efektivitas-outbound-retensi-karyawan-hero.webp"
                alt="Mengukur Efektivitas Outbound Dalam Meningkatkan Retensi &amp; Engagement Karyawan" class="news-mosaic-bg" loading="lazy" width="1600" height="900">
              <div class="news-mosaic-overlay"></div>
              <div class="news-mosaic-content">
                <span class="news-badge badge-emerald"><i class="fas fa-chart-line"></i> HR ANALYTICS</span>
                <h3 class="news-mosaic-title-sub">Mengukur Efektivitas Outbound Dalam Meningkatkan Retensi &amp; Engagement</h3>
                <div class="news-meta">
                  <span>16 Sep 2026</span>
                  <span class="dot"></span>
                  <span>13 Menit Baca</span>
                </div>
              </div>
            </a>

            <!-- Sub 2: Artikel 3 (16 Sep 2026) -->
            <a href="blog/paket-outbound-corporate-synergy-engagement.html" class="news-mosaic-item news-mosaic-sub">
              <img src="assets/image/blog/paket-outbound-corporate-synergy-engagement-hero.webp"
                alt="Paket Outbound Corporate Synergy &amp; Employee Engagement Perusahaan 2026" class="news-mosaic-bg" loading="lazy" width="1600" height="900">
              <div class="news-mosaic-overlay"></div>
              <div class="news-mosaic-content">
                <span class="news-badge badge-gold"><i class="fas fa-handshake"></i> PAKET SYNERGY</span>
                <h3 class="news-mosaic-title-sub">Paket Outbound Corporate Synergy &amp; Employee Engagement 2026</h3>
                <div class="news-meta">
                  <span>16 Sep 2026</span>
                  <span class="dot"></span>
                  <span>12 Menit Baca</span>
                </div>
              </div>
            </a>

            <!-- Sub 3: Artikel 1 (15 Sep 2026) -->
            <a href="blog/membangun-resilience-tim-petualangan-offroad.html" class="news-mosaic-item news-mosaic-sub">
              <img src="assets/image/blog/membangun-resilience-tim-petualangan-offroad-hero.webp"
                alt="Membangun Resilience &amp; Ketangguhan Tim Lewat Petualangan Offroad" class="news-mosaic-bg" loading="lazy" width="1600" height="900">
              <div class="news-mosaic-overlay"></div>
              <div class="news-mosaic-content">
                <span class="news-badge badge-gold"><i class="fas fa-mountain"></i> OUTBOUND OFFROAD</span>
                <h3 class="news-mosaic-title-sub">Membangun Resilience &amp; Ketangguhan Tim Lewat Petualangan Offroad</h3>
                <div class="news-meta">
                  <span>15 Sep 2026</span>
                  <span class="dot"></span>
                  <span>9 Menit Baca</span>
                </div>
              </div>
            </a>

            <!-- Sub 4: Artikel 2 (15 Sep 2026) -->
            <a href="blog/tips-memilih-rute-offroad-aman-pemula.html" class="news-mosaic-item news-mosaic-sub">
              <img src="assets/image/blog/tips-memilih-rute-offroad-aman-pemula-hero.webp"
                alt="Tips Memilih Rute Offroad Yang Aman Untuk Pemula &amp; Rombongan Kantor" class="news-mosaic-bg" loading="lazy" width="1600" height="900">
              <div class="news-mosaic-overlay"></div>
              <div class="news-mosaic-content">
                <span class="news-badge badge-emerald"><i class="fas fa-route"></i> RUTE OFFROAD</span>
                <h3 class="news-mosaic-title-sub">Tips Memilih Rute Offroad Yang Aman Untuk Pemula &amp; Kantor</h3>
                <div class="news-meta">
                  <span>15 Sep 2026</span>
                  <span class="dot"></span>
                  <span>10 Menit Baca</span>
                </div>
              </div>
            </a>

          </div>
        </div>"""

mosaic_pattern = r'<!-- 1\. TOP NEWS MAGAZINE MOSAIC \(1 Large \+ 4 Sub-Featured\) -->\s*<div class="news-mosaic-grid">.*?</div>\s*</div>'
blog_html = re.sub(mosaic_pattern, new_mosaic, blog_html, flags=re.DOTALL)

# Insert 3 articles at top of #newsArticlesGrid
new_cards = """            <!-- UNIFIED ARTICLES GRID -->
            <div class="news-unified-grid" id="newsArticlesGrid">
              <!-- 16 Sep 2026 - H05 Artikel 1 -->
              <article class="news-article-card" data-category="outbound-perusahaan strategi-hr">
                <div class="news-card-thumb-wrap">
                  <img src="assets/image/blog/meruntuhkan-silo-mental-divisi-perusahaan-hero.webp"
                    alt="Strategi Meruntuhkan Silo Mental Antar Divisi Perusahaan Lewat Experiential Games" class="news-card-thumb"
                    loading="lazy" width="1600" height="900">
                </div>
                <div class="news-card-body">
                  <div class="news-card-meta">
                    <span class="news-badge badge-maroon" style="padding:3px 8px;font-size:0.68rem;margin:0;">TEAM BUILDING</span>
                    <span>&bull;</span>
                    <span>16 Sep 2026</span>
                  </div>
                  <h4 class="news-card-title">
                    <a href="blog/meruntuhkan-silo-mental-divisi-perusahaan.html">Strategi Meruntuhkan Silo Mental Antar Divisi Perusahaan Lewat Experiential Games</a>
                  </h4>
                  <p class="news-card-excerpt">
                    Kupas tuntas strategi meruntuhkan sekat antar departemen kerja melalui simulasi paralel terstruktur dan debrief reflektif yang relevan dengan dinamika kantor.
                  </p>
                  <div class="news-card-footer">
                    <span style="font-size:0.75rem;color:#888;"><i class="far fa-user"></i> Arby Ardiansyah</span>
                    <a href="blog/meruntuhkan-silo-mental-divisi-perusahaan.html" class="news-card-readmore">Baca Selengkapnya &rarr;</a>
                  </div>
                </div>
              </article>

              <!-- 16 Sep 2026 - H05 Artikel 2 -->
              <article class="news-article-card" data-category="outbound-perusahaan strategi-hr panduan-vendor">
                <div class="news-card-thumb-wrap">
                  <img src="assets/image/blog/mengukur-efektivitas-outbound-retensi-karyawan-hero.webp"
                    alt="Mengukur Efektivitas Outbound Dalam Meningkatkan Retensi &amp; Engagement Karyawan" class="news-card-thumb"
                    loading="lazy" width="1600" height="900">
                </div>
                <div class="news-card-body">
                  <div class="news-card-meta">
                    <span class="news-badge badge-emerald" style="padding:3px 8px;font-size:0.68rem;margin:0;">HR ANALYTICS</span>
                    <span>&bull;</span>
                    <span>16 Sep 2026</span>
                  </div>
                  <h4 class="news-card-title">
                    <a href="blog/mengukur-efektivitas-outbound-retensi-karyawan.html">Mengukur Efektivitas Outbound Dalam Meningkatkan Retensi &amp; Engagement Karyawan</a>
                  </h4>
                  <p class="news-card-excerpt">
                    Panduan lengkap HR mengukur efektivitas outbound team building melalui indikator kualitatif, survei CSAT, serta kerangka Before-During-After yang objektif.
                  </p>
                  <div class="news-card-footer">
                    <span style="font-size:0.75rem;color:#888;"><i class="far fa-user"></i> Arby Ardiansyah</span>
                    <a href="blog/mengukur-efektivitas-outbound-retensi-karyawan.html" class="news-card-readmore">Baca Selengkapnya &rarr;</a>
                  </div>
                </div>
              </article>

              <!-- 16 Sep 2026 - H05 Artikel 3 -->
              <article class="news-article-card" data-category="outbound-perusahaan panduan-vendor">
                <div class="news-card-thumb-wrap">
                  <img src="assets/image/blog/paket-outbound-corporate-synergy-engagement-hero.webp"
                    alt="Paket Outbound Corporate Synergy &amp; Employee Engagement Perusahaan 2026" class="news-card-thumb"
                    loading="lazy" width="1600" height="900">
                </div>
                <div class="news-card-body">
                  <div class="news-card-meta">
                    <span class="news-badge badge-gold" style="padding:3px 8px;font-size:0.68rem;margin:0;">PAKET CORPORATE</span>
                    <span>&bull;</span>
                    <span>16 Sep 2026</span>
                  </div>
                  <h4 class="news-card-title">
                    <a href="blog/paket-outbound-corporate-synergy-engagement.html">Paket Outbound Corporate Synergy &amp; Employee Engagement Perusahaan 2026</a>
                  </h4>
                  <p class="news-card-excerpt">
                    Pilihan modul komprehensif paket team building 1-day intensif maupun 2-day plus menginap untuk membangun sinergi lintas fungsi dan engagement kerja.
                  </p>
                  <div class="news-card-footer">
                    <span style="font-size:0.75rem;color:#888;"><i class="far fa-user"></i> Arby Ardiansyah</span>
                    <a href="blog/paket-outbound-corporate-synergy-engagement.html" class="news-card-readmore">Baca Selengkapnya &rarr;</a>
                  </div>
                </div>
              </article>"""

grid_target = """            <!-- UNIFIED ARTICLES GRID -->
            <div class="news-unified-grid" id="newsArticlesGrid">"""

if grid_target in blog_html:
    blog_html = blog_html.replace(grid_target, new_cards, 1)

with open("blog.html", "w", encoding="utf-8") as f:
    f.write(blog_html)

print("blog.html updated successfully!")

# 2. Update sitemap.xml
with open("sitemap.xml", "r", encoding="utf-8") as f:
    sitemap = f.read()

new_sitemap_urls = """  <url>
    <loc>https://venroroutbound.id/blog/meruntuhkan-silo-mental-divisi-perusahaan.html</loc>
    <lastmod>2026-09-16</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://venroroutbound.id/blog/mengukur-efektivitas-outbound-retensi-karyawan.html</loc>
    <lastmod>2026-09-16</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://venroroutbound.id/blog/paket-outbound-corporate-synergy-engagement.html</loc>
    <lastmod>2026-09-16</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
</urlset>"""

if "meruntuhkan-silo-mental-divisi-perusahaan.html" not in sitemap:
    sitemap = sitemap.replace("</urlset>", new_sitemap_urls)
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(sitemap)
    print("sitemap.xml updated with 3 new URLs!")
else:
    print("URLs already in sitemap.xml")
