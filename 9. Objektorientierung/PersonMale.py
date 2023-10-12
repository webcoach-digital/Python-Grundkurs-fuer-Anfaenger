from Person import Person

# Vererbung
class PersonMale(Person):

    def __init__(self, name, weight, age=0):
        # Konstrukter von Klasse Person aufrufen mit super()
        super().__init__(name, weight, age)

    # Methode überschreiben
    def getPromille(self):
        promille = self.alcohol / (self.weight * 0.7)
        return promille