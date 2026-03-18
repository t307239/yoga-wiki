#!/usr/bin/env python3
"""
Yoga Wiki Quality Test Suite
Usage: python3 scripts/test_wiki_quality.py
       python3 -m pytest scripts/test_wiki_quality.py -v  (pytest optional)
"""

import os
import re
import glob
import unittest
import xml.etree.ElementTree as ET
from html.parser import HTMLParser

# ── Paths ──────────────────────────────────────────────────────────────────────
WIKI_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
EN_DIR  = os.path.join(WIKI_ROOT, "en")
JA_DIR  = os.path.join(WIKI_ROOT, "ja")
PT_DIR  = os.path.join(WIKI_ROOT, "pt")
SITEMAP = os.path.join(WIKI_ROOT, "sitemap.xml")
STYLE_CSS = os.path.join(WIKI_ROOT, "style.css")

LANGS = {"en": EN_DIR, "ja": JA_DIR, "pt": PT_DIR}
BJJ_APP_URL = "bjj-app-one.vercel.app"
SAMPLE_SIZE = 60


# ── Helpers ────────────────────────────────────────────────────────────────────

def all_html_files(lang_dir: str) -> list[str]:
    return sorted(glob.glob(os.path.join(lang_dir, "*.html")))


def sampled(files: list[str], n: int = SAMPLE_SIZE) -> list[str]:
    if len(files) <= n:
        return files
    step = max(1, len(files) // n)
    return files[::step][:n]


def read(path: str) -> str:
    with open(path, encoding="utf-8") as f:
        return f.read()


class MetaParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self._in_title = False
        self.description = ""
        self.lang = ""
        self.hreflang: set[str] = set()
        self.stylesheets: list[str] = []

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag == "html":
            self.lang = d.get("lang", "")
        if tag == "title":
            self._in_title = True
        if tag == "meta" and d.get("name", "").lower() == "description":
            self.description = d.get("content", "")
        if tag == "link":
            if d.get("rel") == "alternate" and d.get("hreflang"):
                self.hreflang.add(d["hreflang"])
            if d.get("rel") == "stylesheet":
                self.stylesheets.append(d.get("href", ""))

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False

    def handle_data(self, data):
        if self._in_title:
            self.title += data


def parse(path: str) -> MetaParser:
    p = MetaParser()
    p.feed(read(path))
    return p


# ── Tests ──────────────────────────────────────────────────────────────────────

class TestStyleCssExists(unittest.TestCase):
    """style.css must exist at the wiki root (required by batch-generated pages)."""

    def test_style_css_exists(self):
        self.assertTrue(os.path.exists(STYLE_CSS),
            f"style.css が存在しない: {STYLE_CSS}")

    def test_style_css_has_step_classes(self):
        """CSS must define .step-num, .step-item, .steps-list for numbered steps."""
        content = read(STYLE_CSS)
        for cls in [".step-num", ".step-item", ".steps-list"]:
            self.assertIn(cls, content,
                f"style.css に {cls} クラスが定義されていない")

    def test_style_css_has_cta_class(self):
        content = read(STYLE_CSS)
        self.assertIn(".cta-button", content, "style.css に .cta-button クラスなし")


class TestSitemapConsistency(unittest.TestCase):

    def _count_sitemap_urls(self) -> int:
        tree = ET.parse(SITEMAP)
        root = tree.getroot()
        ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        return len(root.findall("sm:url", ns))

    def test_sitemap_file_exists(self):
        self.assertTrue(os.path.exists(SITEMAP))

    def test_sitemap_has_urls(self):
        count = self._count_sitemap_urls()
        self.assertGreater(count, 900, f"sitemap URLが少なすぎる: {count}")

    def test_three_langs_equal_file_count(self):
        counts = {lang: len(all_html_files(d)) for lang, d in LANGS.items()}
        self.assertEqual(counts["en"], counts["ja"],
            f"EN/JA ファイル数不一致: {counts}")
        self.assertEqual(counts["en"], counts["pt"],
            f"EN/PT ファイル数不一致: {counts}")

    def test_minimum_pose_count(self):
        """EN should have at least 350 pose pages."""
        en_count = len(all_html_files(EN_DIR))
        self.assertGreaterEqual(en_count, 350,
            f"EN ポーズ数不足: {en_count} (目標: 350+)")


class TestStylesheetLink(unittest.TestCase):
    """New-format pages (step-item + span) must link to ../style.css.

    Old-format pages use <div class="step"> with inline styles — those are OK.
    New-format pages use <li class="step-item"> without inline step CSS.
    """

    def _check_lang(self, lang: str, lang_dir: str):
        # Only flag pages that use the NEW format: step-item li (not inline div style)
        new_format_pages = [
            f for f in all_html_files(lang_dir)
            if "class=\"step-item\"" in read(f) or "class='step-item'" in read(f)
        ]
        failures = []
        for path in new_format_pages:
            m = parse(path)
            uses_style_css = any("style.css" in s for s in m.stylesheets)
            if not uses_style_css:
                failures.append(os.path.basename(path))
        if failures:
            self.fail(
                f"[{lang}] step-item使用ページがstyle.cssをlinkしていない "
                f"({len(failures)}/{len(new_format_pages)}): {failures[:5]}")

    def test_en_stylesheet(self): self._check_lang("en", EN_DIR)
    def test_ja_stylesheet(self): self._check_lang("ja", JA_DIR)
    def test_pt_stylesheet(self): self._check_lang("pt", PT_DIR)


class TestStepStructure(unittest.TestCase):
    """Pages with steps must use span.step-num + span for text (not raw text)."""

    # Pattern that would indicate broken rendering: digit immediately followed by text
    BROKEN_PATTERN = re.compile(r'<li[^>]*>\d+[A-Za-zぁ-ん一-龥]')

    def _check_lang(self, lang: str, lang_dir: str):
        step_pages = [f for f in all_html_files(lang_dir)
                      if "step-num" in read(f)]
        failures = []
        for path in step_pages:
            content = read(path)
            if self.BROKEN_PATTERN.search(content):
                failures.append(os.path.basename(path))
        if failures:
            self.fail(
                f"[{lang}] ステップ番号が直接テキストに連結されているページ "
                f"({len(failures)}件): {failures[:5]}")

    def test_en_step_structure(self): self._check_lang("en", EN_DIR)
    def test_ja_step_structure(self): self._check_lang("ja", JA_DIR)
    def test_pt_step_structure(self): self._check_lang("pt", PT_DIR)


class TestMetaTags(unittest.TestCase):

    def _check_lang(self, lang: str, lang_dir: str):
        files = sampled(all_html_files(lang_dir))
        missing_title = []
        missing_desc = []
        for path in files:
            m = parse(path)
            name = os.path.basename(path)
            if not m.title.strip():
                missing_title.append(name)
            if not m.description.strip():
                missing_desc.append(name)
        if missing_title:
            self.fail(f"[{lang}] title 欠落: {missing_title[:5]}")
        if missing_desc:
            self.fail(f"[{lang}] meta description 欠落: {missing_desc[:5]}")

    def test_en_meta(self): self._check_lang("en", EN_DIR)
    def test_ja_meta(self): self._check_lang("ja", JA_DIR)
    def test_pt_meta(self): self._check_lang("pt", PT_DIR)


class TestHtmlLangAttribute(unittest.TestCase):

    EXPECTED_PREFIX = {"en": "en", "ja": "ja", "pt": "pt"}

    def _check_lang(self, lang: str, lang_dir: str):
        prefix = self.EXPECTED_PREFIX[lang]
        files = sampled(all_html_files(lang_dir))
        failures = []
        for path in files:
            m = parse(path)
            if not m.lang.startswith(prefix):
                failures.append(
                    f"{os.path.basename(path)}: lang='{m.lang}'")
        if failures:
            self.fail(
                f"[{lang}] html[lang] 不正 ({len(failures)}/{len(files)}): "
                + "\n".join(failures[:5]))

    def test_en_lang_attr(self): self._check_lang("en", EN_DIR)
    def test_ja_lang_attr(self): self._check_lang("ja", JA_DIR)
    def test_pt_lang_attr(self): self._check_lang("pt", PT_DIR)


class TestNoMojibake(unittest.TestCase):

    PATTERNS = ["Ã©", "Ã¨", "Ã£", "â€™", "â€œ", "Â "]

    def _check_lang(self, lang: str, lang_dir: str):
        files = sampled(all_html_files(lang_dir))
        hits = []
        for path in files:
            content = read(path)
            found = [p for p in self.PATTERNS if p in content]
            if found:
                hits.append(f"{os.path.basename(path)}: {found[:2]}")
        if hits:
            self.fail(f"[{lang}] mojibake 検出 ({len(hits)}/{len(files)}): {hits[:5]}")

    def test_en_mojibake(self): self._check_lang("en", EN_DIR)
    def test_ja_mojibake(self): self._check_lang("ja", JA_DIR)
    def test_pt_mojibake(self): self._check_lang("pt", PT_DIR)


class TestCtaBanner(unittest.TestCase):
    """Pose pages should include BJJ App CTA link."""

    def _check_lang(self, lang: str, lang_dir: str):
        files = sampled(all_html_files(lang_dir))
        missing = []
        for path in files:
            content = read(path)
            if BJJ_APP_URL not in content:
                missing.append(os.path.basename(path))
        # Allow up to 10% to be missing (some old format pages)
        threshold = max(3, len(files) * 0.10)
        if len(missing) > threshold:
            self.fail(
                f"[{lang}] BJJ App CTA 欠落が多い "
                f"({len(missing)}/{len(files)}): {missing[:5]}")

    def test_en_cta(self): self._check_lang("en", EN_DIR)
    def test_ja_cta(self): self._check_lang("ja", JA_DIR)
    def test_pt_cta(self): self._check_lang("pt", PT_DIR)


class TestBrokenPlaceholders(unittest.TestCase):
    """Generated pages must not contain unfilled template placeholders."""

    PLACEHOLDER_PATTERNS = [
        r"\{EnglishName\}",         # unfilled variable in instruction text
        r"\{TOPIC_TITLE\}",         # script variable leak
        r"\{\{[A-Za-z_]+\}\}",     # double-brace template leak
    ]

    def _check_lang(self, lang: str, lang_dir: str):
        combined = re.compile("|".join(self.PLACEHOLDER_PATTERNS))
        files = sampled(all_html_files(lang_dir))
        hits = []
        for path in files:
            content = read(path)
            if combined.search(content):
                hits.append(os.path.basename(path))
        if hits:
            self.fail(
                f"[{lang}] テンプレート変数が未置換 ({len(hits)}/{len(files)}): "
                f"{hits[:5]}")

    def test_en_placeholders(self): self._check_lang("en", EN_DIR)
    def test_ja_placeholders(self): self._check_lang("ja", JA_DIR)
    def test_pt_placeholders(self): self._check_lang("pt", PT_DIR)


class TestLangNav(unittest.TestCase):
    """Pages should have language navigation links."""

    def _check_lang(self, lang: str, lang_dir: str):
        files = sampled(all_html_files(lang_dir))
        missing = []
        for path in files:
            content = read(path)
            # Check for links to other language versions
            has_lang_nav = (
                ("/en/" in content or "href=\"../en" in content) and
                ("/ja/" in content or "href=\"../ja" in content) and
                ("/pt/" in content or "href=\"../pt" in content)
            )
            if not has_lang_nav:
                missing.append(os.path.basename(path))
        threshold = max(5, len(files) * 0.15)
        if len(missing) > threshold:
            self.fail(
                f"[{lang}] 言語ナビ欠落が多い "
                f"({len(missing)}/{len(files)}): {missing[:5]}")

    def test_en_lang_nav(self): self._check_lang("en", EN_DIR)
    def test_ja_lang_nav(self): self._check_lang("ja", JA_DIR)
    def test_pt_lang_nav(self): self._check_lang("pt", PT_DIR)


class TestDuplicateTitles(unittest.TestCase):
    """JA/PT titles should differ from EN titles."""

    def _check_different_from_en(self, compare_lang: str, compare_dir: str):
        en_titles: dict[str, str] = {}
        for path in sampled(all_html_files(EN_DIR)):
            en_titles[os.path.basename(path)] = parse(path).title.strip()

        duplicates = []
        for path in sampled(all_html_files(compare_dir)):
            name = os.path.basename(path)
            cmp_title = parse(path).title.strip()
            en_title = en_titles.get(name, "")
            if en_title and cmp_title == en_title:
                duplicates.append(name)

        if duplicates:
            self.fail(
                f"[{compare_lang}] タイトルがENと同一 ({len(duplicates)}件): "
                f"{duplicates[:5]}")

    def test_ja_titles_differ_from_en(self):
        self._check_different_from_en("ja", JA_DIR)

    def test_pt_titles_differ_from_en(self):
        self._check_different_from_en("pt", PT_DIR)


# ── Entry point ────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(__import__(__name__))
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    exit(0 if result.wasSuccessful() else 1)
