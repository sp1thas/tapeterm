# Kasetophono in Terminal
## [Κασετόφωνο](http://www.kasetophono.com) στο Τερματικό

python project for listening [Kasetophono](http://www.kasetophono.com)'s youtube playlists from your terminal
---
Παίξε τις playlist απο το κασετόφωνο στο τερματικό σου. Προς το παρόν είναι είναι λίγες οι playlist και οι κατηγορίες.

με την πάροδο του χρόνου θα προσθέτονται και άλλες.

---

## Prerequirements

### Auto Installation - Build and Run

`git clone https://github.com/sp1thas/kasetophono_sto_termatiko.git & cd kasetophono_sto_termatiko`

`chmod -X build.sh`

then run as root:

`sh build.sh`

### Manual Installation

run as root:

* **Debian\/Ubuntu** based:

`apt-get install mpv python2 python2-pip python3-pip`

`pip3 install mps-youtube`

`pip2 install termcolor menu`

* **Fedora** based:

`yum install mpv python2 python2-pip python3-pip`

`pip3 install mps-youtube`

`pip2 install termcolor menu`

* **Arch** based

`pacman -S install mpv python2 python2-pip python3-pip`

`pip3 install mps-youtube`

`pip2 install termcolor menu`

### [MPV](https://mpv.io/)

* Installation:
  run as root:
  * **Debian\/Ubuntu** based:
    `apt-get install mpv`
  * **Fedora** based:
    `yum install mpv`
  * **Arch** based:
    `pacman -S mpv`


### Python

* Installation:

  run as root
  * **Debian\/Ubuntu** based:
    `apt-get install python2`
  * **Fedora** based:
    `yum install python2`
  * Arch based:
    `pacman -S python2`


### PIP \(Python Package Management\)

* Installation

  * **Debian\/Ubuntu** based:
    `apt-get install python2-pip python3-pip`
  * **Fedora** based:
    `yum install python2-pip python3-pip`
  * **Arch** based:
    `pacman -S python2-pip python3-pip`


### Python Modules

* [termcolor](https://pypi.python.org/pypi/termcolor)

  * Installation
    `sudo pip2 install termcolor`


* [menus](https://pypi.python.org/pypi/Menus)

  * Installation:
    `sudo pip2 install menu`


* [mps-youtube](https://github.com/mps-youtube/)

  * Installation:
    `sudo pip3 install mps-youtube`


`git clone https://github.com/sp1thas/kasetophono_sto_termatiko.git & cd kasetophono_sto_termatiko`

## Usage

just run kasetophono.py

`python2 kasetophono.py`

## Start Page

![](/assets/python-start.png)

## Main menu

![](/assets/python-main.png)

## Sub menu

![](/assets/python-submenu.png)

## Playlists

![](/assets/python-playlist.png)
