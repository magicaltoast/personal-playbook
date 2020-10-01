#!/bin/bash

sudo pacman -S python python-pip ansible

ansible-galaxy install kewlfft.aur jpedrodelacerda.yay kevincoakley.anaconda evandam.conda

ansible-playbook -f 1 -K playbook.yml