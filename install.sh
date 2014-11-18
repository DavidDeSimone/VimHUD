#!/bin/bash
#Install Script for VimHud

echo "alias vim='vim -w ~/.vimlog \"\$@\"'" >> ~/.bashrc
echo "export PYTHONPATH='~/.vim/bundle/VimParser/plugin'" >> ~/.bashrc
