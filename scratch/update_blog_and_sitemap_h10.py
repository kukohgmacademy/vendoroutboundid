import re
import xml.etree.ElementTree as ET

# 1. Update blog.html
blog_file = "blog.html"
with open(blog_file, "r", encoding="utf-8") as f:
    blog_content = f.read()

# Update Top Mosaic
mosaic_new = """      <!-- FEATURED MAGAZINE MOSAIC (3 Top Latest Articles - 10 September 2026) -->
      <div class="mosaic-grid">
        <!-- Main Lead Feature (Article 1) -->
        <article class="mosaic-card mosaic-card--lead">
          <img src="assets/image/blog/peran-karakter-soft-skills-kesiapan-kerja-hero.webp"
            alt="Peran Karakter dan Soft Skills dalam Kesiapan Memasuki Dunia Kerja bagi Lulusan Sekolah"
            class="mosaic-img" loading="eager" fetchpriority="high">
          <div class="mosaic-overlay"></div>
          <div class="mosaic-content">
            <div class="mosaic-meta-top">
              <span class="mosaic-badge mosaic-badge--hot"><i class="fas fa-fire"></i> Edukasi &amp; Soft Skills</span>
              <span class="mosaic-date"><i class="far fa-calendar-alt"></i> 10 Sep 2026</span>
            </div>
            <h2 class="mosaic-title">
              <a href="blog/peran-karakter-soft-skills-kesiapan-kerja.html">Peran Karakter &amp; Soft Skills dalam Kesiapan Memasuki Dunia Kerja bagi Lulusan Sekolah</a>
            </h2>
            <p class="mosaic-excerpt">
              Mengapa penguasaan nilai akademis saja belum cukup? Ulasan komprehensif mengasah problem solving, adaptabilitas, dan kolaborasi tim siswa lewat simulasi luar ruang.
            </p>
            <div class="mosaic-author">
              <div class="mosaic-avatar"><i class="fas fa-user-edit"></i></div>
              <span class="mosaic-by">Oleh <strong>Arby Ardiansyah</strong> &bull; 8 min baca</span>
            </div>
          </div>
        </article>

        <!-- Secondary Side Feature 1 (Article 2) -->
        <article class="mosaic-card mosaic-card--sub">
          <img src="assets/image/blog/manfaat-outbound-vs-seminar-motivasi-siswa-hero.webp"
            alt="5 Manfaat Nyata Outbound Dibandingkan Seminar Motivasi Ruangan Bagi Siswa"
            class="mosaic-img" loading="lazy">
          <div class="mosaic-overlay"></div>
          <div class="mosaic-content">
            <div class="mosaic-meta-top">
              <span class="mosaic-badge mosaic-badge--primary"><i class="fas fa-school"></i> Karakter Siswa</span>
              <span class="mosaic-date"><i class="far fa-calendar-alt"></i> 10 Sep 2026</span>
            </div>
            <h3 class="mosaic-title">
              <a href="blog/manfaat-outbound-vs-seminar-motivasi-siswa.html">5 Manfaat Nyata Outbound Dibandingkan Seminar Motivasi Ruangan Bagi Siswa</a>
            </h3>
            <div class="mosaic-author">
              <span class="mosaic-by">Oleh <strong>Arby Ardiansyah</strong> &bull; 8 min baca</span>
            </div>
          </div>
        </article>

        <!-- Secondary Side Feature 2 (Article 3) -->
        <article class="mosaic-card mosaic-card--sub">
          <img src="assets/image/blog/jasa-fasilitator-outbound-edukasi-sekolah-kampus-hero.webp"
            alt="Jasa Fasilitator Outbound Edukasi Terpercaya untuk Sekolah dan Kampus"
            class="mosaic-img" loading="lazy">
          <div class="mosaic-overlay"></div>
          <div class="mosaic-content">
            <div class="mosaic-meta-top">
              <span class="mosaic-badge mosaic-badge--trending"><i class="fas fa-chalkboard-teacher"></i> Fasilitator Edukasi</span>
              <span class="mosaic-date"><i class="far fa-calendar-alt"></i> 10 Sep 2026</span>
            </div>
            <h3 class="mosaic-title">
              <a href="blog/jasa-fasilitator-outbound-edukasi-sekolah-kampus.html">Jasa Fasilitator Outbound Edukasi Terpercaya untuk Sekolah &amp; Kampus</a>
            </h3>
            <div class="mosaic-author">
              <span class="mosaic-by">Oleh <strong>Arby Ardiansyah</strong> &bull; 8 min baca</span>
            </div>
          </div>
        </article>
      </div>"""

blog_content = re.sub(
    r'<!-- FEATURED MAGAZINE MOSAIC.*?</div>\s*</div>',
    mosaic_new + "\n      </div>",
    blog_content,
    flags=re.DOTALL
)

