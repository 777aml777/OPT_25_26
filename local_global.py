# Definimos la variable global
curso = "Python"

def mostrar_curso():
    """
    Esta función va a mostrar el valor de la variable global
    """
    print(curso)

def cambiar_curso():
    """
    Esta función va a mostrar el valor de una variable local
    """
    curso = "javascript" # Definimos la variable local
    print(curso)

# Ejecutamos las funciones
mostrar_curso()
cambiar_curso()

