#Riempi una lista di 10 numeri casuali (utilizza un ciclo for) e stampa solo i numeri pari
#creazione della lista con 10 numeri casuali
import random
list=[ ]
for x in range(10):
    list.append(random.randrange(0,19))
print (list)
#Stampa numeri pari
for x in list:
    controllo=int(x/2)
    if (controllo*2) == x:
        print(x)
