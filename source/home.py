# -*- coding: utf-8 -*-
import menu, sys, exit
import ksena, greek, categories, mood, alternative_indie, lovers, events, roulette, dj, twentyfour
from termcolor import colored
def ListMenu():
    title = 'Κεντρικό Μενού'
    MainMenu = menu.Menu(title)
    options =   [
                    {"name":"Ξένα","function":ksena.ListMenu},
                    #{"name":"Ελληνικά","function":greek.menu},
                    {"name":"Κατηγορίες","function":categories.ListMenu},
                    {"name":"Διάθεση","function":mood.ListMenu},
                    {"name":"24ωρο","function":twentyfour.ListMenu},
                    #{"name":"Lovers","function":lovers.menu},
                    #{"name":"Events","function":events.menu},
                    #{"name":"Ρουλέτα","function":roulette.menu},
                    #{"name":"DJ","function":dj.menu},
                    {"name":colored("Έξοδος", "red"),"function":exit.exit}
                ]
    MainMenu.addOptions(options)
    MainMenu.open()
