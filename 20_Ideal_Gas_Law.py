#Costante
R = 8.314

#Chiedi all'utente
P = float(input("Inserire il valore della pressione in Pascals: "))
V = float(input("Inserire il valore del volume in litri: "))
T = float(input("Inserire il valore della temperatura in Kelvin: "))

#Calcolo del numero delle moli del gas
n = (P*V)/(R*T)

#Stampa il risultato
print("Il numero di moli del gas è pari a ",n)

#Il test riguardo la tanica SCUBA con le proprietà del gas richieste
#Presenta un numero di moli del gas pari a 98471.674479