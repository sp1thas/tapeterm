from lib import *
import time

def test_setup():
    tl = TapeLib()
    tl.set_driver()
    return tl

def test_close(tl):
    tl.close_driver()

def test_base_url():
    tl = test_setup()
    tl.get_home()
    test_close(tl)

def test_get_ids():
    tl = test_setup()
    tl.get_plid_from_urls()
    test_close(tl)

def test_tapeterm():
    from kasetophono import TapeTerm
    ks = TapeTerm()
