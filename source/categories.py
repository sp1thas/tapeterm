# -*- coding: utf-8 -*-
#   ===================================
#       kasetophon sto termatiko
#   ===================================
#               categories
#   ===================================
__author__ = "Simakis Panagiotis"
__license__ = "GPL"
__email__ = "sp1thas@autistici.org"
#   ===================================

import menu, exit, lovers
import playlist, home, mood, ksena, twentyfour
from termcolor import colored
from lang import curr_lang
from head import *
def ListMenu():
    if not curr_lang():
        title = head() + '''Ξένα'''
        options =   [
                        #{"name":"Καλοκαιρινές","function":kalokairines},
                        {"name":"24ωρο","function":twentyfour.ListMenu},
                        {"name":"Διάθεση","function":mood.ListMenu},
                        {"name":"Μουσικά Είδη","function":mousika_eidi},
                        {"name":"Lovers","function":lovers.ListMenu},
                        {"name":"Δραστηριότητα","function":Activity},
                        {"name":"Μέρες","function":Days},
                        #{"name":"Διασκευές/Remixes","function":remixes},
                        #{"name":"Ορχηστρικές","function":orchestral},
                        #{"name":"Ακουστικές","function":popular},
                        #{"name":"More","function":rock},
                        #{"name":"Home Menu", "function":home.Menu}
                        {"name":colored("Home Menu","yellow"),"function":home.ListMenu},
                        {"name":colored("Έξοδος", "red"),"function":exit.exit}
                    ]
    elif curr_lang():
        title = head() + '''International'''
        options =   [
                        #{"name":"Καλοκαιρινές","function":kalokairines},
                        {"name":"TwentyFour","function":twentyfour.ListMenu},
                        {"name":"Mood","function":mood.ListMenu},
                        {"name":"Kind of Music","function":mousika_eidi},
                        {"name":"Lovers","function":lovers.ListMenu},
                        {"name":"Activities","function":Activity},
                        {"name":"Days","function":Days},
                        #{"name":"Διασκευές/Remixes","function":remixes},
                        #{"name":"Ορχηστρικές","function":orchestral},
                        #{"name":"Ακουστικές","function":popular},
                        #{"name":"More","function":rock},
                        #{"name":"Home Menu", "function":home.Menu}
                        {"name":colored("Home Menu","yellow"),"function":home.ListMenu},
                        {"name":colored("Exit", "red"),"function":exit.exit}
                    ]

    CategoriesMenu = menu.Menu(title)
    CategoriesMenu.addOptions(options)
    CategoriesMenu.open()

def kalokairines():
    pass
def Activity():
    playlist.FullList('Activity','mood.ListMenu')
def Days():
    if not curr_lang():
        title = '''
 ____________________________________________________________________________
   _    _                      _                 _
  | |  | |                    | |               | |
 / __) | | __ __ _  ___   ___ | |_  ___   _ __  | |__    ___   _ __    ___
 \__ \ | |/ // _` |/ __| / _ \| __|/ _ \ | '_ \ | '_ \  / _ \ | '_ \  / _ \\
 (   / |   <| (_| |\__ \|  __/| |_| (_) || |_) || | | || (_) || | | || (_) |
  |_|  |_|\_\\\__,_||___/ \___| \__|\___/ | .__/ |_| |_| \___/ |_| |_| \___/
        _          _                     | |  _                _
       (_)        | |                    |_| (_)              | |
        _  _ __   | |_  ___  _ __  _ __ ___   _  _ __    __ _ | |
       | || '_ \  | __|/ _ \| '__|| '_ ` _ \ | || '_ \  / _` || |
       | || | | | | |_|  __/| |   | | | | | || || | | || (_| || |
       |_||_| |_|  \__|\___||_|   |_| |_| |_||_||_| |_| \__,_||_|
 ____________________________________________________________________________

Μέρες'''

        options = [
                    {"name":"Δευτέρα","function":Monday},
                    {"name":"Τρίτη","function":Tuesday},
                    {"name":"Τετάρτη","function":Wednesday},
                    {"name":"Πέμπτη","function":Thursday},
                    {"name":"Παρασκευή","function":Friday},
                    {"name":"Σάββατο","function":Saturday},
                    {"name":"Κυριακή","function":ksena.world},
                    {"name":colored("Previous Menu","green"),"function":ListMenu},
                    {"name":colored("Home Menu","yellow"),"function":home.ListMenu},
                    {"name":colored("Έξοδος", "red"),"function":exit.exit}
                    ]
    elif curr_lang():
        titlle = '''
 ____________________________________________________________________________
   _    _                      _                 _
  | |  | |                    | |               | |
 / __) | | __ __ _  ___   ___ | |_  ___   _ __  | |__    ___   _ __    ___
 \__ \ | |/ // _` |/ __| / _ \| __|/ _ \ | '_ \ | '_ \  / _ \ | '_ \  / _ \\
 (   / |   <| (_| |\__ \|  __/| |_| (_) || |_) || | | || (_) || | | || (_) |
  |_|  |_|\_\\\__,_||___/ \___| \__|\___/ | .__/ |_| |_| \___/ |_| |_| \___/
        _          _                     | |  _                _
       (_)        | |                    |_| (_)              | |
        _  _ __   | |_  ___  _ __  _ __ ___   _  _ __    __ _ | |
       | || '_ \  | __|/ _ \| '__|| '_ ` _ \ | || '_ \  / _` || |
       | || | | | | |_|  __/| |   | | | | | || || | | || (_| || |
       |_||_| |_|  \__|\___||_|   |_| |_| |_||_||_| |_| \__,_||_|
 ____________________________________________________________________________

Days'''

        options = [
                    {"name":"Monday","function":Monday},
                    {"name":"Tuesday","function":Tuesday},
                    {"name":"Wednesday","function":Wednesday},
                    {"name":"Thursday","function":Thursday},
                    {"name":"Friday","function":Friday},
                    {"name":"Saturday","function":Saturday},
                    {"name":"Sunday","function":ksena.world},
                    {"name":colored("Previous Menu","green"),"function":ListMenu},
                    {"name":colored("Home Menu","yellow"),"function":home.ListMenu},
                    {"name":colored("Exit", "red"),"function":exit.exit}
                    ]
    DaysMenu = menu.Menu(title)
    DaysMenu.addOptions(options)
    DaysMenu.open()
