import pytest
from condicionales import edad_futura

def test_edad_futura():
    assert edad_futura(10,2010) == 70

@pytest.mark.parametrize(
    "imput_a, imput_b, expected",
    [
        (10,2010,7),
        (20,2020,70),
        (edad_futura(10,2010),2070,70)
        ]
    )
def test_edad_futura_multi(imput_a, imput_b, expected):
    assert edad_futura(imput_a, imput_b) == expected
