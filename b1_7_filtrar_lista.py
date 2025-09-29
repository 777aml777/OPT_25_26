"""
El script pide un numero al usuario y genera la tabla de
multiplicar de ese numero
"""

# Indico el nombre del script
print("Tabla de multiplicar")
# Pido al usuario que introduzca el numero
numero = int(input("Introduzca un número entero: "))

for i in range(1, 11): # Con el bucle for recorro los numeros del 1 al 10.
    resultado = numero * i # Guardo el resultado de la multiplicación en la variable resultado.
    print(f"{numero} X {i} = {resultado}") # Muestro por pantalla el resultado.
    i = i + 1 # Paso al siguiente número.