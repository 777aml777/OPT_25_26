# Defino la variable global.
contador = 0

# Utilizo en las funciones globales el comando global,
# Que permite modificar una variable global dentro de la función.
def incrementar():
    # Función que incrementa en uno el valor de la variable contador.
    global contador
    contador = contador + 1

def decrementar():
    # Función que disminuye en uno el valor de la variable contador.
    global contador
    contador = contador - 1

def mostrar_contador():
    # Función que imprime el valor actual de la variable contador.
    global contador
    print(contador)

# Ejecuto la funcion incrementar() dos veces. La funcion decrementar() una vez.
incrementar()
incrementar()
decrementar()

# Y ejecuto la funcion mostrar_contador()
mostrar_contador()

