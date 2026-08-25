# Beispiel: super() und Method Overriding (Folie 15)
# super() ruft die Methode der Basisklasse auf - so vermeidet man Doppelung.

class Tier:
    def __init__(self, name):
        self.name = name

    def laut(self):
        """Standard-Laut der Basisklasse."""
        return "..."


class Hund(Tier):
    def __init__(self, name, alter):
        super().__init__(name)   # Basis-Konstruktor aufrufen (setzt name)
        self.alter = alter

    def laut(self):              # Method Overriding: gleiche Signatur, andere Logik
        return "Wuff!"


class Katze(Tier):
    def laut(self):
        return "Miau!"


bello = Hund("Bello", 3)
print(bello.name, bello.alter)   # -> Bello 3
print(bello.laut())              # -> Wuff!
print(Katze("Minka").laut())     # -> Miau!
