#!/usr/bin/env python3
"""Writes the Chai Wellness pages from one place so the header, footer and app list stay in step.
Run from anywhere: python3 scripts/build.py. Output lands next to style.css (the Website folder)."""
import html, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "https://chaiwellness.example"   # replaced when the domain is chosen (og:url only)

MARK = '''<svg class="mark" viewBox="0 0 64 64" aria-hidden="true"><circle cx="32" cy="32" r="30" fill="#d98e2b"/><text x="32" y="45" text-anchor="middle" font-family="Frank Ruhl Libre, serif" font-weight="700" font-size="34" fill="#2b1a0a" direction="rtl">חי</text></svg>'''

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght,SOFT@0,9..144,300..700,0..100;1,9..144,300..700,0..100&amp;family=Frank+Ruhl+Libre:wght@700&amp;family=Hanken+Grotesk:wght@400;500;600&amp;display=swap">'

NAV_L = [("index.html", "Home"), ("emily.html", "About Emily"), ("consulting.html", "Consulting")]
NAV_R = [("apps.html", "Apps"), ("contact.html", "Contact")]


def nav(items, page):
    cur = ' aria-current="page"'
    return "".join(f'<a href="{h}"{cur if h == page else ""}>{t}</a>' for h, t in items)


def head(title, desc, page, og="og-image.jpg"):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:type" content="website">
<meta property="og:image" content="{og}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#f7f0e4">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
{FONTS}
<link rel="stylesheet" href="style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-head"><div class="wrap bar">
<nav class="left" aria-label="Main">{nav(NAV_L, page)}</nav>
<a class="brand" href="index.html" aria-label="Chai Wellness, home">{MARK}<span><b>Chai Wellness</b><small>Life, steeped well</small></span></a>
<nav class="right" aria-label="More">{nav(NAV_R, page)}</nav>
</div></header>
<main id="main">
'''


FOOT = '''</main>
<footer><div class="wrap">
<div class="foot">
<div><b>Chai Wellness</b><p>Psychology consulting and training, and apps for everyday life. Athens, Georgia.</p></div>
<div><b>Explore</b><ul><li><a href="emily.html">About Emily</a></li><li><a href="consulting.html">Consulting</a></li><li><a href="apps.html">Apps</a></li><li><a href="contact.html">Contact</a></li></ul></div>
<div><b>Right now</b><ul><li><a href="apps.html#all">Eric's apps</a></li><li><a href="consulting.html#engagements">Past workshops</a></li><li><a href="contact.html">Start a conversation</a></li></ul></div>
</div>
<p class="fine">&copy; 2026 Chai Wellness. Dr. Mouilso's consulting is independent of her role at the University of Georgia. Chai Wellness does not provide therapy or crisis services. If you are in crisis, call or text 988.</p>
</div></footer>
<script src="site.js" defer></script>
</body>
</html>
'''

# ---------------------------------------------------------------- apps
APPS = [
    # slug, name, platforms, pitch, status(live|beta|soon), url, store
    ("Everyday life", [
        ("habit-traffic", "Habit Traffic", "iPhone · iPad · Apple Watch", "Gives every routine a green, yellow or red light, so you always know what needs your attention today.", "beta", "https://habittraffic.com", ""),
        ("miles-ahead", "Miles Ahead of Lease", "iPhone · iPad", "Log your odometer now and then and see whether you are ahead of your lease allowance, and what an overage would cost.", "live", "https://milesaheadoflease.com", "https://apps.apple.com/us/app/miles-ahead-of-lease/id6751857922"),
        ("barrelbook", "BarrelBook", "iPhone · iPad", "The whiskey collection app for serious collectors. Track every bottle, log tastings and manage your wishlist.", "live", "https://www.barrelbookapp.com", "https://apps.apple.com/us/app/barrelbook/id6751058765"),
    ]),
    ("Your stuff, in order", [
        ("crate", "Crate Music Library", "iPhone · iPad", "Your Apple Music library as a room full of records. Ask for playlists in plain words, make mixtapes, see every play.", "soon", "https://cratemusicapp.com", ""),
        ("quest-chronicle", "Quest Chronicle", "Mac · iPhone · iPad", "A game library and play tracker. Connect Steam or Xbox and it logs your sessions while you play.", "beta", "https://questchronicleapp.com", ""),
        ("stash", "Stash Library", "Mac · iPhone · iPad", "Saves any tab with one key, knows which links you've opened, and archives what you are done with.", "beta", "https://stashlibraryapp.com", ""),
        ("thumb-through", "Thumb Through", "iPhone · iPad", "Swipe through any folder of photos, one at a time. Keep the good ones, clear out the rest.", "beta", "https://thumbthroughapp.com", ""),
        ("snipe", "Snipe", "Mac · iPhone · iPad", "Keeps the apps you mean to buy in one list and tells you when one drops, goes free, or hits your price.", "beta", "https://snipeappsales.com", ""),
    ]),
    ("Torah and music", [
        ("torah-turn-it", "Torah: Turn It", "iPhone · iPad", "This week's Torah portion for anyone curious: the story in plain English, a question to talk over, a few minutes a day.", "beta", "https://torahturnit.com", ""),
        ("torah-tones", "Torah Tones", "iPad · AUv3 plug-in", "Play the melodic phrases of Torah chanting as MIDI, in any key and mode, locked to your host's tempo.", "beta", "https://torahtones.com", ""),
        ("shofar-tones", "Shofar Tones", "iPad · AUv3 plug-in", "A real ram's horn recording, five real rooms and a step sequencer, played in time with your music.", "beta", "https://eroxx.github.io/shofartones-website/", ""),
    ]),
]
TAGS = {"live": ("live", "On the App Store"), "beta": ("beta", "Public beta"), "soon": ("soon", "Coming soon")}


def app_card(a):
    slug, name, plat, pitch, st, url, store = a
    cls, label = TAGS[st]
    href = store or url
    return f'''<a class="app" href="{href}" rel="noopener"><img src="img/apps/{slug}.webp" width="76" height="76" alt="" loading="lazy"><div><h4>{html.escape(name)}</h4><div class="plat">{plat}</div><p>{html.escape(pitch)}</p><span class="tag {cls}">{label}</span></div></a>'''


def apps_groups():
    return "".join(f'<div class="app-group"><h3>{g}</h3><div class="apps">{"".join(app_card(a) for a in items)}</div></div>' for g, items in APPS)


def fan(slugs):
    return "".join(f'<img src="img/apps/{s}.webp" alt="" width="64" height="64">' for s in slugs)


# ---------------------------------------------------------------- pages
def index():
    return head("Chai Wellness: psychology consulting and apps for everyday life",
                "Chai Wellness is a small company in Athens, Georgia: psychology training and consulting from Dr. Emily Mouilso, and apps for everyday life from Eric Linder.", "index.html") + f'''
