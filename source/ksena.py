# -*- coding: utf-8 -*-
#   ===================================
#       kasetophon sto termatiko
#   ===================================
#              ksena
#   ===================================
__author__ = "Simakis Panagiotis"
__license__ = "GPL"
__email__ = "sp1thas@autistici.org"
#   ===================================

from termcolor import colored
import menu, lang
import playlist, home, exit, categories
from lang import curr_lang
from head import head
def ListMenu():
    if not curr_lang():
        title = head() + '''Ξένα'''
        options =   [
        {"name":"Δημοφιλείς","function":popular}, {"name":"Ροκ","function":rock},
        {"name":"Τζαζ","function":jazz}, {"name":"Ηλεκτρονικές","function":electro},
        {"name":"Alternative/Indie","function":alternative_indie}, {"name":"World","function":world},
        {"name":"Βίντατζ","function":vintage}, {"name":"Διασκευές/Remixes","function":remixes},
        {"name":"Ορχηστρικές","function":orchestral}, {"name":"Ακουστικές","function":acoustic},
        {"name":"More","function":categories.ListMenu},
        {"name":colored("Home Menu","yellow"),"function":home.ListMenu},
        {"name":colored("Έξοδος", "red"),"function":exit.exit}
        ]
    elif curr_lang():
        title = head() + '''International'''
        options =   [
        {"name":"Popular","function":popular}, {"name":"Ροκ","function":rock},
        {"name":"Jazz","function":jazz}, {"name":"Electro","function":electro},
        {"name":"Alternative/Indie","function":alternative_indie}, {"name":"World","function":world},
        {"name":"Vintage","function":vintage}, {"name":"Remixes","function":remixes},
        {"name":"Orchestral","function":orchestral}, {"name":"Acoustic","function":acoustic},
        {"name":"More","function":categories.ListMenu},
        {"name":colored("Home Menu","yellow"),"function":home.ListMenu},
        {"name":colored("Exit", "red"),"function":exit.exit}
        ]
    KsenaMenu = menu.Menu(title)
    KsenaMenu.addOptions(options)
    KsenaMenu.open()


# Δημοφιλείς >> 1
def popular():
    playlist.FullList('Popular', 'ksena.ListMenu()')

# Ροκ >> 2
def rock():
    playlist.FullList('Rock', 'ksena.ListMenu()')

# Τζαζ >> 3
def jazz():
    playlist.FullList('Jazz', 'ksena.ListMenu()')

# Ηλεκτρονικές >> 4
def electro():
    playlist.FullList('Electro', 'ksena.ListMenu()')

# Alternative/Indie >> 5
def alternative_indie():
    playlist.FullList('AlternativeIndie', 'ksena.ListMenu()')

# World >> 6
def world():
    playlist.FullList('World', 'ksena.ListMenu()')

# Βιντατζ >> 7
def vintage():
    playlist.FullList('Vintage', 'ksena.ListMenu()')

# Διασκευές/Remixes >> 8
def remixes():
    playlist.FullList('Remixes', 'ksena.ListMenu()')

# Ορχηστρικές >> 9
def orchestral():
    playlist.FullList('Orchestral', 'ksena.ListMenu()')

# Ακουστικές >> 10
def acoustic():
    playlist.FullList('Acoustic', 'ksena.ListMenu()')
