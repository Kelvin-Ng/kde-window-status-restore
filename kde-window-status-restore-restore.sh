#!/bin/bash

SCRIPT_PATH=$(dirname $(realpath $0))

python3 "$SCRIPT_PATH/kde-window-status-restore.py" restore

