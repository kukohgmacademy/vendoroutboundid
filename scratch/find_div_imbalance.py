import re

content = open("blog.html", "r", encoding="utf-8").read()

# Let's inspect news-mosaic-grid
mosaic_match = re.search(r'(<!-- 1\. TOP NEWS MAGAZINE MOSAIC.*?<!-- 2\. MAIN 2-COLUMN)', content, re.DOTALL)
if mosaic_match:
    block = mosaic_match.group(1)
    opens = len(re.findall(r'<div[\s>]', block))
    closes = len(re.findall(r'</div>', block))
    print(f"Mosaic block: opens={opens}, closes={closes}")
    print(block[-200:])

# Let's inspect newsArticlesGrid
grid_match = re.search(r'(<div class="news-unified-grid" id="newsArticlesGrid">.*?<!-- UNIFIED ARTICLES GRID END / SIDEBAR -->)', content, re.DOTALL)
if grid_match:
    block = grid_match.group(1)
    opens = len(re.findall(r'<div[\s>]', block))
    closes = len(re.findall(r'</div>', block))
    print(f"Grid block: opens={opens}, closes={closes}")
