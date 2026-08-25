# Beispiel: Exception-Hierarchien (Folie 62)
# Eigene Fehler sauber strukturieren - spezifisch VOR allgemein abfangen.

class AppFehler(Exception):
    pass


class UngueltigeEingabe(AppFehler):
    pass


class BenutzerNichtGefunden(AppFehler):
    pass


def lade_benutzer(name):
    if name != "kai":
        raise BenutzerNichtGefunden(name)
    return "Benutzer geladen"


try:
    lade_benutzer("unbekannt")
except BenutzerNichtGefunden:
    print("Spezifisch abgefangen")
except AppFehler:
    print("Allgemein abgefangen")
