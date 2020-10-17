#Percentuale di interesse
interesse = 0.04

#Domanda del conto all'utente
conto = float(input("Inserire la quantità di denaro depositata sul conto: "))

#Calcolo dell'importo dopo 1,2 e 3 anni
primo = conto + (conto*interesse)
secondo = primo + (primo*interesse)
terzo = secondo+ (secondo*interesse)

#Stampa risultato
print("Il conto alla fine del primo anno è pari a $", round(primo,2),", del secondo anno è $", round(secondo,2),"\
mentre del terzo anno è $", round(terzo,2))

