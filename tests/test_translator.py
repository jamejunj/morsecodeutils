import unittest
from morseutils.translator import MorseCodeTranslator

class TestTranslator(unittest.TestCase):
    def test_encode(self):
        self.assertEqual(MorseCodeTranslator.encode('hello'), '.... . .-.. .-.. ---')
        self.assertEqual(MorseCodeTranslator.encode('world'), '.-- --- .-. .-.. -..')
        self.assertEqual(MorseCodeTranslator.encode('hello world'), '.... . .-.. .-.. ---   .-- --- .-. .-.. -..')
    
unittest.main()