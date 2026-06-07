import streamlit as st

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Truth or Dare 🐍🪜",
    page_icon="🎲",
    layout="centered",
)

# ── Game data ──────────────────────────────────────────────────────────────────
# Star squares = Dare | All others = Truth
# Replace every "YOUR_DARE_HERE" / "YOUR_TRUTH_HERE" with your real prompts.

squares = {
    1:  {"type": "Truth", "text": "1.If you had to swap lives with one cartoon character for a week, who would it be??"},
    2:  {"type": "Truth", "text": "2.whats the juiciest gossip you know abt me ?"},
    3:  {"type": "Dare",  "text": "3.Pretend you’re being interviewed after winning the World Championship of doing absolutely nothing"},
    4:  {"type": "Truth", "text": "4.What’s a first impression you had about me that turned out to be completely wrong? (Ik we both like talking abt this so)"},
    5:  {"type": "Truth", "text": "5.if we were sitting in total silnce rn for 5 mins , what would u be thinking abt ?"},
    6:  {"type": "Dare",  "text": "6.record ur fav paragraph of other persons eid wish but in ur language"},
    7:  {"type": "Truth", "text": "7.What’s the most ridiculous thing you’ve ever done because you were bored?"},
    8:  {"type": "Dare",  "text": "8.Invent three laws that would exist if you ruled the world"},
    9:  {"type": "Truth", "text": "9.if u had to describe my personality using only 3 items you can see where u are sitting, what would they be"},
    10: {"type": "Dare",  "text": "10.for the rest of the game , must end ur sentence with yes sir, okay boss / yes princess , understood ma’am"},
    11: {"type": "Dare",  "text": "11.give a TED Talk on why mosquitoes deserve human rights"},
    12: {"type": "Truth", "text": "12.What’s the funniest lie you’ve told that people actually believed?"},
    13: {"type": "Truth", "text": "13. What’s something you’ve never told anyone because you thought it was too embarrassing?"},
    14: {"type": "Truth", "text": "14.What’s something you’ll defend forever, no matter how many people disagree?"},
    15: {"type": "Dare",  "text": "15.find a song on ur spotify that matches ur vibe when u miss me and sing it right now"},
    16: {"type": "Truth", "text": "16. What’s a compliment you’ve always wanted to receive? (and now’s the time to ask for it)"},
    17: {"type": "Dare",  "text": "17.Close your eyes, scroll through your gallery and open any random picture, and send it"},
    18: {"type": "Truth", "text": "18.What’s a fear you don’t talk abt often?"},
    19: {"type": "Truth", "text": "19. if we had met irl (school or university) would you've approached me (knowing my personality etc and how would u approach me?)"},
    20: {"type": "Truth", "text": "20.If your thoughts were accidentally broadcast on a loudspeaker for 10 minutes, how cooked would you be?"},
    21: {"type": "Dare",  "text": "21.a 60 sec speech on why “my fav food is superior” .... no stuttering, stopping or using these words (like, umm , yk , uh etc)"},
    22: {"type": "Truth", "text": "22.What’s the weirdest thing you’ve ever Googled?"},
    23: {"type": "Dare",  "text": "23.Take a selfie looking as angry as possible and send it"},
    24: {"type": "Truth", "text": "24. what's a secret you're keeping from everyone else? (can be abt me or just in general)"},
    25: {"type": "Truth", "text": "25.What’s a moment in your life you’d relive just to experience it again?"},
    26: {"type": "Dare", "text": "26.go and interview a random person around you and ask PEHLY ANADA AYA THA YA MURGHI ..... or ..... move back 3 blocks in game"},
    27: {"type": "Truth", "text": "27. what are the last 3 things u googled?"},
    28: {"type": "Truth", "text": "28.If I was a game character, what would be my superpowers?"},
    29: {"type": "Dare",  "text": "29.Laugh for 20 seconds without stopping"},
    30: {"type": "Truth", "text": "30. What’s something you’ve done that you still can’t believe you got away with?"},
    31: {"type": "Dare",  "text": "31.Pick up a random object near you. u have 45 seconds to act like TV salesman and pitch it to me as a must-buy luxury item"},
    32: {"type": "Dare",  "text": "32.talk in your fav accent, or any accent for the next 3 times you’ll speak"},
    33: {"type": "Truth", "text": "33. what are the things u wish people understood better abt u "},
}

# ── CSS injection ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* ── Google Fonts ── */
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Nunito:wght@400;600;700&display=swap');

