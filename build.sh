#!/bin/bash

OS=$(lsb_release -si)
                    #capture the user distro

    if [  $OS = "Fedora" ]; then

   		sudo yum install python2-pip python3-pip mpv

    elif [ $OS = "Ubuntu" ] || [ $OS = "Debian" ]; then

  		sudo apt-get install python2-pip python3-pip mpv

    elif [$OS = "Arch"]; then
      sudo pacman -S python-pip2 python3-pip mpv
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
    if [ $Choise = "Y" ] || [ $Choise="y" ]; then
      clear
      python kasetophono.py
    else
      exit
    fi
    clear
