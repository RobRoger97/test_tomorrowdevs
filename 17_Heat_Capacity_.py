#Costanti
cap_term_acqua = 4.186
elet_spesa = 8.9
J_to_KWH = 2.777e-7

#Legge volume e differenza termica dall'utente
volume = float(input("Inserire il valore del volume in millilitri "))
d_temp = float(input("Inserire la differenza termica in gradi Celsius: "))

#Calcolo dell'energia ij Joules
q = volume*d_temp*cap_term_acqua

#Stampare il risultato in Joules
print("Saranno richiesti %d Joules di energia." % q)

#Calcolo del costo
kwh = q*J_to_KWH
cost = kwh*elet_spesa

#Stampa il costo
print("Questa energia avrà un costo pari a %.2f centesimi." % cost)

