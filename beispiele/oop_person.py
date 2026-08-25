# Beispiel: Erste Klasse (Folie 9)
# Eine Klasse ist der Bauplan, ein Objekt das konkrete Exemplar.

class Person:
    def __init__(self, name, alter):
        """Konstruktor: wird beim Erzeugen eines Objekts aufgerufen."""
        self.name = name        # Instanzvariable: Name
        self.alter = alter      # Instanzvariable: Alter

    def vorstellen(self):
        """Methode: gibt eine Vorstellung aus."""
        print(f"Hallo, ich bin {self.name} und {self.alter} Jahre alt.")


# Objekt erzeugen und Methode aufrufen
kai = Person("Kai", 42)
kai.vorstellen()
# -> Hallo, ich bin Kai und 42 Jahre alt.
