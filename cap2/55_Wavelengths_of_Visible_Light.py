#Read the wavelenght from the user
w_lenght = int(input("Enter a wavelenght: "))

#Report its color
if w_lenght>= 380 and w_lenght<450:
    color = "Violet"
elif w_lenght>=450 and w_lenght<495:
    color = "Blue"
elif w_lenght>=495 and w_lenght<570:
    color = "Green"
elif w_lenght>=570 and w_lenght<590:
    color = "Yellow"
elif w_lenght>=590 and w_lenght<620:
    color = "Orange"
elif w_lenght>=620 and w_lenght<=750:
    color = "Red"
else:
    color = ""

#Display the result
if color == "":
    print("That wavelenght is ouside of the visible spectrum.")
else:
    print("The color of that wavelenght is: %s" %color)