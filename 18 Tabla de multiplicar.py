# Solicitar un número al usuario
numero = int(input("Introduce un número: "))

# Mostrar la tabla de multiplicar del número
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
