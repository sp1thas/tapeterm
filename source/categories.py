# -*- coding: utf-8 -*-
#   ===================================
#               categories
#   ===================================
__author__ = "Simakis Panagiotis"
__license__ = "GPL"
__email__ = "sp1thas@autistici.org"
#   ===================================

import menu, exit
import playlist, home, mood, ksena
from termcolor import colored

def ListMenu():
    title = 'Ξένα'
    CategoriesMenu = menu.Menu(title)
    options =   [
                    {"name":"Διάθεση","function":mood.ListMenu},
                    #{"name":"Καλοκαιρινές","function":kalokairines},
                    #{"name":"24ωρο","function":twentyfour}
                    #{"name":"Μουσικά Είδη","function":electro},
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
    CategoriesMenu.addOptions(options)
    CategoriesMenu.open()

def kalokairines():
    pass
def twentyfour():
    pass

def mousika_eidi():
    title = "Μουσικά Είδη"
    MouikaEidiMenu = menu.Menu(title)
    options = [
                {"name":"Ροκ","function":ksena.rock},
                {"name":"HipTripHop","function":HipTripHop},
                {"name":"Reggae","function":Reggae}
                #{"name":"Τζαζ","function":ksena.jazz},
                #{"name":"Ηλεκτρονικές","function":ksena.electro},
                #{"name":"Alternative","function":ksena.alternative_indie},
                #{"name":"World Music","function":ksena.world},
                #{"name":"Βίντατζ","function":ksena.vintage},
                #{"name":"Διασκευές","function":ksena.remixes},
                #{"name":"Ορχηστρικές","function":ksena.orchestral},
                #{"name":"Beats","function":beats}

                #{"name":"Ambient","function":Ambient},
                #{"name":"Mainstream","function":Mainstream},
                #{"name":"Blues","function":Blues},
                # {"name":"Funk / Soul","function":FunkSoul},
                # {"name":"Swing","function":Swing},
                # {"name":"Soundtracks","function":Soundtracks},
                # {"name":"Παιδικές","function":Paidikes},
                # {"name":"Θεματικές","function":Thematic},
                # {"name":"Αφιερώματα","function":Afieromata}


    ]
    MouikaEidiMenu.addOptions(options)
    MouikaEidiMenu.open()

def HipTripHop():
    playlist.FullList('HipTripHop')

def Reggae():
    playlist.FullList('Reggae')
def Ambient():
    pass
def Mainstream():
    pass
def Blues():
    pass
def FunkSoul():
    pass
def Swing():
    pass
def Soundtracks():
    pass
def Paidikes():
    pass
def Thematic():
    pass
def Afieromata():
    pass
