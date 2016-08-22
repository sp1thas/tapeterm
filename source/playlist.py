# -*- coding: utf-8 -*-
#   ===================================
#               playlist
#   ===================================
__author__ = "Simakis Panagiotis"
__license__ = "GPL"
__email__ = "sp1thas@autistici.org"
#   ===================================

from termcolor import colored
from subprocess import call
import AllPlaylists, menu, home,exit

'''
    FullList returns a dict.
    Dictionary structure:
    ['playlist label name','playlist youtube id', ]
'''

def FullList(category):
    allPlaylists = AllPlaylists.GetThem()
    FinalPlaylist = {}
    for i in allPlaylists:
        if allPlaylists[i][2] == category or allPlaylists[i][3] == category:
            FinalPlaylist[i] = [allPlaylists[i][0], allPlaylists[i][1]]


    print 'Οι playlist που υπάρχουν προς το παρόν ;\n'
    counter = 0
    for i in FinalPlaylist:
        counter += 1
        FinalPlaylist[counter] = FinalPlaylist.pop(i)

    for i in FinalPlaylist:
        print i,". ",FinalPlaylist[i][0]
    print len(FinalPlaylist)+1,colored(".  Home Menu","yellow")
    select = 0

    select = input("Επιλέξτε λίστα (για έξοδο δώστε 0)\n>>> ")
    if select == len(FinalPlaylist)+1:
        home.ListMenu()
    elif (select > 0 & select <len(FinalPlaylist)+1):
        Play(FinalPlaylist[select][1])
    elif select == 0:
        exit.exit()



def Play(id):

    IDwithArgus = id + ",dump,all"
    call(["mpsyt", "pl", IDwithArgus])
