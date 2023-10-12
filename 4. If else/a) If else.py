# if
promille = 0.4
if promille > 0.5:
    print("Du darfst kein Auto mehr fahren")


# elif
promille = 0.4
if promille > 0.5:
    print("Du darst kein Auto mehr fahren")
elif promille > 0.3:
    print("Du darfst noch Auto fahren, machst Dich aber haftbar bei einem Unfall")


# else
promille = 0.6
if promille > 0.5:
    print("Du darst kein Auto mehr fahren")
elif promille > 0.3:
    print("Du darfst noch Auto fahren, machst Dich aber haftbar bei einem Unfall")
elif promille == 0:
    print("Freie Fahrt!")
else:
    print("Du darst noch Auto fahren, solltest Dir aber der Sicherheitsrisiken bewusst sein")