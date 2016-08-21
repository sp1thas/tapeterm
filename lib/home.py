# -*- coding: utf-8 -*-
import menu, sys, exit
import ksena, greek, categories, mood, alternative_indie, lovers, events, roulette, dj
from termcolor import colored
def Menu():
    title = 'Κεντρικό Μενού'
    MainMenu = menu.Menu(title)
    options =   [
                    {"name":"Ξένα","function":ksena.Menu},
                    #{"name":"Ελληνικά","function":greek.menu},
                    {"name":"Κατηγορίες","function":categories.Menu},
                    {"name":"Διάθεση","function":mood.Menu},
                    #{"name":"24ωρο","function":alternative_indie},
                    #{"name":"Lovers","function":lovers.menu},
                    #{"name":"Events","function":events.menu},
                    #{"name":"Ρουλέτα","function":roulette.menu},
                    #{"name":"DJ","function":dj.menu},
                    {"name":colored("Έξοδος", "red"),"function":exit.exit}
                ]
    MainMenu.addOptions(options)
    MainMenu.open()
