# -*- coding: utf-8 -*-
#   ===================================
#       kasetophon sto termatiko
#   ===================================
#              dj
#   ===================================
__author__ = "Simakis Panagiotis"
__license__ = "GPL"
__email__ = "sp1thas@autistici.org"
#   ===================================

import menu, playlist, home, exit, lang
from termcolor import colored

def menu():
    playlist.FullList('DJ','greek.ListMenu()')
