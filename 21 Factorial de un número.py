# Solicitar al usuario el número
n = int(input("Ingresa un número para calcular su factorial: "))

# Función para calcular el factorial
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

# Calcular y mostrar el resultado
resultado = factorial(n)
print(f"El factorial de {n} es: {resultado}")
