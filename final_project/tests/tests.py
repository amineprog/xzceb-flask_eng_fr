import unittest
from machinetranslation.translator import english_to_french, french_to_english

class TranslatorTests(unittest.TestCase):

    def test_english_to_french_translation(self):
        # Test translation of 'Hello' to French
        input_text = 'Hello'
        result = english_to_french(input_text)
        self.assertEqual(result, 'Bonjour', "Expected translation of 'Hello' to 'Bonjour'")

    def test_french_to_english_translation(self):
        # Test translation of 'Bonjour' to English
        input_text = 'Bonjour'
        result = french_to_english(input_text)
        self.assertEqual(result, 'Hello', "Expected translation of 'Bonjour' to 'Hello'")

    def test_english_to_french_null_input(self):
        # Test for null input in english_to_french
        input_text = None
        with self.assertRaises(ValueError):
            english_to_french(input_text)

    def test_french_to_english_null_input(self):
        # Test for null input in french_to_english
        input_text = None
        with self.assertRaises(ValueError):
            french_to_english(input_text)

    def test_english_to_french_empty_input(self):
        # Test for empty input in english_to_french
        input_text = ''
        with self.assertRaises(ValueError):
            english_to_french(input_text)

    def test_french_to_english_empty_input(self):
        # Test for empty input in french_to_english
        input_text = ''
        with self.assertRaises(ValueError):
            french_to_english(input_text)

if __name__ == '__main__':
    unittest.main()
