'''
    Realizar un programa que permita ingresar grados Fahrenheit y muestre por pantalla
    el dato en grados centígrados o pasar de grados centígrados a grados Fahrenheit
    (puede realizar cualquiera de los dos programas).
'''

fahrenheit = float(input("Fahrenheit: "))
celsius = (fahrenheit-32) * 5/9 # Formula to convert Fahrenheit to Celsius
print(f"{fahrenheit} °F = {celsius} °C")