#!/bin/bash

SCRIPT_PATH=$(dirname $(realpath $0))

mkdir -p "$SCRIPT_PATH"/data

python3 "$SCRIPT_PATH/kde-window-status-restore.py" save

