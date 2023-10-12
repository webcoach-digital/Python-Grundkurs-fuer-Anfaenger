# Eigene Exception Klasse erstellen, die von der Klasse Exception erbt
class TemperatureError(Exception):
    def __init__(self, message):
        super().__init__(message)

# try
try:
    # request age via input() function
    temperature = float(input("Bitte gebe die aktuelle Temparatur ein: "))

    # throw exception wenn das Alter größer als 118 ist
    if temperature > 70 or temperature < -93:
        raise TemperatureError("Falsche Eingabe: Bitte gebe eine REALISTISCHE Temperatur ein")

    print(f"Die aktuelle Temperatur beträgt {temperature} °C")

# catch AgeError Exception - Eigene Exception
except TemperatureError as err:
    print(err)

# catch AgeError Exception - Vorhandene Exception
except ValueError:
    print("Falsche Eingabe: Bitte gebe eine ZAHL für die Temperatur ein")

# allgemein gültige Aussage im immer ausgeführten finally Block
finally:
    print("Die höchste je gemessene Temperatur beträgt 70,7 °C, gemessen im Jahr 2005 im Iran")
