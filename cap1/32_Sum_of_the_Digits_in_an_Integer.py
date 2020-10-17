#Chiedi all'utente
four_digit = int(input("Inserire un numero a 4 cifre: "))

#Convertire in una stringa
fd = str(four_digit)

#Somma delle tre cifre
somma = int(fd[0])+int(fd[1])+int(fd[2])+int(fd[3])

#Stampa risultato
print("La somma delle singole cifre è pari a: ", somma)