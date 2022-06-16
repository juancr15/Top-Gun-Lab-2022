"""
    Dadas dos listas, se debe crear un programa que genere una tercera
    lista con los elementos que se repiten en las dos anteriores listas sin
    repetirse ningún elemento en la nueva lista.
        list_1 = ['h', 'e', 'l', 'l', 'o', ' ', 't', 'e', 'a', 'm']
        list_2 = ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
"""

list_1 = ['h', 'e', 'l', 'l', 'o', ' ', 't', 'e', 'a', 'm']
list_2 = ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']

# Using set interaction to ger the repeted elements
list_3 = list(set(list_1).intersection(set(list_2)))

print("Lista 3: ", list_3)

