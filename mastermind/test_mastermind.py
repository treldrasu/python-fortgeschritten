"""Mastermind CLI - Tests fuer die Vergleichs-Logik (Bonus-Aufgabe).

Fuehre aus:  pytest test_mastermind.py
"""
import pytest

from mastermind import Code, Spiel


def test_code_gleich():
    """Zwei Codes mit gleichen Zahlen sind gleich."""
    assert Code([1, 2, 3, 4]) == Code([1, 2, 3, 4])


def test_code_ungleich():
    """Zwei Codes mit verschiedenen Zahlen sind ungleich."""
    assert Code([1, 2, 3, 4]) != Code([1, 2, 3, 5])


def test_code_laenge():
    """Ein Code hat immer die Laenge 4."""
    assert len(Code([1, 2, 3, 4])) == 4


def test_vergleich_alle_richtig():
    """Alle 4 Zahlen an richtiger Position -> 4 schwarz, 0 weiss."""
    spiel = Spiel(Code([1, 2, 3, 4]))
    assert spiel.vergleichen(Code([1, 2, 3, 4])) == (4, 0)


def test_vergleich_keine_treffer():
    """Keine Zahl stimmt -> 0 schwarz, 0 weiss."""
    spiel = Spiel(Code([1, 2, 3, 4]))
    assert spiel.vergleichen(Code([5, 6, 5, 6])) == (0, 0)


def test_vergleich_nur_positionen():
    """Alle 4 Zahlen richtig, aber alle falsch positioniert -> 0 schwarz, 4 weiss."""
    spiel = Spiel(Code([1, 2, 3, 4]))
    assert spiel.vergleichen(Code([4, 3, 2, 1])) == (0, 4)


def test_vergleich_gemischt():
    """2 richtig positioniert, 1 falsch positioniert, 1 nicht vorhanden."""
    spiel = Spiel(Code([1, 2, 3, 4]))
    assert spiel.vergleichen(Code([1, 2, 4, 5])) == (2, 1)


def test_vergleich_doppelte_zahlen():
    """Doppelte Zahlen im Tipp werden korrekt gezaehlt."""
    spiel = Spiel(Code([1, 1, 2, 3]))
    assert spiel.vergleichen(Code([1, 1, 1, 1])) == (2, 0)


def test_ist_gewonnen():
    """Gewonnen, wenn der Tipp dem geheimen Code entspricht."""
    spiel = Spiel(Code([1, 2, 3, 4]))
    assert spiel.ist_gewonnen(Code([1, 2, 3, 4])) is True
    assert spiel.ist_gewonnen(Code([1, 2, 3, 5])) is False
