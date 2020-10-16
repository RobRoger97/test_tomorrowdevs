#Chiedi all'utente
noise = int(input("Inserire un valore in dB di un rumore: "))

#Verifica
if noise==130:
    print("Il rumore corrisponde al martello pneumatico.")
elif noise==106:
    print("Il rumore corrisponde al rasaerba a gas.")
elif noise==70:
    print("Il rumore corrisponde alla sveglia.")
elif noise==40:
    print("Il rumore corrisponde alla stanza silenziosa.")
elif noise>40 and noise<70:
    print("Corrisponde ad un rumore intermedio tra quello \
di una stanza silenziosa e quello di una sveglia.")
elif noise>70 and noise<106:
    print("Corrisponde ad un rumore intermedio tra quello \
di una sveglia e quello di un rasaerba a gas.")
elif noise>106 and noise<130:
    print("Corrisponde ad un rumore intermedio tra quello \
di un rasaerba a gas e quello di un martello pneumatico.")
elif noise<40:
    print("Il rumore è più silenzioso di quello di una stanza silenziosa")
else:
    print("Il rumore è più forte di quello di un martello pneumatico")