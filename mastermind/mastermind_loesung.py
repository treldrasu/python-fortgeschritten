"""Mastermind CLI - Loesung (Bonus-Aufgabe).

Regeln:
- Der Computer denkt sich einen geheimen Code aus: 4 Zahlen aus 1-6.
- Ihr ratet: 4 Zahlen aus 1-6.
- Antwort: schwarze Pins (richtige Zahl, richtige Position) und
  weisse Pins (richtige Zahl, falsche Position).
- Gewonnen, wenn ihr 4 schwarze Pins habt.
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

        Vorgehen:
        1. Zuerst die schwarzen Pins zaehlen (Position exakt).
        2. Dann die weissen Pins: gemeinsame Zahlen minus schwarze.
           Dafuer zaehlen wir, wie oft jede Zahl (1-6) in beiden
           Codes vorkommt und nehmen jeweils das Minimum.
        """
        schwarz = 0
        for i in range(len(self.geheim)):
            if tipp.zahlen[i] == self.geheim.zahlen[i]:
                schwarz += 1

        # Gemeinsame Zahlen (unabhaengig von der Position) zaehlen
        gemeinsam = 0
        for zahl in range(1, 7):
            im_geheim = self.geheim.zahlen.count(zahl)
            im_tipp = tipp.zahlen.count(zahl)
            gemeinsam += min(im_geheim, im_tipp)

        # Weisse Pins = gemeinsame Zahlen minus die schwarzen
        weiss = gemeinsam - schwarz

        self.versuche.append((tipp, schwarz, weiss))
        return schwarz, weiss

    def ist_gewonnen(self, tipp: Code) -> bool:
        """True, wenn der Tipp dem geheimen Code entspricht."""
        return tipp == self.geheim


def zufalls_code() -> Code:
    """Erzeugt einen zufaelligen geheimen Code aus 4 Zahlen (1-6)."""
    return Code([random.randint(1, 6) for _ in range(4)])


def eingabe_lesen() -> Code:
    """Liest eine Eingabe von 4 Zahlen (1-6) vom Benutzer.

    Beispiel: '1 3 5 2' -> Code([1, 3, 5, 2])
    Wirft ValueError bei ungueltiger Eingabe.
    """
    while True:
        try:
            eingabe = input("Dein Tipp (4 Zahlen 1-6, getrennt durch Leerzeichen): ")
            zahlen = [int(x) for x in eingabe.split()]
            if len(zahlen) != 4:
                print("Bitte genau 4 Zahlen eingeben!")
                continue
            if any(z < 1 or z > 6 for z in zahlen):
                print("Alle Zahlen muessen zwischen 1 und 6 liegen!")
                continue
            return Code(zahlen)
        except ValueError:
            print("Ungueltige Eingabe - bitte nur Zahlen!")


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
            print(f"Du hast {len(spiel.versuche)} Versuche gebraucht.")
            break


if __name__ == "__main__":
    main()
