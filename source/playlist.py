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
import AllPlaylists, menu, home,exit, time, ksena, categories, lovers, mood, twentyfour, greek, lang
from lang import curr_lang
from head import head
'''
    FullList returns a dict.
    Dictionary structure:
    ['playlist label name','playlist youtube id', ]
'''

def FullList(category, *ParentMenuFunc):
    call('clear')
    if not curr_lang():
        print head() + '''Οι playlist που υπάρχουν προς το παρόν ;\n'''
    elif curr_lang():
        print head() + '''Currenty playlists\n'''
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
        if len(str(counter))==1:
            if len(FinalPlaylist[i][0])>1 and curr_lang():
                OutputStr = " "+str(counter)+". "+FinalPlaylist[i][0][1]
            else:
                OutputStr = " "+str(counter)+". "+FinalPlaylist[i][0][0]

        else:
            if len(FinalPlaylist[i][0])>1 and curr_lang():
                OutputStr = str(counter)+". "+FinalPlaylist[i][0][1]
            else:
                OutputStr = str(counter)+". "+FinalPlaylist[i][0][0]

        print OutputStr
        time.sleep(0.03)
    if ParentMenuFunc:
        OutputStr = str(len(FinalPlaylist)+1)+". "+"Previous Menu"
        div = len(OutputStr) + 2
        print colored(OutputStr, "green")
        OutputStr1 = str(len(FinalPlaylist)+2)+". "+"Home Menu"
        div = len(OutputStr1) + 2
        print colored(OutputStr1,"yellow")
    else:
        OutputStr1 = str(len(FinalPlaylist)+1)+". "+"Home Menu"
        div = len(OutputStr1) + 2
        print colored(OutputStr1,"yellow")
    select = -1
    if not curr_lang():
        select = input("Επιλέξτε λίστα (για έξοδο δώστε 0)\n>>> ")
    elif curr_lang():
        select = input("Select playlist (for exit give 0)\n>>> ")
    if select == len(FinalPlaylist)+1:
        eval(*ParentMenuFunc)
    elif select == len(FinalPlaylist)+2:
        home.ListMenu()
    elif (select > 0 & select <len(FinalPlaylist)+1):
        Play(FinalPlaylist[select][1])
    elif select == 0:
        exit.exit()



def Play(id):

    IDwithArgus = id + ",dump,all"
    call(["mpsyt", "pl", IDwithArgus])
