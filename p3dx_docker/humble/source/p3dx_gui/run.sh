#!/bin/bash

Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Run the Python script directly
"$SCRIPT_DIR/main_window_custom_class.py"


