#!/usr/bin/env python3
"""
Fix duplicate titles in JA/PT pages that still have English titles.
JA format: "POSENAME（ヨガポーズ）完全ガイド｜効果・やり方・バリエーション"
PT format: "POSENAME - Guia Completo de Yoga | Benefícios e Instruções"
"""
import os, re, glob

WIKI_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def get_title(path):
    with open(path, encoding="utf-8") as f:
        content = f.read()
    m = re.search(r'<title>(.*?)</title>', content)
    return m.group(1).strip() if m else ""

def extract_pose_name(en_title):
    """Extract pose name from 'X Yoga Pose Guide | Yoga Wiki'"""
    t = en_title
    t = re.sub(r'\s*Yoga Pose Guide.*$', '', t)
    t = re.sub(r'\s*\|\s*Yoga Wiki.*$', '', t)
    return t.strip()

def fix_ja_title(content, pose_name):
    new_title = f"{pose_name}（ヨガポーズ）完全ガイド｜効果・やり方・バリエーション"
    new_og_title = f"{pose_name} | Yoga Wiki"
    new_desc = f"{pose_name}のやり方・効果・バリエーションを詳しく解説。初心者から上級者まで対応した完全ガイド。"
    
    content = re.sub(r'<title>.*?</title>', f'<title>{new_title}</title>', content)
    content = re.sub(r'property="og:title" content="[^"]*"',
                     f'property="og:title" content="{new_og_title}"', content)
    content = re.sub(r'(name="description" content=")[^"]*(")',
                     lambda m: f'{m.group(1)}{new_desc}{m.group(2)}', content, count=1)
    return content

def fix_pt_title(content, pose_name):
    new_title = f"{pose_name} - Guia Completo de Yoga | Benefícios e Instruções"
    new_og_title = f"{pose_name} | Yoga Wiki"
    new_desc = f"Aprenda {pose_name}. Instruções passo a passo, benefícios, dicas e variações para todos os níveis."
    
    content = re.sub(r'<title>.*?</title>', f'<title>{new_title}</title>', content)
    content = re.sub(r'property="og:title" content="[^"]*"',
                     f'property="og:title" content="{new_og_title}"', content)
    content = re.sub(r'(name="description" content=")[^"]*(")',
                     lambda m: f'{m.group(1)}{new_desc}{m.group(2)}', content, count=1)
    return content

def main():
    en_dir = os.path.join(WIKI_ROOT, "en")
    ja_dir = os.path.join(WIKI_ROOT, "ja")
    pt_dir = os.path.join(WIKI_ROOT, "pt")
    
    # Build EN titles index
    en_titles = {}
    for f in glob.glob(os.path.join(en_dir, "*.html")):
        en_titles[os.path.basename(f)] = get_title(f)
    
    fixed_ja = 0
    fixed_pt = 0
    
    # Fix JA
    for f in sorted(glob.glob(os.path.join(ja_dir, "*.html"))):
        name = os.path.basename(f)
        ja_title = get_title(f)
        en_title = en_titles.get(name, "")
        if en_title and ja_title == en_title:
            pose_name = extract_pose_name(en_title)
            content = open(f, encoding="utf-8").read()
            new_content = fix_ja_title(content, pose_name)
            with open(f, "w", encoding="utf-8") as fout:
                fout.write(new_content)
            fixed_ja += 1
    
    # Fix PT
    for f in sorted(glob.glob(os.path.join(pt_dir, "*.html"))):
        name = os.path.basename(f)
        pt_title = get_title(f)
        en_title = en_titles.get(name, "")
        if en_title and pt_title == en_title:
            pose_name = extract_pose_name(en_title)
            content = open(f, encoding="utf-8").read()
            new_content = fix_pt_title(content, pose_name)
            with open(f, "w", encoding="utf-8") as fout:
                fout.write(new_content)
            fixed_pt += 1
    
    print(f"Fixed JA: {fixed_ja}, Fixed PT: {fixed_pt}")

if __name__ == "__main__":
    main()
