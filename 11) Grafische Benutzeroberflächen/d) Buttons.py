from tkinter import *

# Bisheriger Code
window = Tk()
window.geometry("600x300")
window.title("Promille-Rechner")
label = Label(window, text="Bitte fülle alle Felder aus, klicke auf den Button und erhalte deine Promille Anzahl")
label.pack(pady=20)

input_weight = StringVar()
labelWeight = Label(window, text="Gewicht")
labelWeight.pack()
entryWeight = Entry(window, textvariable=input_weight)
entryWeight.pack()

input_alcohol = StringVar()
labelAlcohol = Label(window, text="Alkoholmenge (g)")
labelAlcohol.pack()
entryAlcohol = Entry(window, textvariable=input_alcohol)
entryAlcohol.pack()

# Erstellen einer Funktion die aufgerufen werden soll wenn der Button geklickt wird
def setPromille():
    promille = round(int(input_alcohol.get()) / (int(input_weight.get()) * 0.65), 2)
    labelResult.config(text=promille)

# Button erstellen und Callback Funktion übergeben
button = Button(window, text="Promille berechnen", command=setPromille)
button.pack(pady=20)


# Neues Label erstellen zur Anzeige des aktuellen Promille-Wertes
labelResult = Label(window, text="Es liegt noch kein Ergebnis vor")
labelResult.pack(pady=20)

# Dialog darstellen
window.mainloop()

