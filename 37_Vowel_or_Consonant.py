#Chiedi all'utente
lettera = input("Inserire una lettera: ")

#Verifica
if lettera=="a" or lettera=="e" or \
   lettera=="i" or lettera=="o" or \
   lettera=="u" :
   print("Questa è una vocale")
elif lettera=="y":
    print("Questa a volte è una consonante e a volte è una vocale")
else:
    print("Questa è una consonante")