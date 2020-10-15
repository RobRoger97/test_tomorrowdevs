#Singoli pesi
widget_weighs = 75
gizmo_weighs = 112

#Chiedo all'utente il numero di widgets e di gizmos
widgets = int(input("Inserisci il numero di widgets: "))
gizmos = int(input("Inserisci il numero di gizomos: "))

#Calcolo del risultato
result1 = widget_weighs*widgets
result2 = gizmo_weighs*gizmos

#Stampa risultato
print("Dal numero datoci dall'utente, il peso totale dei widgets è ", result1, "grammi \
e il peso totale dei gizmos è ", result2, "grammi")
