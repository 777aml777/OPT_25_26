def sumar(a, b):
    """
    Devuelve el producto de dos números.
    """
    print(f"{a} + {b} = {a + b}")

def saludo_personal(nombre, saludo="Hola"):
    """
    Muestra un saludo personalizado
    """
    print(f"{saludo} {nombre}, Bienvenido")

sumar(2, 3) # Invoco a la función sumar.
saludo_personal("Pepe") # Invoco la función saludo_personal con un solo argumento.
saludo_personal("Juan", "¡Qué pasa!") # Invoco la función con dos argumentos.
saludo_personal(saludo="¡Qué tal!", nombre="Juan") # Invoco la función con dos argumentos nombrados.