# WORKOUT A

def subtract(a=0, b=0):
    result = a - b
    return result

print(subtract(10, 5))


# ---
# WORKOUT B

def square(number):
    return number*number

counter = 0
number = 2

while number < 1000:
    number = square(number)
    counter += 1
    print(number)

print("Die Ausgangszahl wurde", counter, "Mal mit sich selbst multipliziert. Das Ergebnis lautet:", number)
