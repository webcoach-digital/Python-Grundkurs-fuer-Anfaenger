from Person import Person

eric = Person("Eric")
print(eric.name)
print("Gewicht", eric.weight)

peter = Person("Peter", 90)
print("Gewicht:", peter.weight)

rene = Person("Rene")
print(f"Name: {rene.name}, Getrunkener Alkohol: {rene.alcohol}")