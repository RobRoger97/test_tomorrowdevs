#Chiedo all'utente altezza e peso
h = float(input("Inserire l'altezza in metri: "))
w = float(input("Inserire il peso in chilogrammi: "))

#Calcolo del BMI
bmi = w/(h**2)

#Stampa risultato
print("Il BMI è uguale a: ", round(bmi,1))