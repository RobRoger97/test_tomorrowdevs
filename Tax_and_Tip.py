#Tasse
Tax_rate = 0.22
Tip_rate = 0.18

#Costo del pasto dell'utente
cost = float(input("Inserire il costo del pasto: "))

#Calcolo della tassa e della mancia
tax = cost*Tax_rate
tip = cost*Tip_rate
total = cost + tax + tip

#Stampa il risultato
print("La tassa è %.2f e la mancia è %.2f, quindi il totale è %.2f." % (tax, tip, total))
    
