#!/bin/bash

# check if already have the repo 
if [ "${PWD##*/}" != TapeTerm ]
then
	# if not then clone it
	git clone https://github.com/sp1thas/TapeTerm.git
fi

#capture the user distro
OS=$(lsb_release -si)

if [  $OS = "Fedora" ]
then
  sudo yum -y install python-pip python3-pip mpv
elif [ $OS = "Ubuntu" ] || [ $OS = "Debian" ]
then
	sudo apt-get --assume-yes install python-pip python3-pip mpv
elif [$OS = "Arch"]
then
  sudo pacman -S --yes python2-pip python3-pip mpv
else
  echo "We can't install dependencies packages"
fi

clear
sudo pip2 install menu termcolor
sudo pip3 install mps-youtube
clear
mpsyt set player mpv,q
clear

echo "Ready"

echo "Do you want to start kasetophono_sto_termatiko now? (Y/n)"
read Choise

if [ $Choise = "Y" ] || [ $Choise="y" ]
then
  clear
  cd TapeTerm
  python2 kasetophono.py
else
  exit
fi
  clear
