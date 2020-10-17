#Suggerimenti
in_ft = 12
cm_in =2.54

#Si chiede l'altezza in piedi e in pollici
print("Inserire la tua altezza:")
feet = int(input("Numero di piedi: "))
inches = int(input("Numero di pollici: "))

#Convertire in cm
cm = (feet*in_ft + inches)*cm_in

#Stampo il risultato
print("La tua altezza in centimetri è ", cm)