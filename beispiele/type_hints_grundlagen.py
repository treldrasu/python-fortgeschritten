# Beispiel: Type Hints - Grundlagen (Folie 50)
# Signaturen dokumentieren - mypy prueft sie statisch.

def addiere(a: int, b: int) -> int:
    return a + b


name: str = "Kai"
alter: int = 42


def begruesse(name: str) -> str:
    return f"Hallo {name}!"


print(addiere(3, 4))        # -> 7
print(begruesse("Kai"))      # -> Hallo Kai!
