#!/bin/bash

SCRIPT_PATH=$(dirname $(realpath $0))

export XDG_DATA_HOME=${XDG_DATA_HOME:="$HOME/.local/share"}

python3 "$SCRIPT_PATH/kde-window-status-restore.py" restore

