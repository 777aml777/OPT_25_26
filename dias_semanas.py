# Define una tupla con los 7 dias de la semana.
dias_semana = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")

# Muestra el primer y el último día de la semana.
print()
print("El primer dia de la semana es ", dias_semana[0])
print("El último dia de la semana es ", dias_semana[-1])

# Muestro todos los días de la semana.
print()
print("Los días de la semana son:")
for dia in dias_semana:
    print(dia)

# Encuentro en qué posición se encuentra el día Miércoles en la tupla.
print()
print("La posición de Miercoles en la tupla es:", dias_semana.index("Miércoles"))
