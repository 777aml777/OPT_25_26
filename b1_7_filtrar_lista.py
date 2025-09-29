"""
El programa recorre una lista de nombres y solo va a imprimir
los nombres que no empiezan por A.
"""

# Creo la lista con 9 nombres
nombres = ["Carlos", "Alvaro", "Maria", "Eva", "Ramon", "Luisa"]

for nombre in nombres: # Recorremos la lista con un bucle for
    if nombre[0] == "A" or nombre[0] == "a": # Uso un condicional
        continue                             # Uso continue para saltar los nombres que empiecen por A o por a
    print(nombre)                            # Imprimo los nombres que no empiecen por A o por a.