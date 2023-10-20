# identifier.py

import re

class Identifier:

    def __init__(self, info):
        self.x = info

    def is_string(self):
        return isinstance(self.x, str)

    def matches_regex(self):
        return re.search("^[a-zA-Z0-9]+$", self.x) is not None

    def starts_with_letter(self):
        return self.x[0].isalpha()

    def has_min_size(self):
        return len(self.x) >= 1

    def has_max_size(self):
        return len(self.x) < 6
