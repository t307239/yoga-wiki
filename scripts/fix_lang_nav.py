#!/usr/bin/env python3
"""
Add language navigation links to pages that are missing them.
Adds after <header> or after <body> tag if no header.
"""
import os, re, glob

WIKI_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

LANG_NAV_EN = """<nav>
  <a href="../en/">← All Poses</a>
  <a href="../en/">EN</a> <a href="../ja/">JA</a> <a href="../pt/">PT</a>
</nav>"""

LANG_NAV_JA = """<nav>
  <a href="../ja/">← ポーズ一覧</a>
  <a href="../en/">EN</a> <a href="../ja/">JA</a> <a href="../pt/">PT</a>
</nav>"""

LANG_NAV_PT = """<nav>
  <a href="../pt/">← Todas as Poses</a>
  <a href="../en/">EN</a> <a href="../ja/">JA</a> <a href="../pt/">PT</a>
</nav>"""

def has_lang_nav(content):
    return ("/ja/" in content or 'href="../ja' in content) and \
           ("/en/" in content or 'href="../en' in content) and \
           ("/pt/" in content or 'href="../pt' in content)

def add_lang_nav(content, nav_html):
    """Insert lang nav after </header> or after <body> if no header."""
    # Try after </header>
    if "</header>" in content:
        return content.replace("</header>", f"</header>\n{nav_html}", 1)
    # Try after <body>
    m = re.search(r'<body[^>]*>', content)
    if m:
        pos = m.end()
        return content[:pos] + f"\n{nav_html}" + content[pos:]
    return content

def main():
    fixed = {"en": 0, "ja": 0, "pt": 0}
    
    for lang, nav in [("en", LANG_NAV_EN), ("ja", LANG_NAV_JA), ("pt", LANG_NAV_PT)]:
        lang_dir = os.path.join(WIKI_ROOT, lang)
        for f in sorted(glob.glob(os.path.join(lang_dir, "*.html"))):
            content = open(f, encoding="utf-8").read()
            if not has_lang_nav(content):
                new_content = add_lang_nav(content, nav)
                if new_content != content:
                    with open(f, "w", encoding="utf-8") as fout:
                        fout.write(new_content)
                    fixed[lang] += 1
    
    print(f"Fixed lang nav: EN={fixed['en']}, JA={fixed['ja']}, PT={fixed['pt']}")

if __name__ == "__main__":
    main()
