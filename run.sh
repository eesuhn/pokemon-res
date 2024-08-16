#!/bin/bash

TARGET_DIR="$HOME/Pokemon/src/main/resources/pokemon/"

declare -A dirs
dirs=(
	["pokes-static"]=$TARGET_DIR"pokes-static"
	["sfx-moves"]=$TARGET_DIR"sfx/moves/"
	["pokes"]=$TARGET_DIR"pokes/"
	# ["sfx-misc"]=$TARGET_DIR"sfx/misc/"
)

for dir in "${!dirs[@]}"; do
	cd "$dir" || continue
	python3 main.py
	mv out/* "${dirs[$dir]}"
	cd ..
done
