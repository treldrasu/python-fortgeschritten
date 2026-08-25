# Beispiel: Generator Expressions (Folie 25)
# Runde Klammern statt eckiger - Lazy Evaluation (sparsam im Speicher).

quadrate = [x ** 2 for x in range(1000000)]   # Liste - viel Speicher
gen = (x ** 2 for x in range(1000000))        # Generator - sparsam

print(type(gen))   # <class 'generator'>

# Der Generator liefert nur so viele Werte wie noetig
for wert in gen:
    if wert > 100:
        break
    print(wert)
