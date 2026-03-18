#!/usr/bin/env python3
# gen_yoga_batch_v10.py — 16 more poses to reach 350 EN total
import os, re
from datetime import datetime

BASE = "/sessions/keen-sharp-davinci/mnt/Claude/yoga-wiki"
LANGS = ["en", "ja", "pt"]
NOW = datetime.now().strftime("%Y-%m-%d")

GA4 = "G-XXXXXXXXXX"
AMAZON_TAG = "bjjwiki-20"
BJJ_APP_URL = "https://bjj-app-one.vercel.app"

POSES = [
    {
        "slug": "acro-yoga-basics",
        "en": {"title": "Acro Yoga Basics", "category": "Partner", "desc": "Introduction to acro yoga — a blend of yoga, acrobatics, and Thai massage practiced with a partner for strength, trust, and fun.", "benefits": "Builds upper body strength, improves communication and trust, enhances core stability, develops flexibility", "instructions": "Start as base lying on back with legs vertical. Flyer positions hips over base's feet. Gradually shift weight as base straightens legs. Maintain constant communication throughout.", "tips": "Always practice near a wall or with a spotter when learning. Clear communication is essential. Start with simple poses before advancing.", "duration": "Practice sequences of 10-20 minutes with a trusted partner", "contraindications": "Wrist injuries, shoulder problems, fear of heights, lack of trusted partner"},
        "ja": {"title": "アクロヨガ基礎", "category": "パートナー", "desc": "アクロヨガの入門 — ヨガ、アクロバット、タイマッサージをパートナーと融合させ、筋力・信頼・楽しさを育む実践。", "benefits": "上半身の強化、コミュニケーション向上、コア安定性向上、柔軟性発達", "instructions": "ベースが仰向けで脚を垂直に立てます。フライヤーがベースの足の上に腰を乗せます。ベースが脚を伸ばしながら体重を移動させます。常にコミュニケーションを取り続けます。", "tips": "最初は壁の近くかスポッターを付けて練習しましょう。明確なコミュニケーションが必須です。シンプルなポーズから始めます。", "duration": "信頼できるパートナーと10〜20分のシーケンスを練習", "contraindications": "手首の怪我、肩の問題、高所恐怖症、信頼できるパートナーの不在"},
        "pt": {"title": "Básico de Acro Yoga", "category": "Parceiro", "desc": "Introdução ao acro yoga — uma fusão de yoga, acrobacia e massagem tailandesa praticada com um parceiro para força, confiança e diversão.", "benefits": "Fortalece a parte superior do corpo, melhora comunicação e confiança, estabiliza o core, desenvolve flexibilidade", "instructions": "O base deita de costas com pernas verticais. O voador posiciona o quadril sobre os pés do base. Gradualmente transfira o peso enquanto o base estende as pernas. Mantenha comunicação constante.", "tips": "Sempre pratique perto de uma parede ou com um spotter ao aprender. Comunicação clara é essencial. Comece com poses simples antes de avançar.", "duration": "Pratique sequências de 10-20 minutos com um parceiro de confiança", "contraindications": "Lesões no pulso, problemas no ombro, medo de altura, falta de parceiro confiável"},
    },
    {
        "slug": "standing-crescent-pose",
        "en": {"title": "Standing Crescent Pose", "category": "Standing", "desc": "A graceful standing lateral stretch that elongates the entire side body, opening the intercostal muscles and creating space in the ribs.", "benefits": "Stretches intercostal muscles, lengthens spine, opens side body, improves posture, releases shoulder tension", "instructions": "Stand in mountain pose. Inhale and raise both arms overhead. Clasp fingers or hold opposite wrists. Exhale and lean to the right, creating a crescent shape. Keep hips level. Hold and breathe, then switch sides.", "tips": "Keep both feet planted equally. Don't let the hip jut out — keep it stacked over the ankles. Breathe into the stretched side.", "duration": "Hold 5-8 breaths each side", "contraindications": "Shoulder injuries, scoliosis, hip or spinal issues"},
        "ja": {"title": "スタンディングクレセントポーズ", "category": "立位", "desc": "体の側面全体を伸ばす優雅な立位ラテラルストレッチ。肋間筋を開き、肋骨にスペースを作ります。", "benefits": "肋間筋のストレッチ、脊柱の伸長、体側を開く、姿勢改善、肩の緊張解放", "instructions": "山のポーズで立ちます。息を吸いながら両腕を頭上へ。指を組むか反対の手首を持ちます。息を吐きながら右へ傾き、三日月形を作ります。腰を水平に保ちます。呼吸しながらホールドし、反対側へ。", "tips": "両足を均等に地面に着けます。腰が外に出ないよう注意し、足首の上に保ちます。伸びている側に呼吸を送ります。", "duration": "各側5〜8呼吸ホールド", "contraindications": "肩の怪我、脊柱側弯症、腰や脊椎の問題"},
        "pt": {"title": "Pose da Lua Crescente em Pé", "category": "Em Pé", "desc": "Um gracioso alongamento lateral em pé que alonga todo o lado do corpo, abrindo os músculos intercostais e criando espaço nas costelas.", "benefits": "Estica músculos intercostais, alonga a coluna, abre o lado do corpo, melhora postura, libera tensão nos ombros", "instructions": "Fique em pose da montanha. Inspire e levante ambos os braços acima da cabeça. Entrelace os dedos ou segure os pulsos opostos. Expire e incline para a direita, criando uma forma de crescente. Mantenha o quadril nivelado. Segure e respire, depois troque de lado.", "tips": "Mantenha ambos os pés plantados igualmente. Não deixe o quadril projetar — mantenha-o sobre os tornozelos. Respire para o lado esticado.", "duration": "Segure 5-8 respirações de cada lado", "contraindications": "Lesões nos ombros, escoliose, problemas no quadril ou coluna"},
    },
    {
        "slug": "warrior-flow-sequence",
        "en": {"title": "Warrior Flow Sequence", "category": "Sequence", "desc": "A dynamic vinyasa-style flow linking Warrior I, II, and III with smooth transitions that build heat, strength, and coordination.", "benefits": "Builds leg strength, improves balance and coordination, develops heat, strengthens core, enhances breath-movement connection", "instructions": "Start in Warrior I. On exhale, transition to Warrior II by opening hips. Flow to Reverse Warrior, then cartwheel down to Warrior III balancing on one leg. Return to standing, then repeat on other side.", "tips": "Move with the breath — one breath per movement. Focus on keeping hips aligned in each warrior. Use drishti (gaze point) to improve balance.", "duration": "Complete 3-5 rounds each side as part of a longer practice", "contraindications": "Knee injuries, hip problems, balance issues"},
        "ja": {"title": "ウォーリアーフローシーケンス", "category": "シーケンス", "desc": "ウォーリアーI、II、IIIをスムーズなトランジションで繋ぐダイナミックなヴィンヤサスタイルのフロー。熱・強さ・協調性を育てます。", "benefits": "脚の強化、バランス・協調性向上、熱の生成、コア強化、呼吸と動作の結びつき向上", "instructions": "ウォーリアーIから始めます。息を吐きながら腰を開いてウォーリアーIIへ。リバースウォーリアーへ流れ、次に片足バランスのウォーリアーIIIへ。立位に戻り、反対側へ。", "tips": "呼吸に合わせて動きます — 動作ごとに1呼吸。各ウォーリアーで腰の位置合わせを維持します。ドリシュティ（視点）でバランスを向上させます。", "duration": "長めの練習の一部として各側3〜5ラウンド", "contraindications": "膝の怪我、腰の問題、バランスの問題"},
        "pt": {"title": "Sequência de Fluxo do Guerreiro", "category": "Sequência", "desc": "Um fluxo dinâmico no estilo vinyasa ligando Guerreiro I, II e III com transições suaves que constroem calor, força e coordenação.", "benefits": "Fortalece as pernas, melhora equilíbrio e coordenação, gera calor, fortalece o core, aprimora conexão respiração-movimento", "instructions": "Comece no Guerreiro I. Na expiração, transite para Guerreiro II abrindo os quadris. Flua para Guerreiro Reverso, depois gire para Guerreiro III equilibrando em uma perna. Retorne em pé e repita do outro lado.", "tips": "Mova-se com a respiração — um movimento por respiração. Mantenha os quadris alinhados em cada guerreiro. Use drishti (ponto de olhar) para melhorar o equilíbrio.", "duration": "Complete 3-5 rodadas de cada lado como parte de uma prática mais longa", "contraindications": "Lesões no joelho, problemas no quadril, dificuldades de equilíbrio"},
    },
    {
        "slug": "reclined-cow-face",
        "en": {"title": "Reclined Cow Face Pose", "category": "Restorative", "desc": "A supine variation of Gomukhasana that deeply opens the outer hips and glutes with gravity-assisted relaxation, making it accessible for tight hips.", "benefits": "Releases outer hip tension, stretches IT band and piriformis, relieves sciatic discomfort, promotes deep relaxation", "instructions": "Lie on your back. Cross your right knee over the left, stacking knees if possible. Hold the outer edges of both feet. Flex feet to protect knees. Allow gravity to deepen the stretch. Switch sides.", "tips": "If feet are far from hands, use a strap. Ensure knees are stacked, not offset. Keep the lower back relaxed and released toward the floor.", "duration": "Hold 1-3 minutes each side", "contraindications": "Knee injuries, hip replacement, sacroiliac pain"},
        "ja": {"title": "リクライニング牛面のポーズ", "category": "リストラティブ", "desc": "仰向けで行うゴームカーサナのバリエーション。重力の助けを借りて外腰と臀部を深くオープンし、硬い腰にも取り組みやすいです。", "benefits": "外腰の緊張解放、ITバンドと梨状筋のストレッチ、坐骨神経の不快感緩和、深いリラクゼーション促進", "instructions": "仰向けに寝ます。右膝を左膝の上に交差させ、可能なら膝を重ねます。両足の外側を持ちます。膝を守るため足を曲げます。重力がストレッチを深めるままにします。反対側へ。", "tips": "足が手に届かない場合はストラップを使います。膝はずれずに重なっていることを確認します。腰の下は床に向かってリラックスさせます。", "duration": "各側1〜3分ホールド", "contraindications": "膝の怪我、股関節置換術、仙腸関節痛"},
        "pt": {"title": "Pose do Rosto de Vaca Reclinado", "category": "Restaurativo", "desc": "Uma variação supina do Gomukhasana que abre profundamente os quadris externos e glúteos com relaxamento assistido pela gravidade.", "benefits": "Libera tensão no quadril externo, estica banda IT e piriforme, alivia desconforto ciático, promove relaxamento profundo", "instructions": "Deite de costas. Cruze o joelho direito sobre o esquerdo, empilhando os joelhos se possível. Segure as bordas externas de ambos os pés. Flexione os pés para proteger os joelhos. Permita que a gravidade aprofunde o alongamento. Troque de lado.", "tips": "Se os pés estiverem longe das mãos, use uma faixa. Garanta que os joelhos estejam empilhados, não deslocados. Mantenha a lombar relaxada e liberada em direção ao chão.", "duration": "Segure 1-3 minutos de cada lado", "contraindications": "Lesões no joelho, prótese de quadril, dor sacroilíaca"},
    },
    {
        "slug": "full-wheel-urdhva-dhanurasana",
        "en": {"title": "Full Wheel Pose (Urdhva Dhanurasana)", "category": "Backbend", "desc": "An advanced backbend that creates a full arch of the entire spine, opening the chest, shoulders, and hip flexors while building tremendous strength.", "benefits": "Strengthens arms, wrists, legs, and spine. Opens chest and shoulders. Energizes the body. Stimulates thyroid and pituitary glands.", "instructions": "Lie on back. Place hands by ears, fingers pointing toward shoulders. Plant feet hip-width. Press firmly into hands and feet, lifting hips and head. Straighten arms fully. Press thighs parallel, roll inner thighs in.", "tips": "Warm up thoroughly with bridge, camel, and sphinx first. Engage legs as strongly as arms. Keep breathing throughout. Come down slowly, tucking chin.", "duration": "Hold 3-8 breaths; practice 1-3 times", "contraindications": "Wrist injuries, back injuries, carpal tunnel, headaches, pregnancy"},
        "ja": {"title": "フルホイールポーズ（ウルドヴァダヌラーサナ）", "category": "後屈", "desc": "脊柱全体で完全なアーチを作る上級後屈。胸・肩・腸腰筋を開きながら、絶大な強さを築きます。", "benefits": "腕・手首・脚・脊柱を強化。胸と肩を開く。体にエネルギーを与える。甲状腺と脳下垂体を刺激する。", "instructions": "仰向けに寝ます。耳の横に手を置き、指を肩に向けます。足を腰幅に植えます。手と足に力強く押し付け、腰と頭を持ち上げます。腕を完全に伸ばします。大腿を平行に保ち、内ももを内側へ。", "tips": "ブリッジ、ラクダ、スフィンクスでしっかりウォームアップしましょう。脚を腕と同じくらい強く使います。常に呼吸します。あごを引きながらゆっくり降りてきます。", "duration": "3〜8呼吸ホールド；1〜3回練習", "contraindications": "手首の怪我、背中の怪我、手根管症候群、頭痛、妊娠"},
        "pt": {"title": "Pose da Roda Completa (Urdhva Dhanurasana)", "category": "Flexão Para Trás", "desc": "Uma flexão avançada para trás que cria um arco completo de toda a coluna, abrindo peito, ombros e flexores do quadril enquanto constrói tremenda força.", "benefits": "Fortalece braços, pulsos, pernas e coluna. Abre peito e ombros. Energiza o corpo. Estimula glândulas tireoide e pituitária.", "instructions": "Deite de costas. Coloque as mãos perto das orelhas, dedos apontando para os ombros. Plante os pés na largura do quadril. Pressione firmemente as mãos e pés, levantando quadris e cabeça. Estenda completamente os braços. Mantenha coxas paralelas, gire as coxas internas para dentro.", "tips": "Aqueça completamente com ponte, camelo e esfinge primeiro. Envolva as pernas tão fortemente quanto os braços. Continue respirando. Desça lentamente, encolhendo o queixo.", "duration": "Segure 3-8 respirações; pratique 1-3 vezes", "contraindications": "Lesões nos pulsos, lesões nas costas, síndrome do túnel do carpo, dores de cabeça, gravidez"},
    },
    {
        "slug": "prasarita-padottanasana-variation",
        "en": {"title": "Wide-Legged Forward Fold Variation", "category": "Standing Forward Fold", "desc": "A variation of Prasarita Padottanasana with hands clasped behind the back, combining a deep hamstring stretch with a shoulder opener.", "benefits": "Stretches hamstrings and inner thighs, opens shoulders and chest, calms the nervous system, improves circulation to the brain", "instructions": "Stand with feet 3-4 feet apart. Interlace fingers behind back. Inhale, lift chest. Exhale, fold forward from hips. Let head hang, arms rise overhead (or as far as comfortable). Keep micro-bend in knees.", "tips": "Work toward bringing the crown of the head to the floor. If shoulders are tight, hold a strap between hands. Keep feet parallel or toes slightly turned in.", "duration": "Hold 5-10 breaths", "contraindications": "Low back injuries, glaucoma, vertigo, hamstring tears"},
        "ja": {"title": "脚を広げた前屈バリエーション", "category": "立位前屈", "desc": "プラサリタパドッタナーサナの、両手を背後で組んだバリエーション。深いハムストリングスのストレッチと肩オープナーを組み合わせます。", "benefits": "ハムストリングと内もものストレッチ、肩と胸を開く、神経系を落ち着かせる、脳への血液循環改善", "instructions": "足を3〜4フィート離して立ちます。背後で指を組みます。息を吸って胸を持ち上げます。息を吐きながら腰から前屈します。頭をぶら下げ、腕を頭上へ（快適な範囲で）。膝を少し曲げます。", "tips": "頭頂部を床に向かって伸ばします。肩が硬い場合は手の間にストラップを使います。足を平行か、つま先を少し内向きに保ちます。", "duration": "5〜10呼吸ホールド", "contraindications": "腰の怪我、緑内障、めまい、ハムストリングの断裂"},
        "pt": {"title": "Variação da Dobra Para Frente com Pernas Abertas", "category": "Dobra em Pé", "desc": "Uma variação do Prasarita Padottanasana com as mãos entrelaçadas atrás das costas, combinando um profundo alongamento dos isquiotibiais com uma abertura de ombros.", "benefits": "Estica isquiotibiais e coxas internas, abre ombros e peito, acalma o sistema nervoso, melhora circulação para o cérebro", "instructions": "Fique com os pés a 3-4 pés de distância. Entrelace os dedos atrás das costas. Inspire, levante o peito. Expire, dobre para frente a partir dos quadris. Deixe a cabeça pendurada, braços sobem acima da cabeça (ou o quanto for confortável). Mantenha micro-dobra nos joelhos.", "tips": "Trabalhe para trazer o topo da cabeça ao chão. Se os ombros estiverem tensos, segure uma faixa entre as mãos. Mantenha os pés paralelos ou dedos levemente virados para dentro.", "duration": "Segure 5-10 respirações", "contraindications": "Lesões lombares, glaucoma, vertigem, rupturas nos isquiotibiais"},
    },
    {
        "slug": "low-lunge-twist",
        "en": {"title": "Low Lunge Twist (Parivrtta Anjaneyasana)", "category": "Twist", "desc": "A revolved low lunge that combines hip flexor opening with a deep spinal rotation, detoxifying and energizing the entire torso.", "benefits": "Opens hip flexors, detoxifies organs through compression, improves spinal rotation, strengthens legs, improves digestion", "instructions": "From low lunge with right foot forward, lower left knee. Place left hand on floor inside right foot. Inhale to lengthen spine. Exhale, rotate torso right, extending right arm toward the ceiling. Stack shoulders. Hold, then switch sides.", "tips": "Ground the back knee firmly. Use the bottom hand as a lever to rotate more deeply. Keep the front knee stacked over the ankle. Breathe into the twist on each exhale.", "duration": "Hold 5-8 breaths each side", "contraindications": "Knee injuries, spinal disc issues, sacroiliac dysfunction"},
        "ja": {"title": "ローランジツイスト（パリヴリッタアンジャネーヤサナ）", "category": "ツイスト", "desc": "腸腰筋オープナーと深い脊椎回旋を組み合わせた回旋付きローランジ。胴体全体を解毒し活性化します。", "benefits": "腸腰筋を開く、圧迫による臓器デトックス、脊椎回旋の改善、脚を強化、消化改善", "instructions": "右足を前にしたローランジから左膝を下げます。右足の内側に左手を置きます。息を吸って脊柱を伸長します。息を吐きながら胴体を右に回転させ、右腕を天井に向けます。肩を重ねます。ホールドして反対側へ。", "tips": "後ろの膝をしっかり地面につけます。下の手をレバーとして使いより深く回転します。前の膝を足首の上に保ちます。息を吐くごとにツイストに呼吸を送ります。", "duration": "各側5〜8呼吸ホールド", "contraindications": "膝の怪我、椎間板の問題、仙腸関節機能障害"},
        "pt": {"title": "Torção no Lunge Baixo (Parivrtta Anjaneyasana)", "category": "Torção", "desc": "Um lunge baixo revertido que combina abertura do flexor do quadril com uma profunda rotação espinhal, desintoxicando e energizando todo o tronco.", "benefits": "Abre flexores do quadril, desintoxica órgãos através de compressão, melhora rotação espinhal, fortalece pernas, melhora digestão", "instructions": "Do lunge baixo com o pé direito à frente, abaixe o joelho esquerdo. Coloque a mão esquerda no chão dentro do pé direito. Inspire para alongar a coluna. Expire, gire o tronco para a direita, estendendo o braço direito em direção ao teto. Empilhe os ombros. Segure e troque de lado.", "tips": "Firme bem o joelho traseiro. Use a mão inferior como alavanca para girar mais profundamente. Mantenha o joelho da frente sobre o tornozelo. Respire para a torção a cada expiração.", "duration": "Segure 5-8 respirações de cada lado", "contraindications": "Lesões no joelho, problemas no disco espinhal, disfunção sacroilíaca"},
    },
    {
        "slug": "eagle-pose-garudasana",
        "en": {"title": "Eagle Pose (Garudasana)", "category": "Balance", "desc": "A powerful standing balance pose where the limbs are wrapped around each other, requiring focus, coordination, and opening of the upper back.", "benefits": "Improves balance and concentration, opens upper back and shoulders, stretches hips and IT bands, strengthens standing leg", "instructions": "Stand in mountain pose. Bend knees slightly. Lift right foot and cross right thigh over left. Try to hook right foot behind left calf. Cross left arm over right at elbow, then wrap forearms, pressing palms together. Lift elbows to shoulder height. Hold and switch sides.", "tips": "If wrapping is difficult, use a strap between hands. Focus your gaze on a fixed point. Sit deeper into the pose for a more intense hip stretch.", "duration": "Hold 5-10 breaths each side", "contraindications": "Knee injuries, ankle sprains, vertigo"},
        "ja": {"title": "イーグルポーズ（ガルダーサナ）", "category": "バランス", "desc": "四肢を互いに巻き付ける強力な立位バランスポーズ。集中力・協調性・上背部のオープニングが必要です。", "benefits": "バランスと集中力の改善、上背部と肩を開く、腰とITバンドのストレッチ、立位の脚を強化", "instructions": "山のポーズで立ちます。軽く膝を曲げます。右足を持ち上げ、右大腿を左の上に交差させます。右足を左ふくらはぎの後ろに引っ掛けます。左腕を右腕の上に交差させ、前腕を巻いて手のひらを合わせます。肘を肩の高さに持ち上げます。ホールドして反対側へ。", "tips": "巻き付けが難しい場合は手の間にストラップを使います。固定した点に視線を向けます。より強いヒップストレッチのためにポーズを深めます。", "duration": "各側5〜10呼吸ホールド", "contraindications": "膝の怪我、足首の捻挫、めまい"},
        "pt": {"title": "Pose da Águia (Garudasana)", "category": "Equilíbrio", "desc": "Uma poderosa pose de equilíbrio em pé onde os membros são enrolados uns nos outros, exigindo foco, coordenação e abertura da parte superior das costas.", "benefits": "Melhora equilíbrio e concentração, abre parte superior das costas e ombros, estica quadris e bandas IT, fortalece perna de apoio", "instructions": "Fique na pose da montanha. Dobre levemente os joelhos. Levante o pé direito e cruze a coxa direita sobre a esquerda. Tente enganchar o pé direito atrás da panturrilha esquerda. Cruze o braço esquerdo sobre o direito no cotovelo, depois envolva os antebraços, pressionando as palmas juntas. Levante os cotovelos à altura dos ombros. Segure e troque de lado.", "tips": "Se o enrolamento for difícil, use uma faixa entre as mãos. Fixe o olhar em um ponto fixo. Sente-se mais fundo na pose para um alongamento de quadril mais intenso.", "duration": "Segure 5-10 respirações de cada lado", "contraindications": "Lesões no joelho, entorses de tornozelo, vertigem"},
    },
    {
        "slug": "revolved-triangle-pose",
        "en": {"title": "Revolved Triangle Pose (Parivrtta Trikonasana)", "category": "Twist", "desc": "A challenging standing twist that demands hamstring flexibility, core strength, and balance — considered one of the most beneficial yet demanding yoga poses.", "benefits": "Strengthens legs, stimulates abdominal organs, improves digestion and circulation, stretches spine and hamstrings, develops balance", "instructions": "Stand with feet 3-4 feet apart. Turn right foot out 90°, left foot in 45°. Square hips toward right foot. Inhale, extend arms. Exhale, hinge forward keeping back flat. Place left hand outside or on a block by right foot. Open right arm toward sky. Hold, then switch.", "tips": "Use a block if needed — don't sacrifice spinal length for depth. Engage your core strongly. Maintain length in both sides of the torso.", "duration": "Hold 5-8 breaths each side", "contraindications": "Low back pain, hamstring injury, high blood pressure"},
        "ja": {"title": "回転三角のポーズ（パリヴリッタトリコナーサナ）", "category": "ツイスト", "desc": "ハムストリングスの柔軟性・コアの強さ・バランスを要求する難易度の高い立位ツイスト。最も有益かつ要求が高いヨガポーズの一つとされています。", "benefits": "脚を強化、腹部臓器を刺激、消化と循環改善、脊柱とハムストリングスのストレッチ、バランス開発", "instructions": "足を3〜4フィート離して立ちます。右足を90°外向きに、左足を45°内向きに。腰を右足に向けて正方形にします。息を吸って腕を伸ばします。背中を平らに保ちながら息を吐いて前屈します。右足の外側か横のブロックに左手を置きます。右腕を空に向けて開きます。ホールドして反対側へ。", "tips": "必要に応じてブロックを使います — 深さのために脊柱の長さを犠牲にしません。コアをしっかり使います。胴体の両側の長さを保ちます。", "duration": "各側5〜8呼吸ホールド", "contraindications": "腰痛、ハムストリングの怪我、高血圧"},
        "pt": {"title": "Pose do Triângulo Revertido (Parivrtta Trikonasana)", "category": "Torção", "desc": "Uma exigente torção em pé que demanda flexibilidade dos isquiotibiais, força do core e equilíbrio — considerada uma das poses de yoga mais benéficas e desafiadoras.", "benefits": "Fortalece pernas, estimula órgãos abdominais, melhora digestão e circulação, estica coluna e isquiotibiais, desenvolve equilíbrio", "instructions": "Fique com os pés a 3-4 pés de distância. Vire o pé direito 90°, o esquerdo 45°. Quadre os quadris em direção ao pé direito. Inspire, estenda os braços. Expire, incline para frente mantendo a costas reta. Coloque a mão esquerda fora ou em um bloco perto do pé direito. Abra o braço direito em direção ao céu. Segure e troque.", "tips": "Use um bloco se necessário — não sacrifique o comprimento espinhal pela profundidade. Envolva o core fortemente. Mantenha comprimento em ambos os lados do tronco.", "duration": "Segure 5-8 respirações de cada lado", "contraindications": "Dor lombar, lesão nos isquiotibiais, pressão alta"},
    },
    {
        "slug": "wide-child-pose-variation",
        "en": {"title": "Wide-Knee Child's Pose Variation", "category": "Restorative", "desc": "A variation of Balasana with wider knees and arms extended in different directions to target specific areas of the hips, sides, and upper back.", "benefits": "Releases hip tension, stretches upper back and lats, calms the nervous system, provides a moment of rest during practice", "instructions": "From kneeling, spread knees wide, big toes together. Walk hands to the right, melting the left shoulder toward the floor. Hold, then walk hands center, then left for the other side. Also try both arms extended and in prayer.", "tips": "Place a blanket under knees or torso for comfort. Let the breath naturally release into the floor. Rest for as long as needed.", "duration": "Hold each variation 1-3 minutes", "contraindications": "Knee injuries, ankle issues, pregnancy"},
        "ja": {"title": "ワイドニーチャイルドポーズバリエーション", "category": "リストラティブ", "desc": "バラーサナのバリエーション。膝を広げて腕を様々な方向に伸ばし、腰・体側・上背部の特定の部位にアプローチします。", "benefits": "腰の緊張解放、上背部と広背筋のストレッチ、神経系を落ち着かせる、練習中の休息の時間を提供", "instructions": "膝立ちから膝を広げ、親指を合わせます。両手を右に歩かせ、左肩を床に向けて溶け込ませます。ホールドして手を中央に戻し、左へ。両腕を前方に伸ばしたり、合掌したりも試しましょう。", "tips": "膝や胴体の下に毛布を置いてもいいです。呼吸が自然に床に解放されるままにします。必要な時間だけ休みます。", "duration": "各バリエーション1〜3分ホールド", "contraindications": "膝の怪我、足首の問題、妊娠"},
        "pt": {"title": "Variação da Pose da Criança com Joelhos Abertos", "category": "Restaurativo", "desc": "Uma variação de Balasana com joelhos mais abertos e braços estendidos em diferentes direções para atingir áreas específicas dos quadris, lados e parte superior das costas.", "benefits": "Libera tensão no quadril, estica parte superior das costas e latíssimos, acalma o sistema nervoso, proporciona um momento de descanso durante a prática", "instructions": "Da posição ajoelhada, espalhe os joelhos largos, dedões juntos. Caminhe as mãos para a direita, derretendo o ombro esquerdo em direção ao chão. Segure, depois caminhe as mãos para o centro, depois para a esquerda no outro lado. Tente também com ambos os braços estendidos e em posição de oração.", "tips": "Coloque um cobertor sob os joelhos ou tronco para conforto. Deixe a respiração se soltar naturalmente para o chão. Descanse pelo tempo necessário.", "duration": "Segure cada variação 1-3 minutos", "contraindications": "Lesões no joelho, problemas no tornozelo, gravidez"},
    },
    {
        "slug": "supported-savasana-variations",
        "en": {"title": "Supported Savasana Variations", "category": "Restorative", "desc": "Variations of the classic corpse pose using props to maximize relaxation, address specific tension areas, and deepen the rest experience.", "benefits": "Complete muscular relaxation, reduces stress hormones, integrates yoga practice benefits, calms nervous system, improves sleep quality", "instructions": "Option 1: Place bolster under knees for low back relief. Option 2: Sandbag on belly for grounding. Option 3: Eye pillow over eyes for sensory withdrawal. Option 4: Folded blanket under head. Lie completely still, allowing all effort to dissolve.", "tips": "Keep warm — body temperature drops in savasana. Set a timer so you can fully let go. Aim for 5-15 minutes at the end of practice.", "duration": "5-15 minutes ideally; minimum 5 minutes", "contraindications": "Pregnancy (use side lying), severe GERD (use slight incline)"},
        "ja": {"title": "サポートされたシャヴァーサナバリエーション", "category": "リストラティブ", "desc": "プロップスを使ったクラシックなコープスポーズのバリエーション。リラクゼーションを最大化し、特定の緊張部位にアプローチし、休息体験を深めます。", "benefits": "完全な筋肉リラクゼーション、ストレスホルモン低下、ヨガ練習の恩恵を統合、神経系を落ち着かせる、睡眠の質向上", "instructions": "オプション1: 腰の緩和のため膝の下にボルスター。オプション2: グラウンディングのためお腹にサンドバッグ。オプション3: 感覚遮断のため目の上にアイピロー。オプション4: 頭の下に折りたたんだブランケット。完全に静止し、すべての努力を溶かします。", "tips": "暖かくしてください — シャヴァーサナでは体温が下がります。完全に手放せるようにタイマーをセットします。練習の終わりに5〜15分を目指します。", "duration": "理想的には5〜15分；最低5分", "contraindications": "妊娠（横向きを使用）、重篤なGERD（軽い傾斜を使用）"},
        "pt": {"title": "Variações de Savasana com Suporte", "category": "Restaurativo", "desc": "Variações da clássica pose do cadáver usando adereços para maximizar o relaxamento, abordar áreas específicas de tensão e aprofundar a experiência de descanso.", "benefits": "Relaxamento muscular completo, reduz hormônios do estresse, integra benefícios da prática de yoga, acalma sistema nervoso, melhora qualidade do sono", "instructions": "Opção 1: Coloque bolster sob os joelhos para aliviar a lombar. Opção 2: Saco de areia na barriga para enraizamento. Opção 3: Travesseiro para os olhos para retirada sensorial. Opção 4: Cobertor dobrado sob a cabeça. Fique completamente imóvel, deixando todo esforço se dissolver.", "tips": "Fique aquecido — a temperatura corporal cai no savasana. Defina um timer para poder soltar completamente. Objetive 5-15 minutos no final da prática.", "duration": "5-15 minutos idealmente; mínimo 5 minutos", "contraindications": "Gravidez (use deitado de lado), GERD severo (use leve inclinação)"},
    },
    {
        "slug": "paschimottanasana-seated-forward-bend",
        "en": {"title": "Seated Forward Bend (Paschimottanasana)", "category": "Seated Forward Fold", "desc": "The quintessential seated forward fold that stretches the entire back body — from the heels to the crown of the head — with a calming, introspective quality.", "benefits": "Deeply stretches hamstrings and spine, calms the nervous system, stimulates digestive organs, relieves stress and mild depression, improves kidney function", "instructions": "Sit with legs extended. Flex feet, pressing through heels. Inhale, lengthen spine tall. Exhale, hinge forward from hips. Reach for feet, shins, or use a strap. Keep spine long rather than rounding. Relax head and neck.", "tips": "Prioritize a long spine over reaching the feet. Bend knees slightly if needed. Use a strap to maintain length. Each exhale, allow a gentle release deeper.", "duration": "Hold 1-5 minutes, breathing deeply", "contraindications": "Herniated disc, sciatica, hamstring tears, asthma"},
        "ja": {"title": "座位前屈（パシュチモッタナーサナ）", "category": "座位前屈", "desc": "かかとから頭頂部まで背面全体をストレッチする典型的な座位前屈。落ち着いた内省的な質を持ちます。", "benefits": "ハムストリングスと脊柱の深いストレッチ、神経系を落ち着かせる、消化器官を刺激、ストレスと軽い鬱を和らげる、腎機能改善", "instructions": "足を伸ばして座ります。足を曲げ、かかとで押し出します。息を吸って背骨を高く伸ばします。腰からヒンジして息を吐きながら前屈します。足・すね、またはストラップに手を伸ばします。背骨を丸めずに長く保ちます。頭と首をリラックスさせます。", "tips": "足に届くことより長い脊柱を優先します。必要なら膝を少し曲げます。長さを保つためにストラップを使います。息を吐くごとに穏やかに深まるままにします。", "duration": "深く呼吸しながら1〜5分ホールド", "contraindications": "椎間板ヘルニア、坐骨神経痛、ハムストリングの断裂、喘息"},
        "pt": {"title": "Dobra Para Frente Sentado (Paschimottanasana)", "category": "Dobra Sentado", "desc": "A essência da dobra para frente sentado que estica todo o corpo posterior — dos calcanhares ao topo da cabeça — com uma qualidade calmante e introspectiva.", "benefits": "Estica profundamente isquiotibiais e coluna, acalma sistema nervoso, estimula órgãos digestivos, alivia estresse e depressão leve, melhora função renal", "instructions": "Sente com as pernas estendidas. Flexione os pés, pressionando pelos calcanhares. Inspire, alongue a coluna em altura. Expire, incline para frente a partir dos quadris. Alcance os pés, canelas ou use uma faixa. Mantenha a coluna longa em vez de curvar. Relaxe cabeça e pescoço.", "tips": "Priorize uma coluna longa ao invés de alcançar os pés. Dobre levemente os joelhos se necessário. Use uma faixa para manter o comprimento. A cada expiração, permita uma suave liberação mais profunda.", "duration": "Segure 1-5 minutos, respirando profundamente", "contraindications": "Hérnia de disco, ciática, rupturas nos isquiotibiais, asma"},
    },
    {
        "slug": "firefly-pose-tittibhasana",
        "en": {"title": "Firefly Pose (Tittibhasana)", "category": "Arm Balance", "desc": "An advanced arm balance where the body is held horizontally, legs extended out to the sides — requiring tremendous wrist strength, hamstring flexibility, and core stability.", "benefits": "Builds extreme wrist and arm strength, opens hamstrings dramatically, strengthens core, challenges coordination and mental focus", "instructions": "From a forward fold, squat deep. Thread arms under thighs, placing hands flat on floor. Shift weight into hands, lifting feet. Extend legs straight out to sides. Hold gaze forward. Lower feet slowly.", "tips": "Build shoulder and wrist strength extensively before attempting. Practice with feet on blocks first. Core strength is essential — keep a strong hollow body shape.", "duration": "Hold 3-5 breaths when achieved; practice preparations daily", "contraindications": "Wrist injuries, shoulder injuries, hamstring tears, beginner practitioners"},
        "ja": {"title": "ホタルのポーズ（ティティバーサナ）", "category": "アームバランス", "desc": "体を水平に保ち、脚を両側に伸ばす上級アームバランス。手首の強さ・ハムストリングスの柔軟性・コアの安定性が必要です。", "benefits": "手首と腕の極端な強化、ハムストリングスの劇的なオープニング、コア強化、協調性と精神的集中への挑戦", "instructions": "前屈から深くスクワットします。腕を大腿の下に通し、手を床に平らに置きます。手に体重を移し、足を持ち上げます。脚を両側に真っ直ぐ伸ばします。視線を前に向けます。足をゆっくり下ろします。", "tips": "試みる前に肩と手首の強さを十分に築きます。最初はブロックの上に足を置いて練習します。コアの強さが不可欠 — 強いホロウボディシェイプを維持します。", "duration": "達成したら3〜5呼吸ホールド；毎日準備練習", "contraindications": "手首の怪我、肩の怪我、ハムストリングの断裂、初心者"},
        "pt": {"title": "Pose do Vagalume (Tittibhasana)", "category": "Equilíbrio nos Braços", "desc": "Um equilíbrio avançado nos braços onde o corpo é mantido horizontalmente, pernas estendidas para os lados — exigindo tremenda força nos pulsos, flexibilidade dos isquiotibiais e estabilidade do core.", "benefits": "Constrói força extrema nos pulsos e braços, abre dramaticamente os isquiotibiais, fortalece o core, desafia coordenação e foco mental", "instructions": "De uma dobra para frente, agache fundo. Passe os braços por baixo das coxas, colocando as mãos planas no chão. Transfira o peso para as mãos, levantando os pés. Estenda as pernas retas para os lados. Mantenha o olhar para frente. Abaixe os pés lentamente.", "tips": "Construa força nos ombros e pulsos extensivamente antes de tentar. Pratique com os pés em blocos primeiro. Força do core é essencial — mantenha uma forma forte de corpo oco.", "duration": "Segure 3-5 respirações quando conseguido; pratique preparações diariamente", "contraindications": "Lesões nos pulsos, lesões nos ombros, rupturas nos isquiotibiais, praticantes iniciantes"},
    },
    {
        "slug": "seated-wide-angle-forward-bend",
        "en": {"title": "Seated Wide Angle Forward Bend (Upavistha Konasana)", "category": "Seated Forward Fold", "desc": "A wide-legged seated forward fold that targets the inner thighs, hamstrings, and spine, creating a peaceful, grounding sensation.", "benefits": "Stretches inner thighs and hamstrings, strengthens spine, releases tight groins, calms nervous system, improves hip and groin flexibility", "instructions": "Sit with legs open as wide as comfortable (90-180°). Flex feet. Inhale, lengthen spine. Exhale, fold forward from hips, walking hands between legs. Keep back flat as long as possible. Rest forehead on floor or bolster.", "tips": "Don't force the legs wider than comfortable. Use a blanket under hips if pelvis tilts back. Walk hands forward slowly, breath by breath.", "duration": "Hold 1-5 minutes", "contraindications": "Groin injuries, hamstring tears, sciatica"},
        "ja": {"title": "座位広角前屈（ウパビシュタコナーサナ）", "category": "座位前屈", "desc": "内ももとハムストリングスと脊柱を対象にする、広脚座位前屈。平和でグラウンディングされた感覚を作ります。", "benefits": "内ももとハムストリングスのストレッチ、脊柱の強化、硬い鼠蹊部の解放、神経系を落ち着かせる、腰と鼠蹊部の柔軟性向上", "instructions": "脚を快適な範囲でできるだけ広く開いて座ります（90〜180°）。足を曲げます。息を吸って脊柱を伸長します。腰からヒンジして息を吐きながら前屈し、脚の間に手を歩かせます。できるだけ長く背中を平らに保ちます。額を床かボルスターに乗せます。", "tips": "快適な範囲以上に脚を広げません。骨盤が後ろに倒れる場合は腰の下に毛布を使います。呼吸ごとにゆっくり手を前に歩かせます。", "duration": "1〜5分ホールド", "contraindications": "鼠蹊部の怪我、ハムストリングの断裂、坐骨神経痛"},
        "pt": {"title": "Dobra Para Frente Sentado com Ângulo Amplo (Upavistha Konasana)", "category": "Dobra Sentado", "desc": "Uma dobra para frente sentado com pernas abertas que visa a face interna das coxas, isquiotibiais e coluna, criando uma sensação pacífica e de enraizamento.", "benefits": "Estica face interna das coxas e isquiotibiais, fortalece coluna, libera virilhas tensas, acalma sistema nervoso, melhora flexibilidade do quadril e virilha", "instructions": "Sente com as pernas abertas o mais confortável possível (90-180°). Flexione os pés. Inspire, alongue a coluna. Expire, dobre para frente a partir dos quadris, caminhando as mãos entre as pernas. Mantenha as costas retas o máximo possível. Descanse a testa no chão ou bolster.", "tips": "Não force as pernas mais abertas do que confortável. Use um cobertor sob os quadris se a pelve inclinar para trás. Caminhe as mãos para frente lentamente, respiração por respiração.", "duration": "Segure 1-5 minutos", "contraindications": "Lesões na virilha, rupturas nos isquiotibiais, ciática"},
    },
    {
        "slug": "childs-pose-extended-arms",
        "en": {"title": "Child's Pose with Extended Arms", "category": "Restorative", "desc": "The classic Balasana with arms stretched overhead, creating an active stretch through the upper body while maintaining the grounding, restorative quality of child's pose.", "benefits": "Stretches upper back and lats, releases shoulder tension, decompresses the spine, calms the mind, provides an active rest", "instructions": "From kneeling, knees hip-width or together. Extend arms forward on the floor. Lower torso between or over thighs. Rest forehead on floor. Breathe into the back body, feeling it expand with each inhale. Walk hands further for deeper shoulder stretch.", "tips": "If the forehead doesn't reach the floor, rest it on stacked fists or a block. Actively reach through the fingertips for a more intense shoulder stretch. Breathe deeply into the back ribs.", "duration": "Hold 1-5 minutes as needed during practice", "contraindications": "Knee injuries, ankle injuries, diarrhea, pregnancy"},
        "ja": {"title": "アームエクステンドのチャイルドポーズ", "category": "リストラティブ", "desc": "腕を頭上に伸ばしたクラシックなバラーサナ。上半身を通じてアクティブなストレッチを作りながら、チャイルドポーズのグラウンディングとリストラティブな質を維持します。", "benefits": "上背部と広背筋のストレッチ、肩の緊張解放、脊柱の減圧、心を落ち着かせる、アクティブな休息を提供", "instructions": "膝立ちから、膝を腰幅か揃えます。両腕を床に前方に伸ばします。胴体を大腿の間か上に下ろします。額を床に乗せます。背面に呼吸を送り、息を吸うごとに広がるのを感じます。より深い肩のストレッチのために両手をより前方に歩かせます。", "tips": "額が床に届かない場合は重ねた拳かブロックの上に乗せます。より強い肩のストレッチのために指先を通じて積極的に伸ばします。背中の肋骨に深く呼吸します。", "duration": "練習中に必要に応じて1〜5分ホールド", "contraindications": "膝の怪我、足首の怪我、下痢、妊娠"},
        "pt": {"title": "Pose da Criança com Braços Estendidos", "category": "Restaurativo", "desc": "O clássico Balasana com braços estendidos acima da cabeça, criando um alongamento ativo através da parte superior do corpo enquanto mantém a qualidade restaurativa de enraizamento da pose da criança.", "benefits": "Estica parte superior das costas e latíssimos, libera tensão nos ombros, descomprime a coluna, acalma a mente, proporciona descanso ativo", "instructions": "Da posição ajoelhada, joelhos na largura do quadril ou juntos. Estenda os braços para frente no chão. Abaixe o tronco entre ou sobre as coxas. Descanse a testa no chão. Respire para o corpo posterior, sentindo-o expandir a cada inspiração. Caminhe as mãos mais longe para alongamento mais profundo dos ombros.", "tips": "Se a testa não alcançar o chão, descanse em punhos empilhados ou um bloco. Alcance ativamente através das pontas dos dedos para um alongamento de ombros mais intenso. Respire profundamente para as costelas posteriores.", "duration": "Segure 1-5 minutos conforme necessário durante a prática", "contraindications": "Lesões no joelho, lesões no tornozelo, diarreia, gravidez"},
    },
    {
        "slug": "downward-dog-variations",
        "en": {"title": "Downward Dog Variations", "category": "Inversion", "desc": "Explorations of Adho Mukha Svanasana with different arm and leg positions to target specific areas, build strength, and add variety to this foundational pose.", "benefits": "Strengthens arms and legs, stretches hamstrings and calves, energizes the body, improves circulation, builds shoulder stability", "instructions": "From standard down dog: (1) Three-legged dog — lift one leg. (2) Down dog with bent knees to focus on spine length. (3) Puppy dog — lower chest toward floor with bent knees. (4) Walk the dog — alternate heel presses. (5) Twisted dog — reach one hand to opposite shin.", "tips": "In all variations, maintain a long spine as the priority. Keep hands wide and actively push the floor away. Breathe into the back body.", "duration": "Hold each variation 5-10 breaths; include in warm-up or cool-down", "contraindications": "Carpal tunnel, shoulder injuries, high blood pressure, late pregnancy"},
        "ja": {"title": "ダウンワードドッグバリエーション", "category": "逆転ポーズ", "desc": "様々な腕と脚のポジションを使ったアドムカシュヴァナーサナの探求。特定の部位を対象とし、強さを築き、この基本的なポーズにバリエーションを加えます。", "benefits": "腕と脚の強化、ハムストリングスとふくらはぎのストレッチ、体を活性化、循環改善、肩の安定性構築", "instructions": "スタンダードなダウンドッグから：(1) スリーレッグドドッグ — 片脚を持ち上げる。(2) 膝を曲げたダウンドッグで脊柱の長さに集中。(3) パピードッグ — 膝を曲げて胸を床に向けて下ろす。(4) ウォークザドッグ — かかとを交互に押す。(5) ツイストドッグ — 片手を反対側のすねに伸ばす。", "tips": "すべてのバリエーションで、優先事項として長い脊柱を維持します。手を広く開け、床を積極的に押し離します。背面に呼吸を送ります。", "duration": "各バリエーション5〜10呼吸ホールド；ウォームアップかクールダウンに含める", "contraindications": "手根管症候群、肩の怪我、高血圧、後期妊娠"},
        "pt": {"title": "Variações do Cão Olhando Para Baixo", "category": "Inversão", "desc": "Explorações de Adho Mukha Svanasana com diferentes posições de braços e pernas para atingir áreas específicas, construir força e adicionar variedade a esta pose fundamental.", "benefits": "Fortalece braços e pernas, estica isquiotibiais e panturrilhas, energiza o corpo, melhora circulação, constrói estabilidade nos ombros", "instructions": "Do cão para baixo padrão: (1) Cão de três pernas — levante uma perna. (2) Cão para baixo com joelhos dobrados para focar no comprimento da coluna. (3) Pose do filhote — abaixe o peito em direção ao chão com joelhos dobrados. (4) Caminhe o cão — pressione os calcanhares alternadamente. (5) Cão torcido — alcance uma mão para a canela oposta.", "tips": "Em todas as variações, mantenha uma coluna longa como prioridade. Mantenha as mãos largas e empurre ativamente o chão. Respire para o corpo posterior.", "duration": "Segure cada variação 5-10 respirações; inclua no aquecimento ou resfriamento", "contraindications": "Túnel do carpo, lesões nos ombros, pressão alta, gravidez avançada"},
    },
]

