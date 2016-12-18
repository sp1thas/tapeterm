#!/bin/bash
x-terminal-emulator -e 'python2 kasetophono.py' || { gnome-terminal -e 'python2 kasetophono.py' >&2; exit 1; }
