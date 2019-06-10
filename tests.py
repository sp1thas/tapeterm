import unittest
from tapeterm.tapeterm import *


class TestTapeTerm(unittest.TestCase):

    def test_json_en_files(self):
        with open('tapeterm/config_en.json', 'r') as f:
            self.assertTrue(bool(json.load(f)))

    def test_json_el_files(self):
        with open('tapeterm/config_en.json', 'r') as f:
            self.assertTrue(bool(json.load(f)))

    def test_tapeterm_en_class_init(self):
        self.obj = TapeTerm(JSON=JSON_EN)
        self.assertTrue(isinstance(self.obj, object))
        self.assertTrue(bool(self.obj.data))
        self.assertTrue(bool(self.obj.JSON))
        self.assertTrue(bool(self.obj.mpsyt_bin))

    def test_tapeterm_el_class_init(self):
        self.obj = TapeTerm(JSON=JSON_EL)
        self.assertTrue(isinstance(self.obj, object))
        self.assertTrue(bool(self.obj.data))
        self.assertTrue(bool(self.obj.JSON))
        self.assertTrue(bool(self.obj.mpsyt_bin))


if __name__ == '__main__':
    unittest.main()