/* ── Root palette ── */
:root {
    --bg:           #fdf0f5;
    --card-bg:      #fff7fa;
    --plum:         #4A3B52;
    --plum-light:   #7a6282;
    --dare-coral:   #e8637a;
    --dare-light:   #fde8ed;
    --dare-border:  #e8637a;
    --truth-sage:   #9bb8a8;
    --truth-light:  #eef6f1;
    --truth-border: #7dab92;
    --shadow:       rgba(74,59,82,0.10);
    --shadow-card:  rgba(74,59,82,0.16);
}

/* ── App shell ── */
html, body, [data-testid="stAppViewContainer"] {
    background-color: var(--bg) !important;
    font-family: 'Nunito', sans-serif;
}
[data-testid="stHeader"] { background: transparent !important; }

/* Hide Streamlit branding */
#MainMenu, footer { visibility: hidden; }

/* ── Centred wrapper ── */
.main .block-container {
    max-width: 520px;
    padding-top: 2.5rem;
    padding-bottom: 3rem;
}

/* ── Title ── */
.app-title {
    text-align: center;
    font-family: 'Playfair Display', serif;
    font-size: 2.1rem;
    color: var(--plum);
    margin-bottom: 0.15rem;
    letter-spacing: -0.5px;
}
.app-sub {
    text-align: center;
    font-size: 0.95rem;
    color: var(--plum-light);
    margin-bottom: 2rem;
    letter-spacing: 0.4px;
}

/* ── Label above input ── */
.input-label {
    font-size: 0.85rem;
    font-weight: 700;
    color: var(--plum);
    letter-spacing: 0.8px;
    text-transform: uppercase;
    margin-bottom: 0.4rem;
}

/* ── Streamlit number input ── */
[data-testid="stNumberInput"] input {
    background: white !important;
    border: 2px solid #e8d4e8 !important;
    border-radius: 14px !important;
    color: var(--plum) !important;
    font-family: 'Nunito', sans-serif !important;
    font-size: 1.15rem !important;
    font-weight: 700 !important;
    text-align: center !important;
    padding: 0.5rem 1rem !important;
    box-shadow: 0 2px 8px var(--shadow) !important;
    transition: border-color 0.2s;
}
[data-testid="stNumberInput"] input:focus {
    border-color: var(--dare-coral) !important;
    outline: none !important;
}

/* ── Reveal button ── */
[data-testid="stButton"] > button {
    width: 100%;
    background: linear-gradient(135deg, #e8637a 0%, #c94b6b 100%);
    color: white;
    border: none;
    border-radius: 50px;
    padding: 0.75rem 2rem;
    font-family: 'Nunito', sans-serif;
    font-size: 1rem;
    font-weight: 700;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    cursor: pointer;
    box-shadow: 0 4px 18px rgba(232,99,122,0.35);
    transition: transform 0.15s, box-shadow 0.15s;
    margin-top: 0.4rem;
}
[data-testid="stButton"] > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 22px rgba(232,99,122,0.45);
}
[data-testid="stButton"] > button:active {
    transform: translateY(0);
}

/* ── Flashcard ── */
.flashcard {
    margin-top: 2rem;
    border-radius: 24px;
    padding: 2rem 2rem 1.8rem;
    animation: cardPop 0.35s cubic-bezier(0.34,1.56,0.64,1) both;
    box-shadow: 0 8px 32px var(--shadow-card);
    position: relative;
    overflow: hidden;
}
@keyframes cardPop {
    from { opacity: 0; transform: scale(0.88) translateY(12px); }
    to   { opacity: 1; transform: scale(1)    translateY(0);     }
}

/* Dare card */
.flashcard.dare {
    background: var(--dare-light);
    border-left: 6px solid var(--dare-border);
}
/* Truth card */
.flashcard.truth {
    background: var(--truth-light);
    border-left: 6px solid var(--truth-border);
}

/* Decorative blob */
.flashcard::before {
    content: '';
    position: absolute;
    top: -40px; right: -40px;
    width: 120px; height: 120px;
    border-radius: 50%;
    opacity: 0.12;
}
.flashcard.dare::before  { background: var(--dare-coral); }
.flashcard.truth::before { background: var(--truth-sage); }

/* Pill badge */
.card-badge {
    display: inline-block;
    font-size: 0.72rem;
    font-weight: 800;
    letter-spacing: 1.4px;
    text-transform: uppercase;
    border-radius: 50px;
    padding: 0.28rem 0.85rem;
    margin-bottom: 0.9rem;
}
.dare  .card-badge { background: var(--dare-coral); color: white; }
.truth .card-badge { background: var(--truth-sage); color: white; }

