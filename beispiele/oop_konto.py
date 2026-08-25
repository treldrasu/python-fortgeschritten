# Beispiel: Attribute und Methoden (Folie 10)
# Attribute speichern den Zustand, Methoden das Verhalten.

class Konto:
    def __init__(self, inhaber, startguthaben=0):
        """Konstruktor: legt ein Konto mit Startguthaben an."""
        self.inhaber = inhaber
        self.guthaben = startguthaben

    def einzahlen(self, betrag):
        """Erhoeht das Guthaben um den Betrag."""
        self.guthaben += betrag

    def abheben(self, betrag):
        """Verringert das Guthaben - aber nicht unter 0."""
        if betrag > self.guthaben:
            print("Nicht genug Guthaben!")
            return
        self.guthaben -= betrag

    def info(self):
        """Gibt den Kontostand aus."""
        print(f"{self.inhaber}: {self.guthaben} EUR")


konto = Konto("Kai", 100)
konto.einzahlen(50)
konto.abheben(30)
konto.info()   # -> Kai: 120 EUR
