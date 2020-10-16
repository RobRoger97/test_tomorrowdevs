#Importare il modulo matematico
import math

#Chiedere all'utente
s1 = float(input("Inserire la lunghezza del primo lato in metri: "))
s2 = float(input("Inserire la lunghezza del secondo lato in metri: "))
s3 = float(input("Inserire la lunghezza del terzo lato in metri: "))

#Calcolo della s
s = (s1+s2+s3)/2

#Calcolo area del triangolo
area = math.sqrt(s*(s-s1)*(s-s2)*(s-s3))

#Stampa il risultato
print("L'area del triangolo è: ",round(area,3),"m^2")