<section class="hero"><div class="wrap hero-grid">
<div>
<p class="eyebrow rise">Athens, Georgia</p>
<h1 class="rise d1">Two ways to help <em>life</em> go well.</h1>
<p class="lede rise d2">Chai Wellness is a small company with two halves. Dr. Emily Mouilso offers psychology training and consultation to clinicians and organizations. Eric Linder makes apps that take a little weight off everyday life.</p>
<div class="btn-row rise d3"><a class="btn" href="consulting.html">Psychology consulting</a><a class="btn ghost" href="apps.html">See the apps</a></div>
</div>
<div class="cup rise d2" role="img" aria-label="A cup of chai on a saucer with steam rising, with a saffron band">
<svg viewBox="0 0 400 400" aria-hidden="true">
<path class="arch-bg" d="M50 380 V190 C50 100 115 40 200 40 S350 100 350 190 V380 Z"/>
<g class="steam"><path d="M160 138 C140 112 180 98 160 70 S172 44 168 30"/><path d="M200 138 C180 108 222 92 200 62 S212 34 208 20"/><path d="M240 138 C220 112 260 98 240 70 S252 44 248 30"/></g>
<ellipse cx="200" cy="332" rx="138" ry="10" fill="#2b1e16" opacity=".12"/>
<ellipse class="saucer-under" cx="200" cy="330" rx="140" ry="16"/>
<ellipse class="saucer" cx="200" cy="322" rx="145" ry="18"/>
<ellipse class="saucer-in" cx="200" cy="320" rx="100" ry="9"/>
<defs><clipPath id="cupclip"><path d="M100 168 H300 V204 C300 268 262 312 200 312 C138 312 100 268 100 204 Z"/></clipPath></defs>
<path class="handle" d="M296 196 C352 190 352 268 292 262"/>
<ellipse cx="200" cy="316" rx="46" ry="7" fill="#2f4636"/>
<path class="cup-body" d="M100 168 H300 V204 C300 268 262 312 200 312 C138 312 100 268 100 204 Z"/>
<g clip-path="url(#cupclip)" fill="#d98e2b" stroke="#d98e2b"><path d="M96 200 H304 M96 224 H304" stroke-width="3" fill="none"/><g stroke="none"><circle cx="124" cy="212" r="4"/><circle cx="152" cy="212" r="4"/><circle cx="180" cy="212" r="4"/><circle cx="208" cy="212" r="4"/><circle cx="236" cy="212" r="4"/><circle cx="264" cy="212" r="4"/><circle cx="292" cy="212" r="4"/></g></g>
<ellipse class="cup-rim" cx="200" cy="168" rx="100" ry="15"/>
<ellipse class="tea" cx="200" cy="169" rx="88" ry="9"/>
</svg>
<span class="eighteen">Chai means life, and 18</span>
</div>
</div></section>

