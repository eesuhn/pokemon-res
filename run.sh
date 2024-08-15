#!/bin/bash

TARGET_DIR="$HOME/Pokemon/src/main/resources/pokemon/"

declare -A dirs
dirs=(
	["pokes"]=$TARGET_DIR"pokes/"
	["pokes-static"]=$TARGET_DIR"pokes-static"
	["sfx-misc"]=$TARGET_DIR"sfx/misc/"
	["sfx-moves"]=$TARGET_DIR"sfx/moves/"
)

for dir in "${!dirs[@]}"; do
	cd "$dir" || continue
	python3 main.py
	mv out/* "${dirs[$dir]}"
	cd ..
done
