# Beispiel: parametrize & Mocking (Folie 58)
# Fuehre aus:  pytest pytest_parametrize.py
# parametrize fuehrt den Test mit vielen Faellen aus.

import pytest


def addiere(a, b):
    return a + b


@pytest.mark.parametrize("a,b,erwartet", [
    (2, 3, 5), (0, 0, 0), (-1, 1, 0),
])
def test_addiere(a, b, erwartet):
    assert addiere(a, b) == erwartet
