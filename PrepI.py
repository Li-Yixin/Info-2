#Dichiara due liste. Una con nomi di animali e l’altra con numeri. 
#Aggiungi tutti gli elementi della seconda lista alla prima.
#Stampa soltanto i numeri maggiori di 5
nameanimali=["Cane","Gatto","Leone","Tigre","Lupo"]
listanum=[1,2,3,4,7]
for x in nameanimali:
    for y in listanum:
        if y > 5:
            print(x,y)