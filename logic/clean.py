from typing import List

import re


class RegexCleaner:
    filter = re.compile(r'\$\d+(?:\.\d+)?')

    def clean(self, raw_input: str) -> List[float]:
        raw_input = raw_input.replace(" ", "")
        dollars_string: List = [amt.strip("$") for amt in self.filter.findall(raw_input)]
        dollars_floats = [float(amt) for amt in dollars_string]

        return dollars_floats
