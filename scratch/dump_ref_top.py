with open('blog/pentingnya-manajemen-risiko-outbound-terbuka.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines[:300]):
    print(f"{i+1}: {line}", end="")
