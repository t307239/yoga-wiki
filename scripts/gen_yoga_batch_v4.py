#!/usr/bin/env python3
"""
Yoga Wiki Batch Expansion v4 - 182 → 220+ poses
Generates ~40 new pose pages across EN/JA/PT without external APIs
"""
import os, json, glob, datetime

SITE_URL   = "https://t307239.github.io/yoga-wiki"
AMAZON_TAG = "bjj06-22"
GA4_ID     = "G-7LM8L3TRZM"
ADSENSE_PUB = "ca-pub-5529701443220352"

# 40 new poses not yet generated
NEW_POSES = [
    # Standing & Balance
    ("Bird of Paradise", "bird-of-paradise"),
    ("Humble Warrior", "humble-warrior"),
    ("Crescent Lunge", "crescent-lunge"),
    ("Runner's Lunge", "runners-lunge"),
    ("Twisted Lunge", "twisted-lunge"),
    ("Horse Stance", "horse-stance"),
    ("Standing Straddle", "standing-straddle"),
    ("Tiptoeing Pose", "tiptoeing-pose"),
    # Arm Balances
    ("Compass Pose", "compass-pose"),
    ("Bear Pose", "bear-pose"),
    ("Low Plank", "low-plank"),
    ("Koundinyasana", "koundinyasana"),
    ("Dragonfly Pose", "dragonfly-pose"),
    # Seated & Floor
    ("Rock the Baby", "rock-the-baby"),
    ("Ankle to Knee Pose", "ankle-to-knee-pose"),
    ("Supine Bound Angle", "supine-bound-angle"),
    ("Reclined Mountain Pose", "reclined-mountain-pose"),
    ("Heel Sitting Pose", "heel-sitting-pose"),
    ("Diamond Pose", "diamond-pose"),
    ("Iron Cross Pose", "iron-cross-pose"),
    ("Stacked Legs Pose", "stacked-legs-pose"),
    ("Open Twist Pose", "open-twist-pose"),
    ("Bound Seated Twist 2", "bound-seated-twist-2"),
    # Backbends
    ("Sphinx Variation", "sphinx-variation"),
    ("Low Backbend Variation", "low-backbend-variation"),
    ("Wild Thing Variation", "wild-thing-variation"),
    ("Supported Backbend", "supported-backbend"),
    # Hip Openers
    ("Half Pigeon Flow", "half-pigeon-flow"),
    ("Lizard with Twist", "lizard-with-twist"),
    ("Extended Lizard", "extended-lizard"),
    ("Saddle Pose", "saddle-pose"),
    ("Frog Hip Opener", "frog-hip-opener"),
    # Restorative
    ("Legs Up Bolster Variation", "legs-up-bolster-variation"),
    ("Supported Side Stretch", "supported-side-stretch"),
    ("Bolster Twist", "bolster-twist"),
    ("Eye Pillow Savasana", "eye-pillow-savasana"),
    # Pranayama & Mindfulness
    ("Box Breathing Pose", "box-breathing-pose"),
    ("Alternate Nostril Breathing Pose", "alternate-nostril-breathing"),
    # Sequences
    ("Sun Salutation C Sequence", "sun-salutation-c"),
    ("Moon Salutation Yin Sequence", "moon-salutation-yin"),
]


