# Vendor Bootstrap locally instead of loading it from the jsdelivr CDN

Bootstrap 5.3.3's CSS and JS bundle are now vendored into
`cuhasc/static/cuhasc/vendor/bootstrap/` and served same-origin via WhiteNoise, rather than
loaded from `cdn.jsdelivr.net` as `base.html` previously did.

Two independent reasons drove this:
Being GDPR-compliant (which fetching from a CDN is not),
being able to run locally without internet access (which fetching from a CDN is also not).

The cost accepted: roughly 250 KB added to the installed wheel. 
Bumping the Bootstrap version now requires manually re-downloading and re-vendoring the two files.

No sourcemaps were vendored (they're devtools-only, not needed to serve the app), and no
`integrity`/`crossorigin` attributes remain in `base.html` — those exist to protect against a
compromised or malicious *third-party* host, which is moot once the files are same-origin. 
The hashes were checked once at vendoring time.
