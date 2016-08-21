# -*- coding: utf-8 -*-
from subprocess import call
import AllPlaylists, menu, home

'''
    FullList returns a dict.
    Dictionary structure:
    ['playlist label name','playlist youtube id', ]
'''

def FullList(category):
    allPlaylists = AllPlaylists.GetThem()
    FinalPlaylist = {}
    for i in allPlaylists:
        if allPlaylists[i][2] == category:
            FinalPlaylist[i] = [allPlaylists[i][0], allPlaylists[i][1]]


    print 'Οι playlist που υπάρχουν προς το παρόν ;\n'
    counter = 0
    for i in FinalPlaylist:
        counter += 1
        FinalPlaylist[counter] = FinalPlaylist.pop(i)

    print len(FinalPlaylist)
    for i in FinalPlaylist:
        print i,". ",FinalPlaylist[i][0]
    print len(FinalPlaylist)+1,".  Home Menu"
    select = 0

    select = input("Επιλέξτε λίστα\n>>> ")
    if select == len(FinalPlaylist)+1:
        home.Menu()
    elif (select > 0 & select <len(FinalPlaylist)+1):
        Play(FinalPlaylist[select][1])



def Play(id):

    IDwithArgus = id + ",dump,all"
    call(["mpsyt", "pl", IDwithArgus])