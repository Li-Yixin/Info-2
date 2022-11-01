# Loop: for viene utilizzato per l'iterazione su una sequenza
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#Passare attraverso una stringa
for x in "banana":
  print(x)

#rottura:stampa fino a 
    #dopo
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
  if x == "banana":
    break
    #prima
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

# Non stampare 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#range() il numero non compreso
for x in range(6):
  print(x)

#numero compreso 
for x in range(2, 6):
  print(x)

#Incrementa la sequenza di 3 (il valore predefinito è 1):
for x in range(2, 30, 3): # primi 2 numeri per intervalli il terza il salto di 
  print(x)

#Stampa numeri da 0 a 5 e un messaggio quando il ciclo è terminato:
for x in range(6):
  print(x)
else:
  print("Finally finished!")

#Il messagio no viene stampato se il ciclo viene rotto da break
  for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!") #If the loop breaks, the else block is not executed.

#Loop nidificati: Il "ciclo interno" verrà eseguito una volta per ogni iterazione del "ciclo esterno"
    #Stampa ogni aggettivo per ogni frutto
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)

#dichiarazione di passaggio