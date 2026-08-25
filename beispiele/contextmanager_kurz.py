# Beispiel: contextlib.contextmanager (Folie 45)
# Die kurze Variante - ganz ohne eigene Klasse.

from contextlib import contextmanager


@contextmanager
def temporaere_datei(name):
    print("Oeffne")
    f = open(name, "w")
    try:
        yield f                # Wert fuer den with-Block
    finally:
        print("Schliesse")
        f.close()


with temporaere_datei("t.txt") as f:
    f.write("Inhalt")
