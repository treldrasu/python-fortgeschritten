# Beispiel: Closures (Folie 30)
# Eine Funktion, die eine Funktion zurueckgibt - und sich Variablen merkt.

def aussenhaus(x):
    def innenhaus(y):
        return x + y
    return innenhaus


addiere_5 = aussenhaus(5)
print(addiere_5(10))   # -> 15

# innenhaus 'erinnert' sich an x=5, auch nachdem aussenhaus fertig ist.
