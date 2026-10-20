"""Prefix root-absolute site paths so the site works under a project Pages URL.

The pages use root paths (/about/, /squarespace/..., /pretalx/...), which only
resolve when the site is served at the root of a domain. Until the custom
domain is attached, the deploy workflow runs this with the repo name, e.g.
`python3 .github/prefix-paths.py /GOOD2026-static`, on the files it uploads.
"""
import os, re, sys

prefix = sys.argv[1].rstrip("/")
tops = sorted(n for n in os.listdir(".") if not n.startswith("."))
names = "|".join(re.escape(n) for n in tops)
# A "/" that starts a path: after a quote, "(", "=" or ",", and followed by a
# top-level site entry, a fragment, or the end of the string ("/" itself).
plain = re.compile(r'(?<=["\'(=,])/(?=(?:%s)(?=[/"\'#?)]|$)|["\'#])' % names)
# Scripts and data are full of "/" strings, so only touch the asset folders there.
# Also after ";" (&quot;) and whitespace (srcset lists).
assets = re.compile(r'(?<=["\'(=,;\s])/(?=(?:squarespace|pretalx)/)')
escaped = re.compile(r'(?<=["\'])\\/(?=(?:%s)\\/)' % names)

for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if not d.startswith(".")]
    for f in files:
        if not f.split("?")[0].split("%3F")[0].endswith((".html", ".js", ".css", ".json")):
            continue
        p = os.path.join(root, f)
        with open(p, encoding="utf-8", errors="surrogateescape") as fh:
            t = fh.read()
        n = assets.sub(prefix + "/", t)
        if f.endswith(".html"):
            n = plain.sub(prefix + "/", n)
        n = escaped.sub(prefix.replace("/", "\\/") + "\\/", n)
        if n != t:
            with open(p, "w", encoding="utf-8", errors="surrogateescape") as fh:
                fh.write(n)
