import re

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if '<img' in line:
        context = "".join(lines[max(0, i-2):min(len(lines), i+3)])
        print(f"Line {i+1}:")
        print(context.strip())
        print("-" * 50)
