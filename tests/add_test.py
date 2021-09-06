import unittest

from logic.add import DollarAdder


class DollarAdderTest(unittest.TestCase):
    Adder = DollarAdder()

    def test_adds_dollar_amounts_from_string_input(self):
        dollar_string: str = """Here are some numbers I want to add up:
                                $1\n $5.00, $20\n, 2"""
        expected_result: float = 26.00
        actual_result = self.Adder.get_dollar_amts(dollar_string)
    
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
