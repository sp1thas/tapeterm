# -*- coding: utf-8 -*-
import menu
import ksena, greek, categories, mood, alternative_indie, lovers, events, roulette, dj

def Menu():
    title = 'Κεντρικό Μενού'
    MainMenu = menu.Menu(title)
    options =   [
                    {"name":"Ξένα","function":ksena.Menu},
                    {"name":"Ελληνικά","function":greek.menu},
                    {"name":"Κατηγορίες","function":categories.menu},
                    {"name":"Διάθεση","function":mood.menu},
                    {"name":"24ωρο","function":alternative_indie},
                    {"name":"Lovers","function":lovers.menu},
                    {"name":"Events","function":events.menu},
                    {"name":"Ρουλέτα","function":roulette.menu},
                    {"name":"DJ","function":dj.menu}
                ]
    MainMenu.addOptions(options)
    MainMenu.open()
