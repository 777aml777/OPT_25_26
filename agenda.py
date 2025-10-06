"""
Vamos a crear una agenda. Para ello seguimos los siguientes pasos:
Creamos un diccionario vacío.
Luego introducimos 3 contactos.
Muestra la agenda completa usando un bucle.
Y por último creamos un buscador de contactos.
"""

# Creamos un diccionario vacio.
agenda = {}

# Introducimos 3 contactos.
print("Vamos a introducir 3 contactos para una agenda: ")
nombre1 = input("Introduce el nombre del primer contacto: ")
telf1 = int(input("Introduzca el telefono del primer contacto: "))
nombre2 = input("Introduce el nombre del segundo contacto: ")
telf2 = int(input("Introduzca el telefono del segundo contacto: "))
nombre3 = input("Introduce el nombre del tercer contacto: ")
telf3 = int(input("Introduzca el telefono del tercer contacto: "))

# Añadimos los contactos al diccionario agenda.
agenda[nombre1] = telf1
agenda[nombre2] = telf2
agenda[nombre3] = telf3

# Muestra la agenda completa usando un bucle.
print()
print("Los nombres y telefonos de los contactos son: ")
for clave, valor in agenda.items():
    print(clave, ":", valor)

# Creamos un buscador de contacto.
print()
print("Buscador de contactos.")
nombre = input("Introduzca el nombre del contacto deseado: ")
print("Telefono del contacto: ", agenda.get(nombre, "contacto no encontrado"))

