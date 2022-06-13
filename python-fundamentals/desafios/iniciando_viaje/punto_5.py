'''
    A partir del ejercicio anterior, crea un programa para calcular la nota final de un
    estudiante universitario. Para ello, el usuario debe ingresar 3 notas y el valor
    porcentual de cada nota, realiza y devuelve la media por pantalla.
'''

grade_1 = float(input("Grade 1: "))
grade_1_weight = float(input("Grade 1 weight: ")) / 100

grade_2 = float(input("Grade 2: "))
grade_2_weight = float(input("Grade 2 weight: ")) / 100

grade_3 = float(input("Grade 3: "))
grade_3_weight = float(input("Grade 3 weight: ")) / 100

mean_grade = grade_1*grade_1_weight + grade_2*grade_2_weight + grade_3*grade_3_weight

print(f"\nMean grade: {mean_grade}")