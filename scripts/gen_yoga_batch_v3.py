#!/usr/bin/env python3
"""
Yoga Wiki Batch Expansion v3 - 137 → 200+ poses
Generates 63 new pose pages across EN/JA/PT without Gemini API
"""
import os, json, re, datetime

SITE_URL   = "https://t307239.github.io/yoga-wiki"
AMAZON_TAG = "bjj06-22"
GA4_ID     = "G-7LM8L3TRZM"

# 63 new poses not yet in generated.json
NEW_POSES = [
    # Beginner fundamentals
    ("Child's Pose", "childs-pose"),
    ("Corpse Pose", "corpse-pose"),
    ("Staff Pose", "staff-pose"),
    ("Mountain Pose II", "mountain-pose-variation"),
    ("Downward Dog Variation", "downward-dog-variation"),
    # Standing
    ("Warrior I Variation", "warrior-i-variation"),
    ("Triangle Pose", "triangle-pose"),
    ("Extended Side Angle", "extended-side-angle"),
    ("Half Moon Pose", "half-moon-pose"),
    ("Pyramid Pose", "pyramid-pose"),
    ("Revolved Triangle", "revolved-triangle"),
    ("Chair Pose Variation", "chair-pose-variation"),
    ("Wide Legged Forward Fold", "wide-legged-forward-fold"),
    ("Goddess Pose", "goddess-pose"),
    ("Warrior Lunge", "warrior-lunge"),
    # Seated
    ("Easy Pose", "easy-pose"),
    ("Hero Pose", "hero-pose"),
    ("Lotus Pose", "lotus-pose"),
    ("Bound Angle Pose", "bound-angle-pose"),
    ("Seated Forward Fold", "seated-forward-fold"),
    ("Boat Pose", "boat-pose"),
    ("Camel Pose Prep", "camel-pose-prep"),
    ("Pigeon Pose Prep", "pigeon-pose-prep"),
    ("Sage Pose", "sage-pose"),
    ("Half Spinal Twist", "half-spinal-twist"),
    # Floor / Supine
    ("Bridge Pose", "bridge-pose"),
    ("Supine Twist", "supine-twist"),
    ("Reclining Hero Pose", "reclining-hero-pose"),
    ("Legs Up The Wall", "legs-up-the-wall"),
    ("Wind Relieving Pose", "wind-relieving-pose"),
    ("Knee To Chest Pose", "knee-to-chest-pose"),
    ("Supine Butterfly", "supine-butterfly"),
    ("Fish Pose Variation", "fish-pose-variation"),
    ("Sphinx Pose", "sphinx-pose"),
    ("Crocodile Pose", "crocodile-pose"),
    # Core & Balance
    ("Plank Pose", "plank-pose"),
    ("Side Plank Pose", "side-plank-pose"),
    ("Four Limbed Staff Pose", "four-limbed-staff-pose"),
    ("Upward Facing Dog", "upward-facing-dog"),
    ("Reverse Plank", "reverse-plank"),
    ("Dolphin Pose", "dolphin-pose"),
    ("Forearm Balance", "forearm-balance"),
    # Hip openers
    ("Lizard Pose", "lizard-pose"),
    ("Dragon Pose", "dragon-pose"),
    ("Shoelace Pose", "shoelace-pose"),
    ("Swan Pose", "swan-pose"),
    ("Sleeping Swan", "sleeping-swan"),
    ("Banana Pose", "banana-pose"),
    # Backbends
    ("Cobra Pose Variation", "cobra-pose-variation"),
    ("Upward Bow Prep", "upward-bow-prep"),
    ("Locust Pose Variation", "locust-pose-variation"),
    ("Bow Pose Prep", "bow-pose-prep"),
    ("King Cobra Pose", "king-cobra-pose"),
    # Inversions
    ("Downward Dog to Plank", "downward-dog-to-plank"),
    ("Legs Over Head", "legs-over-head"),
    ("Plow Pose Variation", "plow-pose-variation"),
    ("Shoulder Stand Prep", "shoulder-stand-prep"),
    # Yin / Restorative
    ("Yin Frog Pose", "yin-frog-pose"),
    ("Butterfly Fold", "butterfly-fold"),
    ("Melting Heart Pose", "melting-heart-pose"),
    ("Caterpillar Pose", "caterpillar-pose"),
    ("Snail Pose", "snail-pose"),
    ("Square Pose", "square-pose"),
    ("Reclining Pigeon", "reclining-pigeon"),
]

