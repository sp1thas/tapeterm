# Kasetophono in Terminal
![logo](assets/logo.png)

*** TapeTerm ***

This is a python project for listening [Kasetophono](http://www.kasetophono.com)'s youtube playlists from your terminal

Play kasetophono's playlists directly from your terminal
Available languages: English, Greek.
---

## Prerequirements

### Auto Installation - Build and Run

```bash
$ git clone http://github.com/sp1thas/kasetophono_in_Terminal.git && cd kasetophono_in_Terminal
$ chmod -X build.sh
```



then run as root:

```bash
$ build.sh
```
### Manual Installation

run as root:

* **Debian/Ubuntu** based:

```bash
$ apt-get install mpv python2 python2-pip python3-pip
$ pip3 install mps-youtube
$ pip2 install termcolor menu
```

* **Fedora** based:

```bash
$ yum install mpv python2 python2-pip python3-pip
$ pip3 install mps-youtube
$ pip2 install termcolor menu
```

* **Arch** based

```bash
$ pacman -S install mpv python2 python2-pip python3-pip
$ pip3 install mps-youtube
$ pip2 install termcolor menu
```

### [MPV](https://mpv.io/)

* Installation:
  run as root:
  * **Debian\/Ubuntu** based:

    ```bash
    $ apt-get install mpv
    ```
  * **Fedora** based:
    ```bash
    $ yum install mpv
    ```
  * **Arch** based:
    ```bash
    $ pacman -S mpv
    ```


### Python

* Installation:

  run as root
  * **Debian/Ubuntu** based:
    ```bash
    $ apt-get install python2
    ```
  * **Fedora** based:
    ```bash
    $ yum install python2
    ```
  * Arch based:
    ```bash
    $ pacman -S python2
    ```


### PIP \(Python Package Management\)

* Installation

  * **Debian/Ubuntu** based:
    ```bash
    $ apt-get install python2-pip python3-pip
    ```
  * **Fedora** based:
    ```bash
    $ yum install python2-pip python3-pip
    ```
  * **Arch** based:
    ```bash
    $ pacman -S python2-pip python3-pip
    ```


### Python Modules

* [termcolor](https://pypi.python.org/pypi/termcolor)

  * Installation
    ```bash
    $ sudo pip2 install termcolor
    ```


* [menus](https://pypi.python.org/pypi/Menus)

  * Installation:
    ```bash
    $ sudo pip2 install menu
    ```


* [mps-youtube](https://github.com/mps-youtube/)

  * Installation:
    ```bash
    $ sudo pip3 install mps-youtube
    ```


```bash
$ git clone https://github.com/sp1thas/kasetophono_sto_termatiko.git & cd kasetophono_sto_termatiko
```

## Usage

just run kasetophono.py

```bash
$ python2 kasetophono.py
```

## Start Page

![](https://raw.githubusercontent.com/sp1thas/TapeTerm/master/assets/1.png)

## Main menu

![](https://raw.githubusercontent.com/sp1thas/TapeTerm/master/assets/2.png)

## Sub menu

![](https://raw.githubusercontent.com/sp1thas/TapeTerm/master/assets/3.png)

## Playlists

![](https://raw.githubusercontent.com/sp1thas/TapeTerm/master/assets/4.png)

## Playing..
![](https://raw.githubusercontent.com/sp1thas/TapeTerm/master/assets/5.png)

## Author
Simakis Panagiotis [sp1thas@autistici.org](mailto://sp1thas@autistici.org) (Initial work )

## Licence
This project is licensed under the GNU General Public License version 3 - see the [LICENSE.md](LICENSE.md) file for details
