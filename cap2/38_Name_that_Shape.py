#Chiedere il numero di lati all'utente
n_lati = int(input("Inserire il numero di lati: "))

#Determinare il nome dal numero di lati
nome = ""
if n_lati==3:
    nome = "triangolo"
elif n_lati==4:
    nome = "quadrato"
elif n_lati==5:
    nome = "pentagono"
elif n_lati==6:
    nome = "esagono"
elif n_lati==7:
    nome = "eptagono"
elif n_lati==8:
    nome = "ottagono"
elif n_lati==9:
    nome = "nonagono"
elif n_lati==10:
    nome = "decagono"

#Stampa i risultati
if nome=="":
    print("Questo numero non rientra nel range di questo programma")
else:
    print("Questo è un ",nome)