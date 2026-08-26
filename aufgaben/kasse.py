"""Registrierkasse - Startdatei (Grosse Aufgabe).

Schritt 1 - Kasse:
- Artikel aus produkte.txt laden (Dict)
- Artikel erfassen (Name, Menge)
- Summe berechnen
- Eigene Exceptions: ArtikelNichtGefunden, UngueltigerBetrag

Schritt 2 - Registrierkasse:
- Bon als Textdatei drucken (Kassenbonpflicht!)
- Verkaeufe loggen (logging)
- Tests mit pytest.raises, parametrize, fixtures
"""
import logging
from typing import Dict, List, Tuple

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class KassenFehler(Exception):
    """Basisklasse fuer alle Kassen-Fehler."""
    pass


class ArtikelNichtGefunden(KassenFehler):
    """Wird geworfen, wenn ein Artikel nicht in der Produktliste ist."""
    pass


class UngueltigerBetrag(KassenFehler):
    """Wird geworfen, wenn ein Betrag ungueltig ist (z.B. negativ)."""
    pass


def produkte_laden(dateipfad: str) -> Dict[str, float]:
    """Liest die Produktliste aus einer Datei.

    Format pro Zeile: Name:Preis
    Rueckgabe: Dict {Name: Preis}
    """
    # TODO: Implementieren
    pass


def artikel_hinzufuegen(warenkorb: List[Tuple[str, int]], name: str, menge: int) -> None:
    """Fuegt einen Artikel zum Warenkorb hinzu.

    Wirft ArtikelNichtGefunden, wenn der Artikel nicht existiert.
    Wirft UngueltigerBetrag, wenn die Menge <= 0 ist.
    """
    # TODO: Implementieren
    pass


def summe_berechnen(warenkorb: List[Tuple[str, int]], produkte: Dict[str, float]) -> float:
    """Berechnet die Gesamtsumme des Warenkorbs."""
    # TODO: Implementieren
    pass


def bon_drucken(warenkorb: List[Tuple[str, int]], produkte: Dict[str, float], dateipfad: str) -> None:
    """Druckt den Bon als Textdatei (Kassenbonpflicht!).

    Format:
    ================================
    KASSE - SOBEK INNOVATIONS
    ================================
    Apfel x2          1.00 EUR
    Brot x1           2.50 EUR
    --------------------------------
    SUMME             3.50 EUR
    ================================
    """
    # TODO: Implementieren
    pass


def main() -> None:
    """Einfache CLI fuer die Registrierkasse."""
    # TODO: Implementieren (optional)
    pass


if __name__ == "__main__":
    main()
