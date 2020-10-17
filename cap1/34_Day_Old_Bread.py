#Dati
Pane_prezzo = 3.49
Sconto_old = 0.60

#Chiedi all'utente
n = int(input("Inserire il numero di pane vecchio di un giorno: "))

#Calcoli
prezzo_regolare = n*Pane_prezzo
sconto = prezzo_regolare*Sconto_old
totale = prezzo_regolare-sconto

#Stampa i risultati separatamente
print("Prezzo regolare: %5.2f" % prezzo_regolare)
print("Lo sconto:       %5.2f" % sconto)
print("Il totale:       %5.2f" % totale)