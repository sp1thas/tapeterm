# -*- coding: utf-8 -*-
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
                    #{"name":"Sexy","function":sexy},
                    #{"name":"Ερωτικές","function":erotic},
                    #{"name":"Party","function":party}
                    {"name":colored("Home Menu","yellow"),"function":home.ListMenu},
                    {"name":colored("Έξοδος", "red"),"function":exit.exit}
                ]
    MoodMenu.addOptions(options)
    MoodMenu.open()


def xaroumenes():
    playlist.FullList('Xaroumenes')

def xalarwtikes():
    playlist.FullList('Xalarwtikes')

def melagxolikes():
    playlist.FullList('Melagxolikes')

def reading():
    playlist.FullList('Reading')

def sexy():
    pass

def erotic():
    pass
def party():
    pass
