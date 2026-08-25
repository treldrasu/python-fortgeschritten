# Beispiel: yield - Generatoren (Folie 37)
# yield liefert einen Wert und pausiert - der Zustand wird gemerkt.

def zaehler(n):
    i = 1
    while i <= n:
        yield i        # Wert liefern und pausieren
        i += 1


for z in zaehler(3):
    print(z)
# -> 1, 2, 3

gen = zaehler(3)
print(next(gen))   # -> 1
print(next(gen))   # -> 2
