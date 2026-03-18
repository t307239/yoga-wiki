#!/usr/bin/env python3
"""
Yoga Wiki Batch v9 - 80 new yoga poses × 3 languages = 240 pages
Goal: reach 350 total EN poses (271 existing + 80 new = 351)
"""
import os, datetime

SITE_URL   = "https://t307239.github.io/yoga-wiki"
AMAZON_TAG = "bjj06-22"
GA4_ID     = "G-7LM8L3TRZM"
ADSENSE_PUB = "ca-pub-5529701443220352"
BASE       = "/sessions/keen-sharp-davinci/mnt/Claude/yoga-wiki"
DATE       = "2026-03-18"

NEW_POSES = [
    # Seated & Forward Folds
    ("Seated Cat Cow Stretch",          "seated-cat-cow-stretch"),
    ("Seated Ankle to Knee Pose",       "seated-ankle-to-knee-pose"),
    ("Seated Eagle Arms",               "seated-eagle-arms"),
    ("Seated Heart Opener",             "seated-heart-opener"),
    ("Seated Mountain Forward Fold",    "seated-mountain-forward-fold"),
    # Standing Variations
    ("High Lunge Variation",            "high-lunge-variation"),
    ("Standing Side Stretch",          "standing-side-stretch"),
    ("Standing Hand to Foot",          "standing-hand-to-foot"),
    ("Standing Torso Twist",           "standing-torso-twist"),
    ("Chair Pose Variation",            "chair-pose-variation"),
    ("Wide Stance Forward Fold",        "wide-stance-forward-fold"),
    ("Goddess Squat Variation",         "goddess-squat-variation"),
    ("Warrior Lunge Twist",             "warrior-lunge-twist"),
    ("Standing Backbend",              "standing-backbend"),
    ("Mountain Pose Arms",             "mountain-pose-arms"),
    # Twists
    ("Seated Twist Variation",          "seated-twist-variation"),
    ("Supine Twist Variation",          "supine-twist-variation"),
    ("Chair Twist",                    "chair-twist"),
    ("Revolved Crescent Lunge",         "revolved-crescent-lunge"),
    ("Revolved Side Angle",            "revolved-side-angle"),
    ("Marichyasana A",                 "marichyasana-a"),
    ("Marichyasana C",                 "marichyasana-c"),
    # Backbends
    ("Puppy Pose",                     "puppy-pose"),
    ("Upward Facing Dog Variation",    "upward-facing-dog-variation"),
    ("Low Cobra Variation",            "low-cobra-variation"),
    ("Supported Fish Pose",            "supported-fish-pose"),
    ("King Cobra Pose",                "king-cobra-pose"),
    ("Wild Thing Variation",           "wild-thing-variation"),
    ("Camel Pose Variation",           "camel-pose-variation"),
    ("Bridge Pose Arms",               "bridge-pose-arms"),
    # Hip Openers
    ("Double Pigeon Pose",             "double-pigeon-pose"),
    ("Frog Pose Variation",            "frog-pose-variation"),
    ("Low Lunge Hip Flexor",           "low-lunge-hip-flexor"),
    ("Half Splits Variation",          "half-splits-variation"),
    ("Lizard Variation",               "lizard-variation"),
    ("Swan Pose Yin",                  "swan-pose-yin"),
    ("Shoelace Pose Yin",              "shoelace-pose-yin"),
    # Inversions & Arm Balances
    ("Dolphin Pose",                   "dolphin-pose"),
    ("Tripod Headstand",               "tripod-headstand"),
    ("Feathered Peacock Prep",         "feathered-peacock-prep"),
    ("Firefly Pose",                   "firefly-pose"),
    ("Peacock Pose",                   "peacock-pose"),
    ("Eight Angle Pose",               "eight-angle-pose"),
    ("Flying Lizard Pose",             "flying-lizard-pose"),
    # Core & Strength
    ("Plank to Downdog Flow",          "plank-to-downdog-flow"),
    ("Side Plank Variation",           "side-plank-variation"),
    ("Reverse Plank",                  "reverse-plank"),
    ("Navasana Variation",             "navasana-variation"),
    ("Hollow Body Hold Yoga",          "hollow-body-hold-yoga"),
    ("Superman Pose",                  "superman-pose"),
    # Restorative & Yin
    ("Waterfall Pose",                 "waterfall-pose"),
    ("Reclined Butterfly Variation",   "reclined-butterfly-variation"),
    ("Prone Savasana",                 "prone-savasana"),
    ("Supported Bridge Variation",     "supported-bridge-variation"),
    ("Crocodile Pose",                 "crocodile-pose"),
    ("Reclined Hero Variation",        "reclined-hero-variation"),
    ("Sleeping Swan Variation",        "sleeping-swan-variation"),
    ("Sphinx Variation",               "sphinx-variation"),
    ("Deer Pose Yin",                  "deer-pose-yin"),
    ("Half Dragonfly Yin",             "half-dragonfly-yin"),
    # Pranayama & Meditation
    ("Box Breathing Yoga",             "box-breathing-yoga"),
    ("Three Part Breath",              "three-part-breath"),
    ("Bhramari Pranayama",             "bhramari-pranayama"),
    ("Kapalbhati Pranayama",           "kapalbhati-pranayama"),
    ("Cooling Breath Sitali",          "cooling-breath-sitali"),
    ("Body Scan Meditation",           "body-scan-meditation"),
    ("Walking Meditation Yoga",        "walking-meditation-yoga"),
    ("Yoga Nidra Practice",            "yoga-nidra-practice"),
    # Sequences & Flows
    ("Sun Salutation Modification",    "sun-salutation-modification"),
    ("Evening Wind Down Flow",         "evening-wind-down-flow"),
    ("Morning Energize Flow",          "morning-energize-flow"),
    ("Hip Opening Sequence Advanced",  "hip-opening-sequence-advanced"),
    ("Spinal Mobility Sequence",       "spinal-mobility-sequence"),
    ("Balance Sequence Flow",          "balance-sequence-flow"),
    ("Core Strengthening Sequence",    "core-strengthening-sequence"),
    ("Neck and Shoulder Release",      "neck-and-shoulder-release"),
    ("Wrist Strength Yoga",            "wrist-strength-yoga"),
    ("Post Workout Yoga",              "post-workout-yoga"),
]

