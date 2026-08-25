# Beispiel: @property (Folie 33)
# Attribute mit Logik und Schutz - nach aussen wie ein normales Attribut.

class Temperatur:
    def __init__(self, celsius):
        self._celsius = celsius   # Unterstrich: internes Attribut

    @property
    def fahrenheit(self):
        """Berechnete Eigenschaft - nur lesbar, kein Setter."""
        return self._celsius * 9 / 5 + 32

    @property
    def celsius(self):
        """Getter: liest den Wert."""
        return self._celsius

    @celsius.setter
    def celsius(self, wert):
        """Setter: validiert den Wert vor dem Speichern."""
        if wert < -273.15:
            raise ValueError("Unter dem absoluten Nullpunkt!")
        self._celsius = wert


t = Temperatur(20)
print(t.fahrenheit)   # -> 68.0
t.celsius = 30        # Setter validiert
print(t.celsius)      # -> 30
