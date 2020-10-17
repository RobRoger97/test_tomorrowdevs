#Suggerimento
sqr_ft_acre = 43560

#Chiedere all'utente le dimensioni
lunghezza = float(input("Inserire la lunghezza del campo in piedi: "))
larghezza = float(input("Inserire la larghezza del campo in piedi: "))

#Calcolo dell'area in acri 
acri = (lunghezza*larghezza)/sqr_ft_acre

#Stampa il risultato
print("L'area del campo è ", acri, " acri")
