'''
    Realizar un programa que le solicite a 3 usuarios ingresar por teclado información personal,
    la información de cada usuario se debe guardar en una estructura de colección inmutable, 
    luego mostrar por pantalla la información de los usuarios agrupada en una estructura de colección mutable.
    
    La información para solicitar es:
        a. Nombres y apellidos.
        b. Ocupación.
        c. Edad.
        d. Ciudad.
        e. Número de contacto.
        f. Correo electrónico.
'''

users = []
print("---------- 1st User ----------")
nameUsr1 = input("Name: ")
occupationUsr1 = input("Occupation: ")
ageUsr1 = int(input("Age: "))
cityUsr1 = input("City: ")
phoneUsr1 = int(input("Phone number: "))
emailUsr1 = input("Email: ")

infoUsr1 = (nameUsr1, occupationUsr1, ageUsr1, cityUsr1, phoneUsr1, emailUsr1)
users.append(infoUsr1)

print("\n---------- 2nd User ----------")
nameUsr2 = input("Name: ")
occupationUsr2 = input("Occupation: ")
ageUsr2 = int(input("Age: "))
cityUsr2 = input("City: ")
phoneUsr2 = int(input("Phone number: "))
emailUsr2 = input("Email: ")

infoUsr2 = (nameUsr2, occupationUsr2, ageUsr2, cityUsr2, phoneUsr2, emailUsr2)
users.append(infoUsr2)

print("\n---------- 3rd User ----------")
nameUsr3 = input("Name: ")
occupationUsr3 = input("Occupation: ")
ageUsr3 = int(input("Age: "))
cityUsr3 = input("City: ")
phoneUsr3 = int(input("Phone number: "))
emailUsr3 = input("Email: ")

infoUsr3 = (nameUsr3, occupationUsr3, ageUsr3, cityUsr3, phoneUsr3, emailUsr3)
users.append(infoUsr3)

print("\n", users)