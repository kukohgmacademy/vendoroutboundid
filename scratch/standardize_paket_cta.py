import glob, re

files = sorted(glob.glob('paket/*.html'))
print(f"Standardizing CTA on {len(files)} files...")

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern to find cta-band-luxury and its inner content
    pattern = re.compile(
        r'<div class="cta-band-luxury"[^>]*>.*?'
        r'<div[^>]*style="[^"]*max-width:680px[^"]*"[^>]*>\s*'
        r'<div[^>]*>(.*?)</div>\s*'
        r'<h2[^>]*>(.*?)</h2>\s*'
        r'<p[^>]*>(.*?)</p>\s*'
        r'</div>\s*'
        r'<div[^>]*style="[^"]*flex-shrink:0[^"]*"[^>]*>\s*'
        r'<a href="([^"]+)"[^>]*>\s*'
        r'<i[^>]*class="([^"]*whatsapp[^"]*)"[^>]*></i>\s*'
        r'<span[^>]*>(.*?)</span>\s*'
        r'</a>\s*</div>\s*</div>',
        re.DOTALL | re.IGNORECASE
    )

    m = pattern.search(content)
    if m:
        badge_inner = m.group(1).strip()
        h2_inner = m.group(2).strip()
        p_inner = m.group(3).strip()
        href = m.group(4).strip()
        wa_class = m.group(5).strip()
        btn_text = m.group(6).strip()

        new_cta = f'''<div class="cta-band-luxury">
          <div class="cta-luxury-content">
            <div class="cta-luxury-badge">
              {badge_inner}
            </div>
            <h2 class="cta-luxury-title">{h2_inner}</h2>
            <p class="cta-luxury-desc">{p_inner}</p>
          </div>
          <div class="cta-luxury-action">
            <a href="{href}" target="_blank" rel="noopener" class="btn-wander-cta cta-luxury-btn">
              <i class="{wa_class}"></i>
              <span class="cta-luxury-btn-text">{btn_text}</span>
            </a>
          </div>
        </div>'''

        content = content[:m.start()] + new_cta + content[m.end():]
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"SUCCESS: {fpath}")
    else:
        print(f"PATTERN MISMATCH: {fpath}")
