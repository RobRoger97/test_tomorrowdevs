#importare moduli
import math
import time

#chiede all'utente l'anno
anno = int(input("Inserire l'anno: "))

#the Anonymous Gregorian Computus algorithm
a = anno%19
b = math.floor(anno/100)
c = anno%100
d = math.floor(b/4)
e = b%4
f = math.floor((b+8)/25)
g = math.floor((b-f+1)/3)
h = (19*a+b-d-g+15)%30
i = math.floor(c/4)
k = c%4
l = (32+2*e+2*i-h-k)%7
m = math.floor((a+11*h+22*l)/451)
mese = math.floor((h+l-7*m+114)/31)
giorno = 1+((h+l-7*m+114)%31)

#Calcolare la data
t = (anno,mese,giorno,0,0,0,6,0,0)
data = time.asctime(t)

#Stampa la risposta:
print("Pasqua dell'anno inserito avviene il ", data)