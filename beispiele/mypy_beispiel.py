# Beispiel: mypy - Statische Pruefung (Folie 52)
# Fuehre aus:  mypy mypy_beispiel.py
# mypy findet den Fehler, bevor das Programm laeuft.

def addiere(a: int, b: int) -> int:
    return a + b


ergebnis = addiere("a", 5)   # mypy: error - Argument 1 ist str, erwartet int
print(ergebnis)
