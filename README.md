# GOOD 2026 static site

Static copy of the GOOD 2026 conference website (www.good2026.openondemand.org),
taken from Squarespace on 2026-10-20 before the Squarespace site was retired.
Laid out like [OSC/GOOD-static](https://github.com/OSC/GOOD-static), the 2025
equivalent, and deployed to GitHub Pages by `.github/workflows/static.yml` on
every push to `main`.

    index.html, <page>/index.html   the Squarespace pages, at their original paths
    s/                              PDFs linked from the site (speaker guidelines, prospectus)
    media/                          home page background video (MP4 from the Squarespace HLS stream) and poster
    squarespace/<host>/             Squarespace CDN assets (images, CSS, JS, fonts)
    pretalx/good-2026/              copy of the pretalx schedule: talk and speaker
                                    pages, widget data, and exports (json, xml, ics, xcal)
    pretalx/static, pretalx/media   pretalx stylesheets, scripts and speaker avatars

The schedule page's pretalx widget reads from `pretalx/good-2026/`, so the
schedule works without pretalx.com. Google Maps and Google Fonts still load
from Google.

To point the old hostname here, add a `CNAME` file containing
`www.good2026.openondemand.org` and change that DNS record to a CNAME for the
Pages host.

## Preview

    python3 -m http.server 8000

Speaker photos and abstracts are © their authors; conference photos and logos
belong to the conference sponsors and hosts.
