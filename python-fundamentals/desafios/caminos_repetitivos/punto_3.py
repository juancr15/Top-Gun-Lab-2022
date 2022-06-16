"""
    Implementar una aplicación que dada una altura en metros de un edificio del que se
    va a lanzar una esfera, vaya mostrando la distancia recorrida segundo
    a segundo hasta tocar el suelo.

    d = v * t ± (1/2) * g * t^2, donde:

    • d es la distancia recorrida.
    • g es la aceleración originada por la gravedad es decir 9.8 𝑚/s^2.
    • t es el tiempo transcurrido.
"""

def main():
    height = positive_float("Ingrese la altura del edificio (metros): ")
    g = 9.8 # m/s^2
    t = 0 # s
    distance = 0 # m

    while height > distance:
        # Calculating the distance in t seconds. v=0 m/s because the sphere is falling.
        distance = (1/2) * g * t**2 # m
        if distance > height:
            print(f"En el segundo {t} la esfera ya tocó el suelo.")
        else :
            print(f"La distancia recorrida en {t} segundos es {distance} metros.")
        
        # Increasing the time by one second.
        t += 1

def positive_float(string) :
    """Returns a positive float value after the respective validation.

    Parameters:
    string (string): The string that will be shown to the user in the input.
    user_input : The user input. 

    Returns:
    float: The validated float value.

   """
    user_input = input(string)

    # Validating if the user input is a number
    while not user_input.isnumeric() :
        user_input = input("El valor ingresado no corresponde a un valor númerico. Ingreselo nuevamente.\n" + string)
    user_input = float(user_input)
    return user_input

main()