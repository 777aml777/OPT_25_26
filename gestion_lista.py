"""
En este programa definimos una lista vacía.
Después pedimos al usuario 5 productos y los añadimos a la lista.
Después se muestra la lista completa.
Después pedimos al usuario un producto a eliminar de la lista y lo eliminamos.
Luego se muestra la lista ordenada alfabéticamente.
"""

# Defino una lista vacía.
compras = []

# Pido al usuario 5 productos y los añada a la lista.
print("Vamos a crear una lista con 5 productos.")
producto1 = input("Introduzca el primer producto: ")
producto2 = input("Introduzca el segundo producto: ")
producto3 = input("Introduzca el tercer producto: ")
producto4 = input("Introduzca el cuarto producto: ")
producto5 = input("Introduzca el quinto producto: ")

compras.append(producto1)
compras.append(producto2)
compras.append(producto3)
compras.append(producto4)
compras.append(producto5)

# Muestro la lista completa.
print()
print("Esta es la lista creada.")
print(compras)

# Pido al usuario un producto a eliminar, lo elimino y muestro la nueva lista.
print()
producto_eliminar = input("Introduzca un producto de la lista a eliminar: ")
compras.remove(producto_eliminar)
print()
print("Esta es la nueva lista.")
print(compras)

# Muestro la lista ordenada alfabéticamente.
print()
print("Muestro la lista ordenada alfabéticamente.")
compras.sort()
print(compras)


