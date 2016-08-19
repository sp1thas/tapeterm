# -*- coding: utf-8 -*-
from subprocess import call
from lib import playlist, start

start.logo()


fulllist = playlist.FullList()
counter = 0
print '========================== Playlists ===========================\n'
for i in fulllist:
    counter +=1
    print fulllist[i][0],"  >>  ", i
    
input = input("Επιλέξτε playlist: ")
IDwithArgus = fulllist[input][1] + ",dump,all"
call(["mpsyt", "pl", IDwithArgus])

