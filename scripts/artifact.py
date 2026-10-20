#!/usr/bin/env python3
"""Packs the five pages into ONE self-contained page for a claude.ai Artifact (images inlined, pages switched by #hash)."""
import re, base64, pathlib
R = pathlib.Path(__file__).resolve().parent.parent
rd = lambda n: (R / n).read_text(encoding="utf-8")
css = rd("style.css")
# the artifact viewer sets data-theme explicitly, so mirror the dark tokens under it
m = re.search(r'@media \(prefers-color-scheme: dark\) \{\s*:root:not\(\[data-theme="light"\]\) \{(.*?)\n  \}\n\}', css, re.S)
css += '\n:root[data-theme="dark"] {' + m.group(1) + '\n  color-scheme: dark;\n}\n.rise { animation: none !important; }\n[data-page][hidden]{display:none!important}\n'
css = css.replace("top: 0; z-index: 5;", "top: env(safe-area-inset-top, 0px); z-index: 5;")

def data(path):
    b = (R / path).read_bytes()
    return "data:image/webp;base64," + base64.b64encode(b).decode()

pages = {"home": "index.html", "emily": "emily.html", "consulting": "consulting.html", "apps": "apps.html", "contact": "contact.html"}
links = {"index.html": "#home", "emily.html": "#emily", "consulting.html#engagements": "#consulting", "consulting.html": "#consulting", "apps.html#all": "#apps", "apps.html": "#apps", "contact.html": "#contact"}

def fix(h):
    for k, v in sorted(links.items(), key=lambda kv: -len(kv[0])):
        h = h.replace(f'href="{k}"', f'href="{v}"')
    return re.sub(r'src="(img/[^"]+\.webp)"', lambda mm: f'src="{data(mm.group(1))}"', h)

idx = rd("index.html")
header = fix(re.search(r"<header.*?</header>", idx, re.S).group(0))
footer = fix(re.search(r"<footer.*?</footer>", idx, re.S).group(0))
body = ""
for key, f in pages.items():
    main = re.search(r'<main id="main">(.*?)</main>', rd(f), re.S).group(1)
    body += f'<div data-page="{key}"{"" if key == "home" else " hidden"}>{fix(main)}</div>\n'
site_js = rd("site.js")
fonts = re.search(r'<link rel="preconnect".*?display=swap">', idx, re.S).group(0)
router = """
(function(){
  var pages=[].slice.call(document.querySelectorAll('[data-page]'));
  function show(){
    var h=(location.hash||'#home').slice(1);
    if(!pages.some(function(p){return p.dataset.page===h})) return;
    pages.forEach(function(p){p.hidden=p.dataset.page!==h});
    document.querySelectorAll('.site-head nav a').forEach(function(a){
      if(a.getAttribute('href')==='#'+h) a.setAttribute('aria-current','page'); else a.removeAttribute('aria-current');
    });
    window.scrollTo(0,0);
  }
  window.addEventListener('hashchange',show); show();
})();
"""
out = f"""<title>Chai Wellness</title>
{fonts}
<style>
{css}
</style>
{header}
<main>
{body}</main>
{footer}
<script>
{site_js}
{router}
</script>
"""
(R / "scripts" / "artifact-site.html").write_text(out, encoding="utf-8")
print(len(out) // 1024, "KB")
