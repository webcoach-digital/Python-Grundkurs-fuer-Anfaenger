from Person import Person

# Vererbung
class PersonFemale(Person):

    def __init__(self, name, weight):
        # Konstrukter von Klasse Person aufrufen mit super()
        super().__init__(name, weight)

    # Methode überschreiben
    def getPromille(self):
        promille = self.alcohol / (self.weight * 0.6)
        return promille