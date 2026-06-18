# Render Culture Profile plots as server-side inline SVG

The Culture Profile and Team Culture Profile plots (five horizontal [1,5] axes with dots
per Dimension) are rendered as inline SVG generated server-side in the Django layer, rather
than with matplotlib or a client-side JS charting library.

The plot is geometrically trivial (a handful of lines, dots, and labels), so a charting
library is overkill. matplotlib was rejected because it drags in numpy and a large binary
dependency tree, which conflicts with the NFRs that CuHaSc run "on any system that has
Python 3 installed" and be "distributed as a single file." Inline SVG needs no new
dependency (Python or JS), renders identically everywhere, and prints cleanly.

Future requirement: handbook sections will be attached to certain constellations of Scores.
Whether that attachment is server-side conditional content or click-interactive is unknown.
Inline SVG keeps both paths open — it can stay static or have vanilla JS hung on it later —
whereas a matplotlib raster would have foreclosed interactivity.
