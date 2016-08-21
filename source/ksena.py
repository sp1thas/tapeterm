# -*- coding: utf-8 -*-
from termcolor import colored
import menu
import playlist, home, exit

def ListMenu():
    title = 'Ξένα'
    KsenaMenu = menu.Menu(title)
    options =   [
                    {"name":"Δημοφιλείς","function":popular},
                    {"name":"Ροκ","function":rock},
                    #{"name":"Τζαζ","function":jazz},
                    #{"name":"Ηλεκτρονικές","function":electro},
                    #{"name":"Alternative/Indie","function":alternative_indie},
                    #{"name":"World","function":world},
                    #{"name":"Βίντατζ","function":vintage},
                    #{"name":"Διασκευές/Remixes","function":remixes},
                    #{"name":"Ορχηστρικές","function":orchestral},
                    #{"name":"Ακουστικές","function":popular},
                    #{"name":"More","function":rock},
                    #{"name":"Home Menu", "function":home.Menu}
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
    pass
# Alternative/Indie >> 5
def alternative_indie():
    pass
# World >> 6
def world():
    pass
# Βιντατζ >> 7
def vintage():
    pass
# Διασκευές/Remixes >> 8
def remixes():
    pass
# Ορχηστρικές >> 9
def orchestral():
    pass
# Ακουστικές >> 10
def acoustic():
    pass
