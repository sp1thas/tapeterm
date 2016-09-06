# -*- coding: utf-8 -*-
#   ===================================
#       kasetophon sto termatiko
#   ===================================
#               lovers
#   ===================================
__author__ = "Simakis Panagiotis"
__license__ = "GPL"
__email__ = "sp1thas@autistici.org"
#   ===================================

import menu, exit, playlist, home
from termcolor import colored

def ListMenu():
    title = 'Lovers'
    LoversMenu = menu.Menu(title)
    options =   [

{"name":"Coffee Lovers","function":CoffeeLovers}, {"name":"Food Lovers","function":FoodLovers},
{"name":"Alcohol Lovers","function":AlcoholLovers}, {"name":"Book Lovers","function":BookLovers},
{"name":"Bed Lovers","function":BedLovers}, {"name":"Travel Lovers","function":TravelLovers},
{"name":"Rain Lovers","function":RainLovers}, {"name":"Sea Lovers","function":SeaLovers},
{"name":"Sun Lovers","function":SunLovers},
{"name":colored("Home Menu","yellow"),"function":home.ListMenu},
{"name":colored("Έξοδος", "red"),"function":exit.exit}
                ]

    LoversMenu.addOptions(options)
    LoversMenu.open()


def CoffeeLovers():
    playlist.FullList('CoffeeLovers','lovers.ListMenu()')

def FoodLovers():
    playlist.FullList('FoodLovers','lovers.ListMenu()')
def AlcoholLovers():
    playlist.FullList('AlcoholLovers','lovers.ListMenu()')
def BookLovers():
    playlist.FullList('BookLovers','lovers.ListMenu()')
def BedLovers():
    playlist.FullList('BedLovers','lovers.ListMenu()')
def TravelLovers():
    playlist.FullList('TravelLovers','lovers.ListMenu()')
def RainLovers():
    playlist.FullList('RainLovers','lovers.ListMenu()')
def SeaLovers():
    playlist.FullList('SeaLovers','lovers.ListMenu()')
def SunLovers():
    playlist.FullList('SunLovers','lovers.ListMenu()')
=======
    playlist.FullList('SeaLovers')
def SunLovers():
    playlist.FullList('SunLovers')
>>>>>>> 843615b6c9570c5b4a35849b0e1f4c66ba11a065
