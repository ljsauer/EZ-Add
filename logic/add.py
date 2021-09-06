from typing import List
from clean import RegexCleaner


class DollarAdder(object):
    def __init__(self):
        self.cleaner = RegexCleaner()

    def get_dollar_amts(self, raw_input: str) -> float:
        cleaned_output: List[float] = self.cleaner.clean(raw_input)
        total = 0.0
        for amt in cleaned_output:
            total += amt
        return total
