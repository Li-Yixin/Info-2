# Uno dei 4 modi di Python utilizzati per archiviare i dati, gli altri 3 sono Tuple , Set e Dictionary
Lista_esempio = ["apple", "banana", "cherry"]
print(Lista_esempio)
#Le voci dell'elenco sono ordinate, modificabili e consentono valori duplicati.
Lista_valoriduplici = ["2", "1", "1"]
print(Lista_valoriduplici)
#Lunghezza elenco , quanti elementi ha in un elenco, utilizzare la len()
Lista_quanti_elementi = ["apple", "banana", "cherry"]
print(len(Lista_quanti_elementi))
#Gli elementi dell'elenco possono essere di qualsiasi tipo di dati
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list_misto = ["abc", 34, True, 40, "male"]
# tipo di dati di un elenco
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
# lista dentro lista con list() 
thislist = list(("apple", "strawberry", "banana", "cherry")) # note the double round-brackets
print(thislist)
# Per avere sottoliste
thislist = list((["apple"], "strawberry", "banana", "cherry")) # note the double round-brackets
print(thislist)