/* Card headline */
.card-headline {
    font-family: 'Playfair Display', serif;
    font-size: 1.65rem;
    font-weight: 700;
    line-height: 1.2;
    margin-bottom: 1rem;
}
.dare  .card-headline { color: var(--dare-coral); }
.truth .card-headline { color: #4a7a62; }

/* Square number */
.card-square {
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 0.8px;
    text-transform: uppercase;
    color: var(--plum-light);
    margin-bottom: 0.4rem;
}

/* Divider */
.card-divider {
    height: 1px;
    margin: 0.9rem 0 1.1rem;
    opacity: 0.3;
}
.dare  .card-divider { background: var(--dare-coral); }
.truth .card-divider { background: var(--truth-sage); }

/* Challenge text */
.card-text {
    font-size: 1.08rem;
    line-height: 1.65;
    color: var(--plum);
    font-weight: 600;
}

/* ── Decoration icons ── */
.dare-icon  { font-size: 1.6rem; margin-bottom: 0.2rem; display: block; }
.truth-icon { font-size: 1.6rem; margin-bottom: 0.2rem; display: block; }

/* ── Special squares ── */
.special-card {
    margin-top: 2rem;
    background: linear-gradient(135deg, #fde8ed 0%, #f5e6ff 100%);
    border: 2px dashed #c9a8d4;
    border-radius: 24px;
    padding: 2rem;
    text-align: center;
    animation: cardPop 0.35s cubic-bezier(0.34,1.56,0.64,1) both;
    box-shadow: 0 8px 32px var(--shadow-card);
}
.special-card .special-emoji { font-size: 2.8rem; }
.special-card .special-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.5rem;
    color: var(--plum);
    margin: 0.5rem 0 0.3rem;
}
.special-card .special-sub {
    color: var(--plum-light);
    font-size: 0.95rem;
    font-weight: 600;
}

/* ── Error message ── */
.error-msg {
    margin-top: 1.5rem;
    background: #fff0f3;
    border: 2px solid #f5b8c4;
    border-radius: 14px;
    padding: 1rem 1.2rem;
    color: var(--dare-coral);
    font-weight: 700;
    text-align: center;
    font-size: 0.95rem;
}

/* ── Footer ── */
.app-footer {
    margin-top: 3rem;
    text-align: center;
    font-size: 0.78rem;
    color: var(--plum-light);
    letter-spacing: 0.3px;
}
            
            /* Hide the top right Streamlit header elements (Fork, GitHub icon, etc.) */
header[data-testid="stHeader"] {
    display: none !important;
}

/* Hide the deployment status/footer decoration wrapper at the bottom right */
div[data-testid="stConnectionStatus"], 
.stDeployButton, 
[data-testid="stStatusWidget"] {
    display: none !important;
    visibility: hidden !important;
}

/* Ensure no sneaky floating action elements appear on mobile viewports */
footer {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)

# ── Header ─────────────────────────────────────────────────────────────────────
st.markdown('<div class="app-title">🐍 Truth or Dare 🪜</div>', unsafe_allow_html=True)
st.markdown('<div class="app-sub">Snakes & Ladders Edition — Long Distance Edition ✈️</div>', unsafe_allow_html=True)

# ── Input ──────────────────────────────────────────────────────────────────────
st.markdown('<div class="input-label">Which square did you land on?</div>', unsafe_allow_html=True)

square_input = st.number_input(
    label="square",
    label_visibility="collapsed",
    min_value=1,
    max_value=33,
    step=1,
    value=None,
    placeholder="Enter 1 – 33",
)

reveal = st.button("✨ Reveal")

# ── Flashcard logic ────────────────────────────────────────────────────────────
if reveal:
    if square_input is None:
        st.markdown('<div class="error-msg">Please enter a square number first (1–33).</div>',
                    unsafe_allow_html=True)
    else:
        num = int(square_input)
        data = squares[num]
        card_type = data["type"]
        text = data["text"]

        if card_type == "Dare":
            st.markdown(f"""
            <div class="flashcard dare">
                <span class="dare-icon">⭐</span>
                <div class="card-square">Square {num}</div>
                <div class="card-badge">Star Square</div>
                <div class="card-headline">Do a Dare!</div>
                <div class="card-divider"></div>
                <div class="card-text">{text}</div>
            </div>
            """, unsafe_allow_html=True)

        else:  # Truth
            st.markdown(f"""
            <div class="flashcard truth">
                <span class="truth-icon">💬</span>
                <div class="card-square">Square {num}</div>
                <div class="card-badge">Truth Square</div>
                <div class="card-headline">Tell a Truth!</div>
                <div class="card-divider"></div>
                <div class="card-text">{text}</div>
            </div>
            """, unsafe_allow_html=True)

# ── Footer ─────────────────────────────────────────────────────────────────────
st.markdown(
    '<div class="app-footer">A game by S-💕</div>',
    unsafe_allow_html=True,
)