<section class="band"><div class="wrap">
<p class="eyebrow">What's in a name</p>
<div class="meanings">
<div class="meaning"><span class="big he" lang="he">חי</span><h3>Life</h3><p>Chai is the Hebrew word for life. It is what a wellness company is ultimately about.</p></div>
<div class="meaning"><span class="big">18</span><h3>A number with a blessing</h3><p>The two letters of chai add up to 18, which is why gifts and donations are so often given in multiples of it. <i>L'chaim</i> means "to life."</p></div>
<div class="meaning"><span class="big">☕</span><h3>A cup of tea</h3><p>Spiced, slow and shared. We would like our work to feel like that: warm, unhurried and worth sitting down for.</p></div>
</div>
</div></section>

<section><div class="wrap">
<p class="eyebrow">The two halves</p>
<h2>Pick a door.</h2>
<div class="doors">
<a class="door" href="emily.html">
<div class="arch"><img src="img/emily-560.webp" alt="Dr. Emily Mouilso" width="150" height="188"></div>
<h3>Dr. Emily Mouilso</h3>
<p>A board-certified clinical psychologist who trains therapists, supervises clinics and advises on ethics. Her consulting covers evidence-based treatment, clinical ethics, supervision, and technology and AI in practice.</p>
<span class="go">About Emily and her consulting <span aria-hidden="true">→</span></span>
</a>
<a class="door" href="apps.html">
<div class="icon-fan" aria-hidden="true">{fan(["habit-traffic", "crate", "barrelbook", "stash", "torah-turn-it", "snipe", "quest-chronicle", "thumb-through"])}</div>
<h3>Eric Linder's apps</h3>
<p>Eleven apps for iPhone, iPad, Mac and Apple Watch, from habit tracking to whiskey collections to Torah study. Small, careful and built one at a time.</p>
<span class="go">See all the apps <span aria-hidden="true">→</span></span>
</a>
</div>
</div></section>

<section class="dark-band"><div class="wrap" style="text-align:center;max-width:760px">
<h2>Have a question, a training need or an idea?</h2>
<p class="lede" style="margin-inline:auto">Tell us what you are working on. We read every message ourselves.</p>
<div class="btn-row" style="justify-content:center"><a class="btn" href="contact.html">Get in touch</a></div>
</div></section>
''' + FOOT


def emily():
    return head("About Dr. Emily Mouilso | Chai Wellness",
                "Dr. Emily Mouilso is a board-certified clinical psychologist who trains therapists, supervises clinics and consults on trauma treatment, ethics, and technology in practice.", "emily.html") + '''
<section class="page-title"><div class="wrap">
<p class="eyebrow">About</p>
<h1>Emily R. Mouilso, <em>PhD, ABPP</em></h1>
<p class="lede">Board-certified clinical psychologist. She helps therapists and clinics do the hard parts of the work well: treating trauma, supervising carefully and making sound ethical decisions.</p>
</div></section>