def generic_content(slug, name, lang):
    templates = {
        "en": {
            "title": f"{name} - Complete Yoga Guide | Benefits & Instructions",
            "meta": f"Learn {name} with step-by-step instructions, key benefits, modifications, and practice tips. Suitable for all yoga levels.",
            "intro": f"{name} is a rewarding yoga posture that cultivates strength, flexibility, and mindful awareness. Regular practice integrates body and breath for a balanced state of being.",
            "steps": [
                "Begin in a stable, grounded starting position and establish a calm breath",
                "Activate your core gently and find your natural spinal alignment",
                f"Move gradually and intentionally into the shape of {name}",
                "Align key joints — check knees, hips, shoulders and engage supporting muscles",
                "Hold for 3–5 breaths, staying present and adjusting as needed",
                "To release, reverse your entry path mindfully, returning to neutral",
            ],
            "benefits": [
                "Improves flexibility and range of motion in targeted muscle groups",
                "Builds functional strength through engaged, sustained holds",
                "Enhances body awareness and coordination",
                "Reduces tension held in the muscles and connective tissue",
                "Supports mental focus and stress reduction through breath-linked movement",
            ],
            "modifications": [
                "Use props (blocks, bolsters, straps) to accommodate your current range of motion",
                "Reduce the depth of the pose if you feel sharp or joint pain",
                "Practice near a wall for balance support when needed",
                "Keep a micro-bend in joints to protect against hyperextension",
            ],
            "mistakes": [
                "Forcing range of motion before the body is warm and ready",
                "Holding your breath — maintain smooth, even breathing throughout",
                "Collapsing through the lower back — keep core gently engaged",
                "Rushing transitions in and out of the pose",
            ],
            "amazon_text": "Enhance your practice with quality yoga equipment.",
            "amazon_url": f"https://www.amazon.co.jp/s?k=yoga+mat+block&tag={AMAZON_TAG}",
            "amazon_link": "Shop Yoga Equipment on Amazon",
        },
        "ja": {
            "title": f"{name}の完全ガイド | 効果・やり方・注意点",
            "meta": f"{name}のやり方を分かりやすく解説。効果・バリエーション・よくある間違いまで完全網羅。初心者から上級者まで対応。",
            "intro": f"{name}は、強さ・柔軟性・マインドフルネスを育む充実したヨガポーズです。定期的な練習で身体と呼吸のバランスが整います。",
            "steps": [
                "安定した基本姿勢で始め、穏やかな呼吸を確立する",
                "体幹を軽く引き締め、自然な脊柱のアラインメントを見つける",
                f"{name}の形へゆっくりと意識的に移行する",
                "主要な関節（膝・腰・肩）のアラインメントを確認し、補助筋を使う",
                "3〜5呼吸キープし、現在の感覚に集中しながら調整する",
                "リリース時はエントリーと逆の順序でニュートラルに戻る",
            ],
            "benefits": [
                "対象筋群の柔軟性と可動域が向上する",
                "持続的なホールドによる機能的な筋力が構築される",
                "身体感覚とコーディネーションが高まる",
                "筋肉と結合組織に蓄積された緊張が解放される",
                "呼吸と連動した動きによるメンタルフォーカスとストレス軽減",
            ],
            "modifications": [
                "ブロック・ボルスター・ストラップなどのプロップを使って可動域に合わせる",
                "鋭い痛みや関節痛がある場合はポーズを浅くする",
                "バランスのサポートが必要な場合は壁の近くで練習する",
                "過伸展を防ぐために関節にマイクロベンドを保つ",
            ],
            "mistakes": [
                "身体が温まる前に無理に可動域を広げる",
                "息を止める — 練習中は滑らかで均一な呼吸を維持する",
                "腰部が崩れる — 体幹を軽く引き締めて保つ",
                "ポーズへのトランジションを急ぐ",
            ],
            "amazon_text": "質の高いヨガ用品でプラクティスを充実させよう。",
            "amazon_url": f"https://www.amazon.co.jp/s?k=ヨガマット+ブロック&tag={AMAZON_TAG}",
            "amazon_link": "Amazonでヨガ用品を見る",
        },
        "pt": {
            "title": f"{name} - Guia Completo de Yoga | Benefícios e Instruções",
            "meta": f"Aprenda {name} com instruções passo a passo, benefícios principais, modificações e dicas de prática. Adequado para todos os níveis.",
            "intro": f"{name} é uma postura de yoga recompensadora que cultiva força, flexibilidade e consciência plena. A prática regular integra corpo e respiração para um estado equilibrado.",
            "steps": [
                "Comece em uma posição inicial estável e fundamentada, estabelecendo uma respiração calma",
                "Ative suavemente o núcleo e encontre seu alinhamento espinhal natural",
                f"Mova-se gradual e intencionalmente para a forma de {name}",
                "Alinhe as articulações principais — verifique joelhos, quadris, ombros e envolva os músculos de suporte",
                "Segure por 3–5 respirações, mantendo-se presente e ajustando conforme necessário",
                "Para liberar, inverta seu caminho de entrada com atenção, retornando ao neutro",
            ],
            "benefits": [
                "Melhora a flexibilidade e amplitude de movimento nos grupos musculares alvo",
                "Constrói força funcional através de sustentações engajadas",
                "Aprimora a consciência corporal e a coordenação",
                "Reduz a tensão mantida nos músculos e tecido conjuntivo",
                "Apoia o foco mental e a redução do estresse através do movimento vinculado à respiração",
            ],
            "modifications": [
                "Use adereços (blocos, bolsters, cintas) para acomodar sua amplitude de movimento atual",
                "Reduza a profundidade da pose se sentir dor aguda ou nas articulações",
                "Pratique perto de uma parede para apoio de equilíbrio quando necessário",
                "Mantenha uma micro-flexão nas articulações para proteger contra hiperextensão",
            ],
            "mistakes": [
                "Forçar a amplitude de movimento antes do corpo estar aquecido",
                "Prender a respiração — mantenha uma respiração suave e uniforme ao longo",
                "Colapsar na lombar — mantenha o núcleo suavemente engajado",
                "Apressar as transições para dentro e fora da pose",
            ],
            "amazon_text": "Aprimore sua prática com equipamentos de yoga de qualidade.",
            "amazon_url": f"https://www.amazon.co.jp/s?k=yoga+mat&tag={AMAZON_TAG}",
            "amazon_link": "Compre Equipamentos de Yoga na Amazon",
        },
    }
    t = templates[lang]
    steps_html = "".join(f"<li>{s}</li>" for s in t["steps"])
    benefits_html = "".join(f"<li>{b}</li>" for b in t["benefits"])
    mods_html = "".join(f"<li>{m}</li>" for m in t["modifications"])
    mistakes_html = "".join(f"<li>{m}</li>" for m in t["mistakes"])

    headings = {
        "en": ("How to Practice", "Key Benefits", "Modifications", "Common Mistakes"),
        "ja": ("練習方法", "主な効果", "バリエーション・修正", "よくある間違い"),
        "pt": ("Como Praticar", "Principais Benefícios", "Modificações", "Erros Comuns"),
    }
    h = headings[lang]

    bjj_cta = {
        "en": f"""<div style="background:linear-gradient(135deg,#0f172a,#1e1b4b);border:1px solid #e94560;border-radius:12px;padding:20px 24px;margin:28px 0;text-align:center">
<p style="color:#e2b714;font-weight:700;font-size:1rem;margin-bottom:8px">🥋 Track Your BJJ Training Too</p>
<p style="color:#9ca3af;font-size:.85rem;margin-bottom:14px">Yoga and BJJ complement each other perfectly. Track your BJJ progress with BJJ App.</p>
<a href="https://bjj-app-one.vercel.app" target="_blank" rel="noopener" style="display:inline-block;background:#e94560;color:#fff;padding:10px 24px;border-radius:8px;font-weight:700;text-decoration:none;font-size:.9rem">Try BJJ App Free →</a>
</div>""",
        "ja": f"""<div style="background:linear-gradient(135deg,#0f172a,#1e1b4b);border:1px solid #e94560;border-radius:12px;padding:20px 24px;margin:28px 0;text-align:center">
<p style="color:#e2b714;font-weight:700;font-size:1rem;margin-bottom:8px">🥋 BJJの練習も記録しよう</p>
<p style="color:#9ca3af;font-size:.85rem;margin-bottom:14px">ヨガとBJJは相性抜群。BJJ Appで練習ログ・分析を管理しよう。</p>
<a href="https://bjj-app-one.vercel.app" target="_blank" rel="noopener" style="display:inline-block;background:#e94560;color:#fff;padding:10px 24px;border-radius:8px;font-weight:700;text-decoration:none;font-size:.9rem">BJJ Appを試す →</a>
</div>""",
        "pt": f"""<div style="background:linear-gradient(135deg,#0f172a,#1e1b4b);border:1px solid #e94560;border-radius:12px;padding:20px 24px;margin:28px 0;text-align:center">
<p style="color:#e2b714;font-weight:700;font-size:1rem;margin-bottom:8px">🥋 Registre seu Treino de BJJ Também</p>
<p style="color:#9ca3af;font-size:.85rem;margin-bottom:14px">Yoga e BJJ se complementam perfeitamente. Acompanhe seu progresso no BJJ com o BJJ App.</p>
<a href="https://bjj-app-one.vercel.app" target="_blank" rel="noopener" style="display:inline-block;background:#e94560;color:#fff;padding:10px 24px;border-radius:8px;font-weight:700;text-decoration:none;font-size:.9rem">Experimente Grátis →</a>
</div>""",
    }

    return {
        "title": t["title"],
        "meta": t["meta"],
        "body": f"""<h2>{h[0]}</h2>
<p>{t["intro"]}</p>
<ol>{steps_html}</ol>
<h2>{h[1]}</h2>
<ul>{benefits_html}</ul>
<div style="background:#0f2a1a;border-left:4px solid #4ade80;border-radius:8px;padding:14px 18px;margin:20px 0">
<strong style="color:#4ade80">Tip:</strong> {t["amazon_text"]} <a href="{t["amazon_url"]}" target="_blank" rel="sponsored noopener" style="color:#e2b714">{t["amazon_link"]}</a>
</div>
<h2>{h[2]}</h2>
<ul>{mods_html}</ul>
<h2>{h[3]}</h2>
<ul>{mistakes_html}</ul>
{bjj_cta[lang]}"""
    }


