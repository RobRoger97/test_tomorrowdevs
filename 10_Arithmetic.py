#importare il modulo matematico
import math

#Chiedere i valori di a e b all'utente
a = int(input("Inserire il valore di a: "))
b = int(input("Inserire il valore di b: "))

#Somma, differenza, prodotto, quoziente e resto
print(a,"+",b, "è", a+b)
print(a,"-",b, "è", a-b)
print(a,"*",b, "è", a*b)
print(a,"/",b, "è", a/b)
print(a,"%",b, "è", a%b)

#Calcolo del logaritmo e della potenza
print("Il logaritmo di base 10 di ", a, "è", math.log10(a))
print(a,"^", b, "è", a**b)

