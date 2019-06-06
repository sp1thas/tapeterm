#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
#   ===================================
#        Kasetophono sto termatiko
#   ===================================
__author__ = "Simakis Panagiotis"
__license__ = "GPL"
__email__ = "sp1thas@autistici.org"
#   ===================================

import json, sys
from .config import *
from pyclimenu.menu import Menu
import dpath
import subprocess
import traceback
from .misc import header

class TapeTerm(object):
    """
    Tapeterm main class
    """
    def __init__(self, JSON=None):
        """
        Tape term constructor
        """
        # self.tl = TapeLib()
        self.JSON = JSON
        self.data = self.read_json()
        pr = subprocess.Popen(
            ['which', 'mpsyt'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        self.mpsyt_bin = pr.communicate()[0].strip()
        assert self.mpsyt_bin, 'mpsyt binary not found'
        self.main()

    def main(self):
        self.disp_menu()


    def disp_menu(self, label=''):
        """
        This method with manipulate the options on the terminal
        :param label: dictionary path
        :return: nada
        """
        mn = Menu()
        # mps_youtube.screen.update()
        results = dpath.util.get(self.data, label) if label else self.data.copy()
        items = {}
        if isinstance(results, dict):
            for k,v in results.items():
                if len(k)<2:
                    continue
                if isinstance(v, str) and len(v) == 34:
                    items[k] = {
                        'label': '[PL] '+k.capitalize(),
                        'callback': self.play,
                        'args': (v, label)
                    }
                else:
                    items[k] = {
                        'label': '[  ] '+k.capitalize(),
                        'callback': self.disp_menu,
                        'kwargs': {'label': label+'/'+k}
                    }
        for k in sorted(items.keys()):
            item = items[k]
            mn.add_item(**item)
        if label != '':
            mn.add_item(label='     Parent Category', callback=self.disp_menu, args=('/'.join(label.split('/')[:-1]),))
        mn.add_item(label='     Exit', callback=sys.exit)
        mn.set_colors(num_fg='purple', num_bld=False, label_fg='red', label_bld=True)
        mn.run(header=header())

    def play(self, playlist_id, label):
        """
        Play selected playlist
        :param playlist_id: youtube playlist id
        :param label: dictionary path
        :return:
        """
        try:
            subprocess.call([self.mpsyt_bin, 'pl', playlist_id+',dump,all'])
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print('There has been a error:')
            traceback.print_exc()
        finally:
            self.disp_menu(label)

    def read_json(self):
        """
        Read Config JSON FILE
        :return:
        """
        assert os.path.exists(self.JSON)
        with open(self.JSON, 'r') as f:
            return json.load(f)

def check_config_files():
    import shutil
    print(os.listdir())
    if not os.path.exists(JSON_EN):
        shutil.copy(
            os.path.join('./', os.path.basename(JSON_EN)),
            os.path.join(CONFIG_FOLDER, os.path.basename(JSON_EN))
        )
    if not os.path.exists(JSON_EL):
        shutil.copy(
            os.path.join('.', os.path.basename(JSON_EL)),
            os.path.join(CONFIG_FOLDER, os.path.basename(JSON_EL))
        )

def arg_parsing():
    import argparse
    parser = argparse.ArgumentParser(description='tapeterm: listen your favorite playlist from your terminal')
    # parser.add_argument("--upd", help="Update the list of playlists", action="store_true")
    parser.add_argument("--en", help="English version", action="store_true")
    parser.add_argument("--el", help="Greek version", action="store_true")
    return parser.parse_args()


def main():
    args = arg_parsing()
    # if args.upd:
    #     from .crawler import TapeLib
    #     'Will update: EN: {} EL: {}'.format(int(args.en), int(args.el))
    #     a = TapeLib(lang='el' if args.el else 'en')
    #     a.set_up()
    #     a.get_home()
    if args.en:
        JSON = JSON_EN[:]
    else:
        JSON = JSON_EL[:]

    TapeTerm(JSON=JSON)
