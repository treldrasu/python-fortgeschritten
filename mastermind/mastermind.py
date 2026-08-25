"""Mastermind CLI - Startdatei (Bonus-Aufgabe).

Eure Aufgabe: Vervollstaendigt dieses Programm zu einem spielbaren
Mastermind. Die Struktur ist vorgegeben - ihr fuellt die Methoden aus.

Regeln:
- Der Computer denkt sich einen geheimen Code aus: 4 Zahlen aus 1-6.
- Ihr ratet: 4 Zahlen aus 1-6.
- Antwort: schwarze Pins (richtige Zahl, richtige Position) und
  weisse Pins (richtige Zahl, falsche Position).
- Gewonnen, wenn ihr 4 schwarze Pins habt.

TIPP: Schreibt zuerst Tests fuer die Vergleichs-Logik (test_mastermind.py),
dann implementiert ihr die Methode vergleichen().
"""
import random
from typing import List, Tuple


class Code:
    """Ein Code aus 4 Zahlen (1-6)."""

    def __init__(self, zahlen: List[int]) -> None:
        self.zahlen = zahlen

    def __str__(self) -> str:
        """Gibt den Code als lesbaren String aus, z.B. '1 3 5 2'."""
        return " ".join(str(z) for z in self.zahlen)

    def __eq__(self, other: object) -> bool:
        """Zwei Codes sind gleich, wenn alle Zahlen uebereinstimmen."""
        if not isinstance(other, Code):
            return NotImplemented
        return self.zahlen == other.zahlen

    def __len__(self) -> int:
        """Laenge des Codes (immer 4)."""
        return len(self.zahlen)


class Spiel:
    """Das Mastermind-Spiel: verwaltet den geheimen Code und die Versuche."""

    def __init__(self, geheim: Code) -> None:
        self.geheim = geheim
        self.versuche: List[Tuple[Code, int, int]] = []

    def vergleichen(self, tipp: Code) -> Tuple[int, int]:
        """Vergleicht den Tipp mit dem geheimen Code.

        Rueckgabe: (schwarze_pins, weisse_pins)
        - schwarz: richtige Zahl an richtiger Position
        - weiss:   richtige Zahl an falscher Position
        """
        # TODO: Implementieren
        pass

    def ist_gewonnen(self, tipp: Code) -> bool:
        """True, wenn der Tipp dem geheimen Code entspricht."""
        return tipp == self.geheim


def zufalls_code() -> Code:
    """Erzeugt einen zufaelligen geheimen Code aus 4 Zahlen (1-6)."""
    return Code([random.randint(1, 6) for _ in range(4)])


def eingabe_lesen() -> Code:
    """Liest eine Eingabe von 4 Zahlen (1-6) vom Benutzer.

    Beispiel: '1 3 5 2' -> Code([1, 3, 5, 2])
    """
    # TODO: Implementieren (mit try/except fuer ungueltige Eingaben)
    pass


def main() -> None:
    """Hauptschleife des Spiels."""
    spiel = Spiel(zufalls_code())
    print("Willkommen bei Mastermind!")
    print("Rate den Code: 4 Zahlen aus 1-6, getrennt durch Leerzeichen.")
    print("Beispiel: 1 3 5 2")

    while True:
        tipp = eingabe_lesen()
        schwarz, weiss = spiel.vergleichen(tipp)
        print(f"Schwarz: {schwarz}  Weiss: {weiss}")

        if spiel.ist_gewonnen(tipp):
            print(f"Gewonnen! Der Code war: {spiel.geheim}")
            break


if __name__ == "__main__":
    main()
