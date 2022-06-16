def main() :
    """
    Main function.
    - Calculates the speed of a vehicle 
      according to the distance and time that he user provides.
    - Validates the kind of penalty according to the vehicle's speed.
    
    Parameters:
    initial_distance (float): The initial distance of the vehicle.
    final_distance (float): The final distance of the vehicle.
    time (float): The time that the vehicle takes to travel the distance.
    speed (float): The speed of the vehicle.
    penalty (boolean): True if the vehicle has a penalty, False otherwise.
    breathalyzer (float): The breathalyzer value of the driver.
    """
    initial_distance = positive_float("Ingrese la distancia capturada por la primer haz de luz (metros): ")
    final_distance = positive_float("Ingrese la distancia capturada por la segunda haz de luz (metros): ")
    time = positive_float("Ingrese el tiempo entre las capturas (segundos): ")

    speed = ((final_distance - initial_distance) / 1000) / (time/3600) # km/h
    print(f"\nLa velocidad del vehículo es {speed:.2f} km/s.\n")

    penalty = False

    if speed >= 1 and speed <= 20 :
        print("Llamado de atención por baja velocidad.")
    elif speed >= 21 and speed <= 60 :
        print("Normal.")
    elif speed >= 61 and speed <= 80 :
        print("Llamado de atención por alta velocidad.")
    elif speed >= 81 and speed <= 120 :
        print("Multa tipo I.")
        penalty = True
    else :
        print("Multa tipo II e inmovilización del vehículo.")
        penalty = True

    if penalty :
        print("\n\tDebido a que cuenta con una multa por velocidad, debe realizarse la prueba de alcoholemia.\n")

        breathalyzer = positive_float("Ingrese resultado de la prueba de alcoholemia (mg de etanol/100 ml de sangre): ")
        if breathalyzer >= 20 and breathalyzer < 40 :
            print("Suspención licencia de conducción entre 6 y 12 meses.")
        elif breathalyzer >= 40 and breathalyzer < 100 :
            print("Suspención licencia de conducción entre 1 y 3 años.")
        elif breathalyzer >= 100 and breathalyzer < 150 :
            print("\n\t\tSuspención licencia de conducción entre 3 y 5 años, \n\
                y la obligación de realizar curso de sensibilización, \n\
                conocimientos y consecuencias de la alcoholemia y drogadicción \n\
                en centros de rehabilitación debidamente autorizados, por un mínimo de cuarenta (40) horas.")
        else :
            print("\n\t\tSuspención licencia de conducción entre 5 y 10 años, \n\
                y la obligación de realizar curso de sensibilización, conocimientos \n\
                y consecuencias de la alcoholemia y drogadicción en centros \n\
                de rehabilitación debidamente autorizados, por un mínimo de ochenta (80) horas.")

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

# print(main.__doc__)
main()
