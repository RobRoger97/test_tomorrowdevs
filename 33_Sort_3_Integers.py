#Chiedi all'utente
a = int(input("Inserire il primo numero: "))
b = int(input("Inserire il secondo numero: "))
c = int(input("Inserire il terzo numero: "))

#Calcolo del massimo, del minimo e del medio
mn = min(a,b,c)
mx = max(a,b,c)
md = a+b+c-mn-mx

#Stampa risultato
print("L'ordine dei numeri è il seguente: ")
print("  ",mn)
print("  ",md)
print("  ",mx)