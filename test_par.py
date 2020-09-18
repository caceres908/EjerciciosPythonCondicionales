import pytest
from espar import es_par

def test_par():
    assert es_par(10) == True

@pytest.mark.parametrize(
    "imput_a, expected",
    [
        (2,True),
        (3,False),
        (5,False),
        (-10, True)
        ]
    )
def test_par_multi(imput_a, expected):
    assert es_par(imput_a) == expected