def generic_content(slug, name, lang):
    templates = {
        "en": {
            "title": f"{name} - Complete Yoga Guide | Benefits & Step-by-Step Instructions",
            "meta": f"Learn {name} with detailed instructions, benefits, modifications, and common mistakes. Suitable for beginners and advanced practitioners.",
            "intro": f"{name} is a rewarding yoga posture that cultivates strength, flexibility, and mindful awareness. Regular practice helps integrate body and breath for a balanced state of being.",
            "steps": [
                "Begin in a stable, grounded starting position and establish a calm breath",
                "Activate your core gently and find your natural spinal alignment",
                f"Move gradually and intentionally into the shape of {name}",
                "Align key joints — check knees, hips, shoulders and engage supporting muscles",
                "Hold for 3-8 breaths, then release slowly with full control",
            ],
            "tips": f"Prioritize alignment over depth in {name}. Props like blocks, blankets, or straps can make the pose accessible and safe. Breathe steadily throughout — if the breath becomes labored, ease back slightly.",
            "faq_q": f"Who should avoid {name}?",
            "faq_a": f"Those with relevant joint injuries or acute inflammation should modify or skip {name}. Always consult a qualified yoga teacher or healthcare professional if you have any concerns.",
        },
        "ja": {
            "title": f"{name}（ヨガポーズ）完全ガイド｜効果・やり方・バリエーション",
            "meta": f"{name}の正しいやり方、効果、修正方法を詳しく解説。初心者から上級者まで対応したヨガポーズガイド。",
            "intro": f"{name}は、強さと柔軟性を高めながら、マインドフルな意識を育むヨガポーズです。定期的な練習により、身体と呼吸が統合され、バランスの取れた状態が生まれます。",
            "steps": [
                "安定した、グラウンディングされたスタートポジションをとり、穏やかな呼吸を整える",
                "コアをゆっくり引き締め、自然な背骨のアライメントを見つける",
                f"{name}の形へと意識的にゆっくりと移動する",
                "ひざ、股関節、肩などの主要な関節をチェックし、サポート筋を使う",
                "3〜8呼吸間キープし、完全にコントロールしながらゆっくりリリースする",
            ],
            "tips": f"{name}では深さよりもアライメントを優先しましょう。ブロック、ブランケット、ストラップなどのプロップスを使うと安全に実践できます。呼吸が苦しくなったら少し戻りましょう。",
            "faq_q": f"{name}を避けた方がいい人は？",
            "faq_a": f"関節の怪我や急性炎症がある方は、{name}を修正するか控えましょう。不安がある場合は、資格を持つヨガ講師または医療専門家に相談してください。",
        },
        "pt": {
            "title": f"{name} - Guia Completo de Yoga | Benefícios e Instruções",
            "meta": f"Aprenda {name} com instruções detalhadas, benefícios, modificações e erros comuns. Adequado para iniciantes e praticantes avançados.",
            "intro": f"{name} é uma postura de yoga enriquecedora que cultiva força, flexibilidade e consciência plena. A prática regular ajuda a integrar corpo e respiração para um estado de equilíbrio.",
            "steps": [
                "Comece em uma posição inicial estável e aterrada, estabelecendo uma respiração calma",
                "Ative suavemente o core e encontre o alinhamento natural da coluna",
                f"Mova-se gradualmente e intencionalmente para a forma de {name}",
                "Alinhe as articulações principais — verifique joelhos, quadris e ombros",
                "Mantenha por 3-8 respirações, depois solte lentamente com controle total",
            ],
            "tips": f"Priorize o alinhamento em vez da profundidade em {name}. Acessórios como blocos, cobertores ou cintos podem tornar a postura acessível e segura.",
            "faq_q": f"Quem deve evitar {name}?",
            "faq_a": f"Pessoas com lesões articulares relevantes ou inflamação aguda devem modificar ou evitar {name}. Consulte sempre um professor de yoga qualificado se tiver dúvidas.",
        },
    }
    return templates.get(lang, templates["en"])


def build_html(name, slug, content, lang):
    title = content["title"]
    meta = content["meta"]
    intro = content["intro"]
    steps = content.get("steps", [])
    tips = content.get("tips", "")
    faq_q = content.get("faq_q", "")
    faq_a = content.get("faq_a", "")

    lang_labels = {
        "en": ("en", "Steps", "Tips", "FAQ", "Try these products", "Related Poses"),
        "ja": ("ja", "手順", "ヒント", "よくある質問", "おすすめ商品", "関連ポーズ"),
        "pt": ("pt", "Passos", "Dicas", "Perguntas Frequentes", "Produtos recomendados", "Posturas Relacionadas"),
    }
    ll = lang_labels.get(lang, lang_labels["en"])
    lang_code, steps_lbl, tips_lbl, faq_lbl, amz_lbl, related_lbl = ll

    steps_html = "\n".join(
        f'<li class="step-item"><span class="step-num">{i+1}</span><span>{s}</span></li>'
        for i, s in enumerate(steps)
    )
    now = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S+09:00")

    return f'''<!DOCTYPE html>
<html lang="{lang_code}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{meta}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{meta}">
<meta property="og:type" content="article">
<meta property="og:url" content="{SITE_URL}/{lang}/{slug}.html">
<link rel="canonical" href="{SITE_URL}/{lang}/{slug}.html">
<link rel="stylesheet" href="../style.css">
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id={GA4_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{GA4_ID}');
</script>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={ADSENSE_PUB}" crossorigin="anonymous"></script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "{title}",
  "description": "{meta}",
  "datePublished": "{now}",
  "step": [{",".join(f'{{"@type":"HowToStep","text":"{s.replace(chr(34), chr(39))}"}}' for s in steps)}]
}}
</script>
</head>
<body>
<header class="site-header">
  <div class="container">
    <a href="../index.html" class="logo">🧘 Yoga Wiki</a>
    <nav>
      <a href="../index.html">Home</a>
    </nav>
  </div>
</header>
<main class="container article-main">
  <article>
    <h1>{name}</h1>
    <p class="intro">{intro}</p>

    <h2>{steps_lbl}</h2>
    <ol class="steps-list">{steps_html}</ol>

    <h2>{tips_lbl}</h2>
    <p>{tips}</p>

    <div class="affiliate-box">
      <h3>🛒 {amz_lbl}</h3>
      <a href="https://www.amazon.co.jp/s?k=yoga+mat+block&tag={AMAZON_TAG}"
         class="affiliate-link" target="_blank" rel="noopener sponsored">
        ➜ Amazon: Yoga Mats &amp; Blocks
      </a>
      <a href="https://www.amazon.co.jp/s?k=yoga+strap+props&tag={AMAZON_TAG}"
         class="affiliate-link" target="_blank" rel="noopener sponsored">
        ➜ Amazon: Yoga Props &amp; Straps
      </a>
    </div>

    <div class="cta-banner">
      <h3>🥋 Train like an athlete</h3>
      <p>Track your yoga and BJJ training progress with our free app</p>
      <a href="https://bjj-app-one.vercel.app" class="cta-button" target="_blank">
        Start Tracking Free →
      </a>
    </div>

    <h2>{faq_lbl}</h2>
    <div class="faq-item">
      <h3>{faq_q}</h3>
      <p>{faq_a}</p>
    </div>
  </article>
</main>
<footer class="site-footer">
  <div class="container">
    <p>© 2026 Yoga Wiki | <a href="{SITE_URL}">Home</a></p>
  </div>
</footer>
</body>
</html>'''


