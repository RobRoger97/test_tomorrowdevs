#Equivalenze
d_h = 24
h_m = 60
m_s = 60

#Chiedi all'utente
d = int(input("Inserire il numero di giorni: "))
h = int(input("Inserire il numero di ore: "))
m = int(input("Inserire il numero di minuti: "))
s = int(input("Inserire il numero di secondi: "))

#Calcoli per arrivare ai secondi
d_to_h = d*d_h + h
h_to_m = d_to_h*h_m + m
m_to_s = h_to_m*m_s + s

#Stampa la risposta
print("I secondi totali della durata dell'utente è pari a ", m_to_s,"s")