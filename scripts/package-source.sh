#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p dist
git archive --format=zip --output=dist/personal-device-link-v0151-mac-source.zip HEAD
echo 'Created dist/personal-device-link-v0151-mac-source.zip from committed HEAD'
