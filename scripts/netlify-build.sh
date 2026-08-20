#!/usr/bin/env bash
# Build the Sphinx handbook on Netlify (deploy previews).
set -euo pipefail

# Full history for sphinx-last-updated-by-git last-updated dates.
if [ "$(git rev-parse --is-shallow-repository)" = "true" ]; then
  git fetch --unshallow
fi
git fetch --tags || true

python -m pip install --upgrade pip
python -m pip install nox
nox -s docs
