def registrar_usuario(nombre,edad,ciudad="Madrid"):
    """
    Función que muestra por pantalla el usuario, la edad y la ciudad donde vive.
    """
    print(f"Usuario: {nombre}, Edad: {edad}, Ciudad: {ciudad}")

# Invocamos la función con todos los argumentos posicionales
registrar_usuario("Adrián", 20, "Huelva")

# Invocamos la función con el último argumento omitido
registrar_usuario("Pepe", 53)

# Invocamos la función con los argumentos nombrados en distinto orden
registrar_usuario(ciudad="Barcelona", nombre="Ana", edad=18)
