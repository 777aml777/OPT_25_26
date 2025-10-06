usuario_correcto = "admin"
contrasena_correcta = "1234"

usuario = input("Introduzca el nombre del usuario: ")
contrasena = input("Introduzca su contraseña: ")

print ()
if (usuario == usuario_correcto) and (contrasena == contrasena_correcta):
    print ("Acceso concedido")
else:
    print("Acceso denegado")