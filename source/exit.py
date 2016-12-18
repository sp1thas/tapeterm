# -*- coding: utf-8 -*-
#   ===================================
#       kasetophon sto termatiko
#   ===================================
#               exit
#   ===================================
__author__ = "Simakis Panagiotis"
__license__ = "GPL"
__email__ = "sp1thas@autistici.org"
#   ===================================
from subprocess import call
import sys, lang

def exit():
    call(["clear"])
    print "See Ya!"
    sys.exit()
