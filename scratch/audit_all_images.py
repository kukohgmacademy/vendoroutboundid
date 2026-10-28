import re, glob, os

pages_to_check = ['index.html', 'tentang-kami.html', 'paket.html', 'gallery.html'] + sorted(glob.glob('paket/*.html'))

print(f"Auditing {len(pages_to_check)} pages for image references...\n")

total_errors = 0
all_referenced_images = set()

for page in pages_to_check:
    with open(page, 'r', encoding='utf-8') as f:
        content = f.read()
    
    imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content)
    data_imgs = re.findall(r'data-img=["\']([^"\']+)["\']', content)
    
    combined = imgs + data_imgs
    page_errors = []
    
    for img_path in combined:
        if any(x in img_path.lower() for x in ['logo', 'icon', 'author-artikel', 'blog/']):
            continue
        if img_path.startswith('http'):
            continue
        
        all_referenced_images.add(img_path)
        
        if img_path.endswith('.jpg') and 'avatar' not in img_path and 'testi' not in img_path:
            page_errors.append(f"Old JPG found: {img_path}")
        if 'assets/image/paket/' in img_path:
            page_errors.append(f"Old path found: {img_path}")
        
        page_dir = os.path.dirname(page)
        rel_target = os.path.normpath(os.path.join(page_dir, img_path))
        if not os.path.exists(rel_target):
            page_errors.append(f"File NOT FOUND: {rel_target} (referenced as {img_path})")
        else:
            if rel_target.lower().endswith('.webp'):
                sz = os.path.getsize(rel_target) / 1024
                if sz > 100:
                    page_errors.append(f"OVER 100KB: {rel_target} ({sz:.1f} KB)")
    
    if page_errors:
        print(f"[FAIL] {page}:")
        for e in page_errors:
            print(f"   {e}")
        total_errors += len(page_errors)
    else:
        print(f"[PASS] {page}: OK")

print(f"\nTotal Errors: {total_errors}")
print(f"Total Unique Images Checked: {len(all_referenced_images)}")