def build_amazon_section(lang):
    if lang == "en":
        return f"""<div style="background:linear-gradient(135deg,#1a0a2e,#0d0820);border:1px solid #e94560;border-radius:12px;padding:20px 24px;margin:32px 0;text-align:center">
<p style="font-size:1rem;font-weight:700;margin-bottom:6px">🛒 Yoga Equipment on Amazon</p>
<p style="color:#aaa;font-size:0.85rem;margin-bottom:12px">Premium yoga mats, blocks, and straps</p>
<a href="https://www.amazon.com/s?k=yoga+mat+premium&tag={AMAZON_TAG}" target="_blank" rel="noopener sponsored" style="background:#e94560;color:#fff;padding:8px 20px;border-radius:8px;text-decoration:none;font-weight:600;font-size:0.9rem">Shop Yoga Gear →</a>
</div>"""
    elif lang == "ja":
        return f"""<div style="background:linear-gradient(135deg,#1a0a2e,#0d0820);border:1px solid #e94560;border-radius:12px;padding:20px 24px;margin:32px 0;text-align:center">
<p style="font-size:1rem;font-weight:700;margin-bottom:6px">🛒 Amazonでヨガ用品を見る</p>
<p style="color:#aaa;font-size:0.85rem;margin-bottom:12px">プレミアムヨガマット、ブロック、ストラップ</p>
<a href="https://www.amazon.co.jp/s?k=ヨガマット+プレミアム&tag={AMAZON_TAG}" target="_blank" rel="noopener sponsored" style="background:#e94560;color:#fff;padding:8px 20px;border-radius:8px;text-decoration:none;font-weight:600;font-size:0.9rem">ヨガ用品を見る →</a>
</div>"""
    else:
        return f"""<div style="background:linear-gradient(135deg,#1a0a2e,#0d0820);border:1px solid #e94560;border-radius:12px;padding:20px 24px;margin:32px 0;text-align:center">
<p style="font-size:1rem;font-weight:700;margin-bottom:6px">🛒 Equipamentos de Yoga na Amazon</p>
<p style="color:#aaa;font-size:0.85rem;margin-bottom:12px">Tapetes, blocos e faixas premium</p>
<a href="https://www.amazon.com.br/s?k=tapete+yoga+premium&tag={AMAZON_TAG}" target="_blank" rel="noopener sponsored" style="background:#e94560;color:#fff;padding:8px 20px;border-radius:8px;text-decoration:none;font-weight:600;font-size:0.9rem">Comprar Equipamentos →</a>
</div>"""

