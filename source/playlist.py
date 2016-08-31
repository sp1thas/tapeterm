# -*- coding: utf-8 -*-
#   ===================================
#       kasetophon sto termatiko
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
    FinalPlaylist = AllPlaylists.GetThem(category)

    # for i in allPlaylists:
    #     if allPlaylists[i][2] == category or allPlaylists[i][3] == category or allPlaylists[i][4] == category or allPlaylists[i][5]==category or allPlaylists[i][6] == category or allPlaylists[i][7]==category or allPlaylists[i][8]==category:
    #         counter += 1
    #         FinalPlaylist[i] = [allPlaylists[i][0], allPlaylists[i][1]]
    #         print counter,".",FinalPlaylist[i][0]
    #         FinalPlaylist[counter] = FinalPlaylist.pop(i)
    #         time.sleep(0.02)

    for i in FinalPlaylist:
        counter += 1
        if counter % 2 == 0:
            OutputStr = str(counter)+". "+FinalPlaylist[i][0]
            print colored(OutputStr, "magenta")
            time.sleep(0.1)
        else:
            OutputStr = str(counter)+". "+FinalPlaylist[i][0]
            print OutputStr
            time.sleep(0.1)
    OutputStr = str(len(FinalPlaylist)+1)+". "+"Home Menu"
    print colored(OutputStr,"yellow")
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
