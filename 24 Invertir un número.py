# Solicitar un número entero al usuario
numero = int(input("Introduce un número entero: "))

# Convertir el número a cadena, invertirlo y luego convertirlo de nuevo a entero
numero_invertido = int(str(numero)[::-1])

# Mostrar el número invertido
print("Número invertido:", numero_invertido)
