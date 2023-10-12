from tkinter import *

# Bisheriger Code
window = Tk()
window.geometry("600x300")
window.title("Promille-Rechner")

# Objekt label der Klasse Label erstellen und der __init__() Funktion zwei Argumente übergeben
label = Label(window, text="Bitte fülle alle Felder aus, klicke auf den Button und erhalte deine Promille Anzahl")

# Aufruf der Methode Methode unter Übergabe eines Arguments für den Abstand nach oben
label.pack(pady=20)

# Dialog darstellen
window.mainloop()

