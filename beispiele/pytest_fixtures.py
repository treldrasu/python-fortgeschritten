# Beispiel: Fixtures (Folie 57)
# Fuehre aus:  pytest pytest_fixtures.py
# Fixtures liefern jedem Test eine frische Instanz.

import pytest


class Konto:
    def __init__(self, inhaber, guthaben):
        self.inhaber = inhaber
        self.guthaben = guthaben

    def abheben(self, betrag):
        if betrag > self.guthaben:
            return
        self.guthaben -= betrag


@pytest.fixture
def konto():
    return Konto("Kai", 100)


def test_abheben(konto):
    konto.abheben(40)
    assert konto.guthaben == 60


def test_zu_viel(konto):
    konto.abheben(999)
    assert konto.guthaben == 100   # unveraendert
