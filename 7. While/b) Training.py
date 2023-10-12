# WORKOUT A | REPRODUKTION

# Erstelle eine Liste mit den Zahlen 6 - 10 und nutze dazu die range() und
# list() Funktion. Alternativ kannst du die Liste auch manuell erstellen. Lasse
# Dir nun mithilfe einer while Schleife alle Zahlen mit der print() Funktion im
# Terminal ausgeben die größer als 7 sind.


# WORKOUT B | TRANSFER & HEAVY

# Erstelle ein einfaches Zahlenraten-Spiel in Python. Das Programm soll eine
# zufällige Zahl zwischen 1 und 100 generieren und den Benutzer dazu auffordern,
# diese Zahl zu erraten. Das Programm sollte dem Benutzer Feedback geben, ob die
# geratene Zahl zu hoch oder zu niedrig ist, und den Benutzer solange raten
# lassen, bis er die richtige Zahl errät.
# Mit folgenden Code kannst du eine zufällig gesuchte Zielzahl erstellen:

import random

# Zufällige Zahl zwischen 1 und 100 generieren
zielzahl = random.randint(1, 100)
print(zielzahl)