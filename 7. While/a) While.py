# Nicht effizient
numbers = list(range(1, 6))  # [1, 2, 3, 4, 5]

if numbers[0] <= 3:  # 1 --> True
    print(numbers[0])
if numbers[1] <= 3:  # 2 --> True
    print(numbers[1])
if numbers[2] <= 3:  # 3 --> True
    print(numbers[2])
if numbers[3] <= 3:  # 4 --> False
    print(numbers[3])
if numbers[4] <= 3:  # 5 --> False
    print(numbers[4])


# Effizient - while Schleifen
index = 0
while numbers[index] <= 3:
    print(numbers[index])
    index += 1

