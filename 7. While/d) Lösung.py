# WORKOUT A

# numbers = [6, 7, 8, 9, 10]
numbers = list(range(6, 11))

index = len(numbers) - 1
while numbers[index] > 7:
    print(numbers[index])
    index -= 1


# WORKOUT B

import random

# Zufällige Zahl zwischen 1 und 100 generieren
zielzahl = random.randint(1, 100)
versuche = 0
richtig_geraten = False

while not richtig_geraten:
    versuch = int(input("Rate eine Zahl zwischen 1 und 100: "))
    versuche += 1

    # Bedingungen überprüfen und Feedback geben
    if versuch < zielzahl:
        print("Die geratene Zahl ist zu niedrig. Versuche es erneut.")
    elif versuch > zielzahl:
        print("Die geratene Zahl ist zu hoch. Versuche es erneut.")
    else:
        print(f"Herzlichen Glückwunsch! Du hast die richtige Zahl ({zielzahl}) in {versuche} Versuchen erraten.")
        richtig_geraten = True
