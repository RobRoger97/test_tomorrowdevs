#Coefficienti numerici
c0 = 13.12
c1 = 0.6215
c2 = -11.37
c3 = 0.3965
exp = 0.16

#L'indice di "wind chill" è considerato valido solo per temperature più o meno uguali a 10 gradi Celsius 
#e con velocità del vento che supera i 4.8 chilometri orari.
#Chiede all'utente
t = float(input("Inserire la temperatura dell'aria in gradi Celsius: "))
v = float(input("Inserire la velocità del vento in chilometri orari: "))

#Calcolo dell'indice di wind chill 
wci =c0+(c1*t)+(c2*v**exp)+(c3*t*v**exp)

#Stampa risultato
print("L'indice di wind chill è ", round(wci))