def build_bjj_cta(lang):
    if lang == "en":
        return f"""<div style="background:linear-gradient(135deg,#16213e,#0f3460);border:1px solid rgba(233,69,96,0.3);border-radius:12px;padding:20px 24px;margin:32px 0;text-align:center">
<p style="font-size:0.9rem;color:#e94560;font-weight:700;margin-bottom:6px">🥋 Also Training BJJ?</p>
<p style="color:#aaa;font-size:0.85rem;margin-bottom:12px">Track your jiu-jitsu sessions, techniques, and progress</p>
<a href="{BJJ_APP_URL}" target="_blank" rel="noopener" style="background:#e94560;color:#fff;padding:8px 20px;border-radius:8px;text-decoration:none;font-weight:600;font-size:0.9rem">Try BJJ App Free →</a>
</div>"""
    elif lang == "ja":
        return f"""<div style="background:linear-gradient(135deg,#16213e,#0f3460);border:1px solid rgba(233,69,96,0.3);border-radius:12px;padding:20px 24px;margin:32px 0;text-align:center">
<p style="font-size:0.9rem;color:#e94560;font-weight:700;margin-bottom:6px">🥋 柔術も練習していますか？</p>
<p style="color:#aaa;font-size:0.85rem;margin-bottom:12px">BJJのセッション・テクニック・進捗を記録しよう</p>
<a href="{BJJ_APP_URL}" target="_blank" rel="noopener" style="background:#e94560;color:#fff;padding:8px 20px;border-radius:8px;text-decoration:none;font-weight:600;font-size:0.9rem">BJJ Appを無料で試す →</a>
</div>"""
    else:
        return f"""<div style="background:linear-gradient(135deg,#16213e,#0f3460);border:1px solid rgba(233,69,96,0.3);border-radius:12px;padding:20px 24px;margin:32px 0;text-align:center">
<p style="font-size:0.9rem;color:#e94560;font-weight:700;margin-bottom:6px">🥋 Também Pratica BJJ?</p>
<p style="color:#aaa;font-size:0.85rem;margin-bottom:12px">Acompanhe suas sessões, técnicas e progresso no jiu-jitsu</p>
<a href="{BJJ_APP_URL}" target="_blank" rel="noopener" style="background:#e94560;color:#fff;padding:8px 20px;border-radius:8px;text-decoration:none;font-weight:600;font-size:0.9rem">Experimente BJJ App Grátis →</a>
</div>"""

