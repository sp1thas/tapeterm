import unittest
import json

class TestTapeTerm(unittest.TestCase):
    def test_json_en_files(self):
        with open('tapeterm/config_en.json', 'r') as f:
            self.assertTrue(bool(json.load(f)))

if __name__ == '__main__':
    unittest.main()