def Monday():
    playlist.FullList('Monday','categories.Days()')
def Tuesday():
    playlist.FullList('Tuesday','categories.Days()')
def Wednesday():
    playlist.FullList('Wednesday','categories.Days()')
def Thursday():
    playlist.FullList('Thursday','categories.Days()')
def Friday():
    playlist.FullList('Friday','categories.Days()')
def Saturday():
    playlist.FullList('Saturday','categories.Days()')
def Sunday():
    playlist.FullList('Sunday','categories.Days()')
def mousika_eidi():
    if not curr_lang():
        title = '''
 ____________________________________________________________________________
   _    _                      _                 _
  | |  | |                    | |               | |
 / __) | | __ __ _  ___   ___ | |_  ___   _ __  | |__    ___   _ __    ___
 \__ \ | |/ // _` |/ __| / _ \| __|/ _ \ | '_ \ | '_ \  / _ \ | '_ \  / _ \\
 (   / |   <| (_| |\__ \|  __/| |_| (_) || |_) || | | || (_) || | | || (_) |
  |_|  |_|\_\\\__,_||___/ \___| \__|\___/ | .__/ |_| |_| \___/ |_| |_| \___/
        _          _                     | |  _                _
       (_)        | |                    |_| (_)              | |
        _  _ __   | |_  ___  _ __  _ __ ___   _  _ __    __ _ | |
       | || '_ \  | __|/ _ \| '__|| '_ ` _ \ | || '_ \  / _` || |
       | || | | | | |_|  __/| |   | | | | | || || | | || (_| || |
       |_||_| |_|  \__|\___||_|   |_| |_| |_||_||_| |_| \__,_||_|
 ____________________________________________________________________________

Μουσικά Είδη'''
        options = [
                    {"name":"Ροκ","function":ksena.rock},
                    {"name":"HipTripHop","function":HipTripHop},
                    {"name":"Reggae","function":Reggae},
                    {"name":"Τζαζ","function":ksena.jazz},
                    {"name":"Ηλεκτρονικές","function":ksena.electro},
                    {"name":"Alternative","function":ksena.alternative_indie},
                    {"name":"World Music","function":ksena.world},
                    {"name":"Βίντατζ","function":ksena.vintage},
                    {"name":"Διασκευές","function":ksena.remixes},
                    {"name":"Ορχηστρικές","function":ksena.orchestral},
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
                    {"name":colored("Previous Menu","green"),"function":ListMenu},
                    {"name":colored("Home Menu","yellow"),"function":home.ListMenu},
                    {"name":colored("Έξοδος", "red"),"function":exit.exit}
                ]
    elif curr_lang():
        title = '''
 ____________________________________________________________________________
   _    _                      _                 _
  | |  | |                    | |               | |
 / __) | | __ __ _  ___   ___ | |_  ___   _ __  | |__    ___   _ __    ___
 \__ \ | |/ // _` |/ __| / _ \| __|/ _ \ | '_ \ | '_ \  / _ \ | '_ \  / _ \\
 (   / |   <| (_| |\__ \|  __/| |_| (_) || |_) || | | || (_) || | | || (_) |
  |_|  |_|\_\\\__,_||___/ \___| \__|\___/ | .__/ |_| |_| \___/ |_| |_| \___/
        _          _                     | |  _                _
       (_)        | |                    |_| (_)              | |
        _  _ __   | |_  ___  _ __  _ __ ___   _  _ __    __ _ | |
       | || '_ \  | __|/ _ \| '__|| '_ ` _ \ | || '_ \  / _` || |
       | || | | | | |_|  __/| |   | | | | | || || | | || (_| || |
       |_||_| |_|  \__|\___||_|   |_| |_| |_||_||_| |_| \__,_||_|
 ____________________________________________________________________________

Kind of Music'''
        options = [
                    {"name":"Rock","function":ksena.rock},
                    {"name":"HipTripHop","function":HipTripHop},
                    {"name":"Reggae","function":Reggae},
                    {"name":"Jazz","function":ksena.jazz},
                    {"name":"Electro","function":ksena.electro},
                    {"name":"Alternative","function":ksena.alternative_indie},
                    {"name":"World Music","function":ksena.world},
                    {"name":"Vintage","function":ksena.vintage},
                    {"name":"Remixes","function":ksena.remixes},
                    {"name":"Orchestral","function":ksena.orchestral},
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
                    {"name":colored("Previous Menu","green"),"function":ListMenu},
                    {"name":colored("Home Menu","yellow"),"function":home.ListMenu},
                    {"name":colored("Exit", "red"),"function":exit.exit}
                ]
    MouikaEidiMenu = menu.Menu(title)
    MouikaEidiMenu.addOptions(options)
    MouikaEidiMenu.open()

def HipTripHop():
    playlist.FullList('HipTripHop','categories.Days()')

def Reggae():
    playlist.FullList('Reggae','categories.Days()')
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
