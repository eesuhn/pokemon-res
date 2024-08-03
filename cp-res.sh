#!/bin/bash

python3 res.py

TARGET_DIR=~/Pokemon/src/main/resources/pokemon/

cp gif/resized/* ${TARGET_DIR}pokes/
cp static/output/* ${TARGET_DIR}pokes-static/
cp sfx/reduced/* ${TARGET_DIR}sfx/moves/
