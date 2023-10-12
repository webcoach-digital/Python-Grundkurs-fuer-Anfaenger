# WORKOUT A

def subtract(a=0, b=0):
    result = a - b
    return result


print(subtract(10))


# ---
# WORKOUT B

def square(num):
    return num*num

counter = 0
number = 2

while number < 1000:
    number = square(number)
    counter += 1
    print(number)

print("Die Ausgangszahl wurde", counter, "Mal mit sich selbst multipliziert. Das Ergebnis lautet:", number)