from Person import Person

# Objekt der Klasse Person erstellen
franz = Person("Franz")
franz.printAlcohol()

# Methode aufrufen und deren Code ausführen lassen
franz.drinkBeer500()
franz.drinkBeer500()
franz.printAlcohol()

# Methode 'getPromille()' aufrufen und deren Code ausführen lassen
print(f"Name: {franz.name}, Promille: {franz.getPromille()}")