# Pre-written content for each pose (EN/JA/PT)
POSE_DATA = {
    "childs-pose": {
        "en": {
            "title": "Child's Pose (Balasana) - Complete Guide | Benefits & Instructions",
            "meta": "Master Child's Pose (Balasana) with step-by-step instructions, benefits, and variations. Perfect resting pose for all yoga levels.",
            "intro": "Child's Pose (Balasana) is a fundamental resting posture in yoga that gently stretches the hips, thighs, and ankles while calming the mind. It serves as a go-to resting pose between challenging sequences.",
            "steps": ["Start on hands and knees in tabletop position","Spread knees to mat width or keep them together","Sink hips back toward heels, lowering torso forward","Extend arms forward or rest them alongside body","Rest forehead gently on the mat and breathe deeply"],
            "tips": "If hips don't reach heels, place a folded blanket between thighs and calves. Focus on lengthening the spine with each exhale.",
            "faq_q": "How long should I hold Child's Pose?",
            "faq_a": "Hold for 1-5 minutes depending on your goal — shorter for rest between poses, longer for deep hip and back release.",
        },
        "ja": {
            "title": "チャイルドポーズ（バラーサナ）完全ガイド｜効果とやり方",
            "meta": "チャイルドポーズ（バラーサナ）の正しいやり方、効果、バリエーションを解説。初心者から上級者まで使える休息ポーズ。",
            "intro": "チャイルドポーズ（バラーサナ）は、股関節、太もも、足首を穏やかにストレッチしながら心を落ち着かせる基本の休息ポーズです。チャレンジングなシーケンスの合間の休憩に最適です。",
            "steps": ["四つ這いのテーブルトップポジションから始める","膝をマット幅に開くか閉じたままにする","お尻をかかとの方向に落とし、上体を前に倒す","腕を前方に伸ばすか、体の横に置く","額を優しくマットに置き、深呼吸する"],
            "tips": "お尻がかかとに届かない場合は、太ももとふくらはぎの間に折りたたんだブランケットを置きましょう。",
            "faq_q": "チャイルドポーズはどのくらい保持すればいい？",
            "faq_a": "目的に応じて1〜5分が目安です。ポーズ間の休息なら短め、股関節や背中のリリースなら長めに保持しましょう。",
        },
        "pt": {
            "title": "Postura da Criança (Balasana) - Guia Completo | Benefícios",
            "meta": "Aprenda a Postura da Criança (Balasana) com instruções passo a passo, benefícios e variações. Postura de descanso ideal para todos os níveis.",
            "intro": "A Postura da Criança (Balasana) é uma postura de descanso fundamental no yoga que alonga suavemente os quadris, coxas e tornozelos enquanto acalma a mente.",
            "steps": ["Comece de quatro na posição de mesa","Abra os joelhos na largura do tapete ou mantenha-os juntos","Abaixe os quadris em direção aos calcanhares, inclinando o torso para frente","Estenda os braços para frente ou deixe-os ao lado do corpo","Apoie suavemente a testa no tapete e respire profundamente"],
            "tips": "Se os quadris não chegam aos calcanhares, coloque um cobertor dobrado entre as coxas e as panturrilhas.",
            "faq_q": "Quanto tempo devo manter a Postura da Criança?",
            "faq_a": "Mantenha por 1 a 5 minutos dependendo do objetivo — menor para descanso entre posturas, maior para liberar os quadris e as costas.",
        },
    },
}

