# Beispiel: __str__ und __repr__ (Folie 21)
# __str__ fuer Anwender, __repr__ fuer Entwickler (nachbaubar).

class Person:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

    def __str__(self):
        """Wird bei print() aufgerufen - lesbare Ausgabe."""
        return f"{self.name} ({self.alter})"

    def __repr__(self):
        """Wird im Interpreter aufgerufen - idealerweise nachbaubar."""
        return f"Person('{self.name}', {self.alter})"


p = Person("Kai", 42)
print(p)     # -> Kai (42)          (__str__)
print(repr(p))  # -> Person('Kai', 42) (__repr__)
