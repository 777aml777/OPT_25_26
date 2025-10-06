"""
El programa calcula la media de los 3 trimestres.
"""

print("Calculo de nota media del curso: ")

nota1 = float(input("Introduzca la nota del primer trimestre: "))
nota2 = float(input("Introduzca la nota del segundo trimestre: "))
nota3 = float(input("Introduzca la nota del tercer trimestre: "))

media_curso = round((nota1 + nota2 + nota3) / 3, 2)

print()
print(f"La nota media del curso es de {media_curso}.")