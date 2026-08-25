# Beispiel: Multiple Inheritance & MRO (Folie 16)
# MRO (Method Resolution Order) bestimmt, welche Methode gewinnt.

class Schwimmt:
    def schwimmen(self):
        print("Schwimmt...")


class Fliegt:
    def fliegen(self):
        print("Fliegt...")


class Ente(Schwimmt, Fliegt):
    pass


ente = Ente()
ente.schwimmen()   # -> Schwimmt...
ente.fliegen()     # -> Fliegt...

# MRO-Reihenfolge: Ente -> Schwimmt -> Fliegt -> object
print(Ente.mro())
