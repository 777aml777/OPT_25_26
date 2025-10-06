archivo = "datos.txt"
modo = "r"
encoding = "utf-8"

try:
    with open(archivo, modo, encoding=encoding) as f:
        for linea in f:
            print(linea.strip())
except FileNotFoundError:
    print("No se encontró el archivo.")