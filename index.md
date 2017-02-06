<title>Panagiotis Simakis ➔ TapeTerm</title>
# Kasetophono in Terminal
![logo](assets/logo.png)

**TapeTerm**

This is a python project for listening [Kasetophono](http://www.kasetophono.com)'s youtube playlists from your terminal

Play kasetophono's playlists directly from your terminal
Available languages: English, Greek.
---

## Prerequirements

### Auto Installation - Build and Run

```bash
wget https://raw.githubusercontent.com/sp1thas/TapeTerm/master/build.sh; sh build.sh
```

### Manual Installation

run as root:

* **Debian/Ubuntu** based:

```bash
➔ apt-get install mpv python2 python2-pip python3-pip
➔ pip3 install mps-youtube
➔ pip2 install termcolor menu
```

* **Fedora** based:

```bash
➔ yum install mpv python2 python2-pip python3-pip
➔ pip3 install mps-youtube
➔ pip2 install termcolor menu
```

* **Arch** based

```bash
➔ pacman -S install mpv python2 python2-pip python3-pip
➔ pip3 install mps-youtube
➔ pip2 install termcolor menu
```

### [MPV](https://mpv.io/)

* Installation:
  run as root:
  * **Debian/Ubuntu** based:
    `➔ apt-get install mpv`
  * **Fedora** based:
    `➔ yum install mpv`
  * **Arch** based:
    `➔ pacman -S mpv`


### Python

* Installation:

  run as root:

  * **Debian/Ubuntu** based:
  `➔ apt-get install python2`

  * **Fedora** based:
  `➔ yum install python2`

  * **Arch** based:
  `➔ pacman -S python2`


### PIP \(Python Package Management\)

* Installation

  * **Debian/Ubuntu** based:
    `➔ apt-get install python2-pip python3-pip`

  * **Fedora** based:
    `➔ yum install python2-pip python3-pip`

  * **Arch** based:
    `➔ pacman -S python2-pip python3-pip`


### Python Modules

* [termcolor](https://pypi.python.org/pypi/termcolor)

  * Installation
  `➔ sudo pip2 install termcolor`


* [menus](https://pypi.python.org/pypi/Menus)

  * Installation:
    `➔ sudo pip2 install menu`


* [mps-youtube](https://github.com/mps-youtube/)

  * Installation:
    `➔ sudo pip3 install mps-youtube`

## Usage

just run kasetophono.py

```bash
$ python2 kasetophono.py
```

## Demo
<script type="text/javascript" src="https://asciinema.org/a/102102.js" id="asciicast-102102" async></script>

## Author
Simakis Panagiotis [sp1thas@autistici.org](mailto://sp1thas@autistici.org) (Initial work )

## Licence
This project is licensed under the GNU General Public License version 3 - see the [LICENSE.md](LICENSE.md) file for details
<style>
.asciicast{
  padding: 10px;
  background: #f8f8f8;
  border-radius: 5px;
  border: 1px solid #e5e5e5;
}
.powered{
  display:none;
}
.asciinema-player{
  border-radius: 5px;
}
.iframe{
  padding: 5px;
}
</style>
