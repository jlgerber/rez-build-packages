#!/usr/bin/env bash

pkg=$(basename $(pwd))
versions=("21.10b0")
pyvers=("3.7" "3.9.5")

if [[ "$1" == "-r" ]]; then
	release_or_install="-i -r"
else
	release_or_install="-i"
fi

for version in $versions; do
	for pyver in $pyvers; do
		rez pip ${release_or_install} ${pkg}==${version} --python-version $pyver 
	done
done
