# Beispiel: __iter__ und __next__ (Folie 38)
# Eigene Iteratoren bauen - StopIteration beendet die Schleife.

class MeinIter:
    def __init__(self, limit):
        self.limit = limit
        self.i = 0

    def __iter__(self):
        """Liefert den Iterator (hier: sich selbst)."""
        return self

    def __next__(self):
        """Liefert den naechsten Wert - StopIteration am Ende."""
        if self.i >= self.limit:
            raise StopIteration
        self.i += 1
        return self.i ** 2


for x in MeinIter(3):
    print(x)   # -> 1, 4, 9
