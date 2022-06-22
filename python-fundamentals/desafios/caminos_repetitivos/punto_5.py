"""
    Se debe crear un programa que dada una longitud en cuadros
    (mayor a cero), genere un tablero.

    Ejemplo: 3
        ***
        ***
        ***
     ***   ***
     ***   ***
     ***   ***
        ***
        ***
        ***
"""

import math

def main() :
    length = greater_zero_int("Ingrese la longitud en cuadros: ")
    string = ""

    for i in range(length) :
        # Validating if the row is even or odd
        if i % 2 == 0 :
            string += rows(math.floor(length/2), "even")
        else :
            string += rows(math.ceil(length/2), "odd")
    print(string)

def greater_zero_int(string) :
    """Returns a greater than zero int.

    Parameters:
    string (string): The string that will be shown to the user in the input.
    user_input : The user input. 

    Returns:
    int: The validated int value.
   """

    flag = True
    while flag :
        user_input = input(string)
        # Validating if the user input is a number
        if not user_input.isnumeric() :
            print("El valor ingresado no corresponde a un valor númerico. Ingreselo nuevamente.\n")
        # Validating if the user input is a number greater than zero
        elif int(user_input) < 1 :
            print("El valor ingresado no corresponde a un valor entero mayor a cero. Ingreselo nuevamente.\n")
        else :
            flag = False
    return int(user_input)

def rows(length, kind) :
    """ Returns a string with the drawn row according its kind (even or odd) and size.

    Parameters:
    length (int): The length of the board
    kind (string): even or odd

    Returns:
    string: The drawn row.
    """
    string = ""

    for _ in range(3) :
        for _ in range(length) :
            if kind == "odd" :
                string += "***   "
            else :
                string += "   ***"
        string += "\n"
    
    return string


main()