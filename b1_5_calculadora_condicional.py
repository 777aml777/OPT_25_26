print ("Calculadora simple con dos números.")
num1 = int(input ("Introduzca el primer número entero: "))
num2 = int(input ("Introduzca el segundo número entero: "))

print ("Introduzca la operación a realizar: ")
print ("1   Suma")
print("2   Resta")
print("3   Multiplicación")
print("4   División")
operacion = int(input())

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 // num2
modulo = num1 % num2

if (operacion == 1):
    print (f"El resultado de sumar {num1} mas {num2} es {suma}")
elif (operacion == 2):
    print (f"El resultado de restar {num1} menos {num2} es {resta}")
elif (operacion == 3):
    print (f"El resultado de multiplicar {num1} por {num2} es {multiplicacion}")
elif (operacion == 4):
    print (f"El cociente de la división de {num1} entre {num2} es {division}")
    print (f"El resto de la division de {num1} entre {num2} es {modulo}")
else:
    print ("La opción introducida no es correcta.")