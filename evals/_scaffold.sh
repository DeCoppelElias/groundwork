#!/bin/sh
# Copies the sample project into the empty eval workspace and makes it a git repo.
set -e
sample="$(cd "$(dirname "$0")/.." && pwd)/_sample"
cp -R "$sample/." .
git init -q -b main
git add -A
git -c user.name=eval -c user.email=eval@example.com commit -q -m "sample"
