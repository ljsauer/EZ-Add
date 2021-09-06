import unittest

from logic.clean import RegexCleaner


class RegexCleanerTests(unittest.TestCase):
    cleaner = RegexCleaner()

    def test_parses_dollar_amounts_from_string(self):
        starting_string = "Amount: $4.00"
        cleaned_output = self.cleaner.clean(starting_string)

        self.assertTrue(cleaned_output == [4.0])


if __name__ == '__main__':
    unittest.main()
