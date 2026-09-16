import re

with open("blog.html", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Clean duplicated section comment
text = text.replace(
    """    <!-- ================= EDITORIAL NEWS PORTAL MAIN SECTION ================= -->
        <!-- ================= EDITORIAL NEWS PORTAL MAIN SECTION ================= -->""",
    """    <!-- ================= EDITORIAL NEWS PORTAL MAIN SECTION ================= -->"""
)

# 2. Fix the broken mosaic area
# Find start of news-mosaic-grid to start of news-body-layout
mosaic_match = re.search(r'(<!-- 1\. TOP NEWS MAGAZINE MOSAIC.*?)(<!-- 2\. MAIN 2-COLUMN EDITORIAL LAYOUT)', text, re.DOTALL)
if mosaic_match:
    current_mosaic = mosaic_match.group(1)
    print("Found mosaic length:", len(current_mosaic))
    
clean_mosaic = """<!-- 1. TOP NEWS MAGAZINE MOSAIC (1 Large + 4 Sub-Featured) -->
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
        </div>

        """

text = re.sub(r'<!-- 1\. TOP NEWS MAGAZINE MOSAIC.*?<!-- 2\. MAIN 2-COLUMN EDITORIAL LAYOUT', clean_mosaic + '<!-- 2. MAIN 2-COLUMN EDITORIAL LAYOUT', text, flags=re.DOTALL)

# Update Semua count to 48
text = text.replace('Semua (45)', 'Semua (48)')

# Ensure filter tabs include outbound-perusahaan
if 'data-filter="outbound-perusahaan"' not in text:
    old_pills = """              <div class="news-filter-pills" id="newsFilterPills">
                <button class="news-filter-btn active" data-filter="all"><i class="fas fa-layer-group"></i> Semua (48)</button>"""
    new_pills = """              <div class="news-filter-pills" id="newsFilterPills">
                <button class="news-filter-btn active" data-filter="all"><i class="fas fa-layer-group"></i> Semua (48)</button>
                <button class="news-filter-btn" data-filter="outbound-perusahaan"><i class="fas fa-building"></i> Outbound Perusahaan</button>"""
    text = text.replace(old_pills, new_pills)

with open("blog.html", "w", encoding="utf-8") as f:
    f.write(text)

print("Replacement done. Re-checking tag balance...")

tags = ['div', 'section', 'article', 'a', 'header', 'footer', 'main']
for t in tags:
    open_count = len(re.findall(r'<' + t + r'[\s>]', text))
    close_count = len(re.findall(r'</' + t + r'>', text))
    print(f"{t}: open={open_count}, close={close_count}, diff={open_count - close_count}")
