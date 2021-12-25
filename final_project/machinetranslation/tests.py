import unittest

from translator import french_to_english, english_to_french

class TestMyModule(unittest.TestCase):
    def test_french_to_english(self):
        self.assertEqual(french_to_english("Bonjour"),"Hello")
        self.assertNotEqual(french_to_english("Bonjour"),"What's up")

    def test_english_to_french(self):
        pass
        self.assertEqual(english_to_french("Hello"),"Bonjour")
        self.assertNotEqual(english_to_french("Hello"),"Hola")

if __name__ == '__main__':
    unittest.main()
