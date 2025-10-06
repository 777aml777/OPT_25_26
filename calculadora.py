def sumar(a, b):
    """
    Función que devuelve la suma de dos números, con 2 decimales máximo
    """
    return round(a + b, 2)

def restar(a, b):
    """
    Función que devuelve la resta de dos números, con 2 decimales máximo
    """
    return round(a - b, 2)

def multiplicar(a, b):
    """
    Función que devuelve el producto de dos números, con 2 decimales máximo
    """
    return round(a * b, 2)

def dividir(a, b):
    """
    Función que devuelve el cociente de dos números, con 2 decimales máximo
    """
    return round(a / b, 2)

# Pedimos al usuario que introduzca los dos argumentos que necesito para los cálculos
print("Vamos a hacer la suma, resta, multiplicación y división de dos números.")
num1 = float(input("Introduzca el valor del primer número: "))
num2 = float(input("Introduzca el valor del segundo número: "))

# Me muestra la suma, resta, multiplicación y división de los dos números.
print()
print("La suma de los dos números es:  ", sumar(num1,num2))
print("La resta de los dos números es:  ", restar(num1,num2))
print("La multiplicación de los dos números es:  ", multiplicar(num1,num2))
print("La división de los dos números es:  ", dividir(num1,num2))