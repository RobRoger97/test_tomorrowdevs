#Importare modulo del tempo
import time

#Quando la tupla temporale non è presente, viene utilizzata l'ora corrente restituita da localtime ().
t = time.asctime()

#Stampa risultato
print("L'ora corrente è: ",t)