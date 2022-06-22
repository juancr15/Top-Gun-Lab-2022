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

    path = rf"{os.getcwd()}/python-fundamentals/desafios/mentalidad_colmena/required_data.txt"
    file = open(path, "r+")
    # text = file.read()
    lines = file.readlines()

    file.writelines("\n\nUser data:")
    # print(lines)
    for line in lines:
        if line.find("|") != -1:

            print("\n------ " + line.split("|")[1].strip() + " ------\n")
        
        if line.find(":") != -1:
            if line.find("•") != -1:
                print("\n*** Family member", line.split(":")[0].strip(), " ***\n")
            else :
                set_info(line, path)
                break
        
        
        # print(lines.index(line))
        # print(line)

    file.close()

def set_info(field, path):
    user_info = ask_user(field)
    with open(path, "r+") as file:
        file.writelines(user_info)
    file.close()

def ask_user(field) :
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