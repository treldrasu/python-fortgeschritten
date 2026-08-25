# Beispiel: pytest Grundlagen (Folie 56)
# Fuehre aus:  pytest pytest_grundlagen.py
# Tests sind einfache Funktionen mit assert.

def addiere(a, b):
    return a + b


def test_addiere():
    assert addiere(2, 3) == 5


def test_addiere_negativ():
    assert addiere(-1, 1) == 0
