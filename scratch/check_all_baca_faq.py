import glob
import re

files = glob.glob('blog/*.html')

print("Checking baca-juga and faq structure across blog files...")

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    baca_classes = re.findall(r'<div class="([^"]*baca[^"]*)"', content, re.IGNORECASE)
    faq_classes = re.findall(r'<div class="([^"]*faq[^"]*)"', content, re.IGNORECASE)
    
    baca_boxes = re.findall(r'<div class="baca-juga[^"]*">.*?</div>\s*</div>', content, re.DOTALL)
    
    # Check sample baca structure
    baca_sample = baca_boxes[0].strip().replace('\n', ' ')[:100] if baca_boxes else 'NONE'
    
    # Check faq structure
    faq_match = re.search(r'<div class="faq-item">.*?<button[^>]*class="([^"]*)"', content, re.DOTALL)
    faq_btn_class = faq_match.group(1) if faq_match else 'NONE'
    
    faq_h3 = re.search(r'<div class="faq-section"[^>]*>\s*<h3[^>]*>(.*?)</h3>', content, re.DOTALL)
    faq_h3_text = faq_h3.group(1).strip() if faq_h3 else 'NONE'

    if 'pentingnya-manajemen' in fpath or 'peran-karakter' in fpath or 'manfaat-outbound' in fpath or 'jasa-fasilitator' in fpath or 'pentingnya-melatih' in fpath:
        print(f"\nFile: {fpath}")
        print(f"  Baca boxes count: {len(baca_boxes)}")
        print(f"  Baca sample: {baca_sample}")
        print(f"  FAQ button class: {faq_btn_class}")
        print(f"  FAQ H3: {faq_h3_text}")
