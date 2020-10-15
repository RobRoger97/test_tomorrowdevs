#Prezzo del versamento
Less_deposit = 0.10
More_deposit = 0.25

#Quanti contenitori dei vari litri
less = int(input("Quanti contenitori da 1 litro o meno? "))
more = int(input("Quanti contenitori da più di 1 litro? "))

#Calcolo del rimborso
rimborso = less*Less_deposit + more*More_deposit

#Stampare il risultato con 2 cifre dopo la virgola
print("Il tuo rimborso totale sarà di $%.2f." % rimborso)
