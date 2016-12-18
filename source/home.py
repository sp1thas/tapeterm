# -*- coding: utf-8 -*-
#   ===================================
#       kasetophon sto termatiko
#   ===================================
#              home
#   ===================================
__author__ = "Simakis Panagiotis"
__license__ = "GPL"
__email__ = "sp1thas@autistici.org"
#   ===================================

import menu, sys, exit
import ksena, greek, categories, mood, alternative_indie, lovers, roulette, dj, twentyfour, playlist
from termcolor import colored
from lang import curr_lang
def ListMenu():
	if not curr_lang():
		title = 'Κεντρικό Μενού'
		MainMenu = menu.Menu(title)
		options =   [
						{"name":"Ξένα","function":ksena.ListMenu},
						{"name":"Ελληνικά","function":greek.ListMenu},
						{"name":"Κατηγορίες","function":categories.ListMenu},
						{"name":"Διάθεση","function":mood.ListMenu},
						{"name":"24ωρο","function":twentyfour.ListMenu},
						{"name":"Lovers","function":lovers.ListMenu},
						#{"name":"Events","function":events.menu},
						#{"name":"Ρουλέτα","function":roulette.menu},
						{"name":"DJ","function":dj.menu},
						{"name":"Month's tape","function":month},
						{"name":colored("Έξοδος", "red"),"function":exit.exit}
					]
		MainMenu.addOptions(options)
		MainMenu.open()
	elif curr_lang():
		title = 'Κεντρικό Μενού'
		MainMenu = menu.Menu(title)
		options =   [
						{"name":"International","function":ksena.ListMenu},
						{"name":"Greek Music","function":greek.ListMenu},
						{"name":"Categories","function":categories.ListMenu},
						{"name":"Mood","function":mood.ListMenu},
						{"name":"TwentyFour","function":twentyfour.ListMenu},
						{"name":"Lovers","function":lovers.ListMenu},
						#{"name":"Events","function":events.menu},
						#{"name":"Ρουλέτα","function":roulette.menu},
						{"name":"DJ","function":dj.menu},
						{"name":"Month's tape","function":month},
						{"name":colored("Exit", "red"),"function":exit.exit}
					]
		MainMenu.addOptions(options)
		MainMenu.open()
def month():
    playlist.FullList('Month','home.ListMenu()')
