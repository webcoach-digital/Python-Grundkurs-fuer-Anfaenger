# Spritverbrauch pro 100km in Liter - Bei schneller Fahrweise (200km/h)
spritverbrauchSchnell = 10

# Spritverbrauch pro 100km in Liter - Bei moderater Fahrweise (130km/h)
spritverbrauchModerat = 7

# Sprit im Tank in Liter
tank = 70

# Strecke Köln Augsburg
strecke = 550

fahrweise = input("Möchtest Du schnell fahren oder moderat. Antworte mit 'SCHNELL' oder 'MODERAT'")

if fahrweise == 'SCHNELL':
    spritverbrauch = strecke/100 * spritverbrauchSchnell
elif fahrweise == 'MODERAT':
    spritverbrauch = strecke/100 * spritverbrauchModerat

print("Spritverbrauch:", spritverbrauch)

tankEnde = tank - spritverbrauch

print("Tank am Ende der Fahrt:",tankEnde)

if tankEnde > 0:
    print("Glückwunsch, du wirst ankommen")
elif tankEnde <= 0:
    print("Du bleibst liegen, wenn Du nicht tankst während der Fahrt")



