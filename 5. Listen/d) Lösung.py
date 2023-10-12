# WORKOUT A

# Liste
uneven_numbers = [1, 3, 5, 7, 9]
print(uneven_numbers)

# Erstes Element (Index)
first_element = uneven_numbers[0]
print("Erstes Element:", first_element)

# Länge der Liste
length = len(uneven_numbers)
print("Länge:", length)

# Letztes Element
last_element = uneven_numbers[length-1]
print("Letztes Element:", last_element)

# Element hinzufügen
uneven_numbers.append(11)
print(uneven_numbers)

# Liste leeren
uneven_numbers.clear()
print(uneven_numbers)

# range() Funktion
uneven_numbers = list(range(12))
print(uneven_numbers)


# ---
# WORKOUT B

even_numbers = []
uneven_numbers = []

# Erster Durchlauf
numberOne = int(input("Gib eine Zahl deiner Wahl ein:"))

bEvenNumber = numberOne % 2 == 0
print(numberOne, "ist eine gerade Zahl:", bEvenNumber)

if bEvenNumber:
    even_numbers.append(numberOne)
else:
    uneven_numbers.append(numberOne)

# Zweiter Durchlauf
numberTwo = int(input("Gib eine Zahl deiner Wahl ein:"))

bEvenNumber = numberTwo%2 == 0
print(numberTwo, "ist eine gerade Zahl:", bEvenNumber)

if bEvenNumber:
    even_numbers.append(numberTwo)
else:
    uneven_numbers.append(numberTwo)

# Dritter Durchlauf
numberThree = int(input("Gib eine Zahl deiner Wahl ein:"))

bEvenNumber = numberThree%2 == 0
print(numberThree, "ist eine gerade Zahl:", bEvenNumber)

if bEvenNumber:
    even_numbers.append(numberThree)
else:
    uneven_numbers.append(numberThree)

# Ausgabe
print("Gerade Zahlen:", even_numbers)
print("Ungerade Zahlen", uneven_numbers)