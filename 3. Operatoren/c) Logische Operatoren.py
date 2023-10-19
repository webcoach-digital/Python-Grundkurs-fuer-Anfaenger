# Und
a = True
b = True
result = a and b
print(a, "und", b, "ergeben:", result)

# Oder
a = 5 > 1 # True
b = 5 < 1 # False
result = a or b
print(a, "oder", b, "ergeben:", result)


# Umkehren
olderThan18 = True
youngerThan18 = not olderThan18
print("Älter als 18:", olderThan18)
print("Jünger als 18:", youngerThan18)