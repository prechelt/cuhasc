# Releasing cuhasc

## One-time setup

Create a PyPI API token scoped to the `cuhasc` project: 
pypi.org -> Account settings -> API tokens -> "Add API token" -> scope it to the `cuhasc` project.

## Making a release

1. Bump `version` in `pyproject.toml` and commit that change.
2. Run:
   ```
   export UV_PUBLISH_TOKEN=pypi-...
   cmd/release.sh
   ```
   (add `--yes`/`-y` to skip the confirmation prompt, e.g. for scripted use).

The script refuses to run if the working tree isn't clean, if the version's git tag already
exists, or if `UV_PUBLISH_TOKEN` isn't set. 
On success, it builds the sdist/wheel with `uv build`, 
uploads them with `uv publish`, 
then tags the release (`vX.Y.Z`) and 
pushes the tag -- tagging/pushing only happen after a successful publish.
