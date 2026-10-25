#!/usr/bin/env bash
set -euo pipefail

PKG_NAME="icinga-installer"

fail() {
  echo "ERROR: $*" >&2
  exit 1
}

if command -v rpm >/dev/null 2>&1; then
  rpm -q "$PKG_NAME" >/dev/null 2>&1 || fail "RPM package $PKG_NAME is not installed"
elif command -v dpkg-query >/dev/null 2>&1; then
  dpkg-query -W -f='${Status}\n' "$PKG_NAME" 2>/dev/null | grep -q '^install ok installed$' \
    || fail "DEB package $PKG_NAME is not installed"
else
  fail "Neither rpm nor dpkg-query is available"
fi

echo "Smoke test passed: package and kafo gem are installed"
