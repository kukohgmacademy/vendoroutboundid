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
                # print(f"Closed {opener_text} (from {opener_line}) at {idx}")
        else:
            stack.append((idx, t))

print(f"Remaining open tags: {len(stack)}")
for idx, t in stack:
    print(f"  Line {idx}: {t}")
