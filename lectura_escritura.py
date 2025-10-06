# Creo un archivo llamado mi_archivo.txt y le añado 3 frases (una por línea).
archivo = "mi_archivo.txt"
modo = "w"
encoding = "utf-8"

with open(archivo, modo, encoding=encoding) as f:
    f.write("Esta es la primera línea\n")
    f.write("Esta es la segunda línea\n")
    f.write("Esta es la tercera línea\n")

# Abro el archivo en modo lectura y muestro todo el contenido
archivo = "mi_archivo.txt"
modo = "r"
encoding = "utf-8"

with open(archivo, modo, encoding=encoding) as f:
    contenido = f.read()
    print(contenido)

# Abro el archivo en modo lectura y muestro la primera linea
archivo = "mi_archivo.txt"
modo = "r"
encoding = "utf-8"

with open(archivo, modo, encoding=encoding) as f:
    primera_linea = f.readline()
    print(primera_linea)

# Abro el archivo el modo lectura y muestra todas las lineas en una lista.
archivo = "mi_archivo.txt"
modo = "r"
encoding = "utf-8"

with open(archivo, modo, encoding=encoding) as f:
    todas_las_lineas = f.readlines()
    print(todas_las_lineas)

# Abro el archivo en modo anexar y agrego una nueva linea a lo existente.
archivo = "mi_archivo.txt"
modo = "a"
encoding = "utf-8"

with open(archivo, modo, encoding=encoding) as f:
    f.write("Nueva linea añadida\n")

# Abro el archivo en modo lectura y muestro el contenido final.
archivo = "mi_archivo.txt"
modo = "r"
encoding = "utf-8"

with open(archivo, modo, encoding=encoding) as f:
    contenido = f.read()
    print(contenido)
