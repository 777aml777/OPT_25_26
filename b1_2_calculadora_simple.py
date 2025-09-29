print ("Calculadora simple con dos números.")
num1 = int(input ("Introduzca el primer número entero: "))
num2 = int(input ("Introduzca el segundo número entero: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 // num2
modulo = num1 % num2
potencia = num1 ** num2

print ()
print (f"El resultado de sumar {num1} mas {num2} es {suma}")
print (f"El resultado de restar {num1} menos {num2} es {resta}")
print (f"El resultado de multiplicar {num1} por {num2} es {multiplicacion}")
print (f"El cociente de la división de {num1} entre {num2} es {division}")
print (f"El resto de la division de {num1} entre {num2} es {modulo}")
print (f"El resultado de {num1} elevado a {num2} es {potencia}")