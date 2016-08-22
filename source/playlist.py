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
import AllPlaylists, menu, home,exit, time

'''
    FullList returns a dict.
    Dictionary structure:
    ['playlist label name','playlist youtube id', ]
'''

def FullList(category):
    print 'Οι playlist που υπάρχουν προς το παρόν ;\n'
    counter = 0
    allPlaylists = AllPlaylists.GetThem()
    FinalPlaylist = {}
    for i in allPlaylists:
        if allPlaylists[i][2] == category or allPlaylists[i][3] == category or allPlaylists[i][4] == category or allPlaylists[i][5]==category or allPlaylists[i][6] == category or allPlaylists[i][7]==category or allPlaylists[i][8]==category:
            counter += 1
            FinalPlaylist[i] = [allPlaylists[i][0], allPlaylists[i][1]]
            print counter,".",FinalPlaylist[i][0]
            FinalPlaylist[counter] = FinalPlaylist.pop(i)
            time.sleep(0.02)

    print len(FinalPlaylist)+1,".",colored(" Home Menu","yellow")
    select = -1

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
