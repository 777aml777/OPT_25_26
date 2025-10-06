# Genero una lista con los números del 1 al 10 elevados al
# cuadrado usando comprensión de listas.
cuadrados = [n ** 2 for n in range(1, 11)]
print(cuadrados)

# Genero otra lista con los números pares entre 1 y 20 usando
# comprensión de listas.
pares = [n for n in range(1, 21) if n % 2 == 0]
print(pares)

# Crea un diccionario que relacione cada número del 1 al 5
# con su cubo usando comprensión de diccionarios.
cubos = {n: n ** 3 for n in range(1, 6)}
print(cubos)