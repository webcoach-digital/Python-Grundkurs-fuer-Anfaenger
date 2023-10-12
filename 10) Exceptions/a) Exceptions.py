class AgeError(Exception):
    def __init__(self, message):
        super().__init__(message)


try:
    # request age via input() function
    age = int(input("Bitte gebe dein Alter ein: "))

    # throw exception wenn das Alter größer als 118 ist
    if age > 118:
        raise AgeError("Falsche Eingabe: Bitte gebe ein REALISTISCHES Alter ein")

# catch AgeError Exception - Eigene Exception
except AgeError as err:
    print(err)

# catch AgeError Exception - Vorhandene Exception
except ValueError:
    print("Falsche Eingabe: Bitte gebe eine ZAHL für dein Alter ein")

# finally Code - Hier ohne Bedeutung
finally:
    print("Finally wird immer aufgerufen")