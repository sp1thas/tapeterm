# -*- coding: utf-8 -*-
#   ===================================
#       kasetophon sto termatiko
#   ===================================
#              mood
#   ===================================
__author__ = "Simakis Panagiotis"
__license__ = "GPL"
__email__ = "sp1thas@autistici.org"
#   ===================================

import menu, playlist, exit, home
from termcolor import colored

def ListMenu():
    title = 'Διαθεση'
    MoodMenu = menu.Menu(title)
    options =   [
                    {"name":"Χαρούμενες","function":xaroumenes},
                    {"name":"Χαλαρωτικές","function":xalarwtikes},
                    {"name":"Μελαγχολικές","function":melagxolikes},
                    {"name":"Διάβασμα","function":reading},
                    {"name":"Sexy","function":sexy},
                    {"name":"Ερωτικές","function":erotic},
                    #{"name":"Party","function":party}
                    {"name":colored("Home Menu","yellow"),"function":home.ListMenu},
                    {"name":colored("Έξοδος", "red"),"function":exit.exit}
                ]
    MoodMenu.addOptions(options)
    MoodMenu.open()


def xaroumenes():
    playlist.FullList('Xaroumenes','mood.ListMenu')

def xalarwtikes():
    playlist.FullList('Xalarwtikes','mood.ListMenu')

def melagxolikes():
    playlist.FullList('Melagxolikes','mood.ListMenu')

def reading():
    playlist.FullList('Reading','mood.ListMenu')

def sexy():
    playlist.FullList('Sexy','mood.ListMenu')

def erotic():
    playlist.FullList('Erotic','mood.ListMenu')
def party():
    pass
