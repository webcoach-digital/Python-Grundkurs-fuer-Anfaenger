from tkinter import *

# Bisheriger Code
window = Tk()
window.geometry("600x300")
window.title("Promille-Rechner")

label = Label(window, text="Bitte fülle alle Felder aus, klicke auf den Button und erhalte deine Promille Anzahl")
label.pack(pady=20)

# Eingabe Gewicht
input_weight = StringVar()
labelWeight = Label(window, text="Gewicht")
labelWeight.pack()
entryWeight = Entry(window, textvariable=input_weight)
entryWeight.pack()

# Eingabe Alkoholmenge (g)
input_alcohol = StringVar()
labelAlcohol = Label(window, text="Alkoholmenge (g)")
labelAlcohol.pack()
entryAlcohol = Entry(window, textvariable=input_alcohol)
entryAlcohol.pack()

# Dialog darstellen
window.mainloop()

