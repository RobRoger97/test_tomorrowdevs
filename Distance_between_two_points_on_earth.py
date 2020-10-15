#Richiamare il modulo matematico
import math

#Raggio terrestre in Km
radius = 6371.01

#Chiede latitudine e longitudine dei due punti all'utente
lat1 = float(input("Inserire il valore della latitudine del primo punto: "))
lat2 = float(input("Inserire il valore della latitudine del secondo punto: "))
lon1 = float(input("Inserire il valore della longitudine del primo punto: "))
lon2 = float(input("Inserire il valore della longitudine del secondo punto: "))

#Trasformazione in radianti
t1 = math.radians(lat1)
t2 = math.radians(lat2)
g1 = math.radians(lon1)
g2 = math.radians(lon2)

#Calcolo della distanza
distance = radius*math.acos(math.sin(t1)*math.sin(t2) + math.cos(t1)*math.cos(t2)*math.cos(g1-g2))

#Stampa la distanza
print("La distanza tra i due punti è ", round(distance,4), "Km")
