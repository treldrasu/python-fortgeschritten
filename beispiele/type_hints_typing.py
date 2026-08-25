# Beispiel: typing-Modul (Folie 51)
# Komplexere Typen: Optional, List, Dict, Any, Callable.

from typing import Optional, List, Dict, Any, Callable


def verarbeite(zahlen: List[int]) -> Dict[str, int]:
    return {"summe": sum(zahlen)}


def finde(name: Optional[str] = None) -> str:
    return name or "Unbekannt"


def anwenden(f: Callable[[int], int], wert: int) -> int:
    return f(wert)


def egal(x: Any) -> Any:
    return x


print(verarbeite([1, 2, 3]))   # -> {'summe': 6}
print(finde())                 # -> Unbekannt
print(anwenden(lambda x: x * 2, 5))   # -> 10
