#!/bin/zsh
#
# i.hackon
# ********
#
# Installation script for hackon.io
#
# author: Arturo "hellais" Filastò <art@fuffa.org>
# license: see LICENSE

git clone https://github.com/hellais/hackon.git $HOME/.hackon
echo "# This was added by MMDA" >> $HOME/.zshrc
echo "source $HOME/.hackon/hackon" >> $HOME/.zshrc
