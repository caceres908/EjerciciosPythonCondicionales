import pytest
from palabra import palabras

def test_palabras():
    assert palabras("Jose") == ("J","e")

@pytest.mark.parametrize(
    "imput_a, expected",
    [
       ("Jose",("J","e")),
       ("Maria",("M","a")),
       ("af",("a","f")),
       ("12-45",("1","5"))
        ]
    )
def test_palabras_multi(imput_a, expected):
    assert palabras(imput_a) == expected
