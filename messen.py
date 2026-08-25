import timeit

code_schleife = """
quadrate = []
for x in range(1000):
    quadrate.append(x ** 2)
"""

code_comp = "quadrate = [x ** 2 for x in range(1000)]"

t1 = timeit.timeit(code_schleife, number=10000)
t2 = timeit.timeit(code_comp, number=10000)
print(f"Schleife: {t1:.3f}s  Comprehension: {t2:.3f}s")
