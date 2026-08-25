# Beispiel: logging statt print (Folie 65)
# Fehler dokumentieren statt nur ausgeben - mit Level und Zeitstempel.

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    ergebnis = 10 / 0
except ZeroDivisionError:
    logger.error("Division durch 0", exc_info=True)

# Levels: DEBUG < INFO < WARNING < ERROR < CRITICAL
# Ausgabe: ERROR:__main__:Division durch 0 + Traceback (dank exc_info=True)
