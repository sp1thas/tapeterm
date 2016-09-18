# -*- coding: utf-8 -*-
#   ===================================
#       kasetophon sto termatiko
#   ===================================
#               greek
#   ===================================
__author__ = "Simakis Panagiotis"
__license__ = "GPL"
__email__ = "sp1thas@autistici.org"
#   ===================================

import menu, playlist, home, exit
from termcolor import colored

def ListMenu():
    title = 'Ελληνικά'
    GreekMenu = menu.Menu(title)
    options =   [

{"name":"Έντεχνες","function":Entexnes},
{"name":"Λαικές/Ρεμπέτικες","function":LaikesRempetikes},
{"name":"Όμορφες","function":Omorfes},
{"name":"Αγγλόφωνες/Αλτέρνατιβ","function":AggloAltern},
# {"name":"Θεματικές","function":Thematikes},
{"name":"Βίντατζ","function":GreekVintage},
{"name":"Αφιερώματα","function":Afieromata},
{"name":"Παραδοσιακές","function":Paradosiakes},
{"name":"Παιδικές","function":Paidikes},
{"name":colored("Home Menu","yellow"),"function":home.ListMenu},
{"name":colored("Έξοδος", "red"),"function":exit.exit}
                ]

    GreekMenu.addOptions(options)
    GreekMenu.open()

def Entexnes():
    playlist.FullList('Entexnes','greek.ListMenu()')

def LaikesRempetikes():
    playlist.FullList('LaikesRempetikes', 'greek.ListMenu()')

def Omorfes():
    playlist.FullList('Omorfes', 'greek.ListMenu()')

def AggloAltern():
    playlist.FullList('AggloAltern', 'greek.ListMenu()')

def Thematikes():
    pass
    # ThematikesMenu = menu.Menu('Θεματικές')
    # options = [
    #     {"name":"","function":},
    #     {"name":colored("Home Menu","yellow"),"function":home.ListMenu},
    #     {"name":colored("Έξοδος", "red"),"function":exit.exit}
    # ]
    # ThematikesMenu.addOptions(options)
    # ThematikesMenu.open()

def GreekVintage():
    playlist.FullList('GreekVintage', 'greek.ListMenu()')

def Afieromata():
    playlist.FullList('Afieromata','greek.ListMenu')

def Paradosiakes():
    playlist.FullList('Paradosiakes', 'greek.ListMenu()')

def Paidikes():
    playlist.FullList('Paidikes', 'greek.ListMenu()')