<section style="padding-top:0"><div class="wrap profile">
<aside class="portrait">
<div class="frame"><img src="img/emily-1000.webp" alt="Portrait of Dr. Emily Mouilso, smiling, seated in front of a bookshelf" width="1000" height="1250" fetchpriority="high"></div>
<p class="caption">Dr. Emily Mouilso</p>
</aside>
<div>
<div class="prose">
<p>Dr. Emily Mouilso is a licensed psychologist in Georgia and is board certified in Behavioral and Cognitive Psychology by the American Board of Professional Psychology. She is a Clinical Associate Professor at the University of Georgia, where she directs the Psychology Clinic and serves as Associate Director of Clinical Training for the doctoral program in clinical psychology.</p>
<p>Her clinical roots are in trauma. She trained at the Ralph H. Johnson VA Medical Center and the National Crime Victims Research and Treatment Center in Charleston, then completed a fellowship at the Charlie Norwood VA Medical Center, where she treated veterans and set up a new co-located psychology clinic on a unit that had never had embedded behavioral health care.</p>
<p>Since 2015 she has run a training clinic, which means she spends her days on the questions clinicians actually face: which treatment fits, how to supervise it, and what the right thing to do is when the answer is not obvious. When her clinic moved to telehealth in 2020 she chose the secure technology and wrote the consent and crisis procedures. She later led her program's policies on telesupervision and on artificial intelligence, and other clinics at her university have adopted the AI policy.</p>
<p>She has served on the Georgia Psychological Association's Ethics Committee since 2021, advising colleagues on difficult dilemmas, and is an exam chair for her specialty board at ABPP and a site visitor for the American Psychological Association's accreditation body.</p>
</div>

<h2 style="margin-top:56px;font-size:1.7rem">Focus areas</h2>
<ul class="chips">
<li>Trauma and PTSD</li><li>Exposure therapy</li><li>Cognitive behavioral therapy</li><li>Suicide prevention</li><li>Clinical ethics</li><li>Supervision and training</li><li>Integrated primary care</li><li>Technology and AI in practice</li>
</ul>

<h2 style="margin-top:56px;font-size:1.7rem">Credentials</h2>
<dl class="facts">
<div><dt>Board certified</dt><dd>Behavioral and Cognitive Psychology, American Board of Professional Psychology (2019)</dd></div>
<div><dt>Licensed</dt><dd>Psychologist, State of Georgia (2015)</dd></div>
<div><dt>Education</dt><dd>PhD (2014) and MS (2011) in Clinical Psychology, University of Georgia. BA in Psychology, University of Wisconsin-Madison (2007)</dd></div>
<div><dt>Training</dt><dd>Predoctoral internship, Charleston Consortium, including the Ralph H. Johnson VA and the National Crime Victims Research and Treatment Center. Postdoctoral fellowship, Charlie Norwood VA Medical Center</dd></div>
<div><dt>Appointment</dt><dd>Clinical Associate Professor, University of Georgia. Clinic Director and Associate Director of Clinical Training</dd></div>
</dl>
</div>
</div></section>

<section class="band"><div class="wrap cols2">
<div>
<p class="eyebrow">Service</p>
<h2 style="font-size:1.9rem">Leadership in the profession</h2>
<ul class="plain-list">
<li>Georgia Psychological Association, Ethics Committee<span>Member since 2021</span></li>
<li>American Board of Professional Psychology<span>Behavioral and Cognitive Psychology specialty board: examiner, exam chair and board of directors</span></li>
<li>American Psychological Association<span>Site visitor, Commission on Accreditation</span></li>
<li>Association of Directors of Training Clinics<span>Member</span></li>
</ul>
</div>
<div>
<p class="eyebrow">Recognition</p>
<h2 style="font-size:1.9rem">Honors</h2>
<ul class="plain-list">
<li>Georgia Psychological Association Outstanding Service Award<span>2025</span></li>
<li>Georgia Psychological Association Fellow<span>2022</span></li>
<li>University of Georgia Psychology Program Teaching Award<span>2022, 2024 and 2026</span></li>
<li>Best Clinical Supervisor, UGA Psychology Program<span>2017, 2018 and 2019</span></li>
<li>Phi Beta Kappa<span>Initiated 2006, chapter president 2020 to 2025</span></li>
</ul>
</div>
</div></section>

