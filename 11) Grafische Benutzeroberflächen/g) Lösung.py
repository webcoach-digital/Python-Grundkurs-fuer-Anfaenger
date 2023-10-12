from tkinter import *

# Bisheriger Code
window = Tk()
window.geometry("600x300")
window.title("Addtions-Rechner")
label = Label(window, text="Bitte gebe zwei Zahlen ein die Du addieren möchtest, klicke auf den Button und erhalte dein Ergebnis")
label.pack(pady=20)

input_one = StringVar()
labelOne = Label(window, text="Zahl Eins")
labelOne.pack()
entryOne = Entry(window, textvariable=input_one)
entryOne.pack()

input_two = StringVar()
labelTwo = Label(window, text="Zahl Zwei")
labelTwo.pack()
entryTwo = Entry(window, textvariable=input_two)
entryTwo.pack()

# Erstellen einer Funktion die aufgerufen werden soll wenn der Button geklickt wird
def add():
    result = int(input_one.get()) + int(input_two.get())
    labelResult.config(text=result)

# Button erstellen und Callback Funktion übergeben
button = Button(window, text="Ergebnis berechnen", command=add)
button.pack(pady=20)

# Neues Label erstellen zur Anzeige des aktuellen Promille-Wertes
labelResult = Label(window, text="Es liegt noch kein Ergebnis vor")
labelResult.pack(pady=20)

# Dialog darstellen
window.mainloop()