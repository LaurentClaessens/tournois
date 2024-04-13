#!/bin/bash


MAIN_DIR=$(pwd)
VENV_DIR="$MAIN_DIR/venv"
BIN_DIR="$VENV_DIR/bin"
PYTHON_VERSION=3.10.6

PYTHON3="$HOME/.pyenv/versions/$PYTHON_VERSION/bin/python3"

echo "Creating the virtual environment"
"$PYTHON3" -m venv "$VENV_DIR"

cd "$BIN_DIR" || exit 1
./pip3 install --upgrade pip

cd "$BIN_DIR" || exit 1
./pip3 install -r "$MAIN_DIR/requirements.txt"
./pip3 freeze
