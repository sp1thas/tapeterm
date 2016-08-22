# -*- coding: utf-8 -*-
#   ===================================
#               twentyfour
#   ===================================
__author__ = "Simakis Panagiotis"
__license__ = "GPL"
__email__ = "sp1thas@autistici.org"
#   ===================================

from termcolor import colored
import menu
import playlist, home, exit

def ListMenu():
    title = '24ωρο'
    CurrentMenu = menu.Menu(title)
    options =   [
                    {"name":"Πρωί","function":Morning},
                    {"name":"Μεσημέρι","function":Noon},
                    {"name":"Απόγευμα","function":AfterNoon},
                    {"name":"Νύχτα","function":Night},
                    {"name":colored("Home Menu","yellow"),"function":home.ListMenu},
                    {"name":colored("Έξοδος", "red"),"function":exit.exit}
                ]
    CurrentMenu.addOptions(options)
    CurrentMenu.open()

def Morning():
    playlist.FullList('Morning')
def Noon():
    playlist.FullList('Noon')
def AfterNoon():
    playlist.FullList('AfterNoon')
def Night():
    playlist.FullList('Night')
