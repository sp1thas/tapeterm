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
    playlist.FullList('CoffeeLovers')

def FoodLovers():
    playlist.FullList('FoodLovers')
def AlcoholLovers():
    playlist.FullList('AlcoholLovers')
def BookLovers():
    playlist.FullList('BookLovers')
def BedLovers():
    playlist.FullList('BedLovers')
def TravelLovers():
    playlist.FullList('TravelLovers')
def RainLovers():
    playlist.FullList('RainLovers')
def SeaLovers():
    playlist.FullList('SeaLovers')
def SunLovers():
    playlist.FullList('SunLovers')
