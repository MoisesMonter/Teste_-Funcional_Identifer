from src.identifier.fake import Identifier
import pytest
Avaliable =True

test_numb_str = [ ("Hello123",Avaliable),("Hell*123",not Avaliable),
                  (321,Avaliable),("@rroba", not Avaliable)]

@pytest.mark.parametrize("input,expected", test_numb_str)
def test_only_numbers_str(input,expected):
    id = Identifier(input)
    assert id.matches_regex == expected