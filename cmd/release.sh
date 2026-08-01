#!/bin/bash
set -eo pipefail

# ----- call args:
skip_confirm=0
for arg in "$@"; do
  case "$arg" in
    --yes|-y) skip_confirm=1 ;;
    *) echo "Usage: $0 [--yes|-y]" >&2; exit 1 ;;
  esac
done

# ----- read version from pyproject.toml (single source of truth):
version=$(python3 -c "import tomllib; print(tomllib.load(open('pyproject.toml', 'rb'))['project']['version'])")
tag="v$version"

# ----- preflight checks:
if [ -n "$(git status --porcelain)" ]; then
  echo "!!! working tree is not clean -- commit or stash first !!!" >&2
  exit 1
fi
if git rev-parse -q --verify "refs/tags/$tag" >/dev/null; then
  echo "!!! tag $tag already exists locally -- has this version already been released? !!!" >&2
  exit 1
fi
if [ -z "$UV_PUBLISH_TOKEN" ]; then
  echo "!!! UV_PUBLISH_TOKEN is not set -- export a PyPI API token first (see docs/RELEASING.md) !!!" >&2
  exit 1
fi

# ----- confirm:
cat <<PLAN
About to release cuhasc $version:
  1. rm -rf dist/
  2. uv build
  3. uv publish            (uploads dist/* to PyPI)
  4. git tag -a $tag -m "cuhasc $version"
  5. git push origin $tag
PLAN
if [ "$skip_confirm" -ne 1 ]; then
  read -r -p "Proceed? [y/N] " reply
  case "$reply" in
    [yY]|[yY][eE][sS]) ;;
    *) echo "Aborted." >&2; exit 1 ;;
  esac
fi

# ----- do it (tag/push only after a successful publish, so a failed publish never leaves a
# stray tag):
rm -rf dist/
uv build
uv publish
git tag -a "$tag" -m "cuhasc $version"
git push origin "$tag"

echo "----- released: https://pypi.org/project/cuhasc/$version/ -----"
