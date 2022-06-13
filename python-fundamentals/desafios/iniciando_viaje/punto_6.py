'''
    La siguiente matriz (o lista con listas anidadas) debe cumplir que el cuarto elemento
    de cada fila se la suma de los tres primeros elementos de la fila respectiva. Si nota
    las sumas que se encuentran están erróneas, debe modificarlas dando 2 soluciones,
    una con append y otra con slicing.
'''

matriz = [
    [2, 4, 3, 6],
    [8, 3, 4, 5],
    [7, 1, 3, 10],
    [9, 2, 1, 4]
]

# Using append()

matriz[0].pop()
matriz[0].append(sum(matriz[0]))
matriz[1].pop()
matriz[1].append(sum(matriz[1]))
matriz[2].pop()
matriz[2].append(sum(matriz[2]))
matriz[3].pop()
matriz[3].append(sum(matriz[3]))
print(matriz)

# Using slicing

matriz[0][-1:] = [sum(matriz[0][0:3])]
matriz[1][-1:] = [sum(matriz[1][0:3])]
matriz[2][-1:] = [sum(matriz[2][0:3])]
matriz[3][-1:] = [sum(matriz[3][0:3])]
print(matriz)