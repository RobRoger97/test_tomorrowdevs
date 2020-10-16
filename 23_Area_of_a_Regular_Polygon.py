#Importare modulo matematico
import math

#Chiedi all'utente
s = float(input("Inserire la lunghezza del lato in metri: "))
n = int(input("Inserire il numero dei lati del poligono regolare: "))

#Calcolo area
area = (n*s**2)/(4*math.tan(math.pi/n))

#Stampa risultato
print("L'area del poligono regolare con numero di lati pari a ",n," con \
lunghezza pari a ",s, "m è pari a ", round(area,3),"m^2")