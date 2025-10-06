def area_rectangulo(base, altura):
    """
    Función que devuelve el área de un rectángulo
    """
    return base * altura

def perimetro_rectangulo(base, altura):
    """
    Función que devuelve el perímetro de un rectángulo
    """
    return (2 * base) + (2 * altura)

# Pedimos al usuario que introduzca los dos argumentos que necesito para los cálculos
print("Vamos a calcular el área y el perímetro de un rectángulo.")
valor1 = float(input("Introduzca el valor de la base: "))
valor2 = float(input("Introduzca el valor de la altura: "))

# Me muestra el área y el perímetro del rectángulo
print()
print("El área de un rectángulo es ", area_rectangulo(valor1,valor2) )
print("El perimetro de un rectángulo es ", perimetro_rectangulo(valor1, valor2))