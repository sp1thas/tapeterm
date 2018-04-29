#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#   ===================================
#        Kasetophono sto termatiko
#   ===================================
__author__ = "Simakis Panagiotis"
__license__ = "GPL"
__email__ = "sp1thas@autistici.org"
#   ===================================
import os, json
HOME = os.environ['HOME']
CONFIG_FOLDER = os.path.join(HOME, '.tapeterm')
JSON = os.path.join(CONFIG_FOLDER, 'config.json')

from lib import TapeLib
from pyclimenu import Menu

class TapeTerm(object):
    def __init__(self):
        self.tl = TapeLib()
        self.data = self.read_json()
        self.mn = Menu()
        self.main()

    def main(self):
        items = ()
        for k in self.data.keys():
            items += (
                {
                    'label': k,
                    'callback': self.sub_menu,
                    'params': {'menu': k}
                }
            ,)
        print items
        # self.mn.display(header='TapeTerm')

    def sub_menu(self, menu=None):
        assert isinstance(menu, basestring), 'menu must be string'
        print 'sdsd'


    def read_json(self):
        """
        Read Config JSON FILE
        :param filepath:
        :return:
        """
        assert os.path.exists(JSON)
        with open(JSON, 'r') as f:
            return json.load(f)