CSS = """  :root{{--bg:#0a0e1a;--card:#111827;--accent:#e2b714;--text:#e5e7eb;--muted:#9ca3af}}
  *{{box-sizing:border-box;margin:0;padding:0}}
  body{{background:var(--bg);color:var(--text);font-family:'Segoe UI',sans-serif;line-height:1.75}}
  header{{background:linear-gradient(135deg,#0f172a,#1a1040);padding:24px 16px;text-align:center;border-bottom:2px solid var(--accent)}}
  header h1{{color:var(--accent);font-size:1.8rem;margin-bottom:6px}}
  header p{{color:var(--muted);font-size:.95rem}}
  nav{{background:#111827;padding:10px 20px;display:flex;gap:12px;flex-wrap:wrap;justify-content:center;font-size:.85rem}}
  nav a{{color:var(--muted);text-decoration:none}}nav a:hover{{color:var(--accent)}}
  .container{{max-width:860px;margin:0 auto;padding:24px 16px}}
  h2{{color:var(--accent);margin:28px 0 12px;font-size:1.2rem}}
  p{{color:var(--text);margin-bottom:12px}}
  ul,ol{{padding-left:20px;margin-bottom:14px}}
  li{{margin-bottom:6px;color:var(--text)}}
  footer{{background:#060d1a;text-align:center;padding:28px;color:var(--muted);font-size:.8rem;margin-top:40px}}
  footer a{{color:var(--muted);text-decoration:none}}"""

