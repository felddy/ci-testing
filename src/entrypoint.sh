#!/bin/sh

set -o nounset
set -o errexit
# shellcheck disable=SC3040
# pipefail is supported by busybox
set -o pipefail

if [ "${1-}" = "--version" ]; then
  cat image_version.txt
  exit 0
fi

sleep 1

echo "I am running on $(cat target_platform.txt)"
echo "I was built on $(cat build_platform.txt)"

sleep 1
