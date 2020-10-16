#Imporare il modulo matematico
import math

#Accelerazione di gravità e velocità iniziale
vi = 0.0
g = 9.8

#Chiede all'utente l'altezza in metri da cui partel'oggetto
h = float(input("Inserire l'altezza in metri: "))

#Calcolo della velocità
vf = math.sqrt(vi**2 + 2*g*h)

#Stampa risultato
print("L'oggetto colpirà il terreno con una velocità finale pari a %.2f m/s" % vf)