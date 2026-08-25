# Beispiel: @staticmethod und @classmethod (Folie 34)
# Methoden ohne Objekt-Bezug.

class Rechner:
    def __init__(self, name):
        """Konstruktor: damit cls(name) in der Klassenmethode funktioniert."""
        self.name = name

    @staticmethod
    def addiere(a, b):
        """Statische Methode: kein self, kein cls - nur eine Funktion."""
        return a + b

    @classmethod
    def erzeuge(cls, name):
        """Klassenmethode: bekommt die Klasse (cls) - wichtig bei Vererbung."""
        return cls(name)


class SpezialRechner(Rechner):
    pass


print(Rechner.addiere(3, 4))       # -> 7
r = SpezialRechner.erzeuge("x")    # erzeugt SpezialRechner, nicht Rechner
print(type(r).__name__)            # -> SpezialRechner
