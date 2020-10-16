#monete rappresentate in centesimi
cents_per_toonie = 200
cents_per_loonie = 100
cents_per_quarter = 25
cents_per_dime = 10
cents_per_nickel = 5

#Legge il numero di centesimi dell'utente
cents = int(input("Numero di centesimi dell'utente: "))

#Per sapere quanti toonies ci sono, basta calcolare il quoziente.
#Poi viene calcolato il resto da dare
print(" ", cents//cents_per_toonie,"toonies")
cents = cents % cents_per_toonie

#Ripetere lo stessoper loonie, quarter, dime e nickel
print(" ", cents//cents_per_loonie,"loonies")
cents = cents % cents_per_loonie

print(" ", cents//cents_per_quarter,"quarters")
cents = cents % cents_per_quarter

print(" ", cents//cents_per_dime,"dimes")
cents = cents % cents_per_dime

print(" ", cents//cents_per_nickel,"nickels")
cents = cents % cents_per_nickel

#Stampa il numero pennies
print (" ", cents, "pennies")