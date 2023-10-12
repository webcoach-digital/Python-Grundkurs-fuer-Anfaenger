# Leere Liste
empty_list = []

# Liste
even_numbers = [2, 4, 6, 8, 10]
print(even_numbers)

# Erstes Element (Index)
first_element = even_numbers[0]
print("Erstes Element:", first_element)

# Länge der Liste
length = len(even_numbers)
print("Länge:", length)

# Letztes Element
last_element = even_numbers[length-1]
print("Letztes Element:", last_element)

# Element hinzufügen
even_numbers.append(12)
print(even_numbers)

# Liste leeren
even_numbers.clear()
print(even_numbers)

# range() Funktion
even_numbers = list(range(2, 13, 2))
print(even_numbers)