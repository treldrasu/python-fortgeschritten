"""Einkaufsliste - Startdatei (TDD-Aufgabe).

Eure Aufgabe: Baut eine Einkaufsliste komplett per TDD.

TDD-Ablauf:
1. Schreibt ZUERST die Tests (test_einkaufsliste.py)
2. Lasst sie fehlschlagen (ROT)
3. Implementiert die Funktionen (GRUEN)
4. Raeumt auf (REFACTOR)

Anforderungen:
- Artikel hinzufuegen (Name, Preis)
- Artikel entfernen
- Liste anzeigen
- Gesamtsumme berechnen

Die Produktliste liegt in produkte.txt (Name:Preis pro Zeile).
"""
from typing import Dict, List, Tuple


def produkte_laden(dateipfad: str) -> Dict[str, float]:
    """Liest die Produktliste aus einer Datei.

    Format pro Zeile: Name:Preis
    Rueckgabe: Dict {Name: Preis}
    """
    # TODO: Implementieren
    pass


def artikel_hinzufuegen(einkaufsliste: List[Tuple[str, float]], name: str, preis: float) -> None:
    """Fuegt einen Artikel zur Einkaufsliste hinzu."""
    # TODO: Implementieren
    pass


def artikel_entfernen(einkaufsliste: List[Tuple[str, float]], name: str) -> None:
    """Entfernt einen Artikel aus der Einkaufsliste.

    Wirft ValueError, wenn der Artikel nicht existiert.
    """
    # TODO: Implementieren
    pass


def gesamtsumme(einkaufsliste: List[Tuple[str, float]]) -> float:
    """Berechnet die Gesamtsumme aller Artikel."""
    # TODO: Implementieren
    pass


def liste_anzeigen(einkaufsliste: List[Tuple[str, float]]) -> None:
    """Gibt die Einkaufsliste in der Konsole aus."""
    # TODO: Implementieren
    pass


def main() -> None:
    """Einfache CLI fuer die Einkaufsliste."""
    # TODO: Implementieren (optional)
    pass


if __name__ == "__main__":
    main()
