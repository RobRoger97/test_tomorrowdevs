#sottomultipli e multipli del piede
f_y= 1/3
f_in = 12
f_m = 1/5280

#Chiede una misurazione in piedi all'utente
ft = int(input("Numero di piedi: "))

#Convertire
inches = ft*f_in
yards = ft*f_y
miles = ft*f_m

#Risultati
print(ft, " piedi corrispondono a ", inches, " pollici, ", yards, " yards e ", miles, " miglia.")

