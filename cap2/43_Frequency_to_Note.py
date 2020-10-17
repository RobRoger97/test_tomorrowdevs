#Data
C4_f = 261.63
D4_f = 293.66
E4_f = 329.63
F4_f = 349.23
G4_f = 392.00
A4_f = 440.00
B4_f = 493.88
Lim  = 1

#Read the frequency from the user
freq = float(input("Enter a frequency in Hz: "))

# If the frequency is within one Hertz of a value listed in
# the table in the previous question then report the name of the corresponding note.
# Otherwise report that the frequency does not correspond to a known note.
if freq >= C4_f - Lim and freq <= C4_f + Lim:
    note = "C4"
elif freq >= D4_f - Lim and freq <= D4_f + Lim:
    note = "D4"
elif freq >= E4_f - Lim and freq <= E4_f + Lim:
    note = "E4"
elif freq >= F4_f - Lim and freq <= F4_f + Lim:
    note = "F4"
elif freq >= G4_f - Lim and freq <= G4_f + Lim:
    note = "G4"
elif freq >= A4_f - Lim and freq <= A4_f + Lim:
    note = "A4"
elif freq >= B4_f - Lim and freq <= B4_f + Lim:
    note = "B4"
else:
    note = ""
# Display the result, or an appropriate error message
if note == "":
    print("There is no note that corresponds to that frequency.")
else:
    print("That frequency is", note)