"""
    Debe crear un programa que dada una generación (mayor o igual a
    cero):
    - Le indique al usuario el número total de personas de la familia (de
      todas las generaciones hasta la generación dada).
    - Muestre el número de personas de cada generación mientras
      hace el cálculo.
"""

def main() :
    generation = greater_equal_zero_int("Ingrese una generación: ")
    family_members = 0
    
    for i in range(generation + 1) :
        # Each generation has twice the members of the previous generation
        print(f"La familia tiene {2**i} personas en la generacion {i}.")
        family_members += 2**i
    
    print(f"\nLa familia tiene {family_members} integrantes en total.")
            

def greater_equal_zero_int(string) :
    """Returns a greater than or equal to zero int.

    Parameters:
    string (string): The string that will be shown to the user in the input.
    user_input : The user input. 

    Returns:
    int: The validated int value.

   """
    user_input = input(string)

    # Validating if the user input is a number greater or equal to zero
    while not user_input.isnumeric() :
        user_input = input("El valor ingresado no corresponde a un número mayor o igual a cero. Ingreselo nuevamente.\n" + string)
    user_input = int(user_input)

    return user_input

main()