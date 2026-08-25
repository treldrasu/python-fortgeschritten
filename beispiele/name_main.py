# Beispiel: __name__ == '__main__' (Folie 69)
# Modul als Bibliothek ODER als Skript.

def main():
    print("Starte Programm...")


if __name__ == "__main__":
    main()

# Direkt ausgefuehrt:  python name_main.py   -> main() laeuft
# Importiert:          import name_main     -> main() laeuft NICHT