def generate_page(pose, lang):
    d = pose[lang]
    slug = pose["slug"]
    title = d["title"]
    category = d["category"]
    desc = d["desc"]
    benefits = d["benefits"]
    instructions = d["instructions"]
    tips = d["tips"]
    duration = d["duration"]
    contraindications = d["contraindications"]

    if lang == "en":
        lang_label = "English"
        other_langs = [("日本語", f"../ja/{slug}.html"), ("Português", f"../pt/{slug}.html")]
        index_link = ("← All Poses", "../index.html")
        headings = {"benefits": "Benefits", "instructions": "How to Do It", "tips": "Tips", "duration": "Duration / Frequency", "contraindications": "Contraindications"}
    elif lang == "ja":
        lang_label = "日本語"
        other_langs = [("English", f"../en/{slug}.html"), ("Português", f"../pt/{slug}.html")]
        index_link = ("← 全ポーズ一覧", "../index.html")
        headings = {"benefits": "効果・メリット", "instructions": "やり方", "tips": "ポイント・コツ", "duration": "時間・頻度", "contraindications": "禁忌・注意事項"}
    else:
        lang_label = "Português"
        other_langs = [("English", f"../en/{slug}.html"), ("日本語", f"../ja/{slug}.html")]
        index_link = ("← Todas as Poses", "../index.html")
        headings = {"benefits": "Benefícios", "instructions": "Como Fazer", "tips": "Dicas", "duration": "Duração / Frequência", "contraindications": "Contraindicações"}

    other_lang_links = " | ".join(f'<a href="{url}" style="color:#e94560;text-decoration:none">{lbl}</a>' for lbl, url in other_langs)

    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} — Yoga Wiki</title>
