import re

def check_div_tree(fpath):
    with open(fpath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    depth = 0
    stack = []
    print(f"\nChecking divs for {fpath}:")
    for idx, line in enumerate(lines, 1):
        tokens = re.findall(r'(<div\b[^>]*>|</div\b[^>]*>)', line, re.IGNORECASE)
        for t in tokens:
            if t.startswith('</'):
                if depth == 0:
                    print(f"  Line {idx}: EXTRA CLOSING DIV: {line.strip()}")
                else:
                    depth -= 1
                    stack.pop()
            else:
                depth += 1
                stack.append((idx, t[:40]))
    print(f"Final div depth: {depth}")
    if depth > 0:
        print("Unclosed divs opened at:")
        for line_num, tag in stack:
            print(f"  Line {line_num}: {tag}")

check_div_tree('blog/peran-karakter-soft-skills-kesiapan-kerja.html')
check_div_tree('blog/manfaat-outbound-vs-seminar-motivasi-siswa.html')
check_div_tree('blog/jasa-fasilitator-outbound-edukasi-sekolah-kampus.html')