# Generic template for poses without specific data
def generic_content(slug, name, lang):
    templates = {
        "en": {
            "title": f"{name} - Complete Yoga Guide | Benefits & Step-by-Step Instructions",
            "meta": f"Learn {name} with detailed instructions, benefits, modifications, and common mistakes. Suitable for beginners and advanced practitioners.",
            "intro": f"{name} is a powerful yoga posture that builds strength, flexibility, and body awareness. Regular practice develops balance between effort and ease.",
            "steps": [
                f"Begin in a stable, comfortable starting position",
                f"Engage your core and establish a steady breath",
                f"Move gradually into the shape of {name}",
                f"Align joints properly — knees over ankles, shoulders over wrists",
                f"Hold for 3-5 breaths, then release with control",
            ],
            "tips": f"Focus on alignment over depth. Use props like blocks or straps to maintain proper form. Listen to your body and avoid forcing the pose.",
            "faq_q": f"What are the main benefits of {name}?",
            "faq_a": f"{name} builds core strength, improves flexibility, and develops body awareness. It also promotes mental focus and stress reduction through mindful breathing.",
        },
        "ja": {
            "title": f"{name}（ヨガポーズ）完全ガイド｜効果・やり方・バリエーション",
            "meta": f"{name}の正しいやり方、効果、修正方法を詳しく解説。初心者から上級者まで対応したヨガポーズガイド。",
            "intro": f"{name}は、強さ、柔軟性、ボディアウェアネスを高める効果的なヨガポーズです。定期的な練習により、努力とリラックスのバランスが身につきます。",
            "steps": [
                "安定した快適なスタートポジションをとる",
                "コアを引き締め、安定した呼吸を確立する",
                f"{name}の形へと徐々に移動する",
                "ひざはくるぶしの上、肩は手首の上など関節を正しくアライメントする",
                "3〜5呼吸間キープし、コントロールしながらリリースする",
            ],
            "tips": "深さよりもアライメントを優先しましょう。ブロックやストラップなどのプロップスを使って正しいフォームを維持してください。",
            "faq_q": f"{name}の主な効果は？",
            "faq_a": f"{name}はコアの強化、柔軟性の向上、ボディアウェアネスの発達に役立ちます。また、意識的な呼吸によるメンタルフォーカスやストレス軽減効果もあります。",
        },
        "pt": {
            "title": f"{name} - Guia Completo de Yoga | Benefícios e Instruções",
            "meta": f"Aprenda {name} com instruções detalhadas, benefícios, modificações e erros comuns. Adequado para iniciantes e praticantes avançados.",
            "intro": f"{name} é uma poderosa postura de yoga que desenvolve força, flexibilidade e consciência corporal. A prática regular promove equilíbrio entre esforço e leveza.",
            "steps": [
                "Comece em uma posição inicial estável e confortável",
                "Ative o core e estabeleça uma respiração estável",
                f"Mova-se gradualmente para a forma de {name}",
                "Alinhe as articulações corretamente — joelhos sobre tornozelos, ombros sobre pulsos",
                "Mantenha por 3-5 respirações, depois solte com controle",
            ],
            "tips": f"Foque no alinhamento em vez da profundidade. Use acessórios como blocos ou cintos para manter a forma correta.",
            "faq_q": f"Quais são os principais benefícios de {name}?",
            "faq_a": f"{name} desenvolve força no core, melhora a flexibilidade e desenvolve a consciência corporal. Também promove foco mental e redução do estresse.",
        },
    }
    return templates.get(lang, templates["en"])

ADSENSE_PUB = "ca-pub-5529701443220352"

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
        ➜ Amazon: Yoga Mats & Blocks
      </a>
      <a href="https://www.amazon.co.jp/s?k=yoga+strap+props&tag={AMAZON_TAG}" 
         class="affiliate-link" target="_blank" rel="noopener sponsored">
        ➜ Amazon: Yoga Props & Straps
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

def main():
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Load existing generated slugs
    gen_file = os.path.join(base, "generated.json")
    raw = json.load(open(gen_file)) if os.path.exists(gen_file) else {"poses": []}
    if isinstance(raw, dict):
        existing = raw.get("poses", [])
    else:
        existing = raw
    existing_slugs = {p["slug"] for p in existing if isinstance(p, dict)}
    
    generated = 0
    new_entries = []
    
    for name, slug in NEW_POSES:
        if slug in existing_slugs:
            print(f"  Skip (exists): {slug}")
            continue
        
        for lang in ["en", "ja", "pt"]:
            out_dir = os.path.join(base, lang)
            os.makedirs(out_dir, exist_ok=True)
            out_file = os.path.join(out_dir, f"{slug}.html")
            
            if os.path.exists(out_file):
                continue
            
            # Get content (specific or generic)
            specific = POSE_DATA.get(slug, {}).get(lang)
            content = specific if specific else generic_content(slug, name, lang)
            
            html = build_html(name, slug, content, lang)
            with open(out_file, "w", encoding="utf-8") as f:
                f.write(html)
            print(f"  ✅ {lang}/{slug}.html")
        
        new_entries.append({"slug": slug, "name": name})
        existing_slugs.add(slug)
        generated += 1
    
    # Update generated.json (preserve original structure)
    if isinstance(raw, dict):
        raw["poses"] = existing + new_entries
        with open(gen_file, "w", encoding="utf-8") as f:
            json.dump(raw, f, indent=2, ensure_ascii=False)
    else:
        with open(gen_file, "w", encoding="utf-8") as f:
            json.dump(existing + new_entries, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Generated {generated} new poses ({generated*3} pages)")
    return generated, [e["slug"] for e in new_entries]

if __name__ == "__main__":
    main()
