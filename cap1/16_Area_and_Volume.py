#importare il modulo matematico
import math

#Lettura del raggio
radius = float(input("Inserire il valore del raggio: "))

#Calcolo dell'area della cerchio e il volume della sfera 
area_cerchio = math.pi*(radius**2)
vol_sfera = (4/3)*math.pi*(radius**3)

#Stampa il risultato
print("L'area del cerchio è pari a ", round(area_cerchio,4), "m^2, ,mentre il volume della sfera è ", round(vol_sfera,4), "m^3.")
