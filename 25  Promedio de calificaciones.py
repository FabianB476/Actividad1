# Inicializar variables
calificaciones = []
calificacion = 0

# Solicitar calificaciones al usuario hasta que ingrese -1
while calificacion != -1:
    calificacion = float(input("Ingresa una calificación (-1 para terminar): "))
    
    if calificacion != -1:
        calificaciones.append(calificacion)

# Calcular el promedio
if len(calificaciones) > 0:
    promedio = sum(calificaciones) / len(calificaciones)
    print(f"Promedio: {promedio:.2f}")
else:
    print("No se ingresaron calificaciones.")
