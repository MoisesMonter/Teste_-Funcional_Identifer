from src.identifier.fake import Identifier
import pytest

Avaliable =True

test_string = [ ("A", Avaliable),         (123,  not Avaliable),
               (str(123), Avaliable),      (2.4,   not Avaliable),] #testar strings

test_first_str = [("a",Avaliable), ("@", not Avaliable),
                  ("B1nn",Avaliable),(str(55.5), not Avaliable)] #primeiro string

test_min_max =[ ("A", Avaliable),       ("", not Avaliable),
                ("H3LLO",Avaliable),    ("W0rlds!",  not Avaliable)]# testar Min Max

@pytest.mark.parametrize("input, expected", test_min_max)
def test_identifier_Min_Size(input, expected):
    identifier = Identifier(input)
    assert identifier.has_min_size() == expected

@pytest.mark.parametrize("input,expected", test_min_max)
def test_identifier_max_size(input, expected):
    identifier = Identifier(input)
    assert identifier.has_max_size() == expected

@pytest.mark.parametrize("input,expected",test_string)
def test_identifier_str(input,expected):
    identifier = Identifier(input)
    assert identifier.is_string() == expected

@pytest.mark.parametrize("input,excpeted",test_first_str)
def test_identifier_first_str(input,excpeted):
    id = Identifier(input)
    assert id.first_str() == excpeted