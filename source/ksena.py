# -*- coding: utf-8 -*-
#   ===================================
#              ksena
#   ===================================
__author__ = "Simakis Panagiotis"
__license__ = "GPL"
__email__ = "sp1thas@autistici.org"
#   ===================================

from termcolor import colored
import menu
import playlist, home, exit, categories

def ListMenu():
    title = 'Ξένα'
    KsenaMenu = menu.Menu(title)
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
                
    KsenaMenu.addOptions(options)
    KsenaMenu.open()


# Δημοφιλείς >> 1
def popular():
    playlist.FullList('Popular')

# Ροκ >> 2
def rock():
    playlist.FullList('Rock')

# Τζαζ >> 3
def jazz():
    playlist.FullList('Jazz')

# Ηλεκτρονικές >> 4
def electro():
    playlist.FullList('Electro')

# Alternative/Indie >> 5
def alternative_indie():
    playlist.FullList('AlternativeIndie')

# World >> 6
def world():
    playlist.FullList('World')

# Βιντατζ >> 7
def vintage():
    playlist.FullList('Vintage')

# Διασκευές/Remixes >> 8
def remixes():
    playlist.FullList('Remixes')

# Ορχηστρικές >> 9
def orchestral():
    playlist.FullList('Orchestral')

# Ακουστικές >> 10
def acoustic():
    playlist.FullList('Acoustic')
