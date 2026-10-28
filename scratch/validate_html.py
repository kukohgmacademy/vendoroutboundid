import glob, html.parser

class TagValidator(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.void_tags = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}
        self.errors = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() not in self.void_tags:
            self.stack.append((tag.lower(), self.getpos()))

    def handle_endtag(self, tag):
        tag_lower = tag.lower()
        if tag_lower in self.void_tags:
            return
        if not self.stack:
            self.errors.append(f"Unexpected closing tag </{tag}> at line {self.getpos()[0]}")
            return
        last_tag, pos = self.stack[-1]
        if last_tag == tag_lower:
            self.stack.pop()
        else:
            # Check if tag is in stack
            tag_names = [t[0] for t in self.stack]
            if tag_lower in tag_names:
                # Pop until matched
                while self.stack and self.stack[-1][0] != tag_lower:
                    unclosed, unclosed_pos = self.stack.pop()
                    self.errors.append(f"Unclosed <{unclosed}> from line {unclosed_pos[0]} before closing </{tag}> at line {self.getpos()[0]}")
                if self.stack:
                    self.stack.pop()
            else:
                self.errors.append(f"Mismatched closing tag </{tag}> at line {self.getpos()[0]} (expected </{last_tag}>)")

files = ['index.html', 'tentang-kami.html', 'paket.html', 'gallery.html'] + glob.glob('paket/*.html')
has_err = False
for f in files:
    v = TagValidator()
    with open(f, 'r', encoding='utf-8') as fp:
        try:
            v.feed(fp.read())
        except Exception as e:
            print(f"[ERROR] {f} parse failed: {e}")
            has_err = True
            continue
    # Filter critical errors (ignore unclosed <p> if any standard html allows)
    critical_errors = [e for e in v.errors if not e.startswith("Unclosed <p>")]
    if critical_errors:
        print(f"[FAIL] {f}: {len(critical_errors)} tag errors")
        for e in critical_errors[:3]:
            print(f"   {e}")
        has_err = True
    else:
        print(f"[PASS] {f}: HTML structure valid")

if not has_err:
    print("\nALL TARGET HTML FILES PASS VALIDATION!")
