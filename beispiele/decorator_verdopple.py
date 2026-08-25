# Beispiel: @decorator (Folie 32)
# Eine Funktion veraendern, ohne sie anzufassen.

def verdopple(funktion):
    def wrapper(*args, **kwargs):
        ergebnis = funktion(*args, **kwargs)
        return ergebnis * 2
    return wrapper


@verdopple
def quadrat(x):
    return x ** 2


print(quadrat(3))   # -> 18 (nicht 9!)

# @verdopple ist Kurzschreibweise fuer: quadrat = verdopple(quadrat)
