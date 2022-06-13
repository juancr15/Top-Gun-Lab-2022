'''
    Debes utilizar todo lo que sabes sobre los strings, las listas y sus métodos o funciones
    para transformar el siguiente texto:

        thor lanzó su martillo#flash ha fallado por un pie! -gritó Loki Laufeyson#dos
        pies -le corrigió Hulk#flash menea la cabeza como disgustado… -agrega el
        comentarista

    En:
        Thor lanzó su martillo…
        - ¡Flash ha fallado por un pie! -gritó Loki Laufeyson.
        - Dos pies le corrigió Hulk.
        - Flash menea la cabeza como disgustado… -agrega el comentarista.
'''

og_string = "thor lanzó su martillo#flash ha fallado por un pie! -gritó Loki Laufeyson#dos pies -le corrigió Hulk#flash menea la cabeza como disgustado… -agrega el comentarista"

split_string = og_string.split("#")

split_string[0] = split_string[0].capitalize() + ".."
split_string[1] = split_string[1][0].upper() + split_string[1][1:]
split_string[2] = split_string[2].split("-")
split_string[2] = split_string[2][0].capitalize() + split_string[2][1]
split_string[3] = split_string[3].capitalize() + "."


new_string = '.\n - '.join(split_string)

print(new_string)