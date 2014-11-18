#!/bin/bash
#Install Script for VimHud

echo "alias vim='vim -w ~/.vimlog \"$@\"'" >> ~/.bashrc
export PYTHONPATH='~/.vim/bundle/VimParser/plugin'
