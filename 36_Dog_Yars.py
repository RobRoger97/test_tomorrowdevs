#Dati
due_anni = 10.5

#Chiede all'utente
anni_umani = float(input("Inserire gli anni umani: "))

#Conversione in anni canini:
if anni_umani<=2 and anni_umani>=0:
    anni_canini= anni_umani*due_anni
    print("L'età canina è ",anni_canini)
elif anni_umani>2:
    anni_canini= 2*due_anni+((anni_umani-2)*4)
    print("L'età canina è ",anni_canini)
else:
    print("Errore: il numero è negativo")