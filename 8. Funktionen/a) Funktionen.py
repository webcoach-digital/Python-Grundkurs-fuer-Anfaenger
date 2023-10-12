# Funktion ohne Parameter erstellen
def sayHello():
    print("Hello from Cologne")

# Funktion ohne Parameter aufrufen
sayHello()


# Funktion mit Parameter erstellen
def sayHelloTo(name):
    print("Hello", name)

# Funktion mit Parametern aufrufen
sayHelloTo("Eric")


# Funktion mit optionalen Parametern erstellen
def add(a=0, b=0):
    result = a + b
    print(result)

# Funktion mit optionalen Paremtern aufrufen
add(5, 5)
add(a=6, b=6)
add(b=13)


# Funktion mit Rückgabewert erstellen
def getSum(a, b):
    return a + b

# Funktion mit Rückgabewert aufrufen und diesen in einer Variablen speichern
sum = getSum(4, 5)
print(sum)