<meta name="description" content="{desc[:155]}">
<meta property="og:title" content="{title} — Yoga Wiki">
<meta property="og:description" content="{desc[:155]}">
<meta property="og:type" content="article">
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id={GA4}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{GA4}');
</script>
<style>
  *{{box-sizing:border-box;margin:0;padding:0}}
  body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:#0d0d1a;color:#e0e0e0;line-height:1.7;font-size:16px}}
  .container{{max-width:780px;margin:0 auto;padding:20px 16px 60px}}
  header{{background:linear-gradient(135deg,#16213e,#0f3460);padding:16px 20px;margin-bottom:24px;border-radius:12px;border:1px solid rgba(233,69,96,0.2)}}
  .nav{{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px}}
  .nav a{{color:#e94560;text-decoration:none;font-size:0.9rem}}
  h1{{font-size:1.8rem;font-weight:800;margin:20px 0 8px;color:#fff}}
  .category-badge{{display:inline-block;background:#e94560;color:#fff;padding:3px 12px;border-radius:20px;font-size:0.8rem;font-weight:600;margin-bottom:16px}}
  .desc{{font-size:1rem;color:#bbb;margin-bottom:24px;line-height:1.8}}
  .section{{background:#16213e;border:1px solid rgba(255,255,255,0.08);border-radius:12px;padding:20px;margin-bottom:16px}}
  .section h2{{font-size:1.05rem;font-weight:700;color:#e94560;margin-bottom:12px}}
  .section p{{color:#ccc;line-height:1.75;font-size:0.95rem}}
  footer{{text-align:center;color:#555;font-size:0.8rem;margin-top:40px}}
</style>
</head>
<body>
<div class="container">
  <header>
    <div class="nav">
      <a href="{index_link[1]}">{index_link[0]}</a>
      <span style="font-size:0.85rem;color:#aaa">{other_lang_links}</span>
    </div>
  </header>

  <h1>{title}</h1>
  <span class="category-badge">{category}</span>
  <p class="desc">{desc}</p>

  <div class="section">
    <h2>✨ {headings["benefits"]}</h2>
    <p>{benefits}</p>
  </div>

  <div class="section">
    <h2>📋 {headings["instructions"]}</h2>
    <p>{instructions}</p>
  </div>

  <div class="section">
    <h2>💡 {headings["tips"]}</h2>
    <p>{tips}</p>
  </div>

  <div class="section">
    <h2>⏱️ {headings["duration"]}</h2>
    <p>{duration}</p>
  </div>

  <div class="section">
    <h2>⚠️ {headings["contraindications"]}</h2>
    <p>{contraindications}</p>
  </div>

  {build_amazon_section(lang)}
  {build_bjj_cta(lang)}

  <footer>
    <p>Yoga Wiki — {NOW}</p>
  </footer>
</div>
</body>
</html>"""

def update_sitemap(new_slugs):
    sitemap_path = os.path.join(BASE, "sitemap.xml")
    with open(sitemap_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_entries = ""
    for slug in new_slugs:
        for lang in LANGS:
            url = f"https://t307239.github.io/yoga-wiki/{lang}/{slug}.html"
            if url not in content:
                new_entries += f"""  <url>
    <loc>{url}</loc>
    <lastmod>{NOW}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
"""

    if new_entries:
        content = content.replace("</urlset>", new_entries + "</urlset>")
        with open(sitemap_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated sitemap with {len(new_slugs) * 3} new URLs")

generated = []
skipped = []

for pose in POSES:
    slug = pose["slug"]
    for lang in LANGS:
        out_path = os.path.join(BASE, lang, f"{slug}.html")
        if os.path.exists(out_path):
            skipped.append(f"{lang}/{slug}")
            continue
        html = generate_page(pose, lang)
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
        generated.append(f"{lang}/{slug}")

print(f"Generated: {len(generated)} pages")
print(f"Skipped (existing): {len(skipped)}")

new_slugs = list(set(pose["slug"] for pose in POSES))
update_sitemap(new_slugs)

# Count EN pages
en_dir = os.path.join(BASE, "en")
en_count = len([f for f in os.listdir(en_dir) if f.endswith(".html") and f != "index.html"])
print(f"Total EN yoga pages (excl index): {en_count}")
print("Done!")
