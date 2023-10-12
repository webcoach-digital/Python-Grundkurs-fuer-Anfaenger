# WORKOUT A

age = int(input("Bitte gib dein Alter ein:"))

if age >= 18:
    print("Du darfst wählen")
elif age >= 16:
    print("In Bremen darfst Du bei der Landtagswahl wählen")
else:
    print("Du darfst noch nicht wählen")


# WORKOUT B

# Alkohol in Gramm
gBeer500 = 20
gBeer330 = 13
gWine200 = 18
gWine100 = 9
gChampagne100 = 9
gShot40 = 11
gShot20 = 5.5

# Abfrage der getrunkenen Mengen
nBeer500 = int(input("Wie viele große Bierflaschen (500ml) hast Du getrunken:"))
nBeer330 = int(input("Wie viele kleine Bierflaschen (300ml) hast Du getrunken:"))
nWine200 = int(input("Wie viele große Weingläser (200ml) hast Du getrunken:"))
nWine100 = int(input("Wie viele große Weingläser (100ml) hast Du getrunken:"))
nChampagne100 = int(input("Wie viele Champagnergläser (100ml) hast Du getrunken:"))
nShot40 = int(input("Wie viele große Shots (40ml) hast Du getrunken:"))
nShot20 = int(input("Wie viele kleine Shots (20ml) hast Du getrunken:"))

# Berechnung der konsumierten Akoholmenge in Gramm
gAlcohol = gBeer500*nBeer500 + gBeer330*nBeer330 + gWine200*nWine200 + gWine100*nWine100 + gChampagne100*nChampagne100 + gShot40*nShot40 + gShot20*nShot20

# Gewicht abfragen
kgWeight = int(input("Wie viel wiegst Du?"))

# Promille berechnen
promille = gAlcohol / kgWeight * 0.7

# Ausgabe Promille
print(promille)

# If else Bedingung
if promille > 0.5:
    print("Du darst kein Auto mehr fahren")
elif promille > 0.3:
    print("Du darfst noch Auto fahren, machst Dich aber haftbar bei einem Unfall")
elif promille == 0:
    print("Freie Fahrt!")
else:
    print("Du darst noch Auto fahren, solltest Dir aber der Sicherheitsrisiken bewusst sein")