lang_meta = {"en": "en", "ja": "ja", "pt": "pt"}
lang_index = {"en": "All Poses", "ja": "全ポーズ一覧", "pt": "Todas as Poses"}
lang_back  = {"en": "← All Poses", "ja": "← 全ポーズ一覧", "pt": "← Todas as Poses"}

generated = []
skipped = []

for name, slug in NEW_POSES:
    for lang in ["en", "ja", "pt"]:
        out_dir = f"{BASE}/{lang}"
        out_path = f"{out_dir}/{slug}.html"
        if os.path.exists(out_path):
            skipped.append(f"{lang}/{slug}")
            continue
        c = generic_content(slug, name, lang)
        title = c["title"]
        meta  = c["meta"]
        body  = c["body"]

        html = f"""<!DOCTYPE html>
<html lang="{lang_meta[lang]}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{meta}">
  <link rel="canonical" href="{SITE_URL}/{lang}/{slug}.html">
  <link rel="alternate" hreflang="en" href="{SITE_URL}/en/{slug}.html">
  <link rel="alternate" hreflang="ja" href="{SITE_URL}/ja/{slug}.html">
  <link rel="alternate" hreflang="pt" href="{SITE_URL}/pt/{slug}.html">
  <link rel="alternate" hreflang="x-default" href="{SITE_URL}/en/{slug}.html">
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={ADSENSE_PUB}" crossorigin="anonymous"></script>
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id={GA4_ID}"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', '{GA4_ID}');
  </script>
  <style>
{CSS}
  </style>
  <script type="application/ld+json">
  {{
    "@context":"https://schema.org",
    "@graph":[
      {{
        "@type":"Article",
        "headline":"{title}",
        "description":"{meta}",
        "url":"{SITE_URL}/{lang}/{slug}.html",
        "datePublished":"{DATE}",
        "dateModified":"{DATE}",
        "publisher":{{"@type":"Organization","name":"Yoga Wiki","url":"https://t307239.github.io/yoga-wiki/"}},
        "inLanguage":"{lang_meta[lang]}"
      }},
      {{
        "@type":"BreadcrumbList",
        "itemListElement":[
          {{"@type":"ListItem","position":1,"name":"Yoga Wiki","item":"{SITE_URL}/{lang}/"}},
          {{"@type":"ListItem","position":2,"name":"{name}","item":"{SITE_URL}/{lang}/{slug}.html"}}
        ]
      }}
    ]
  }}
  </script>
</head>
<body>
<header>
  <h1>{name}</h1>
  <p>{meta}</p>
</header>
<nav>
  <a href="../{lang}/">{lang_back[lang]}</a>
  <a href="../en/">EN</a> <a href="../ja/">JA</a> <a href="../pt/">PT</a>
</nav>
<div class="container">
{body}
</div>
<footer><p>Yoga Wiki — Free yoga resources for practitioners worldwide. <a href="../{lang}/">Back to index</a></p></footer>
</body>
</html>"""
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
        generated.append(f"{lang}/{slug}")

print(f"✅ Generated: {len(generated)} pages")
print(f"⏭️  Skipped (existing): {len(skipped)} pages")

# Update sitemap.xml
sitemap_path = f"{BASE}/sitemap.xml"
with open(sitemap_path, "r", encoding="utf-8") as f:
    sitemap = f.read()

new_entries = ""
for name, slug in NEW_POSES:
    for lang in ["en", "ja", "pt"]:
        url = f"{SITE_URL}/{lang}/{slug}.html"
        if url not in sitemap:
            new_entries += f"""  <url>
    <loc>{url}</loc>
    <lastmod>{DATE}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>
"""

if new_entries:
    sitemap = sitemap.replace("</urlset>", new_entries + "</urlset>")
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(sitemap)
    total = sitemap.count("<url>")
    print(f"✅ sitemap.xml: {total} URLs")

# Count EN pages
en_pages = len([f for f in os.listdir(f"{BASE}/en") if f.endswith(".html") and f != "index.html"])
print(f"📊 Total EN pages: {en_pages}")
