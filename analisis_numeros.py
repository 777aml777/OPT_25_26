# Genera una lista de 20 números enteros mediante comprensión
numeros = [n for n in range(1, 21)]

# Genera una lista con los cuadrados de los números de la
# lista numeros.
cuadrados = [n ** 2 for n in numeros]

# Genera una lista con los pares de los números de la
# lista numeros.
pares = [n for n in numeros if n % 2 == 0]

# Genera una lista con los números mayores de 10
# de la lista números.
mayor_diez = [n for n in numeros if n > 10]

# Genera un diccionario que relaciona cada número de la lista
# números con su doble.
dobles = {n: n * 2 for n in numeros}

# Imprimo todos los resultados.
print()
print("Lista de 20 numeros enteros.")
print(numeros)

print()
print("Lista de los cuadrados de esos números.")
print(cuadrados)

print()
print("Lista de los números pares.")
print(pares)

print()
print("Lista de los números mayores que 10.")
print(mayor_diez)

print()
print("Diccionario de los números y su valor doble.")
print(dobles)
