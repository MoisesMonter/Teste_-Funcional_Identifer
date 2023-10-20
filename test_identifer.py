# test_identifier.py

import pytest

from identifer import Identifier

test_cases = [ ("A", True),         ("", False),
               ("B2c4D6", True),    ("@123456789", False),
    
    
]
@pytest.mark.parametrize("input, expected", test_cases)
def test_identifier(input, expected):
    identifier = Identifier(input)
    assert identifier.has_min_size() == expected
    assert identifier.matches_regex() == expected
    assert identifier.starts_with_letter() == expected
    assert identifier.has_min_size() == expected
    assert identifier.has_max_size() == expected