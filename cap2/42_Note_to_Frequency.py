#Note's frequency
C4_f = 261.63
D4_f = 293.66
E4_f = 329.63
F4_f = 349.23
G4_f = 392.00
A4_f = 440.00
B4_f = 493.88

#Read the note name from user
name = input ("Enter the two character note name, such as C4: ")

#Store the note and its octave in separate variables
note = name[0]
octave = int(name[1])

#Get the frequency of the note, assuming it is in the fourth octave
if note=="A":
    f = A4_f
elif note=="B":
    f = B4_f
elif note=="C":
    f = C4_f
elif note=="D":
    f = D4_f
elif note=="E":
    f = E4_f
elif note=="F":
    f = F4_f
elif note=="G":
    f = G4_f

#Now adjust the frequency to bring it into the crrect octave
freq = f/(2**(4-octave))

#Display the result
print("The frequency of ", name, "is", freq)