def update_sitemap(base, new_slugs):
    sitemap_file = os.path.join(base, "sitemap.xml")
    if not os.path.exists(sitemap_file):
        return
    with open(sitemap_file, encoding="utf-8") as f:
        sitemap = f.read()
    entries = []
    for slug in new_slugs:
        for lang in ["en", "ja", "pt"]:
            if f"{lang}/{slug}.html" not in sitemap:
                entries.append(f"""  <url>
    <loc>{SITE_URL}/{lang}/{slug}.html</loc>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>""")
    if entries:
        insert = "\n" + "\n".join(entries) + "\n"
        sitemap = sitemap.replace("</urlset>", insert + "</urlset>")
        with open(sitemap_file, "w", encoding="utf-8") as f:
            f.write(sitemap)
        print(f"  📍 Added {len(entries)} sitemap entries")


def update_index(base, new_slugs_names):
    """Add cards to each language index.html for new poses"""
    for lang in ["en", "ja", "pt"]:
        idx_file = os.path.join(base, lang, "index.html")
        if not os.path.exists(idx_file):
            continue
        with open(idx_file, encoding="utf-8") as f:
            idx = f.read()
        cards = []
        for slug, name in new_slugs_names:
            if f"{slug}.html" not in idx:
                cards.append(f'<div class="pose-card"><a href="{slug}.html">{name}</a></div>')
        if cards:
            insert = "\n".join(cards) + "\n"
            idx = idx.replace("</div>\n</main>", insert + "</div>\n</main>")
            with open(idx_file, "w", encoding="utf-8") as f:
                f.write(idx)
    print(f"  📄 Updated index.html for {len(new_slugs_names)} new poses")


def main():
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Get already existing slugs from filesystem
    existing_slugs = set(
        os.path.basename(f).replace(".html", "")
        for f in glob.glob(os.path.join(base, "en", "*.html"))
        if os.path.basename(f) != "index.html"
    )

    generated = 0
    new_slug_names = []

    for name, slug in NEW_POSES:
        if slug in existing_slugs:
            print(f"  Skip (exists): {slug}")
            continue

        for lang in ["en", "ja", "pt"]:
            out_dir = os.path.join(base, lang)
            os.makedirs(out_dir, exist_ok=True)
            out_file = os.path.join(out_dir, f"{slug}.html")
            content = generic_content(slug, name, lang)
            html = build_html(name, slug, content, lang)
            with open(out_file, "w", encoding="utf-8") as f:
                f.write(html)
            print(f"  ✅ {lang}/{slug}.html")

        existing_slugs.add(slug)
        new_slug_names.append((slug, name))
        generated += 1

    if new_slug_names:
        new_slugs = [s for s, _ in new_slug_names]
        update_sitemap(base, new_slugs)
        update_index(base, new_slug_names)

    print(f"\n✅ Generated {generated} new poses ({generated * 3} pages)")
    return generated


if __name__ == "__main__":
    main()
