# Nicht effizient
prime_numbers = [2, 3, 5, 7, 11, 13]

print(prime_numbers[0])
print(prime_numbers[1])
print(prime_numbers[2])
print(prime_numbers[3])
print(prime_numbers[4])


# Effizient - for Schleifen
prime_numbers = [2, 3, 5, 7, 11, 13]

for prime_number in prime_numbers:
    print(prime_number)


# For Schleifen mit range() Funktion
print(list(range(10)))

for number in range(10):
    if number > 5:
        print("Zahl die größer als ist", number)