<section class="dark-band"><div class="wrap" style="text-align:center;max-width:760px">
<h2>Work with Emily</h2>
<p class="lede" style="margin-inline:auto">Workshops, trainings and consultation for clinicians, clinics and organizations.</p>
<div class="btn-row" style="justify-content:center"><a class="btn" href="consulting.html">See consulting offerings</a></div>
</div></section>
''' + FOOT


ENGAGEMENTS = [
    ("2026", "Ethical considerations in the use of AI for mental health providers", "Continuing education workshop, The Knowledge Tree"),
    ("2026", "The Unified Protocol for the transdiagnostic treatment of emotional disorders", "Continuing education workshop, Advantage Behavioral Health Systems"),
    ("2026", "An overview of exposure therapy for trauma-related disorders", "Continuing education workshop, Athens Area Psychological Association"),
    ("2026", "Exposure therapy, and supervision of exposure therapy", "Training series, Advantage Behavioral Health Systems"),
    ("2026", "Ethics in motion: connection and change in global psychological practice", "Workshop, Georgia Psychological Association annual meeting"),
    ("2025", "Ethical decision making on technology and social media", "Workshop, Georgia Psychological Association Ethics Committee"),
    ("2025", "Implementing manualized, empirically supported treatments", "Training, Advantage Behavioral Health Systems"),
    ("2024 to 25", "CBT foundations, CBT for supervisors, CBT for suicide prevention, and the Collaborative Assessment and Management of Suicidality", "Training series, Advantage Behavioral Health Systems"),
    ("2024", "Practice and ethical considerations for psychologists in a post-Roe world", "Virtual workshop, Emory and Grady Healthcare System"),
    ("2024", "Ethical hot topics in psychology training and education", "Workshop, Georgia Psychological Association annual meeting"),
    ("2023", "Hot topics in ethics", "Workshop, Athens Area Psychological Association"),
    ("2023", "Becoming board certified in behavioral and cognitive psychology", "Talk, Association for Behavioral and Cognitive Therapies annual meeting"),
]


def consulting():
    eng = "".join(f'<li><time>{y}</time><div><b>{html.escape(t)}</b><span>{html.escape(w)}</span></div></li>' for y, t, w in ENGAGEMENTS)
    return head("Psychology consulting and training | Chai Wellness",
                "Workshops, training and consultation from Dr. Emily Mouilso: evidence-based treatment, clinical ethics, supervision and training, and technology and AI in practice.", "consulting.html") + f'''
<section class="page-title"><div class="wrap">
<p class="eyebrow">Consulting</p>
<h1>Training, consultation <em>and ethics</em></h1>
<p class="lede">Practical, evidence-based help for the people who do clinical work and the organizations that support them. In person or virtual, for a single session or an ongoing series.</p>
</div></section>

<section style="padding-top:20px"><div class="wrap">
<p class="eyebrow">Current offerings</p>
<h2>For clinicians, clinics and organizations</h2>
<div class="offer-grid">
<article class="offer"><span class="n">01</span><h3>Evidence-based treatment training</h3>
<p>Skills training that clinicians can use the next morning, delivered with the supervision and implementation support that make it stick.</p>
<ul><li>Cognitive behavioral therapy foundations</li><li>Exposure therapy and trauma-focused treatment</li><li>The Unified Protocol for emotional disorders</li><li>Implementing manualized, empirically supported treatments</li></ul></article>
<article class="offer"><span class="n">02</span><h3>Suicide prevention and risk work</h3>
<p>Training in structured, collaborative approaches to assessing and treating suicidal thoughts, for clinicians and the people who supervise them.</p>
<ul><li>Collaborative Assessment and Management of Suicidality</li><li>Cognitive behavioral therapy for suicide prevention</li></ul></article>
<article class="offer"><span class="n">03</span><h3>Clinical ethics</h3>
<p>Ethics consultation and continuing education grounded in the APA Ethics Code and the realities of current practice. Case-based, candid and useful.</p>
<ul><li>Ethical decision making through case analysis</li><li>Technology, social media and telepsychology</li><li>Artificial intelligence in mental health care</li><li>Mandated reporting and practice after Roe</li></ul></article>
<article class="offer"><span class="n">04</span><h3>Supervision, training and program development</h3>
<p>For training clinics, practices and agencies that want to supervise well, build policy and grow their people.</p>
<ul><li>Supervision of CBT and exposure therapy</li><li>Telesupervision and AI policies</li><li>Setting up and running a training clinic</li><li>Integrated primary care and interdisciplinary partnerships</li><li>Preparing for board certification</li></ul></article>
</div>
<p class="note" style="margin-top:40px">Don't see your topic? Many engagements start as a conversation. Tell us what your team is facing and we will say honestly whether Emily is the right person for it.</p>
<div class="btn-row"><a class="btn" href="contact.html">Start a conversation</a></div>
</div></section>

