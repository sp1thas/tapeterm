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

import menu, playlist, exit, home, lang
from termcolor import colored
from lang import curr_lang
from head import head

def ListMenu():
    if not curr_lang():
        title = head() + '''Διάθεση'''

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
    elif curr_lang():
        title = head() + '''Mood'''

        options =   [
                        {"name":"Happy","function":xaroumenes},
                        {"name":"Relaxing","function":xalarwtikes},
                        {"name":"Melancholy","function":melagxolikes},
                        {"name":"Reading","function":reading},
                        {"name":"Sexy","function":sexy},
                        {"name":"Erotic","function":erotic},
                        #{"name":"Party","function":party}
                        {"name":colored("Home Menu","yellow"),"function":home.ListMenu},
                        {"name":colored("Exit", "red"),"function":exit.exit}
                    ]
    MoodMenu = menu.Menu(title)
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
    playlist.FullList('Party','mood.ListMenu')
