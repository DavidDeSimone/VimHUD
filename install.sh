#!/bin/bash
#Install Script for VimHud

echo "alias vim='vim -w ~/.vimlog \"\$@\"'" >> ~/.bashrc
export PYTHONPATH=$PYTHONPATH:~/.vim/bundle/VimHUD/plugin
