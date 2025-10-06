# Creo el diccionario persona con las claves nombre, edad y ciudad.
persona = {"nombre": "Adrian", "edad": 20, "ciudad": "Huelva"}

# Muestro el valor de cada clave.
print(persona["nombre"], persona["edad"], persona["ciudad"])

# Añado una nueva clave profesion con su valor.
persona["profesion"] = "Informático"

# Elimino la clave ciudad.
del persona["ciudad"]

# Recorro el diccionario mostrando clave y valor en cada línea.
for clave, valor in persona.items():
    print(clave, ":", valor)