<section class="band" id="engagements"><div class="wrap">
<p class="eyebrow">Previous engagements</p>
<h2>Where this work has been presented</h2>
<ul class="engagements">{eng}</ul>
</div></section>

<section><div class="wrap">
<p class="eyebrow">Good to know</p>
<h2 style="font-size:1.9rem">What this is, and isn't</h2>
<p class="note">Consulting through Chai Wellness is education, training and professional consultation for clinicians and organizations. It is not therapy, and it does not provide crisis services. If you or someone you know is in crisis, call or text 988 (the Suicide and Crisis Lifeline) or your local emergency number.</p>
</div></section>

<section class="dark-band"><div class="wrap" style="text-align:center;max-width:760px">
<h2>Bring Emily to your team</h2>
<p class="lede" style="margin-inline:auto">Send a note about what you are hoping to do. A reply comes from a person, usually within a few days.</p>
<div class="btn-row" style="justify-content:center"><a class="btn" href="contact.html">Contact</a></div>
</div></section>
''' + FOOT


def apps():
    return head("Apps by Eric Linder | Chai Wellness",
                "Eleven small, careful apps for iPhone, iPad, Mac and Apple Watch: habits, collections, music, photos, prices, and Torah.", "apps.html") + f'''
<section class="page-title"><div class="wrap">
<p class="eyebrow">Apps</p>
<h1>Small apps, <em>made carefully.</em></h1>
<p class="lede">Eric Linder builds apps for the things that pile up in everyday life: habits, bottles, songs, photos, bookmarks and weekly Torah. Each one has its own website, and every one is built to do its job quietly.</p>
</div></section>

<section id="all" style="padding-top:20px"><div class="wrap">
{apps_groups()}
</div></section>

<section class="band"><div class="wrap maker">
<div class="he" lang="he" dir="rtl" aria-hidden="true">חי</div>
<div>
<p class="eyebrow">The maker</p>
<h2 style="font-size:1.9rem">Built in Athens, Georgia</h2>
<p class="lede" style="margin-bottom:0">Eric Linder is a rabbi and a lifelong tinkerer. He makes the apps he wants for his own days, then shares them. Questions, bug reports and ideas are welcome, and each app has its own support page and Discord community.</p>
<div class="btn-row"><a class="btn" href="contact.html">Write to Eric</a></div>
</div>
</div></section>
''' + FOOT


def contact():
    return head("Contact | Chai Wellness",
                "Contact Chai Wellness about psychology training and consultation with Dr. Emily Mouilso, or about Eric Linder's apps.", "contact.html") + '''
<section class="page-title"><div class="wrap">
<p class="eyebrow">Contact</p>
<h1>Let's <em>talk.</em></h1>
<p class="lede">Tell us a little about what you have in mind. Your note opens in your email app, addressed to us, so you can read it over before you send it.</p>
</div></section>

<section style="padding-top:0"><div class="wrap">
<form class="form" id="contact" novalidate>
<div class="two">
<label>Your name<input name="name" autocomplete="name" required></label>
<label>Your email<input name="email" type="email" autocomplete="email" required></label>
</div>
<label>Organization <span class="hint">(optional)</span><input name="org" autocomplete="organization"></label>
<label>What is this about?
<select name="topic">
<option>Training or workshop for my team</option>
<option>Ethics consultation</option>
<option>Supervision or program development</option>
<option>Something else for Emily</option>
<option>One of Eric's apps</option>
</select></label>
<label>Message<textarea name="message" required></textarea></label>
<div><button class="btn" type="submit">Open my email</button></div>
<p class="status" id="status" role="status" aria-live="polite"></p>
</form>
<p class="crisis">Chai Wellness does not provide therapy or crisis services, and email is not monitored around the clock. If you or someone you know is in crisis, call or text <b>988</b>, or call your local emergency number.</p>
<p id="direct" hidden>Prefer to write directly? <a id="direct-link" href="#"></a></p>
</div></section>
''' + FOOT


for name, fn in [("index.html", index), ("emily.html", emily), ("consulting.html", consulting), ("apps.html", apps), ("contact.html", contact)]:
    (ROOT / name).write_text(fn(), encoding="utf-8")
    print("wrote", name)
