"""
    Ace quiere ser voluntario para viajar a K-Pax, para ello la 
    Agencia Espacial Canadiense requiere que llene un formulario 
    que ayude a obtener más información de él y su familia. 
    Tu debes ayudar a Ace creando un programa para completar la 
    información solicitada sin sobrescribir el archivo. Ten presente 
    que los datos con * son los más importantes, si uno de esos 
    campos no se llena, no podrá ser admitido, en caso de que el 
    dato solicitado no sea importante, el programa deberá poner “unknown”.
"""
import os

def main():

    text = ''

    # Set the path of the file
    path = rf"{os.getcwd()}/python-fundamentals/desafios/mentalidad_colmena/required_data.txt"
    # Open the file
    file = open(path, "r+")
    # Read the file
    lines = file.readlines()
    
    file.writelines("\n\n/////// New User \n")

    # Go through the lines and set the info
    for line in lines:
        if line.find("|") != -1:
            text = "\n------ " + line.split("|")[1].strip() + " ------\n"
            file.writelines(text)
            print(text)
        
        if line.find(":") != -1:
            if line.find("â€¢") != -1:
                text = "\n*** Family member " + line.split(":")[0].strip() + " ***\n"
                file.writelines(text)
                print(text)
            else :
                set_info(file, line)
    file.close()

def set_info(file, field):
    """ Sets the info in the file.

    Parameters:
    file (file): The file where the info will be written.
    field (string): The field to be written.

    Returns:
    None: The info is written in the file.
    """
    user_info = ask_user(field)
    file.writelines(f"{field.rstrip()} {user_info}\n")

def ask_user(field) :
    """ Asks the user for the info.
    
    Parameters:
    field (string): The field to be asked.

    Returns:
    string: The info of the user.
    """
    while True:
        user_input = input(field.strip() + " ")
        if user_input == "" :
            if field.find("*") != -1:
                print("This field is required. Try again.")
            else :
                user_input = "unknown"
                break
        else:
            break
    return user_input

main()