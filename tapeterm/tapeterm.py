#!/usr/bin/env python
from __future__ import unicode_literals, absolute_import
import json
import sys
import argparse
from tapeterm.config import *
from pyclimenu.menu import Menu
import dpath.util
import subprocess
import traceback
from tapeterm.misc import header


class TapeTerm(object):
    """
    Tapeterm main class

    :param json_file: json file path
    :type json_file: str
    :param api_key: youtube API key
    :type api_key: str
    :param player: audio player bin
    :type player: str
    """
    def __init__(self, json_file=None, api_key=None, player=None):
        """
        Tape term constructor
        """
        # self.tl = TapeLib()
        self.JSON = json_file
        self.data = self.read_json()
        pr = subprocess.Popen(
            ['which', 'mpsyt'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        if not api_key:
            raise ValueError('API Key is not provided')
        self.mpsyt_bin = pr.communicate()[0].strip()

        p = subprocess.Popen(
            ['rm', '~/.config/mps-youtube/cache_py*', '||', 'mpsyt'],
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE
        )
        o, e = p.communicate(
            input='set api_key {}\nset show_video false\nset player {}\nexit\n'.format(api_key, player).encode()
        )

        if not self.mpsyt_bin:
            raise OSError('mpsyt binary not found')

    def disp_menu(self, label=''):
        """
        This method with manipulate the options on the terminal
        :param label: dictionary path
        :return: nada
        """
        mn = Menu()
        results = dpath.util.get(self.data, label) if label else self.data.copy()
        items = {}
        if isinstance(results, dict):
            for k,v in results.items():
                if len(k)<2:
                    continue
                if isinstance(v, str) and len(v) == 34:
                    items[k] = {
                        'label': '[PL] '+k.capitalize(),
                        'clb': self.play,
                        'args': (v, label)
                    }
                else:
                    items[k] = {
                        'label': '[  ] '+k.capitalize(),
                        'clb': self.disp_menu,
                        'kwargs': {'label': label+'/'+k}
                    }
        for k in sorted(items.keys()):
            item = items[k]
            mn.add_item(**item)
        if label != '':
            mn.add_item(label='     Parent Category', clb=self.disp_menu, args=('/'.join(label.split('/')[:-1]),))
        mn.add_item(label='     Exit', clb=sys.exit)
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
        except Exception:
            print('There has been a error:')
            traceback.print_exc()
        finally:
            self.disp_menu(label)

    def read_json(self):
        """
        Read Config JSON FILE
        :return:
        """
        if not os.path.exists(self.JSON):
            raise OSError('JSON file not found')
        with open(self.JSON, 'r') as f:
            return json.load(f)


def arg_parsing():
    parser = argparse.ArgumentParser(description='tapeterm: listen your favorite playlist from your terminal')
    parser.add_argument("--language", help="Select language", choices=['en', 'el'], default='en')
    parser.add_argument("--youtube-api-key", help="Provide your youtube API Key", required=True)
    parser.add_argument("--player", help="Specify player (must be installed)", default='cvlc')
    return parser.parse_args()
