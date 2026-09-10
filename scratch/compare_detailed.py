import re
import difflib

with open('blog/pentingnya-manajemen-risiko-outbound-terbuka.html', 'r', encoding='utf-8') as f:
    ref = f.read()

with open('blog/peran-karakter-soft-skills-kesiapan-kerja.html', 'r', encoding='utf-8') as f:
    art1 = f.read()

print("=== HEAD TAGS COMPARISON ===")
head_ref = re.search(r'<head>(.*?)</head>', ref, re.DOTALL).group(1)
head_art1 = re.search(r'<head>(.*?)</head>', art1, re.DOTALL).group(1)

css_links_ref = re.findall(r'<link[^>]*stylesheet[^>]*>', head_ref)
css_links_art1 = re.findall(r'<link[^>]*stylesheet[^>]*>', head_art1)
print("CSS links ref:", css_links_ref)
print("CSS links art1:", css_links_art1)

inline_styles_ref = re.findall(r'<style[^>]*>(.*?)</style>', ref, re.DOTALL)
inline_styles_art1 = re.findall(r'<style[^>]*>(.*?)</style>', art1, re.DOTALL)
print("Inline styles ref count:", len(inline_styles_ref))
print("Inline styles art1 count:", len(inline_styles_art1))

if inline_styles_ref and inline_styles_art1:
    diff = list(difflib.unified_diff(inline_styles_ref[0].splitlines(), inline_styles_art1[0].splitlines()))
    print("Style diff:", len(diff))
    for d in diff[:20]:
        print(d)

scripts_ref = re.findall(r'<script(?![^>]*ld\+json)[^>]*>(.*?)</script>', ref, re.DOTALL)
scripts_art1 = re.findall(r'<script(?![^>]*ld\+json)[^>]*>(.*?)</script>', art1, re.DOTALL)
print("\nScripts diff:")
for i, (sr, sa) in enumerate(zip(scripts_ref, scripts_art1)):
    if sr.strip() != sa.strip():
        print(f"--- Script {i} diff ---")
        diff = list(difflib.unified_diff(sr.splitlines(), sa.splitlines(), lineterm=''))
        for l in diff:
            print(l)
