# Beispiel: __enter__ und __exit__ (Folie 44)
# Was with wirklich macht - Ressourcen werden immer freigegeben.

class Datei:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        """Wird beim Eintritt in den with-Block ausgefuehrt."""
        print("Oeffne Datei")
        self.f = open(self.name, "w")
        return self.f

    def __exit__(self, typ, wert, traceback):
        """Wird beim Verlassen ausgefuehrt - auch bei Fehlern."""
        print("Schliesse Datei")
        self.f.close()
        return False   # Fehler nicht verschlucken


with Datei("test.txt") as f:
    f.write("Hallo")
