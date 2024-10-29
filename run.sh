#!/bin/bash

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Change to the script's directory and run docker-compose
echo "$SCRIPT_DIR"/p3dx_docker
cd "$SCRIPT_DIR"/p3dx_docker && docker-compose up --build
