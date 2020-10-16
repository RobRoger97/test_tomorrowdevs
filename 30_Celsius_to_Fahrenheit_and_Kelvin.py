#Chiedi all'utente la temperatura in Celsius
T_Celsius = float(input("Inserire il valore della temperatura in gradi Celsius: "))

#Trasformazione in Fahrenheit
T_Fahrenheit = (T_Celsius*(9/5))+32
print("Il risultato della temperatura in Fahrenheit è: ",T_Fahrenheit, "°F")

#Trasformazione in Kelvin
T_Kelvine = T_Celsius+273.15
print("Il risultato della temperatura in Kelvin è: ", T_Kelvine, "K")