# New 3 cards for grid
cards_new = """        <!-- Card H-10 1 -->
        <article class="article-card" data-category="sekolah">
          <div class="article-card-thumb">
            <img src="assets/image/blog/peran-karakter-soft-skills-kesiapan-kerja-hero.webp"
              alt="Peran Karakter dan Soft Skills dalam Kesiapan Kerja Lulusan Sekolah"
              loading="lazy" width="600" height="338">
            <span class="card-badge"><i class="fas fa-graduation-cap"></i> Outbound Pelajar</span>
          </div>
          <div class="article-card-body">
            <div class="article-card-meta">
              <span><i class="far fa-calendar-alt"></i> 10 Sep 2026</span>
              <span><i class="far fa-clock"></i> 8 Min Baca</span>
            </div>
            <h3 class="article-card-title">
              <a href="blog/peran-karakter-soft-skills-kesiapan-kerja.html">Peran Karakter &amp; Soft Skills dalam Kesiapan Memasuki Dunia Kerja bagi Lulusan Sekolah</a>
            </h3>
            <p class="article-card-excerpt">
              Membahas pentingnya adaptabilitas, penyelesaian masalah, dan kerja sama tim dalam menjembatani kesiapan transisi siswa menuju dunia industri.
            </p>
            <div class="article-card-footer">
              <span class="article-card-author"><i class="far fa-user"></i> Arby Ardiansyah</span>
              <a href="blog/peran-karakter-soft-skills-kesiapan-kerja.html" class="article-card-readmore">Baca Selengkapnya <i class="fas fa-arrow-right"></i></a>
            </div>
          </div>
        </article>

        <!-- Card H-10 2 -->
        <article class="article-card" data-category="sekolah">
          <div class="article-card-thumb">
            <img src="assets/image/blog/manfaat-outbound-vs-seminar-motivasi-siswa-hero.webp"
              alt="5 Manfaat Nyata Outbound Dibandingkan Seminar Motivasi Ruangan Bagi Siswa"
              loading="lazy" width="600" height="338">
            <span class="card-badge"><i class="fas fa-school"></i> Edukasi Siswa</span>
          </div>
          <div class="article-card-body">
            <div class="article-card-meta">
              <span><i class="far fa-calendar-alt"></i> 10 Sep 2026</span>
              <span><i class="far fa-clock"></i> 8 Min Baca</span>
            </div>
            <h3 class="article-card-title">
              <a href="blog/manfaat-outbound-vs-seminar-motivasi-siswa.html">5 Manfaat Nyata Outbound Dibandingkan Seminar Motivasi Ruangan Bagi Siswa</a>
            </h3>
            <p class="article-card-excerpt">
              Mengapa siswa lebih mudah mengingat pembelajaran melalui pengalaman langsung ketimbang ceramah di aula? Simak analisis komparatifnya.
            </p>
            <div class="article-card-footer">
              <span class="article-card-author"><i class="far fa-user"></i> Arby Ardiansyah</span>
              <a href="blog/manfaat-outbound-vs-seminar-motivasi-siswa.html" class="article-card-readmore">Baca Selengkapnya <i class="fas fa-arrow-right"></i></a>
            </div>
          </div>
        </article>

        <!-- Card H-10 3 -->
        <article class="article-card" data-category="sekolah">
          <div class="article-card-thumb">
            <img src="assets/image/blog/jasa-fasilitator-outbound-edukasi-sekolah-kampus-hero.webp"
              alt="Jasa Fasilitator Outbound Edukasi Terpercaya untuk Sekolah dan Kampus"
              loading="lazy" width="600" height="338">
            <span class="card-badge"><i class="fas fa-chalkboard-teacher"></i> Paket Sekolah</span>
          </div>
          <div class="article-card-body">
            <div class="article-card-meta">
              <span><i class="far fa-calendar-alt"></i> 10 Sep 2026</span>
              <span><i class="far fa-clock"></i> 8 Min Baca</span>
            </div>
            <h3 class="article-card-title">
              <a href="blog/jasa-fasilitator-outbound-edukasi-sekolah-kampus.html">Jasa Fasilitator Outbound Edukasi Terpercaya untuk Sekolah &amp; Kampus</a>
            </h3>
            <p class="article-card-excerpt">
              Panduan memilih instruktur berpengalaman untuk merancang paket outbound edukatif yang aman, terarah, dan ramah bagi peserta didik.
            </p>
            <div class="article-card-footer">
              <span class="article-card-author"><i class="far fa-user"></i> Arby Ardiansyah</span>
              <a href="blog/jasa-fasilitator-outbound-edukasi-sekolah-kampus.html" class="article-card-readmore">Baca Selengkapnya <i class="fas fa-arrow-right"></i></a>
            </div>
          </div>
        </article>
"""

# Insert at top of newsArticlesGrid
blog_content = re.sub(
    r'(<div class="articles-grid" id="newsArticlesGrid">)',
    r'\1\n' + cards_new,
    blog_content,
    count=1
)

with open(blog_file, "w", encoding="utf-8") as f:
    f.write(blog_content)
print(f"Updated: {blog_file}")

# 2. Update sitemap.xml
sitemap_file = "sitemap.xml"
with open(sitemap_file, "r", encoding="utf-8") as f:
    sitemap_content = f.read()

new_urls = """  <url>
    <loc>https://venroroutbound.id/blog/jasa-fasilitator-outbound-edukasi-sekolah-kampus.html</loc>
    <lastmod>2026-09-10</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://venroroutbound.id/blog/manfaat-outbound-vs-seminar-motivasi-siswa.html</loc>
    <lastmod>2026-09-10</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://venroroutbound.id/blog/peran-karakter-soft-skills-kesiapan-kerja.html</loc>
    <lastmod>2026-09-10</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
</urlset>"""

sitemap_content = re.sub(r'</urlset>', new_urls, sitemap_content)

with open(sitemap_file, "w", encoding="utf-8") as f:
    f.write(sitemap_content)
print(f"Updated: {sitemap_file}")
