#Importare il modulo matematico
import math

#Richiesta di raggio e altezza del cilindro
r = float(input("Inserire il valore del raggio: "))
h = float(input("Inserire il valore dell'altezza: "))

#Calcolo dell'area e del volume del cilindro
area = r**2*math.pi
volume = area*h

#Stampa il risultato
print ("Il volume del cilindro è: ", round(volume,1))
