with open('blog/peran-karakter-soft-skills-kesiapan-kerja.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

import re

stack = []
for idx, line in enumerate(lines, 1):
    tokens = re.finditer(r'(<div\b[^>]*>|</div\b[^>]*>)', line, re.IGNORECASE)
    for m in tokens:
        t = m.group(0)
        if t.startswith('</'):
            if not stack:
                print(f"EXTRA CLOSE at line {idx}: {line.strip()}")
            else:
                opener_line, opener_text = stack.pop()
                if opener_line >= 480 or idx >= 480:
                    print(f"Line {opener_line:3d} ({opener_text[:30]}) closed at Line {idx:3d}")
        else:
            stack.append((idx, t))
