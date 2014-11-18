VimHUD is used an addon for Vim built in python and VimScript, that recommends commands for you to learn. VimHUD remembers which commands you know and can identify which commands will reduce the most amount of keystrokes and displays a new command on the bottom of your screen.

Installation: The easiest way to install is to use pathogen. After installing pathogen clone this repo into your .vim/bundle folder. After this, run the following shell script:

~/.vim/bundle/VimParser/install.sh

This is needed for VimHUD to record you keystrokes while you are in vim. This may change in the future if we find a better way of doing this.

After that, just launch vim and you'll be getting suggestions in no time! To increase or decrease the rate of suggestion, you can do

:set updatetime=<some number>

Lower means faster updates, and higher means slower updates. We are still experimenting with the default value.

Please understand that we are still in a development state, so please bare with us and report any bugs :)

Dependencies:
Python 2.7
