# b) Klassen: Klasse erstellen und Namen definieren
class Person:

    # b) Klassen: Konstruktor Funktion definieren --> Wird beim Erstellen eines Objekts automatisch aufgerufen
    def __init__(self, name, weight=80, age=0):
        self.name = name
        self.weight = weight
        self.alcohol = 0
        self.age = age

    # d) Methoden: Erstellen der Methode (Funktion) 'drinkBeer500'
    def drinkBeer500(self):
        self.alcohol = self.alcohol + 20

    # Training
    def drinkWine200(self):
        self.alcohol = self.alcohol + 18

    # d) Methoden: Erstellen der Methode (Funktion) 'printAlcohol'
    def printAlcohol(self):
        print(f"Name: {self.name}, Getrunkener Alkohol: {self.alcohol}")

    # d) Methoden: Erstellen der Methode (Funktion) 'getPromille'
    def getPromille(self):
        promille = self.alcohol / (self.weight * 0.65)
        return promille

    # Workout B
    def drive(self):
        promille = self.getPromille()

        if self.age < 18:
            print("Zu jung zum Autofahren")
        elif promille > 0.5:
            print("Bitte kein Auto mehr fahren!")
        elif promille > 0:
            print("Du darfst fahren, solltest es besser sein lassen")
        else:
            print("Gute Fahrt")


