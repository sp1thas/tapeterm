# -*- coding: utf-8 -*-
import menu, playlist

def Menu():
    title = 'Διαθεση'
    MoodMenu = menu.Menu(title)
    options =   [
                    {"name":"Χαρούμενες","function":xaroumenes},
                    #{"name":"Χαλαρωτικές","function":xalarwtikes}
                    #{"name":"Μελαγχολικές","function":melagxolikes},
                    {"name":"Διάβασμα","function":reading},
                    #{"name":"Sexy","function":sexy},
                    #{"name":"Ερωτικές","function":erotic},
                    #{"name":"Party","function":party}
                ]
    MoodMenu.addOptions(options)
    MoodMenu.open()


def xaroumenes():
    playlist.FullList('Xaroumenes')

def xalarwtikes():
    pass

def melagxolikes():
    pass

def reading():
    playlist.FullList('Reading')

def sexy():
    pass

def erotic():
    pass
def party():
    pass
