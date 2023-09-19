# WORKOUT A

result = not (5**2 > 5%2 or ("5" == 5 or 30 >= 30))
print("Das Ergebnis ist:", result)


# ---
# WORKOUT B

# "5": String (str)
#  5 : Integer (int)
# 5.0: Float (float)
isEqual = 5 == 5.0
print("5 und 5.0 sind gleich:", isEqual)


# ---
# WORKOUT C
age = input("Bitte geben Sie ihr Alter ein:")

# Via input() erhaltene Nutzereingaben sind vom Datentyp String (str):
print("Datentyp von input() Eingaben:", type(age))

# Folgender Code gibt eine Fehlermeldung (TypeError: '>' not supported between instances of 'str' and 'int')aus, weil sich Werte vom Datentyp String und Integer nicht miteinander verglichen werden können. Kommentiere diesen daher aus indem du vor diese Code Zeile einen Hashtag ("#") setzt 
# olderThan18 = age > 18

# Umwandlung der input() Eingabe in den Datentyp Integer (int)
olderThan18 = int(age) > 18
print("Älter als 18:", olderThan18)

