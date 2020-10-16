#Chiedere all'utente
mese = input("Inserire il nome di un mese: ")

#Verificare
giorni = 31
if mese=="Aprile" or mese=="Giugno" or \
   mese=="Settembre" or mese=="Novembre":
   giorni = 30
elif mese=="Febbraio":
    giorni = "28 o 29"

#Stampa risultato
print(mese, "ha", giorni, "giorni")