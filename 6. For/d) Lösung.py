# WORKOUT A
prime_numbers = [11, 13, 17, 19, 23, 29]

for prime_number in prime_numbers:
    print(prime_number)


# ---
# WORKOUT B
even_numbers = []

for number in range(101):
    is_even_number = number%2 == 0
    if (is_even_number and number > 0): even_numbers.append(number)

print(even_numbers)

# ---
# WORKOUT C
prime_numbers = []

for number in range(101):
    is_prime_number = number > 1
    for number_two in range(2, number):
        if number%number_two == 0: 
            is_prime_number = False
            break
    if is_prime_number: prime_numbers.append(number)

print(prime_numbers)

    
    