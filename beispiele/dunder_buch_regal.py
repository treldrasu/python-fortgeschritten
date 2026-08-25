# Beispiel: __eq__, __len__, __getitem__ (Folie 22)
# So verhalten sich eigene Klassen wie eingebaute Typen.

class Buch:
    def __init__(self, titel, seiten):
        self.titel = titel
        self.seiten = seiten

    def __eq__(self, other):
        """Vergleich: gleicher Titel = gleiches Buch."""
        if not isinstance(other, Buch):
            return NotImplemented   # kein Buch -> nicht vergleichbar
        return self.titel == other.titel

    def __len__(self):
        """len() liefert die Seitenzahl."""
        return self.seiten


class Regal:
    def __init__(self):
        self.buecher = []

    def __getitem__(self, i):
        """Macht das Regal indexierbar: regal[0]."""
        return self.buecher[i]

    def __len__(self):
        return len(self.buecher)


b1 = Buch("Der Hobbit", 310)
b2 = Buch("Der Hobbit", 310)
print(b1 == b2)   # -> True (gleicher Titel)
print(len(b1))    # -> 310

regal = Regal()
regal.buecher = [b1, b2]
print(regal[0].titel)   # -> Der Hobbit
print(len(regal))       # -> 2
