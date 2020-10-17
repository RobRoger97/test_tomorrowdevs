#Chiedi all'utente
p_kpascal = float(input("Inserire il valore della pressione in chilopascal: "))

#Trasformazione in libbre per pollice qudrato
p_psi = p_kpascal/6.895
print("La pressione in PSI è pari a: ", round(p_psi,3))

#Trasformazione in Torr 
p_torr = p_kpascal*7.501
print("La pressione in Torr è pari a: ", round(p_torr,3))

#Trasformazione in atm
p_atm = p_kpascal/101
print("La pressione in atm è pari a: ", round(p_atm,3))