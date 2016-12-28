# -*- coding: utf-8 -*-
#   ===================================
#       kasetophon sto termatiko
#   ===================================
#              start
#   ===================================
__author__ = "Simakis Panagiotis"
__license__ = "GPL"
__email__ = "sp1thas@autistici.org"
#   ===================================
from subprocess import call
from termcolor import cprint
import lang
from head import head

def SetMPV():
    call(["mpsyt", "set", "player", "mpv,q"])
    call(["clear"])

def logo():
    call(["clear"])
    cprint (head(),'red', attrs=['bold'],)
    tmp = input('Choose language: "1" for English or "2" for Greek\n>>> ')
    return tmp
