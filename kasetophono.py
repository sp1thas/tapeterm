#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#   ===================================
#        Kasetophono sto termatiko
#   ===================================
__author__ = "Simakis Panagiotis"
__license__ = "GPL"
__email__ = "sp1thas@autistici.org"
#   ===================================
from subprocess import call
from source import *
from source import start
from source import lang
from source import home

language_input = start.logo()

lang.set_lang(language_input)

home.ListMenu()
