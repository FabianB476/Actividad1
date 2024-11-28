# Función para verificar si un número es primo
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Encontrar y mostrar todos los números primos entre 1 y 50
primos = [num for num in range(1, 51) if es_primo(num)]

# Imprimir la lista de números primos
print("Los números primos entre 1 y 50 son:", ", ".join(map(str, primos)))
