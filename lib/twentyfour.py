# -*- coding: utf-8 -*-
import menu, playlist
from termcolor import colored

def menu():
    title = '24ωρο'
    Menu = menu.Menu(title)
    options =   [
                    {"name":"Πρωί","function":Morning},
                    #{"name":"Μεσημέρι","function":xalarwtikes}
                    #{"name":"Απόγευμα","function":melagxolikes},
                    #{"name":"Νύχτα","function":reading},
                    {"name":colored("Home Menu","yellow"),"function":home.Menu},
                    {"name":colored("Έξοδος", "red"),"function":exit.exit}
                ]
    MoodMenu.addOptions(options)
    MoodMenu.open()

def Morning():
    playlist.FullList('Morning')
