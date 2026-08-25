# Beispiel: itertools - Overview (Folie 39)
# Vorgefertigte, effiziente Iteratoren - immer mit islice begrenzen!

from itertools import count, cycle, repeat, islice

for z in islice(count(10), 5):            # 10, 11, 12, 13, 14
    print(z)

for f in islice(cycle(["A", "B"]), 4):     # A, B, A, B
    print(f)

for w in islice(repeat("x", 3), 3):       # x, x, x
    print(w)
