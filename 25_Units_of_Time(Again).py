#Equivalenze
s_d = 86400
s_h = 3600
s_m =60

#Chiedi all'utente
s = int(input("Inserire il numero di secondi: "))

#Trasformazione dei secondi in giorno,ore,minuti e secondi
d = s/s_d
s = s%s_d

h = s/s_h
s = s%s_h

m = s/s_m
s = s%s_m

#Stampare il risultato
print("L'equivalente risultato è %d:%02d:%02d:%02d." %(d,h,m,s))